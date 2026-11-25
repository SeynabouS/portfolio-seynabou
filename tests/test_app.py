"""Regression checks for navigation, project filters and the official PDF."""

import hashlib
import unittest
from html.parser import HTMLParser
from pathlib import Path

from streamlit.testing.v1 import AppTest

ROOT = Path(__file__).resolve().parents[1]


class Document(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.ids, self.anchors, self.cards, self.text = [], [], [], []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.append(attrs["id"])
        if tag == "a" and attrs.get("href", "").startswith("#"):
            self.anchors.append(attrs["href"][1:])
        if "project-card" in attrs.get("class", "").split():
            self.cards.append(attrs["id"])

    def handle_data(self, data):
        self.text.append(data)


def rendered_document(app):
    return Document("\n".join(block.proto.body for block in app.get("html")))


class PortfolioTests(unittest.TestCase):
    def setUp(self):
        self.app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=20).run()
        self.assertEqual(len(self.app.exception), 0)

    def test_all_projects_and_section_links(self):
        doc = rendered_document(self.app)
        self.assertEqual(len(doc.cards), 6)
        self.assertEqual(len(doc.ids), len(set(doc.ids)))
        self.assertTrue(set(doc.anchors).issubset(set(doc.ids)))

    def test_project_filter_and_reset(self):
        cases = [
            ("Réseaux & SIG", {"projet-resilience", "projet-irise"}),
            ("Cybersécurité & IA", {"projet-juritech", "projet-llm", "projet-infrastructure"}),
            ("Développement", {"projet-crowdfunding"}),
        ]
        for category, expected in cases:
            with self.subTest(category=category):
                self.app.get("button_group")[0].set_value([category]).run()
                self.assertEqual(len(self.app.exception), 0)
                self.assertEqual(set(rendered_document(self.app).cards), expected)
                self.assertEqual(len(self.app.get("download_button")), 1)
        self.app.get("button_group")[0].set_value(["Tous les projets"]).run()
        self.assertEqual(len(rendered_document(self.app).cards), 6)
        self.app.get("button_group")[0].set_value([]).run()
        self.assertEqual(len(rendered_document(self.app).cards), 6)

    def test_official_cv_is_exact_original_and_downloadable(self):
        digest = hashlib.sha256((ROOT / "CV_Seynabou_Sougou.pdf").read_bytes()).hexdigest()
        self.assertEqual(digest, "75b4d9a0d1a9a88047fb5a7468d0cd6132daa4edde7bee4760a96b8eb0377f24")
        download = self.app.get("download_button")[0].proto
        self.assertTrue(download.url.endswith(".pdf"))
        self.assertFalse(download.disabled)
        self.assertTrue(download.ignore_rerun)
        self.assertTrue((ROOT / "assets/cv_preview.png").is_file())

    def test_excluded_topics_and_stale_claims_are_absent(self):
        content = " ".join(rendered_document(self.app).text).lower()
        for excluded in ["inseec", "master", "kls", "en poste (alternance)", "future ingénieure", "92.4%", "99.98%"]:
            with self.subTest(excluded=excluded):
                self.assertNotIn(excluded, content)
        self.assertIn("sipperec", content)
        self.assertIn("juritech", content)


if __name__ == "__main__":
    unittest.main()

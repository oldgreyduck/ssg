import unittest
from src.extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual(
            [("image", "https://i.imgur.com/zjjcJKZ.png")],
            matches,
        )

    def test_extract_markdown_links(self):
        matches = extract_markdown_links(
            "Link [to site](https://example.com)"
        )
        self.assertListEqual(
            [("to site", "https://example.com")],
            matches,
        )

    def test_mixed_images_and_links(self):
        text = "Pic ![alt](https://img.png) and [site](https://example.com)"
        img_matches = extract_markdown_images(text)
        link_matches = extract_markdown_links(text)

        self.assertListEqual([("alt", "https://img.png")], img_matches)
        self.assertListEqual([("site", "https://example.com")], link_matches)

if __name__ == "__main__":
    unittest.main()


import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_eq_italic(self):
        node = TextNode("This is an Italic text node", TextType.ITALIC_TEXT)
        node2 = TextNode("This is an Italic text node", TextType.ITALIC_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is plain text node", TextType.PLAIN_TEXT)
        node2 = TextNode("This is not a plain text node", TextType.PLAIN_TEXT)
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("There is no url -- Nietsche", TextType.PLAIN_TEXT, None)
        node2 = TextNode("There is no url -- Nietsche", TextType.PLAIN_TEXT, None)
        self.assertEqual(node, node2)

    def test_url_diff(self):
        node = TextNode("There is no url -- Nietsche", TextType.PLAIN_TEXT, None)
        node2 = TextNode("There is no url -- Nietsche", TextType.PLAIN_TEXT, "https://www.shenanigans.com")
        self.assertNotEqual(node, node2)

    def test_TextType_diff(self):
        node = TextNode("South Park rules", TextType.PLAIN_TEXT)
        node2 = TextNode("South Park rules", TextType.BOLD_TEXT)
        self.assertNotEqual(node, node2)


if __name__ == "__main__":
    unittest.main()

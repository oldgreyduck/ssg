import unittest
from src.textnode import TextNode, TextType
from src.inline_markdown import inline_markdown

class TestInlineMarkdown(unittest.TestCase):
    def test_simple_split(self):
        node = TextNode("a **b** c", TextType.TEXT)
        out = inline_markdown([node], "**", TextType.BOLD)
        self.assertEqual(out, [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode(" c", TextType.TEXT),
        ])

    def test_unmatched_raises(self):
        node = TextNode("a **b c", TextType.TEXT)
        with self.assertRaises(Exception):
            inline_markdown([node], "**", TextType.BOLD)

    def test_double_split(self):
        node = TextNode("a **b** c **d** e", TextType.TEXT)
        out = inline_markdown([node], "**", TextType.BOLD)
        self.assertEqual(out, [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.BOLD),
            TextNode(" c ", TextType.TEXT),
            TextNode("d", TextType.BOLD),
            TextNode(" e", TextType.TEXT),
        ])

    def test_simple_italic_split(self):
        node = TextNode("a _b_ c", TextType.TEXT)
        out = inline_markdown([node], "_", TextType.ITALIC)
        self.assertEqual(out, [
            TextNode("a ", TextType.TEXT),
            TextNode("b", TextType.ITALIC),
            TextNode(" c", TextType.TEXT),
        ])

    def test_outside_split(self):
        node = TextNode("**a** b c", TextType.TEXT)
        out = inline_markdown([node], "**", TextType.BOLD)
        self.assertEqual(out, [
            TextNode("a", TextType.BOLD),
            TextNode(" b c", TextType.TEXT),
        ])

if __name__ == "__main__":
    unittest.main()

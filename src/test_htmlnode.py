import unittest
from src.htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextType, TextNode
from src.textnode_to_htmlnode import textnode_to_htmlnode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_with_attributes(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        expected = ' href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected)
    
    def test_props_to_html_empty_props(self):
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")
    
    def test_props_to_html_single_prop(self):
        node = HTMLNode(props={"class": "container"})
        expected = ' class="container"'
        self.assertEqual(node.props_to_html(), expected)

    def test_props_to_html_color(self):
        node = HTMLNode("h1", "BOOTS!", props={"style": "color: grey;"})
        expected = ' style="color: grey;"'
        self.assertEqual(node.props_to_html(), expected)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_head(self):
        node = LeafNode("h1", "Boots is Magic!", props={"style": "color: grey;"})
        expected = '<h1 style="color: grey;">Boots is Magic!</h1>'
        self.assertEqual(node.to_html(), expected)

    def test_leaf_to_html_empty_val(self):
        node = LeafNode("p", "", props={"style": "color: teal;"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "HTML sucks")
        expected = 'HTML sucks'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = textnode_to_htmlnode(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_unknown_text(self):
        node = TextNode("This is a text node", TextType.UNKNOWN)
        with self.assertRaises(Exception):
            text_node_to_html_node(node) 

if __name__ == "__main__":
    unittest.main()

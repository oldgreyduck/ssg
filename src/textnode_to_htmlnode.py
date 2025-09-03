from src.textnode import TextNode, TextType
from src.htmlnode import HTMLNode, LeafNode, ParentNode


def textnode_to_htmlnode(node):
    if node.text_type == TextType.TEXT:
        return LeafNode(None, node.text)
    if node.text_type == TextType.BOLD:
        return LeafNode("b", node.text)
    if node.text_type == TextType.ITALIC:
        return LeafNode("i", node.text)
    if node.text_type == TextType.CODE:
        return LeafNode("code", node.text)
    if node.text_type == TextType.LINK:
        return LeafNode("a", node.text, props={"href": node.url})
    if node.text_type == TextType.IMAGE:
        return LeafNode("img", "", props={"src": node.url, "alt": node.text})
    raise Exception ("Unknown TextType")
    
from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode


def main():
    node = TextNode("some text here", TextType.LINK, "https://example.com")
    print(node)


main()

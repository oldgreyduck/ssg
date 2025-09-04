from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode
from copystatic import copy_directory_recursive


def main():
    node = TextNode("some text here", TextType.LINK, "https://example.com")
    print(node)

    copy_directory_recursive("static", "public")

if __name__ == "__main__":
    main()

from textnode import TextNode, TextType


def main():
    node = TextNode("some text here", TextType.LINK, "https://example.com")
    print(node)

main()

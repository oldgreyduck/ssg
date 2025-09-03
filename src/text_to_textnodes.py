from src.textnode import TextNode, TextType
from src.split_nodes import split_nodes_image, split_nodes_link
from src.inline_markdown import inline_markdown

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    second_node = [initial_node]
    image_node = split_nodes_image(second_node)
    link_node = split_nodes_link(image_node)
    bold_node = inline_markdown(link_node, "**", TextType.BOLD)
    italic_node = inline_markdown(bold_node, "_", TextType.ITALIC)
    code_node = inline_markdown(italic_node, "`", TextType.CODE)
    return code_node



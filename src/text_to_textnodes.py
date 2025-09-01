from src.textnode import TextNode, TextType

def text_to_textnodes(text):
    initial_node = TextNode(text, TextType.TEXT)
    second_node = [initial_node]
    image_node = split_nodes_image(second_node)
    link_node = split_nodes_link(image_node)
    bold_node = split_nodes_delimiter(link_node, "**", TextType.BOLD)
    italic_node = split_nodes_delimiter(bold_node, "_", TextType.ITALIC)
    code_node = split_nodes_delimiter(italic_node, "`", TextType.CODE)
    return code_node



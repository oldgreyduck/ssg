from src.textnode import TextNode, TextType
from src.extract_markdown import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if getattr(node, "text_type", None) != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_images(node.text)  # list of (alt, url)
        if not extracted:
            new_nodes.append(node)
            continue

        image_alt, image_url = extracted[0]
        before, after = node.text.split(f"![{image_alt}]({image_url})", 1)

        if before:
            new_nodes.append(TextNode(before, TextType.TEXT))
        new_nodes.append(TextNode(image_alt, TextType.IMAGE, image_url))
        if after:
            new_nodes.extend(split_nodes_image([TextNode(after, TextType.TEXT)]))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if getattr(node, "text_type", None) != TextType.TEXT:
            new_nodes.append(node)
            continue

        extracted = extract_markdown_links(node.text)  # returns list of (text, url)
        if not extracted:
            new_nodes.append(node)
            continue

        link_text, link_url = extracted[0]
        before, after = node.text.split(f"[{link_text}]({link_url})", 1)

        if before:
            new_nodes.append(TextNode(before, TextType.TEXT))
        new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
        if after:
            new_nodes.extend(split_nodes_link([TextNode(after, TextType.TEXT)]))
    return new_nodes

from src.textnode import TextNode, TextType
from src.text_to_textnodes import text_to_textnodes
from src.textnode_to_htmlnode import textnode_to_htmlnode

def text_to_children(text):
    if not text or text.strip() == "":
        return []
    else:
        nodes = text_to_textnodes(text)
        return [textnode_to_htmlnode(n) for n in nodes]
from src.htmlnode import ParentNode
from src.text_to_children import text_to_children
from src.block_markdown import markdown_to_blocks, block_to_block_type, BlockType


def markdown_to_htmlnode(markdown: str):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            text = " ".join(block.splitlines())
            children = text_to_children(text)
            nodes.append(ParentNode("p", children))
    return ParentNode("div", nodes)

from src.htmlnode import ParentNode, LeafNode
from src.text_to_children import text_to_children
from src.block_markdown import markdown_to_blocks, block_to_block_type, BlockType


def markdown_to_htmlnode(markdown: str):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        if block_to_block_type(block) == BlockType.PARAGRAPH:
            text = " ".join(block.splitlines())
            children = text_to_children(text)
            para = ParentNode("p", children)
            nodes.append(para)
        if block_to_block_type(block) == BlockType.CODE:
            lines = block.splitlines()
            inner = "\n".join(lines[1:-1]) + "\n"
            code_leaf = LeafNode("code", inner)
            pre = ParentNode("pre", [code_leaf])
            nodes.append(pre)
        if block_to_block_type(block) == BlockType.HEADING:
            first = block.splitlines()[0].lstrip()
            level = 0
            while level < len(first) and first[level] == "#" and level < 6:
                level += 1
            text = first[level + 1:]
            children = text_to_children(text)
            nodes.append(ParentNode(f"h{level}", children))
        if block_to_block_type(block) == BlockType.QUOTE:
            lines = block.splitlines()
            cleaned = []
            for line in lines:
                rest = line
                if rest.startswith(">"):
                    rest = rest[1:]
                if rest.startswith(" "):
                    rest = rest[1:]
                cleaned.append(rest)
            text = " ".join(cleaned)
            children = text_to_children(text)
            nodes.append(ParentNode("blockquote", children))
        

    return ParentNode("div", nodes)

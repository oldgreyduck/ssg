from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown: str) -> list[str]:
    parts = markdown.split("\n\n")
    blocks = [p.strip() for p in parts if p.strip() != ""]
    return blocks

def block_to_block_type(block) -> BlockType:
    lines = block.split("\n")
    first = lines[0]
    last = lines[-1]
    if first == "```" and last == "```":
        return BlockType.CODE
    parts = first.split(" ", 1)
    if len(parts) == 2 and 1 <= len(parts[0]) <= 6 and set(parts[0]) == {"#"}:
        return BlockType.HEADING
    elif all(line.startswith(">") for line in lines):
         return BlockType.QUOTE
    elif all(line.startswith("- ") for line in lines):
         return BlockType.UNORDERED_LIST
    elif all(line.startswith(f"{i}. ") for i, line in enumerate(lines, start=1)):
         return BlockType.ORDERED_LIST
    else:
         return BlockType.PARAGRAPH
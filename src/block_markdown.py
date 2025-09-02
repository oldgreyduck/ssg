def markdown_to_blocks(markdown: str) -> list[str]:
    parts = markdown.split("\n\n")
    blocks = [p.strip() for p in parts if p.strip() != ""]
    return blocks
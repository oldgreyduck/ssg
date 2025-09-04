from src.markdown_to_htmlnode import markdown_to_htmlnode


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        line = line.lstrip()
        if line.startswith("# ") and not line.startswith("##"):
            return line[2:].strip()
    raise Exception("No h1 header found")
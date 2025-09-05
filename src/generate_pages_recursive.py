import os

from src.markdown_to_htmlnode import markdown_to_htmlnode
from src.extract_title import extract_title

def generate_pages_recursive(from_path, template_path, dest_path):
    for root, dirs, files in os.walk(from_path):
        for file in files:
            if file.endswith(".md"):
                from_filepath = os.path.join(root, file)

                relative_path = os.path.relpath(from_filepath, from_path)

                dest_filepath = os.path.join(dest_path, relative_path)
                dest_filepath = os.path.splitext(dest_filepath)[0] + ".html"

                generate_page(from_filepath, template_path, dest_filepath)

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, "r", encoding="utf-8") as f:
        markdown = f.read()
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    html = markdown_to_htmlnode(markdown).to_html()
    title = extract_title(markdown)

    out = template.replace("{{ Title }}", title).replace("{{ Content }}", html)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(out)

import os, shutil
from src.copystatic import copy_directory_recursive
from src.generate_page import generate_page


def main():
    shutil.rmtree("public", ignore_errors=True)
    os.makedirs("public", exist_ok=True)

    copy_directory_recursive("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()

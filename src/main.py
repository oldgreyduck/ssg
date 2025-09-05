import os, shutil
from src.copystatic import copy_directory_recursive
from src.generate_pages_recursive import generate_pages_recursive


def main():
    shutil.rmtree("public", ignore_errors=True)
    os.makedirs("public", exist_ok=True)

    copy_directory_recursive("static", "public")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()

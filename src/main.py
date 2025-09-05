import os, shutil, sys
from src.copystatic import copy_directory_recursive
from src.generate_pages_recursive import generate_pages_recursive


def main():
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    print(f"basepath: {basepath}")

    shutil.rmtree("docs", ignore_errors=True)
    os.makedirs("docs", exist_ok=True)

    copy_directory_recursive("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()

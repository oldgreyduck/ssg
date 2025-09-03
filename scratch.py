# python
from src.text_to_children import text_to_children

children = text_to_children("hi **bold** and `code`")
html = "".join(child.to_html() for child in children)
print(html)
import unittest
from src.markdown_to_htmlnode import markdown_to_htmlnode


class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_code(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```

"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
    )
        
    def test_heading(self):
        md = """
### This is some damn fine code
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><h3>This is some damn fine code</h3></div>",
    )
        
    def test_quote(self):
        md = """
> This is some **damn** _fine_ code
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><blockquote>This is some <b>damn</b> <i>fine</i> code</blockquote></div>",
    )
        
    def test_unordered(self):
        md = """
- This is some damn fine code
- That **thou** hast written
- Using _exquisite_ codemanship
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ul><li>This is some damn fine code</li><li>That <b>thou</b> hast written</li><li>Using <i>exquisite</i> codemanship</li></ul></div>",
    )
        
    def test_ordered(self):
        md = """
1. This is some damn fine code
2. That **thou** hast written
3. Using _exquisite_ codemanship
"""

        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
        "<div><ol><li>This is some damn fine code</li><li>That <b>thou</b> hast written</li><li>Using <i>exquisite</i> codemanship</li></ol></div>",
    )
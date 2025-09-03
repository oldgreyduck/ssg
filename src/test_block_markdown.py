import unittest
from src.block_markdown import BlockType, markdown_to_blocks, block_to_block_type

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_empty_lines(self):
        md = """


"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [],
        )

    def test_markdown_to_blocks_single_block(self):
        md = """
_Italian_ food is very **bold** in flavor
DaVinci often painted in `coded language`
Amalfi lemons are tangy
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                    "_Italian_ food is very **bold** in flavor\nDaVinci often painted in `coded language`\nAmalfi lemons are tangy",
            ],
        )

class TestBlockToBlockType(unittest.TestCase):
    def test_block_to_block_type_code(self):
        block = "```\nthis is some damn fine code homey\n```"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.CODE)

    def test_block_to_block_type_heading(self):
        block = "## this is some damn fine code homey"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.HEADING)

    def test_block_to_block_type_quote(self):
        block = "> this is some damn fine code homey\n> yo"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.QUOTE)

    def test_block_to_block_type_unordered(self):
        block = "- this is some damn fine code homey\n- yo"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.UNORDERED_LIST)

    def test_block_to_block_type_ordered(self):
        block = "1. this is some damn fine code homey\n2. yo"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.ORDERED_LIST)

    def test_block_to_block_type_paragraph(self):
        block = "this is some damn fine code homey\nyo"
        bt = block_to_block_type(block)
        self.assertEqual(bt, BlockType.PARAGRAPH)

# test_md2html.py — written BEFORE implementation (TDD)
from md2html import convert

# Feature 1: Headings
def test_h1_heading():
    assert convert("# Hello") == "<h1>Hello</h1>"

def test_h2_heading():
    assert convert("## Sub") == "<h2>Sub</h2>"

def test_h3_heading():
    assert convert("### Deep") == "<h3>Deep</h3>"

# Feature 2: Bold and Italic
def test_bold():
    assert convert("**bold**") == "<p><strong>bold</strong></p>"

def test_italic():
    assert convert("*italic*") == "<p><em>italic</em></p>"

def test_inline_code():
    assert convert("`code`") == "<p><code>code</code></p>"

# Feature 3: Lists
def test_unordered_list():
    result = convert("- one\n- two")
    assert "<ul>" in result
    assert "<li>one</li>" in result
    assert "<li>two</li>" in result

def test_ordered_list():
    result = convert("1. first\n2. second")
    assert "<ol>" in result
    assert "<li>first</li>" in result
    assert "<li>second</li>" in result

# Feature 4: Links
def test_link():
    assert convert("[Google](https://google.com)") == '<p><a href="https://google.com">Google</a></p>'

# Feature 5: Paragraphs
def test_paragraph():
    assert convert("Hello world") == "<p>Hello world</p>"

def test_two_paragraphs():
    result = convert("First\n\nSecond")
    assert "<p>First</p>" in result
    assert "<p>Second</p>" in result

# Feature 6: Code blocks
def test_fenced_code_block():
    result = convert("```\ncode here\n```")
    assert "<pre><code>" in result
    assert "code here" in result
    assert "</code></pre>" in result

# Edge cases
def test_empty_input():
    assert convert("") == ""

def test_mixed_inline():
    result = convert("**bold** and *italic*")
    assert "<strong>bold</strong>" in result
    assert "<em>italic</em>" in result

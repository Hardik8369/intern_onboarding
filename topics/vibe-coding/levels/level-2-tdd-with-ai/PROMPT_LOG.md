# Prompt Log — TDD with AI (md2html Level 2)

## How this works

For each feature: wrote the test first → ran it (RED/error) → prompted AI to implement →
ran again (GREEN). Tests were always written before implementation.

---

## Cycle 1: Headings

**Tests written first:**
```python
def test_h1_heading():
    assert convert("# Hello") == "<h1>Hello</h1>"
def test_h2_heading():
    assert convert("## Sub") == "<h2>Sub</h2>"
def test_h3_heading():
    assert convert("### Deep") == "<h3>Deep</h3>"
```

**Ran tests:** ERROR — ModuleNotFoundError: No module named 'md2html'. Confirmed RED.

**AI prompt:**
I am doing TDD. I have written these failing tests for a markdown to HTML converter.
Write a convert() function in md2html.py that makes them pass. Only implement heading
support for now (# ## ###). Do not use any third-party markdown libraries.

**AI response:** Generated convert() with regex for h1/h2/h3 using startswith checks.

**Result:** Tests passed. Accepted implementation as-is.

---

## Cycle 2: Inline formatting (bold, italic, code)

**Tests written first:**
```python
def test_bold():
    assert convert("**bold**") == "<p><strong>bold</strong></p>"
def test_italic():
    assert convert("*italic*") == "<p><em>italic</em></p>"
def test_inline_code():
    assert convert("`code`") == "<p><code>code</code></p>"
```

**Ran tests:** FAILED — convert() returned raw text, no inline parsing.

**AI prompt:**
My TDD tests for bold, italic, and inline code are failing. Add a parse_inline() helper
function that handles **bold** → strong, *italic* → em, and backtick code → code tags.
Apply it inside the paragraph handler. Order matters: process inline code before bold/italic
so backticks are not affected by asterisk parsing.

**AI response:** Generated parse_inline() with three regex substitutions in correct order
(inline code first, then bold, then italic).

**Result:** All three tests passed. Accepted. Verified ordering was correct by checking
that `**bold `code` bold**` did not break.

---

## Cycle 3: Lists (unordered and ordered)

**Tests written first:**
```python
def test_unordered_list():
    result = convert("- one\n- two")
    assert "<ul>" in result
    assert "<li>one</li>" in result

def test_ordered_list():
    result = convert("1. first\n2. second")
    assert "<ol>" in result
    assert "<li>first</li>" in result
```

**Ran tests:** FAILED — list items rendered as paragraphs.

**AI prompt:**
My tests for unordered and ordered lists are failing. Add list handling to convert().
Collect consecutive lines starting with "- " into a ul block. Collect consecutive lines
matching r"^\d+\. " into an ol block. Important: place these checks BEFORE the paragraph
fallback in the if/elif chain, otherwise numbered lines get caught by the paragraph handler.

**AI response:** Added both list handlers with while loops to collect consecutive items.
Placed them before the paragraph fallback as instructed.

**Result:** Tests passed. I verified the branch ordering myself before accepting — confirmed
ordered list check comes before paragraph fallback in the elif chain.

---

## Cycle 4: Links, paragraphs, code blocks, and edge cases

**Tests written first:**
```python
def test_link():
    assert convert("[Google](https://google.com)") == '<p><a href="https://google.com">Google</a></p>'
def test_paragraph():
    assert convert("Hello world") == "<p>Hello world</p>"
def test_two_paragraphs():
    result = convert("First\n\nSecond")
    assert "<p>First</p>" in result
    assert "<p>Second</p>" in result
def test_fenced_code_block():
    result = convert("```\ncode here\n```")
    assert "<pre><code>" in result
def test_empty_input():
    assert convert("") == ""
def test_mixed_inline():
    result = convert("**bold** and *italic*")
    assert "<strong>bold</strong>" in result
    assert "<em>italic</em>" in result
```

**Ran tests:** FAILED — links not parsed, paragraphs missing, code blocks not handled.

**AI prompt:**
My remaining TDD tests are failing. Add to md2html.py: (1) link parsing [text](url) to
parse_inline(), (2) paragraph wrapping for plain text lines in p tags, (3) blank line
handling as paragraph separator, (4) fenced code block support using triple backticks,
(5) empty input should return empty string. Make all these tests pass without breaking
the heading and list tests already passing.

**AI response:** Added link regex to parse_inline(), paragraph collector with blank-line
separation, fenced code block handler, and empty string check at top of convert().

**Result:** All 14 tests passed. Reviewed the paragraph collector while-loop conditions
carefully — confirmed it stops at headings, lists, blockquotes, and code fences to avoid
consuming those lines as paragraph text.

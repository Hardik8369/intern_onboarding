# Verification — md2html

## How I verified

Ran python3 md2html.py for each test case and checked the HTML output matched expectations.

## Test Cases

### TC1: Headings (happy path)
Input: # Heading 1 / ## Heading 2 / ### Heading 3
Expected: h1, h2, h3 tags
Actual: Matched exactly
Result: PASS

### TC2: Bold, italic, inline code (happy path)
Input: This is **bold** and *italic* and backtick code backtick
Expected: strong, em, code tags inside a p tag
Actual: Matched exactly
Result: PASS

### TC3: Unordered list (happy path)
Input: - Item one / - Item two / - Item three
Expected: ul with three li tags
Actual: Matched exactly
Result: PASS

### TC4: Ordered list (bug found and fixed)
Input: 1. First / 2. Second / 3. Third
Expected: ol with three li tags
Actual before fix: Items rendered as paragraphs because paragraph branch came before ordered list check
Bug fix: Reordered if/elif chain in convert() so ordered list check comes before paragraph fallback
Actual after fix: Matched expected exactly
Result: PASS after fix

### TC5: Fenced code block (happy path)
Input: triple backtick block with python code
Expected: pre and code tags wrapping the code
Actual: Matched exactly
Result: PASS

### TC6: Link and blockquote (happy path)
Input: [Google](https://www.google.com) and > blockquote text
Expected: a tag and blockquote tag
Actual: Matched exactly
Result: PASS

### TC7: Missing input file (edge case)
Command: python3 md2html.py nonexistent.md -o out.html
Expected: Clean error message, no traceback
Actual: Error: input file "nonexistent.md" not found.
Result: PASS

### TC8: No arguments (edge case)
Command: python3 md2html.py
Expected: Usage/help shown, not a crash
Actual: argparse shows usage and required arguments error
Result: PASS

### TC9: Horizontal rule (happy path)
Input: ---
Expected: hr tag
Actual: Matched exactly
Result: PASS

## Bugs Found and Fixed

Bug 1: Ordered lists rendered as paragraphs
Found: TC4 manual testing
Fix: Reordered if/elif branches so ordered list check comes before paragraph fallback

Bug 2: Image regex greedy match broke on empty alt text
Found: Code review of AI output
Fix: Changed (.+) to ([^\]]*) in image regex to handle empty alt text

## Overall
9 test cases, all pass after fixes. 2 bugs found and fixed.

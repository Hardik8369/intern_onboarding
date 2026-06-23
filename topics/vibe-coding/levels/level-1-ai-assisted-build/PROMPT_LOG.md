# Prompt Log — AI-Assisted Build (md2html)

## Prompt 1 — Initial build request

**What I asked:**
I am building a Python CLI tool called `md2html.py` that converts a Markdown file to HTML.
Requirements: takes an input `.md` filename and an `-o output.html` flag; supports headings
(#/##/###), bold (**), italic (*), inline code (backtick), unordered and ordered lists,
links ([text](url)), and paragraphs (blank-line separated); wraps output in a basic
html/body skeleton; has a --help flag via argparse. Please write the full file, then explain
each function. Do NOT use third-party markdown libraries; I want to learn the parsing myself.

**AI response summary:**
AI generated a full `md2html.py` with argparse CLI, regex-based inline parsing (bold,
italic, code, links), block-level parsing (headings, lists, paragraphs), fenced code blocks,
and an HTML skeleton wrapper. Each function was explained clearly.

**What I did:**
Accepted the overall structure. Read through each function carefully. Noticed that the
paragraph collector did not handle the case where a paragraph runs into a heading — it would
consume the heading line as paragraph text. Modified the paragraph while-loop condition to
stop at heading lines, list lines, blockquotes, and code fences.

---

## Prompt 2 — Adding missing features

**What I asked:**
The tool works for basic cases but is missing: blockquotes (> text), horizontal rules (---),
and image support (![alt](url)). Please add these to the existing parse_inline and convert
functions. Also the fenced code block is not being closed correctly when the closing ``` is
on the last line of the file — fix that too.

**AI response summary:**
AI added blockquote handling (`> ` prefix → `<blockquote>`), horizontal rule detection
(`---` → `<hr>`), and image regex in `parse_inline`. Also fixed the fenced code block loop
to handle EOF without a closing fence gracefully.

**What I did:**
Accepted blockquote and horizontal rule additions. Modified the image regex slightly — the
AI used a greedy match for the alt text which would break on nested brackets. Changed
`(.+)` to `([^\]]*)` to make it non-greedy and handle empty alt text correctly.

---

## Prompt 3 — Edge case handling and error messages

**What I asked:**
When I run `python3 md2html.py nonexistent.md -o out.html` the tool crashes with a Python
FileNotFoundError traceback. I want it to print a clean error message like:
`Error: input file "nonexistent.md" not found.` and exit with code 1.
Also when run with no arguments it should show help, not a cryptic argparse error.

**AI response summary:**
AI added an `os.path.exists()` check before opening the file, with a clean error message
printed to stderr and `sys.exit(1)`. For the no-arguments case, AI suggested using
`parser.print_help()` when `len(sys.argv) == 1`, but noted argparse already shows usage
on missing required args.

**What I did:**
Accepted the file existence check — exactly what was needed. Rejected the `len(sys.argv)`
suggestion because argparse already handles missing required positional arguments with a
clear "the following arguments are required" message, so adding a separate check would be
redundant. Kept the cleaner argparse default behavior.

---

## Prompt 4 — Verification of ordered lists

**What I asked:**
I tested ordered lists (`1. item`, `2. item`) and the tool is not outputting `<ol>` tags —
it is treating them as paragraphs. The unordered list uses `re.match(r'^- ')` which works,
but the ordered list regex `r'^\d+\. '` does not seem to be matching. Can you help debug?

**AI response summary:**
AI identified that the ordered list branch was placed after the paragraph catch-all in the
if/elif chain, so the paragraph collector was consuming numbered lines before the ordered
list check was reached. AI suggested reordering the elif branches so ordered and unordered
list checks come before the paragraph fallback.

**What I did:**
Accepted the fix. Reordered the branches in the convert() function: headings → hr →
blockquote → unordered list → ordered list → blank line → paragraph. Tested again and
ordered lists now produce correct `<ol><li>` output.

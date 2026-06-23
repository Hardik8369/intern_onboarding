#!/usr/bin/env python3
"""md2html.py — Convert a Markdown file to HTML."""

import argparse
import re
import sys
import os


def parse_inline(text):
    """Convert inline Markdown (bold, italic, code, links) to HTML."""
    # Inline code (must come before bold/italic)
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    # Bold
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    # Images
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img alt="\1" src="\2">', text)
    return text


def convert(md_text):
    """Convert full Markdown text to HTML body content."""
    lines = md_text.splitlines()
    html_lines = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Fenced code block
        if line.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].startswith('```'):
                code_lines.append(lines[i])
                i += 1
            html_lines.append('<pre><code>' + '\n'.join(code_lines) + '</code></pre>')
            i += 1
            continue

        # Headings
        if line.startswith('### '):
            html_lines.append(f'<h3>{parse_inline(line[4:])}</h3>')
        elif line.startswith('## '):
            html_lines.append(f'<h2>{parse_inline(line[3:])}</h2>')
        elif line.startswith('# '):
            html_lines.append(f'<h1>{parse_inline(line[2:])}</h1>')

        # Horizontal rule
        elif re.match(r'^---+$', line.strip()):
            html_lines.append('<hr>')

        # Blockquote
        elif line.startswith('> '):
            html_lines.append(f'<blockquote>{parse_inline(line[2:])}</blockquote>')

        # Unordered list item
        elif re.match(r'^- ', line):
            # Collect all consecutive list items
            items = []
            while i < len(lines) and re.match(r'^- ', lines[i]):
                items.append(f'  <li>{parse_inline(lines[i][2:])}</li>')
                i += 1
            html_lines.append('<ul>\n' + '\n'.join(items) + '\n</ul>')
            continue

        # Ordered list item
        elif re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                content = re.sub(r'^\d+\. ', '', lines[i])
                items.append(f'  <li>{parse_inline(content)}</li>')
                i += 1
            html_lines.append('<ol>\n' + '\n'.join(items) + '\n</ol>')
            continue

        # Blank line — paragraph separator
        elif line.strip() == '':
            html_lines.append('')

        # Regular paragraph
        else:
            # Collect consecutive non-empty, non-special lines as a paragraph
            para_lines = []
            while i < len(lines) and lines[i].strip() != '' and \
                  not lines[i].startswith('#') and \
                  not lines[i].startswith('- ') and \
                  not lines[i].startswith('> ') and \
                  not lines[i].startswith('```') and \
                  not re.match(r'^\d+\. ', lines[i]) and \
                  not re.match(r'^---+$', lines[i].strip()):
                para_lines.append(lines[i])
                i += 1
            if para_lines:
                html_lines.append(f'<p>{parse_inline(" ".join(para_lines))}</p>')
            continue

        i += 1

    return '\n'.join(html_lines)


def wrap_html(body_content, title='Document'):
    """Wrap body content in a full HTML skeleton."""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
</head>
<body>
{body_content}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(
        prog='md2html',
        description='Convert a Markdown file to HTML.'
    )
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('-o', '--output', required=True, help='Output HTML file')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f'Error: input file "{args.input}" not found.', file=sys.stderr)
        sys.exit(1)

    if not args.input.endswith('.md'):
        print('Warning: input file does not have a .md extension.', file=sys.stderr)

    with open(args.input, 'r', encoding='utf-8') as f:
        md_text = f.read()

    title = os.path.splitext(os.path.basename(args.input))[0]
    body = convert(md_text)
    html = wrap_html(body, title=title)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Converted "{args.input}" → "{args.output}"')


if __name__ == '__main__':
    main()

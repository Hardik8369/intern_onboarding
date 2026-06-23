import re
import argparse
import sys
import os


def parse_inline(text):
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    return text


def convert(md_text):
    if not md_text.strip():
        return ""

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

        # Unordered list
        elif re.match(r'^- ', line):
            items = []
            while i < len(lines) and re.match(r'^- ', lines[i]):
                items.append(f'<li>{parse_inline(lines[i][2:])}</li>')
                i += 1
            html_lines.append('<ul>\n' + '\n'.join(items) + '\n</ul>')
            continue

        # Ordered list
        elif re.match(r'^\d+\. ', line):
            items = []
            while i < len(lines) and re.match(r'^\d+\. ', lines[i]):
                content = re.sub(r'^\d+\. ', '', lines[i])
                items.append(f'<li>{parse_inline(content)}</li>')
                i += 1
            html_lines.append('<ol>\n' + '\n'.join(items) + '\n</ol>')
            continue

        # Blank line
        elif line.strip() == '':
            html_lines.append('')

        # Paragraph
        else:
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

    return '\n'.join(line for line in html_lines if line != '').strip()


def wrap_html(body_content, title='Document'):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{title}</title>
</head>
<body>
{body_content}
</body>
</html>"""


def main():
    parser = argparse.ArgumentParser(prog='md2html', description='Convert Markdown to HTML.')
    parser.add_argument('input', help='Input Markdown file (.md)')
    parser.add_argument('-o', '--output', required=True, help='Output HTML file')
    args = parser.parse_args()

    if not os.path.exists(args.input):
        print(f'Error: input file "{args.input}" not found.', file=sys.stderr)
        sys.exit(1)

    with open(args.input, 'r', encoding='utf-8') as f:
        md_text = f.read()

    title = os.path.splitext(os.path.basename(args.input))[0]
    body = convert(md_text)
    html = wrap_html(body, title=title)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f'Converted "{args.input}" -> "{args.output}"')


if __name__ == '__main__':
    main()

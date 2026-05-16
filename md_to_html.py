#!/usr/bin/env python3

import re
import sys

def markdown_to_html(md_content):
    html = md_content
    
    # Code blocks (fenced)
    def code_block(m):
        code = m.group(1)
        return f'<pre><code>{code}</code></pre>'
    html = re.sub(r'```(\w+)?\n(.*?)```', lambda m: f'<pre><code>{m.group(2)}</code></pre>', html, flags=re.DOTALL)
    
    # Code blocks (simple backticks)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Headers
    def h1(m): return f'<h1>{m.group(1)}</h1>'
    def h2(m): 
        text = m.group(1)
        anchor = text.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '')
        return f'<h2 id="{anchor}">{text}</h2>'
    def h3(m): return f'<h3>{m.group(1)}</h3>'
    
    html = re.sub(r'^# (.+)$', h1, html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', h2, html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', h3, html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)
    
    # Links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Horizontal rules
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)
    
    # Tables (simplified)
    lines = html.split('\n')
    in_table = False
    result = []
    for line in lines:
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                result.append('<table>')
            # Remove leading/trailing pipes
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            if all(cell == '-' * len(cell) for cell in cells):
                continue  # Skip separator row
            result.append('<tr>')
            for cell in cells:
                result.append(f'<td>{cell}</td>')
            result.append('</tr>')
        else:
            if in_table:
                in_table = False
                result.append('</table>')
            result.append(line)
    if in_table:
        result.append('</table>')
    html = '\n'.join(result)
    
    # Lists (simple)
    lines = html.split('\n')
    in_list = False
    result = []
    for line in lines:
        if line.strip().startswith('- ') or line.strip().startswith('* '):
            if not in_list:
                in_list = True
                result.append('<ul>')
            item = re.sub(r'^[\s]*[-*]\s+', '', line)
            result.append(f'<li>{item}</li>')
        elif line.strip().startswith(r'\d+. '):
            if not in_list:
                in_list = True
                result.append('<ol>')
            item = re.sub(r'^[\s]*\d+\.\s+', '', line)
            result.append(f'<li>{item}</li>')
        else:
            if in_list:
                in_list = False
                result.append('</ul>' if result[-1] == '<ol>' else '</ul>')
            result.append(line)
    if in_list:
        result.append('</ul>')
    html = '\n'.join(result)
    
    # Paragraphs
    lines = html.split('\n\n')
    result = []
    for paragraph in lines:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        # Skip if already HTML block element
        if re.match(r'^<(h|ul|ol|table|pre|hr|div)', paragraph):
            result.append(paragraph)
        elif '|' in paragraph and '|' not in ' '.join(paragraph.split()):
            # Don't wrap table rows
            result.append(paragraph)
        else:
            # Wrap non-empty text in <p>
            if paragraph:
                result.append(f'<p>{paragraph}</p>')
    html = '\n\n'.join(result)
    
    return html

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: md_to_html.py <input.md> <output.html>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    
    with open(input_file, 'r') as f:
        md_content = f.read()
    
    html_content = markdown_to_html(md_content)
    
    with open(output_file, 'w') as f:
        f.write(html_content)
    
    print(f"Converted {input_file} -> {output_file}")

#!/usr/bin/env python3

import re
import sys

def markdown_to_html(md_content):
    # Strip Jekyll frontmatter
    if md_content.startswith('---'):
        frontmatter_end = md_content.find('\n---\n', 3)
        if frontmatter_end != -1:
            md_content = md_content[frontmatter_end + 4:]
    
    html = md_content
    
    # Code blocks (fenced)
    html = re.sub(r'```(\w+)?\n(.*?)```', lambda m: f'<pre><code>{m.group(2)}</code></pre>', html, flags=re.DOTALL)
    
    # Code blocks (simple backticks)
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Headers
    def h1(m): return f'<h1>{m.group(1)}</h1>'
    def h2(m): 
        text = m.group(1)
        anchor = text.lower().replace(' ', '-').replace(':', '').replace('(', '').replace(')', '').replace(',', '')
        return f'<h2 id="{anchor}">{text}</h2>'
    def h3(m): return f'<h3>{m.group(1)}</h3>'
    
    html = re.sub(r'^# (.+)$', h1, html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', h2, html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', h3, html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', html)
    
    # Images
    html = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1">', html)
    
    # Links (must come after images to avoid matching image syntax)
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # Horizontal rules
    html = re.sub(r'^---+$', '<hr>', html, flags=re.MULTILINE)
    
    # Tables (simplified)
    lines = html.split('\n')
    in_table = False
    header_done = False
    result = []
    for line in lines:
        if '|' in line and line.strip().startswith('|'):
            if not in_table:
                in_table = True
                header_done = False
                result.append('<table>')
            cells = [cell.strip() for cell in line.strip('|').split('|')]
            if all(cell.startswith('-') and cell.endswith('-') and cell.strip('-') == '' for cell in cells):
                header_done = True
                continue
            is_header = not header_done and any(cell for cell in cells)
            result.append('<tr>')
            for cell in cells:
                if is_header:
                    result.append(f'<th>{cell}</th>')
                else:
                    result.append(f'<td>{cell}</td>')
            result.append('</tr>')
            if is_header:
                header_done = True
        else:
            if in_table:
                in_table = False
                header_done = False
                result.append('</table>')
            result.append(line)
    if in_table:
        result.append('</table>')
    html = '\n'.join(result)
    
    # Lists (simple)
    lines = html.split('\n')
    in_list = False
    list_type = None
    result = []
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('- ') or stripped.startswith('* '):
            if not in_list:
                in_list = True
                list_type = 'ul'
                result.append('<ul>')
            item = re.sub(r'^[\s]*[-*]\s+', '', line)
            result.append(f'<li>{item}</li>')
        elif re.match(r'^\d+\.\s', stripped):
            if not in_list:
                in_list = True
                list_type = 'ol'
                result.append('<ol>')
            item = re.sub(r'^[\s]*\d+\.\s+', '', stripped)
            # Reconstruct line with original indentation
            indent = line[:len(line) - len(line.lstrip())]
            result.append(f'{indent}<li>{item}</li>')
        else:
            if in_list:
                in_list = False
                result.append('</ul>' if list_type == 'ul' else '</ol>')
            result.append(line)
    if in_list:
        result.append('</ul>' if list_type == 'ul' else '</ol>')
    html = '\n'.join(result)
    
    # Paragraph wrapping - be smarter about what to wrap
    lines = html.split('\n\n')
    result = []
    # Tags that should NOT be wrapped in <p>
    block_tags = (
        'h[1-6]', 'ul', 'ol', 'li', 'table', 'tr', 'th', 'td',
        'pre', 'hr', 'div', 'details', 'summary',
        'svg', 'defs', 'rect', 'circle', 'line', 'path', 'polygon',
        'text', 'g', 'marker', 'linearGradient', 'stop',
        'figure', 'figcaption', 'blockquote', 'nav', 'aside', 'main',
        'head', 'body', 'html', 'script', 'style', 'form', 'input',
        'button', 'select', 'textarea', 'label', 'iframe', 'img',
        'canvas', 'video', 'audio', 'source', 'track',
        'dl', 'dt', 'dd', 'section', 'article', 'header', 'footer',
    )
    block_pattern = re.compile(r'^</?(' + '|'.join(block_tags) + r')')
    # Also skip lines that start with anything that looks like an HTML tag
    any_tag_pattern = re.compile(r'^<\w+')

    for paragraph in lines:
        paragraph = paragraph.strip()
        if not paragraph:
            continue
        # If it starts with a known block tag, don't wrap
        if block_pattern.match(paragraph):
            result.append(paragraph)
        elif any_tag_pattern.match(paragraph):
            result.append(paragraph)
        elif '|' in paragraph and '|' not in ' '.join(paragraph.split()):
            result.append(paragraph)
        else:
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

"""
Convert USER_GUIDE_VI.md to PDF with A4 page size
"""

import markdown
from weasyprint import HTML, CSS
from pathlib import Path

# Read markdown file
md_file = Path("docs/USER_GUIDE_VI.md")
with open(md_file, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Convert markdown to HTML
html_content = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])

# Add CSS for A4 page
css = """
@page {
    size: A4;
    margin: 2cm;
}
body {
    font-family: 'Arial', sans-serif;
    font-size: 11pt;
    line-height: 1.6;
}
h1 {
    font-size: 20pt;
    color: #2c3e50;
    border-bottom: 2px solid #3498db;
    padding-bottom: 0.5em;
}
h2 {
    font-size: 16pt;
    color: #34495e;
    margin-top: 1em;
}
h3 {
    font-size: 14pt;
    color: #7f8c8d;
}
code {
    background: #f4f4f4;
    padding: 2px 5px;
    border-radius: 3px;
    font-family: 'Courier New', monospace;
}
pre {
    background: #f4f4f4;
    padding: 10px;
    border-left: 3px solid #3498db;
    overflow-x: auto;
}
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1em 0;
}
th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
}
th {
    background-color: #3498db;
    color: white;
}
"""

# Create full HTML
full_html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Hướng Dẫn Sử Dụng - Multi-Strategy Backtesting Platform</title>
</head>
<body>
{html_content}
</body>
</html>
"""

# Generate PDF
output_file = "docs/USER_GUIDE_VI.pdf"
HTML(string=full_html).write_pdf(
    output_file,
    stylesheets=[CSS(string=css)]
)

print(f"✅ PDF created: {output_file}")
print("📄 Page size: A4 (210mm x 297mm)")

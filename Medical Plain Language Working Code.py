
import os
import re
import sys
import argparse
from datetime import datetime

def in_notebook():
    try:
        get_ipython()
        return True
    except NameError:
        return False

# CDC thesaurus: simplified for demo
terms = {
    "hypertension": ["high blood pressure"],
    "dyspnea": ["shortness of breath", "difficulty breathing"],
    "febrile": ["feverish", "caused by a fever"],
    "utilize": ["use"],
    "abdomen": ["stomach", "belly", "tummy"]
    # Add more terms as needed
}

def simplify(text):
    for term, synonyms in terms.items():
        if synonyms:
            simple = synonyms[0]
            tooltip = ", ".join(synonyms)
            pattern = re.compile(rf'\b{re.escape(term)}\b', re.IGNORECASE)
            text = pattern.sub(
                rf'<abbr title="{tooltip}" style="text-decoration:underline dotted;" aria-describedby="tooltip">{simple}</abbr>',
                text)
    return text

def make_html(original, simplified):
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Accessible Medical Text</title>
<style>
  body {{ font-family: Arial; color: #000; background: #fff; line-height: 1.6; }}
  .container {{ max-width: 800px; margin: auto; padding: 1em; }}
  abbr {{ border-bottom: 1px dotted; cursor: help; }}
</style>
</head>
<body>
  <main class="container" role="main">
    <h1 tabindex="0">Medical Text Simplifier</h1>
    <section><strong>Original Text:</strong><p>{original}</p></section>
    <section><strong>Simplified Text:</strong><p>{simplified}</p></section>
    <footer><small>Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</small></footer>
  </main>
</body>
</html>"""

def main():
    parser = argparse.ArgumentParser(description="Simplify medical text into WCAG 2.2 accessible HTML.")
    parser.add_argument("-i", "--input", help="Input text file (optional). If omitted, reads from stdin or prompts.")
    parser.add_argument("-o", "--output", help="Output HTML file path", required=True)

    if in_notebook():
        args = parser.parse_args(["-i", "input.txt", "-o", "output.html"])
    else:
        args = parser.parse_args()

    if args.input:
        if not os.path.exists(args.input):
            print("Error: Input file does not exist.")
            sys.exit(1)
        with open(args.input, "r", encoding="utf-8") as f:
            original = f.read()
    elif not sys.stdin.isatty():
        original = sys.stdin.read()
    else:
        print("Enter/paste medical text (press Enter twice to finish):")
        lines = []
        while True:
            line = input()
            if line.strip() == "":
                break
            lines.append(line)
        original = "\n".join(lines)

    simplified = simplify(original)
    html = make_html(original, simplified)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"✅ Accessible HTML file created: {args.output}")

if __name__ == "__main__":
    main()





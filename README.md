
# 🩺 Medical Text Simplifier – WCAG 2.2 Compliant

This project is a **rule-based medical language simplifier** that converts complex clinical language into **plain, accessible language**. It wraps simplified terms in semantic HTML with tooltips to meet **WCAG 2.2 accessibility guidelines**.

---

## ✅ What the Code Does

- **Loads a CDC-inspired thesaurus** of complex medical terms and their plain-language equivalents.
- Scans any clinical text and replaces complex terms with simpler synonyms.
- **Wraps replacements in `<abbr>` tags** with `aria-describedby` and tooltips to assist screen readers.
- Generates a fully accessible, clean **HTML file** showing both the original and simplified versions of the text.

---

## 💡 How to Use It

You can run the script from your terminal or command line using Python.

### 🔹 Option 1: Use a text file

```bash
python medical_text_simplifier.py -i input.txt -o output.html
```

- `-i`: Path to your input medical text file.
- `-o`: Path to save the accessible output HTML file.

### 🔹 Option 2: Paste text interactively

```bash
python medical_text_simplifier.py -o output.html
```

- You’ll be prompted to paste or type in your text.
- Press **Enter twice** to finish input.

---

## 📚 Dataset or Model Used

- This tool uses a **custom-built medical plain language dictionary** adapted from the **CDC’s Plain Language Thesaurus for Health Communications**.
- No AI model or machine learning is used — it's a **deterministic, rule-based system** for maximum clarity and reproducibility.

---

## 🧪 Example

**Input**:
```
The patient was febrile and complained of dyspnea. Antihypertensive therapy was initiated.
```

**Output (HTML)**:
> The patient was  
> `<abbr title="feverish, caused by a fever">feverish</abbr>`  
> and complained of  
> `<abbr title="shortness of breath, difficulty breathing">shortness of breath</abbr>`...

---

## 📁 Want to Contribute?

Feel free to:
- Expand the thesaurus (`terms`) with more terms and synonyms
- Add support for PDF export or JSON output
- Submit PRs for performance or accessibility improvements

---

## 🔧 Future Enhancements

- 🔄 Azure Text Analytics API integration for dynamic term recognition  
- 💻 GUI or web form interface for real-time EHR text simplification  
- 📊 Flesch-Kincaid readability scoring and feedback  

# 🩺🥼💉Medical Plain Language Simplifier
This Python script simplifies complex medical text into plain language using **rule-based logic** and a curated **medical thesaurus**. It is designed to support projects aimed at improving patient understanding and reducing barriers caused by **low health literacy**.

This repository supports a research initiative focused on health literacy improvement by translating dense medical language into accessible terms. While the current version uses Python-based string processing and pattern matching, future expansion includes leveraging **Artificial Intelligence (AI)** and **Natural Language Processing (NLP)** for more dynamic and context-aware simplification.

---
##  What the Code Does

The script performs the following:
- Loads a **CDC-inspired thesaurus** of complex-to-plain medical terms
- Applies a series of **language simplification rules** to:
  - Convert medical jargon into everyday language
  - Replace passive voice with active voice
  - Eliminate redundancy and complex phrases
  - Format longer sentences into clearer chunks
- Processes sample sentences and outputs simplified results
---

## ▶️ How to Use It

### 1. Install Python
Ensure you are running **Python 3.6+**

### 2. Run the Script
Save the script as `plain_language_simplifier.py` and run:

```bash
python plain_language_simplifier.py

---
## Dataset / Model Used

Plain Language Thesaurus
The embedded thesaurus (cdc_thesaurus) is based on terminology adapted from the CDC’s Plain Language Thesaurus, covering a wide range of medical and healthcare-specific terms.

Rule-Based NLP Logic
The script uses custom regular expressions and substitution rules to support:

-Grammar refinement
-Medical term translation
-Jargon removal
-Readability improvements

This version does not require a machine learning model or external API, ensuring fast, offline usage and transparency.
---
## Example Output
Original: The patient was diagnosed with hypertension and requires antihypertensive therapy.
Simplified: The patient is diagnosed with high blood pressure.

Original: The treatment should be initiated in order to ameliorate the patient's condition.
Simplified: The treatment should be started to improve the patient's condition.

---
## Future Enhancements

-Azure Text Analytics API integration for dynamic term recognition
-GUI or web form interface for real-time EHR text simplification
-Flesch-Kincaid readability scoring and feedback

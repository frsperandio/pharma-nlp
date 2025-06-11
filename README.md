# Pharma NLP

A Natural Language Processing (NLP) pipeline for pharmacovigilance, focusing on adverse drug reactions. The project includes named entity recognition, severity classification, explanation generation, and clinical text summarization.

## Features

- 🧠 Named Entity Recognition (NER) for symptoms and medications  
- ⚠️ Severity classification of clinical reports  
- 💬 Explanation generation for model decisions  
- 📝 Summarization of clinical narratives  
- 📚 Integration with ANVISA's drug database and ICD-10 code tables

## Project Structure

```
.
├── app/                  # Entry-point for running the app
├── core/                 # Core logic for classification, extraction, explanation, summarization
├── data/                 
│   ├── inputs/           # ANVISA dataset and ICD-10 CSVs
│   └── lookup/           # Lookup tables for drug names and adverse reactions
├── notebooks/            # Exploratory Jupyter notebooks
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (excluded via .gitignore)
└── .gitignore            # Git ignore file
```

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/pharma-nlp.git
cd pharma-nlp

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

## How to Run

```bash
# Run the main script
streamlit run app/main.py
```

You may need to configure your environment variables in the `.env` file.

## Data Sources

- ANVISA Open Drug Registry (`DADOS_ABERTOS_MEDICAMENTOS.csv`)
- ICD-10 code tables
- Custom curated lists of drug names and adverse reactions

## License

This project is licensed under the MIT License.

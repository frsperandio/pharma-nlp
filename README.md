# Pharma NLP

A Natural Language Processing (NLP) pipeline for pharmacovigilance, focusing on adverse drug reactions. The project includes named entity recognition, severity classification, explanation generation, and clinical text summarization.

## Features

- 🧠 Named Entity Recognition (NER) for symptoms and medications  
- ⚠️ Severity classification of clinical reports  
- 💬 Explanation generation for model decisions  
- 📝 Summarization of clinical narratives  
- 📚 Integration with ANVISA's drug database and ICD-10 code tables

## Examples

Here are some example inputs and outputs from the pipeline:

### Example 1
**Clinical Note:**  
> "O paciente apresentou tontura e náusea após tomar Losartana por três dias."

- **Medications Detected:** Losartana  
- **Symptoms Detected:** tontura, náusea  
- **Severity Classification:** Leve  
- **Explanation:** Sintomas comuns e autolimitados, sem risco imediato à vida.  
- **Summary:** Paciente apresentou sintomas leves após uso de Losartana.

---

### Example 2  
**Clinical Note:**  
> "Após iniciar o tratamento com Amoxicilina, o paciente desenvolveu erupções cutâneas e dificuldade para respirar."

- **Medications Detected:** Amoxicilina  
- **Symptoms Detected:** erupções cutâneas, dificuldade para respirar  
- **Severity Classification:** Grave  
- **Explanation:** Indícios de possível reação anafilática, requer intervenção médica imediata.  
- **Summary:** Reação alérgica grave observada após administração de Amoxicilina.

---

### Example 3  
**Clinical Note:**  
> "Uso prolongado de Ibuprofeno resultou em dor abdominal e sangue nas fezes."

- **Medications Detected:** Ibuprofeno  
- **Symptoms Detected:** dor abdominal, sangue nas fezes  
- **Severity Classification:** Moderada  
- **Explanation:** Potencial sinal de sangramento gastrointestinal induzido por AINEs.  
- **Summary:** Sintomas moderados relacionados ao uso prolongado de Ibuprofeno.

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

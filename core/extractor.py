import spacy
from spacy.pipeline import EntityRuler
import os

# Carrega o spaCy e adiciona regras de medicamentos e reações adversas
def load_nlp_with_matchers():
    nlp = spacy.blank("pt")  # pipeline leve

    # Carrega lista de medicamentos
    med_path = os.path.join("data", "lookup", "nomes_medicamentos_anvisa.txt")
    with open(med_path, encoding="utf-8") as f:
        med_nomes = [line.strip() for line in f if line.strip()]

    # Carrega lista de reações adversas
    reac_path = os.path.join("data", "lookup", "reacoes_adversas.txt")
    with open(reac_path, encoding="utf-8") as f:
        reac_nomes = [line.strip() for line in f if line.strip()]

    # EntityRuler para medicamentos
    #med_ruler = nlp.add_pipe("entity_ruler", name="med_ruler", config={"overwrite_ents": True})
    med_ruler = nlp.add_pipe("entity_ruler", name="med_ruler", config={"phrase_matcher_attr": "LOWER"})

    med_patterns = [{"label": "MEDICAMENTO", "pattern": nome} for nome in med_nomes]
    med_ruler.add_patterns(med_patterns)

    # EntityRuler para reações adversas
    #reac_ruler = nlp.add_pipe("entity_ruler", name="reac_ruler", config={"overwrite_ents": False})
    reac_ruler = nlp.add_pipe("entity_ruler", name="reac_ruler", config={"phrase_matcher_attr": "LOWER"})

    reac_patterns = [{"label": "REACAO", "pattern": nome} for nome in reac_nomes]
    reac_ruler.add_patterns(reac_patterns)

    return nlp

# Carrega modelo uma vez
nlp_model = load_nlp_with_matchers()

def extract_entities(text):
    doc = nlp_model(text)

    medicamentos = [ent.text for ent in doc.ents if ent.label_ == "MEDICAMENTO"]
    reacoes = [ent.text for ent in doc.ents if ent.label_ == "REACAO"]

    return {
        "medicamento": medicamentos[0] if medicamentos else None,
        "sintomas": reacoes
    }
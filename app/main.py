import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import json
from core.extractor import extract_entities
from core.classifier import classify_severity
from core.summarizer import generate_summary
from core.explainer import explain_decision

st.set_page_config(page_title="Analisador de Reações Adversas", layout="centered")

st.title("💊 Analisador de Reações Adversas com LLM")

st.markdown("Insira abaixo o relato textual do paciente:")

user_input = st.text_area("Relato do Paciente", height=200, placeholder="Digite ou cole o relato do paciente aqui...")

if st.button("Analisar"):
    if user_input.strip():
        with st.spinner("Processando..."):

            entities = extract_entities(user_input)
            severity, justification = classify_severity(user_input)
            summary = generate_summary(user_input, entities, severity, justification)

            output = {
                "medicamento": entities["medicamento"],
                "sintomas": entities["sintomas"],
                "gravidade": severity,
                "justificativa": justification,
                "resumo": summary
            }

        st.success("Análise concluída!")
        st.subheader("📋 Resultado Estruturado")
        st.json(output)

    else:
        st.warning("Por favor, insira um relato antes de clicar em 'Analisar'.")
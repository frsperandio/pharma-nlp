import os
from dotenv import load_dotenv
from openai import OpenAI
import re

def classify_severity(text):
    load_dotenv(override=True)
    openai_api_key = os.getenv("OPENAI_API_KEY")

    '''
    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set")
        return None, None
    '''

    system_prompt = (
        "Você é um classificador de gravidade de reações adversas a medicamentos.\n"
        "Sua tarefa é classificar o texto fornecido como 'leve', 'moderada' ou 'grave',\n"
        "com uma explicação curta justificando a decisão.\n"
        "Sempre responda no seguinte formato:\n"
        "Classificação: <leve|moderada|grave>\n"
        "Justificativa: <explicação curta>\n\n"
        "Exemplos:\n"
        "Texto: 'O paciente teve dor de cabeça leve e passageira.'\n"
        "Classificação: leve\n"
        "Justificativa: sintomas leves e autolimitados.\n\n"
        "Texto: 'O paciente teve reações alérgicas graves com fechamento da glote.'\n"
        "Classificação: grave\n"
        "Justificativa: risco de morte imediato.\n\n"
        "Texto: 'O paciente teve tontura e queda ao levantar, precisou de observação médica.'\n"
        "Classificação: moderada\n"
        "Justificativa: sintomas mais relevantes, com necessidade de cuidados.\n"
    )

    openai = OpenAI()

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Texto: {text}\nClassificação:"}
        ]
    )

    response = completion.choices[0].message.content

    # Regex para extrair classificação e justificativa
    classification_match = re.search(r"Classificação:\s*(\w+)", response, re.IGNORECASE)
    justification_match = re.search(r"Justificativa:\s*(.+)", response, re.IGNORECASE)

    classification = classification_match.group(1).strip() if classification_match else None
    justification = justification_match.group(1).strip() if justification_match else None

    return classification, justification
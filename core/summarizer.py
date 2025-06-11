import os
from dotenv import load_dotenv
from openai import OpenAI

def generate_summary(text, entities, severity, justification):
    load_dotenv(override=True)
    openai_api_key = os.getenv("OPENAI_API_KEY")

    '''
    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set")
        return None
    '''    

    system_prompt = (
        "Você é um assistente que gera resumos clínicos com base em relatos de reações adversas a medicamentos.\n"
        "Dado um relato do paciente, uma lista de entidades extraídas (medicamentos e sintomas) e a classificação da gravidade (leve, moderada, grave),\n"
        "gere um resumo claro e objetivo que ajude profissionais de saúde a entender o caso rapidamente.\n"
        "Inclua os medicamentos envolvidos, os sintomas descritos e destaque a gravidade da situação.\n"
        "Use frases curtas, linguagem técnica acessível e tom informativo.\n"
    )

    user_message = (
        f"Relato: {text}\n"
        f"Entidades: {entities}\n"
        f"Gravidade: {severity}\n"
        f"Justificativa: {justification}\n"
        f"Gere um resumo clínico:"
    )

    openai = OpenAI()

    completion = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )

    return completion.choices[0].message.content
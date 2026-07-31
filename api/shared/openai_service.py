from openai import AzureOpenAI
import os
import json

from shared.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT
)

def get_client():
    return AzureOpenAI(
        api_key=AZURE_OPENAI_KEY,
        azure_endpoint=AZURE_OPENAI_ENDPOINT,
        api_version="2024-12-01-preview"
    )

def create_embedding(text: str):
    client = get_client()
    response = client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return response.data[0].embedding

def ask_gpt(context, question):
    client = get_client()
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful research paper assistant. "
                    "Answer ONLY using the provided context. "
                    "If the answer is not found in the context, reply "
                    "'I couldn't find that information in the uploaded paper.'"
                )
            },
            {
                "role": "user",
                "content": f"""
                            Context:
                            {context}

                            Question:
                            {question}
                            """
            }
        ],
        max_completion_tokens=500
    )

    return response.choices[0].message.content

def summarize_paper(context):
    client = get_client()
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a research paper assistant. Summarize the following document in exactly 5 concise bullet points."
                )
            },
            {
                "role": "user",
                "content": context
            }
        ],
        max_completion_tokens=1200
    )

    print(response)

    print("Message:")
    print(response.choices[0].message)

    return response.choices[0].message.content

def generate_quiz(context):
    client = get_client()
    response = client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {
                "role": "system",
                "content": (
                    "Generate exactly 5 multiple-choice questions "
                    "from the given document.\n\n"
                    "Return ONLY valid JSON in this format:\n"
                    "{\n"
                    '  "questions":[\n'
                    "    {\n"
                    '      "question":"...",\n'
                    '      "options":["...","...","...","..."],\n'
                    '      "answer":"..."\n'
                    "    }\n"
                    "  ]\n"
                    "}\n\n"
                    "Do not include markdown or explanations."
                )
            },
            {
                "role": "user",
                "content": context
            }
        ],
        max_completion_tokens=1500
    )

    return response.choices[0].message.content
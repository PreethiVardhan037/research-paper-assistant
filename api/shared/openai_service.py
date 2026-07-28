from openai import AzureOpenAI
import os

from shared.config import (
    AZURE_OPENAI_ENDPOINT,
    AZURE_OPENAI_KEY,
    AZURE_OPENAI_EMBEDDING_DEPLOYMENT
)

client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    azure_endpoint=AZURE_OPENAI_ENDPOINT,
    api_version="2024-12-01-preview"
)

def create_embedding(text: str):
    response = client.embeddings.create(
        model=AZURE_OPENAI_EMBEDDING_DEPLOYMENT,
        input=text
    )

    return response.data[0].embedding

def ask_gpt(context, question):
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
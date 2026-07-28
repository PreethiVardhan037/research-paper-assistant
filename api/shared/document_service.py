from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient

from shared.config import (
    DOCUMENT_INTELLIGENCE_ENDPOINT,
    DOCUMENT_INTELLIGENCE_KEY
)

client = DocumentIntelligenceClient(
    endpoint=DOCUMENT_INTELLIGENCE_ENDPOINT,
    credential=AzureKeyCredential(DOCUMENT_INTELLIGENCE_KEY)
)

def extract_text(file_bytes: bytes) -> str:
    poller = client.begin_analyze_document(
        "prebuilt-read",
        body=file_bytes
    )

    result = poller.result()

    text = []

    text = []

    for i, page in enumerate(result.pages):
        print(f"Page {i+1}: {len(page.lines)} lines")

        for line in page.lines:
            text.append(line.content)

    print("Total pages:", len(result.pages))

    return "\n".join(text)
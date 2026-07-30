from azure.core.credentials import AzureKeyCredential
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents import SearchClient
from azure.search.documents.indexes.models import (
    SearchIndex,
    SearchField,
    SearchFieldDataType,
    SimpleField,
    SearchableField,
    VectorSearch,
    HnswAlgorithmConfiguration,
    VectorSearchProfile
)
from .openai_service import create_embedding
from azure.search.documents.models import VectorizedQuery
import uuid
import os

endpoint = os.getenv("SEARCH_ENDPOINT")
key = os.getenv("SEARCH_KEY")

search_client = SearchClient(
    endpoint=endpoint,
    index_name="research-papers",
    credential=AzureKeyCredential(key)
)

index_client = SearchIndexClient(
    endpoint=endpoint,
    credential=AzureKeyCredential(key)
)

def create_index_if_not_exists():
    index_name = "research-papers"

    indexes = [index.name for index in index_client.list_indexes()]

    if index_name in indexes:
        print("Index already exists.")
        return

    fields = [
        SimpleField(
            name="id",
            type=SearchFieldDataType.String,
            key=True
        ),

        SearchableField(
            name="filename",
            type=SearchFieldDataType.String
        ),

        SearchableField(
            name="content",
            type=SearchFieldDataType.String
        ),

        SearchField(
            name="embedding",
            type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
            searchable=True,
            vector_search_dimensions=1536,
            vector_search_profile_name="vector-profile"
        )
    ]

    vector_search = VectorSearch(
        algorithms=[
            HnswAlgorithmConfiguration(name="hnsw")
        ],
        profiles=[
            VectorSearchProfile(
                name="vector-profile",
                algorithm_configuration_name="hnsw"
            )
        ]
    )

    index = SearchIndex(
        name=index_name,
        fields=fields,
        vector_search=vector_search
    )

    index_client.create_index(index)

    print("Index created successfully.")

def clear_index():

    results = search_client.search(
        search_text="*",
        select=["id"],
        top=1000
    )

    documents = []

    for result in results:

        documents.append({
            "id": result["id"]
        })

    if documents:

        search_client.delete_documents(documents=documents)

        print(f"Deleted {len(documents)} documents.")

    else:

        print("Index already empty.")

def index_chunks(filename, chunks):
    documents = []

    for chunk in chunks:
        embedding = create_embedding(chunk)

        documents.append({
            "id": str(uuid.uuid4()),
            "filename": filename,
            "content": chunk,
            "embedding": embedding
        })

    result = search_client.upload_documents(documents)

    print(f"Uploaded {len(result)} documents")

def search_similar_chunks(question, top_k=3):
    embedding = create_embedding(question)

    vector_query = VectorizedQuery(
        vector=embedding,
        k_nearest_neighbors=top_k,
        fields="embedding"
    )

    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=["content"]
    )

    chunks = []

    for result in results:
        chunks.append(result["content"])

    context = "\n\n".join(chunks)

    return context


def get_all_chunks():
    results = search_client.search(
        search_text="*",
        select=["content"],
        top=100
    )

    chunks = []

    for result in results:
        chunks.append(result["content"])

    context = "\n\n".join(chunks)

    print("Number of chunks:", len(chunks))
    print("Context length:", len(context))
    print(context[:300])

    return context


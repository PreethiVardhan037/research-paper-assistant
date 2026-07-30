import json
import logging
import azure.functions as func
from shared.blob_service import upload_pdf,clear_container
from shared.document_service import extract_text
from shared.openai_service import create_embedding
from shared.chunk_service import chunk_text
from shared.search_service import (
    create_index_if_not_exists,
    clear_index,
    index_chunks,
    search_similar_chunks
)


def upload(req: func.HttpRequest) -> func.HttpResponse:

    logging.info("Received upload request")

    try:

        file = req.files.get("file")

        if file is None:

            return func.HttpResponse(

                json.dumps({

                    "success": False,

                    "message": "No PDF uploaded."

                }),

                mimetype="application/json",

                status_code=400

            )

        pdf_bytes = file.read()

        create_index_if_not_exists()

        clear_index()

        clear_container()
        
        blob_url = upload_pdf(
            file.filename,
            pdf_bytes
        )

        text = extract_text(pdf_bytes)

        print(f"PDF Bytes: {len(pdf_bytes)}")
        print("Extracted text:", len(text))

        chunks = chunk_text(text)

        print(len(chunks))

        index_chunks(file.filename, chunks)

        logging.info(file.filename)

        logging.info(len(pdf_bytes))

        return func.HttpResponse(
            json.dumps({
                "success": True,
                "filename": file.filename,
                "blobUrl": blob_url,
                "text": text[:1000]
            }),
            mimetype="application/json"
        )

    except Exception as e:

        logging.exception(e)

        return func.HttpResponse(

            json.dumps({

                "success": False,

                "message": str(e)

            }),

            mimetype="application/json",

            status_code=500

        )
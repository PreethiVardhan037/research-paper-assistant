import json
import logging

import azure.functions as func


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

        logging.info(file.filename)

        logging.info(len(pdf_bytes))

        return func.HttpResponse(

            json.dumps({

                "success": True,

                "filename": file.filename,

                "size": len(pdf_bytes)

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
import azure.functions as func
import datetime
import json
import logging

app = func.FunctionApp()

@app.route(route="upload", auth_level=func.AuthLevel.ANONYMOUS)
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

        if not file.filename.lower().endswith(".pdf"):

            return func.HttpResponse(
                json.dumps({
                    "success": False,
                    "message": "Only PDF files are allowed."
                }),
                mimetype="application/json",
                status_code=400
            )

        pdf_bytes = file.read()

        logging.info(f"Filename : {file.filename}")
        logging.info(f"Size : {len(pdf_bytes)} bytes")

        return func.HttpResponse(

            json.dumps({

                "success": True,

                "filename": file.filename,

                "size": len(pdf_bytes)

            }),

            mimetype="application/json",

            status_code=200

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
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="summary", auth_level=func.AuthLevel.ANONYMOUS)
def summary(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="ask", auth_level=func.AuthLevel.ANONYMOUS)
def ask(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="quiz", auth_level=func.AuthLevel.ANONYMOUS)
def quiz(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )

@app.route(route="sections", auth_level=func.AuthLevel.ANONYMOUS)
def sections(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
import azure.functions as func

from shared.blob_service import get_current_paper_name
import json


def current_paper(req: func.HttpRequest) -> func.HttpResponse:
    try:
        filename = get_current_paper_name()

        return func.HttpResponse(
            body=json.dumps({
                "filename": filename,
                "uploaded" : True,
            }),
            mimetype="application/json",
            status_code=200
        )


    except Exception as e:
        return func.HttpResponse(
            body=str(e),
            status_code=500
        )
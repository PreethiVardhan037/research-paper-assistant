import azure.functions as func

from shared.search_service import get_all_chunks
from shared.openai_service import summarize_paper


def summary(req: func.HttpRequest):

    try:
        context = get_all_chunks()

        summary = summarize_paper(context)

        return func.HttpResponse(
            summary,
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
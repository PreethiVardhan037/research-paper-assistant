import azure.functions as func

from shared.search_service import search_similar_chunks
from shared.openai_service import ask_gpt


def ask(req: func.HttpRequest):

    try:
        body = req.get_json()

        question = body["question"]

        context = search_similar_chunks(question)

        answer = ask_gpt(context, question)

        return func.HttpResponse(
            answer,
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
import azure.functions as func

from shared.search_service import get_all_chunks
from shared.openai_service import generate_quiz


def quiz(req: func.HttpRequest):

    try:
        context = get_all_chunks()

        quiz_json = generate_quiz(context)

        quiz_json = quiz_json.replace("```json", "").replace("```", "").strip()

        return func.HttpResponse(
            quiz_json,
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            str(e),
            status_code=500
        )
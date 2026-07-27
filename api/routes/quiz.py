import azure.functions as func


def quiz(req: func.HttpRequest):

    return func.HttpResponse("Quiz endpoint")
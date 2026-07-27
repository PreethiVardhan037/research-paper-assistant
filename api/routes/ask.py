import azure.functions as func


def ask(req: func.HttpRequest):

    return func.HttpResponse("Ask endpoint")
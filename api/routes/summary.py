import azure.functions as func


def summary(req: func.HttpRequest):

    return func.HttpResponse("Summary endpoint")
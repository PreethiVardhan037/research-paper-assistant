import azure.functions as func


def sections(req: func.HttpRequest):

    return func.HttpResponse("Sections endpoint")
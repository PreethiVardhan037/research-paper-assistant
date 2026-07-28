import azure.functions as func

from routes.upload import upload
from routes.summary import summary
from routes.ask import ask
from routes.quiz import quiz
from routes.sections import sections


app = func.FunctionApp()


app.route(
    route="upload",
    auth_level=func.AuthLevel.ANONYMOUS
)(upload)

app.route(
    route="summary",
    auth_level=func.AuthLevel.ANONYMOUS
)(summary)

app.route(
    route="ask",
    auth_level=func.AuthLevel.ANONYMOUS
)(ask)

app.route(
    route="quiz",
    auth_level=func.AuthLevel.ANONYMOUS
)(quiz)

app.route(
    route="sections",
    auth_level=func.AuthLevel.ANONYMOUS
)(sections)


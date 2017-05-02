from apistar import App
from project.routes import routes
from project.settings import settings

app = App(routes=routes, settings=settings)

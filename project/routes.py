from apistar import Route
from project.views import attempts, welcome

routes = [
    Route('/', 'GET', welcome),
    Route('/attempts/', 'GET', attempts)
]

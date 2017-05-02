from apistar import Route
from project.views import attempts, welcome, teachers_list

routes = [
    Route('/', 'GET', welcome),
    Route('/attempts/', 'GET', attempts),

    Route('/teachers/', 'GET', teachers_list),
]

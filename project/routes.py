from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes

from project.views import attempts, welcome, add_teacher, teachers_list


routes = [
    Route('/', 'GET', welcome),
    Route('/attempts/', 'GET', attempts),

    Route('/teachers/', 'GET', teachers_list),
    Route('/teachers/', 'POST', add_teacher),
    Include('/docs', docs_routes),
    Include('/static', static_routes),
]

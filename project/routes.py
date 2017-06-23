from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes

from project.views import attempts, welcome, add_teacher, delete_teacher, teacher_details, teachers_list


routes = [
    Route('/', 'GET', welcome),
    Route('/attempts/', 'GET', attempts),

    Route('/teachers/', 'GET', teachers_list),
    Route('/teachers/', 'POST', add_teacher),
    Route('/teacher/{teacher_id}/', 'GET', teacher_details),
    Route('/teacher/{teacher_id}/', 'DELETE', delete_teacher),
    Include('/docs', docs_routes),
    Include('/static', static_routes),
]

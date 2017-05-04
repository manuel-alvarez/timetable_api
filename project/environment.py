from apistar import environment, schema


class Env(environment.Environment):
    properties = {
        'DEBUG': schema.Boolean(default=False),
        'DATABASE_URL': schema.String(default='sqlite:///timetable.db'),
        'ATTEMPTS': schema.Integer(default=1)
    }

env = Env()

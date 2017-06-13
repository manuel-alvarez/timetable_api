from apistar import schema


class TeacherSerializer(schema.Object):
    properties = {
        'id': schema.Integer,
        'name': schema.String,
    }
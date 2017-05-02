from apistar.settings import Settings


def welcome():
    return {'message': 'Welcome to API Star!'}


def attempts(settings: Settings):
    return {'attempts': settings['ATTEMPTS']}

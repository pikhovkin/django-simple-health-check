class BaseHealthCheck(object):
    def __init__(self, **options):
        ...

    def check(self):
        raise NotImplementedError
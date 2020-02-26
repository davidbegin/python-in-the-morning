import bobo

@bobo.query('/')
def hello(person="Begin"):
    return 'Hello %s!' % person

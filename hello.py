from os import environ


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text-plain')])
    print(environ['QUERY_STRING'])
    return [bytes(i + '\n', 'ascii') for i in environ['QUERY_STRING'].split('&')]

# test

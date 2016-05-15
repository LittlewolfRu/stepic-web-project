
def hello_app(env, start_response):
    body = [
        '%s=%s\n' % (key, value) for key, value in env.items()
    ]
    status = '200 OK'
    response_headers = [('Content-Type', 'text/plain')]

    start_response(status, response_headers)
    return body
        

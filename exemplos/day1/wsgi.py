# callable - função(..) , obj(..), (lambda)(..)
# environ, callback (start_response)
# return iteravel

def application(environ,start_response):
    # montar o response
    status = "200 OK"
    headers = [("Content-type", "text/html")]
    body = b"<strong>Hello World!!!</strong>"
    start_response(status, headers)
    return [body]

# if __name__ == "__main__":
#     from wsgiref.simple_server import make_server
#     server = make_server("0.0.0.0", 8000, application)
#     server.serve_forever()

def application(environ, start_response):
  body = b'Beeplaw Chaudary is third gender\n'
  status = '200 OK'
  header = [('Content-type' , 'text/plain')]
  start_response(status, headers)
  return [body]

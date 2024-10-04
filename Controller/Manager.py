
from Falconapp.App import DynamicRoute,falcon1
from Services.Service import post_service, get_service, get_email_service


@falcon1.route('/hello')
class Demo:
    def on_post(req,res):
       post_service(req,res)

    def on_get(request,response):
        get_service(response)


@falcon1.route('/hello/email')
class Demo1:
    def on_get(request,response):
       get_email_service(request,response)


if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.make_server('localhost', 8000, falcon1.app)
    httpd.serve_forever()
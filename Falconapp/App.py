
import falcon

class DynamicRoute:
    def __init__(self,app):
        self.app=app

    def route(self,path):
        def decorator(resource):
            self.app.add_route(path,resource)
            return resource
        return decorator


app=falcon.App()
falcon1=DynamicRoute(app)

# demo=Demo()
# app.add_route('/hello',demo)
# app.add_route('/hello/email',demo,suffix='email')


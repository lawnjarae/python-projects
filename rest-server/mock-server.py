import time
import web

class MyApplication(web.application):
    def run(self, port=8080, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

urls = (
    '/', 'index',
    '/sleep', 'sleep',
    '/thread', 'thread'
)

class index:
    def GET(self):
        output = "Available endpoints:\n" \
                "/ - outputs this explaination\n" \
                "/sleep - will sleep for 5 seconds and return a 200\n"
        return output

class sleep:
    def GET(self):
        time.sleep(5)
        return "Sleep for 5 seconds"


if __name__ == "__main__":
    app = MyApplication(urls, globals())
    app.run(port=3030)

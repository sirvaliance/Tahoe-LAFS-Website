import os
import logging
import uuid
import datetime
import re

import tornado.ioloop
import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    pass


class MainHandler(BaseHandler):

    def get(self):
        self.render("main.html")


class Application(tornado.web.Application):

    def __init__(self):
        handlers = [
            (r"/", MainHandler),

        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            cookie_secret="",
            debug=True
        )

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    application = Application()
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

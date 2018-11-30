import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        html=''''''
        for i in range(1, 10):
            for j in range(1, i+1):
                m='{}x{}={}\t'.format(j, i, i*j)
                html+=m
            html+="<br>"

        self.write(html)

class ABCHandler(tornado.web.RequestHandler):
    def get(self,m):
        html=''''''
        if int(m)<10:
            for i in range(1, int(m)+1):
                for j in range(1, i+1):
                    m='{}x{}={}\t'.format(j, i, i*j)
                    html+=m
                html+="<br>"
            self.write(html)
        else:
            self.write("请输入一个不超过9的正整数")


application = tornado.web.Application([
    (r"/", MainHandler),
    (r"/([0-9]+)", ABCHandler),
],debug=True)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()

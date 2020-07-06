import web

render = web.template.render('views')

class Alumnos:
    def GET(self):

        raise web.seeother('/static/index.html')

        try:
            return render.index()
        except Exception as e:
            return "Error "+str(e.args)

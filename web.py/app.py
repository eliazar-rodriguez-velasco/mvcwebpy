import web

urls = (
    '/', 'controllers.alumnos.Alumnos'
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
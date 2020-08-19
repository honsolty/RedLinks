from logic import post, get, web


def init():
    app = web.Application()
    app.router.add_get('/visited_links', post)
    app.router.add_get('/visited_domains', get)
    return app


app = init()
web.run_app(app)
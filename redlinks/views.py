import redis
from .red import add_link_to_db, get_link_from_db


def post_link(request):
    print(request)
    try:
        links = request.query['address']
    except Exception:
        links = request['address']

    add_link_to_db(links)


def get_link(request):
    try:
        f = int(request.query['from'])
        t = int(request.query['to'])
    except Exception:
        f = int(request['from'])
        t = int(request['to'])

    print(redis.Redis().zrange("links", 0, -1))
    response = get_link_from_db(f, t)

    return response
import redis
from red import add_link_to_db, get_link_from_db


def post_link(request):
    print(request)
    links = request.query['address']
    add_link_to_db(links)


def get_link(request):
    f = int(request.query['from'])
    t = int(request.query['to'])

    print(redis.Redis().zrange("links", 0, -1))
    response = get_link_from_db(f, t)

    return response
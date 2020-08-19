import time
import redis
# from custom_errors import LinkError


def add_link_to_db(links):
    for link in links.replace(' ', '').split(','):
        if link.count('.') != 1:
            print('oh')
            # raise LinkError(link)
        print("Address:", link, "Time:", str(int(time.time() * 1000)))
        redis.Redis().zadd("links", {link: str(int(time.time() * 1000))})


def get_link_from_db(f, t):
    response = {"status": "ok", "domains": []}
    for site in redis.Redis().zrangebyscore("links", f, t + 1):
        if site.decode("utf-8") not in response["domains"]:
            response['domains'].append(site.decode("utf-8"))
    return response
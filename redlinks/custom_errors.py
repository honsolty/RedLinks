class LinkError(Exception):
    def __init__(self, link):
        self.message = f"address '{link}' is wrong"

    def __str__(self):
        return self.message
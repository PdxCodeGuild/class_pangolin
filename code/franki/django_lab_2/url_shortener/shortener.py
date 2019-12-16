import random
import string


class Shortener:
    token_size = 6
    
    def __init__(self, token_size=None):
        self.token_size = token_size if token_size is not None else 5

    def issue_token(self):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for i in range(self.token_size))
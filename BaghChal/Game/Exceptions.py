
class InvalidMove(Exception):
    """excecption describes an invalid move in the game"""
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
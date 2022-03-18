class Split:
    def __init__(self, type):
        self.type = type
        self._share = None

    def set_share(self, share):
        self._share = share

    def get_share(self):
        return self._share

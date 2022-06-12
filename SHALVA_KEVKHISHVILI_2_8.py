class Building:
    def init(self, location, price, story):
        self._location = location
        self._price = price
        self._story = story

    @property
    def price(self):
        return self.price

    @price.setter
    def price(self, p):
        self._price = p

    def print_info(self):
        print(self._location, self._price, self._story)

    def gt(self, other):
        return self._story > other._story

    def lt(self, other):
        return self._story < other._story
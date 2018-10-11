class Player:
    name = 'Spike'
    coin = 1000
    dragons_killed = 0

    def __repr__(cls):
        stats = f"Name: {cls.name}\n"
        stats += f"Coin: {cls.coin}\n"
        stats += f"Dragons Killed: {cls.dragons_killed}\n"
        return stats

    class __metaclass__(type):
        @property
        def name(cls):
            return cls.name
        
        @property
        def coin(cls):
            return cls.coin

        @property
        def dragons_killed(cls):
            return cls.dragons_killed

        @name.setter
        def name(cls, name):
            cls.name = name

        @coin.setter
        def coin(cls, coin):
            cls.coin = coin

        @dragons_killed.setter
        def dragons_killed(cls, dk):
            cls.dragons_killed = dk
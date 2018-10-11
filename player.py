class Player:
    name = 'Spike'
    coin = 1000
    dragons_killed = 0

    @classmethod
    def __repr__(cls):
        stats = f"Name: {cls.name}\n"
        stats += f"Coin: {cls.coin}\n"
        stats += f"Dragons Killed: {cls.dragons_killed}\n"
        return stats

    @classmethod
    def set_name(cls, name):
        cls.name = name

    @classmethod
    def set_coin(cls, coin):
        cls.coin = coin

    @classmethod
    def set_dragons_killed(cls, dk):
        cls.dragons_killed = dk
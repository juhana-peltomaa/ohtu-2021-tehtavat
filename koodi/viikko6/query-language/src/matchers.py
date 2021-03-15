class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False

        return True


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def matches(self, player):
        return player.team == self._team


class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value


class All:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        if player:
            return True
        else:
            return False


class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return player_value < self._value


class Not:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return True

        return False


class Or:
    def __init__(self, *matchers):
        self._matchers = matchers

    def matches(self, player):
        for matcher in self._matchers:
            if matcher.matches(player):
                return True

        return False


class QueryBuilder:
    def __init__(self):
        self._kysely = []

    def build(self):
        rakennettava = And(*self._kysely)
        self._kysely = []
        return rakennettava

    def playsIn(self, team):
        self._kysely.append(PlaysIn(team))
        return self

    def hasAtLeast(self, value, attr):
        self._kysely.append(HasAtLeast(value, attr))
        return self

    def hasFewerThan(self, value, attr):
        self._kysely.append(HasFewerThan(value, attr))
        return self

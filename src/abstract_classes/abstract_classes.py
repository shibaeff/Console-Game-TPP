"""
    This module sets character types
"""
common_params = ["name", "reputation", "leadership", "possessions"]


class AbsCharacter():
    pos_name = "Abstract Character"

    def __init__(self, name, leadership,
                 reputation, possessions):
        assert valid_args(name, leadership, reputation, possessions)
        self._name = name
        self._leadership = leadership
        self._reputation = reputation
        self._possessions = possessions
        # self._pos_name = "Abs Character"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def reputation(self):
        return self._reputation

    @reputation.setter
    def reputation(self, val):
        self._reputation = val

    @property
    def leadership(self):
        return self._leadership

    @leadership.setter
    def leadership(self, val):
        self._leadership = val

    @property
    def possessions(self):
        return self._possessions

    @possessions.setter
    def possessions(self, val):
        self._possessions = val

    def __str__(self):
        return type(self).pos_name


class AbsTech(AbsCharacter):
    pos_name = "Abstract Character"

    def __init__(self, name, leadership, reputation, tech_vision, possesisons):
        assert valid_args(name, leadership, reputation, possesisons, tech_vision)
        AbsCharacter.__init__(self, name, leadership, reputation, possesisons)
        self._tech_vision = tech_vision

    @property
    def tech_vision(self):
        return self._tech_vision

    @tech_vision.setter
    def tech_vision(self, val):
        self._tech_vision = val


class AbsManager(AbsCharacter):
    pos_name = "Abstract Manager"

    def __init__(self, name, leadership, reputation,
                 team_work, organization, possessions):
        assert valid_args(name, leadership, reputation,
                          possessions, organization, team_work)

        AbsCharacter.__init__(self, name, leadership, reputation, possessions)
        self._pos_name = "AbsManager"
        self._team_work = team_work
        self._organization = organization

    @property
    def team_work(self):
        return self._team_work

    @team_work.setter
    def team_work(self, val):
        self._team_work = val

    @property
    def organization(self):
        return self._organization

    @organization.setter
    def organization(self, val):
        self._organization = val


def valid_args(*args):
    for arg in args:
        if arg is None:
            return False
    return True


from src.abstract_classes import abstract_classes as ac

manager_params = ["team_work", "organization"]


class LegalOff(ac.ac.AbsManager):
    pos_name = "Legal Officer"
    skill_name = "legal"

    def __init__(self, name, leadership, reputation,
                 team_work, organization, legal, possessions):
        ac.AbsManager.__init__(self, name, leadership, reputation,
                            team_work, organization, possessions)
        self._legal = legal

    @property
    def legal(self):
        return self._legal

    @legal.setter
    def legal(self, val):
        self._legal = val


class AnalyticsOff(ac.AbsManager):
    pos_name = "Analytics Officer"
    skill_name = "analytics"

    def __init__(self, name, leadership, reputation,
                 team_work, organization, analytics, possessions):
        ac.AbsManager.__init__(self, name, leadership, reputation,
                            team_work, organization, possessions)
        self._analytics = analytics

    @property
    def analytics(self):
        return self._analytics

    @analytics.setter
    def analytics(self, val):
        self._analytics = val


class FinancialOff(ac.AbsManager):
    pos_name = "Financial officer"
    skill_name = "financial"

    def __init__(self, name, leadership, reputation,
                 team_work, organization, financial, possessions):
        ac.AbsManager.__init__(self, name, leadership, reputation,
                            team_work, organization, possessions)
        self._financial = financial

    @property
    def financial(self):
        return self._financial

    @financial.setter
    def financial(self, val):
        self._financial = val


manager_classes_list = [AnalyticsOff, FinancialOff, LegalOff]

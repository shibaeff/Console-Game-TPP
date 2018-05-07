from src.abstract_classes import abstract_classes as tc


class DataOff(tc.AbsTech):
    pos_name = "Data Officer"
    skill_name = "data"

    def __init__(self, name, leadership, reputation,
                 tech_vision, data, possessions):
        tc.AbsTech.__init__(self, name, leadership, reputation,
                         tech_vision, possessions)
        self._data = data

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, val):
        self._data = val


class SecurityOff(tc.AbsTech):
    pos_name = "Security Officer"
    skill_name = "security"

    def __init__(self, name, leadership, reputation,
                 tech_vision, security, possessions):
        tc.AbsTech.__init__(self, name, leadership, reputation,
                         tech_vision, possessions)
        self._security = security

    @property
    def security(self):
        return self._security

    @security.setter
    def data(self, val):
        self._security = val


class ResearchOff(tc.AbsTech):
    pos_name = "Research Officer"
    skill_name = "research"

    def __init__(self, name, leadership, reputation,
                 tech_vision, research, possessions):
        tc.AbsTech.__init__(self, name, leadership, reputation,
                         tech_vision, possessions)
        self._research = research

    @property
    def research(self):
        return self._research

    @research.setter
    def research(self, val):
        self._research = val


class WebOff(tc.AbsTech):
    pos_name = "Web Officer"
    skill_name = "web"

    def __init__(self, name, leadership, reputation,
                 tech_vision, web, possessions):
        tc.AbsTech.__init__(self, name, leadership, reputation,
                         tech_vision, possessions)
        self._web = web

    @property
    def web(self):
        return self._web

    @web.setter
    def data(self, val):
        self._web = val

tech_classes_list = [WebOff, SecurityOff, DataOff, ResearchOff]
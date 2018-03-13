from numpy import random as rand
import random

deck_size = 6
"""int: The size of the deck in the games
Can be used in the models importing this
"""


# Card Classes
class AbstractCharCard():
    """
    Every Character Card in the game matches
    this pattern. Currently there are two types
    of characters: Managerial Executives and Technical ones.
    """

    def __init__(self, name=None, soft_skills=None, reputation=None,
                 pos_short=None, position=None):
        """
        soft_skills -- employee soft skills esitmate (0-10)
        leadership  -- employee leadership est (0-10)
        pos_short   --  position's abbrev
        position     -- position's full name
        """
        self.name = name
        self.soft_skills = soft_skills
        self.reputation = reputation
        self.pos_short = pos_short
        self.position = position

    def __str__(self):
        return "{} {}-{} at pos {}".format(self.name, self.soft_skills,
                                           self.reputation, self.pos_short)


class ManagerCard(AbstractCharCard):
    def __init__(self, name=None, soft_skills=None, managerial=None,
                 reputation=None, pos_short=None, position=None):
        """
        soft_skills -- employee soft skills estimate (0-10)
        leadership  -- employee leadership est (0-10)
        managerial  -- managerial est (0-10)
        pos_short   -- position's abbrev
        position_full     -- position's full name
        """
        self.managerial = managerial
        AbstractCharCard.__init__(self, name, soft_skills,
                                  reputation, pos_short, position)

    def __str__(self):
        return "manager {} {}-{}-{} at position {}({})".\
            format(self.name,
                   self.soft_skills,
                   self.managerial,
                   self.reputation,
                   self.position,
                   self.pos_short)


class TechCard(AbstractCharCard):
    def __init__(self, name=None, soft_skills=None, tech=None,
                 reputation=None, pos_short=None, position=None):
        """
        soft_skills -- employee soft skills estimate (0-10)
        leadership  -- employee leadership est (0-10)
        tech        -- tech est (0-10)
        pos_short   -- position's abbrev
        position_full     -- position's full name
        """
        self.tech = tech
        AbstractCharCard.__init__(self, name, soft_skills,
                                  reputation, pos_short, position)

    def __str__(self):
        return "tech {} {}-{}-{} at position {}({})".format(self.name,
                                                            self.soft_skills,
                                                            self.tech,
                                                            self.reputation,
                                                            self.position,
                                                            self.pos_short)


# Factories to generate manager and tech folks stuff
# Card can be created either manually with custom parameters
# or can be randomly generated. Manual creation relies on additional parameters
class AbsCardFactory():
    def create_manager(self):
        pass

    def create_tech(self):
        pass


class CustomFactory(AbsCardFactory):
    def create_manager(self, name, soft_skills, managerial,
                       reputation, pos_short, position):
        """All arguments have to be passed"""
        return ManagerCard(name, soft_skills, managerial,
                           reputation, pos_short, position)

    def create_tech(self, name, soft_skills, tech,
                    reputation, pos_short, position):
        """All arguments have to be passed"""
        return TechCard(name, soft_skills, tech,
                        reputation, pos_short, position)


class RandomFactory(AbsCardFactory):
    @staticmethod
    def gen_parameters(pos_type=None):
        name = ResDumper.get_rand_string_from_file("./res/first-names.txt") + \
               " " + ResDumper.get_rand_string_from_file("./res/Surnames.txt")
        soft_skills = random.randrange(0, 10)
        spec = random.randrange(0, 10)
        reputation = random.randrange(0, 10)
        position = ""
        if pos_type == "man":
            position = ResDumper.\
                get_rand_string_from_file("./res/managerial.txt")
        if pos_type == "tech":
            position = ResDumper.\
                get_rand_string_from_file("./res/tech.txt")
        pos = "".join([word[0] for word in position.split()]).upper()
        return name, soft_skills, spec, reputation, pos, position

    def create_manager(self):
        return ManagerCard(*RandomFactory.gen_parameters("man"))

    def create_tech(self):
        return TechCard(*RandomFactory.gen_parameters("tech"))


class ResDumper:
    @staticmethod
    def get_rand_string_from_file(path):
        dump = list(open(path, "r"))
        return rand.choice(dump).strip("\n")

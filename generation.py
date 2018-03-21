import builders
from random import randint
from numpy.random import choice
from abstract_classes import common_params
from manager_classes import  manager_params
from manager_classes import manager_classes_list
from tech_classes import tech_classes_list

skill_upper_bound = 11


class Pool:
    """
    This class creates a set of cards for the player to choose from
    """
    @staticmethod
    def skill_val():
        return randint(0, skill_upper_bound)

    @staticmethod
    def gen_random(pos_type):
        name = ResDumper.get_rand_string_from_file("./res/first-names.txt") + \
               " " + ResDumper.get_rand_string_from_file("./res/Surnames.txt")
        leadership, reputation = Pool.skill_val(), Pool.skill_val()

        if pos_type == "manager":
            char_class = choice(manager_classes_list)
            man_builder = builders.AbsManagerBuilder(char_class)
            man_builder.set_to_obj("_name", name)
            man_builder.set_to_obj("_leadership", leadership)
            man_builder.set_to_obj("_reputation", reputation)
            for param in manager_params:
                man_builder.set_to_obj("_" + param, Pool.skill_val())
            man_builder.set_to_obj("_"+char_class.pos_name, Pool.skill_val())
            man_builder.set_to_obj("_possessions", None)
            return man_builder.return_obj()

        if pos_type == "tech":
            char_class = choice(tech_classes_list)
            tech_builder = builders.AbsTechBuilder(char_class)
            tech_builder.set_to_obj("_name", name)
            tech_builder.set_to_obj("_leadership", leadership)
            tech_builder.set_to_obj("_reputation", reputation)
            tech_builder.set_to_obj("_tech_vision", Pool.skill_val())
            tech_builder.set_to_obj("_" + char_class.pos_name, Pool.skill_val())
            tech_builder.set_to_obj("_possessions", None)
            return tech_builder.return_obj()
        return None

    @staticmethod
    def gen_pool(managers, tech):
        pool = []
        for i in range(managers):
            pool.append(Pool.gen_random("manager"))
        for i in range(tech):
            pool.append(Pool.gen_random("tech"))
        return pool


class ResDumper:
    @staticmethod
    def get_rand_string_from_file(path):
        dump = list(open(path, "r"))
        return choice(dump).strip("\n")
import character_classes as cl
from numpy import random


class Singleton(type):
    """
    A standard singleton metaclass
    """

    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class Pool(metaclass=Singleton):
    """
    We have a unique pool in the beginning of the game.
    Pool is a randomly generated diverse collection of
    card. Player is to choose 5 characters for the deck
    """
    # cards are retrived from cards fabric with random parameters
    def __init__(self):
        self.__pool_list = []
        self.__generate_pool_list()

    def get_pool_list(self):
        """
        Returns:
             a generated list of cards
        """
        return self.__pool_list

    def __generate_pool_list(self):
        """
        creates a random factory to generate a pool of size 18
        Returns:
            nothing
        """
        manager_number = random.choice([3, 4])  # number of managers
        tech_number = cl.deck_size - manager_number
        rfactory = cl.RandomFactory()
        self.__pool_list.extend([rfactory.create_manager()
                                for i in range(3 * manager_number)])
        self.__pool_list.extend([rfactory.create_tech()
                                 for i in range(3 * tech_number)])

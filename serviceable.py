from abc import ABCMeta, abstractmethod
from typing import List
"""@Interface"""


class Serviceable(ABCMeta):
    __metaclass__ = ABCMeta
    @abstractmethod
    def needs_service(self):
        pass
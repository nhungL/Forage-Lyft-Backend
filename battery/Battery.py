from abc import ABCMeta, abstractmethod
from typing import List
"""@Interface"""

class Battery(ABCMeta):
	__metaclass__ = ABCMeta
	@abstractmethod
	def needs_service(self):
		pass

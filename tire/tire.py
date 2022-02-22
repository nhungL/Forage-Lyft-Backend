from abc import ABCMeta, abstractmethod
"""@Interface"""

class Tire(ABCMeta):
	__metaclass__ = ABCMeta
	@abstractmethod
	def needs_service(self):
		pass
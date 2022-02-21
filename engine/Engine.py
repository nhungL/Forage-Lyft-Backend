from abc import ABCMeta, abstractmethod
"""@Interface"""

class Engine(ABCMeta):
	__metaclass__ = ABCMeta
	@abstractmethod
	def needs_service(self):
		pass

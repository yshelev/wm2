from abc import ABC, abstractmethod


class ReportPrinter(ABC):
	"""
	Abstract ReportPrinter class
	to create ReportPrinter class just inherit from this class and implement print method
	"""
	@abstractmethod
	def print(self):
		raise NotImplementedError()
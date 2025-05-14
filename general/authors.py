from abc import ABC, abstractmethod

from .models import UserReport


class ReportAuthor(ABC):
	"""
	Abstract ReportAuthor class
	to create ReportAuthor class just inherit from this class and implement create_report method
	"""
	@abstractmethod
	def create_report(self, data) -> list[UserReport]:
		raise NotImplementedError()
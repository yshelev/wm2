from typing import Generator, Type

from general.authors import ReportAuthor
from .models import UserReport, PayoutReport


class PayoutReportAuthor(ReportAuthor):
	"""
	custom ReportAuthor class for payout report model
	"""
	def create_report(self, data_generators: list[Type[Generator]]) -> list[PayoutReport]:
		"""
		create payout report list from many files
		:param data_generators: data generators from files
		:return:
		"""
		output = []
		for gen in data_generators:
			output += self._create_report(gen)

		return output

	def _create_report(self,
	                   data_generator: Type[Generator]) -> list[PayoutReport]:
		"""
		create payout report list from one file
		:param data_generator: data from files
		:return:
		"""
		output_data = []
		headers = next(data_generator)

		headers = headers.replace("salary", "rate").replace("hourly_rate", "rate").strip().split(",")

		while True:
			try:
				row = next(data_generator).strip().split(",")
			except StopIteration:
				break

			output_data_row = {
				headers[i]: row[i] for i in range(len(headers))
			}
			output_data.append(PayoutReport(**output_data_row)) # можем отлавливать ошибку из PayoutReport'a если данные
																# невалидны, но в задаче они валидны всегда (и соответственно
																# рейзить ошибку из PayoutReport'a.

		return output_data


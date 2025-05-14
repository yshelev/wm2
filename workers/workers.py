import os
from typing import Generator


class EmptyInputDataException(Exception):
	pass


class CsvFileWorker:
	"""
	class to parse files by lines
	"""
	PATH = "data/csv/"

	def _get_data_from_file(self,
	                        filename: str):
		"""
		parse FILE by lines
		:param filename:
		:return:
		"""
		absolute_path = os.path.abspath(self.PATH + filename)
		try:
			with open(absolute_path, "r") as f:
				while a := f.readline():
					yield a
		except FileNotFoundError:
			raise FileNotFoundError()


	def get_data_from_files(self,
	                        filenames: list[str]) -> list[Generator]:
		"""
		parse files by lines each
		:param filenames:
		:return:
		"""

		data = []
		for filename in filenames:
			try:
				data.append(self._get_data_from_file(filename))
			except FileNotFoundError:
				print(f"file with filename {filename} not found in directory {self.PATH}. file will be ignored.")
		if len(data) > 0:
			return data

		raise EmptyInputDataException("You must pass filename of at least one non empty file in argv")
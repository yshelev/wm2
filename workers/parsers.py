import argparse

from workers.workers import EmptyInputDataException


class ArgParser:
	"""
	ArgParser class parse args by using argparse library
	"""

	def __init__(self):
		self._parser = argparse.ArgumentParser()

	def parse(self) -> tuple[list[str], str]:
		"""
		parse input args
		:return: filenames, report_type
		"""
		self._parser.add_argument("filenames",
		                          nargs="+")
		self._parser.add_argument("--report",
		                          "-r")

		args = self._parser.parse_args()

		if len(args.filenames) > 0:
			return (args.filenames,
			        args.report)

		raise EmptyInputDataException("You must pass filename of at least one non empty file in argv")

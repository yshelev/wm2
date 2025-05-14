from payout.printers import ReportPrinter
from payout.authors import ReportAuthor
from workers.workers import CsvFileWorker


class Chooser:
	"""
	a class that performs the main functions of a program
	"""
	def __init__(self,
	             printer_class: ReportPrinter.__class__,
	             author_class: ReportAuthor.__class__):
		"""
		init Chooser object
		:param printer_class: class for writing report to terminal
		:param author_class: class for create report
		"""
		self._printer_class = printer_class
		self._author_class = author_class
		self._file_worker = CsvFileWorker()


	def main(self,
	         filenames) -> None:
		"""
		main function of program
		:param filenames: filenames of input files
		:return:
		"""
		data = self._file_worker.get_data_from_files(filenames)

		author = self._author_class()
		reports = author.create_report(data)

		printer = self._printer_class(reports)
		printer.print()
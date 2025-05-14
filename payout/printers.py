from general.printers import ReportPrinter
from .models import PayoutReport


class PayoutReportPrinter(ReportPrinter):
	"""
	custom report printer for payout model
	"""
	DEPARTMENT_SPACE = 10
	NAME_SPACE = 20
	HOURS_SPACE = 8
	RATE_SPACE = 8
	PAYOUT_SPACE = 10

	def __init__(self, data: list[PayoutReport]):
		"""
		:param data: payout reports list
		"""
		self._data = data

	def print(self):
		"""
		print payout reports in terminal sorting them by department first
		:return:
		"""
		self._data.sort(key=lambda report: report.department)

		cur_output = []

		self._print_headers()
		prev_department = None

		for row in self._data:
			if row.department != prev_department:
				self._print_department_row(cur_output)
				self._print_department_name(row.department)
				prev_department = row.department
				cur_output = []
			else:
				cur_output.append(row)

		self._print_department_row(cur_output)


	def _print_headers(self):
		header_string = (f"{self.DEPARTMENT_SPACE * " "}name{(self.NAME_SPACE - 4) * " "}"
		                 f"hours{(self.HOURS_SPACE - 5) * " "}"
		                 f"rate{(self.RATE_SPACE - 5) * " "}"
		                 f"payout{(self.PAYOUT_SPACE - 6) * " "}")
		print(header_string)

	def _print_department_name(self,
	                           department_name):
		print(department_name)

	def _print_department_row(self,
	                           department_rows):
		if not department_rows:
			return
		sum_hours = 0
		sum_payout = 0

		for row in department_rows:
			row_string = (f"{self.DEPARTMENT_SPACE * "-"}{row.name}{(self.NAME_SPACE - len(row.name)) * " "}"
		                 f"{row.hours_worked}{(self.HOURS_SPACE - len(str(row.hours_worked))) * " "}"
		                 f"{row.rate}{(self.RATE_SPACE - len(str(row.rate)) - 1) * " "}"
		                 f"${row.payout}{(self.PAYOUT_SPACE - len(str(row.payout))) * " "}")
			sum_hours += row.hours_worked
			sum_payout += row.payout
			print(row_string)

		print(
			(f"{(self.DEPARTMENT_SPACE + self.NAME_SPACE) * " "}"
             f"{sum_hours}{(self.HOURS_SPACE - len(str(sum_hours))) * " "}"
             f"{(self.RATE_SPACE - 1) * " "}"
             f"${sum_payout}{(self.PAYOUT_SPACE - len(str(sum_payout))) * " "}")
		)
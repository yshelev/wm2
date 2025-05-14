from workers.Chooser import Chooser
from workers.parsers import ArgParser
from general.settings import report_type_dict, DEFAULT_TYPE

def main():
	"""
	parse args, invoke report type to Author and Printer then hand over control to Chooser
	:return:
	"""

	filenames, report_type = ArgParser().parse()
	report_type = report_type or DEFAULT_TYPE
	if not report_type in report_type_dict:
		raise ValueError(f"Не существует отчета с типом {report_type}")

	Chooser(*report_type_dict[report_type]).main(filenames)

if __name__ == "__main__":
	main()
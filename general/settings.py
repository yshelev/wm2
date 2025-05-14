"""
project settings / constant variables
"""


from payout.authors import PayoutReportAuthor
from payout.printers import PayoutReportPrinter

report_type_dict = {
	"payout": [PayoutReportPrinter,
	            PayoutReportAuthor]
}

DEFAULT_TYPE = "payout"
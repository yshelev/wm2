import pytest

from payout.authors import PayoutReportAuthor
from workers.parsers import ArgParser

@pytest.fixture()
def arg_parser():
	return ArgParser()

@pytest.fixture(scope="module")
def payout_author():
	return PayoutReportAuthor()

def payout_data_generator():
	data = ["id,email,name,department,hours_worked,hourly_rate",
	"1,alice@example.com,Alice Johnson,Marketing,160,50"]
	for i in data:
		yield i

def payout_data_generator2():
	data = ["department,id,email,name,hours_worked,rate",
	"HR,101,grace@example.com,Grace Lee,160,45",
	"Marketing,102,henry@example.com,Henry Martin,150,35"]
	for i in data:
		yield i
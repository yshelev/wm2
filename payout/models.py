from general.models import UserReport


class PayoutReport(UserReport):
	"""
	custom UserReport
	"""
	hours_worked: int
	rate: int
	payout: int
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.hours_worked = int(kwargs.get("hours_worked"))
		self.rate = int(kwargs.get("rate"))
		self.payout = self.rate * self.hours_worked
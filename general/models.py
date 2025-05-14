from dataclasses import dataclass


@dataclass
class UserReport:
	"""
	default UserReport model.
	to create custom report model inherit from this class.
	"""
	def __init__(self,
	             **kwargs):
		self.id = int(kwargs.get("id"))
		self.email = kwargs.get("email")
		self.name = kwargs.get("name")
		self.department = kwargs.get("department")
	id: int
	email: str
	name: str
	department: str
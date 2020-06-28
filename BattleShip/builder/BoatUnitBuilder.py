import arcade
from base.Unit import Unit
from builder.UnitBuilder import UnitBuilder

class BoatUnitBuilder(UnitBuilder):
	def __init__(self):
		super().__init__()
		self._contents = []

	def add_sprite(self):
		self._contents.append("pic/boat.png")

	def add_cost(self):
		self._contents.append(100)

	def add_hp(self):
		self._contents.append(1000)

	def add_damage(self):
		self._contents.append(100)

	def add_blow_damage(self):
		self._contents.append(50)

	def add_consumption(self):
		self._contents.append(1200)

	def get_unit(self) -> Unit:
		return Unit(self._contents)
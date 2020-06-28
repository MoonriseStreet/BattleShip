import arcade
from base.Unit import Unit
from builder.UnitBuilder import UnitBuilder

class Player(object):
	def __init__(self):
		self.builder: UnitBuilder

	def set_builder(self, builder: UnitBuilder):
		self.builder = builder

	def clone(self) -> Unit:
		self.builder.add_sprite()
		self.builder.add_cost()
		self.builder.add_hp()
		self.builder.add_damage()
		self.builder.add_blow_damage()
		self.builder.add_consumption()
		return self.builder.get_unit()

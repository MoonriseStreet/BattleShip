import arcade

class Unit(object):
	def __init__(self, components: list()):
		self._components = components
		self.fighter = arcade.Sprite(components[0])
		self.cost = components[1]
		self.hp = components[2]
		self.damage = components[3]
		self.blow_damage = components[4]
		self.consumption = components[5]

	def __repr__(self):
		return self._components
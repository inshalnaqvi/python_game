class Settings:
	"""A class to store all settings of alien invasion"""

	def __init__(self):
		"""Initializethe game's setting"""
		#Screen settings
		self.screen_width = 1200
		self.screen_height = 800

		self.bg_color = (230, 230, 230)

		#ship settings
		self.ship_speed = 1.5
from serviceable import Serviceable
import engine.Engine as Engine
import battery.Battery as Battery

class Car(Serviceable, Engine, Battery):
	def __init__(self, engine, battery):
		self.___engine : Engine = None
		self.___battery : Battery = None

	def needs_service(self):
		return Engine.needs_service() or Battery.needs_service()
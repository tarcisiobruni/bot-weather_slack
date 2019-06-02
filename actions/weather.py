from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet
from apixu.client import ApixuClient

class ActionWeather(Action):
	def name(self):
		return 'action_weather'


	def run(self, dispatcher, tracker, domain):

		api_key = 'api_key'
		client = ApixuClient(api_key)

		loc = tracker.get_slot('location')
		current = client.current(q=loc)

		country = current['location']['country']
		city = current['location']['name']
		condition = current['current']['condition']['text']
		temperature_c = current['current']['temp_c']
		humidity = current['current']['humidity']
		wind_mph = current['current']['wind_mph']

		response = """It is currently {} in {} at the moment.
				The temperature is {} degrees, the humidity is {}% ^ the wind speed is {} mph.""".format(condition, city, temperature_c, humidity, wind_mph)

		dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

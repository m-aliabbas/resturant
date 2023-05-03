from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionConfirmPizzaOrder(Action):
    def name(self) -> Text:
        return "utter_confirm_pizza_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        pizza_type = tracker.get_slot("pizza_type")
        pizza_size = tracker.get_slot("pizza_size")
        dispatcher.utter_message(text=f"Got it! You've ordered a {pizza_size} {pizza_type} pizza. Would you like to add anything else?")
        return []

class ActionConfirmDrinkOrder(Action):
    def name(self) -> Text:
        return "utter_confirm_drink_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        drink = tracker.get_slot("drink")
        dispatcher.utter_message(text=f"Alright! We've added a {drink} to your order. Anything else?")
        return []

class ActionConfirmAddress(Action):
    def name(self) -> Text:
        return "utter_confirm_address"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        address = tracker.get_slot("address")
        dispatcher.utter_message(text=f"Thank you for providing your address: {address}. Your order will be delivered there.")
        return []

class ActionProvideDeliveryTime(Action):
    def name(self) -> Text:
        return "utter_provide_delivery_time"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="The estimated delivery time is 30-45 minutes. Enjoy your meal!")
        return []

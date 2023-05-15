from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionShowMenu(Action):
    def name(self) -> Text:
        return "action_show_menu" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cuisine =  tracker.get_slot("cuisine") or ''
        latest_message = tracker.latest_message
        entities = latest_message.get("entities", [])
        intent = latest_message.get("intent", {}).get("name")

        if intent == 'select_cuisine':
            cuisine = entities[0]['value']
        print(f"----------------- {intent}-------------------------------")
        
        if cuisine != '':
            dispatcher.utter_message(text=f"You have selected {cuisine}")
            return [SlotSet("cuisine", cuisine)]
        return []
    
class ActionMakeOrder(Action):
    def name(self) -> Text:
        return "action_make_order" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        existing_food_order= tracker.get_slot("food_order") or []
        
        latest_message = tracker.latest_message

        # Retrieving the entities from the latest message
        entities = latest_message.get("entities", [])
        intent = latest_message.get("intent", {}).get("name")
        print(f"----------------- {intent}-------------------------------")
        print(existing_food_order)
        food_order= existing_food_order
        if intent == 'order_food':
            print(entities)
            if len(entities)>0:
                for entity in entities:
                    food_order += [entity['value']]
                    food_order.append(entity['value'])
            food_order += existing_food_order
            dispatcher.utter_message(text=f"You have selected {food_order} from food order")
            return [SlotSet("food_order", food_order)]
        return []

class ActionMakeOrder(Action):
    def name(self) -> Text:
        return "action_make_order" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        existing_food_order= tracker.get_slot("food_order") or []
        
        latest_message = tracker.latest_message

        # Retrieving the entities from the latest message
        entities = latest_message.get("entities", [])
        intent = latest_message.get("intent", {}).get("name")
        print(f"----------------- {intent}-------------------------------")
        print(existing_food_order)
        food_order= existing_food_order
        if intent == 'order_food':
            print(entities)
            if len(entities)>0:
                for entity in entities:
                    food_order += [entity['value']]
                    food_order.append(entity['value'])
            food_order += existing_food_order
            dispatcher.utter_message(text=f"You have selected {food_order} from food order")
            return [SlotSet("food_order", food_order)]
        return []

class ActionAddAddress(Action):
    def name(self) -> Text:
        return "action_add_address" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text=f"You have added address")
        return []
    
class ActionAddBurger(Action):
    def name(self) -> Text:
        return "action_add_burger" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"You have added burger")
        return []
    

class ActionAddDessert(Action):
    def name(self) -> Text:
        return "action_add_dessert" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"You have added sandwich")
        return []
    
class ActionAddDrink(Action):
    def name(self) -> Text:
        return "action_add_drink" 

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text=f"You have added drink")
        return []
# class ActionConfirmPizzaOrder(Action):
#     def name(self) -> Text:
#         return "utter_confirm_pizza_order"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         pizza_type = tracker.get_slot("pizza_type")
#         pizza_size = tracker.get_slot("pizza_size")
#         dispatcher.utter_message(text=f"Got it! You've ordered a {pizza_size} {pizza_type} pizza. Would you like to add anything else?")
#         return []

# class ActionConfirmDrinkOrder(Action):
#     def name(self) -> Text:
#         return "utter_confirm_drink_order"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         drink = tracker.get_slot("drink")
#         dispatcher.utter_message(text=f"Alright! We've added a {drink} to your order. Anything else?")
#         return []

# class ActionConfirmAddress(Action):
#     def name(self) -> Text:
#         return "utter_confirm_address"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         address = tracker.get_slot("address")
#         dispatcher.utter_message(text=f"Thank you for providing your address: {address}. Your order will be delivered there.")
#         return []

# class ActionProvideDeliveryTime(Action):
#     def name(self) -> Text:
#         return "utter_provide_delivery_time"

#     def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         dispatcher.utter_message(text="The estimated delivery time is 30-45 minutes. Enjoy your meal!")
#         return []

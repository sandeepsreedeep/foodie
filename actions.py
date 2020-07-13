# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormAction
import zomatopy
import json
result_g = ""
import smtplib
from email.message import EmailMessage

class RestaurantSearchForm(FormAction):

    def name(self):
        return "restaurant_search_form"

    @staticmethod
    def required_slots(tracker):
        return ['location', 'price', 'cuisine']

    def slot_mappings(self):
        return {
                'location' : self.from_entity(entity = 'location', intent = ['location', 'restaurant_search']),
                'price' : self.from_entity(entity = 'price', intent = ['inform_price', 'restaurant_search']),
                'cuisine' : self.from_entity(entity = 'cuisine', intent = ['inform_cusine', 'restaurant_search']),
                }

    def submit(self, dispatcher, tracker, domain):
        config={ "user_key":"4d7466cbf52f6f0656f7c1261ba73801"}
        zomato = zomatopy.initialize_app(config)
        cities = [
        'ahmedabad', 'bangalore', 'chennai', 'delhi', 'hyderabad', 'kolkata' , 'mumbai', 'pune', 'agra', 'ajmer', 'aligarh',
        'amravati', 'amritsar', 'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi', 'bhopal', 'bhubaneswar',
        'bikaner', 'bilaspur', 'bokaro steel city', 'chandigarh', 'coimbatore', 'cuttack', 'dehradun', 'dhanbad', 'bhilai', 'durgapur',
        'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga', 'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur',
        'hubli–dharwad', 'indore', 'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi', 'jodhpur', 'kakinada',
        'Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura',
        'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nagpur', 'nanded', 'nashik', 'nellore', 'noida', 'patna', 'pondicherry', 'purulia',
        'prayagraj', 'raipur', 'rajkot', 'rajahmundry', 'ranchi', 'rourkela', 'ralem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar',
        'surat', 'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur', 'vadodara', 'varanasi', 'vasai-virar city',
        'vijayawada', 'visakhapatnam', 'vellore', 'warangal'
        ]
        loc = tracker.get_slot('location')
        if loc.lower() in cities:
            cuisine = tracker.get_slot('cuisine')
            price = tracker.get_slot('price')


            location_detail=zomato.get_location(loc, 1)
            d1 = json.loads(location_detail)
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
            city_ID = d1['location_suggestions'][0]['city_id']
            cuisines_dict= {'Chinese':25, 'American':1, 'Italian':55, 'Mexican':73, 'North Indain':50, 'South Indian':85}
            response=""
            response_p=""
            ctr = 1
            iter = True
            st = 0
            for each in range(21):
                results = zomato.restaurant_search_mod("", lat, lon, str(cuisines_dict.get(cuisine)), city_ID,10,each*20)
                d = json.loads(results)
                if d :
                    if d['results_found'] == 0:
                        response= "no results"
                    else:
                        if price == 'low':
                            for restaurant in d['restaurants']:
                                if restaurant['restaurant']['average_cost_for_two'] < 300:
                                    if ctr <= 10:
                                        response=response+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                        ctr+=1
                                    if ctr <= 5:
                                        response_p = response_p+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                    if ctr >10:
                                        break
                        if price == 'mid':
                            for restaurant in d['restaurants']:
                                if (restaurant['restaurant']['average_cost_for_two'] > 300) and (restaurant['restaurant']['average_cost_for_two']) < 700:
                                    if ctr <= 10:
                                        response=response+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                        ctr+=1
                                    if ctr <= 5:
                                        response_p = response_p+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                    if ctr >10:
                                        break
                        if price == 'high':
                            for restaurant in d['restaurants']:
                                if restaurant['restaurant']['average_cost_for_two'] > 700:
                                    if ctr <= 10:
                                        response=response+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                        ctr+=1
                                    if ctr <= 5:
                                        response_p = response_p+ "\nFound "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+"average_cost_for_two : " +str(restaurant['restaurant']['average_cost_for_two'])+"\n"+"Zomato User Rating : " +str(restaurant['restaurant']['user_rating']['aggregate_rating'])
                                    if ctr >10:
                                        break
                            # else:
                            #     response= "Sorry there were no search results!!"
            if response != "":
                dispatcher.utter_message(response_p)
            else:
                dispatcher.utter_message("Sorry there were no search results")
            global result_g
            result_g = response
            return []
        else:
            dispatcher.utter_message("Sorry!! we do not operate in that area yet")
            return []



class ActionSentMail(Action):

    def name(self):
        return "action_sent_mail"

    def run(self, dispatcher, tracker, domain):
        # print(result_g)
        password = '<password>'
        my_email = '<your_email_id>'
        _mail_id = tracker.get_slot('email_id')
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(my_email, password)
            # dispatcher.utter_message(_mail_id)

            subject = 'Foodie Search Results'
            msg = (f'Subject: {subject}\n\n{result_g}').encode('ascii', 'ignore')
            smtp.sendmail(my_email, _mail_id, msg)
            print(_mail_id)


        return [SlotSet('email_id',_mail_id)]

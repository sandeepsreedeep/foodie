## happy path form
* greet
  - utter_greet
* restaurant_search{"location": "Ernakulam"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* affirm{"response": "yes"}
  - slot{"response": "yes"}
  - utter_ask_email
* sent_mail{"email_id": "testing123@gmail.com"}
  - slot{"email_id": "testing123@gmail.com"}
  - action_sent_mail
  - utter_goodbye

## happy path form no mail
* greet
  - utter_greet
* restaurant_search{"location": "Ernakulam"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* deny{"response": "no"}
  - slot{"response": "no"}
  - utter_goodbye


## happy path form 2
* restaurant_search{"location": "Ernakulam"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* affirm{"response": "yes"}
  - slot{"response": "yes"}
  - utter_ask_email
* sent_mail{"email_id": "testing123@gmail.com"}
  - slot{"email_id": "testing123@gmail.com"}
  - action_sent_mail
  - utter_goodbye

## happy path form 2 no mail
* restaurant_search{"location": "Ernakulam"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* deny{"response": "no"}
  - slot{"response": "no"}
  - utter_goodbye

## happy path form 3
* restaurant_search{"price": "low"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* affirm{"response": "yes"}
  - slot{"response": "yes"}
  - utter_ask_email
* sent_mail{"email_id": "testing123@gmail.com"}
  - slot{"email_id": "testing123@gmail.com"}
  - action_sent_mail
  - utter_goodbye

## happy path form 3 no mail
* restaurant_search{"price": "low"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* deny{"response": "no"}
  - slot{"response": "no"}
  - utter_goodbye

## happy path form 4
* restaurant_search{"cuisine": "North Indian"}
  - restaurant_search_form
  - form{"name" : "restaurant_search_form"}
  - form{"name":"null"}
  - utter_forward
* affirm{"response": "yes"}
  - slot{"response": "yes"}
  - utter_ask_email
* sent_mail{"email_id": "testing123@gmail.com"}
  - slot{"email_id": "testing123@gmail.com"}
  - action_sent_mail
  - utter_goodbye


## interactive_story_1
* restaurant_search{"location": "ernakulam"}
    - slot{"location": "ernakulam"}
    - restaurant_search_form
    - form{"name" : "restaurant_search_form"}
    - form{"name":"null"}
    - utter_forward
  * affirm{"response": "yes"}
    - slot{"response": "yes"}
    - utter_ask_email
  * sent_mail{"email_id": "testing123@gmail.com"}
    - slot{"email_id": "testing123@gmail.com"}
    - action_sent_mail
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "price"}
* form: inform_price{"price": "low"}
    - slot{"price": "low"}
    - form: restaurant_search_form
    - slot{"price": "low"}
    - slot{"requested_slot": "cuisine"}
* form: inform_cusine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_search_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_forward
* affirm{"location": "Yes"}
    - slot{"location": "Yes"}
    - utter_ask_email
* inform_mail{"email_id": "jj500simpsons@gyanmail.com"}
    - action_sent_mail
    - slot{"email_id": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "price"}
* form: inform_price{"price": "low"}
    - slot{"price": "low"}
    - form: restaurant_search_form
    - slot{"price": "low"}
    - slot{"requested_slot": "cuisine"}
* form: inform_cusine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_search_form
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_forward
* affirm{"location": "Yes"}
    - slot{"location": "Yes"}
    - utter_ask_email
* inform_mail{"email_id": "ggggg2221@hotmail.com"}
    - action_sent_mail
    - slot{"email_id": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "price"}
* form: inform_price{"price": "low"}
    - slot{"price": "low"}
    - form: restaurant_search_form
    - slot{"price": "low"}
    - slot{"requested_slot": "cuisine"}
* form: inform_cusine{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - form: restaurant_search_form
    - slot{"cuisine": "chinese"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_forward
* deny{"response": "No"}
    - slot{"response": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - restaurant_search_form
    - form{"name": "restaurant_search_form"}
    - slot{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - slot{"requested_slot": "location"}
* form: location{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - form: restaurant_search_form
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "price"}
* form: inform_price{"price": "high"}
    - slot{"price": "high"}
    - form: restaurant_search_form
    - slot{"price": "high"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_forward
* deny{"response": "No"}
    - slot{"response": "No"}
    - utter_goodbye

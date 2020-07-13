## intent:greet
- hey
- hello
- hi
- good morning
- good evening
- hey there

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- [yes]{"entity": "response", "value": "Yes"}
- [indeed]{"entity": "response", "value": "Yes"}
- [of course]{"entity": "response", "value": "Yes"}
- [that sounds good]{"entity": "response", "value": "Yes"}
- [correct]{"entity": "response", "value": "Yes"}
- [sure]{"entity": "response", "value": "Yes"}
- [Yes](response)

## intent:deny
- [No](response)
- [no]{"entity": "response", "value": "No"}
- [never]{"entity": "response", "value": "No"}
- [I don't think so]{"entity": "response", "value": "No"}
- [don't like that]{"entity": "response", "value": "No"}
- [no way]{"entity": "response", "value": "No"}
- [not really]{"entity": "response", "value": "No"}
- [not necessary]{"entity": "response", "value": "No"}
- [No](response)

## intent:inform_price
- [250]{"entity": "price", "value": "low"}
- [100]{"entity": "price", "value": "low"}
- [50]{"entity": "price", "value": "low"}
- [low price]{"entity": "price", "value": "low"}
- [low priced]{"entity": "price", "value": "low"}
- [low end]{"entity": "price", "value": "low"}
- [lowend]{"entity": "price", "value": "low"}
- [cheap]{"entity": "price", "value": "low"}
- [300]{"entity": "price", "value": "mid"}
- [500]{"entity": "price", "value": "mid"}
- [650]{"entity": "price", "value": "mid"}
- [mid ranged]{"entity": "price", "value": "mid"}
- [mid range]{"entity": "price", "value": "mid"}
- [midrange]{"entity": "price", "value": "mid"}
- [average]{"entity": "price", "value": "mid"}
- [700]{"entity": "price", "value": "high"}
- [750]{"entity": "price", "value": "high"}
- [800]{"entity": "price", "value": "high"}
- [2000]{"entity": "price", "value": "high"}
- [high end]{"entity": "price", "value": "high"}
- [highend]{"entity": "price", "value": "high"}
- [posh]{"entity": "price", "value": "high"}
- [pricey]{"entity": "price", "value": "high"}
- [expensive]{"entity": "price", "value": "high"}
- [200]{"entity": "price", "value": "low"}
- [low](price)
- [850]{"entity": "price", "value": "high"}
- [high](price)
- [mid](price)
- [high](price)

## intent:location
- [Mumbai](location)
- [Delhi](location)
- [Kolkata](location)
- [Chennai](location)
- [Bangalore](location)
- [Hyderabad](location)
- [Ahmedabad](location)
- [Surat](location)
- [Pune](location)
- [Kanpur](location)
- [Indore](location)
- [Jaipur](location)
- [Vadodara](location)
- [Nagpur](location)
- [Lucknow](location)
- [Patna](location)
- [Vishakapatnam](location)
- [Bhopal](location)
- [delhi](location)
- [mumbai](location)
- [bangalore](location)
- [ernakulam](location)
- [mumbai](location)

## intent:inform_cusine
- [South Indian](cuisine)
- [North Indian](cuisine)
- [Italian](cuisine)
- [American](cuisine)
- [Chinese](cuisine)
- [Mexican](cuisine)
- [Chinese]{"entity": "cuisine", "value": "chinese"}
- [chinese](cuisine)

## intent:inform_mail
- [testing123@gmail.com](email_id)
- [corey_schafer@yahoo.com](email_id)
- please send it to [anjaneyan@gmail.com](email_id)
- my email id is [sandhesh2k@hotmail.com](email_id)
- better sent it to the id [fffgavhebe@gmail.com](email_id)
- forward it to [hdgvdvssvgdsv11@gmail.com](email_id)

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- show me [chinese](cuisine) restaurants
- show me [chines]{"entity": "cuisine", "value": "chinese"} restaurants in the [New Delhi]{"entity": "location", "value": "Delhi"}
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- in [delhi](location)
- find me a [cheap]{"entity": "price", "value": "low"} restaurant
- find me an [expensive]{"entity": "price", "value": "high"} restaurant
- I am looking for [midrange]{"entity": "price", "value": "mid"} restaurant in [Mumbai](location)
- I am looking for some [cheap]{"entity": "price", "value": "low"} restaurants
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- find me restaurant that costs [300]{"entity": "price", "value": "mid"} per plate
- I am looking for a restaurant in [mumbai](location)
- i am looking for a [cheap]{"entity": "price", "value": "low"} restaurant
- find me a restaurant
- find a [cheap]{"entity": "price", "value": "low"} restaurant
- find a restaurant in [mumbai](location)
- find me an [expensive]{"entity": "price", "value": "high"} restaurant in [mumbai](location)
- find me the cheapest restaurant in [kochi](location)
- find me a [cheap]{"entity": "price", "value": "low"} restaurant in [delhi](location)
- find me a restaurant in [kochi](location)
- find me a north [indian resta]{"entity": "cuisine", "value": "north indian"}urant in [kochi](location)
- i am looking for a north indian restaurant[]{"entity": "cuisine", "value": "north indian"}

## synonym:American
- american
- america
- America

## synonym:Chinese
- chinese
- China

## synonym:Delhi
- New Delhi
- Delhi
- delhi
- NewDelhi
- new delhi
- newdelhi
- Dilli

## synonym:Italian
- italian
- italy
- Italy

## synonym:Kolkata
- kolkata
- kolkatta
- Culcutta
- culcutta
- culcuta
- Culcuta

## synonym:Mexican
- mexican
- mexicano
- Mexico
- espanol

## synonym:No
- no
- never
- I don't think so
- don't like that
- no way
- not really
- not necessary

## synonym:North Indian
- north indian
- North indian
- north Indian

## synonym:South Indian
- north
- south indian
- South indian
- south Indian

## synonym:Yes
- yes
- indeed
- of course
- that sounds good
- correct
- sure

## synonym:bangalore
- Bangalore
- bengaluru
- Bengaluru
- Bangaluru
- bangaluru
- Bengalore
- bengalore
- Bangalur
- bangalur
- Bengalur
- bengalur

## synonym:chinese
- Chinese
- chines

## synonym:high
- 700
- 750
- 800
- 2000
- high end
- highend
- posh
- pricey
- expensive
- 850

## synonym:low
- 250
- 100
- 50
- low price
- low priced
- low end
- lowend
- cheap
- 200

## synonym:mid
- 300
- 500
- 650
- mid ranged
- mid range
- midrange
- average

## synonym:mumbai
- Mumbai
- bombay
- bombei
- bombey
- mumby
- mumbye

## synonym:north indian
- indian resta

## regex:email_id
- ([a-zA-Z0-9._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)

## regex:greet
- hey[^\s]*
- hi[^\s]*

## regex:location
- [0-9]{6}

## regex:price
- [0-9]{4}

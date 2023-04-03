import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
   w = w.lower()
   if w in data:
       return data[w]
   elif w.title() in data: 
        return data[w.title()]
   elif w.upper() in data: 
        return data[w.upper()]
   elif len(get_close_matches(w, data.keys())) > 0:
      yn = input("Did you mean %s? Enter Y is Yes, or N if No: " % get_close_matches(w, data.keys()) [0])
      if yn == "Y":
         return data[get_close_matches(w, data.keys()) [0]]
      elif yn == "N":
         yn1 = input("Maybe you meant %s then? Enter Y is Yes, or N if No:" % get_close_matches(w, data.keys()) [1])
         if yn1 == "Y":
            return data[get_close_matches(w, data.keys()) [1]]
         elif yn1 =="N":
            yn2 = input("Last suggestion! Is %s the word you are looking for? Enter Y is Yes, or N if No:" % get_close_matches(w, data.keys()) [2])
            if yn2 =="Y":
               return data[get_close_matches(w, data.keys()) [2]]
            elif yn2 =="N":
               return "Really?! Well, I suppose I just don't know that word then"
            else:
               return "We didn't understand your entry"
         else:
           return "We didn't understand your entry." 
      else: 
         return "We didn't understand your entry."
   else:
      return "Word not found. Please double-check!"

word = input("Enter Word: ")

output = translate(word)

if type(output) == list:
   for item in output:
       print(item)
else:
   print(output)

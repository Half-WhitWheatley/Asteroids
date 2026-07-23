import random

insults = [
    "Git good, scrub",
    "Pathetic",
    "Dishonor on you! Dishonor on your cow!",
    "You put the Ram in Dodge.",
    "You utilize the space bar about as well as you use the space between your ears!"  
]

def get_insult():
    return random.choice(insults)
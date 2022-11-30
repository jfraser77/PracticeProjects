"""
Name: Joe Fraser
Date: 11/10/22
Description: Abruptly Goblin Planner
Opening your comic book store, the Sorcery Society, has been a lifelong dream come true. You quickly diversified your shop offerings to include miniatures, plush toys, collectible card games, and board games. Eventually, the store became more a games store with a selection of this week's newest comic books and a small offering of graphic novel paperbacks. Completing your transformation means offering space for local tabletop gamers. They love to play their favorite RPG, "Abruptly Goblins!" and will happily pay you per chair to secure the space to do it. Unfortunately, planning the game night has fallen to you. If you pick the wrong night, not enough people will come and the game night will be cancelled. You decide it's best that you automate the game night selector to get the most people through the door. First you need to create a list of people who will be attending the game night.

Instructions


"""

# Create an empty list called gamers. This will be your list of people who are attending game night.


gamers = []

form_email = "Greetings {name}! Your game night {day_of_week} for {game}"

"""
Now we want to create a function that will update this list and add a new gamer to the this gamers list. Each gamer should be a dictionary with the following keys:

"name": a string that contains the gamer's full or presumed name. E.g., "Vicky Very"
"availability": a list of strings containing the names of the days of the week that the gamer is available. E.g., ["Monday", "Thursday", "Sunday"]
Instructions

Create a function called add_gamer that takes two parameters: gamer and gamers_list. The function should check that the argument passed to the gamer parameter has both "name" and a "availability" as keys and if so add gamer to gamers_list.
"""

def add_gamer(gamer, gamers_list):
    if gamer.get("name") and gamer.get("availability"):
        gamers_list.append(gamer)
    else:
        print("Gamer does not meet name and availability format.")
    
"""
Finding the perfect availability
Now that we have a list of all of the people interested in game night, we want to be able to calculate which nights would have the most participation. First we need to create a frequency table which correlates each day of the week with gamer availability.

Instructions

Create a function called build_daily_frequency_table that takes no argument returns a dictionary with the days of the week as keys and 0s for values. We'll be using this to count the availability per night. Call build_daily_frequency_table and save the results to a variable called count_availability.
"""
def build_daily_frequency_table():
    return {"Monday": 0, "Tuesday": 0, "Wednesday": 0, "Thursday": 0, "Friday": 0, "Saturday": 0, "Sunday": 0}

"""
Next we need to count the number of people every night.

Instructions

Write a function called calculate_availability that takes a list of gamers as an argument gamers_list and a frequency table available_frequency. The function should iterate through each gamer in gamers_list and iterate through each day in the gamer's availability. For each day in the gamer's availability, add one to that date on the frequency table.
"""
def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list:
        for day in gamer["availability"]:
            available_frequency[day] +=  1

"""
Instructions

Create a function available_on_night that takes two parameters: gamers_list and day and returns a list of people who are available on that particular day.
"""
def available_on_night(gamers_list, day):
    my_list = []
    for gamer in gamers_list:
        for avail in gamer['availability']:
            if avail == day:
                my_list.append(gamer['name'])
    return my_list

"""
**Instructions**

Write a function `find_best_night` that takes a dictionary `availability_table` and returns the key with the highest number.
"""
def find_best_night(availability_table):
    best_availability = 0
    for day, availability in availability_table.items(): # Key is Day and Value is Availability
        if availability > best_availability:             # If Availability is greater than best_avail parameter
            best_night = day                             # Day will be updated best_night
            best_availability = availability             # Tracing availability to best_avail
    return best_night

"""
Instructions

Create a function send_email with three parameters: gamers_who_can_attend, day, and game. Print form_email for each gamer in gamers_who_can_attend with the appropriate day and game. Call send_email with attending_game_night, game_night, and "Abruptly Goblins!".
"""
def send_email(gamers_who_can_attend, day, game):
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day_of_week=day, game=game))


def main():

    """
    Next we want to add our first gamer! Her name is Kimberly Warner and she's available on Mondays, Tuesdays, and Fridays.

    Instructions

    Create a dictionary called kimberly with the name and availability given above.
    Call add_gamer with kimberly as the first argument and gamers as the second.
    """
    kimberly = {"name": "Kimberly Warner", "availability": ["Monday", "Tuesday", "Friday"]}
    add_gamer(kimberly, gamers)

    add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
    add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
    add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
    add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
    add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
    add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
    add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
    add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
    add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

    count_availability = build_daily_frequency_table()

    """
    Now let's use these tools to find the best night to run Abruptly Goblins!

    Instructions

    Call calculate_availability with gamers and count_availability. Print out count_availability afterwards.
    """
    calculate_availability(gamers, count_availability)

    #print(count_availability)

    game_night = "Friday"
    attending_game_night = available_on_night(gamers, game_night)
    #print(attending_game_night)

    game_night = find_best_night(count_availability)
    print(game_night)

    #send_email(attending_game_night, game_night, "Abruptly Goblins!")

    unable_to_attend_best_night = [gamer for gamer in gamers if game_night not in gamer["availability"]]

    """ for gamer in gamers:
        if game_night not in game_night['availability']:
            unable_to_attend_best_night.append(gamer) """

    print(unable_to_attend_best_night)

    second_night_availability = build_daily_frequency_table()

    calculate_availability(unable_to_attend_best_night, second_night_availability)

    second_night = find_best_night(second_night_availability)

    available_second_game_night = available_on_night(gamers, second_night)

    send_email(available_second_game_night, second_night, "Abruptly Goblins")

if __name__ == "__main__":
    main()

import time
import math
import random


number_of_players = ""
number_of_ACs = ""
number_of_mountain_sides = ""


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_text_input(input_description, valid_responses):
    while True:
        response = input(input_description).lower()
        for option in valid_responses:
            if option in response and len(option) == len(response):
                return response
        print_pause("Sorry, please enter a valid input.")

def valid_number_input(input_description, number_range):
    response = None
    while response is None:
        try:
            response = int(input(input_description))
        except ValueError:
            print("Not a number value... Please enter a valid number:") 
        while True:
            if response not in number_range:
                print("Please enter a valid number")
                response = None
            else:
                return response
            break


def games_setup():
    global number_of_players
    global number_of_ACs
    print_pause(f"Please select the number of players for this game"
                f" (max 6 players):\n")
    number_of_players = valid_number_input(f"Choose between 1 and 6 players:",
                                            range(1,7,1))
    print(f"You have chosen {number_of_players} players for this game.")
    print_pause(f"You have selected {number_of_players} players for this game.")
    max_number_of_ACs = (6 - (number_of_players))
    print_pause("Please select the number of Automatic Climbers you would like to use")
    number_of_ACs = valid_number_input(f"The maximum number of AC's you may "
                    f"use is {max_number_of_ACs}",range(0,max_number_of_ACs,1))


def color_of_players(number_of_players):
    print_pause("What color would you like your players to be?")
    players_list = []
    players = 1
    for players in range(0,(number_of_players+1),1):
        players_list.append("Player + {players}")
        players += 1


games_setup()
color_of_players(number_of_players)
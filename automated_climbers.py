import time
import math
import random


number_of_players = ""
number_of_ACs = ""
number_of_mountain_sides = ""


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def valid_text_input(text_input, valid_responses):
    while True:
        response = input(text_input).lower()
        for option in valid_responses:
            if option in response and len(option) == len(response):
                return response
        print_pause("Sorry, please enter a valid input.")

def valid_number_input(number_input, valid_responses):
    while True:
        response = int(input(number_input))
        for option in valid_responses:
            if option in response == (valid_responses):
                return response
        print_pause("Sorry, please enter a valid number.")


def games_setup():
    global number_of_players
    global number_of_ACs
    print_pause("Please select the number of players for this game:\n")
    number_of_players = valid_number_input(f"1 to 6 players allowed", [1, 2, 3, 4, 5, 6])
    max_number_of_ACs = (6 - int(number_of_players))
    print_pause("Please select the number of Automatic Climbers you would like to use")
    number_of_ACs = valid_number_input(f"The maximum number of AC's you may "
                    f"use is {max_number_of_ACs}",2)
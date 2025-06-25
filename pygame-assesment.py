# this makes it a game that opens up in a different terminal
import pygame
import sys
import json
import os
import time

pygame.init()

WIDTH, HEIGHT = 800, 600 # sets height and width of screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pathsway") # this sets the terminal name

WHITE = (255, 255, 255) # sets the colour to the word
BLACK = (0, 0, 0)
FONT = pygame.font.SysFont('Arial', 24) # sets font

# this states the story for the game
story = {
    "story_choice": {
        "text": [
            "You have three choices for a story!",
            "Do you want to go into a dungeon, circus, hospital or more choices?",
        ],
        "choice_a": "Dungeon",
        "choice_b": "Abandoned Circus",
        "choice_c": "Abandoned Hospital",
        "choice_d": "More Choices",
        "next_a": "start",
        "next_b": "start_1",
        "next_c": "start_2",
        "next_d": "more_choices"
    },
    "start": {
        "text": [
            "You are in a dungeon.",
            "Do you want to go left or right?",
        ],
        "choice_a": "Go left",
        "choice_b": "Go right",
        "next_a": "left_path",
        "next_b": "right_path"
    },
    "left_path": {
        "text": [
            "You found a door!",
            "Do you want to go open it or walk away?",
        ],
        "choice_a": "Open",
        "choice_b": "Walk away",
        "next_a": "open_door",
        "next_b": "walk_away"
    },
    "right_path": {
        "text": [
            "You found a door!",
            "Do you want to go open it or walk away?",
        ],
        "choice_a": "Open",
        "choice_b": "Walk away",
        "next_a": "open_right_door",
        "next_b": "walk_right_away"
    },
    "open_right_door": {
        "text": [
            "You found a cerberus!",
            "Do you want to keep it or walk away?",
        ],
        "choice_a": "Keep",
        "choice_b": "Walk away",
        "next_a": "keep_cerberus",
        "next_b": "walk_away_cerberus"
    },
    "walk_right_away": {
        "text": [
            "You run into a a gold chest!",
            "Do you want to open it or leave it?",
        ],
        "choice_a": "Open",
        "choice_b": "Leave it",
        "next_a": "open_chest",
        "next_b": "leave_chest"
    },
    "keep_cerberus": {
        "text": [
            "You now have a pet!",
            "Oh no!",
            "There a dragon ahead",
            "Do you want to fight it?",
        ],
        "choice_a": "Fight",
        "choice_b": "Run away",
        "next_a": "keep_cerberus_fight",
        "next_b": "run_away"
    },
    "run_away": {
        "text": [
            "You are sprinting!",
            "You climb on the cerberus back!",
            "The dragon swoops in and opens his mouth...",
            "Fire hits you and the cerberus!",
            "You have died!"
        ],
    },
    "keep_cerberus_fight": {
        "text" : [
            "Your cerberus stood in front of you!",
            "The fight has started!",
            "The cerberus leaped into the air and...",
            "Won the fight",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene"
    },
    "open_chest": {
        "text": [
            "You found treausre!",
            "Piles of gold!",
            "Oh no you activated the booby trap!",
            "It is a giant boulder",
            "Do you want to run from it or stay?",
        ],
        "choice_a": "Run",
        "choice_b": "Stay",
        "next_a": "run_from_boulder",
        "next_b": "stay"
    },
    "stay": {
        "text": [
            "The boulder is coming!",
            "Why are you still standing there move!",
            "Last chance!",
            "You died from a boulder!"
        ],
    },
    "run_from_boulder": {
        "text": [
            "You are sprinting away from the boulder!",
            "You see a door!",
            "You are nearly there!",
            "The door about to shut!",
            "You start sliding and...",
            "You made it barely!",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene"
    },
    "walk_away": {
        "text": [
            "You run into a goblin!",
            "Do you want to fight him or run from him?",
        ],
        "choice_a": "Fight",
        "choice_b": "Walk away",
        "next_a": "fight_without_sword",
        "next_b": "walk_away_left"
    },
    "walk_away_left": {
        "text": [
            "You start running!",
            "You keep running!",
            "The goblin just ate you!"
        ],
    },
    "open_door": {
        "text": [
            "You found a sword!",
            "Do you want to continue with the sword or leave it?",
            ],
        "choice_a": "Onwards with sword",
        "choice_b": "Drop the sword",
        "next_a": "goblin_fight_sword",
        "next_b": "drop_sword"
    },
    "goblin_fight_sword": {
        "text": [
            "You found a goblin!",
            "Do you want to fight with the sword or leave it?",
        ],
        "choice_a": "Fight",
        "choice_b": "Flight",
        "next_a": "fight_find_exit",
        "next_b": "flight_find_exit"
    },
    "flight_find_exit": {
        "text": [
            "You start running!",
            "You keep running!",
            "The goblin just ate you!"
        ],
    },
    "fight_find_exit": {
        "text": [
            "You won the fight!",
            "Do you want to find the exit?",
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene",
    },
    "drop_sword": {
        "text": [
            "You died!",
            "The sword landed on you!",
        ],
    },
    "find_exit_scene": {
        "text": [
            "You are looking for the exit!",
            "Do you want to use a map or walk around?",
        ],
        "choice_a": "Use map",
        "choice_b": "Walk around",
        "next_a": "exit_scene",
        "next_b": "lost_scene"
    },
    "exit_scene": {
        "text": [
            "You got the map!",
            "You are walking through the dungeon!",
            "You found the exit!",
        ],
    },
    "lost_scene": {
        "text": [
            "You start wondering around in circles!",
            "You haven't found exit yet!",
            "Oh no you have died of hunger!",
        ],
    },
    "start_1": {
        "text": [
            "You are in a abandoned circus.",
            "Do you want to go left or right?",
        ],
        "choice_a": "Go left",
        "choice_b": "Go right",
        "next_a": "left_path_circus",
        "next_b": "right_path_circus",
    },
    "left_path_circus": {
        "text": [
            "You found a a ferris wheel!",
            "Do you want to take a ride on it or walk away?",
        ],
        "choice_a": "Ride it",
        "choice_b": "Walk away",
        "next_a": "ride_ferris_wheel",
        "next_b": "walk_away_ferris_wheel",
    },
    "right_path_circus": {
        "text": [
            "You found a clown changing room!",
            "Do you want to go inside or walk away?",
        ],
        "choice_a": "Open",
        "choice_b": "Walk away",
        "next_a": "go_inside_circus",
        "next_b": "walk_right_away_circus"
    },
    "go_inside_circus": {
        "text": [
            "You found a old and creepy clown costume!",
            "Then you feel something tap on your shoulder!",
            "As you slowly turn around you see a...",
            "CLOWN!",
            "Do you want to run away from the clown or fight it?",
        ],
        "choice_a": "Fight",
        "choice_b": "Run away",
        "next_a": "fight_clown",
        "next_b": "run_away_from_clown"
    },
    "fight_clown": {
        "text": [
            "You decided to fight a clown...",
            "AMAZING IDEA!",
            "But the clown has a a a...",
            "A AXE!",
            "You have died and been hang up like a scarecrow",
        ],
    },
    "run_away_from_clown": {
        "text": [
            "You start running",
            "you are still running",
            "2 hours later!",
            "Oh no!",
            "There a mirror maze ahead",
            "Do you want to go inside or go around it?",
        ],
        "choice_a": "Enter",
        "choice_b": "Go around it",
        "next_a": "enter_mirror_maze",
        "next_b": "go_around_it"
    },
    "go_around_it": {
        "text": [
            "You are sprinting!",
            "You start going around the building but as you turn...",
            "You see a elephant stampeed coming",
            "You have been ran over by a stampeed of elephants!",
            "You have died!"
        ],
    },
    "enter_mirror_maze": {
        "text" : [
            "Your cerberus stood in front of you!",
            "The fight has started!",
            "The cerberus leaped into the air and...",
            "Won the fight",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene_circus"
    },
    "ride_ferris_wheel": {
        "text": [
            "You reach the top!",
            "A ggroup of bats start flying at you in the face!",
            "Oh no!",
            "The ferris wheel broke",
            "Do you want to jump of the ferris wheel or stay?",
        ],
        "choice_a": "Jump",
        "choice_b": "Stay",
        "next_a": "jump_of_ferris_wheel",
        "next_b": "stay_ferris_wheel"
    },
    "stay_ferris_wheel": {
        "text": [
            "The ferris wheel started working again!",
            "You made it to the ground!",
            "You only have one chance to escape!",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a":  "find_exit_scene_circus"
    },
    "jump_of_ferris_wheel": {
        "text": [
            "You are sprinting!",
            "You are about to jump!",
            "You are nearly there!",
            "You leap in the air!",
            "But then you realise that there is no water below you!",
            "You hit the ground!",
            "You have died!"
        ],
    },
    "walk_away_ferris_wheel": {
        "text": [
            "You run into a a guy dressed as The Terminator!",
            "Do you want to fight him or run from him?",
        ],
        "choice_a": "Fight",
        "choice_b": "Walk away",
        "next_a": "fight_the_terminator",
        "next_b": "walk_away_the_terminator"
    },
    "walk_away_the_terminator": {
        "text": [
            "You start running!",
            "You keep running!",
            "The Terminator just ran over you!"
        ],
    },
    "fight_the_terminator": {
        "text": [
            "You start fighting The Terminator!",
            "Do you want to steal his knife or run?",
        ],
        "choice_a": "Take his knife",
        "choice_b": "Run",
        "next_a": "take_knife",
        "next_b": "run_from_terminator"
    },
    "take_knife": {
        "text": [
            "You have won the fight!",
            "Do you want to continue your quest",
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene_circus",
    },
    "run_from_terminator": {
        "text": [
            "You start running!",
            "You keep running!",
            "The Terminator just ran you over!"
        ],
    },
    "find_exit_scene_circus": {
        "text": [
            "You are looking for the exit!",
            "Do you want to use a map or walk around?",
        ],
        "choice_a": "Use map",
        "choice_b": "Walk around",
        "next_a": "exit_scene_circus",
        "next_b": "lost_scene_circus"
    },
    "exit_scene_circus": {
        "text": [
            "You got the map!",
            "You are walking through the circus!",
            "You found the exit!",
        ],
    },
    "lost_scene_circus": {
        "text": [
            "You start wondering around in circles!",
            "You haven't found exit yet!",
            "Oh no you have died of hunger!",
        ],
    },
    "start_2": {
        "text": [
            "You are in a abandoned hospital.",
            "Do you want to go left or right?",
        ],
        "choice_a": "Go left",
        "choice_b": "Go right",
        "next_a": "left_path_hospital",
        "next_b": "right_path_hospital"
    },
    "left_path_hospital": {
        "text": [
            "You found a door!",
            "Do you want to go open it or walk away?",
        ],
        "choice_a": "Open",
        "choice_b": "Walk away",
        "next_a": "open_door_hospital",
        "next_b": "walk_away_hospital"
    },
    "right_path_hospital": {
        "text": [
            "You found a door!",
            "Do you want to go open it or walk away?",
        ],
        "choice_a": "Open",
        "choice_b": "Walk away",
        "next_a": "open_right_door_hospital",
        "next_b": "walk_right_away_hospital"
    },
    "open_right_door_hospital": {
        "text": [
            "You found a scapel!",
            "Do you want to keep it or walk away?",
        ],
        "choice_a": "Keep",
        "choice_b": "Walk away",
        "next_a": "keep_scapel",
        "next_b": "walk_away_scapel"
    },
    "walk_right_away_hospital": {
        "text": [
            "You run into a a treasure chest!",
            "Do you want to open it or leave it?",
        ],
        "choice_a": "Open",
        "choice_b": "Leave it",
        "next_a": "open_chest_hospital",
        "next_b": "leave_chest_hospital"
    },
    "leave_chest_hospital": {
        "text": [
            "You tried leaving the chest but you got locked in a room!",
            "You wait and wait and wait unti...",
            "You died of hunger!"
        ],
    },
    "keep_scapel": {
        "text": [
            "You now have a weapon!",
            "Oh no!",
            "There a doctor up ahead",
            "Do you want to fight the doctor or run away?",
        ],
        "choice_a": "Fight",
        "choice_b": "Run away",
        "next_a": "keep_scapel_fight",
        "next_b": "run_away_doctor"
    },
    "run_away_doctor": {
        "text": [
            "You are sprinting!",
            "You jump onto a hospital gurney!",
            "The doctor catches up to you and...",
            "Throws you out the 5 floor window!",
            "You have died!"
        ],
    },
    "keep_scapel_fight": {
        "text" : [
            "You pointed the scapel at the doctor!",
            "The fight has started!",
            "You tossed the scapel at him and...",
            "He died!",
            "Won the fight",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene_hospital"
    },
    "open_chest_hospital": {
        "text": [
            "You found a bunch of...",
            "Teddy bears!",
            "Oh no you activated the booby trap!",
            "A bunch of hospital machines at rolling at you",
            "Do you want to run from it or stay?",
        ],
        "choice_a": "Run",
        "choice_b": "Stay",
        "next_a": "run_from_machines",
        "next_b": "stay_machines"
    },
    "stay_machines": {
        "text": [
            "The machines are still coming!",
            "Why are you still standing there move!",
            "Last chance!",
            "You died from a bunch of hospital machines!"
        ],
    },
    "run_from_machines": {
        "text": [
            "You are sprinting away from the machines!",
            "You see a door!",
            "You are nearly there!",
            "The door about to shut!",
            "You start sliding and...",
            "You made it barely!",
            "Do you want to continue your quest?"
        ],
        "choice_a": "Yes",
        "next_a": "find_exit_scene_hospital"
    },
    "walk_away_scapel": {
        "text": [
            "You run into a doctor!",
            "Do you want to fight him or run from him?",
        ],
        "choice_a": "Fight",
        "choice_b": "Walk away",
        "next_a": "fight_without_scapel",
        "next_b": "walk_away_left_2"
    },
    "walk_away_left_2": {
        "text": [
            "You start running!",
            "You keep running!",
            "The doctor just dropped you off the 6th floor window!"
        ],
    },
    "fight_without_scapel": {
        "text": [
            "You start fighting!",
            "You are losing and you just...!",
            "Died!"
        ],
    },
    "find_exit_scene_hospital": {
        "text": [
            "You are looking for the exit!",
            "Do you want to use a map or walk around?",
        ],
        "choice_a": "Use map",
        "choice_b": "Walk around",
        "next_a": "exit_scene_hospital",
        "next_b": "lost_scene_hospital"
    },
    "exit_scene_hospital": {
        "text": [
            "You got the map!",
            "You are walking through the hospital!",
            "You found the exit!",
        ],
    },
    "lost_scene_hospital": {
        "text": [
            "You start wondering around in circles!",
            "You haven't found exit yet!",
            "Oh no you have died of hunger!",
        ],
    },
    "more_choices": {
        "text": [
            "You have got two more choices!",
            "Do you want to go into a school, a subway tunnel or more choices?",
        ],
        "choice_a": "Abandoned School",
        "choice_b": "Abandoned Subway Tunnel",
        "choice_c": "More choices",
        "next_a": "abandoned_school",
        "next_b": "abandoned_subway_tunnel",
        "next_c": "choices_more"
    },
    "abandoned_school": {
        "text": [
            "You are in a abandoned school.",
            "Rubble is stacked high up.",
            "Do you want to climb over it?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "climb_rubble",
        "next_b": "leave_game",
    },
    "climb_rubble": {
        "text": [
            "You start climbing the rubble.",
            "Rubble is stacked high up.",
            "You made it over!",
            "But you see a zombie principal!",
            "Do you want to fight him?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "fight_principal",
        "next_b": "run_from_principal",
    },
    "leave_game": {
        "text": [
            "You are walking to the exit.",
            "The door is locked",
            "Do you want to still leave?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "leave_game_fully",
        "next_b": "climb_rubble",
    },
    "leave_game_fully": {
        "text": [
            "You try pick locking the door.",
            "But it doesn't work.",
            "So jump through the class head first!",
        ],
    },
    "fight_principal": {
        "text": [
            "You are about to fight the principal.",
            "But you just remember...",
            "Zombies are already dead.",
            "You died from trying to fight a zombie!",
        ],
    },
    "run_from_principal": {
        "text": [
            "You start running and enter the lunch hall.",
            "Then you see a robotic mascot.",
            "Do you want to fight it?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "fight_mascot",
        "next_b": "run_from_mascot",
    },
    "fight_mascot": {
        "text": [
            "You start punching him.",
            "But then you see a off switch.",
            "Do you want to press the big red button?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "press_button",
        "next_b": "dont_press_button",
    },
    "run_from_mascot": {
        "text": [
            "You start running but then the mascot enables his...",
            "Jetpack!",
            "You died from the jetpack heat.",
        ],
    },
    "press_button": {
        "text": [
            "He ended up shutting down.",
            "Now you have one more fight left.",
            "You need to fight the gym coach!",
            "Do you want to fight the gym coach?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "fight_gym_coach",
        "next_b": "run_from_gym_coach",
    },
    "dont_press_button": {
        "text": [
            "You have died.",
        ],
    },
    "fight_gym_coach": {
        "text": [
            "He brings out a tennis ball launcher.",
            "You died from being hit by a tennis ball.",
        ],
    },
    "run_from_gym_coach": {
        "text": [
            "You ran from and he couldn't catch up to you",
            "You have won!",
        ],
    },
    "abandoned_subway_tunnel": {
        "text": [
            "You are in a abandoned subway tunnel.",
            "You see a old and rusted train."
            "Do you want to go onto the train?"
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "go_on_train",
        "next_b": "dont_go_on_train",
    },
    "go_on_train": {
        "text": [
            "You enter the train.",
            "You see a button to start the train."
            "Do you want to press the button?"
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "press_button_train",
        "next_b": "dont_press_button_train",
    },
    "dont_go_on_train": {
        "text": [
            "A group of bats come at you .",
            "They pick you up and then drop you."
            "You have died to bats!"
        ],
    },
    "press_button_train": {
        "text": [
            "You pressed the button.",
            "The train starts moving."
            "The train cannot stop."
            "You've died in a train crash!",
        ],
    },
    "dont_press_button_train": {
        "text": [
            "You didn't press the button on the train.",
            "But who is that behind you?"
            "Oh no it is the...",
            "Police!",
            "Do you want to run or fight the police?"
        ],
        "choice_a": "Fight",
        "choice_b": "Run",
        "next_a": "fight_police",
        "next_b": "run_from_police",
    },
    "fight_police": {
        "text": [
            "You ended up winning the fight.",
            "Because they were just security guards."
            "BRUHHHHHHHHHHHHHHH!",
            "Do you want to continue?"
        ],
        "choice_a": "Yes",
        "next_a": "find_subway_exit",
    },
    "run_from_police": {
        "text": [
            "You have died!"
            "They hit you with their batons!"
        ],
    },
    "find_subway_exit": {
        "text": [
            "You are so close to escaping!",
            "Do you want to climb a ladder or go to the light?"
        ],
        "choice_a": "Climb the ladder",
        "choice_b": "Go to the light",
        "next_a": "end_up_subway",
        "next_b": "went_to_heaven"
    },
    "went_to_heaven": {
        "text": [
            "You have died!",
            "Since you went towards the light!",
        ],
    },
    "end_up_subway": {
        "text": [
            "You have ended up inside a...",
            "A subway?",
            "Do you want to order a sandwich?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "died_posin",
        "next_b": "won_subway"
    },
    "died_posin": {
        "text": [
            "You have died!"
            "From the subway sandwich!"
        ],
    },
    "won_subway": {
        "text": [
            "You have won!",
        ],
    },
    "choices_more": {
        "text": [
            "You got one last option.",
            "Do you want to go into a abandoned village?",
        ],
        "choice_a": "Yes",
        "next_a": "abandoned_village",
    },
    "abandoned_village": {
        "text": [
            "You are outside a old village",
            "Do you want to go into the village?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "enter_village",
        "next_b": "village_instant_death"
    },
    "village_instant_death": {
        "text": [
            "You been hit by some lightning!",
            "You have died!",
        ],
    },
    "enter_village": {
        "text": [
            "You hear a howl",
            "You see a cottage in front of you.",
            "Do you want to go into the cottage?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "enter_cottage",
        "next_b": "die_cottage"
    },
    "enter_cottage": {
        "text": [
            "You enter the cottage.",
            "Then you see a vampire in front of you!",
            "Do you want to fight a vampire?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "fight_vampire",
        "next_b": "run_from_vampire"
    },
    "fight_vampire": {
        "text": [
            "You start throwing punches.",
            "But then you see it is morning.",
            "So you expose the vampire to light.",
            "He has died!",
            "Do you want to continue?",
        ],
        "choice_a": "Yes",
        "next_a": "grab_garlic",
    },
    "run_from_vampire": {
        "text": [
            "You been bitten by a vampire!",
            "You have died!",
        ],
    },
    "grab_garlic": {
        "text": [
            "You found some garlic.",
            "But then a person comes along and holds garlic in front of you.",
            "You start sneezing and then someone yells WITCH!",
            "Do you want to run?",
        ],
        "choice_a": "Yes",
        "choice_b": "No",
        "next_a": "escape_game",
        "next_b": "been_put_on_fire"
    },
    "escape_game": {
        "text": [
            "You have escaped the village!",
            "You have WON!",
        ],
    },
    "been_put_on_fire": {
        "text": [
            "You been grabbed and put on fire for being a witch!",
            "You have died!",
        ],
    }
}

SAVE_FILE = "save_data.json"

def save_progress(current_scene):
    with open(SAVE_FILE, "w") as f:
        json.dump({"current_scene": current_scene}, f)

def load_progress():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            data = json.load(f)
            return data.get("current_scene", "story_choice")
    return "story_choice"

# this draws the text on the screen
def draw_text_lines(lines, x, y, font, surface):
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, WHITE)
        surface.blit(text_surface, (x, y + i * 30))

# this draws the loading animation on the screen
def loading_animation(surface, font, pos, duration=2.0):
    start_time = time.time()
    while time.time() - start_time < duration:
        surface.fill(BLACK)
        dots_count = ((int((time.time() - start_time) * 2) % 3) + 1)
        dots = "." * dots_count
        text = font.render("Loading" + dots, True, WHITE)
        surface.blit(text, pos)
        pygame.display.flip()
        pygame.time.delay(250)

def main_menu():
    anim_circle_y = 0
    start = False
    while not start:
        screen.fill(BLACK)

        anim_circle_y = (anim_circle_y + 2) % HEIGHT
        pygame.draw.circle(screen, (100, 100, 255), (WIDTH // 2, anim_circle_y), 20)

        title_text = FONT.render("Welcome to Pathsway!", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 150))

        start_text = FONT.render("Press ENTER to Start", True, WHITE)
        quit_text = FONT.render("Press ESC to Quit", True, WHITE)
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, 300))
        screen.blit(quit_text, (WIDTH // 2 - quit_text.get_width() // 2, 340))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start = True
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        pygame.time.Clock().tick(60)

def save_exists():
    return os.path.exists(SAVE_FILE)

if save_exists():
    current_scene = load_progress()
else:
    main_menu()
    current_scene = "story_choice"


running = True

while running:
    screen.fill(BLACK)
    default_scene = story['story_choice']
    scene = story.get(current_scene, default_scene) # sets the current_scene

    text_lines = scene["text"] if isinstance(scene["text"], list) else [scene["text"]]
    draw_text_lines(text_lines, 20, 20, FONT, screen)

    # this sets choice_a and choice_b to has_a and has_b
    has_a ="choice_a" in scene
    has_b ="choice_b" in scene
    has_c ="choice_c" in scene
    has_d ="choice_d" in scene

    # this makes the game to end if it doesn't have has_a or has_b
    if not has_a and not has_b and not has_c and not has_d:
        end_text = FONT.render("The End! Please press ESC to quit.", True, WHITE)
        screen.blit(end_text, (20, HEIGHT - 50))

    # this makes it show the choices set
    else:
        if has_a:
            choice_a_text = f"A: {scene['choice_a']}"
            screen.blit(FONT.render(choice_a_text, True, WHITE), (20, HEIGHT - 120))
        if has_b:
            choice_b_text = f"B: {scene['choice_b']}"
            screen.blit(FONT.render(choice_b_text, True, WHITE), (20, HEIGHT - 90))
        if has_c:
            choice_c_text = f"C: {scene['choice_c']}"
            screen.blit(FONT.render(choice_c_text, True, WHITE), (20, HEIGHT - 60))
        if has_d:
            choice_d_text = f"D: {scene['choice_d']}"
            screen.blit(FONT.render(choice_d_text, True, WHITE), (20, HEIGHT - 30))

    pygame.display.flip()

    # this states which keys would be used to play the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

            if has_a and event.key == pygame.K_a:
                loading_animation(screen, FONT, (20, HEIGHT // 2))
                current_scene = scene["next_a"]
                save_progress(current_scene)

            elif has_b and event.key == pygame.K_b:
                loading_animation(screen, FONT, (20, HEIGHT // 2))
                current_scene = scene["next_b"]
                save_progress(current_scene)

            elif has_c and event.key == pygame.K_c:
                loading_animation(screen, FONT, (20, HEIGHT // 2))
                current_scene = scene["next_c"]
                save_progress(current_scene)

            elif has_d and event.key == pygame.K_d:
                loading_animation(screen, FONT, (20, HEIGHT // 2))
                current_scene = scene["next_d"]
                save_progress(current_scene)

# this closes the screen so it doesn't stay open
pygame.quit()
sys.exit()

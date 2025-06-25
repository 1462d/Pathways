import time

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
    "walk_away_cerberus": {
        "text": [
            "The ceberus ate you!",
            "Oh no!",
            "You have died!",
        ],
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

# this sets the first scene to start
current_scene = "story_choice"

while True:
    scene = story[current_scene] # sets the current_scene

    for line in scene["text"]:
        print(line) # this prints the text in a terminal
        time.sleep(2) # this sets the time inbetween texts

    # this changes the names
    has_a ="choice_a" in scene
    has_b ="choice_b" in scene
    has_c ="choice_c" in scene
    has_d ="choice_d" in scene

    # this makes the game to end if it doesn't have has_a or has_b
    if not has_a and not has_b and not has_c and not has_d:
        print("The End!")
        break

    # this makes it show the four choices set
    if has_a and has_b and has_c and has_d:
        print("A:", scene["choice_a"])
        print("B:", scene["choice_b"])
        print("C:", scene["choice_c"])
        print("D:", scene["choice_d"])
        choice = input("Choose A, B, C or D to continue: ").lower()

        # this switches the scene depending on what they chose
        if choice == "a":
            print("You have chosen: ", scene["choice_a"])
            time.sleep(1)
            current_scene = scene["next_a"]
        elif choice == "b":
            print("You have chosen: ", scene["choice_b"])
            time.sleep(1)
            current_scene = scene["next_b"]
        elif choice == "c":
            print("You have chosen: ", scene["choice_c"])
            time.sleep(1)
            current_scene = scene["next_c"]
        elif choice == "d":
            print("You have chosen: ", scene["choice_d"])
            time.sleep(1)
            current_scene = scene["next_d"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_a and has_b and has_c:
        print("A:", scene["choice_a"])
        print("B:", scene["choice_b"])
        print("C:", scene["choice_c"])
        choice = input("Choose A, B or C to continue: ").lower()

        if choice == "a":
            print("You have chosen: ", scene["choice_a"])
            time.sleep(1)
            current_scene = scene["next_a"]
        elif choice == "b":
            print("You have chosen: ", scene["choice_b"])
            time.sleep(1)
            current_scene = scene["next_b"]
        elif choice == "c":
            print("You have chosen: ", scene["choice_c"])
            time.sleep(1)
            current_scene = scene["next_c"]
        else:
            print("Invalid request!")
            time.sleep(1)


    elif has_a and has_b:
        print("A:", scene["choice_a"])
        print("B:", scene["choice_b"])
        choice = input("Choose A or B to continue: ").lower()

        if choice == "a":
            print("You have chosen: ", scene["choice_a"])
            time.sleep(1)
            current_scene = scene["next_a"]
        elif choice == "b":
            print("You have chosen: ", scene["choice_b"])
            time.sleep(1)
            current_scene = scene["next_b"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_a and has_c:
        print("A:", scene["choice_a"])
        print("C:", scene["choice_c"])
        choice = input("Choose A or C to continue: ").lower()

        if choice == "a":
            print("You have chosen: ", scene["choice_a"])
            time.sleep(1)
            current_scene = scene["next_a"]
        elif choice == "c":
            print("You have chosen: ", scene["choice_c"])
            time.sleep(1)
            current_scene = scene["next_c"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_b and has_c:
        print("B:", scene["choice_b"])
        print("C:", scene["choice_c"])
        choice = input("Choose B or C to continue: ").lower()

        if choice == "b":
            print("You have chosen: ", scene["choice_b"])
            time.sleep(1)
            current_scene = scene["next_b"]
        elif choice == "c":
            print("You have chosen: ", scene["choice_c"])
            time.sleep(1)
            current_scene = scene["next_c"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_a and has_d:
        print("A:", scene["choice_a"])
        print("D:", scene["choice_d"])
        choice = input("Choose A or D to continue: ").lower()

        if choice == "a":
            print("You have chosen: ", scene["choice_a"])
            time.sleep(1)
            current_scene = scene["next_a"]
        elif choice == "d":
            print("You have chosen: ", scene["choice_d"])
            time.sleep(1)
            current_scene = scene["next_d"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_b and has_d:
        print("B:", scene["choice_b"])
        print("D:", scene["choice_d"])
        choice = input("Choose B or D to continue: ").lower()

        if choice == "b":
            print("You have chosen: ", scene["choice_b"])
            time.sleep(1)
            current_scene = scene["next_b"]
        elif choice == "d":
            print("You have chosen: ", scene["choice_d"])
            time.sleep(1)
            current_scene = scene["next_d"]
        else:
            print("Invalid request!")
            time.sleep(1)

    elif has_c and has_d:
        print("C:", scene["choice_c"])
        print("D:", scene["choice_d"])
        choice = input("Choose C or D to continue: ").lower()

        if choice == "c":
            print("You have chosen: ", scene["choice_c"])
            time.sleep(1)
            current_scene = scene["next_c"]
        elif choice == "d":
            print("You have chosen: ", scene["choice_d"])
            time.sleep(1)
            current_scene = scene["next_d"]
        else:
            print("Invalid request!")
            time.sleep(1)


    # this sets it to continue if only one choice availible
    elif has_a:
        print("A:", scene["choice_a"])
        input("Press enter to continue the game!")
        current_scene = scene["next_a"]

    elif has_b:
        print("B:", scene["choice_b"])
        input("Press enter to continue the game!")
        current_scene = scene["next_b"]

    elif has_c:
        print("C:", scene["choice_c"])
        input("Press enter to continue the game!")
        current_scene = scene["next_c"]

    elif has_d:
        print("D:", scene["choice_d"])
        input("Press enter to continue the game!")
        current_scene = scene["next_d"]

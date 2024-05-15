# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#2b5309")
define s = Character("Sally", color="#25088d")
define m = Character("Monika", color="#705200")
define y = Character("%(player_name)", color="#ff49c2ff")


# The game starts here.
image sally="images/sally.png"
image eillen="images/eillien.png"
image monika="images/monika.png"
image yn="images/main.png"

label start:
   "I've been thinking about changing my name."

# The phrase in the brackets is the text that the game will display to prompt 
# the player to enter the name they've chosen.

$ player_name = renpy.input("What is your name?")

$ player_name = player_name.strip()
# The .strip() instruction removes any extra spaces the player 
# may have typed by accident.

#  If the player can't be bothered to choose a name, then we
#  choose a suitable one for them:
if player_name == "":
    $ player_name="Y/N"
    
# Now the other characters in the game can greet the player.

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

scene bg room
show yn at center

# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

show sally at left

# These display lines of dialogue.

s "hey %(player_name)s wasup!"# %(player_name) is the name of Y/N
show monika at right 
m "hey bro wanna hangout?"
hide sally
show eillen at left
e "No hang out with me!"
hide eillen
show sally at left
s "you gotta pick one of us to not go since theirs only room for three of us"
menu:
    "uhh i choose Eillen":
        jump No_Eillen
    "oh i guess sally is out":
        jump No_Sally
    "sorry monika your out":
        jump No_Monika
label No_Monika:
    m "if only this was a game i would just make those two dissapear"
    s "hey!"
    e "yea cmon monkia"
label No_Eillen:
    e "damn see you later %(player_name)"
label No_Sally:
    s "godamn it!"

label Eillen_ending:
label Sally_Ending:
label Monika_Ending:
# Return ends the game.

return
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen", color="#2b5309")
define s = Character("Sara", color="#25088d")
define m = Character("Monika", color="#705200")
define y = Character("%(player_name)", color="#ff49c2ff")


# The game starts here.
image sara="images/sara.png"
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

show sara at left

# These display lines of dialogue.

s "hey %(player_name)s wasup!"# %(player_name) is the name of Y/N
show monika at right 
m "Hey! I wanted to hang you with %(player_name)s."
hide sara
show eillen at left
e "No! I wanted to hang out with them!"
hide eillen
show sara at left
s "This isn't going anywhere, %(player_name)s? you should choose who you wanna leave behind with since there's only room for 3."
menu:
    "Uhh... Eillen? can you stay behind?":
        jump No_Eillen
   "Oh... well i guess Sara can stay behind.":
        jump No_Sara
   "Uhm... Monika should stay behind.":
        jump No_Monika
label No_Monika:
    m "if only this was a game i would just make those two dissapear"
    s "hey!"
    e "yea cmon monkia"
label No_Eillen:
    e "damn see you later %(player_name)"
label No_Sara:
    s "godamn it! well i can see you again some other time"

label Eillen_ending:
label Sally_Ending:
label Monika_Ending:
# Return ends the game.

return
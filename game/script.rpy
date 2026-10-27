# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define i = Character("Ishikawa")
define dissolveS = Dissolve(0.3)
define audio.bgm1 = "bgm1.mp3"
define audio.bgm2 = "bgm2.mp3"
define audio.bgm3 = "bgm3.mp3"
define audio.bgm4 = "bgm4.mp3"
default temp_name = ""
default temp_password = ""
default pass_result = None

image studio_logo = "images/Fishware.png"

label splashscreen:

    scene black

    pause 0.5

    show studio_logo at truecenter
    with dissolve

    pause 2.5

    hide studio_logo
    with dissolve

    pause 0.5

    return

# The game starts here.
image ishikawa:
    "ishikawa.png"
    yalign 0.0
    zoom 0.4
image ishikawa smile:
    "ishikawa smile.png"
    yalign 0.0
    zoom 0.4
image ishikawa frown:
    "ishikawa frown.png"
    yalign 0.0
    zoom 0.4
image ishikawa armcross:
    "ishikawa armcross.png"
    yalign 0.0
    zoom 0.4
image ishikawa armcross smile:
    "ishikawa armcross smile.png"
    yalign 0.0
    zoom 0.4
image ishikawa armcross frown:
    "ishikawa armcross frown.png"
    yalign 0.0
    zoom 0.4
image ishikawa pointing:
    "ishikawa pointing.png"
    yalign 0.0
    zoom 0.4
image ishikawa pointing smile:
    "ishikawa pointing smile.png"
    yalign 0.0
    zoom 0.4
image ishikawa pointing frown:
    "ishikawa pointing frown.png"
    yalign 0.0
    zoom 0.4
image BG_BigSisterRoom_Night:
    "BG_BigSisterRoom_Night.jpg"
    zoom 1.5
image BG_BigSisterRoom:
    "BG_BigSisterRoom.jpg"
    zoom 1.5
image BG_ComputerCenter:
    "BG_ComputerCenter.jpg"
    zoom 1.5


screen name_input():

    modal True

    frame:
        xalign 0.5
        yalign 0.50
        xsize 900
        ysize 300
        background Frame("frame.png", 20, 20)

        vbox:
            spacing 15
            xalign 0.5
            yalign 0.5

            text "Enter your name?" size 40 xalign 0.5

            input value VariableInputValue("temp_name") length 20:
                xalign 0.5

            textbutton "Confirm":
                xalign 0.5
                action Return(temp_name if temp_name != "" else "Shin")

screen password_input():

    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        ysize 300
        background Frame("frame.png", 20, 20)

        vbox:
            spacing 15
            xalign 0.5
            yalign 0.5

            text "Enter a Password" size 40 xalign 0.5

            input value VariableInputValue("temp_password") length 30:
                xalign 0.5
                pixel_width 600

            textbutton "Check Password":
                xalign 0.5
                action Return(temp_password)

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene BG_BigSisterRoom_Night with dissolve
    pause
    scene BG_BigSisterRoom
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    


    # These display lines of dialogue.
    show ishikawa 
    with dissolve
    pause
    show ishikawa smile
    play music bgm1
    i "Welcome to the Last Firewall."
    show ishikawa armcross smile
    with dissolveS
    i "You must be the new recruit."
    show ishikawa smile
    with dissolveS
    i "My name is Ishikawa."
    i "I will show you the ropes."

    show ishikawa
    with dissolveS
    i "I'm the one who will guide you..."
    extend " and teach you how to protect yourself against {b}Threats{b}."
    show ishikawa armcross smile
    with dissolveS
    i "So... uh,"
    show ishikawa armcross
    with dissolveS
    i "Tell me your name?"
    show ishikawa
    with dissolveS

    $ temp_name = ""
    $ player_name = renpy.call_screen("name_input")

    $ player_name = player_name.strip()

    if player_name == "":
        $ player_name="Bob"

    show ishikawa smile
    with dissolveS
    i "Nice to meet you, %(player_name)s!"
    
    show ishikawa armcross
    with dissolveS
    i "Hmmm..."

    show ishikawa armcross smile
    with dissolveS
    extend " where do I start?"
    
    show ishikawa
    with dissolveS
    i "Do you know what cybersecurity is?"
    show ishikawa smile
    i "You probably already have an idea what cybersecurity is"

    show ishikawa
    with dissolveS
    i "but I’ll explain it anyway."

    show ishikawa pointing smile
    with dissolveS
    i "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks."
    show ishikawa armcross
    with dissolveS
    i "Think of cyberspace like a city."
    show ishikawa armcross smile
    with dissolveS
    i "Every device you own? That’s a house."
    extend " Every account? A locked room."
    extend " Every piece of data? Something valuable inside."

    show ishikawa pointing
    with dissolveS
    i "Now imagine someone trying to break in."

    show ishikawa pointing smile
    with dissolveS
    i "That’s where cybersecurity comes in."
    show ishikawa smile
    with dissolveS
    i "We build defenses—"
    extend " like firewalls to block intruders,"
    extend " passwords to secure access,"  
    extend " and encryption to hide information so only the right people can read it."
    show ishikawa armcross frown
    with dissolveS
    pause
    show ishikawa pointing frown
    with dissolveS
    i "But here’s the problem"
    i "Not all threats break the door down."
    show ishikawa pointing frown
    with dissolveS
    i "Some trick you into opening it."

    i "Some hide… and wait."

    i "And some—"
    show ishikawa armcross frown
    with dissolveS
    extend " don’t follow any rules at all."
    show ishikawa smile
    with dissolveS
    i "That’s what we’re dealing with."
    show ishikawa armcross smile
    with dissolveS
    i "So from here on out,  %(player_name)s."
    i "You will learn how to fight against this {b}Threats{b}."
    show ishikawa
    with dissolveS
    pause
    show ishikawa smile
    i "Aight, let's go to the training room."

    scene BG_ComputerCenter
    with blinds

    show ishikawa 
    with dissolve
    pause
    show ishikawa smile
    i "Here in the training room before we go into battle against {b}Threats{b}"
    show ishikawa armcross smile
    with dissolveS
    i "We study and learn how a {b}Threat{b} acts or behaves."
    show ishikawa pointing smile
    with dissolveS
    i "So, what is a {b}Threat{b}?"
    show ishikawa
    with dissolveS
    i "A threat is anything that can damage your data."
    show ishikawa smile
    with dissolveS
    i "A threat is something that can steal your data,"
    extend " damage systems,"
    extend " or trick users like you."
    show ishikawa pointing
    with dissolveS
    i "It can take many forms."
    show ishikawa pointing smile
    with dissolveS
    i "Sometimes, it's obvious—"
    extend " like a malicious system trying to break into your system."
    show ishikawa pointing frown
    with dissolveS
    i "Other times… it's not."
    show ishikawa armcross smile
    with dissolveS
    i "But every move a threat makes follows a pattern—"
    extend "even if it doesn’t seem like it at first."
    show ishikawa smile
    with dissolveS
    i "They search for weaknesses.\n"
    extend " They test defenses.\n"
    extend " They adapt."

    i "Not much of an explanation, but"
    show ishikawa
    with dissolveS
    i "that's pretty much it."
    stop music fadeout 1.0

    show ishikawa smile
    with dissolveS
    i "I hope you understand it."
    show ishikawa armcross
    with dissolve
    pause
    show ishikawa armcross smile
    i "So... uhhh"
label tutorials:

    show ishikawa
    with dissolveS
    pause
    show ishikawa smile

    i "What do you want to learn?"
    show ishikawa
    menu:
        "Cyber Threat Landscape":
            jump cyberland
        "Phishing":
            jump phishing
        "Passwords":
            jump cpassword

        "Proceed.":
            jump test1
    return

label test1:
    i "Alright..."
    play music bgm4
    show ishikawa smile
    with dissolveS
    i "Let’s see what you’ve learned."
    show ishikawa
    with dissolveS
    i "Uhh..."
    show ishikawa smile
    with dissolveS
    extend " we’ll run a few simulations"
    extend " to test what you’ve picked up."

    show ishikawa pointing
    with dissolveS
    i "First one’s simple."
    show ishikawa pointing smile
    with dissolveS
    i "Let’s check how you handle passwords."
    show ishikawa pointing
    with dissolveS

    jump password_test

label password_test:

    call screen password_input
    $ user_pass = _return

    $ strength, feedback = check_password(user_pass)

    show ishikawa
    with dissolveS
    i "Hmm..."

    if strength == "Weak":
        show ishikawa frown
        with dissolveS
        i "That’s weak."
        i "Anyone could break that."

    elif strength == "Medium":
        show ishikawa armcross
        with dissolveS
        i "Not bad..."
        show ishikawa armcross smile
        with dissolveS
        i "But it still has weaknesses."

    else:
        show ishikawa
        with dissolveS
        i "Good."
        show ishikawa smile
        with dissolveS
        i "That’ll hold up better."

    if feedback:

        show ishikawa pointing
        with dissolveS

        i "Let’s go over the issues."

        python:
            for f in feedback:
                renpy.pause(0.2)
                renpy.say(i, f)


    if strength == "Strong":

        show ishikawa
        i "You passed the test."
        i "Moving on..."
        extend " to the next simulation"
        hide ishikawa

        jump startTurn

    else:

        i "Try again."

        jump password_test

label allthreatdf:
    scene bg
    show screen battleP
    show player zorder 2
    show expression currentThreatImage as threat zorder 1
    stop music fadeout 1.0

    t1 "Not bad"
    t1 "You win"
    $ threatHp -=40

    jump end1

label end1:
    hide screen battleP
    scene BG_ComputerCenter
    with dissolveS

    show ishikawa
    with dissolveS
    i "Congratulations, %(player_name)s."

    show ishikawa smile
    with dissolveS

    i "You successfully completed all of the cybersecurity courses."

    i "And you passed every test that stood in your way."

    show ishikawa
    with dissolveS

    i "You’ve learned how to recognize threats..."

    show ishikawa smile
    with dissolveS
    i "how to think carefully under pressure..."
    i "and how to protect both yourself and others online."

    i "I’m proud of how far you’ve come."

    show ishikawa
    with dissolveS

    i "I guess it's time to say goodbye..."
    extend "until we meet again."

    show ishikawa smile
    with dissolveS

    i "Remember all the things i've taught you"

    show ishikawa
    with dissolveS

    i "From this point forward..."

    show ishikawa smile
    with dissolveS

    i "You are no longer just a student."

    show ishikawa
    with dissolveS

    i "You are someone prepared to face cyber threats with confidence."

    




    jump finalcredits

label finalcredits:

    scene black

    call screen creditscreen

    return


screen creditscreen():

    timer 102 action Return()

    vbox:

        xsize 1000
        xalign 0.5
        ypos 720

        at credits_scroll

        spacing 30

        text "THE LAST FIREWALL":
            size 80
            xalign 0.5
            color "#0044ff"

        text "A Ren'Py Educational Game":
            size 40
            xalign 0.5

        null height 80

        text "Created By":
            size 45
            xalign 0.5

        text "Fishware":
            size 35
            xalign 0.5

        null height 100

        text "Game Designer: Christian Oliver Obrero":
            size 45
            xalign 0.5

        text "Creative Writer: Lee Ivan Sahurda":
            size 45
            xalign 0.5
        text "Illustrator: Emmanuelle Christian Obrero":
            size 45
            xalign 0.5
        text "Programming&Scripting: John Paul Caigas":
            size 45
            xalign 0.5
        text "                        Christian Oliver Obrero":
            size 45
            xalign 0.5
        text "               Emmanuelle Christian Obrero":
            size 45
            xalign 0.5
        text "                     Vince Francis Bazar":
            size 45
            xalign 0.5
        text "Proofreading&QA Tester: Vince Francis Bazar":
            size 45
            xalign 0.5
        text "                John Gilbert Balbuena":
            size 45
            xalign 0.5
        text "Play Tester: John Gilbert Balbuena":
            size 45
            xalign 0.5
        null height 100

        text "Credits to":
            size 45
            xalign 0.5

        text "Blue Archive Wiki":
            size 35
            xalign 0.5

        text "Steins Gate Ost":
            size 35
            xalign 0.5

        text "World Trigger Ost":
            size 35
            xalign 0.5

        text "Log Horizon Ost":
            size 35
            xalign 0.5

        null height 120

        text "Made with Ren'Py":
            size 40
            xalign 0.5

        null height 200

        text "Thank you for playing!":
            size 60
            xalign 0.5
            color "#00ffcc"


transform credits_scroll:

    subpixel True

    ypos 720

    linear 100 ypos -5000
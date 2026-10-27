define t = Character("Threat")
define i = Character("Ishikawa")
define you = Character("[player_name]")

default awareness = 50
default enemy_pressure = 50
default battle_phase = 1

scene BG
screen battle_ui():

    frame:
        align (0.02, 0.02)
        xpadding 15
        ypadding 10

        vbox:
            text "Awareness: [awareness]"
            bar value awareness range 100 xmaximum 200

    frame:
        align (0.98, 0.02)
        xpadding 15
        ypadding 10

        vbox:
            text "Threat Level: [enemy_pressure]"
            bar value enemy_pressure range 100 xmaximum 200


screen response_menu_phase1():

    modal True

    frame:
        align (0.5, 0.75)
        xpadding 20
        ypadding 20

        vbox:
            spacing 12

            text "What will you do?"

            textbutton "Open the link to check if your information is correct":
                action Return("risky")

            textbutton "Verify the request through official school channels first":
                action Return("smart")

            textbutton "Ignore it since it doesn't seem urgent":
                action Return("neutral")

screen response_menu_phase2():

    modal True

    frame:
        align (0.5, 0.75)
        xpadding 20
        ypadding 20

        vbox:
            spacing 12

            text "How do you respond?"

            textbutton "Open the link, but carefully inspect the website before logging in":
                action Return("risky")

            textbutton "Contact IT through official channels to confirm the alert":
                action Return("smart")

            textbutton "Ignore it for now since it might just be a scare tactic":
                action Return("neutral")

screen response_menu_phase3():

    modal True

    frame:
        align (0.5, 0.75)

        vbox:
            spacing 12

            text "Choose your response:"

            textbutton "Send only your username to avoid full exposure":
                action Return("risky")

            textbutton "Refuse and report the message immediately":
                action Return("smart")

            textbutton "Comply since it's from IT and seems urgent":
                action Return("wrong")

label battle:

    i "Welcome to the training simulation."
    i "This is a dialogue battle. Your words are your weapon."

    jump battle_start

label battle_start:

    $ awareness = 50
    $ enemy_pressure = 50
    $ battle_active = True

    show screen battle_ui

    i "Welcome to the training simulation." 
    i "This is a dialogue battle. Your words are your weapon."

    jump battle_loop

label battle_loop:

    if battle_active:

        if battle_phase == 1:
                t "Hello, this is from your school admin office."
                t "We're currently updating student records for this semester."
                t "Please review your information using the link below to avoid issues with enrollment."

                $ result = renpy.call_screen("response_menu_phase1")

        elif battle_phase == 2:
            t "This is IT Support. We've detected suspicious activity on your account."
            t "If you don't verify within 5 minutes, your account will be permanently locked."
            t "Use the secure link we provided."

            $ result = renpy.call_screen("response_menu_phase2")

        elif battle_phase == 3:
            t "We noticed multiple failed login attempts."
            t "To secure your account, reply with your username and password so we can verify ownership."

            $ result = renpy.call_screen("response_menu_phase3")

        jump process_result

label process_result:

    if result == "smart":
        $ enemy_pressure -= 15
        "You verified the situation safely. The threat loses ground."

    elif result == "risky":
        $ awareness -= 10
        $ enemy_pressure -= 5
        "You tried to be careful... but you still exposed yourself."

    elif result == "neutral":
        $ awareness -= 5
        "Doing nothing bought you time... but didn't solve the problem."

    elif result == "wrong":
        $ awareness -= 20
        "You fell directly into the trap."

    $ battle_phase += 1

    jump check_battle_end

label battle_win:

    hide screen battle_ui

    i "Well done."
    i "You successfully identified the threat."

    return


label battle_lose:

    hide screen battle_ui

    t "You fell for the trap..."

    i "Don't worry. Learn from this and try again."

    return

label check_battle_end:

    if enemy_pressure <= 0:
        jump battle_win

    elif awareness <= 0:
        jump battle_lose

    elif battle_phase > 3:
        jump battle_win  # survived all phases

    else:
        jump battle_loop
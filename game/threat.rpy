default threatHp = 100
default characterHp = 100
define you = Character("[player_name]")
define i = Character("Ishikawa")
define t1 = Character("Threat")
define audio.sound1 = "Fah.mp3"
define audio.sound2 = "Fahfahh.mp3"
default turnCount = 0
default maxTurns = 5
default threatStage = 1
default ThreatName = "Cyber Threat"
default phase2_triggered = False
default currentThreatImage = "threat1"

image frameBox = "frameBox.png"

image player: 
    "player.png"
    xalign 1.50
    yalign 0.0
    zoom 0.3
image pAttack:
    "pATK1.png"
    pause 0.15
    "pATK2.png"
    pause 0.10
    "pATK3.png"
    pause 0.15
    "pATK4.png"
    pause 1.0

image threat1: 
    "spider.png"
    xalign 0.05
    yalign 0.50
    zoom 0.2

image threat2:
    "cat.png"
    xalign 0.05
    yalign 0.50
    zoom 0.2

image threat3:
    "cube.png"
    xalign 0.05
    yalign 0.50
    zoom 0.2
    
screen battleP:

    frame:
        xalign 0.05
        yalign 0.10
        background Transform ("frameBox", zoom = 0.7)
        xsize 350
        ysize 80

        fixed:

            text "[ThreatName]":
                xpos 50
                ypos -50

            bar:
                range 100
                value FieldValue(store, "threatHp", 100)
                xsize 447
                xpos 0.39
                ypos 0.17


    frame:
        xalign 0.75
        yalign 0.65
        background Transform ("frameBox", zoom = 0.7)
        xsize 350
        ysize 80

        fixed:

            text "[player_name]":
                xpos 50
                ypos -50

            bar:
                range 50
                value FieldValue(store, "characterHp", 100)
                xsize 447
                xpos 0.39
                ypos 0.17


label playerAttack:

    hide player
    play sound sound2
    show pAttack zorder 3
    show expression currentThreatImage as threat zorder 1:
        xoffset 0
        linear 0.05 xoffset -30
        linear 0.05 xoffset 20
        linear 0.05 xoffset -10
        linear 0.05 xoffset 0
    pause 0.45
    hide pAttack
    show player zorder 2

    return

label threatAttack:

    hide threat
    play sound sound1
    show expression currentThreatImage as threat zorder 1:
        xalign 0.05 yalign 0.50
        linear 0.15 xalign 0.78 yalign 0.0

    pause 0.15

    show expression currentThreatImage as threat zorder 1:
        xalign 0.78 yalign 0.0
        linear 0.06 xalign 0.82
        linear 0.06 xalign 0.75
        linear 0.05 xalign 0.79
        linear 0.05 xalign 0.78

    show player zorder 2:
        xoffset 0
        linear 0.05 xoffset -30
        linear 0.05 xoffset 20
        linear 0.05 xoffset -10
        linear 0.05 xoffset 0

    pause 0.2

    show expression currentThreatImage as threat zorder 1:
        linear 0.2 xalign 0.05 yalign 0.50

    return

label resolveTurn:

    if player_hit:
        $ threatHp -= 15
        call playerAttack from _call_playerAttack_1
    else:
        $ characterHp -= 20
        call threatAttack from _call_threatAttack_1

    call battleTurns from _call_battleTurns
    return

label battleTurns:

    $ turnCount += 1

    if threatStage == 1 and threatHp <= 40 and not phase2_triggered:
        $ phase2_triggered = True
        t1 "Not bad"
        t1 "How about this!"
        t1 "Tell me—can you spot which email is real?"
        t1 "And which one is a fake?"
        t1 "hahaha!"
        call emailMinigame from _call_emailMinigame

    elif threatStage == 2 and threatHp <= 40 and not phase2_triggered:
        $ phase2_triggered = True
        t1 "you are pretty good"
        t1 "but can you overcome this!"
        t1 "Can you Spot the Difference!"
        call phishing_attack from _call_phishing_attack

    elif threatStage == 3 and threatHp <= 40 and not phase2_triggered:
        $ phase2_triggered = True
        t1 "You’ve done well so far..."
        t1 "But this time... it’s not about tricking you."
        t1 "It’s about infecting your system."
        call open_terminal from _call_open_terminal

    if characterHp <= 0:
        jump gameOver

    if threatHp <= 0:
        jump victory

    if turnCount >= maxTurns:

        if characterHp > threatHp:
            jump victory

        elif threatHp > characterHp:
            jump gameOver

    return

label turnTutorial:

    hide screen battleP
    hide player
    hide threat

    scene bg
    with fade

    i "Before we begin, I’ll explain how this system works."

    i "You will face cyber threats one at a time."

    i "Each battle is turn-based. Every turn, you’ll answer a question."

    i "Your choice determines what happens next."

    i "If you answer correctly, the threat takes damage."

    i "If you’re wrong, you take damage instead."

    show screen battleP

    i "This is the battlefield UI."

    show expression currentThreatImage as threat zorder 1
    with dissolve

    i "This is the threat."

    i "The bar at the top shows the threat’s HP."

    i "Reduce it to zero to win the battle."

    hide threat
    with dissolve

    show player zorder 2
    with dissolve

    i "This is you."

    i "The bar at the bottom shows your HP."

    i "If your HP reaches zero, you lose the battle."

    i "Keep an eye on both HP bars during combat."

    show expression currentThreatImage as threat zorder 1
    with dissolve

    i "Now, let’s test it with a simple scenario."

    menu:
        "What is the safest response to a suspicious email attachment?"

        "Open it to check what's inside":
            $ player_hit = False
            $ characterHp -= 20
            call threatAttack from _call_threatAttack_2
            i "That was dangerous. Never open unknown attachments."

        "Verify the sender or delete it":
            $ player_hit = True
            $ threatHp -= 20
            call playerAttack from _call_playerAttack_2
            i "Correct. Always verify before interacting."

    i "Good. That’s how combat works."

    i "Each battle also has a turn limit."

    i "If you run out of turns, the one with higher HP wins."

    i "As you progress, new types of threats will appear."

    i "Some will introduce new mechanics."

    i "Stay focused. Think before you choose."

    i "That’s all you need to know."

    return


label startTurn:

    call turnTutorial from _call_turnTutorial

    $ characterHp = 100
    $ threatHp = 100
    $ turnCount = 0
    $ phase2_triggered = False

    scene bg
    show screen battleP
    show player zorder 2
    show expression currentThreatImage as threat zorder 1
    play music bgm2
    i "Incoming Threat Detected!!!"

    jump turn1

label victory:

    if threatStage == 1:
        "You defeated the first threat!"

        $ threatStage += 1

        jump nextThreat

    elif threatStage == 2:
        "You defeated the second threat!"

        $ threatStage += 1

        jump nextThreat

    else:
        "You defeated all threats!"
        return

label gameOver:
    "You were defeated..."

    menu:
        "Try again?"

        "Retry":
            $ characterHp = 100
            $ threatHp = 100
            $ turnCount = 0
            $ phase2_triggered = False

            scene bg
            show screen battleP
            show player zorder 2
            show expression currentThreatImage as threat zorder 1
            play music bgm2

            if threatStage == 1:
                jump turn1
            elif threatStage == 2:
                jump turn6
            elif threatStage == 3:
                jump turn11

        "Quit":
            return

label nextThreat:

    "A new threat appears..." 

    $ characterHp += 50
    if characterHp > 100:
        $ characterHp = 100
    
    $ turnCount = 0
    $ phase2_triggered = False

    if threatStage == 2:
        $ ThreatName = "Phishing Threat"
        $ threatHp = 100
        $ currentThreatImage = "threat2"

        hide threat with dissolve

        show expression currentThreatImage as threat zorder 1
        with dissolve

        jump turn6

    elif threatStage == 3:
        $ ThreatName = "Social Engineer"
        $ threatHp = 100
        $ currentThreatImage = "threat3"

        hide screen std_screen

        hide threat with Dissolve(0.5)
        scene bg with fade

        show screen battleP
        show player zorder 2

        show expression currentThreatImage as threat zorder 1
        with Dissolve(0.5)

        jump turn11
    else:
        jump victory

label turn1:
    menu:
        "What is the cyber threat landscape?"


        "The environment where cyber attacks happen":
            $ player_hit = True
        "A type of antivirus software":
            $ player_hit = False
        "A computer hardware system":
            $ player_hit = False
        "A gaming platform":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn
    jump turn2


label turn2:
    menu:
        "Who are threat actors?"


        "People or groups behind cyber attacks":
            $ player_hit = True
        "Only government officials":
            $ player_hit = False
        "Computer hardware devices":
            $ player_hit = False
        "Internet service providers":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_1
    jump turn3


label turn3:
    menu:
        "What do attackers usually target?"


        "Only large companies":
            $ player_hit = False
        "Only servers":
            $ player_hit = False
        "Data, accounts, and devices":
            $ player_hit = True
        "Only social media posts":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_2
    jump turn4


label turn4:
    menu:
        "How do most cyber attacks begin?"


        "By physically breaking computers":
            $ player_hit = False
        "Through human actions like clicking links":
            $ player_hit = True
        "By turning off electricity":
            $ player_hit = False
        "By changing screen settings":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_3
    jump turn5


label turn5:
    menu:
        "What is the weakest point in cybersecurity?"

    
        "Strong encryption":
            $ player_hit = False
        "Advanced software":
            $ player_hit = False
        "Human mistakes":
            $ player_hit = True
        "Fast internet":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_4
    return

label turn6:
    menu:
        "You receive a message saying: 'Your account will be locked! Act now!' What is this a sign of?"

        "It creates urgency to scare you":
            $ player_hit = True
        "It means the company is helping you":
            $ player_hit = False
        "It is safe because it sounds official":
            $ player_hit = False
        "It is just a normal reminder":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_5
    jump turn7


label turn7:
    menu:
        "Before clicking a link in a message, what should you do?"

        "Check if the message looks colorful":
            $ player_hit = False
        "Check the URL and verify it is official":
            $ player_hit = True
        "Trust it if it has a logo":
            $ player_hit = False
        "Click quickly before it expires":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_6
    jump turn8


label turn8:
    menu:
        "Why do attackers use fear and urgency in phishing messages?"

        "To make you think carefully":
            $ player_hit = False
        "To pressure you into acting without thinking":
            $ player_hit = True
        "To improve communication":
            $ player_hit = False
        "To make messages shorter":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_7
    jump turn9


label turn9:
    menu:
        "You suspect a message is fake. What should you do?"

        "Click the link to check":
            $ player_hit = False
        "Send your details to confirm":
            $ player_hit = False
        "Go directly to the official website or report it":
            $ player_hit = True
        "Ignore it and do nothing":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_8
    jump turn10


label turn10:
    menu:
        "What is the safest way to log into your account?"

        "Use links sent through email":
            $ player_hit = False
        "Visit the official website directly or use bookmarks":
            $ player_hit = True
        "Click ads or random search results":
            $ player_hit = False
        "Ask someone else for a link":
            $ player_hit = False
    
    call resolveTurn from _call_resolveTurn_9
    return

label turn11:
    menu:
        "What is malware?"

        "Malicious software designed to harm or exploit systems":
            $ player_hit = True
        "A tool used to improve performance":
            $ player_hit = False
        "A type of secure application":
            $ player_hit = False
        "A harmless background process":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_10
    jump turn12


label turn12:
    menu:
        "Which of these is a type of malware?"

        "Firewall":
            $ player_hit = False
        "Trojan":
            $ player_hit = True
        "VPN":
            $ player_hit = False
        "Operating System":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_11
    jump turn13


label turn13:
    menu:
        "How does malware commonly enter your device?"

        "By updating your system":
            $ player_hit = False
        "By clicking unsafe links or downloading unknown files":
            $ player_hit = True
        "By turning off your computer":
            $ player_hit = False
        "By using strong passwords":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_12
    jump turn14


label turn14:
    menu:
        "What can malware do once inside your device?"

        "Improve system speed":
            $ player_hit = False
        "Steal data, monitor activity, or damage files":
            $ player_hit = True
        "Fix errors automatically":
            $ player_hit = False
        "Increase storage space":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_13
    jump turn15


label turn15:
    menu:
        "How can you reduce the risk of malware?"

        "Download anything from the internet":
            $ player_hit = False
        "Install only from trusted sources and avoid suspicious links":
            $ player_hit = True
        "Ignore system updates":
            $ player_hit = False
        "Open all attachments to check them":
            $ player_hit = False

    call resolveTurn from _call_resolveTurn_14
    return
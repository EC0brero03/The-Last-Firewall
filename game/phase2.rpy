image spider:
    "spider.png"
    yalign 0.0
    xalign 0.5

define circleirisout = ImageDissolve(
    Transform("images/imagedissolve circleiris.png", zoom=1.5),
    1.0,
    8,
)

screen std_screen(game, scale=1.0):

    add Transform(game, zoom= 0.8, align= (0.5, 0.5))

    if _return:
        timer 0.1 action Return(_return)

init python:
    diff_items = []
    
    diff_items.append(STD_Item("images/difference_changes.png", 1, 5, 252, 39))
    diff_items.append(STD_Item("images/difference_changes.png", 447, 48, 582, 71))
    diff_items.append(STD_Item("images/difference_changes.png", 771, 350, 857, 383))
        
    cc = Position(xpos=0.5, xanchor='center', ypos=0.5,
                yanchor='center')
    
label phishing_attack:

    hide screen battleP
    scene black dissolve with circleirisout
    hide black dissolve
    scene black

    python:
        starttime = renpy.time.time()

        joe = SpotTheDifference("images/difference.png", diff_items)
        joe.randomizeItems(3)

        result = renpy.call_screen("std_screen", game=joe)


    $ elapsed = round(renpy.time.time() - starttime)

    i "You took [elapsed] seconds."

    if result == "win":
        i "You resisted the phishing attack!"
        $ threatHp -= 40
        jump victory

    else:
        i "You failed to identify the threat!"
        i "Try again..."
        jump phishing_attack

    return

default email_index = 0
default email_score = 0

default emails = [


    {
        "content": "From: hr@company.com\n\nThis is a reminder that the submission deadline for your timesheet is Friday at 5:00 PM.\nPlease ensure all entries are completed on time.",
        "answer": "legit"
    },

    {
        "content": "From: registrar@university.edu\n\nEnrollment for the next semester is now open.\nPlease check the student portal for your schedule and requirements.",
        "answer": "legit"
    },

    {
        "content": "From: rewards@amaz0n-gift.net\n\nCongratulations! You’ve been selected to receive a $500 gift card.\nClaim your reward immediately before it expires.",
        "answer": "phishing"
    },

    {
        "content": "From: support@bank-secure-alert.net\n\nYour banking access has been limited.\nClick the link below to confirm your identity.",
        "answer": "phishing"
    },

    {
        "content": "From: notifications@discord.com\n\nWe noticed a login to your account from a new device.\nIf this was you, you can safely ignore this message.",
        "answer": "legit"
    },

    {
        "content": "From: security-update@micr0softverify.com\n\nSuspicious login detected on your account.\nVerify your password immediately to avoid permanent suspension.",
        "answer": "phishing"
    }
]



screen emailCheck(email_content):

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 650
        background Frame("frame1.png", 20, 20)

        hbox:
            spacing 40

            frame:
                xsize 850
                ysize 550
                background Frame("frame2.png")

                vbox:
                    spacing 20
                    xpos 30
                    ypos 30

                    text "EMAIL":
                        size 40
                        color "#ffffff"
                        bold True
                        xalign 0.5

                    frame:
                        xsize 760
                        ysize 420
                        background Frame("frame3.png")

                        viewport:
                            draggable True
                            mousewheel True

                            text "[email_content]":
                                size 30
                                color "#ffffff"
                                xpos 20
                                ypos 20

            vbox:
                spacing 80
                xalign 0.5
                yalign 0.5

                textbutton " ":
                    xsize 120
                    ysize 120
                    background Frame("circle.png")

                    text_size 60
                    text_color "#fff"

                    action Return("legit")

                textbutton " ":
                    xsize 120
                    ysize 120
                    background Frame("cross.png")

                    text_size 60
                    text_color "#fff"

                    action Return("phishing")


label emailMinigame:

    $ email_index = 0
    $ score = 0

    show expression currentThreatImage as threat:
        yoffset 0
        linear 0.08 yoffset -40
        linear 0.08 yoffset 0
        linear 0.08 yoffset -20
        linear 0.08 yoffset 0

    while email_index < len(emails):

        $ current_email = emails[email_index]

        call screen emailCheck(current_email["content"])

        if _return == current_email["answer"]:

            show expression currentThreatImage as threat:
                yoffset 0
                linear 0.08 yoffset -40
                linear 0.08 yoffset 0
                linear 0.08 yoffset -20
                linear 0.08 yoffset 0

            "Impossible!!!"

            $ score += 1
            $ threatHp -= 6

            call playerAttack from _call_playerAttack

        else:

            "Haha! You Monkey!"

            $ characterHp -= 15

            call threatAttack from _call_threatAttack

        hide screen emailCheck
        with dissolve

        $ email_index += 1

    return
    
default current_cmd = ""
default tutorial_step = 0
default terminal_time = 200
default terminal_failed = False
default terminal_should_scroll = False

init python:

    terminal_history = []

    system_state = {
        "hacker_process": True,
        "malicious_ip": "185.22.44.10",
        "dns_hijacked": True,
        "system_infected": True,
        "hacker_user": True
    }

    def add_terminal(text):

        terminal_history.append(text)

        store.terminal_should_scroll = True

        renpy.restart_interaction()

    def terminal_autoscroll():

        if not store.terminal_should_scroll:
            return

        try:

            screen = renpy.get_screen("cmd_terminal")

            if not screen:
                return

            adj = screen.scope["terminal_adjustment"]

            adj.change(adj.range)

            store.terminal_should_scroll = False

        except:
            pass

    def run_command(cmd):

        cmd = cmd.strip()
        cmd_lower = cmd.lower()

        add_terminal("> " + cmd)

        output = ""

        if store.tutorial_step == 0:

            if cmd_lower == "tasklist":

                output = (
                    "chrome.exe\n"
                    "svchost.exe\n"
                    "winupdate.exe\n"
                    "cryptominer.exe [[DANGER]]\n"
                    "randomapp.exe [[DANGER]]"
                )

                store.tutorial_step = 1

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}That cryptominer process is malicious.{/color}")
                add_terminal("{color=#0084ff}Terminate it using:{/color}")
                add_terminal("{color=#0084ff}taskkill /IM cryptominer.exe /F{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Try using TASKLIST first.{/color}"

        elif store.tutorial_step == 1:

            if "taskkill" in cmd_lower and "cryptominer.exe" in cmd_lower:

                system_state["hacker_process"] = False

                output = "Process cryptominer.exe terminated successfully."

                store.tutorial_step = 2

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Good. Now check the network connections.{/color}")
                add_terminal("{color=#0084ff}Use NETSTAT.{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Remove cryptominer.exe .{/color}"

        elif store.tutorial_step == 2:

            if cmd_lower == "netstat":

                output = (
                    "Active Connections:\n"
                    "TCP 192.168.1.5:443 -> 185.22.44.10:4444 (ESTABLISHED)\n"
                    "TCP 192.168.1.5:80 -> 192.168.1.20:5321 (SUSPICIOUS)"
                )

                store.tutorial_step = 3

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}That IP is the attacker's connection.{/color}")
                add_terminal("{color=#0084ff}Block it using:{/color}")
                add_terminal("{color=#0084ff}netsh advfirewall firewall add rule name=block dir=in action=block remoteip=185.22.44.10{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Use NETSTAT.{/color}"

        elif store.tutorial_step == 3:

            if "netsh" in cmd_lower and system_state["malicious_ip"] in cmd_lower:

                output = (
                    f"Firewall rule added. "
                    f"IP {system_state['malicious_ip']} blocked."
                )

                store.tutorial_step = 4

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Nice work.")
                add_terminal("{color=#0084ff}Now check if DNS settings were hijacked.{/color}")
                add_terminal("{color=#0084ff}Use IPCONFIG.{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Block the malicious IP.{/color}"

        elif store.tutorial_step == 4:

            if cmd_lower == "ipconfig":

                output = "DNS Server: 185.66.33.99 [[COMPROMISED]]"

                store.tutorial_step = 5

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}The DNS cache is compromised.{/color}")
                add_terminal("{color=#0084ff}Flush it using:{/color}")
                add_terminal("{color=#0084ff}ipconfig /flushdns{/color}")

                return

            else:
                output = "Ishikawa: Use IPCONFIG."

        elif store.tutorial_step == 5:

            if cmd_lower == "ipconfig /flushdns":

                system_state["dns_hijacked"] = False

                output = "DNS cache successfully flushed."

                store.tutorial_step = 6

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Good.{/color}")
                add_terminal("{color=#0084ff}Now inspect user accounts.{/color}")
                add_terminal("{color=#0084ff}Use NET USER.{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Flush the DNS cache.{/color}"

        elif store.tutorial_step == 6:

            if cmd_lower == "net user":

                output = (
                    "Admin\n"
                    "Guest\n"
                    "SupportUser\n"
                    "hacker_admin [[UNAUTHORIZED]]"
                )

                store.tutorial_step = 7

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Remove the unauthorized account.{/color}")
                add_terminal("{color=#0084ff}Use:{/color}")
                add_terminal("{color=#0084ff}net user hacker_admin /delete{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Use NET USER.{/color}"

        elif store.tutorial_step == 7:

            if "hacker_admin" in cmd_lower and "/delete" in cmd_lower:

                system_state["hacker_user"] = False

                output = "User hacker_admin removed."

                store.tutorial_step = 8

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Final step.{/color}")
                add_terminal("{color=#0084ff}Repair corrupted system files.{/color}")
                add_terminal("{color=#0084ff}Use:{/color}")
                add_terminal("{color=#0084ff}sfc /scannow{/color}")

                return

            else:
                output = "{color=#0084ff}Ishikawa: Delete the hacker account.{/color}"

        elif store.tutorial_step == 8:

            if cmd_lower == "sfc /scannow":

                system_state["system_infected"] = False

                output = "System scan complete. Corrupted files repaired."

                store.tutorial_step = 9

                add_terminal(output)

                add_terminal("")
                add_terminal("{color=#0084ff}[[ISHIKAWA]]{/color}")
                add_terminal("{color=#0084ff}Excellent work.{/color}")
                add_terminal("{color=#0084ff}Threat neutralized.{/color}")


                return

            else:
                output = "{color=#0084ff}Ishikawa: Run SFC /SCANNOW.{/color}"

        else:
            output = "Command not recognized."

        add_terminal(output)

init python:

    def terminal_timer():

        if store.terminal_failed:
            return

        store.terminal_time -= 1

        if store.terminal_time <= 0:

            store.terminal_failed = True

            return

        renpy.restart_interaction()

screen cmd_terminal():

    tag cmd_terminal

    modal True

    default terminal_adjustment = ui.adjustment()

    if tutorial_step >= 9:
        timer 0.1 action Return("success")

    if terminal_failed:
        timer 0.1 action Return("fail")

    timer 1.0 repeat True action Function(terminal_timer)
    timer 0.01 repeat True action Function(terminal_autoscroll)

    key "K_RETURN" action Function(run_terminal_command)
    key "K_KP_ENTER" action Function(run_terminal_command)


    frame:
        xfill True
        yfill True
        background "#000000"

        vbox:

            xpos 20
            ypos 20

            spacing 10

            text "TERMINAL v1.0":
                color "#00ff00"
                font "windows_command_prompt.ttf"

            text "TIME REMAINING: [terminal_time]":
                color "#ff4444"
                font "windows_command_prompt.ttf"

            viewport:

                id "terminal_viewport"

                yadjustment terminal_adjustment

                mousewheel True
                draggable False
                scrollbars None

                ysize 500
                xsize 1200

                vbox:

                    spacing 4

                    for line in terminal_history:

                        text line substitute False:
                            color "#00ff00"
                            font "windows_command_prompt.ttf"

            hbox:

                spacing 5

                text "> ":
                    color "#00ff00"
                    font "windows_command_prompt.ttf"

                input:
                    value VariableInputValue("current_cmd")
                    length 200
                    color "#00ff00"
                    font "windows_command_prompt.ttf"

init python:


    def run_terminal_command():

        if store.current_cmd.strip() == "":
            return

        run_command(store.current_cmd)

        store.current_cmd = ""

        renpy.restart_interaction()


label open_terminal:

    hide screen battleP
    scene black with circleirisout
    hide black
    scene black

    $ terminal_history = []
    $ current_cmd = ""
    $ tutorial_step = 0
    $ terminal_time = 200
    $ terminal_failed = False

    call ishikawa1 from _call_ishikawa1

    $ result = renpy.call_screen("cmd_terminal")

    if result == "success":
        jump terminal_success

    elif result == "fail":
        jump terminal_fail

    return

label ishikawa1:
    
    show ishikawa frown

    i "I'm sorry..."
    i "I didn't expect the threat actor to escalate the attack this quickly."

    i "The attacker is interfering with the system..."

    i "I can't access the controls directly anymore."

    i "But I can still communicate through the terminal."

    i "Watch the terminal carefully."

    i "I'll leave instructions there."

    i "Follow them exactly if you want to stop the attack."

    hide ishikawa frown

    $ terminal_history.append("{color=#0084ff}[[ISHIKAWA]]{/color}")
    $ terminal_history.append("{color=#0084ff}First, we need to identify suspicious processes.{/color}")
    $ terminal_history.append("{color=#0084ff}Use TASKLIST.{/color}")

    return

label terminal_success:

    show ishikawa
    with dissolveS

    i "You did it."
    show ishikawa smile
    with dissolveS
    i "The system is secure again."

    jump allthreatdf

    return


label terminal_fail:

    show ishikawa armcross frown

    i "No..."
    i "We ran out of time."

    i "The attacker gained full control of the system."

    jump gameOver

    return
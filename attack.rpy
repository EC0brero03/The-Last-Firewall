define t = Character("Threat")
define you = Character("[player_name]")
default case1_facts = ['Never share passwords'] #This creates the facts inventory
default check_fact = None #This is a variable where we will store the fact you choose
default life = 50

screen your_life:
    frame:
        text "Awareness: [life]"

screen facts_list(items):
    frame:
            vbox:
                text "Security Awareness:"
                for i in items:
                    textbutton i action SetVariable('check_fact', i), Return()
                   
                textbutton "Go back" action SetVariable('check_fact', None), Return()

# The game starts here.

label trial:

    show screen your_life #Show life points

    "System" "Incoming Threat Detected..."

    $ correct_fact = 'Never share passwords'

    $ life = 50

    label statement1:

        menu:

            t "Hey, this is IT support. We detected an issue with your account."

            "Ask Questions":

                you "It support? Can you prove it?"

                t "This is time-sensitive. We don’t have much time before your account gets locked."

                if not 'Attackers create urgency' in case1_facts:
                    $ case1_facts.append('Attackers create urgency')
                    "New Knowledge Added."

                jump statement1


            "Apply Knowledge":

                call screen facts_list(case1_facts)

                if check_fact == "Attackers create urgency":
                    jump statement2
                else:
                    jump case1_failure

            "I'll think about it.":
                jump statement2

label statement2: 

        menu:
            t "I just need your password to fix it quickly."

            "Ask Questions":
                you "Why do you need my password?"

                t "It's part of the process."

                if not 'Support teams use secure verification methods' in case1_facts:
                    $ case1_facts.append('Support teams use secure verification methods')
                    "New Knowledge Added."

                jump statement2

            "Apply Knowledge":
                call screen facts_list(case1_facts)

                if check_fact == None:
                    jump statement2
                else:
                    jump case1_failure

            "I'll think about it...":
                jump statement3

label statement3: #This is the faulty statement

    menu:
        t "If you don't act now, your account will be locked permanently!"

        "Ask Questions":
            you "That sounds like pressure tactics..."
            jump statement3

        "Apply Knowledge":
            call screen facts_list(case1_facts)

            if check_fact == correct_fact:
                jump case1_objection

            elif check_fact == None:
                jump statement3

            else:
                jump case1_failure

        "This is suspicious":
            jump after_statements
                                                     

label after_statements:

    you "Something feels off... I need to think carefully."
    jump statement1

label case1_failure: 
                                
    "That doesn't prove anything..."

    t "I get your concern. This is a standard procedure— "
    extend "Just trust me so I can fix it quickly."

    $ life -= 10

    "System" "Awareness Dropped!"

    if life <= 0:
        jump bad_end

    jump statement1
    

label case1_objection: #This is called only when you present the right evidence.

    you "STOP."

    you "You're trying to manipulate me."

    you "Legitimate services NEVER ask for passwords!"
    you "And you're using urgency to pressure me!"

    you "This is a social engineering attack!"

    jump end

label end:

    t "Tch... you caught me."

    "System Secure. Threat blocked."

label bad_end: 
                         
    "You were tricked. Your account has been compromised."

    return
label insist_furry:
    Y "I want to help you."
    "You lead him over to the couch, and he begins to bawl"
    "He tells you stories of how he met Fiona, the adventures they went on, and the life they had."
    #S "(something sweet about his children)"
    S "I should have gone with her that fateful day."

    menu:
        "Blame him for her death":
            Y "Yeah, but..."
            "He breaks down even further."
            "Oops."
            "You feel awkward, so you let him cry it out."
            jump asked_to_leave

        "Reassure him":
            Y "There's no way you could've known, Shrek."

    S "B-but..."
    "You grab his face. It is covered in snot and tears."
    Y "LOOK AT ME!"
    Y "THIS IS NOT YOUR FAULT."
    "He begins to cry again, so you pull him into you."

    menu:
        "Push him off you":
            Y "Ew! You're getting snot all over me! Get off!"
            "He pulls away from you and whimpers."
            "Great job, jerk. Now you feel guilty for yelling at this poor, inoccent ogre in his time of need."

            menu:
                "Apologize":
                    Y "Listen, I'm sorry. It's just that you were dirtying my work shirt with your snot, and its kinda gross."
                    S "Gross?"
                    S "She never found me gross."
                    S "She was the only person in the world who accepted me for me. Flaws and all."
                    "He wails and begins crying again. With the air tense and awkward, you're not sure what to do."
                    "You end up just sitting next to him as he cries it out."
                    "He sniffs and goes quiet for a while."
                    jump asked_to_leave

                "Hug him":
                    Y "I'm sorry, bring it in, Shrek."
                    "You pull him into you."

        "Be a shoulder to cry on":
            "You pull him into you."

    "His tears and snot are getting your work shirt dirty, but you don't mind."
    S "Thank you."
    "You smile back and hug him again."
    "The two of you stay like that for a while."
    "You glance outside and notice that it started getting dark."
    "Panicking, you quickly pull away from him and tell him,"
    Y "Oh no! I have to return my mail bag before the post office closes!"
    "You turn to him and notice him staring at your lips."
    S "Can’t you return it tomorrow?"
    "He says it in a husky voice, still staring at your lips, which causes you to blush."
    Y "B-but I have to return it or else my boss will be angry with me..."
    "You get up to leave, but he grabs your hand."
    S "Ok, but could I at least get your number before you go?"
    Y "Of course!"
    "You gesture for his phone, and you enter in your contact information. After you hand him his phone back, he giggles."
    S "I guess we'll be seeing each other more often."
    "He winks at you, and you bite your lip. You wave and head on your way."
    "Before you even reach the door, he shouts at you."
    S "Wait! There's something I want to show you."
    "Puzzled, you stare at him for a second. He gestures for you to wait, and he races towards a hallway."
    "He comes out later dressed as...donkey???"
    S "Ta-da!"
    "He is really proud of that costume."
    menu:
        "Giggle":
            jump giggle
        "Cringe":
            jump cringe


label asked_to_leave:
    S "I'm sorry, but could you give me some space? I need to be alone right now."
    "You nod and get up to leave."
    "As you open the door, you glance at him one last time. You can't help but feel bad."
    "You failed to comfort your idol at his most vulnerable."
    "You glance down and leave his apartment."

    "On your walk home, you notice some people stumbling into a car."
    "Noticeably, the one who entered the drivers seat doesn't appear to be sober."
    menu:
        "Intervene":
            jump intervene_drunks
        "Leave it alone":
            jump leave_drunks

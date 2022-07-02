label insist_furry:
    Y "I want to help you."
    "You lead him over to the couch, and he begins to bawl"
    "He tells you stories of how he met Fiona, the adventures they went on, and the life they had."
    S "(something sweet about his children)"
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
    "[placeholder]"
    S "Thank you, "

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

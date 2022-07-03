label strip_club:
    "He extends his arm, and you grab it."
    "He leads you towards a nightclub."
    "You head inside and hear the oontz oontz music begin playing."
    Y "{i}Oh wow, these men are gorgeous.{/i}"
    "The two of you walk past the stage and towards the bar."
    "The cosplayer motions for the bartender."
    S "One platter of wings, extra spicy, please."
    Y "{i}Extra spicy? You can't handle spice!{/i}"
    Y "{i}Well, you can't handle anything. You're kinda like a widdle baby.{/i}"
    S "Oh, and 2 Jack and Cokes, please."
    "He hands his card over to the bartender."
    "You happen to notice that it's a black card."
    "ADD MORE DIALOGUE HERE TO DEVELOP THEIR RELATIONSHIP"
    #have the player blance between eating and talking

    "After a few more Jack and Cokes, the cosplayer begins slurring his speech a bit."
    "He slams his fist down on the bar, knocking the remaining wings to the floor."
    "You look down at the wings sadly, but you immediately go back to looking at him as he starts to belt."
    S "SOMEBODY ONCE TOLD ME THE W-"
    "He doesn't get to finish as he is interrupted by his own vomit."
    "Ew. It gets all over the floor and wings on the floor."
    "The bartender glares at the two of you as he continues singing."
    S "IN THE SHAPE OF AN \"L\" ON HER FOREHEAD."
    "At this point he stands up and begins undressing."

    #show shrek_shirtless
    if hearts >= 3:
        "Wait a second."
        "..."
        "..."
        "SHREK?????"
        Y "WAIT! You're ACTUALLY Shrek?"
        "He looks at you confused."
        S "That's my name~"
    else:
        "Disgusted, you quickly get up and march out of the club."
        "The cosplayer is too wasted to even notice you gone, and that stings a bit."
        #scene street
        "You hesitate and glance back."
        "You swallow your emotions and quickly head home."
        #scene black
        "..."
        #scene apartment
        "Lying in your bed that night you reflect on the day's events."
        "It was an adventure hanging out with him."
        "Even though you only knew him for day, your heart longs for him."
        "You think about when you flew into his arms on the train and you blush a bit."
        Y "{i}I wish I had someone to hold me like that all the time...{/i}"
        "BAD END: Forever Alone"
        return

    "He gets on the bar now."
    "You notice the bartender run towards the back, so you frantically try and get him off the bar."
    "It doesn't work."
    "The bartender returns with what you assume to be the owner, and they begin to berate Shrek."
    Character("Bartender") "Sir, please get off the counter!"
    Character("Owner") "GET OFF MY BAR!"
    S "Sowwy~"
    "He climbs off the counter and tries to get back in the chair."
    Character("Owner") "Get out."
    "Other patrons have begun to stare."
    "You gently grab Shrek's arm to urge him to leave."
    "He looks so defeated, but you're able to drag him out of the club."
    "The two of you stumble onto the dimly lit street."
    "You pull out your phone to call him a Cuber."
    "When it arrives, he falls in the back and smiles at you."
    S "It was nice meeting you~"
    Y "S-same!"
    "You close the door and the car drives off."
    Y "{i}Oh no! I didn't get his number!{/i}"
    

    return

label strip_club:
    scene strip_club with dissolve
    "You head inside and hear the oontz oontz music begin playing."
    Y "{i}Oh wow, these men are gorgeous.{/i}"
    show shrek_cosplay at enter_m
    "The two of you walk past the stage and towards the bar."
    "The cosplayer motions for the bartender."
    S "One platter of wings, extra spicy, please."
    Y "{i}{b}Extra{/b} spicy? I can't handle spice!{/i}"
    Y "{i}Well, I can't handle anything. I'm kinda like a widdle baby.{/i}"
    Y "I'll have a burger, please."
    S "Oh, and 2 Jack and Cokes, please."
    "He hands his card over to the bartender."
    "You happen to notice that it's a black card."
    #have the player blance between eating and talking to give/remove more hearts. still max 3 appear on screen (no idea how you wanna implement this, need more info :crycat:)
    menu:
        "Talk":
            Y "This is pretty good food right?"
            $ hearts -= 1
            S "Eattt."
        "Eat":
            "You smile and take a big munch from your borger with EXTRA ONIONS."
            $ hearts += 1

    "After a few more Jack and Cokes, the cosplayer begins slurring his speech a bit."
    "He slams his fist down on the bar, knocking the remaining wings to the floor."
    "You look down at the wings sadly, but you immediately go back to looking at him as he starts to belt."
    S "SOMEBODY ONCE TOLD ME THE W-"
    "He doesn't get to finish as he is interrupted by his own vomit."
    "Ew. It gets all over the floor and wings on the floor."
    "The bartender glares at the two of you as he continues singing."
    S "IN THE SHAPE OF AN \"L\" ON HER FOREHEAD."
    "At this point he stands up and begins undressing."

    show shrek_shirtless as shrek_cosplay at exp
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
        scene city with dissolve
        "You hesitate and glance back."
        "You swallow your emotions and quickly head home."
        scene blackscreen with Dissolve(2)
        stop music fadeout(1)
        "..."
        scene studio with dissolve
        play music ogre_tears fadein(1)
        "Lying in your bed that night you reflect on the day's events."
        "It was an adventure hanging out with him."
        "Even though you only knew him for day, your heart longs for him."
        "You think about when you flew into his arms on the train and you blush a bit."
        Y "{i}I wish I had someone to hold me like that all the time...{/i}"
        stop music fadeout 1
        hide screen romance_bar with Dissolve(1)
        scene blackscreen with Dissolve(2)
        pause(1)
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
    scene city
    show shrek_shirtless:
        align(0.5, 1.0)
    "The two of you stumble onto the dimly lit street."
    "You pull out your phone to call him a Cuber."
    "When it arrives, he falls in the back and smiles at you."
    show shrek_shirtless as shrek_shirtless at exp
    S "It was nice meeting you~"
    Y "S-same!"
    hide shrek_shirtless
    "You close the door and the car drives off."
    Y "{i}Oh no! I didn't get his number!{/i}"
    "The car is well out of sight, so you can't chase after him."
    "Great job, idiot. You blew yet another chance."
    "Just go home. You pushed your luck even meeting him so take what you can get."
    "..."
    scene studio with dissolve
    "You recollect the days events."
    "Recalling the real life Shrek in the flesh shirtless makes you blush."
    "However, you're too drunk to think about it any further and pass out in your bed."
    scene blackscreen with Dissolve(2)
    $ renpy.music.set_pause(True, channel=u'music')
    pause(1)
    play sound alarm_sfx
    pause(2)
    "You wake up and check your phone."
    "You remember it going off in your dream, so it must've been going off for a while."
    stop sound
    scene studio with dissolve
    $ renpy.music.set_pause(False, channel=u'music')
    "Your eyes focus."
    Y "I'm late for work!"
    "You quickly wipe the remaining green face paint you left on from last night and throw on your work clothes."
    scene post_office with dissolve
    "You arrive to work with just a minute to spare."
    "On your locker theres a note."
    Character("Locker Note") "Attached is the new mail delivery route you'll be taking. You'll be ending in the Upper East Side. - Boss Man"
    Y "Ugh. Snooty rich people."
    "You tear the note off the locker, grab your mail bag, and head out."
    scene shrek_front_apartment with dissolve
    "You reach the end of your route, and you stand right in front of some brand new high rise."
    Y "{i}What I would give to live here.{/i}"
    "You head inside and head towards the mailboxes."
    "You open them all, and a familiar figure appears. It's Shrek!"
    show shrek_base at enter_m
    "You feel your face get hot as he approaches, so you lower your head to hide your blushing."
    #add DIALOGUE here to increase/decrease hearts again
    #He recalls the time he saved a princess with a legendary sword (Totally happened) After meeting you and moving in he recalls his first love “Fiona.” Saying her name put a reminiscent look in his eyes. He shakes it off. (what)

    if hearts >= 3:
        S "Are you free?"
        Y "Technically, my shift is over, yeah."
        S "Well, then come upstairs. I'm cooking dinner."
        jump apartment_beginning
    else:
        S "Well, it's nice seeing you again!"
        Y "Yeah!"
        Y "I'm done with my shift this was the last delivery."
        S "That's great to hear! Maybe you could get home and rest up for tomorrow's work."
        Y "{i}Is he saying I look tired?{/i}"
        "Ouch. Rejected."
        "LOL. Sucks for you."
        "Go home, nerd."
        Y "Yeah, I'll do that. See you around!"
        hide shrek_base
        "You wave at him and turn to leave."
        scene blackscreen with dissolve
        stop music fadeout(1)
        pause(1)
        scene studio with dissolve
        play music ogre_tears fadein(1)
        "When you arrive home from work, you reflect on the conversation you had with Shrek."
        "You had an opportunity to get to know your idol more, but you blew it."
        Y "{i}God, can I do anything right?{/i}"
        "your vision blurs"
        scene studio at blurry with dissolve
        "You begin to sob."
        "And sob."
        "..."
        "And..."
        "...sob."
        "You slowly drift to sleep."
        "You never wake up."
        stop music fadeout 1
        hide screen romance_bar with Dissolve(1)
        scene blackscreen with Dissolve(2)
        pause(1)
        "BAD END: Alone on a Friday Night"
        return

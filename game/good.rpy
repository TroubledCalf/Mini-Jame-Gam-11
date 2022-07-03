label good_route:
    "You nod and get up to leave."
    hide shrek_base
    "On your way out, you notice some sticky notes, so you walk over and grab one."
    "You write your number on the note and place it on his Shrek-sized fridge."
    "God, that fridge is massive."
    "You leave his beautiful apartment and return to your shitty \$2 apartment."
    scene studio with dissolve
    "That night you lie awake waiting for a call."
    "But it never arrives."
    "You slowly drift to sleep, waiting for the next day to begin."
    stop music fadeout(1)
    scene blackscreen with dissolve
    pause(1)
    scene post_office with dissolve
    play music default_theme
    "The next day just as you head out to deliver today's letters, you get a text from an unknown number."
    Y "{i}It has to be Shrek, right?{/i}"
    "It's Shrek!"
    S "Hey, when you get off work come stop by I have something I need to tell you."
    "What does that mean? Your mind races with the possibilities."
    "What could he want? Does he hate you? Did you fuck up?"
    "Should you have stayed?"
    "With countless anxiety filled thoughts you slog through your job."
    "Finally it’s time to leave and visit Shrek."
    scene shrek_front_apartment with dissolve
    "Your nerves are killing you, but nevertheless you swallow the fear welling up in your gut and you arrive at Shrek’s highrise."
    "Finally, after a minute of contemplation you knock on the door."
    "After just a few seconds of waiting he opens and you are greeted with the love of your life."
    show shrek_base at enter_m
    "He invites you in, when you enter you feel a sense of warmth radiating from Shrek."
    scene shrek_apartment
    show shrek_base at enter_m:
        align(0.5, 1.0)
    "He is definitely doing better than he was when you saw him last."
    "Despite doing better you can still feel the pain seeping through his warm smile."
    "You take a seat on his nice couch, and he plops down right next to you."
    "He places one of his MASSIVE ogre hands upon your back."
    "Ooooooooo. He's ~touching~ you. Awoooooga"
    "You feel your face get hot."
    S "So about yesterday, I think it’s only right that you know who that package was from and why it affected me so deeply."
    show shrek_reminisce as shrek_base at exp
    "He tells you how him and Fiona were beginning to hvae a rocky marriage before she died and that she must've had that sword sent to try and remind him of the good times"
    Y "I-I had no idea..I'm so s-{w=0.2} {nw}"
    "Shrek cuts you off with a big bear hug"
    show shrek_base as shrek_base at exp
    S "Let me finish you dummy, I'm not upset anymore, cause now I've got you and well after all this...I-I think I love you!!"
    "You don't know what to say, you obviously love him too, but with no way to express it....Ah who am I kidding you kiss him on the lips!! A true sign of affection"
    "After that day you quit your shitty job and live with Shrek, he provides for you and makes you the happiest Ex-Mailman alive. You are blessed to have met him"
    stop music fadeout 1
    hide screen romance_bar with Dissolve(1)
    scene blackscreen with Dissolve(2)
    pause(1)
    "GOOD END: You're a Lifesaver"
    return

label giggle:
    "You giggle a little bit."
    Y "It's cute!"
    "You say with a big bright smile."
    show shrek_shy as shrek_base
    S "You really like it?"
    Y "Yeah!"
    show shrek_laughing as shrek_base at exp
    "Shrek squeals with excitement, and he traps you in a big bear hug."
    S "Oh wait, sorry. I just got really happy for a second."
    "He says then awkwardly pulls away from you."
    Y "N-no it's okay you're a great hugger. You're so strong."
    show shrek_blush as shrek_base at zoomin
    "You slide yourself into his still open arms, and he embraces you."
    "You bury your face in his chest, and you can hear his heart beating quickly."
    "After a little while, you glance up at him, and he’s blushing."
    "The two of you lock eyes, and he slowly begins to lean in towards you."
    play sound lightning_sfx
    "Shocked, you both jump away from each other and look outside. It has begun to pour." with vpunch
    show shrek_blush as shrek_base at zoomout
    Y "Oh no! I’m gonna get soaked!"
    "You say with fear, you can't stand getting wet."
    S "You could stay here until it passes."
    "He says with a slight joy in his voice."
    Y "I would love to, but I really have to get back."
    "You say with a hint of sadness in your voice as he walks up to you and hugs you."
    show shrek_shy as shrek_base at zoomout
    S "Well, ok, but be safe, ok?"
    "You quietly nod and turn towards the door. You smile at him one last time before you leave. He looks like he wants to say something, but you’ll see him soon."
    hide shrek_base
    pause(1)
    scene blackscreen with dissolve
    stop music fadeout(1)
    pause(1)
    scene post_office with dissolve
    play music default_theme fadein(1)
    "The next day you jollily hum the tune “All Star” by Smash Mouth during your route. What has gotten into you? You’re never this happy ever about doing your job."
    "It’s too much work for too little pay, you get exactly 40 hours paid sick leave, your boss is a jerk, and you could go on and on for hours about Janelle and her warming fish in the microwave."
    "Like c’mon, Janelle, you’ve been trying to stick to these stupid fad diets for years now, and you haven’t lost an ounce."
    "I know you don’t have any medical issues, you told me, so just please for the love of god eat chicken like the rest of us. It costs nothing, it doesn’t stink, and it’s easier to prepare than your Atlantic cod."
    scene shrek_front_apartment with dissolve
    "Eventually, you arrive at the end of your route again: right in front of Shrek’s apartment complex. You walk inside, and he's waiting by the mailboxes for you, smiling."
    show shrek_base at enter_m
    S "Hey stranger!"
    "You giggle and blush. Just the sight of him standing there, a peak male specimen, makes your face hot. As you quickly sort the mail, he continues talking to you."
    hide shrek_base
    pause(1)
    scene shrek_apartment with dissolve
    "After some top-tier banter, he invites you upstairs again."
    show shrek_base at enter_m
    Y "I have to return my mail bag remember."
    show shrek_reminisce as shrek_base
    S "Oh yeah..."
    "He seems to scratch the back of his neck, but before you leave he grabs your arm." with vpunch
    show shrek_shy as shrek_base
    S "Well what if instead of returning the mail bag...You stay with me for a bit? You see, I saw how much you loved my donkey costume yesterday. So I bought you a dragon costume!"
    "You hesitate, but seeing how happy he is to have gotten you something so great, you can't help, but stay!"
    Y "Oh well okay! I can't say no to you after all!"
    "You and Shrek hang around for a bit heck he even puts his Donkey fur suit on, you of course put on the Dragon fur suit."
    "Out of nowhere he gets down on one knee. He has something very important to ask you, so you give him 110 percent of your attention."
    show shrek_blush as shrek_base
    S "%(player_name)s, I know we haven't known each other very long, but I really want you to come to a furry convention with me. UwU"
    "You gasp in shock, you never would've dreamed of this day to come, your one true love wants to go to a furry convention, WITH YOU??? Yes! Yes! 100 times yes! Ah, but you need to play it cool."
    Y "YES! YES! OMG I WOULD LOVE TO SHREK!"
    "Nailed it! Anyway after a big warm hug you take off! You have to get ready for the con tomorrow after all ;)"
    scene blackscreen with Dissolve(2)
    stop music fadeout(1)
    pause(1)
    "..."
    if hearts >= 5:
        jump kidnap
    else:
        "GOOD END: You're a... furry?"
        return

label kidnap:
    play music tragedy_of_shrek fadein(1)
    "How could this happen? You just wanted to go to a con with Shrek...but right before you got into the center you were knocked out and taken to a dark dank werehouse. You can't see anything. The man's got you blindfolded."
    Y "Let me go!! I need to meet my love at the convention!! Let me go you Furists!!"
    F "Oi! Shut ya bleeding mouth you fithy fur mutt! Don't you make me getcha a Muzzle!"
    "You feel a sharp pain in your side! The Furist just stabbed you, he just leaves the knife there, he has plans for you"
    Y "GAH- AHHHHH! SOMEONE HELP ME PLEASE!!"
    F "WHAT DID I SAY?"
    "His fist collides with your face you feel a tooth fall out of your mouth, you can also taste blood. Is this how your life ends...? You just wish you could see Shrek one more time..."
    "Suddenly a loud bang echoes throughout the werehouse you hear loud booming footsteps charge towards you."
    F "Oi! What the H- GAH!"
    "You hear the sound of skin colliding with skin then some loud crash then suddenly, there's a bright white light and you see"
    scene white with dissolve
    pause(0.5)
    show shrek_angry at enter_m
    S "%(player_name)s! Are You alright??? Gah that bastard I can't believe he'd do this to you!!"
    show shrek_reminisce as shrek_angry
    "Shrek unties you then he places a kiss upon your cheek, his voice was shaky and filled with worry, his eyes are red and puffy almost as if he had been crying. You feel nothing but pain all over your body, but to make matters worse..."
    F "Gah ha ha ha! Touching little reunion, I hate to cut things short, but your little friend there ain't got long left"
    "The Furist laughs as he pulls out a bottle simply labeled Poison"
    show shrek_angry as shrek_angry
    S "Wh-what? No No NOOOOOOOOOOO You're lying you Bastardddddddddddddddddddddddddddd!!!!!!!!!!!!!!" with vpunch
    "Shrek gently puts you down then he charges the guy before he can even defend himself Shrek's hand bursts through his chest Killing him instantly"
    "Shrek fings the lifeless man off of his arm and then wipes his hand off, before running back to you. You look weak, ready to keel over at a moments notice. This was the end"
    Y "Th-thank you...for the best time of my life....I-I hope I'll get to see you....again....some...day....."
    show shrek_crying as shrek_angry
    "Shrek bursts into tears holding you in his arms as the light fades from your eyes, He showed you the best times of your life you will always be thankful for that"
    hide screen romance_bar with Dissolve(1)
    scene blackscreen with Dissolve(2)
    pause(1)
    "True End: My One and Only"
    window hide
    show credit1 at credit
    pause(28)
    hide credit1 with dissolve
    show credit2
    pause(5)
    hide credit2 with dissolve
    pause(1)
    return

label cringe:
    $ hearts -= 5
    "You try not to show it, but your face twists into a grimace. He looks hurt."
    show shrek_sad as shrek_base at exp
    S "You don’t like it?"
    "He says that rather sadly, the expression on his face says it all."
    #note Sad shrek sprite needed
    Y "Um..."
    "You begin to say, but before even finishing you could see you reallly hurt him."

    menu:
        "Fix it":
            "You never intended to hurt your one true love, but god that stupid outfit just, ugh anyway you need to do some damage control."
            Y "Um...No no I like it, I just think that a donkey doesn’t suit you as much as something more majestic, like uh Stallion yeah that’s it!"
            Y "You’d look much better as a cool horse, much better than a stinky donkey anyway"
            jump stabbed

        "Just leave":
            jump stabbed

label stabbed:
    "You smile and laugh rubbing the back of your head, whew looks like you saved that one!"
    stop music
    show red at stab_ef
    play music tragedy_of_shrek fadein(1)
    "So you thought, but suddenly without warning you feel a sudden sharp pain in your chest."
    hide red with dissolve
    show red at stab_ef
    Y "Wh-what....?"
    hide red with dissolve
    show red with dissolve:
        alpha 0.3
    "You say in pure shock and Horror as you see a sharp object protruding from your chest"
    "Shrek had impaled you upon the sword you just returned to him, how could he????"
    show shrek_angry as shrek_base
    "He looks at you with pure disgust, a far cry from the warm bear you had come to know oh so well."
    S "You insulted my best friend, you disgusting Onion, {b}HE DIED SAVING MY LIFE AND YOU BLOODY INSULT HIM{/b}!!!"
    hide screen romance_bar with Dissolve(1)
    hide red with Dissolve(1)
    scene blackscreen with Dissolve(2)
    "Suddenly everything goes black, Shrek, fueled by pure rage, ripped the sword out and cut you into unrecognizable pieces"
    pause(1)
    "BAD END: Dice to Meat you"
    return

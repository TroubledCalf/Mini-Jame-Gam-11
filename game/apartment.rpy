label apartment_beginning:
    stop music
    play music ogre_tears fadein 1.0
    "You follow him to the elevator. He hits the top button."
    scene shrek_apartment with dissolve
    "He leads you down a pristine hallway, and he opens the door to his apartment."
    "Your jaw drops. The place is immaculate."
    "Tall ceilings, full length windows, tile floor, expensive looking furniture, and a water feature."
    Y "{i}How does he maintain that?{/i}"
    Y "{i}I guess it doesn't matter.{/i}"
    "You turn around and see him heading towards the kitchen. He puts on an apron and begins to slice an onion and puts the chopped onion in a pan."
    show shrek_base at enter_m
    "You hear a sizzle and slowly the smell wafts towards you. He looks up and smiles."

    menu:
        "Tell him it smells good":
            $ hearts += 1
            Y "That smells great!"
            show shrek_laughing as shrek_base at exp
            S "You really think so?"
            Y "Yeah! I love onions!"
            show shrek_sad as shrek_base
        "Tell him it smells terrible":
            $ hearts -= 1
            Y "Um...could you cook something else? I don't like onions."

    if hearts >= 4:
        "It feels as if you've known him for forever."
    else:
        show shrek_sad as shrek_base at exp
        S "..."
        "You can't stand this awkward silence."
        Y "{i}I gotta come up with an excuse somehow.{/i}"
        "You have an idea."
        Y "I'm not feeling well. I'm so sorry, but I'm gonna head home."
        S "Are you sure? If I look, I'm sure I can find some medicine."
        Y "No, it's perfectly fine. I worked a long day, too, so I'm kinda tired."
        S "Aw. Sorry to hear that."
        "You get up and walk towards the door."
        S "See you around, I guess."
        hide shrek_base
        "You turn back and feel a pang of guilt, but you're really uncomfortable."
        "..."
        scene blackscreen with dissolve
        stop music fadeout(1)
        pause(1)
        scene studio with dissolve
        play music ogre_tears fadein(1)
        "You lie awake feeling guilty."
        Y "{i}Should I have stayed?{/i}"
        "YES!!!"
        "You FOOL!"
        stop music fadeout 1
        hide screen romance_bar with Dissolve(1)
        scene blackscreen with Dissolve(2)
        pause(1)
        "BAD END: Fool's Gold"
        return

    show shrek_crying as shrek_base
    "He goes quiet for a second, and you notice tears well in his eyes."
    S "Onions, ya know?"

    menu:
        "Ask what's wrong":
            Y "What's wrong?"
        "Don't push it":
            "Maybe you just imagined it."
            show shrek_reminisce as shrek_base at exp
            "I can promise you that you didn't, you just don't know how to comfort people since you never talk to anyone, ever."
            "He quietly finished cooking. He plates the food and hands some over to you."
            "Mother said never to take food from strangers, so you eye it suspiciously."
            show shrek_sad as shrek_base
            S "It's my mother's recipe for skirlie."
            "Bro, you literally just watched him make it, and now you're making him feel bad? Not cool, mailman-kun. Not cool."
            "You've never even had this dish before. You live off ramen and not-so-easy mac. C'mon, man. Live a little."
            Y "It smells good!"
            "Oh, we're doing damage control now? Don't you think its a bit late for that?"
            "..."
            "The two of you eat in silence."
            "..."
            "When you both finish, he grabs your plate and places it in the sink."
            Y "Thank you for the meal!"
            show shrek_reminisce as shrek_base
            S "Unfortunately, this is probably the last meal I'll cook for someone while I'm here."
            Y "What do you mean?"
            show shrek_sad as shrek_base
            S "I'm moving out soon. I think it's time for me to finally return to Scotland. I haven't seen my children in years."
            show shrek_crying as shrek_base at exp
            S "They were grown when I left them, but so much time has passed...I don't even know if they've forgiven me."
            Y "I'll miss you."
            "Before he can respond, you turn around and leave."
            show shrek_sad as shrek_base
            hide shrek_base
            pause(1)
            scene blackscreen with dissolve
            stop music fadeout(1)
            pause(1)
            scene post_office with dissolve
            play music ogre_tears fadein(1)
            "As you change out of your uniform and place it in your locker, you can't help but feel guilty."
            Y "{i}Maybe I didn't imagine his pained face.{/i}"
            "News flash: you didn't."
            Y "{i}Should I have pressured him for an answer?{/i}"
            "Are we really doing this? Of course you should have. He clearly wanted to talk about it."
            "But who knows what could have come of it? I'm just the narrator."
            stop music fadeout 1
            hide screen romance_bar with Dissolve(1)
            scene blackscreen with Dissolve(2)
            pause(1)
            "BAD END: Blind to the Truth"
            return
    "He wipes a tear from his cheek."
    show shrek_reminisce as shrek_base at exp
    S "Nothing...you just remind me of someone I used to know."
    Y "Tell me about it. I may not be able to do much, but at the very least talking about it can ease the pain."
    "He shakes his head."
    S "I don’t want to bother you with my problems, ha."
    Y "It's ok. I won't be bothered."
    "He sighs."
    S "You sure?"
    Y "Positive."
    show shrek_sad as shrek_base at exp
    S "The night Fiona died was eight years ago."
    S "She was killed in a hit and run. The police never found the culprits."
    show shrek_crying as shrek_base
    S "It's all my fault."
    S "I should have gone with her that day, but instead I was selfish and slept in."
    S "I can't even give her a proper memorial because I lost the sword I used to rescue her years ago."
    "Could that sword have been in that teeny package you found at work? It was signed by a mysterious \"F\" after all."
    Y "Excuse me. I think I have something that belongs to you."
    hide shrek_base
    "You race to the post office."
    scene post_office with dissolve
    "You get there and check your locker. It's right where you left it!"
    "You snatch the package and race back towards Shrek's apartment."
    scene shrek_front_apartment with dissolve
    "He's waiting for you in the lobby."
    "You both take the elevator and go to his apartment."
    scene shrek_apartment with dissolve
    show shrek_base at enter_m
    show darken with dissolve
    show package with dissolve:
        align(0.5, 0.5)
    "You reveal the comically small package and place it on the kitchen counter."
    hide package with dissolve
    "You both hover over it, and you look up at Shrek expectantly."
    show sword with dissolve:
        align(0.5, 0.5)
    "He opens it slowly and pulls out a long sword."
    "It's alot longer than you thought it would be."
    Y "{i}How did that fit in that tiny box?{/i}"
    hide sword with dissolve
    hide darken with dissolve
    show shrek_crying as shrek_base at exp
    "He inspects the hilt and bursts into tears again."
    S "I-it's the sword. After so many years, I finally have it."
    "He looks up at you and embraces you tenderly."
    S "Thank you."
    "He pulls away, taking his warmth with him."
    S "I think I need to be alone right now. I know this is rude after what you've done for me, but could you leave?"

    menu:
        "Leave":
            jump good_route
        "Insist to stay":
            jump insist_furry

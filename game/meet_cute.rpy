label train:
    #show subway
    "There you see him."
    "Another perfect cosplay,"
    "Shrek as Fiona."
    "You are flustered and accidentally make eye contact on the train."
    "Once your eyes lock a second time you finally gain the courage to walk up to him."
    Y "H-hello, I am %(player_name)s, also known as Mailman-kun. uWu"
    S "Nice cosplay, %(player_name)s."
    "He smiles gently at you."
    S "How long did it take?"
    Y "Uhhhhh...t-three months"
    "His eyes go wide, but then he regains his gentle smile."
    S "Wow. That's some real dedication. I'm honored."
    Y "Y-yeah."
    "There's an awkward silence, and the Shrek/Fiona cosplayer scratches his head."
    menu:
        "Break the awkward silence":
            $ hearts += 1
            "You look up at him and smile."
            Y "Where did you get that wig from? It looks so good!"
            "He lights up."
            S "Oh, this old thing? I bought some cheap hair and bleached and dyed it myself."
            Y "Woah! That’s amazing I could never do that, I had to just buy this silly bald mask, you can still see my hair, haha."
            S "It still looks good though!"
            "The silence returns."
            "You open your mouth to continue the conversation, but the train grinds to a halt."

            "Stare at him lovingly"
            "He notices your stare, and his eyes dart around."
            "Idiot, you have clearly made him uncomfortable."
            "Uhhh...do you want a picture...or...?"
            Y "AH! I'm so sorry! I-i didn't mean to."
            "The two of you return to the silence."
            "Embarrassed, you faint."
            "Just before you black out, you catch a glimpse of a concerned and creeped out Shrek/Fiona cosplayer."
            "BAD END: Way to go, Dumbass"
            return

    "You fly forward and fly into the cosplayer's arms."
    "Immediately, your face gets hot as you realize that you're buried in his chest."
    "Trying to pry yourself off of him, you notice that his costume feels {i}really{/i} real."
    "He grabs your shoulders and gently pushes you off of him."
    "He doesn't make eye contact as you try to regain your stability."
    S "Well, here's the convention center."
    Y "U-uh, yeah. I'll, uh, see you inside?"
    S "Maybe."
    S "Also, do you have any more of that face paint? It kinda...smeared."
    "You pull out your phone to check and nearly scream."
    "You glance back at him to see how it smeared on him, but because of the color of his dress, no harm is done."
    "The only problem is that you now look ridiculous."
    "I wish we had time to make an asset for it because you look really dumb."
    "You quickly dash off the train, covering your face in fear of judgement and race to the convention center. There'll be a bathroom there, right?"
    "..."

    jump convention

label convention:
    "As you wait in line to get in, you notice you're getting stares."
    Y "Is my cosplay that good?"
    Character("Mean Stranger") "No. You look stupid. Your face and forehead are two completely different colors."
    Character("Mean Stranger") "It looks weird."
    Y "O-oh..."
    "..."
    "Once inside, you race to the bathroom. Luckily, you did bring some extra green face paint."
    "You begin to smear it all over your face."
    "As other cosplayers walk in and out of the bathroom, you can't help but feel self conscious."
    "Their cosplays are all amazing."
    "They have perfect bodies."
    "Their makeup is impeccable."
    Y "{i}I bet their idols would be proud of them{/i}"

    menu:
        "Cry in the bathroom stall":
            "You quickly rush towards the nearest empty stall and begin to bawl."
            "You bury your face in your hands and begin to sob quietly."
            "After you're done, you open your eyes and see green drops on your hands and shirt."
            Y "Great. My face paint ran again."
            "You leave the stall, wash your hands, and head back into the crowd."
        "Brush it off":
            $ face_paint = True
            "You can't cry here, your face paint will run again."
            "After a few seconds of trying to cheer yourself up in the mirror, you regain your composure and head back into the crowd."

    "The first place you head towards is the meet-and-greet booths. You want to meet your favorite comic books and manga artists as well as your favorite voice actors."
    "You get to meet some of the people behind People 5, Multiple Pieces, Chiropractor What, and Dogdude."
    "It's like a dream come true."
    "While you're in line to meet one of the artists behind Livingpool, you spot a familiar face in line."
    Y "You confidently walk up to him."

    if face_paint:
        S "I see you fixed your cosplay."
        Y "Yeah! I wouldn't be able to fully capture Shrek's beauty and grace if I didn't."
        "I think you went too far again, buddy. He looks uncomfortable."
        S "Haha...yeah."
    else:
        $ hearts += 1
        "He stares for a long while."
        "He smiles."
        S "Honestly, props to you for walking around like that, ha ha."
        Y "I'm doing my best here, man."
    Y "Anyway...you like Livingpool?"
    "His eyes light up, and he beings fangirling."
    "..."
    "You both finally get to the front of the line."

    if hearts >= 3:
        S "So, you free after this?"
        Y "Depends on what you have in mind."
        S "Well, theres a strip club down the street."
        Y "Oooo. Spicy."
        S "Yeah, the food is great! I used to go there all the time I was visiting NYC with an uh...old friend of mine."
        S "She was there for the guys, and after a few times of being dragged there begrudgingly, I discovered their wing menu and was hooked."
        S "She used to think I was two-timing because I used to fly here all the way from Scotland just for the food."
    else:
        S "Well, it was nice meeting you!"
        Y "Yeah, same!"
        Y "I know I said it a million times, but your cosplay is really good!"

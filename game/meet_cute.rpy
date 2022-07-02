label train:
    #scene train
    "There you see him."
    #show fiona shrek neutral
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
    #show fiona shrek uncomfortable
    "There's an awkward silence, and the Shrek/Fiona cosplayer scratches his head."
    menu:
        "Break the awkward silence":
            $ hearts += 1
            "You look up at him and smile."
            Y "Where did you get that wig from? It looks so good!"
            #show shrek_blush
            "He lights up."
            S "Oh, this old thing? I bought some cheap hair and bleached and dyed it myself."
            Y "Woah! That’s amazing I could never do that, I had to just buy this silly bald mask, you can still see my hair, haha."
            S "It still looks good though!"
            "The silence returns."
            "You open your mouth to continue the conversation, but the train grinds to a halt."

        "Stare at him lovingly":
            "He notices your stare, and his eyes dart around."
            "Idiot, you have clearly made him uncomfortable."
            "Uhhh...do you want a picture...or...?"
            Y "AH! I'm so sorry! I-i didn't mean to."
            "The two of you return to the silence."
            #show black
            "Embarrassed, you faint."
            "Just before you black out, you catch a glimpse of a concerned and creeped out Shrek/Fiona cosplayer."
            "BAD END: Way to go, Dumbass"
            return

    #show shrek shy zoom
    "You fly forward and fly into the cosplayer's arms."
    "Immediately, your face gets hot as you realize that you're buried in his chest."
    "Trying to pry yourself off of him, you notice that his costume feels {i}really{/i} real."
    #show shrek shy
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
    #hide shrek
    jump convention

label convention:
    #scene convention
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
    Y "{i}I bet their idols would be proud of them.{/i}"

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
    #show shrek base
    "While you're in line to meet one of the artists behind Livingpool, you spot a familiar face in line."
    Y "You confidently walk up to him."

    if face_paint:
        S "I see you fixed your cosplay."
        Y "Yeah! I wouldn't be able to fully capture Shrek's beauty and grace if I didn't."
        #show shrek shy
        "I think you went too far again, buddy. He looks uncomfortable."
        S "Haha...yeah."
    else:
        $ hearts += 1
        "He stares for a long while."
        "He smiles."
        S "Honestly, props to you for walking around like that, ha ha."
        Y "I'm doing my best here, man."
    Y "Anyway...you like Livingpool?"
    #show shrek base
    "His eyes light up, and he beings fangirling."
    "Time passes quickly as you admire him speak so passionately about Livingpool."
    "In no time at all you both finally get to the front of the line."

    menu:
        "Fangirl to the artist":
            Y "OH MY GOD!!! I LOVE YOUR WORK SO MUCH. IT MEANS SO MUCH TO ME!!!"
            #show shrek shy
            "You have made both the cosplayer and the artist uncomfortable."
            S "Uh...yeah. I also love your work."
            "The artist glances between the two of you."
            S "Yeah, so, could you sign this?"
            "The cosplayer hands the artist a notebook."
            "The artist nods and takes it. He quickly signs it and returns it."
            "He then turns to you expectantly."
            Y "U-u-uh."
            "You pat your pockets and realize you forgot your notebook."
            "You glance up at the cosplayer with a guilty smile."
            "He sighs and rips out a page from his notebook."
            "You hand the paper to the artist. After he signs it, he once again glances between the two of you."
            Character(player_name + " and Cosplayer") "Thank you!"
            "You cheerily squeal, and you and the cosplayer turn to leave."
        "Ask for a signature and leave":
            $ hearts += 1
            Y "H-hi!"
            Y "I'm %(player_name)s. It's so nice to finally meet you!"
            "The artist smiles as you hand him a notebook."
            "The cosplayer does the same."
            "The artist signs both notebooks, and you both thank him and turn to leave."

    if hearts >= 3:
        #show shrek base
        S "So, you free after this?"
        Y "Depends on what you have in mind."
        S "Well, theres a strip club down the street."
        Y "Oooo. Spicy."
        #show shrek reminisce
        S "Yeah, the food is great! I used to go there all the time I was visiting NYC with an uh...old friend of mine."
        S "She was there for the guys, and after a few times of being dragged there begrudgingly, I discovered their wing menu and was hooked."
        S "She used to think I was two-timing her because I used to fly here all the way from Scotland just for the food."
        Y "Sounds great! Lets go, then!"
        jump strip_club
    else:
        #show shrek base
        Y "Well, it was nice meeting you!"
        S "Yeah!"
        Y "I know I said it a million times, but your cosplay is really good!"
        S "Thank you!"
    "You both awkwardly look down at the ground."
    "After a while, the cosplayer looks up at you and waves."
    S "See you around, I guess."
    Y "Y-yeah."
    #hide shrek
    "You can't help but feel disappointed as you watch him walk away."
    Y "{i}Why does this keep happening?{/i}"
    Y "{i}What is it about me that makes everyone keep walking away?{/i}"
    "You choke back tears as you turn away and head home."
    "..."
    #scene apartment
    "As you lie in your shabby \$2 apartment, you recall the days events."
    "Could it have gone better?"
    "Maybe you could've at the very least made a friend?"
    Y "{i}Is this why I don't have anyone?{/i}"
    Y "{i}No friends, no partner.{/i}"
    Y "{i}Just lil' ol' me.{/i}"
    "You can't even bother to clean off the green makeup. You just let the darkness consume you as you drift to sleep."
    "BAD END: Waste of Space (prlly rename that one)"

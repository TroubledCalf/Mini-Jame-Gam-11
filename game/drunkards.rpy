label intervene_drunks:
    $ drunks = True

    Y "HEY!"
    "You briskly walk towards them."
    "The ones sober enough to realize what's going on turn towards you. The others continue to try stopping themselves from vomiting."
    B "What the hell do you want?!"
    Y "For you to get home safe!"
    "You smile at them."
    B "Why the hell do you care?"
    Y "Because...because I can!"
    "You firmly plant yourself next to the group and pull out your phone to call them a Cuber."
    "The one who shouted at you eyes you suspiciously, but you think they understand."
    "After a few minutes, the Cuber arrives, and they all pile in. The belligerent one glares at you one last time as they drive away."
    "It doesn't matter, though. You feel good. You don't know what could have happened if you didn't intervene."

    "This feeling is fleeting, however, and soon guilt sets in."
    scene blackscreen with Dissolve(2)
    "Head heavy, you return home and prepare for work the next day."

    jump drunks


label leave_drunks:
    scene blackscreen with dissolve
    "Once you get to work, your mind is all foggy. You can only think about what you should have said."
    "You should’ve comforted him better."
    "You shouldn’t have been so squeamish."
    "There are a million “shoulds” that you didn’t do."
    "..."
    "Weeks go by and you notice that you haven’t delivered a single letter to his apartment."
    "This also bothers you, and it starts to affect your work. Your boss notices your change and calls you into their office one day..."
    "..."
    "Months go by. You’ve been in and out of shelters and bouncing from friend’s couches for months now."
    scene city with dissolve
    "Right now you’re wandering around NYC looking for a place to spend the night."
    scene convention_center with dissolve
    "On your walk, you stroll by the convention center where you met Shrek."
    Y "{i}If only...{/i}"
    "Tired and defeated, you collapse on the street, but noone notices." with vpunch
    scene blackscreen with Dissolve(2)

    jump drunks


label drunks:
    if drunks:
        "As your vision fades to black, you hear murmurs of \"druggie\" and \"drunkard.\""
        "The last thing you feel before the darkness consumes you is a tear roll down your cheek, and you can't help but giggle a bit."
        Y "{i}Is this how it feels to be alone?{/i}"
    else:
        "As your vision fades to black, you catch a glimpse of a passing cab. The ad on top is an anti drinking and driving campaign."
        Y "{i}Has is already been that long since that fateful night?{/i}"
        "The night you walked away from him, and he chased after you. He met the same fate his beloved Fiona did, hit by a couple of drunks in a hit and run."
        "You've long since lost the blood-stained note he had in his hand, but you still remember what it said."
        SN "For the first time in a long time, someone made me feel whole again."
        SN "Since we first spoke, you made me feel warm. You gave me butterflies in my stomach."
        SN "It was like meeting an old friend that I hadn't seen in years."
        SN "After losing Fiona and losing contact with my children, that small talk we had really changed my mind."
        SN "I made sure before I left that I called my children to remind them how proud I am of them and how much I love them."
        SN "For years, I was afraid that they would reject me again, but because of you, I'm not afraid anymore."
        SN "I feel as though I'm on top of the world, but I don't want to risk losing you, too."
        SN "I've lost so much already, so please, I'm begging you. Come back to me."
        "Even though you knew him for just a day, you were able to be a shining light in darkness for him. You meant so much to him."
        "Sometimes all someone needs is a shoulder to cry on."
        Y "{i}So why did I walk away?{/i}"

    "You never even delivered that weird package you found."
    "What happened to it anyway?"
    stop music fadeout 1
    hide screen romance_bar with Dissolve(1)
    scene blackscreen with Dissolve(2)
    pause(1)
    "BAD END: Consumed by Guilt"
    return

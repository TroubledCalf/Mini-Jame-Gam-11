#python
init:
    $ renpy.music.register_channel("blips", mixer=None, loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True)
init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/v1.ogg", loop=True, channel="blips")
        elif event == "slow_done":
            renpy.sound.stop(channel="blips")

#sound files
define audio.default_theme = "./audio/Out_n_about.mp3"

#tracker varibles
define hearts = 0
define furry = False
define drunks = False

#define characters
define S = Character("Shrek")
define player_name = ""
define Y = Character(player_name)
define B = Character("Drunk Rando")
define SN = Character("Shrek's Note")


#define misc
define config.character_callback = beepy_voice

label start:

    #opening mailroom
    Y "UGHHHHHH"
    Y "My back hurts"
    "You grumpily waltz over to your locker."

    $ player_name = renpy.input("Each locker has a name tag and yours says:")
    $ Y = Character(player_name)

    "After changing into your uniform, you head on over to the mailroom."
    "This whole \"mailman\" job is grueling."
    "You have to wake up early every day and lug a heavy bag around New York City."
    "You walk on over to the mailroom, and notice a small package thats hidden beneath your mailbag."
    "It has no return address and is in plain packaging. There's a note attached to the outside that reads:"
    Character("Package") "To my dearly beloved, I will always treasure the day you came for me. Here is my greatest possession: the tool to my heart. - F."

    "Do you find the packages owner?"
    menu:
        "Don't bother":
            "You don't get paid enough to hunt down randos."
            "BAD END: Minimum Wage"
            return
        "Find Owner":
            "Determined to find the owner, you ask around the office if it belongs to anyone, as a dutiful mailman would."
            "Noone recognizes it, so you place it in your locker to take home after your shift."

    "When you finally end your long shift, you head to your \$2 shabby apartment.
    "It's Friday night, so there are a lot of couples out. Living in a large city, you see them all the time, but you can’t help but feel hurt and lonely."
    "You're getting old."
    "Your mother does a good job of reminding you that your window to find love is closing."
    Character("Mother") "The only people available when you get old are divorcees and creeps."
    "You can hear her scoffing at you even in your flashback."
    "However, there is some glimmer of hope."
    "Tomorrow you have plans; tomorrow you’re going to..."
    "COMIC CON!!!"
    "Cheered up by this fact, you skip all the way home, ignoring all the judging stares."

    #fade to black
    #show your apartment
    "You wake up bright and early ready to take on the day."
    "You've spent months procuring the perfect cosplay."
    "It took a lot of green paint. It's heavy, too."
    "You admire yourself in the mirror."
    "Your Shrek cosplay is perfect."
    "You're too short to accurately capture his beauty, but otherwise, you have the look down pat."
    "You have his signature green, his striking ears, and his sexy dad bod."
    "Excited and proud of your work, you merrily leave your apartment and head towards the subway."

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
            Y "Woah! That’s amazing I could never do that, I had to just buy this silly face mask, you can still see my hair, haha."
            S "It still looks good though!"
            "The silence returns."
            "You open your mouth to continue the conversation, but the train grinds to a halt."

        "Stare at him lovingly":
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
    Y "U-uh, yeah. Maybe I'll see you inside?"
    S "Maybe."
    S "Also, do you have any more of that face paint? It kinda...smeared."


    #just to test the possible furry route
    jump insist_furry


    return

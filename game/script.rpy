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
define audio.ogre_tears = "./audio/Ogre_Tears.mp3"

#tracker varibles
define hearts = 0
define furry = False
define drunks = False
define face_paint = False

#define characters
define S = Character("Shrek")
define player_name = ""
define Y = Character(player_name)
define B = Character("Drunk Rando")
define SN = Character("Shrek's Note")
define F = Character("Furists")


#define misc
define config.character_callback = beepy_voice

label start:
    stop music
    show screen romance_bar
    #opening mailroom

    Y "UGHHHHHH"
    Y "My back hurts."
    "You grumpily waltz over to your locker."

    $ player_name = renpy.input("Each locker has a name tag and yours says:")
    $ Y = Character(player_name)

    play music default_theme
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

    "When you finally end your long shift, you head to your \$2 shabby apartment."
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

    jump train
    #goes to passed_convention.rpy


    return

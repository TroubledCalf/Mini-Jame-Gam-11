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

#defaults

#define characters
define S = Character("Shrek")
define player_name = ""
define Y = Character(player_name)


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
    "This whole 'mailman' job is grueling."
    "You have to wake up early every day and lug a heavy bag around New York City."
    "You walk on over to the mailroom, and notice a small package thats hidden beneath your mailbag."
    "It has no return address and is in plain packaging. There's a note attached to the outside that reads:"
    Character("Package") "To my dearly beloved, I will always treasure the day you came for me. Here is my greatest possession: the tool to my heart. - F."
    "Do you find the packages owner?"
    menu:
        "Don't bother":
            "You don't get paid enough to hunt down randos."
            "BAD END"
            return
        "Find Owner":
            "Determined to find the owner, you ask around the office if it belongs to anyone, as a dutiful mailman would."
            "Noone recognizes it, so you place it in your locker to take home after your shift."
        

    return

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

#define misc
define config.character_callback = beepy_voice

label start:

    S "Ayo this is a test"
    "double test"

    return

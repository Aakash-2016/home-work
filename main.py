def on_forever():
    basic.show_leds("""
        . . . . .
        . . # # #
        # # # # .
        # # # . .
        # . # . .
        """)
    basic.show_leds("""
        . . . . .
        # # # . .
        . # # # #
        . . # # #
        . . # . #
        """)
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(262, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(247, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
    music.play(music.tone_playable(196, music.beat(BeatFraction.EIGHTH)),
        music.PlaybackMode.IN_BACKGROUND)
basic.forever(on_forever)

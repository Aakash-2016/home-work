basic.forever(function () {
    basic.showLeds(`
        . . . . .
        . . # # #
        # # # # .
        # # # . .
        # . # . .
        `)
    basic.pause(200)
    basic.showLeds(`
        . . . . .
        # # # . .
        . # # # #
        . . # # #
        . . # . #
        `)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(262, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(247, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
    music.play(music.tonePlayable(196, music.beat(BeatFraction.Eighth)), music.PlaybackMode.InBackground)
})

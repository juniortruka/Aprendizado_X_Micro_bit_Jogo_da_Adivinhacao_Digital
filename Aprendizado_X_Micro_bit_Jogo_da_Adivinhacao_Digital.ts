// Jogo da adivinhação 
let index = 0
let text_list: string[] = ["CACHORRINHO", "RELOGIO", "NOITE"]

game.startCountdown(30000)

// Quando o micro:bit vira com o logo para cima → mostra a palavra
input.onGesture(Gesture.LogoUp, function () {
    index = randint(0, text_list.length - 1)

    // Som antes de mostrar a palavra
    music.playTone(440, music.beat(BeatFraction.Quarter))

    basic.showString(text_list[index])
})

// Virou a tela para baixo → acertou → ganha ponto
input.onGesture(Gesture.ScreenDown, function () {
    game.addScore(1)

    // Som de ponto
    music.playTone(880, music.beat(BeatFraction.Half))
})

// Virou a tela para cima → errou → perde vida
input.onGesture(Gesture.ScreenUp, function () {
    game.removeLife(1)

    // Som de erro
    music.playTone(131, music.beat(BeatFraction.Half))
})

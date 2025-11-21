# Jogo da adivinhação com SOM
index = 0
text_list: List[str] = ["CACHORRINHO", "RELOGIO", "NOITE"]
game.start_countdown(30000)
# Quando o micro:bit vira com o logo para cima → mostra a palavra

def on_gesture_logo_up():
    global index
    index = randint(0, len(text_list) - 1)
    # Som antes de mostrar a palavra
    music.play_tone(440, music.beat(BeatFraction.QUARTER))
    basic.show_string(text_list[index])
input.on_gesture(Gesture.LOGO_UP, on_gesture_logo_up)

# Virou a tela para baixo → acertou → ganha ponto

def on_gesture_screen_down():
    game.add_score(1)
    # Som de ponto
    music.play_tone(880, music.beat(BeatFraction.HALF))
input.on_gesture(Gesture.SCREEN_DOWN, on_gesture_screen_down)

# Virou a tela para cima → errou → perde vida

def on_gesture_screen_up():
    game.remove_life(1)
    # Som de erro
    music.play_tone(131, music.beat(BeatFraction.HALF))
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

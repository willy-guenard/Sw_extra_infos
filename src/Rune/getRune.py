def get_infos_rune(dataAeraGames):
    screanshotRune = get_screan_rune(dataAeraGames)

    rune = Rune(screanshotRune)

    rune.calculate_Rating()
    rune.show_Rating()

def get_screan_rune ():
    get_aera_rune()
    pass

def get_aera_rune():
    pass
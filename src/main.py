from Aera_games.findAeraGames import find_aera_emulater, check_aera_emulater
from Rune.getRune import get_infos_rune
# from Artifacts.getArtifacts import get_infos_artefact
# from Sieges.getOffance import get_offance

if __name__ == '__main__':
    running = True
    aeraEmuIsFind = False
    dataAeraGames = ""
    while running:

        # attendre de savoir ce que veut le user truc visuel ?
        userWant = input("tu veut quoi ?")

        aeraEmuIsFind = check_aera_emulater(dataAeraGames)

        if not aeraEmuIsFind:
            dataAeraGames = find_aera_emulater()

        if userWant == "Rune" :
            get_infos_rune(dataAeraGames)
        # elif userWant == "Artifacts":
        #     get_infos_artefact(dataAeraGames)
        # elif userWant == "Sieges":
        #     get_offance(dataAeraGames)

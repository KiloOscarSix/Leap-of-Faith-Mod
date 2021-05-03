init python:
    def isUpToDate(fileName, url):
        import requests
        import hashlib

        f = open(fileName, "r")
        file = f.read()
        f.close()
        hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

        urlcode = requests.get(url).text
        urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

        if hash == urlhash:
            return True
        return False

    def upToDate():
        modConfigPath = os.path.join(config.basedir, "game", "modAdditions", "modConfig.txt")
        try:
            return isUpToDate(modConfigPath, "https://raw.githubusercontent.com/KiloOscarSix/Sun-Breed-Mod/main/game/modAdditions/modConfig.txt")
        except:
            return True


label after_load:

    if ep2Eyecontact == 3:
        menu:
            mod "To prevent future bugs we have reverted the take picture of both girls improvement, please select which girl you would like to take a picture of"
            "Cece":
                $ ep2Eyecontact = 1
            "Linda":
                $ ep2Eyecontact = 2

    if MenuChoice == " ":
        call screen MenuScreen nopredict

        $ MenuChoice = _return[0]
        $ Best = "{color=" + _return[1] + "}"
        $ Worst = "{color=" + _return[2] + "}"
        $ Good = "{color=" + _return[3] + "}"
        $ Bad = "{color=" + _return[4] + "}"

        if MenuChoice == "HintsNone":
            call MenusHintsNone
        elif MenuChoice == "HintsStatsAllGirls":
            call MenusHintsStatsAllGirls
        elif MenuChoice == "HintsAllGirls":
            call MenusHintsAllGirls
        elif MenuChoice == "HintsStatsCece":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsCece
        elif MenuChoice == "HintsStatsLexi":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsLexi
        elif MenuChoice == "HintsStatsLinda":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsLinda
        elif MenuChoice == "HintsStatsKira":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsKira
        elif MenuChoice == "HintsStatsRobin":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsRobin
        elif MenuChoice == "HintsStatsStephanie":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsStephanie
        elif MenuChoice == "HintsStatsKiraRobin":
            call MenusHintsStatsAllGirls
            call MenusHintsStatsKiraRobin
        elif MenuChoice == "HintsCece":
            call MenusHintsAllGirls
            call MenusHintsCece
        elif MenuChoice == "HintsLexi":
            call MenusHintsAllGirls
            call MenusHintsLexi
        elif MenuChoice == "HintsLinda":
            call MenusHintsAllGirls
            call MenusHintsLinda
        elif MenuChoice == "HintsKira":
            call MenusHintsAllGirls
            call MenusHintsKira
        elif MenuChoice == "HintsRobin":
            call MenusHintsAllGirls
            call MenusHintsRobin
        elif MenuChoice == "HintsStephanie":
            call MenusHintsAllGirls
            call MenusHintsStephanie
        elif MenuChoice == "HintsKiraRobin":
            call MenusHintsAllGirls
            call MenusHintsKiraRobin
        else:
            call MenusHintsNone
    return

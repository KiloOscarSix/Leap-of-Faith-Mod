init python:
    try:
        import requests
        import hashlib
        import logging
    except:
        pass
    else:
        def isUpToDate(fileName, url):
            f = open(fileName, "r")
            file = f.read()
            f.close()
            hash = hashlib.sha256((file).encode('utf-8')).hexdigest()

            urlcode = requests.get(url).text
            urlhash = hashlib.sha256((urlcode).encode('utf-8')).hexdigest()

            if hash == urlhash:
                return True
            else:
                return False
    modConfigPath = os.path.join(os.getcwd(), "game", "oscarAdditions", "modConfig.txt")

    def updateChecker():
        try:
            if not isUpToDate(modConfigPath, "https://raw.githubusercontent.com/KiloOscarSix/Leap-of-Faith-Mod/main/game/oscarAdditions/modConfig.txt"):
                return True
            else:
                return False
        except:
            return False

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

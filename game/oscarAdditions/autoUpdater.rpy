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
    return

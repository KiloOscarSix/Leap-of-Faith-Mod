init python:
    galleryCharacter = "Kira"
    galleryPageNumber = 1

    def galleryDecreasePageNumber():
        global galleryPageNumber
        galleryPageNumber -= 1
        return

    def galleryIncreasePageNumber():
        global galleryPageNumber
        galleryPageNumber += 1
        return

    sceneGalleryMenuDict = {
    "galleryMenu": [
    ["Kira", "/images/ep1/bowling/ep1_bowling_down_blink_a.jpg"],
    ["Stephanie", "/images/ep1/home/ep1_steph_blink_a.jpg"],
    ["Robin", "/images/ep1/bowling/ep1_bowling_robin1.jpg"],
    ["Linda", "/images/ep2/bar/ep2_bar13.jpg"],
    ["Lexi", "/images/ep3/airplaneinside/ep3_airplane96.jpg"],
    ["Cece", "/images/ep2/endbench/ep2_endbench08.jpg"],
    ],
    "Kira": {
    1: [
    ["e01s01", {}, "/images/ep1/special/ep1s01_kiraphoto1.jpg"],
    ["galleryScene2", {"Impact_KiraRobin":True}, "/images/ep3/cafe/ep3_cafe21.jpg"],
    ["galleryScene3", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True}, "/images/ep3/airplaneinside/ep3_airplane71.jpg"],
    ["ep3KiraLewd", {"contact_text_me":"", "contact_text_kira":"", "todayIs":5, "XPkira":99, "meRomantic":99, "meFlirty":99, "meSporty":99, "ep2RejectedRobin":True, "stephRejected":True}, "/images/ep3/kiras/ep3_kiramain78.jpg"],
    ],
    },
    "Stephanie": {
    1: [
    ["StephSlider4", {"todayIs":3}, "/images/ep1/steph/ep1_steph_leg1.jpg"],
    ],
    },
    "Robin": {
    1: [
    ["ep2RobinVideogamesTheory", {"todayIs":4, "XProbin":99, "meSporty":99, "meRomantic":99,}, "/images/ep2/robin/ep2_robin_intimate11.jpg"],
    ["e02s01", {}, "/images/ep2/special/ep2_bonusrobin16.jpg"],
    ["galleryScene2", {"Impact_KiraRobin":True}, "/images/ep3/cafe/ep3_cafe21.jpg"],
    ["galleryScene3", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True}, "/images/ep3/airplaneinside/ep3_airplane71.jpg"],
    ],
    },
    "Linda": {
    1: [
    ["lindaScene1", {}, "/images/ep2/shopping/ep2_shopping47.jpg"],
    ],
    },
    "Lexi": {
    1: [
    ["galleryScene4", {"XPlexi":99, "phone_task_list":[], "ep3CeceDrinkMojito":True}, "/images/ep3/airplaneinside/ep3_airplane98.jpg"],
    ["e03s01", {}, "/images/ep3/special/ep3_special17.jpg"],
    ],
    },
    "Cece": {
    1: [
    ["ep3CeceHome", {"contact_text_me":"", "contact_text_kira":"", "todayIs":5}, "/images/ep3/cecehome/ep3_cecehome14.jpg"],
    ],
    },
    }

label galleryNameChange:
    scene bg empty
    default persistent.name = ""
    if persistent.name == "":
        $ persistent.name = renpy.input("What is your name?", default="James")
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "Oscar's Scene Gallery":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                idle "/oscarAdditions/images/button.png"
                hover Transform(im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2)))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        imagebutton:
            action OpenURL("https://www.patreon.com/oscarsix/overview")
            idle Transform("/oscarAdditions/images/become_a_patron_button.png", zoom=0.7465437788)
            hover Transform(im.MatrixColor("/oscarAdditions/images/become_a_patron_button.png", im.matrix.brightness(0.2)), zoom=0.7465437788)
            xanchor 1.0

    vpgrid:
        cols 4
        xspacing 50
        yspacing 37
        pos (117, 360)

        for i in sceneGalleryMenuDict["galleryMenu"]:
            vbox:
                imagebutton:
                    action ShowMenu("sceneCharacterMenu"), Hide("sceneGalleryMenu"), SetVariable("galleryCharacter", i[0])
                    idle Transform(i[1], zoom=0.2)
                    hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                text i[0]:
                    style "galleryBody"
                    xcenter 0.5

screen sceneGalleryMenu():
    tag menu
    modal True
    add "#23272a"

    text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
        style "galleryHeader"
        xcenter 0.5
        ycenter 165

    vbox:
        spacing 20
        pos (1868, 50)

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            imagebutton:
                if galleryPageNumber == 1:
                    action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
                else:
                    action Function(galleryDecreasePageNumber)
                idle "/oscarAdditions/images/button.png"
                hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
            text "Back":
                style "galleryBody"
                xcenter 0.5
                ycenter 0.5

        fixed:
            xmaximum 186
            ymaximum 76
            xanchor 1.0

            if galleryPageNumber != len(sceneGalleryMenuDict[galleryCharacter]):
                imagebutton:
                    action Function(galleryIncreasePageNumber)
                    idle "/oscarAdditions/images/button.png"
                    hover im.MatrixColor("/oscarAdditions/images/button.png", im.matrix.brightness(0.2))
                text "Next":
                    style "galleryBody"
                    xcenter 0.5
                    ycenter 0.5

    vpgrid:
        cols 4
        xspacing 50
        yspacing 100
        pos (117, 360)

        for i in sceneGalleryMenuDict[galleryCharacter][galleryPageNumber]:
            $ scopeDict = {"name":persistent.name}
            $ scopeDict.update(i[1])
            imagebutton:
                action Replay(i[0], scope=scopeDict, locked=False)
                idle Transform(i[2], zoom=0.2)
                hover Transform(im.MatrixColor(i[2], im.matrix.brightness(0.2)), zoom=0.2)

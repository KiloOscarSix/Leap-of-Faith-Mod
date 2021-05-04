init python:
    import math
    galleryItems = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = math.floor(len(filter(lambda s: s.char == char, galleryItems))/8) + 1
            self.label = label

            if scope is None: self.scope = {}
            else: self.scope = scope

            self.thumbnail = os.path.join("/images/", thumbnail)
            galleryItems.append(self)

    def updateScope(newScope):
        rv = scopeDict.copy()
        rv.update(newScope)
        return rv

    ## GALLERY ITEMS HERE
define Kira1 = GalleryItem("Kira", "e01s01", "ep1/special/ep1s01_kiraphoto1.jpg")
define Kira2 = GalleryItem("Kira", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
define KiraRobin1 = GalleryItem("Kira", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
define KiraRobin2 = GalleryItem("Kira", "galleryScene3", "ep3/airplaneinside/ep3_airplane71.jpg", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True})
define KiraRobin3 = GalleryItem("Kira", "galleryScene9", "ep4/krromance/ep4p2_krdate03.jpg")
define KiraRobin4 = GalleryItem("Kira", "galleryScene10", "ep4/krromance/ep4p2_krthree01.jpg", {"todayIs":99})
define KiraRobin5 = GalleryItem("Kira", "ep5WakeKiraRobin", "ep5/intro/ep5_kirawake12.jpg", {"ep4NightChoose":5})

define Stephanie1 = GalleryItem("Stephanie", "StephSlider4", "ep1/steph/ep1_steph_leg1.jpg", {"todayIs":3})
define Stephanie2 = GalleryItem("Stephanie", "ep4StephRomance", "ep4/stephcouch/ep4_stephcouch80.jpg", {"todayIs":8, "meSporty":99})
define Stephanie3 = GalleryItem("Stephanie", "galleryScene13", "ep5/steph/ep5_stephshower26.jpg", {"stephRejected":False, "meSporty":99})
define Stephanie4 = GalleryItem("Stephanie", "galleryScene14", "ep5/steph/ep5_stephtub06.jpg")

define Robin1 = GalleryItem("Robin", "ep2RobinVideogamesTheory", "ep2/robin/ep2_robin_intimate11.jpg", {"todayIs":4, "XProbin":99, "meSporty":99, "meRomantic":99})
define Robin2 = GalleryItem("Robin", "e02s01", "ep2/special/ep2_bonusrobin16.jpg")
define KiraRobin1 = GalleryItem("Robin", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
define KiraRobin2 = GalleryItem("Robin", "galleryScene3", "ep3/airplaneinside/ep3_airplane71.jpg", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True})
define KiraRobin3 = GalleryItem("Robin", "galleryScene9", "ep4/krromance/ep4p2_krdate03.jpg")
define KiraRobin4 = GalleryItem("Robin", "galleryScene10", "ep4/krromance/ep4p2_krthree01.jpg", {"todayIs":99})
define KiraRobin5 = GalleryItem("Robin", "ep5WakeKiraRobin", "ep5/intro/ep5_kirawake12.jpg", {"ep4NightChoose":5})

define Linda1 = GalleryItem("Linda", "galleryScene1", "ep2/shopping/ep2_shopping47.jpg", {"meFlirty":99, "todayIs":4})
define Linda2 = GalleryItem("Linda", "galleryScene8", "ep4/firstsleep/ep4_firstsleep11.jpg", {"meFlirty":99, "todayIs":4})
define Linda3 = GalleryItem("Linda", "galleryScene11", "ep4/linda/ep4p2_lindaromance35.jpg", {"ep4NightChoose":6, "todayIs":99, "ep4SetupChrisWith":0})

define Lexi1 = GalleryItem("Lexi", "galleryScene4", "ep3/airplaneinside/ep3_airplane98.jpg", {"XPlexi":99, "phone_task_list":[], "ep3CeceDrinkMojito":True})
define Lexi2 = GalleryItem("Lexi", "e03s01", "ep3/special/ep3_special17.jpg")
define Lexi3 = GalleryItem("Lexi", "galleryScene5", "ep4/bunny/ep4p2_bunnydance51.jpg", {"Impact_Steph":True})
define Lexi4 = GalleryItem("Lexi", "galleryScene12", "ep4/lexi/ep4p2_lexiromance17.jpg")
define Lexi5 = GalleryItem("Lexi", "ep5WakeLexi", "ep5/intro/ep5_leximorning01.jpg")
define Lexi6 = GalleryItem("Lexi", "galleryScene15", "ep5/yacht/ep5_yacht125.jpg", {"todayIs":99, "ep5KissOK":3})

define Cece1 = GalleryItem("Cece", "ep3CeceHome", "ep3/cecehome/ep3_cecehome14.jpg", {"contact_text_me":"", "contact_text_kira":"", "todayIs":5})
define Cece2 = GalleryItem("Cece", "galleryScene6", "ep4/cece/ep4_ceceromance24.jpg")
define Cece3 = GalleryItem("Cece", "galleryScene7", "ep4/cece/ep4_ceceromance41.jpg")

define Holly1 = GalleryItem("Holly", "ep5HollyBend", "ep5/hollybalcony/ep5_holly02soloend.jpg", {"todayIs":99, "ep4NightChoose":2, "ep5ChrisHolly":False})

default galleryPageNumber = 1
default scopeDict = {}

define galleryMenu = [
    ["Kira", "/images/ep1/bowling/ep1_bowling_down_blink_a.jpg"],
    ["Stephanie", "/images/ep1/home/ep1_steph_blink_a.jpg"],
    ["Robin", "/images/ep1/bowling/ep1_bowling_robin1.jpg"],
    ["Linda", "/images/ep2/bar/ep2_bar13.jpg"],
    ["Lexi", "/images/ep3/airplaneinside/ep3_airplane96.jpg"],
    ["Cece", "/images/ep2/endbench/ep2_endbench08.jpg"],
    ["Holly", "/images/ep4/party/ep4p2_assgame07.jpg"]
]

label galleryNameChange:
    scene bg empty
    default persistent.name = ""
    if persistent.name == "":
        $ persistent.name = renpy.input("What is your name?", default="James")

    $ scopeDict = {"name":persistent.name}    
    return

screen sceneGalleryMenu():
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("sceneGalleryMenu"), ShowMenu("main_menu")
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for i in galleryMenu:
                vbox:
                    imagebutton:
                        action [Show("sceneCharacterMenu", galleryCharacter=i[0]), Hide("sceneGalleryMenu")]
                        idle Transform(i[1], zoom=0.2)
                        hover Transform(im.MatrixColor(i[1], im.matrix.brightness(0.2)), zoom=0.2)
                    text i[0]:
                        style "modTextBody"
                        xcenter 0.5

screen sceneCharacterMenu(galleryCharacter="None"):
    tag menu
    modal True
    add "/modAdditions/images/galleryBackground.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[galleryCharacter] Scenes - Page [galleryPageNumber]":
            style "modTextHeader"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if galleryPageNumber == 1:
                action Show("sceneGalleryMenu"), Hide("sceneCharacterMenu")
            else:
                action SetVariable(galleryPageNumber, galleryPageNumber - 1)
            idle "/modAdditions/images/backButton.png"
            hover Transform(im.MatrixColor("/modAdditions/images/backButton.png", im.matrix.brightness(0.2)))

        if galleryPageNumber != max([galleryItem.pageNum for galleryItem in galleryItems if galleryItem.char == galleryCharacter]):
            imagebutton:
                action SetVariable(galleryPageNumber, galleryPageNumber + 1)
                idle "/modAdditions/images/nextButton.png"
                hover im.MatrixColor("/modAdditions/images/nextButton.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for galleryItem in galleryItems:
                if galleryItem.char == galleryCharacter and galleryItem.pageNum == galleryPageNumber:
                    imagebutton:
                        action Replay(galleryItem.label, scope=updateScope(galleryItem.scope), locked=False)
                        idle Transform(galleryItem.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(galleryItem.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(galleryItem.thumbnail, 15), zoom=0.2)
init python:
    gallery_items = []

    class GalleryItem:
        def __init__(self, char, label, thumbnail, scope=None):
            self.char = char
            self.pageNum = (len(filter(lambda s: s.char == char, gallery_items)) // 8) + 1
            self.label = label

            if scope is None: self.scope = {}
            else: self.scope = scope

            self.thumbnail = os.path.join("images/", thumbnail)
            gallery_items.append(self)

    def update_scope(new_scope):
        rv = scope_dict.copy()
        rv.update(new_scope)
        return rv

    ## GALLERY ITEMS HERE
    kira = GalleryItem("Kira", "e01s01", "ep1/special/ep1s01_kiraphoto1.jpg")
    kira = GalleryItem("Kira", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
    kira_robin = GalleryItem("Kira", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
    kira_robin = GalleryItem("Kira", "galleryScene3", "ep3/airplaneinside/ep3_airplane71.jpg", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True})
    kira_robin = GalleryItem("Kira", "galleryScene9", "ep4/krromance/ep4p2_krdate03.jpg")
    kira_robin = GalleryItem("Kira", "galleryScene10", "ep4/krromance/ep4p2_krthree01.jpg", {"todayIs":99})
    kira_robin = GalleryItem("Kira", "ep5WakeKiraRobin", "ep5/intro/ep5_kirawake12.jpg", {"ep4NightChoose":5})
    kira = GalleryItem("Kira", "gallery_scene_19", "ep6/kirawork/ep6_kiraworking98.jpg", {"ep6DayOrder": 1, "todayIs":99})

    stephanie = GalleryItem("Stephanie", "StephSlider4", "ep1/steph/ep1_steph_leg1.jpg", {"todayIs":3})
    stephanie = GalleryItem("Stephanie", "ep4StephRomance", "ep4/stephcouch/ep4_stephcouch80.jpg", {"todayIs":8, "meSporty":99})
    stephanie = GalleryItem("Stephanie", "galleryScene13", "ep5/steph/ep5_stephshower26.jpg", {"stephRejected":False, "meSporty":99})
    stephanie = GalleryItem("Stephanie", "galleryScene14", "ep5/steph/ep5_stephtub06.jpg")

    robin = GalleryItem("Robin", "ep2RobinVideogamesTheory", "ep2/robin/ep2_robin_intimate11.jpg", {"todayIs":4, "XProbin":99, "meSporty":99, "meRomantic":99})
    robin = GalleryItem("Robin", "e02s01", "ep2/special/ep2_bonusrobin16.jpg")
    kira_robin = GalleryItem("Robin", "galleryScene2", "ep3/cafe/ep3_cafe21.jpg", {"Impact_KiraRobin":True})
    kira_robin = GalleryItem("Robin", "galleryScene3", "ep3/airplaneinside/ep3_airplane71.jpg", {"todayIs":5, "ep3TimePassed":0, "Impact_KiraRobin":True})
    kira_robin = GalleryItem("Robin", "galleryScene9", "ep4/krromance/ep4p2_krdate03.jpg")
    kira_robin = GalleryItem("Robin", "galleryScene10", "ep4/krromance/ep4p2_krthree01.jpg", {"todayIs":99})
    kira_robin = GalleryItem("Robin", "ep5WakeKiraRobin", "ep5/intro/ep5_kirawake12.jpg", {"ep4NightChoose":5})
    robin = GalleryItem("Robin", "gallery_scene_20", "ep6/robinwork/ep6_bowling88.jpg", {"ep4NightChoose": 4})

    linda = GalleryItem("Linda", "galleryScene1", "ep2/shopping/ep2_shopping47.jpg", {"meFlirty":99, "todayIs":4})
    linda = GalleryItem("Linda", "galleryScene8", "ep4/firstsleep/ep4_firstsleep11.jpg", {"meFlirty":99, "todayIs":4})
    linda = GalleryItem("Linda", "galleryScene11", "ep4/linda/ep4p2_lindaromance35.jpg", {"ep4NightChoose":6, "todayIs":99, "ep4SetupChrisWith":0})
    linda = GalleryItem("Linda", "gallery_scene_17", "ep6/adds/ep6_linda36.jpg")
    linda = GalleryItem("Linda", "gallery_scene_18", "ep6/hike/ep6_hike50.jpg")

    lexi = GalleryItem("Lexi", "galleryScene4", "ep3/airplaneinside/ep3_airplane98.jpg", {"XPlexi":99, "phone_task_list":[], "ep3CeceDrinkMojito":True})
    lexi = GalleryItem("Lexi", "e03s01", "ep3/special/ep3_special17.jpg")
    lexi = GalleryItem("Lexi", "galleryScene5", "ep4/bunny/ep4p2_bunnydance51.jpg", {"Impact_Steph":True})
    lexi = GalleryItem("Lexi", "galleryScene12", "ep4/lexi/ep4p2_lexiromance17.jpg")
    lexi = GalleryItem("Lexi", "ep5WakeLexi", "ep5/intro/ep5_leximorning01.jpg")
    lexi = GalleryItem("Lexi", "galleryScene15", "ep5/yacht/ep5_yacht125.jpg", {"todayIs":99, "ep5KissOK":3})

    cece = GalleryItem("Cece", "ep3CeceHome", "ep3/cecehome/ep3_cecehome14.jpg", {"contact_text_me":"", "contact_text_kira":"", "todayIs":5})
    cece = GalleryItem("Cece", "galleryScene6", "ep4/cece/ep4_ceceromance24.jpg")
    cece = GalleryItem("Cece", "galleryScene7", "ep4/cece/ep4_ceceromance41.jpg")
    cece = GalleryItem("Cece", "gallery_scene_16", "ep6/cece/ep6_cecel09.jpg", {"todayIs": 99, "ep4NightChoose": 1})

    holly = GalleryItem("Holly", "ep5HollyBend", "ep5/hollybalcony/ep5_holly02soloend.jpg", {"todayIs":99, "ep4NightChoose":2, "ep5ChrisHolly": False})

default gallery_page_number = 1
default scope_dict = {}

define gallery_menu = [
    ["Kira", "/images/ep1/bowling/ep1_bowling_down_blink_a.jpg"],
    ["Stephanie", "/images/ep1/home/ep1_steph_blink_a.jpg"],
    ["Robin", "/images/ep1/bowling/ep1_bowling_robin1.jpg"],
    ["Linda", "/images/ep2/bar/ep2_bar13.jpg"],
    ["Lexi", "/images/ep3/airplaneinside/ep3_airplane96.jpg"],
    ["Cece", "/images/ep2/endbench/ep2_endbench08.jpg"],
    ["Holly", "/images/ep4/party/ep4p2_assgame07.jpg"]
]

label gallery_name_set:
    default persistent.name = ""

    scene bg empty
    if persistent.name == "":
        $ persistent.name = renpy.input("What is your name?", default="James")

    $ scope_dict = {"name": persistent.name}    
    return

screen mod_scene_gallery_menu():
    tag mod_gallery
    modal True
    style_prefix "mod_gallery"

    add "mod_additions/images/gallery_background.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "Scene Gallery":
            style "mod_gallery_header"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            action Hide("mod_gallery"), ShowMenu("main_menu")
            idle "/mod_additions/images/back_button.png"
            hover Transform(im.MatrixColor("/mod_additions/images/back_button.png", im.matrix.brightness(0.2)))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for name, thumbnail in gallery_menu:
                vbox:
                    imagebutton:
                        action Show("mod_gallery_character_menu", character=name)
                        idle Transform(thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                    text name:
                        xcenter 0.5

screen mod_gallery_character_menu(character="All"):
    tag mod_gallery
    modal True
    style_prefix "mod_gallery"

    add "/mod_additions/images/gallery_background.png"

    fixed:
        xysize (1536, 98)
        pos (85, 14)

        text "[character] Scenes - Page [gallery_page_number]":
            style "mod_gallery_header"
            align (0.5, 0.5)

    vbox:
        spacing 20
        pos (1666, 39)

        imagebutton:
            if gallery_page_number == 1:
                action Show("mod_scene_gallery_menu")
            else:
                action SetVariable("gallery_page_number", gallery_page_number - 1)
            idle "/mod_additions/images/back_button.png"
            hover im.MatrixColor("/mod_additions/images/back_button.png", im.matrix.brightness(0.2))

        if gallery_page_number != max([item.pageNum for item in gallery_items if item.char == character]):
            imagebutton:
                action SetVariable("gallery_page_number", gallery_page_number + 1)
                idle "/mod_additions/images/next_button.png"
                hover im.MatrixColor("/mod_additions/images/next_button.png", im.matrix.brightness(0.2))

    fixed:
        xysize (1875, 789)
        pos(19, 115)

        vpgrid:
            cols 4
            spacing 50
            align (0.5, 0.5)

            for item in gallery_items:
                if item.char == character and item.pageNum == gallery_page_number:
                    imagebutton:
                        action Replay(item.label, scope=update_scope(item.scope), locked=False)
                        idle Transform(item.thumbnail, zoom=0.2)
                        hover Transform(im.MatrixColor(item.thumbnail, im.matrix.brightness(0.2)), zoom=0.2)
                        insensitive Transform(im.Blur(item.thumbnail, 15), zoom=0.2)
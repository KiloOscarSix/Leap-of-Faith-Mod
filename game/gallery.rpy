default persistent.galleryUnlocked = False

screen bonus_scenes:
    tag bonus_scenes
    modal True
    add "seethrough"

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_back")
        hover Transform("ph_ic_back_h")
        action Hide("bonus_scenes")
        xpos 300
        ypos 100

    fixed:
        pos(50, 250)

        if persistent.galleryUnlocked:
            textbutton "{size=50}Lock Scenes":
                action SetVariable("persistent.galleryUnlocked", False)
        else:
            textbutton "{size=50}Unlock Scenes":
                action SetVariable("persistent.galleryUnlocked", True)


    if persistent.scene01 or persistent.galleryUnlocked:
        imagebutton:
            focus_mask True
            idle Transform("e01s01_unlocked")
            hover Transform("e01s01_unlocked_h")
            action (Hide("main_menu"), Hide("bonus_scenes"), Start("e01s01"))
            xpos 500
            ypos 100
    else:
        imagebutton:
            focus_mask True
            idle Transform("e01s01_locked")
            hover Transform("e01s01_locked_h")
            action (NullAction())
            xpos 500
            ypos 100

    if persistent.scene02 or persistent.galleryUnlocked:
        imagebutton:
            focus_mask True
            idle Transform("e02s01_unlocked")
            hover Transform("e02s01_unlocked_h")
            action (Hide("main_menu"), Hide("bonus_scenes"), Start("e02s01"))
            xpos 1050
            ypos 100
    else:
        imagebutton:
            focus_mask True
            idle Transform("e02s01_locked")
            hover Transform("e02s01_locked_h")
            action (NullAction())
            xpos 1050
            ypos 100

    if persistent.scene03 or persistent.galleryUnlocked:
        imagebutton:
            focus_mask True
            idle Transform("e03s01_unlocked")
            hover Transform("e03s01_unlocked_h")
            action (Hide("main_menu"), Hide("bonus_scenes"), Start("e03s01"))
            xpos 500
            ypos 400
    else:
        imagebutton:
            focus_mask True
            idle Transform("e03s01_locked")
            hover Transform("e03s01_locked_h")
            action (NullAction())
            xpos 500
            ypos 400
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

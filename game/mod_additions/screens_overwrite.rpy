screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("Mod Options") action Show("mod_options")
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action Show("preferences")

        if main_menu:
            textbutton _("Scene Gallery") action (ui.callsinnewcontext("gallery_name_set"), Show("mod_scene_gallery_menu"))
            textbutton _("Bonus Scenes") action ShowMenu("bonus_scenes")
        textbutton _("Music") action Show("music_credits")
        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            textbutton _("Help") action Show("help")
        if renpy.variant("pc"):


            textbutton _("Quit") action Quit(confirm=not main_menu)


screen save():

    tag menu

    use file_slots(_("Save"))

    vbox:
        align(0.28, 0.185)
        text "{color=#fff}Save Name:{/color}"
        input:
            yalign 0.05
            value VariableInputValue("save_name")

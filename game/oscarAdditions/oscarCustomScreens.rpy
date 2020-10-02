screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")
        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action Show("preferences")

        if main_menu:
            textbutton _("Oscar's Gallery") action [ui.callsinnewcontext("galleryNameChange"), Show("sceneGalleryMenu")]
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

screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            order_reverse True

            if title == "Save":
                text "{color=#4ed6e7}Save Name:{/color}":
                    xalign 0
                    yalign -0.005
                input:
                    xalign 0
                    yalign 0.05
                    value VariableInputValue("save_name")

            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value


            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action If(renpy.get_screen("save"), true=Show("savegametag", accept=FileSave(slot)), false=FileLoad(slot))

                        vbox:

                            add FileScreenshot(slot) xalign 0.5

                            if FileSaveName(slot):
                                $ y = FileSaveName(slot).find("-")
                                if y >= -1:
                                    $ y = FileSaveName(slot).split("-")


                                    text FileSaveName(slot):
                                        style "slot_name_text"
                                else:

                                    text FileSaveName(slot):
                                        style "slot_name_text"
                            else:

                                text FileSaveName(slot):
                                    style "slot_name_text"

                            text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                style "slot_time_text"

                            key "save_delete" action FileDelete(slot)

                        if FileLoadable(slot):
                            imagebutton:
                                idle "images/common/del_icon.png"
                                hover "images/common/del_icon_h.png"
                                action FileDelete(slot)
                                xalign 1.02
                                yalign -0.02


            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")


                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

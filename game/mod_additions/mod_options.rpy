# Define commonly used hints or colours here
define gr = "{color=#0f0}"
define red = "{color=#f00}"
define blue = "{color=#00f}"

define mod = Character("The Warehouse", color="#0f0")

# Add any toggleable options here
screen mod_options():
    modal True
    style_prefix "mod_options"

    add "#23272a"

    vbox:
        xalign 0.5
        ypos 33
        spacing 33

        text "Mod Options"

        textbutton "Change In-Game Names" action ui.callsinnewcontext("mod_change_ingame_names")

        textbutton "Change Gallery Names" action ui.callsinnewcontext("mod_change_gallery_names")

    textbutton _("Return") action Hide("modOptions"):
        yanchor 1.0
        align (0.1, 0.9)


label mod_change_gallery_names:
    $ persistent.name = renpy.input("What is your name? (leave blank for James)").strip() or "James"
    return


label mod_change_ingame_names:
    $ name = renpy.input("What is your name? (leave blank for James)").strip() or "James"
    return

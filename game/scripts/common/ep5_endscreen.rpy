$ credits_show = True

screen ep5_endscreen:
    tag ep5_endscreen

    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep5_bonusscene = 0
    if persistent.scene01:
        $ ep5_bonusscene += 1
    if persistent.scene02:
        $ ep5_bonusscene += 1
    if persistent.scene03:
        $ ep5_bonusscene += 1
    if persistent.scene04:
        $ ep5_bonusscene += 1
    if persistent.scene05:
        $ ep5_bonusscene += 1
    else:
        if ep4Dawgs:
            $ persistent.scene05 = True
            $ ep5_bonusscene += 1

    $ ep5_opportunity = 0
    $ ep5_op_none = "."


    if not ep5HugSea:
        $ ep5_opportunity += 1


    $ meFlirtyName = "-"
    if meFlirty <= 1:
        $ meFlirtyName = "Low"
    elif meFlirty == 2:
        $ meFlirtyName = "Medium"
    elif meFlirty >= 3:
        $ meFlirtyName = "High"

    $ meRomanticName = "-"
    if meRomantic <= 1:
        $ meRomanticName = "Low"
    elif meRomantic == 2:
        $ meRomanticName = "Medium"
    elif meRomantic >= 3:
        $ meRomanticName = "High"

    $ meSportyName = "-"
    if meSporty <= 1:
        $ meSportyName = "Low"
    elif meSporty == 2:
        $ meSportyName = "Medium"
    elif meSporty >= 3:
        $ meSportyName = "High"

    imagebutton:
        focus_mask True
        idle Transform("endscreen_cece")
        hover Transform("endscreen_cece_on")
        action (ToggleScreen("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep5_endscreen_kira"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep5_endscreen_lexi"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep5_endscreen_robin"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    if Impact_Steph:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_stephanie")
            hover Transform("endscreen_stephanie_on")
            action (ToggleScreen("ep5_endscreen_stephanie"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_updateinfo"))
            xpos 1200
            ypos 350

        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"))
            xpos 1400
            ypos 350
    else:
        imagebutton:
            focus_mask True
            idle Transform("endscreen_linda")
            hover Transform("endscreen_linda_on")
            action (ToggleScreen("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"))
            xpos 1200
            ypos 350

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_ty")
        hover Transform("ph_ic_ty_h")


        action (Hide("ep5_endscreen_linda"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_updateinfo"), Jump("credits"))
        xpos 1560
        ypos 900

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_discord")
        hover Transform("ph_ic_discord_h")
        action OpenURL("https://discord.gg/2jqGPuD")
        xpos 1660
        ypos 780

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_patreon")
        hover Transform("ph_ic_patreon_h")
        action OpenURL("https://www.patreon.com/DriftyGames")
        xpos 1760
        ypos 780

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_youtube")
        hover Transform("ph_ic_youtube_h")
        action OpenURL("https://www.youtube.com/c/DriftyGames")
        xpos 1660
        ypos 900

    if renpy.loadable("script06.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep5_endscreen"), Hide("ep5_endscreen_updateinfo"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"), Jump("ch6Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep5_endscreen"), Hide("ep5_endscreen_updateinfo"), Hide("ep5_endscreen_cece"), Hide("ep5_endscreen_kira"), Hide("ep5_endscreen_lexi"), Hide("ep5_endscreen_robin"), Hide("ep5_endscreen_stephanie"), Hide("ep5_endscreen_linda"))
            xpos 1760
            ypos 900

    $ ep5_endmsg = "Thank you for playing Leap of Faith chapter 1-5. I hope you enjoyed it, and that you will come back for the continuation of the story. "
    $ ep5_endmsg += "\n\n{color=ffff77}Found a bug or need help?\nJoin my discord and check the channels #bug-reports or #lof-help-spoilers.{/color}"
    $ ep5_endmsg += "\n\nBest regards\n// Drifty"

    vpgrid:
        xalign 0.965
        ypos 0.092
        xmaximum 250
        xminimum 250
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 250
                        xminimum 250
                        textbutton "{size=18}{color=77ff77}[ep5_endmsg]{/color}{/size}" text_style "task_general_notify"

    vpgrid:
        xalign 0.758
        ypos 0.56
        xmaximum 600
        xminimum 600
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Bonus-Scenes unlocked: [ep5_bonusscene]/5" text_style "task_general_notify"





                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Non romancable options missed: [ep5_opportunity] (this playthrough)[ep5_op_none]" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Flirty level: [meFlirtyName]\nRomantic level: [meRomanticName]\nAthletic level: [meSportyName]" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "The game consists of [totalDia] screens. You have seen [seenDia] of them." text_style "task_general_notify"

screen ep5_endscreen_updateinfo:
    tag ep5_endscreen_updateinfo
    $ ep5_end_update = "If you've downloaded Chapter 6 as a patch, you can install it from here (incase the automatic update didn't go through). "
    $ ep5_end_update += "\n\nPatch file not found. "
    $ ep5_end_update += "\nIf you have already downloaded Chapter 6 as a patch, make sure you unzip the patch, and put it's contents in the game/ folder. "

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_update]" text_style "task_general_notify"

screen ep5_endscreen_cece:
    tag ep5_endscreen_cece
    add "emptyendscreen"
    if ep4NightChoose == 1:
        add "ep4_es_cece_happy"
    else:
        add "ep4_es_cece_smile"

    $ ep5_end_cece = "Cece went home with the others while you stayed behind in LA with Lexi and Holly. "
    if ep4NightChoose == 1:
        $ ep5_end_cece = "\n\nShe missed you. "
    $ ep5_end_cece += "\n\nYou just came home and rejoined her. She seemed very happy to see you."

    $ ep5_opportunity_ce = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_cece]\n\nCece options missed: [ep5_opportunity_ce]" text_style "task_general_notify"

screen ep5_endscreen_kira:
    tag ep5_endscreen_kira
    add "emptyendscreen"
    if ep4NightChoose == 3:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_kira_happy"
    elif ep4NightChoose == 4:
        add "ep4_es_kira_sad"
    else:
        add "ep4_es_kira_smile"

    $ ep5_end_kira = "Kira went home with the others. She told you she saw you as a good friend, and hoped you stopped by MaKenzie one day."
    if ep4NightChoose == 3:
        $ ep5_end_kira = "\n\nRobin has been avoiding you. Kira said she would talk to her. "
    elif ep4NightChoose == 4:
        $ ep5_end_kira = "\n\nRobin is acting weird. Probably because of the whole situation. But you should go talk to her about the radio silence. "
    elif ep4NightChoose == 5:
        $ ep5_end_kira = "\n\nRobin is acting weird. Maybe it's because of the whole situation. But you should probably go talk to her about the radio silence - or both. "

    $ ep5_opportunity_ki = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_kira]\n\nKira options missed: [ep5_opportunity_ki]" text_style "task_general_notify"

screen ep5_endscreen_lexi:
    tag ep5_endscreen_lexi
    add "emptyendscreen"
    if ep4NightChoose == 2:
        add "ep4_es_lexi_happy"
    else:
        add "ep4_es_lexi_smile"

    if Impact_Steph:
        $ ep5_end_lexi = "After getting the call from your dad, you stayed behind in LA with Lexi and Holly while Steph went to Holly's apartment. The others went home. "
    else:
        $ ep5_end_lexi = "After getting the call from your dad, you stayed behind in LA with Lexi and Holly. The others went home. "

    $ ep5_end_lexi += "\n\nThey accompanied you as you went to see your dad, but you met him alone. "
    $ ep5_end_lexi += "\n\nIn the evening you reunited at the docks, where you took a trip on Lexi's yacht. "

    if ep4NightChoose == 2:
        $ ep5_end_lexi += "\n\nYou caught Lexi and Holly kissing. Lexi apologized for doing so. "
        if ep5KissOK == 1:
            $ ep5_end_lexi += "You told her it was nothing to apologize for, being cute more than anything else. "
        elif ep5KissOK == 2:
            $ ep5_end_lexi += "You accepted the apology, but told her to stop doing so in the future. "
        elif ep5KissOK == 3:
            $ ep5_end_lexi += "You accepted the apology and confided in her that you wouldn't mind a threesome. "
        if ep5HollyComplete == 1:
            $ ep5_end_lexi += "\n\nLate at night while fucking Lexi, you included Holly and went full threesome. "
            $ ep5_end_lexi += "It ended with Holly cumming all over Lexi, and you all over Holly. Or was it in Holly? "
        elif ep5HollyComplete == 2:
            $ ep5_end_lexi += "\n\nLate at night while fucking Lexi, you included Holly and went full threesome. "
            $ ep5_end_lexi += "It ended with Holly cumming all over you, and you all over Lexi. Or was it in Lexi? "
        else:
            $ ep5_end_lexi += "\n\nLater that night you fucked Lexi. "
    if ep5BoughtCigarettes == 1:
        $ ep5_end_lexi += "\n\nYou bought cigarettes for Holly, but not the right brand. "
    elif ep5BoughtCigarettes == 2:
        $ ep5_end_lexi += "\n\nYou bought cigarettes for Holly. It was even the right brand. "
    else:
        $ ep5_end_lexi += "\n\nYou did not buy cigarettes for Holly."

    $ ep5_opportunity_le = 0

    if ep5KissOK == 3:
        $ ep5_opportunity_le += 1
    if ep5HollyComplete > 0:
        $ ep5_opportunity_le += 1
    if ep5BoughtCigarettes == 0:
        $ ep5_opportunity_le += 1


    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_lexi]\n\nLexi options missed: [ep5_opportunity_le]" text_style "task_general_notify"

screen ep5_endscreen_robin:
    tag ep5_endscreen_robin
    add "emptyendscreen"
    if ep4NightChoose == 4:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 5:
        add "ep4_es_robin_happy"
    elif ep4NightChoose == 3:
        add "ep4_es_robin_sad"
    else:
        add "ep4_es_robin_smile"

    $ ep5_end_robin = "Robin went home with the others. "
    if ep4NightChoose == 3:
        $ ep5_end_robin += "\n\nShe seemed to avoid you before going home. Kira said she would talk to her. "
    elif ep4NightChoose == 4:
        $ ep5_end_robin += "\n\nShe seemed to avoid you before going home. You might want to talk to her now that you're home. "
    elif ep4NightChoose == 5:
        $ ep5_end_robin += "\n\nShe is acting weird. Maybe it's because of the whole situation. "

    if ep4SetupChrisWith == 3:
        if ep4NightChoose == 3:
            $ ep5_end_robin += "\n\nShe seems to get along with Chris. "
        else:
            $ ep5_end_robin += "\n\nShe seems to get along with Chris. Unless it's purely friends with benefits. "

    $ ep5_opportunity_ro = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_robin]\n\nRobin options missed: [ep5_opportunity_ro]" text_style "task_general_notify"

screen ep5_endscreen_stephanie:
    tag ep5_endscreen_stephanie
    add "emptyendscreen"
    if Impact_Steph:
        if ep4NightChoose == 7:
            add "ep4_es_steph_happy"
        else:
            add "ep4_es_steph_smile"
    else:
        add "ep4_es_steph_sad"


    $ ep5_end_stephanie = "Steph went early to Holly's appartment, to prepare for a meeting with her old job and her dad. "

    if ep4NightChoose == 7:
        $ ep5_end_stephanie += "She did not know that you stayed behind in LA. "
        $ ep5_end_stephanie += "\n\nYou went to surprise her after seeing your dad. "
        if ep5StephGameTrait == 1 and not ep5NoTrait:
            $ ep5_end_stephanie += "\n\nWhile sneaking up on her, you activated your super secret flirty trait cheat. "
        elif ep5StephGameTrait == 2:
            $ ep5_end_stephanie += "\n\nWhile sneaking up on her, you activated your super secret athletic sporty trait cheat. "
        elif ep5StephGameTrait == 3:
            $ ep5_end_stephanie += "\n\nWhile sneaking up on her, you activated your super secret romantic trait cheat. "
        else:
            $ ep5_end_stephanie += "\n\nWhile sneaking up on her, you realized you'd been missing out on a lot of opportunities to give yourself traits, and could not activate any cheats. "
        if ep5PhoneMuted:
            $ ep5_end_stephanie += "\n\nDue to your efforts, traits and preparations you won the Steph Game - successfully sneaking up on her. "
            $ ep5_end_stephanie += "Afterwards you had a very good shower and bath. "
        else:
            if ep5StephGameHorny:
                $ ep5_end_stephanie += "\n\nYou decided to Sext her while sneaking to keep her occupied, but still could not avoid a game over. "
            else:
                $ ep5_end_stephanie += "\n\nYou decided to send her romantic messages while sneaking to keep her occupied, but still could not avoid a game over. "
            $ ep5_end_stephanie += "You were still rewarded with a good time afterwards. "
    else:
        $ ep5_end_stephanie += "She did not know that you stayed behind in LA, and you did not get to go see her. "

    if ep5StephForgive:
        $ ep5_end_stephanie += "\n\nLater in the day Steph dropped you off at the docks and went to see her dad. You can't help but wonder how that went. "
        $ ep5_end_stephanie += "\n\nYou told her you'd forgiven her about the past and her leaving. She is going to live in LA though, while you go back home. "
    else:
        $ ep5_end_stephanie += "\n\nLater in the day Steph dropped you off at the docks and went to see her dad. "
        $ ep5_end_stephanie += "\n\nIn the end you told her you couldn't forgive her for your past and her leaving. She is set to live in LA, while you go back home. "

    $ ep5_opportunity_st = 0

    if ep5NoTrait:
        $ ep5_opportunity_st += 1
    if ep5PhoneMuted:
        $ ep5_opportunity_st += 1

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_stephanie]\n\nStephanie options missed: [ep5_opportunity_st]" text_style "task_general_notify"

screen ep5_endscreen_linda:
    tag ep5_endscreen_linda
    add "emptyendscreen"
    if ep4NightChoose == 6:
        add "ep4_es_linda_happy"
    else:
        add "ep4_es_linda_smile"

    $ ep5_end_linda = "Linda went home with the others. "

    $ ep5_end_linda += "\n\nShe promised not to see Matt before you returned home, but was not at home when you arrived. "

    if ep4NightChoose == 6:
        $ ep5_end_linda += "\n\nThat ring seems important to her. You have to help get it back somehow. "
    else:
        $ ep5_end_linda += "\n\nThat ring seems important to her. You should help get it back somehow. "

    $ ep5_opportunity_li = 0

    vpgrid:
        xalign 0.1
        ypos 0.092
        xmaximum 800
        xminimum 800
        spacing 4
        cols 1
        xfill True
        yfill True
        vbox spacing 8:
            hbox spacing 20:
                vbox spacing 8:
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 800
                        xminimum 800
                        textbutton "[ep5_end_linda]\n\nLinda options missed: [ep5_opportunity_li]" text_style "task_general_notify"

if credit_show:
    $ credits_show = False
    jump credits

screen endscreen_credits:
    tag endscreen_credits
    modal True
    imagebutton:
        focus_mask True
        idle Transform("credits")
        hover Transform("credits")
        action Hide("endscreen_credits")
        xpos 0
        ypos 0

init:
    transform credits_scroll:
        subpixel True align (0.15,-1.10)
        linear 70.0 align (0.15,5.0)
        Null()

label credits:
    show text [
"{size=40}{color=#4ec4d9}Leap of Faith is written,\nrendered, animated and scripted by{/color}{/size}",
"{size=30}\n\n",
"{color=#ffb0d0}Drifty{/color}",
"\n\n\n{/size}",
"{size=40}{color=#4ec4d9}Discord Team and Beta Testers{/color}{/size}",
"{size=30}\n\n",
"Rob 'The Panty Sniffer' Johnson\n",
"Pial\n",
"Cursen\n",
"Eerie Entity\n",
"Steele\n",
"Dawe\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Guest appearances{/size}",
"{size=30}\n\n",
"Jaye Campbell appears courtesy of\nStone Fox Studios\n\n",
"The 'Last Call' logo is a trademark of\nThunderline Studios\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Top Tier Patreon Supporters{/color}{/size}",
"{size=30}\n\n",
"The-Exotic-Titan\n",
"Smolpenus\n",
"Kytronix\n",
"Xor\n",
"Wolvy\n",
"Touhara\n",
"\n",
"Andrew Rider\n",
"aob86\n",
"Balvenie41\n",
"Darkness65\n",
"Derrek\n",
"Dudemandavid23\n",
"Lee Sullivan\n",
"MasterSav\n",
"ODX\n",
"RødTop\n",
"scalvi\n",
"TsunamiKata\n",
"Yukinohki\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}Thank you to{/color}{/size}",
"{size=30}\n\n",
"Wibble\n",
"for the 3d conversion of the Drifty logo\n\n",
"All my patreon supporters,\n",
"for helping me realize this project.\n",
"You help me create a better game,\n",
"and it wouldn't be possible without you.\n",
"\n\n{/size}",
"{size=40}{color=#4ec4d9}A special thank you to{/color}{/size}",
"{size=30}\n\n",
"{color=#9f91f9}C.{/color}\n",
"for inspiring me to make this.\n\n\n",
"'{i}To be continued...{/i}'{/size}"
] at credits_scroll
    $ renpy.pause(1, hard=True)
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

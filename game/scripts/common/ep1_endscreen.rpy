image endscreen_cece_on = Movie(channel="main", play="images/common/es_cece.webm")
image endscreen_kira_on = Movie(channel="main", play="images/common/es_kira.webm")
image endscreen_lexi_on = Movie(channel="main", play="images/common/es_lexi.webm")
image endscreen_robin_on = Movie(channel="main", play="images/common/es_robin.webm")
image endscreen_stephanie_on = Movie(channel="main", play="images/common/es_steph.webm")

default ep1_bonusscene_total = 3
default ep1_opportunity = 0
default ep1_opportunity_ce = 0
default ep1_opportunity_ki = 0
default ep1_opportunity_le = 0
default ep1_opportunity_li = 0
default ep1_opportunity_ro = 0
default ep1_opportunity_st = 0

screen ep1_endscreen:
    tag ep1_endscreen
    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep1_bonusscene = 0
    if persistent.scene01:
        $ ep1_bonusscene += 1
    else:
        if d1_responded_kira_thinkingof == 1:
            $ persistent.scene01 = True
            $ ep1_bonusscene += 1






    $ ep1_opportunity = 0
    if d1_responded_chris == 0:
        $ ep1_opportunity += 1

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
        action (ToggleScreen("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep1_endscreen_kira"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep1_endscreen_lexi"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep1_endscreen_robin"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep1_endscreen_stephanie"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_uk"), Hide("ep1_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_uk")
        hover Transform("endscreen_uk_on")
        action (ToggleScreen("ep1_endscreen_uk"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_updateinfo"))
        xpos 1400
        ypos 350

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

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_continue")
        hover Transform("ph_ic_continue_h")
        action (Hide("ep1_endscreen"), Hide("ep1_endscreen_updateinfo"), Hide("ep1_endscreen_cece"), Hide("ep1_endscreen_kira"), Hide("ep1_endscreen_lexi"), Hide("ep1_endscreen_robin"), Hide("ep1_endscreen_stephanie"), Hide("ep1_endscreen_uk"), Jump("ch2Update"))
        xpos 1760
        ypos 900























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
                        textbutton "Bonus-Scenes unlocked: [ep1_bonusscene]/[ep1_bonusscene_total]" text_style "task_general_notify"





                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Non romancable options missed: [ep1_opportunity] (this playthrough)\n{size=18}{color=ffff00}(Options are choices that in some way will impact future chapters. See individual characters for more.){/color}{/size}" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Flirty level: [meFlirty]-[meFlirtyName]\nRomantic level: [meRomantic]-[meRomanticName]\nAthletic level: [meSporty]-[meSportyName]" text_style "task_general_notify"
                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "The game consists of [totalDia] screens. You have seen [seenDia] of them." text_style "task_general_notify"

screen ep1_endscreen_updateinfo:
    tag ep1_endscreen_updateinfo
    $ ep1_end_update = "If you've downloaded Chapter 2 as a patch, you can install it from here (incase the automatic update didn't go through). "
    $ ep1_end_update += "\n\nPatch file not found. "
    $ ep1_end_update += "\nIf you have already downloaded Chapter 2 as a patch, make sure you unzip the patch, and put it's contents in the game/ folder. "

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
                        textbutton "[ep1_end_update]" text_style "task_general_notify"

screen ep1_endscreen_cece:
    tag ep1_endscreen_cece
    $ ep1_end_cece = "You saved Cece's life. For her, you are a second chance at life. "
    $ ep1_end_cece += "\n\nShe is currently hospitalized. You are there with her. "

    $ ep1_opportunity_ce = 0
    if not ep1OfferedCeceStay:
        $ ep1_opportunity_ce += 1

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
                        textbutton "[ep1_end_cece]\n\nCece options missed: [ep1_opportunity_ce]\nCece points: [XPcece]" text_style "task_general_notify"

screen ep1_endscreen_kira:
    tag ep1_endscreen_kira
    $ ep1_end_kira = "You met Kira at MaKenzie having lunch. "
    if d1_responded_kira != 0:
        $ ep1_end_kira += "\n\nYou got her telephone number and messaged her back. "
        if wentBowlingKira:
            if ep1KiraWalkHome:
                $ ep1_end_kira += "\n\nThe two of you went bowling, and after walking her home she invited you in. "
                if ep1RejectedKira:
                    $ ep1_end_kira += "You declined her advances. "
                else:
                    $ ep1_end_kira += "You accepted, but she reconcidered. "
            else:
                $ ep1_end_kira += "\n\nThe two of you went bowling, but you didn't walk her home. "
            if d1_responded_kira_thinkingof == 1:
                $ ep1_end_kira += "\n\nYou told her in a message that you would be thinking about her while at the metro. "
        else:
            $ ep1_end_kira += "\n\nYou declined going bowling with her. "
    else:
        $ ep1_end_kira += "\n\nYou got her telephone number, but did not message her back. "

    $ ep1_opportunity_ki = 0
    if not wentBowlingKira:
        $ ep1_opportunity_ki += 2

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
                        textbutton "[ep1_end_kira]\n\nKira options missed: [ep1_opportunity_ki]\nKira points: [XPkira]" text_style "task_general_notify"

screen ep1_endscreen_lexi:
    tag ep1_endscreen_lexi
    $ ep1_end_lexi = "You met Lexi at the Metronome inbetween her performances, where she had a few glasses of wine with you. "
    if saidLexiWasBeautiful:
        $ ep1_end_lexi += "\n\nShe thought about you later that night. "
    else:
        $ ep1_end_lexi += "\n\nShe thought you were cute. "

    $ ep1_opportunity_le = 0
    if not saidLexiWasBeautiful:
        $ ep1_opportunity_le += 1

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
                        textbutton "[ep1_end_lexi]\n\nLexi options missed: [ep1_opportunity_le]\nLexi points: [XPlexi]" text_style "task_general_notify"

screen ep1_endscreen_robin:
    tag ep1_endscreen_robin
    if wentBowlingKira:
        $ ep1_end_robin = "You met Robin going bowling with Kira. She owns the bowling alley. "
        $ ep1_end_robin += "She told you to decline Kira if she offered herself to you during the evening. "
        if ep1SaidLikedRobin:
            $ ep1_end_robin += "\n\nYou told her you liked her. "
    else:
        $ ep1_end_robin = "You haven't met Robin yet. "

    $ ep1_opportunity_ro = 0
    if not ep1SaidLikedRobin:
        $ ep1_opportunity_ro += 1

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
                        textbutton "[ep1_end_robin]\n\nRobin options missed: [ep1_opportunity_ro]\nRobin points: [XProbin]" text_style "task_general_notify"

screen ep1_endscreen_stephanie:
    tag ep1_endscreen_stephanie
    $ ep1_end_stephanie = "You dreamt about Stephanie, which made you think about her again. "
    $ ep1_end_stephanie += "\n\nThe two of you ran into eachother late at night at the Metronome, where she commanded you home to her place."
    if stephRejected:
        $ ep1_end_stephanie += "\n\nYou rejected her advances and demanded answers. She had none."
    else:
        $ ep1_end_stephanie += "\n\nYou fucked her silly. Then her husband came home, and you had to abandon ship."
        if ep1StephOrg:
            $ ep1_end_stephanie += "\n\nShe orgasmed - you did not."

    $ ep1_opportunity_st = 0
    if not ep1StephOrg:
        $ ep1_opportunity_st += 1
    if d1_responded_stephanie == 0:
        $ ep1_opportunity_st += 1

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
                        textbutton "[ep1_end_stephanie]\n\nStephanie options missed: [ep1_opportunity_st]\nStephanie points: [XPstephanie]" text_style "task_general_notify"

screen ep1_endscreen_uk:
    tag ep1_endscreen_uk
    $ ep1_end_uk = "The last of the romancable characters. You will meet her in Chapter 2. "

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
                        textbutton "[ep1_end_uk]" text_style "task_general_notify"
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

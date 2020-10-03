image endscreen_linda_on = Movie(channel="main", play="images/common/es_linda.webm")

default ep2_bonusscene_total = 1
default ep2_opportunity = 0
default ep2_opportunity_ce = 0
default ep2_opportunity_ki = 0
default ep2_opportunity_le = 0
default ep2_opportunity_li = 0
default ep2_opportunity_ro = 0
default ep2_opportunity_st = 0

screen ep2_endscreen:
    tag ep2_endscreen

    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep2_bonusscene = 0
    if persistent.scene02:
        $ ep2_bonusscene += 1
    else:
        if ep2RespondedRobin == 2:
            $ persistent.scene02 = True
            $ ep2_bonusscene += 1
    $ ep2_bonusscene += 1

    $ ep2_opportunity_sum = ep1_opportunity
    $ ep2_opportunity = 0
    if ep2ChrisShopConv == 4:
        $ ep2_opportunity += 1
        $ ep2_opportunity_sum += 1
    if not ep2BunnyPicFlex:
        $ ep2_opportunity += 1
        $ ep2_opportunity_sum += 1

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
        action (ToggleScreen("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep2_endscreen_kira"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep2_endscreen_lexi"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep2_endscreen_robin"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep2_endscreen_stephanie"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_linda"), Hide("ep2_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep2_endscreen_linda"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_updateinfo"))
        xpos 1400
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_ty")
        hover Transform("ph_ic_ty_h")
        action Show("endscreen_credits")
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

    if renpy.loadable("script03.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep2_endscreen"), Hide("ep2_endscreen_updateinfo"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"), Jump("ch3Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep2_endscreen"), Hide("ep2_endscreen_updateinfo"), Hide("ep2_endscreen_cece"), Hide("ep2_endscreen_kira"), Hide("ep2_endscreen_lexi"), Hide("ep2_endscreen_robin"), Hide("ep2_endscreen_stephanie"), Hide("ep2_endscreen_linda"))
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
                        textbutton "Bonus-Scenes unlocked: [ep2_bonusscene]/3" text_style "task_general_notify"





                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Non romancable options missed: [ep2_opportunity] (this playthrough)\n{size=18}{color=ffff00}(Options are choices that in some way will impact future chapters. See individual characters for more.){/color}{/size}" text_style "task_general_notify"
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

screen ep2_endscreen_updateinfo:
    tag ep2_endscreen_updateinfo
    $ ep2_end_update = "If you've downloaded Chapter 3 as a patch, you can install it from here (incase the automatic update didn't go through). "
    $ ep2_end_update += "\n\nPatch file not found. "
    $ ep2_end_update += "\nIf you have already downloaded Chapter 3 as a patch, make sure you unzip the patch, and put it's contents in the game/ folder. "

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
                        textbutton "[ep2_end_update]" text_style "task_general_notify"

screen ep2_endscreen_cece:
    tag ep2_endscreen_cece
    $ ep2_end_cece = "She is currently living in your apartment. There is something about her. "
    $ ep2_end_cece += "\n\nYou didn't get to address her problems, or spend a lot of time under four eyes. But she seemed to open up a bit in the end. "

    $ ep2_opportunity_ce_total = ep1_opportunity_ce
    $ ep2_opportunity_ce = 0
    if ep2Eyecontact <> 1:
        $ ep2_opportunity_ce += 1
        $ ep2_opportunity_ce_total += 1
    if ep2ToldChrisAboutCece:
        $ ep2_opportunity_ce += 1
        $ ep2_opportunity_ce_total += 1

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
                        textbutton "[ep2_end_cece]\n\nCece options missed: [ep2_opportunity_ce]\nCece points: [XPcece]" text_style "task_general_notify"

screen ep2_endscreen_kira:
    tag ep2_endscreen_kira
    $ ep2_end_kira = "You didn't get to spend any time with Kira this chapter. "
    if ep2KiraReply:
        $ ep2_end_kira += "\n\nShe sent you a text message, and you replied. "
        if ep2KiraReplyTwo:
            $ ep2_end_kira += "\n\nThe next day she sent you a new message, where she acted kinda strange. "
        else:
            $ ep2_end_kira += "\n\nThe next day she sent you a new message, to which you didn't reply. "
    else:
        $ ep2_end_kira += "\n\nShe sent you a text message. You didn't reply. "
    if not ep2RobinCrosseyed:
        $ ep2_end_kira += "\n\nOh, and it seems you share a little secret with Kira about Robin when she's drunk. "

    $ ep2_opportunity_ki_total = ep1_opportunity_ki
    $ ep2_opportunity_ki = 0
    if not ep2KiraReply:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1
    if not ep2KiraReplyTwo:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1
    if ep2RobinCrosseyed:
        $ ep2_opportunity_ki += 1
        $ ep2_opportunity_ki_total += 1

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
                        textbutton "[ep2_end_kira]\n\nKira options missed: [ep2_opportunity_ki]\nKira points: [XPkira]" text_style "task_general_notify"

screen ep2_endscreen_lexi:
    tag ep2_endscreen_lexi
    $ ep2_end_lexi = "Chris told you he talked to Lexi after you left Metro; where she'd been asking for you. Though, he forgot to give her your phone number. "
    if ep2LexiReply:
        $ ep2_end_lexi += "\n\nYou did however manage to find a way to give her your phone number. "
    else:
        $ ep2_end_lexi += "\n\nYou did not manage to find a way to give her your phone number. "

    $ ep2_opportunity_le_total = ep1_opportunity_le
    $ ep2_opportunity_le = 0
    if not ep2LexiReply:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1
    if not ep2LexiSlippers:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1
    if not ep2NukeDance:
        $ ep2_opportunity_le += 1
        $ ep2_opportunity_le_total += 1

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
                        textbutton "[ep2_end_lexi]\n\nLexi options missed: [ep2_opportunity_le]\nLexi points: [XPlexi]" text_style "task_general_notify"

screen ep2_endscreen_robin:
    tag ep2_endscreen_robin
    if ep2WentToRobin:
        $ ep2_end_robin = "You went to Plaza Bowling to help Robin out on her opening night. "
        $ ep2_end_robin += "Unfortunately, she'd had a run of bad luck, and decided to close up early and go home. You joined her. "
        if ep2SaidLikedRobin:
            $ ep2_end_robin += "\n\nYou told her you liked her. "
    else:
        $ ep2_end_robin = "You did not go to Plaza Bowling to help Robin out on her opening night. "
    if ep2RejectedRobin:
        $ ep2_end_robin += "\n\nShe tried hooking up with you for the night, but you declined. "
    else:
        $ ep2_end_robin += "\n\nYou had sex with her. She hinted towards a friends with benefits relationship, but who knows. Maybe it was the alcohol talking. "

    $ ep2_opportunity_ro_total = ep1_opportunity_ro
    $ ep2_opportunity_ro = 0
    if not ep2WentToRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2SaidLikedRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if ep2RejectedRobin:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2RobinCrosseyed:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if not ep2RobinCommandoAbuse:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1
    if ep2RespondedRobin == 0:
        $ ep2_opportunity_ro += 1
        $ ep2_opportunity_ro_total += 1

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
                        textbutton "[ep2_end_robin]\n\nRobin options missed: [ep2_opportunity_ro]\nRobin points: [XProbin]" text_style "task_general_notify"

screen ep2_endscreen_stephanie:
    tag ep2_endscreen_stephanie
    $ ep2_end_stephanie = "You have not seen Stephanie since that night after Metro. "
    $ ep2_end_stephanie += "\n\nAfter adding Nüke to your phone, you saw she's there as well."

    $ ep2_opportunity_st_total = ep1_opportunity_st
    $ ep2_opportunity_st = 0
    if ep2ChrisConvOverSteph == 1:
        $ ep2_opportunity_st += 1
        $ ep2_opportunity_st_total += 1

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
                        textbutton "[ep2_end_stephanie]\n\nStephanie options missed: [ep2_opportunity_st]\nStephanie points: [XPstephanie]" text_style "task_general_notify"

screen ep2_endscreen_linda:
    tag ep2_endscreen_linda
    $ ep2_end_linda = "Seems it's a small world. Cece's best friend is no one else than your childhood friend, Linda. "
    $ ep2_end_linda += "\n\nYou haven't had a chance to sit down and talk to her properly, yet."
    if ep2LindaDressingFlirt:
        $ ep2_end_linda += "\n\nThings got kinda steamy in the dressing room at Ashley's."

    $ ep2_opportunity_li_total = ep1_opportunity_li
    $ ep2_opportunity_li = 0
    if ep2Eyecontact <> 2:
        $ ep2_opportunity_li += 1
        $ ep2_opportunity_li_total += 1
    if not ep2LindaDressingFlirt:
        $ ep2_opportunity_li += 1
        $ ep2_opportunity_li_total += 1

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
                        textbutton "[ep2_end_linda]\n\nLinda options missed: [ep2_opportunity_li]\nLinda points: [XPlinda]" text_style "task_general_notify"

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
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

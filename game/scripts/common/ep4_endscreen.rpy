screen ep4_endscreen:
    tag ep4_endscreen

    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep4_bonusscene = 0
    if persistent.scene01:
        $ ep4_bonusscene += 1
    if persistent.scene02:
        $ ep4_bonusscene += 1
    if persistent.scene03:
        $ ep4_bonusscene += 1
    if persistent.scene04:
        $ ep4_bonusscene += 1





    $ ep4_opportunity = 0
    $ ep4_op_none = "."




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
        action (ToggleScreen("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep4_endscreen_kira"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep4_endscreen_lexi"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep4_endscreen_robin"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep4_endscreen_stephanie"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_linda"), Hide("ep4_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep4_endscreen_linda"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_updateinfo"))
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

    if renpy.loadable("script05.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep4_endscreen"), Hide("ep4_endscreen_updateinfo"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"), Jump("ch5Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep4_endscreen"), Hide("ep4_endscreen_updateinfo"), Hide("ep4_endscreen_cece"), Hide("ep4_endscreen_kira"), Hide("ep4_endscreen_lexi"), Hide("ep4_endscreen_robin"), Hide("ep4_endscreen_stephanie"), Hide("ep4_endscreen_linda"))
            xpos 1760
            ypos 900

    $ ep4_endmsg = "Thank you for playing Leap of Faith. I hope you enjoyed it, and that you will come back for the continuation of the story. "
    $ ep4_endmsg += "\n\nRemember that saves made after the Chapter 3 endscreen (not this endscreen) will not be usable when the second part of this chapter is released."
    $ ep4_endmsg += "\n\n{color=ffff77}Found a bug?\nJoin the discord and post it in the #bug-reports channel please (link below).{/color}"
    $ ep4_endmsg += "\n\nBest regards\n// Drifty"

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
                        textbutton "{size=18}{color=77ff77}[ep4_endmsg]{/color}{/size}" text_style "task_general_notify"

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
                        textbutton "Bonus-Scenes unlocked: [ep4_bonusscene]/3" text_style "task_general_notify"





                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Non romancable options missed: [ep4_opportunity] (this playthrough)[ep4_op_none]" text_style "task_general_notify"
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

screen ep4_endscreen_updateinfo:
    tag ep4_endscreen_updateinfo
    $ ep4_end_update = "If you've downloaded Chapter 5 as a patch, you can install it from here (incase the automatic update didn't go through). "
    $ ep4_end_update += "\n\nPatch file not found. "
    $ ep4_end_update += "\nIf you have already downloaded Chapter 4 as a patch, make sure you unzip the patch, and put it's contents in the game/ folder. "

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
                        textbutton "[ep4_end_update]" text_style "task_general_notify"

screen ep4_endscreen_cece:
    tag ep4_endscreen_cece
    if ep4NightChoose == 1:
        add "ep4_es_cece_happy"
    else:
        add "ep4_es_cece_smile"

    if ep4NightChoose == 1:
        $ ep4_end_cece = "You went for a night walk by the downstairs pool with Cece. "
        $ ep4_end_cece += "It became rather interesting. "
        if ep4CeceSexTalk == 0:
            $ ep4_end_cece += "\n\nWhen she asked you if you'd been with a lot of women, you truthfully said that you hadn't been with anybody else since Steph. "
        elif ep4CeceSexTalk == 1:
            $ ep4_end_cece += "\n\nWhen she asked you if you'd been with a lot of women, you lied to her and said that you hadn't been with anybody else since Steph. "
        elif ep4CeceSexTalk == 2:
            $ ep4_end_cece += "\n\nWhen she asked you if you'd been with a lot of women, you said yes. "
    else:
        $ ep4_end_cece = "You did not go for a night walk with Cece. "
    if ep4GotCoffee:
        $ ep4_end_cece += "\n\nIn the morning, you got her coffee. "
    else:
        $ ep4_end_cece += "\n\nIn the morning, you did not get her coffee. "
    if not ep3RejectedKira:
        $ ep4_end_cece += "\n\nShe found out that you and Kira had been having sex the day before. "
        if ep4NightChoose == 1:
            if ep4CeceSexTalk == 1:
                $ ep4_end_cece += "\nShe did not like it. "
            else:
                $ ep4_end_cece += "\nIt didn't seem to matter all that much to her. "
    $ ep4_end_cece += "\n\nAfter having talked to Steph, she advised you to bring her along. "
    if Impact_Steph:
        $ ep4_end_cece += "\nYou agreed. "
    else:
        $ ep4_end_cece += "\nYou declined. "

    if ep4AskedForDawgAutograph:
        $ ep4_end_cece += "\n\nYou were able to get Nite Dawgs autograph for Cece, but not the Bonus event. "
        $ ep4_end_cece += "\n{a=jump:ep4Dawg}Click here{/a} for a preview. "
    else:
        if ep4Dawgs:
            $ ep4_end_cece += "\n\nYou were able to get both Nite Dawgs autograph for Cece, and the Bonus event. "
            $ ep4_end_cece += "\n{a=jump:ep4Dawg}Click here{/a} for a preview. "
        else:
            $ ep4_end_cece += "\n\nYou were not able to get Nite Dawgs autograph for Cece, or the Bonus event. "

    $ ep4_opportunity_ce = 0
    if ep4NightChoose <> 1:
        $ ep4_opportunity_ce += 1
    else:
        if ep4CeceSexTalk == 1:
            $ ep4_opportunity_ce += 1
    if not ep4GotCoffee:
        $ ep4_opportunity_ce += 1
    if not ep4Dawgs:
        $ ep4_opportunity_ce += 1

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
                        textbutton "[ep4_end_cece]\n\nCece options missed: [ep4_opportunity_ce]\nCece points: [XPcece]" text_style "task_general_notify"

screen ep4_endscreen_kira:
    tag ep4_endscreen_kira
    add "ep4_es_kira_smile"
    $ ep4_end_kira = "Kira will be the focus of the third and final part of this Chapter. "




    $ ep4_opportunity_ki = 0



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
                        textbutton "[ep4_end_kira]\n\nKira options missed: [ep4_opportunity_ki]\nKria points: [XPkira]" text_style "task_general_notify"

screen ep4_endscreen_lexi:
    tag ep4_endscreen_lexi
    add "ep4_es_lexi_smile"
    $ ep4_end_lexi = "Lexi will be the focus of the second part of this Chapter. "



    $ ep4_opportunity_le = 0



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
                        textbutton "[ep4_end_lexi]\n\nLexi options missed: [ep4_opportunity_le]\nLexi points: [XPlexi]" text_style "task_general_notify"

screen ep4_endscreen_robin:
    tag ep4_endscreen_robin
    add "ep4_es_robin_smile"
    $ ep4_end_robin = "Robin will be the focus of the third and final part of this Chapter. "





    $ ep4_opportunity_ro = 0



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
                        textbutton "[ep4_end_robin]\n\nRobin options missed: [ep4_opportunity_ro]\nRobin points: [XProbin]" text_style "task_general_notify"

screen ep4_endscreen_stephanie:
    tag ep4_endscreen_stephanie
    if Impact_Steph:
        if ep4NightChoose == 7:
            add "ep4_es_steph_happy"
        else:
            add "ep4_es_steph_smile"
    else:
        add "ep4_es_steph_sad"
    if ep4NightChoose == 7:
        $ ep4_end_stephanie = "You decided to message her in the night to try and meet up again. "
    else:
        $ ep4_end_stephanie = "You did not message her in the night to try and meet up again. "

    $ ep4_end_stephanie += "\n\nWhen you realized she was already in Los Angeles, you went to see her. "

    $ ep4_end_stephanie += "\n\nUpon seeing her you were initially "
    if ep4StephConfrontationMood == 0:
        $ ep4_end_stephanie += "friendly"
    elif ep4StephConfrontationMood == 1:
        $ ep4_end_stephanie += "neutral"
    elif ep4StephConfrontationMood == 2:
        $ ep4_end_stephanie += "angry"
    $ ep4_end_stephanie += ". When she was done talking, you were "
    if ep4StephLeaveMode == 0:
        $ ep4_end_stephanie += "friendly"
    elif ep4StephLeaveMode == 1:
        $ ep4_end_stephanie += "neutral"
    elif ep4StephLeaveMode == 2:
        $ ep4_end_stephanie += "angry"
    $ ep4_end_stephanie += "."

    if ep4StephLeaveMode == 2:
        if Impact_Steph:
            $ ep4_end_stephanie += "\n\nYou still decided to bring her along for the rest of the trip."
        else:
            $ ep4_end_stephanie += "\n\nYou decided to not bring her along for the rest of the trip."
    else:
        if Impact_Steph:
            $ ep4_end_stephanie += "\n\nYou decided to bring her along for the rest of the trip."
        else:
            $ ep4_end_stephanie += "\n\nYou decided to not bring her along for the rest of the trip."

    if not ep4TNDSteph:
        $ ep4_end_stephanie += "\n\nYou did not want to hear what she had to say at the Truth or Dare, minitruths."

    if ep4NightChoose == 7:
        if ep4StephSunsetChoose:
            $ ep4_end_stephanie += "\n\nYou felt nostalgic sitting in the sunset with her and told her you could fix your relationship with her. "
            $ ep4_end_stephanie += "\nShe declined. "
        else:
            $ ep4_end_stephanie += "\n\nYou shared the sunset with her. "

    $ ep4_opportunity_st = 0
    if ep4NightChoose <> 7:
        $ ep4_opportunity_st += 1
    if not Impact_Steph:
        $ ep4_opportunity_st += 1
    if not ep4TNDSteph:
        $ ep4_opportunity_st += 1

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
                        textbutton "[ep4_end_stephanie]\n\nStephanie options missed: [ep4_opportunity_st]\nStephanie points: [XPstephanie]" text_style "task_general_notify"

screen ep4_endscreen_linda:
    tag ep4_endscreen_linda
    add "ep4_es_linda_smile"
    $ ep4_end_linda = "Linda will be the focus of the second part of this Chapter. "




    $ ep4_opportunity_li = 0



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
                        textbutton "[ep4_end_linda]\n\nLinda options missed: [ep4_opportunity_li]\nLinda points: [XPlinda]" text_style "task_general_notify"

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
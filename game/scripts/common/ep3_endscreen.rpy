screen ep3_endscreen:
    tag ep3_endscreen

    modal True

    $ newDia = renpy.count_newly_seen_dialogue_blocks()
    $ seenDia = renpy.count_seen_dialogue_blocks()
    $ totalDia = renpy.count_dialogue_blocks()

    $ ep3_bonusscene = 0
    if persistent.scene01:
        $ ep3_bonusscene += 1
    if persistent.scene02:
        $ ep3_bonusscene += 1
    if persistent.scene03:
        $ ep3_bonusscene += 1
    else:
        if ep3RespondedLexiEyes:
            $ persistent.scene03 = True
            $ ep3_bonusscene += 1

    $ ep3_opportunity = 0
    $ ep3_op_none = "."
    if not ep3PlaneParty:
        $ ep3_opportunity += 1
        $ ep3_op_none = "\nYou did not bring the party to Lexi's jet."

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
        action (ToggleScreen("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1000
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_kira")
        hover Transform("endscreen_kira_on")
        action (ToggleScreen("ep3_endscreen_kira"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1200
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_lexi")
        hover Transform("endscreen_lexi_on")
        action (ToggleScreen("ep3_endscreen_lexi"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1400
        ypos 100

    imagebutton:
        focus_mask True
        idle Transform("endscreen_robin")
        hover Transform("endscreen_robin_on")
        action (ToggleScreen("ep3_endscreen_robin"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1000
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_stephanie")
        hover Transform("endscreen_stephanie_on")
        action (ToggleScreen("ep3_endscreen_stephanie"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_linda"), Hide("ep3_endscreen_updateinfo"))
        xpos 1200
        ypos 350

    imagebutton:
        focus_mask True
        idle Transform("endscreen_linda")
        hover Transform("endscreen_linda_on")
        action (ToggleScreen("ep3_endscreen_linda"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_updateinfo"))
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

    if renpy.loadable("script04.rpyc"):
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_continue")
            hover Transform("ph_ic_continue_h")
            action (Hide("ep3_endscreen"), Hide("ep3_endscreen_updateinfo"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"), Jump("ch4Update"))
            xpos 1760
            ypos 900

    else:
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action (Hide("ep3_endscreen"), Hide("ep3_endscreen_updateinfo"), Hide("ep3_endscreen_cece"), Hide("ep3_endscreen_kira"), Hide("ep3_endscreen_lexi"), Hide("ep3_endscreen_robin"), Hide("ep3_endscreen_stephanie"), Hide("ep3_endscreen_linda"))
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
                        textbutton "Bonus-Scenes unlocked: [ep3_bonusscene]/3" text_style "task_general_notify"





                    frame:
                        background Frame("taskop_general",10,10)
                        xmaximum 550
                        xminimum 550
                        textbutton "Non romancable options missed: [ep3_opportunity] (this playthrough)[ep3_op_none]" text_style "task_general_notify"
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

screen ep3_endscreen_updateinfo:
    tag ep3_endscreen_updateinfo
    $ ep3_end_update = "If you've downloaded Chapter 4 as a patch, you can install it from here (incase the automatic update didn't go through). "
    $ ep3_end_update += "\n\nPatch file not found. "
    $ ep3_end_update += "\nIf you have already downloaded Chapter 4 as a patch, make sure you unzip the patch, and put it's contents in the game/ folder. "

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
                        textbutton "[ep3_end_update]" text_style "task_general_notify"

screen ep3_endscreen_cece:
    tag ep3_endscreen_cece
    add "ep3_epilogue_cece_blank"
    $ ep3_end_cece = "She started the Chapter by sleeping in. "
    if ep3RejectedKira:
        $ ep3_end_cece += "\n\nLater on, when you came home you walked in on her while drying up after a shower. She didn't seem to mind. "
        $ ep3_end_cece += "\n\nAfterwards you shared a moment. "
    $ ep3_end_cece += "\n\nOn the plane, you agreed you would try getting an autograph by Nite Dawg - one way or the other. "
    if ep3CeceDrinkMojito:
        $ ep3_end_cece += "\n\nYou managed to find the drink best suited for her. "
    if not ep3PlaneParty:
        $ ep3_end_cece += "\n\nYou did not manage to turn the flight into a party. "
    $ ep3_end_cece += "\n\nIn the evening, Chris told her the whole story about Stephanie, which made her think. "
    $ ep3_end_cece += "\n\nShe seems to be doing better. "

    $ ep3_opportunity_ce = 0
    if not ep3RejectedKira:
        $ ep3_opportunity_ce += 1
    if not ep3CeceDrinkMojito:
        $ ep3_opportunity_ce += 1
    if ep3ToldChrisWhoMcLike <> 2:
        $ ep3_opportunity_ce += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_ce += 1

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
                        textbutton "[ep3_end_cece]\n\nCece options missed: [ep3_opportunity_ce]\nCece points: [XPcece]" text_style "task_general_notify"

screen ep3_endscreen_kira:
    tag ep3_endscreen_kira
    add "ep3_epilogue_kira_blank"
    $ ep3_end_kira = "You got an explanation to why she had been acting a bit weird yesterday. She had seen you in Robin's apartment, and apparently they are in a relationship. "

    if ep3KiraSexTalk == 1:
        $ ep3_end_kira += "\n\nYou truthfully told her that nothing happened. "
    elif ep3KiraSexTalk == 2:
        $ ep3_end_kira += "\n\nWith a smile on your face you asked her to get the story from Robin instead - knowing very well nothing happened. "
    elif ep3KiraSexTalk == 3:
        $ ep3_end_kira += "\n\nYou admitted to having had sex with Robin while awaiting getting bitchslapped. Flabbergasted, you realized she was not going to slap you, and didn't mind at all. "
    elif ep3KiraSexTalk == 4:
        $ ep3_end_kira += "\n\nYou didn't feel like telling her about your and Robin's sexual adventures and asked her to get the story from Robin instead. She did a bit later on, and ... didn't mind it at all. "

    if Impact_KiraRobin:
        $ ep3_end_kira += "\n\nYou told Kira you were OK with her being in a relationship with Robin. "
    else:
        $ ep3_end_kira += "\n\nYou told Kira you didn't like her being in a relationship with Robin. "

    if ep3RejectedKira:
        $ ep3_end_kira += "\n\nBeing the straightforward person she is, she invited you home to her place to 'fuck like rabbits'. You decided to go home instead. "
    else:
        $ ep3_end_kira += "\n\nBeing the straightforward person she is, she invited you home to her place to 'fuck like rabbits'. Of course you couldn't turn down an offer like that. "
    if ep3KiraEndGame == 0:
        $ ep3_end_kira += "\n\nKira didn't get to feel your 'twirl', you talking her into submission, or showing her how to tame a wild horse. "
    elif ep3KiraEndGame == 1:
        $ ep3_end_kira += "\n\nYou talked Kira into submission after round one, and she happily went for another round. "
    elif ep3KiraEndGame == 2:
        $ ep3_end_kira += "\n\nYou showed Kira the twirl, and she happily went for another round. "
    elif ep3KiraEndGame == 3:
        $ ep3_end_kira += "\n\nYou showed Kira how to tame a wild horse, and she happily went for another round. "

    $ ep3_opportunity_ki = 0
    if ep3RejectedKira:
        $ ep3_opportunity_ki += 1
    if ep3KiraEndGame == 0:
        $ ep3_opportunity_ki += 1
    if ep3ToldChrisWhoMcLike <> 3 and ep3ToldChrisWhoMcLike <> 7:
        $ ep3_opportunity_ki += 1

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
                        textbutton "[ep3_end_kira]\n\nKira options missed: [ep3_opportunity_ki]\nKria points: [XPkira]" text_style "task_general_notify"

screen ep3_endscreen_lexi:
    tag ep3_endscreen_lexi
    add "ep3_epilogue_lexi_blank"
    $ ep3_end_lexi = "She called you while you were at the Cafe with Kira and invited you and your friends to her place in LA. "
    if ep3SawLexiTopless:
        $ ep3_end_lexi += "\n\nOn the plane you saw her topless. You went to see her just a bit too early. You did not get to take a picture of her. "
    if ep3SawLexiDress:
        $ ep3_end_lexi += "\n\nOn the plane she showed you her new dress. You have a feeling that what she really wanted to show you was the parts not covered by the dress. "
        if ep3LexiPhoto:
            $ ep3_end_lexi += "\n\nYou got to take a picture of her by her request in that dress. "
    if ep3SaidHiToKevin:
        $ ep3_end_lexi += "\n\nShe absolutely adored that you said hi to her driver, Kevin, before entering the limo. "
    else:
        $ ep3_end_lexi += "\n\nYou didn't seem to notice her driver, Kevin. "
    if "ep3_leximsg1" in cam_gallery:
        $ ep3_end_lexi += "\n\nShe got a very good impression of you while texting the evening before the departure. "
    if "ep3_leximsg2" in cam_gallery:
        $ ep3_end_lexi += "\n\nShe enjoyed texting with you on the evening before the departure. "
    if not ep3PlaneParty:
        $ ep3_end_lexi += "\n\nYou did not manage to turn the flight into a party. "


    $ ep3_opportunity_le = 0
    if not ep3SaidHiToKevin:
        $ ep3_opportunity_le += 1
    if ep3TimePassed >= 2:
        $ ep3_opportunity_le += 1
    if not ep3LexiPhoto:
        $ ep3_opportunity_le += 1
    if ep3ToldChrisWhoMcLike <> 1:
        $ ep3_opportunity_le += 1
    if not ep3RespondedLexiExtended:
        $ ep3_opportunity_le += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_le += 1

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
                        textbutton "[ep3_end_lexi]\n\nLexi options missed: [ep3_opportunity_le]\nLexi points: [XPlexi]" text_style "task_general_notify"

screen ep3_endscreen_robin:
    tag ep3_endscreen_robin
    add "ep3_epilogue_robin_blank"
    $ ep3_end_robin = "You went to the Cafe with Kira and met her there. "
    if Impact_KiraRobin:
        $ ep3_end_robin += "\n\nYou told Kira you were OK with them being in a relationship. "
    else:
        $ ep3_end_robin += "\n\nYou told Kira you didn't like them being in a relationship. "

    $ ep3_opportunity_ro = 0
    if ep3ToldChrisWhoMcLike <> 4 and ep3ToldChrisWhoMcLike <> 7:
        $ ep3_opportunity_ro += 1

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
                        textbutton "[ep3_end_robin]\n\nRobin options missed: [ep3_opportunity_ro]\nRobin points: [XProbin]" text_style "task_general_notify"

screen ep3_endscreen_stephanie:
    tag ep3_endscreen_stephanie
    add "ep3_epilogue_steph_blank"
    $ ep3_end_stephanie = "It would seem she did tell you she was going away after all, though not in an obvious eye to eye kind of way. "
    $ ep3_end_stephanie += "\n\nYou should hear her out when you get an opportunity to do so. Closure or forgiveness. "
    $ ep3_end_stephanie += "After all, you can't really move forwards until you've buried the past. "
    if ep3ToldChrisWhoMcLike == 6:
        $ ep3_end_stephanie += "\n\nYou told Chris that you love her."

    $ ep3_opportunity_st = 0
    if ep3ToldChrisWhoMcLike <> 6:
        $ ep3_opportunity_st += 1

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
                        textbutton "[ep3_end_stephanie]\n\nStephanie options missed: [ep3_opportunity_st]\nStephanie points: [XPstephanie]" text_style "task_general_notify"

screen ep3_endscreen_linda:
    tag ep3_endscreen_linda
    add "ep3_epilogue_linda_blank"
    $ ep3_end_linda = "Linda has been out a whole lot, trying to get a job? "
    $ ep3_end_linda += "\n\nYou still haven't had a chance to sit down and talk to her properly."
    if Impact_KiraRobin:
        if ep3LindaWatchRK:
            $ ep3_end_linda += "\n\nShe seemed to get turned on by watching Kira and Robin going at it on the airplane."
    if not ep3PlaneParty:
        $ ep3_end_linda += "\n\nYou did not manage to turn the flight into a party. "
    if ep3LimoLindaPic:
        $ ep3_end_linda += "\n\nYou taking her picture in the limo, greatly pleased her."

    $ ep3_opportunity_li = 0
    if not ep3LookedLinda:
        $ ep3_opportunity_li += 1
    if ep3ToldChrisWhoMcLike <> 5:
        $ ep3_opportunity_li += 1
    if not ep3LimoLindaPic:
        $ ep3_opportunity_li += 1
    if not ep3PlaneParty:
        $ ep3_opportunity_li += 1

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
                        textbutton "[ep3_end_linda]\n\nLinda options missed: [ep3_opportunity_li]\nLinda points: [XPlinda]" text_style "task_general_notify"

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

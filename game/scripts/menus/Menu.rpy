screen MenuScreen:
    tag MenuScreen
    add "bg_empty" alpha 0.5
    modal True
    text "Show Hints and Stats" size 60 xalign 0.15 ypos 100 color "#A0A0A0"
    vbox:
        xpos 200
        ypos 200
        text "You can click on the image of your Love Interest and it will activate that character for hints.\n\nRobin and Kira are special cases where both can be selected.\n\nBelow that you can select if you just want hints or hints and stats.\n\nIf no Love Interests are selected, No hints will be supplied.\n\nYou can also click on the Menu colors below to cycle through color options." size 15 color "#A0A0A0" xsize 600 ysize 600
        text ""
        text ""
        text "Menus will appear with the following colors:" size 20
        text ""
        hbox:
            vbox:
                xpos 20
                textbutton "Good response: " text_color "#E0E0E0" text_size 20
                textbutton "Neutral Response:" text_color "#E0E0E0" text_size 20
                textbutton "Bad Response:" text_color "#E0E0E0" text_size 20
            vbox:
                xpos 20
                hbox:
                    if Best == "#00FF00":
                        textbutton "Kiss Cece" action SetVariable("Best","#32CD32") text_color Best text_size 20
                    elif Best == "#32CD32":
                        textbutton "Kiss Cece" action SetVariable("Best","#008000") text_color Best text_size 20
                    elif Best == "#008000":
                        textbutton "Kiss Cece" action SetVariable("Best","#00FF00") text_color Best text_size 20
                    textbutton " (" text_color "#E0E0E0" text_size 20
                    if Good == "#0000FF":
                        textbutton "Cece+1" action SetVariable("Good","#4682B4") text_color Good text_size 20
                    elif Good == "#4682B4":
                        textbutton "Cece+1" action SetVariable("Good","#00BFFF") text_color Good text_size 20
                    elif Good == "#00BFFF":
                        textbutton "Cece+1" action SetVariable("Good","#0000FF") text_color Good text_size 20
                    textbutton ")" text_color "#E0E0E0" text_size 20
                hbox:
                    textbutton "Do nothing" text_color "#E0E0E0" text_size 20
                hbox:
                    if Worst == "#FF0000":
                        textbutton "Insult Cece" action SetVariable("Worst","#800000") text_color Worst text_size 20
                    elif Worst == "#800000":
                        textbutton "Insult Cece" action SetVariable("Worst","#F08080") text_color Worst text_size 20
                    elif Worst == "#F08080":
                        textbutton "Insult Cece" action SetVariable("Worst","#FF0000") text_color Worst text_size 20
                    textbutton " (" text_color "#E0E0E0" text_size 20
                    if Bad == "#FFA500":
                        textbutton "Cece-10" action SetVariable("Bad","#FF8C00") text_color Bad text_size 20
                    elif Bad == "#FF8C00":
                        textbutton "Cece-10" action SetVariable("Bad","#FFD700") text_color Bad text_size 20
                    elif Bad == "#FFD700":
                        textbutton "Cece-10" action SetVariable("Bad","#FFA500") text_color Bad text_size 20
                    textbutton ")" text_color "#E0E0E0" text_size 20
    if MenuChoiceCece:
        imagebutton focus_mask True xpos 1000 ypos 100 idle Transform("statscreen_cece_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1075 ypos 300 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1000 ypos 100 idle Transform("statscreen_cece_bw") action (SetVariable("MenuChoiceCece",True),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Inactive" xcenter 1075 ypos 300 text_color "#9e0f25"

    if MenuChoiceKira:
        imagebutton focus_mask True xpos 1200 ypos 100 idle Transform("statscreen_kira_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1275 ypos 300 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1200 ypos 100 idle Transform("statscreen_kira_bw") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",True),SetVariable("MenuChoiceStephanie",False))
        textbutton "Inactive" xcenter 1275 ypos 300 text_color "#9e0f25"

    if MenuChoiceLexi:
        imagebutton focus_mask True xpos 1400 ypos 100 idle Transform("statscreen_lexi_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1475 ypos 300 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1400 ypos 100 idle Transform("statscreen_lexi_bw") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",True),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Inactive" xcenter 1475 ypos 300 text_color "#9e0f25"

    if MenuChoiceRobin:
        imagebutton focus_mask True xpos 1000 ypos 450 idle Transform("statscreen_robin_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1075 ypos 650 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1000 ypos 450 idle Transform("statscreen_robin_bw") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceRobin",True),SetVariable("MenuChoiceStephanie",False))
        textbutton "Inactive" xcenter 1075 ypos 650 text_color "#9e0f25"

    if MenuChoiceStephanie:
        imagebutton focus_mask True xpos 1200 ypos 450 idle Transform("statscreen_stephanie_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1275 ypos 650 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1200 ypos 450 idle Transform("statscreen_stephanie_bw") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",True))
        textbutton "Inactive" xcenter 1275 ypos 650 text_color "#9e0f25"

    if MenuChoiceLinda:
        imagebutton focus_mask True xpos 1400 ypos 450 idle Transform("statscreen_linda_color") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",False),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Active" xcenter 1475 ypos 650 text_color "#008000"
    else:
        imagebutton focus_mask True xpos 1400 ypos 450 idle Transform("statscreen_linda_bw") action (SetVariable("MenuChoiceCece",False),SetVariable("MenuChoiceLinda",True),SetVariable("MenuChoiceLexi",False),SetVariable("MenuChoiceKira",False),SetVariable("MenuChoiceRobin",False),SetVariable("MenuChoiceStephanie",False))
        textbutton "Inactive" xcenter 1475 ypos 650 text_color "#9e0f25"

    if MenuChoiceBestChoiceStatsTest:
        vbox:
            xpos 1600
            ypos 380
            textbutton "Hints\n   &\nStats" xcenter 150 ycenter 200 text_color "#008000" action (SetVariable("MenuChoiceBestChoiceStats","Hints"),SetVariable("MenuChoiceBestChoiceStatsTest",False))
    else:
        vbox:
            xpos 1600
            ypos 380
            textbutton "Hints" xcenter 150 ycenter 200 text_color "#008000" action (SetVariable("MenuChoiceBestChoiceStats","HintsStats"),SetVariable("MenuChoiceBestChoiceStatsTest",True))

    if MenuChoiceCece == False and MenuChoiceLinda == False and MenuChoiceLexi == False and MenuChoiceKira == False and MenuChoiceRobin == False and MenuChoiceStephanie == False:
        $ MenuChoice = "HintsNone"
    elif MenuChoiceBestChoiceStats == "HintsStats":
        if MenuChoiceCece:
            $ MenuChoice = "HintsStatsCece"
        elif MenuChoiceLinda:
            $ MenuChoice = "HintsStatsLinda"
        elif MenuChoiceLexi:
            $ MenuChoice = "HintsStatsLexi"
        elif MenuChoiceKira and MenuChoiceRobin:
            $ MenuChoice = "HintsStatsKiraRobin"
        elif MenuChoiceKira:
            $ MenuChoice = "HintsStatsKira"
        elif MenuChoiceRobin:
            $ MenuChoice = "HintsStatsRobin"
        elif MenuChoiceStephanie:
            $ MenuChoice = "HintsStatsStephanie"
    elif MenuChoiceBestChoiceStats == "Hints":
        if MenuChoiceCece:
            $ MenuChoice = "HintsCece"
        elif MenuChoiceLinda:
            $ MenuChoice = "HintsLinda"
        elif MenuChoiceLexi:
            $ MenuChoice = "HintsLexi"
        elif MenuChoiceKira and MenuChoiceRobin:
            $ MenuChoice = "HintsKiraRobin"
        elif MenuChoiceKira:
            $ MenuChoice = "HintsKira"
        elif MenuChoiceRobin:
            $ MenuChoice = "HintsRobin"
        elif MenuChoiceStephanie:
            $ MenuChoice = "HintsStephanie"
    else:
        $ MenuChoice = "HintsNone"
    $ MenuInfo[0] = MenuChoice
    $ MenuInfo[1] = Best
    $ MenuInfo[2] = Worst
    $ MenuInfo[3] = Good
    $ MenuInfo[4] = Bad
    imagebutton focus_mask True idle Transform("ph_ic_continue") hover Transform("ph_ic_continue_h") action (Hide("MenuScreen"),Return(MenuInfo)) xpos 1760 ypos 900

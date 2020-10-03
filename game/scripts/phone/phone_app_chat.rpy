
screen phone_chat:
    tag phone_chat
    modal True
    add "phone_bg_chat"
    key custom_phone_key action (Hide("phone_chat"), Show("phone_full"))
    vpgrid:
        xpos 0.505
        ypos 0.17
        ysize 0.7
        xsize 0.5
        cols 1
        spacing 0
        draggable True
        mousewheel True

        scrollbars "vertical"
        side_xalign 0.5
        xfill True
        yfill True
        xmaximum 410
        xminimum 410
        yminimum 690
        ymaximum 690

        if contact_cece:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_cece:
                            idle "cont_cece_smln"
                            hover "cont_cece_smln_h"
                            action (SetVariable("chat_notify_cece",False), SetVariable("chat_sel_name","Cece"), SetVariable("chat_sel_icon","cont_cece"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_cece_sml"
                            hover "cont_cece_sml_h"
                            action (SetVariable("chat_sel_name","Cece"), SetVariable("chat_sel_icon","cont_cece"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ce]" text_style "contactlist_ce" action (SetVariable("chat_notify_cece",False), SetVariable("chat_sel_name","Cece"), SetVariable("chat_sel_icon","cont_cece"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_chris:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_chris:
                            idle "cont_chris_smln"
                            hover "cont_chris_smln_h"
                            action (SetVariable("chat_notify_chris",False), SetVariable("chat_sel_name","Chris"), SetVariable("chat_sel_icon","cont_chris"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_chris_sml"
                            hover "cont_chris_sml_h"
                            action (SetVariable("chat_sel_name","Chris"), SetVariable("chat_sel_icon","cont_chris"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ch]" text_style "contactlist_ch" action (SetVariable("chat_notify_chris",False), SetVariable("chat_sel_name","Chris"), SetVariable("chat_sel_icon","cont_chris"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_christine:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_christine:
                            idle "cont_christine_smln"
                            hover "cont_christine_smln_h"
                            action (SetVariable("chat_notify_christine",False), SetVariable("chat_sel_name","Christine"), SetVariable("chat_sel_icon","cont_christine"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_christine_sml"
                            hover "cont_christine_sml_h"
                            action (SetVariable("chat_sel_name","Christine"), SetVariable("chat_sel_icon","cont_christine"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[cr]" text_style "contactlist_cr" action (SetVariable("chat_notify_christine",False), SetVariable("chat_sel_name","Christine"), SetVariable("chat_sel_icon","cont_christine"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_holly:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_holly:
                            idle "cont_holly_smln"
                            hover "cont_holly_smln_h"
                            action (SetVariable("chat_notify_holly",False), SetVariable("chat_sel_name","Holly"), SetVariable("chat_sel_icon","cont_holly"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_holly_sml"
                            hover "cont_holly_sml_h"
                            action (SetVariable("contact_sel_name","Holly"), SetVariable("chat_sel_icon","cont_holly"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ho]" text_style "contactlist_ho" action (SetVariable("chat_notify_holly",False), SetVariable("chat_sel_name","Holly"), SetVariable("chat_sel_icon","cont_holly"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_jane:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_jane:
                            idle "cont_jane_smln"
                            hover "cont_jane_smln_h"
                            action (SetVariable("chat_notify_jane",False), SetVariable("chat_sel_name","Jane"), SetVariable("chat_sel_icon","cont_jane"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_jane_sml"
                            hover "cont_jane_sml_h"
                            action (SetVariable("chat_sel_name","Jane"), SetVariable("chat_sel_icon","cont_jane"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ja]" text_style "contactlist_ja" action (SetVariable("chat_notify_jane",False), SetVariable("chat_sel_name","Jane"), SetVariable("chat_sel_icon","cont_jane"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_kira:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_kira:
                            idle "cont_kira_smln"
                            hover "cont_kira_smln_h"
                            action (SetVariable("chat_notify_kira",False), SetVariable("chat_sel_name","Kira"), SetVariable("chat_sel_icon","cont_kira"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_kira_sml"
                            hover "cont_kira_sml_h"
                            action (SetVariable("chat_sel_name","Kira"), SetVariable("chat_sel_icon","cont_kira"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ki]" text_style "contactlist_ki" action (SetVariable("chat_notify_kira",False), SetVariable("chat_sel_name","Kira"), SetVariable("chat_sel_icon","cont_kira"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_lexi:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_lexi:
                            idle "cont_lexi_smln"
                            hover "cont_lexi_smln_h"
                            action (SetVariable("chat_notify_lexi",False), SetVariable("chat_sel_name","Lexi"), SetVariable("chat_sel_icon","cont_lexi"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_lexi_sml"
                            hover "cont_lexi_sml_h"
                            action (SetVariable("chat_sel_name","Lexi"), SetVariable("chat_sel_icon","cont_lexi"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[le]" text_style "contactlist_le" action (SetVariable("chat_notify_lexi",False), SetVariable("chat_sel_name","Lexi"), SetVariable("chat_sel_icon","cont_lexi"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_linda:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_linda:
                            idle "cont_linda_smln"
                            hover "cont_linda_smln_h"
                            action (SetVariable("chat_notify_linda",False), SetVariable("chat_sel_name","Linda"), SetVariable("chat_sel_icon","cont_linda"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_linda_sml"
                            hover "cont_linda_sml_h"
                            action (SetVariable("chat_sel_name","Linda"), SetVariable("chat_sel_icon","cont_linda"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[li]" text_style "contactlist_li" action (SetVariable("chat_notify_linda",False), SetVariable("chat_sel_name","Linda"), SetVariable("chat_sel_icon","cont_linda"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_matt:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_matt:
                            idle "cont_matt_smln"
                            hover "cont_matt_smln_h"
                            action (SetVariable("chat_notify_matt",False), SetVariable("chat_sel_name","Matt"), SetVariable("chat_sel_icon","cont_matt"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_matt_sml"
                            hover "cont_matt_sml_h"
                            action (SetVariable("chat_sel_name","Matt"), SetVariable("chat_sel_icon","cont_matt"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ma]" text_style "contactlist_ma" action (SetVariable("chat_notify_matt",False), SetVariable("chat_sel_name","Matt"), SetVariable("chat_sel_icon","cont_matt"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_robin:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_robin:
                            idle "cont_robin_smln"
                            hover "cont_robin_smln_h"
                            action (SetVariable("chat_notify_robin",False), SetVariable("chat_sel_name","Robin"), SetVariable("chat_sel_icon","cont_robin"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_robin_sml"
                            hover "cont_robin_sml_h"
                            action (SetVariable("chat_sel_name","Robin"), SetVariable("chat_sel_icon","cont_robin"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[ro]" text_style "contactlist_ro" action (SetVariable("chat_notify_robin",False), SetVariable("chat_sel_name","Robin"), SetVariable("chat_sel_icon","cont_robin"), Hide("phone_chat"), Show("phone_chat_single"))

        if contact_stephanie:
            vbox:
                hbox:
                    add "cont_background"
                    imagebutton:
                        xoffset -363
                        yoffset 8
                        if chat_notify_stephanie:
                            idle "cont_stephanie_smln"
                            hover "cont_stephanie_smln_h"
                            action (SetVariable("chat_notify_stephanie",False), SetVariable("chat_sel_name","Stephanie"), SetVariable("chat_sel_icon","cont_stephanie"), Hide("phone_chat"), Show("phone_chat_single"))
                        else:
                            idle "cont_stephanie_sml"
                            hover "cont_stephanie_sml_h"
                            action (SetVariable("chat_sel_name","Stephanie"), SetVariable("chat_sel_icon","cont_stephanie"), Hide("phone_chat"), Show("phone_chat_single"))
                    vbox:
                        xoffset -363
                        yoffset 8
                        xminimum 400
                        textbutton "[st]" text_style "contactlist_st" action (SetVariable("chat_notify_stephanie",False), SetVariable("chat_sel_name","Stephanie"), SetVariable("chat_sel_icon","cont_stephanie"), Hide("phone_chat"), Show("phone_chat_single"))

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_back")
        hover Transform("ph_ic_back_h")
        action (Hide("phone_chat"), Show("phone_full"))
        xpos 760
        ypos 860

    imagebutton:
        focus_mask True
        idle Transform("ph_ic_exit")
        hover Transform("ph_ic_exit_h")
        action Hide("phone_chat")
        xpos 910
        ypos 860


screen phone_chat_single:
    tag phone_chat_single
    modal True
    add "phone_bg_chat"







    vpgrid:
        xalign 0.505
        ypos 0.17
        xmaximum 400
        xminimum 400
        yminimum 510
        ymaximum 510
        spacing 4
        cols 1
        xfill True
        yfill True
        draggable True
        mousewheel True
        scrollbars "vertical"
        side_xalign 0.505
        vbox spacing 8:
            box_reverse True
            if chat_sel_name == "Cece":

                $ chat_temp = chat_cece.copy()
            elif chat_sel_name == "Chris":
                $ chat_temp = chat_chris.copy()
            elif chat_sel_name == "Christine":
                $ chat_temp = chat_christine.copy()
            elif chat_sel_name == "Holly":
                $ chat_temp = chat_holly.copy()
            elif chat_sel_name == "Jane":
                $ chat_temp = chat_jane.copy()
            elif chat_sel_name == "Kira":
                $ chat_temp = chat_kira.copy()
            elif chat_sel_name == "Lexi":
                $ chat_temp = chat_lexi.copy()
            elif chat_sel_name == "Linda":
                $ chat_temp = chat_linda.copy()
            elif chat_sel_name == "Matt":
                $ chat_temp = chat_matt.copy()
            elif chat_sel_name == "Robin":
                $ chat_temp = chat_robin.copy()
            elif chat_sel_name == "Stephanie":
                $ chat_temp = chat_stephanie.copy()
            else:
                $ chat_temp = []
            $ chat_showexit = True
            $ chat_picture = ""
            $ chat_active = ""
            $ chat_counted = 1
            $ chat_temp0 = ""
            $ chat_temp1 = ""
            $ chat_temp2 = ""
            $ chat_temp3 = ""
            $ i = 0

            for x in chat_temp:
                $ chat_active = chat_temp[i]
                $ y = chat_active.split(";")
                $ chat_temp0 = y[0]
                $ chat_temp1 = y[1]
                $ chat_temp2 = y[2]
                $ chat_temp3 = y[3]
                $ i += 1
                if chat_temp2 <> "999999":
                    if chat_temp0 == "0":
                        hbox spacing 4:
                            imagebutton:
                                idle Transform("cont_blank_sml")
                                action NullAction()
                            vbox spacing 8:
                                frame:
                                    background Frame("chat_bg_me",10,10)
                                    xmaximum 336
                                    xminimum 336
                                    if chat_temp1 == "0":
                                        textbutton "[chat_temp3]" text_style "chat_me"
                                    elif chat_temp1 == "1":
                                        imagebutton:
                                            idle Transform(chat_temp3 + "_sml")
                                            action (Show("phone_chat_picture"), SetVariable("chat_picture",chat_temp3))
                    elif chat_temp0 == "2":
                        hbox spacing 4:
                            imagebutton:
                                idle Transform("cont_blank_sml")
                                action NullAction()
                            vbox spacing 8:
                                frame:
                                    background Frame("chat_bg_other",10,10)
                                    xmaximum 336
                                    xminimum 336
                                    if chat_temp1 == "0":
                                        textbutton "{i}{size=18}{color=#ffff77}[chat_temp3]{/color}{/size}{/i}" text_style "chat_other"
                    else:
                        frame:
                            background Frame("chat_bg_other",10,10)
                            xmaximum 380
                            xminimum 380
                            has hbox spacing 4
                            imagebutton:
                                idle Transform(chat_sel_icon)
                                action NullAction()
                            vbox spacing 8:
                                if chat_temp1 == "0":
                                    textbutton "[chat_temp3]" text_style "chat_other"
                                elif chat_temp1 == "1":
                                    imagebutton:
                                        idle Transform(chat_temp3 + "_sml")
                                        action (Show("phone_chat_picture"), SetVariable("chat_picture",chat_temp3))
    if chat_temp2 == "1":
        if todayIs <= 1:
            if phChatCanReplyChris:
                $ chat_showexit = False
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox

                    textbutton "Sure, wassup." text_style "chatreply" action AddToSet(chat_chris,"0;0;2;Sure, wassup.")
    elif chat_temp2 == "2":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if AssesOrBreasts == 1:
                textbutton "Wait for reply" text_style "chatreply" action (AddToSet(chat_chris,"1;1;3;ep1_photoop_kira_ass"), AddToSet(cam_gallery,"ep1_photoop_kira_ass"))
            elif AssesOrBreasts == 2:
                textbutton "Wait for reply" text_style "chatreply" action (AddToSet(chat_chris,"1;1;3;ep1_photoop_kira_boob"), AddToSet(cam_gallery,"ep1_photoop_kira_boob"))
    elif chat_temp2 == "3":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if AssesOrBreasts == 1:
                textbutton "Wait. You took a picture of Kira's ass?" text_style "chatreply" action AddToSet(chat_chris,"0;0;4;Wait. You took a picture of Kira's ass?")
            elif AssesOrBreasts == 2:
                textbutton "Wait. You took a picture of Kira's boobs?" text_style "chatreply" action AddToSet(chat_chris,"0;0;5;Wait. You took a picture of Kira's boobs?")
    elif chat_temp2 == "4":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;6;Of course, assman. That was your preference, no?")
    elif chat_temp2 == "5":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;11;Of course, breastman. That was your preference, no?")
    elif chat_temp2 == "6":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "That's just creepy." text_style "chatreply" action AddToSet(chat_chris,"0;0;7;That's just creepy.")
    elif chat_temp2 == "7":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;8;You should have seen the first one. I accidentally took an upskirt.")
    elif chat_temp2 == "8":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Send it, asap!" text_style "chatreply" action AddToSet(chat_chris,"0;0;9;Well, what are you waiting for? Send that one too!")
        frame:
            background Frame("reply_action_opt",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "You suck at taking pictures" text_style "chatreply" action AddToSet(chat_chris,"0;0;10;You suck at taking pictures.")
            else:
                textbutton "You suck at taking pictures" text_style "chatreplygood" action AddToSet(chat_chris,"0;0;10;You suck at taking pictures.")
    elif chat_temp2 == "9":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;20;Haha. GOT YA!!! No upskirt. Now who's the creep!")
    elif chat_temp2 == "10":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;20;Right back at ya!")
    elif chat_temp2 == "11":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "That's just creepy." text_style "chatreply" action AddToSet(chat_chris,"0;0;12;That's just creepy. At least you didn't follow her to the dressing room.")
    elif chat_temp2 == "12":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;13;Yeah, about that. I might just have... Those pictures were a bit better though.")
    elif chat_temp2 == "13":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Send it, asap!" text_style "chatreply" action AddToSet(chat_chris,"0;0;14;Well, what are you waiting for? Send them!")
        frame:
            background Frame("reply_action_opt",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "You suck at taking pictures" text_style "chatreply" action AddToSet(chat_chris,"0;0;15;You suck at taking pictures.")
            else:
                textbutton "You suck at taking pictures" text_style "chatreplygood" action AddToSet(chat_chris,"0;0;15;You suck at taking pictures.")
    elif chat_temp2 == "14":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;20;Haha. GOT YA!!! Of course i didn't. Now who's the creep!")
    elif chat_temp2 == "15":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;20;Right back at ya!")
    elif chat_temp2 == "20":
        if "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;2" not in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit conversation" text_style "chatreply" action (RemoveFromSet(phone_task_list,"1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;1"), AddToSet(phone_task_list,"1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;2"), SetVariable("d1_responded_chris","1"), Call("norollback"))
    elif chat_temp2 == "101":
        if todayIs <= 1:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Thank her for the FapFrappy." text_style "chatreply" action (AddToSet(chat_kira,"0;0;102;Best FapFrappy I've ever had!\n//Secret admirer"), SetVariable("d1_responded_kira","1"), SetVariable("chat_bowling_required",False))
                else:
                    textbutton "Thank her for the FapFrappy." text_style "chatreplygood" action (AddToSet(chat_kira,"0;0;102;Best FapFrappy I've ever had!\n//Secret admirer"), SetVariable("d1_responded_kira","1"), SetVariable("chat_bowling_required",False))
            frame:
                background Frame("reply_action_opt",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Joke about it." text_style "chatreply" action (AddToSet(chat_kira,"0;0;102;Hopefully I got the number right. Your handwriting is absolutely terrible :p\n//FapFrappy"), SetVariable("d1_responded_kira","2"), SetVariable("chat_bowling_required",False))
    elif chat_temp2 == "102":
        if "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;2" not in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "She's probably working now. Let's wait." text_style "chatreply" action (RemoveFromSet(phone_task_list,"2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;1"), AddToSet(phone_task_list,"2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;2"), Call("norollback"))
    elif chat_temp2 == "201":
        if todayIs == 1:

            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "I dreamt about you last night." text_style "chatreply" action (AddToSet(chat_stephanie,"0;0;202;I dreamt about you last night. It was a good dream :)"))
                else:
                    textbutton "I dreamt about you last night." text_style "chatreplygood" action (AddToSet(chat_stephanie,"0;0;202;I dreamt about you last night. It was a good dream :)"))
            frame:
                background Frame("reply_action_opt",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Seek answers." text_style "chatreply" action (AddToSet(chat_stephanie,"0;0;202;I still hope that some day we can sit down for a cup of coffee and have a chat about the past. It's long overdue."))
    elif chat_temp2 == "202":
        if not d1_responded_stephanie:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Honestly, I dont think I will get a reply." text_style "chatreply" action (SetVariable("d1_responded_stephanie",True), Call("norollback"))
    elif chat_temp2 == "301":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Nah, relaxing at home. How come?" text_style "chatreply" action AddToSet(chat_kira,"0;0;311;Nah, I'm relaxing at home. How come?")
    elif chat_temp2 == "302":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Of course. Happens to me all the time." text_style "chatreply" action AddToSet(chat_kira,"0;0;303;Of course, happens to me every day. Lots of guys staring at my ass while I'm writing my phone number on Fapfrappys.")
    elif chat_temp2 == "303":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;304;lol. You'd be perfect for selling burgers! But... you busy?")
    elif chat_temp2 == "304":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Nah, relaxing at home. How come?" text_style "chatreply" action AddToSet(chat_kira,"0;0;311;Nah, I'm relaxing at home. How come?")
    elif chat_temp2 == "311":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;312;I just got off work. AND I'm bored. Want to hang out for a bit, or you have other plans?")
    elif chat_temp2 == "312":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Sure thing. A stroll in the park maybe?" text_style "chatreply" action AddToSet(chat_kira,"0;0;315;Sure thing. How about a little stroll in the park?")








    elif chat_temp2 == "313":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;314;Another time then. :)")
    elif chat_temp2 == "314":
        if "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;0" not in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "That probably could have gone better." text_style "chatreply" action (RemoveFromSet(phone_task_list,"3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;1"), AddToSet(phone_task_list,"3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;0"), Hide("phone_notify"), Jump("beforeEveningStroll"), Call("norollback"))
    elif chat_temp2 == "315":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;316;Actually, I have a better idea. A friend of mine is opening a new bowling alley downtown. You want to check it out with me?")
    elif chat_temp2 == "316":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I'd love to!" text_style "chatreply" action AddToSet(chat_kira,"0;0;317;I'd love to! Where?")
    elif chat_temp2 == "317":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;318;It's on main street. Top floor of the Plaza. Red door. You can't miss it. See you there in 30?")
    elif chat_temp2 == "318":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "See you there." text_style "chatreply" action AddToSet(chat_kira,"0;0;319;See you there. :)")
    elif chat_temp2 == "319":
        if "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;2" not in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "I should get ready." text_style "chatreply" action (RemoveFromSet(phone_task_list,"3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;1"), AddToSet(phone_task_list,"3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;2"), Hide("phone_chat_single"), Hide("phone_notify"), Jump("goingOutWithKira"), Call("norollback"))
    elif chat_temp2 == "601":
        $ chat_showexit = False
        frame:
            background Frame("chat_bg_exit",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Hmmm..." text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep1WhatAboutKira"))
    elif chat_temp2 == "602":
        $ chat_showexit = False
        frame:
            background Frame("chat_bg_exit",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Hmmm..." text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep1WhatAboutKira"))
    elif chat_temp2 == "603":
        $ chat_showexit = False
        frame:
            background Frame("chat_bg_exit",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Hmmm..." text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep1WhatAboutKira"))
    elif chat_temp2 == "611":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;616;Thank you. At least I feel better now.")
    elif chat_temp2 == "612":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;614;Oh yeah? This huge ass certainly got your attention. :)")
    elif chat_temp2 == "613":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;616;I would like that. :)")
    elif chat_temp2 == "614":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Camera was at fault" text_style "chatreply" action AddToSet(chat_kira,"0;0;615;Noooooooo... It was a camera misfire. Won't happen again... Maybe...")
    elif chat_temp2 == "615":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;616;Assman.")
    elif chat_temp2 == "616":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "About the ticket" text_style "chatreply" action AddToSet(chat_kira,"0;0;617;I tried checking if I could get an extra ticket for Metronome for you today. But unfortunately, no luck. Sorry.")
    elif chat_temp2 == "617":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;618;Don't worry about it. I didn't have any real expectations knowing how hard they are to come by. But you have fun though. Go get them girls.")
    elif chat_temp2 == "618":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Nah, I'll be thinking about you" text_style "chatreply" action (AddToSet(chat_kira,"0;0;619;I'm pretty sure you'll be on my mind though."), SetVariable("d1_responded_kira_thinkingof",1))
            else:
                textbutton "Nah, I'll be thinking about you" text_style "chatreplygood" action (AddToSet(chat_kira,"0;0;619;I'm pretty sure you'll be on my mind though."), SetVariable("d1_responded_kira_thinkingof",1))
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Thanks" text_style "chatreply" action AddToSet(chat_kira,"0;0;619;Thanks, I will. Enjoy yourself as well sweetie.")
    elif chat_temp2 == "619":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;620;Flattery will get you everywhere. :)")
    elif chat_temp2 == "620":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"0;0;621;:-*")
    elif chat_temp2 == "621":
        if "4;2;1;2;0;0;Kira;Answer Kira before;Metronome tickets for Kira;1" in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit conversation" text_style "chatreply" action (RemoveFromSet(phone_task_list,"4;2;1;2;0;0;Kira;Answer Kira before;Metronome tickets for Kira;1"), AddToSet(phone_task_list,"4;2;1;2;0;0;Kira;Answer Kira before;Metronome tickets for Kira;4"), Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep1WhatAboutKiraChoseChris"), Call("norollback"))
    elif chat_temp2 == "701":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;703;It's past 10. Of course I'm awake.")
    elif chat_temp2 == "703":
        $ chat_showexit = False
        if ep1_bowling_normalselfie:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send selfie of you and Kira" text_style "chatreply" action AddToSet(chat_chris,"0;1;704;ep1_bowling_kira_me_selfie_nice")
        else:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send selfie of you and Kira" text_style "chatreply" action AddToSet(chat_chris,"0;1;704;ep1_bowling_kira_me_selfie_goof")
    elif chat_temp2 == "704":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;705;OMGWTF! HOW DID THAT HAPPEN?")
    elif chat_temp2 == "705":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Tell you later" text_style "chatreply" action AddToSet(chat_chris,"0;0;706;I'll tell you all about it later when you get here. Just thought you might enjoy that. :D")
    elif chat_temp2 == "706":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;707;ENJOY??? I'm so fucking happy for you right now, you don't even know. Finally you're back!")
    elif chat_temp2 == "707":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Ask for an extra ticket to Metronome" text_style "chatreply" action (AddToSet(chat_chris,"0;0;708;Look...I have to ask you this. I promised Kira I would ask you if that boss of yours got a third ticket...for her?"), SetVariable("ep1KiraRepliedMsgTickets",True))
            else:
                textbutton "Ask for an extra ticket to Metronome" text_style "chatreplygood" action (AddToSet(chat_chris,"0;0;708;Look...I have to ask you this. I promised Kira I would ask you if that boss of yours got a third ticket...for her?"), SetVariable("ep1KiraRepliedMsgTickets",True))
        frame:
            background Frame("reply_action_opt",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Don't ask him" text_style "chatreply" action AddToSet(chat_chris,"0;0;710;I guess I owe you a thank you for that stunt at MaKenzie.")
    elif chat_temp2 == "708":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;709;Do you have any idea how hard these are to come by?")
    elif chat_temp2 == "709":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Sorry, I promised her I'd ask" text_style "chatreply" action AddToSet(chat_chris,"0;0;712;No problem, it's fine. Just promised her I'd ask you.")
    elif chat_temp2 == "710":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;711;Oh, I'll find some way for you to return that, don't you worry.")
    elif chat_temp2 == "711":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Now I am worried" text_style "chatreply" action AddToSet(chat_chris,"0;0;712;Ok, now I'm worried.")
    elif chat_temp2 == "712":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;713;Yeah, you just get ready for tonight. Let's rock this joint.")
    elif chat_temp2 == "713":
        if "1;2;2;0;0;0;Chris;Be home at;Chris is coming over.;1" in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit conversation" text_style "chatreply" action (RemoveFromSet(phone_task_list,"1;2;2;0;0;0;Chris;Be home at;Chris is coming over.;1"), AddToSet(phone_task_list,"1;2;2;0;0;0;Chris;Be home at;Chris is coming over.;2"), Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep1WhatAboutKira2"), Call("norollback"))
    elif chat_temp2 == "702":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;716;It's past 10. Of course I'm awake.")
    elif chat_temp2 == "716":
        $ chat_showexit = False
        if ep1_bowling_normalselfie:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send selfie of you and Kira" text_style "chatreply" action AddToSet(chat_chris,"0;1;717;ep1_bowling_kira_me_selfie_nice")
        else:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send selfie of you and Kira" text_style "chatreply" action AddToSet(chat_chris,"0;1;717;ep1_bowling_kira_me_selfie_goof")
    elif chat_temp2 == "717":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;718;OMGWTF! HOW DID THAT HAPPEN?")
    elif chat_temp2 == "718":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "We went bowling" text_style "chatreply" action AddToSet(chat_chris,"0;0;719;We kinda ended up bowling yesterday.")
    elif chat_temp2 == "719":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;720;I'm so fucking happy for you right now, you don't even know. Finally you're back!")
    elif chat_temp2 == "720":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Bad news" text_style "chatreply" action AddToSet(chat_chris,"0;0;721;Are you sitting down right now? Because you're going to hate me for what I'm about to say.")
    elif chat_temp2 == "721":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;722;What's going on bro...")
    elif chat_temp2 == "722":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I lost the tickets (lie)" text_style "chatreply" action AddToSet(chat_chris,"0;0;723;I don't really know how to say this but...I lost the tickets to Metronome on my date with Kira yesterday.")
    elif chat_temp2 == "723":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;724;Nononono...Don't joke about this man. Tell me you're joking.")
    elif chat_temp2 == "724":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I wish I could" text_style "chatreply" action AddToSet(chat_chris,"0;0;725;I wish I could.")
    elif chat_temp2 == "725":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"0;0;726;Talk to me man...")
    elif chat_temp2 == "726":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait longer" text_style "chatreply" action AddToSet(chat_chris,"0;0;727;Say something...")
    elif chat_temp2 == "727":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait even longer" text_style "chatreply" action AddToSet(chat_chris,"1;0;728;Fuck man. That's just horrible. I was really looking forward to going today.")
    elif chat_temp2 == "728":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I'm so sorry" text_style "chatreply" action AddToSet(chat_chris,"0;0;729;I'm so sorry man. I really am. I feel awful.")
    elif chat_temp2 == "729":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;730;You know what. It's fine. I'm really happy for you though. Scrolling back to that picture actually put a smile on my face again. You deserve this.")
    elif chat_temp2 == "730":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I'm a fucking idiot" text_style "chatreply" action AddToSet(chat_chris,"0;0;731;I'm a fucking idiot.")
    elif chat_temp2 == "731":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;732;Yeah, you are. But we'll get another chance.")
    elif chat_temp2 == "732":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I'm a fucking idiot" text_style "chatreply" action AddToSet(chat_chris,"0;0;733;I'm going to make it my life purpose to make it up to you. I promise.")
    elif chat_temp2 == "733":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;734;I know you will man. Don't worry.")
    elif chat_temp2 == "916":
        if not ep2RespondedChris:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Text him back" text_style "chatreply" action AddToSet(chat_chris,"0;0;917;Yeah, I'm awake. And I feel I owe you like a thousand apologies for leaving you yesterday. Sorry man. Truly.")
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Call him back" text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), SetVariable("call_sel_text",contact_text_chris), SetVariable("call_sel_name",ch), SetVariable("call_sel_icon","cont_chris"), Jump("ep2InterCallingChris"))
                else:
                    textbutton "Call him back" text_style "chatreplygood" action (Hide("phone_chat_single"), Hide("phone_notify"), SetVariable("call_sel_text",contact_text_chris), SetVariable("call_sel_name",ch), SetVariable("call_sel_icon","cont_chris"), Jump("ep2InterCallingChris"))
    elif chat_temp2 == "917":
        if not ep2RespondedChris:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Wait for reply" text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), Jump("ep2InterChrisCalling"))
    elif chat_temp2 == "1001":
        if todayIs == 3:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Flirty reply" text_style "chatreply" action AddToSet(chat_kira,"0;0;1002;Hey Sexy. Yes, I had a good time. :D")
                else:
                    textbutton "Flirty reply" text_style "chatreplygood" action AddToSet(chat_kira,"0;0;1002;Hey Sexy. Yes, I had a good time. :D")
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Friendly reply" text_style "chatreply" action AddToSet(chat_kira,"0;0;1002;Hey Kira. Yes, I had a good time.")
    elif chat_temp2 == "1002":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1003;Oh, come on. You got to give me some more details than that! :p")
    elif chat_temp2 == "1003":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Tell her about Lexi" text_style "chatreply" action AddToSet(chat_kira,"0;0;1004;We had this completely unknown artist performing. Lexi something...")
    elif chat_temp2 == "1004":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1005;Nooooooo way. THE Lexi???")
    elif chat_temp2 == "1005":
        $ chat_showexit = False
        if ep1AskedLexiForChris:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send picture of Chris and Lexi" text_style "chatreply" action AddToSet(chat_kira,"0;1;1006;ep1_metro_bar_selfie03")
        else:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Send picture of you and Lexi" text_style "chatreply" action AddToSet(chat_kira,"0;1;1006;ep1_metro_bar_selfie01")
    elif chat_temp2 == "1006":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1007;That is sooo awesome! You got to talk to her?? Was she nice?")
    elif chat_temp2 == "1007":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Talk about Lexi" text_style "chatreply" action AddToSet(chat_kira,"0;0;1008;She was the sweetest, most down to earth kind of person you'll ever meet. And we even shared a bottle of wine. :)")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Tell her next time you meet" text_style "chatreply" action AddToSet(chat_kira,"0;0;1009;I'll tell you all about it next time we meet. :)")
            else:
                textbutton "Tell her next time you meet" text_style "chatreplygood" action AddToSet(chat_kira,"0;0;1009;I'll tell you all about it next time we meet. :)")
    elif chat_temp2 == "1008":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1010;I am so envious. So... you want to meet up again? Tell me all about it in person? I also miss looking at your cute butt. :)")
    elif chat_temp2 == "1009":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1010;I'd love to! When?")
    elif chat_temp2 == "1010":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Today?" text_style "chatreply" action AddToSet(chat_kira,"0;0;1011;Are you comming by Robin today? To help out on her launch?")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Tomorrow?" text_style "chatreply" action AddToSet(chat_kira,"0;0;1015;How about tomorrow?")
            else:
                textbutton "Tomorrow?" text_style "chatreplygood" action AddToSet(chat_kira,"0;0;1015;How about tomorrow?")
    elif chat_temp2 == "1011":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1012;No. I got evening shift today, and morning shift tomorrow, so it's right home and sleep after work today :(")
    elif chat_temp2 == "1012":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I'll text you tomorrow then." text_style "chatreply" action AddToSet(chat_kira,"0;0;1013;How about I text you tomorrow then, and see what happens?")
    elif chat_temp2 == "1013":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1014;Sounds good, handsome. Have a nice day! :-*")
    elif chat_temp2 == "1014":
        if not "6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;1" in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit conversation" text_style "chatreply" action (AddToSet(phone_task_list,"6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;1"), Hide("phone_chat_single"), Hide("phone_notify"), SetVariable("phone_taskadd","New task\nText Kira tomorrow."), SetVariable("ep2KiraReply",True), Call("norollback"))
    elif chat_temp2 == "1015":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1016;It's a date then! Come pick me up after work? I get off at 16:00.")
    elif chat_temp2 == "1016":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Can't wait." text_style "chatreply" action AddToSet(chat_kira,"0;0;1017;Sure. Looking forward to it. :)")
    elif chat_temp2 == "1017":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1018;Me too! :-*")
    elif chat_temp2 == "1018":
        if not "6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;1" in phone_task_list:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit conversation" text_style "chatreply" action (AddToSet(phone_task_list,"6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;1"), Hide("phone_chat_single"), Hide("phone_notify"), SetVariable("phone_taskadd","New task\nPick up Kira at MaKenzie in two days."), SetVariable("ep2KiraReply",True), Call("norollback"))
    elif chat_temp2 == "1201":

        if todayIs == 4:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "I'm up now." text_style "chatreply" action (AddToSet(chat_linda,"0;0;1202;I'm up now. :)"))
    elif chat_temp2 == "1202":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action (AddToSet(chat_linda,"1;0;1203;Enjoy your morning. We're just out and about. :) Be back soon."))
    elif chat_temp2 == "1203":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Have fun." text_style "chatreply" action (AddToSet(chat_linda,"0;0;1204;Have fun."))
    elif chat_temp2 == "1204":
        if not ep2LindaCheckedMsg:
            if todayIs == 4:
                $ chat_showexit = False
                frame:
                    background Frame("chat_bg_exit",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Exit conversation" text_style "chatreply" action (Hide("phone_chat_single"), Hide("phone_notify"), SetVariable("ep2LindaCheckedMsg",True), Jump("ep2AfterLindaCheckedMsg"))
    elif chat_temp2 == "1301":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1302;Feeling much better bro. I slept for 12 hours straight.")
    elif chat_temp2 == "1302":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Want to meet up?" text_style "chatreply" action AddToSet(chat_chris,"0;0;1303;Good to hear. I'm headed out now. Want to meet up?")
    elif chat_temp2 == "1303":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1304;Sure. I need a word with you anyway.")
    elif chat_temp2 == "1304":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Meet at Ashley's?" text_style "chatreply" action AddToSet(chat_chris,"0;0;1305;Yeah, me too. Can you meet me at that store... Ashley's?")
    elif chat_temp2 == "1305":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1306;Sounds good to me. 30 minutes?")
    elif chat_temp2 == "1306":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Sure." text_style "chatreply" action AddToSet(chat_chris,"0;0;1307;Sure, and I got a huge surprise for you.")
    elif chat_temp2 == "1307":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1308;Surprise? Do tell!")
    elif chat_temp2 == "1308":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Got a surprise" text_style "chatreply" action AddToSet(chat_chris,"0;0;1309;Eh... You kinda don't get the ...surprise... part do you?")
    elif chat_temp2 == "1309":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1310;30 minutes then.")
    elif chat_temp2 == "1310":
        if not ep2PhoneTextChrisRestaurant:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Head over to Ashley's." text_style "chatreply" action (SetVariable("ep2PhoneTextChrisRestaurant",True), Call("norollback"))
    elif chat_temp2 == "1401":
        if todayIs == 4:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Are you ok?" text_style "chatreply" action AddToSet(chat_kira,"0;0;1402;Are you ok?")
                else:
                    textbutton "Are you ok?" text_style "chatreplygood" action AddToSet(chat_kira,"0;0;1402;Are you ok?")
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Sure, we can try again some other time." text_style "chatreply" action AddToSet(chat_kira,"0;0;1404;Sure, we can try again some other time?")
    elif chat_temp2 == "1402":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1403;Yeah, don't worry about it.")
    elif chat_temp2 == "1403":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Flirty goodbye" text_style "chatreply" action AddToSet(chat_kira,"0;0;1405;Have a nice day sweetie, and hope to see you soon.")
            else:
                textbutton "Flirty goodbye" text_style "chatreplygood" action AddToSet(chat_kira,"0;0;1405;Have a nice day sweetie, and hope to see you soon.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Normal goodbye." text_style "chatreply" action AddToSet(chat_kira,"0;0;1405;Ok. Have a nice day.")
    elif chat_temp2 == "1404":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1405;Yeah, we can.")
    elif chat_temp2 == "1405":
        if not "6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;2" in phone_task_list:
            if not ep2KiraReplyTwo:
                $ chat_showexit = False
                frame:
                    background Frame("chat_bg_exit",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Exit Conversation." text_style "chatreply" action (RemoveFromSet(phone_task_list,"6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;1"), AddToSet(phone_task_list,"6;4;2;3;5;9;Kira;Let's see what happens before;Get in touch with Kira.;2"), SetVariable("ep2KiraReplyTwo",True), Call("norollback"))
    elif chat_temp2 == "1501":
        if todayIs == 4:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "I'm not sure we did the right thing." text_style "chatreply" action AddToSet(chat_robin,"0;0;1502;Listen, Robin. This is kinda weird, but I'm not sure we did the right thing? I mean, it was great, but maybe ... at least take it a bit slow?")
            if ep2OptToReplyRobin:
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 780
                    has hbox
                    if MenuChoice == "HintsNone":
                        textbutton "Something tells me I should have stayed the night?" text_style "chatreply" action AddToSet(chat_robin,"0;0;1503;Something tells me I should have stayed the night? :D Unfortunately, I'm a bit busy right now. Truly sorry. :)")
                    else:
                        textbutton "Something tells me I should have stayed the night?" text_style "chatreplygood" action AddToSet(chat_robin,"0;0;1503;Something tells me I should have stayed the night? :D Unfortunately, I'm a bit busy right now. Truly sorry. :)")
    elif chat_temp2 == "1502":
        if ep2RespondedRobin == 0:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Hmmm. Weird. No reply." text_style "chatreply" action (SetVariable("ep2RespondedRobin",1), Call("norollback"))
    elif chat_temp2 == "1503":
        if ep2RespondedRobin == 0:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Hmmm. Weird. No reply." text_style "chatreply" action (SetVariable("ep2RespondedRobin",2), Call("norollback"))
    elif chat_temp2 == "1701":
        if ep3PhoneEventLexi:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Confirm." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1702;You bet. I'm really looking forward to it.")
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Chat with her." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1705;Sounds perfect. I'm really looking forward to it. And you? Got some time off from your busy schedule?")
                else:
                    textbutton "Chat with her." text_style "chatreplygood" action AddToSet(chat_lexi,"0;0;1705;Sounds perfect. I'm really looking forward to it. And you? Got some time off from your busy schedule?")
    elif chat_temp2 == "1702":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1703;Me too. See you tomorrow then. :)")
    elif chat_temp2 == "1703":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "We'll be there." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1704;We'll be there.")
    elif chat_temp2 == "1704":
        if not ep3RespondedLexi:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep3RespondedLexi",True), SetVariable("ep3PhoneEventLexi",False), Call("norollback"))
    elif chat_temp2 == "1705":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1706;That is so nice to hear. And yes, you have no idea. This tour was almost too much. But now I have several months off! :)")
    elif chat_temp2 == "1706":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "That gives you plenty of time to be just normal." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1707;Well, if nothing else, that gives you plenty of time to be just a normal non-superstar person then.")
    elif chat_temp2 == "1707":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1708;That's one of the things I liked about you when I met you at that club. Somehow you saw me underneath it all.")
    elif chat_temp2 == "1708":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Normal response." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1709;I just saw a woman. A very nice woman that I enjoyed spending time with.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Flirty response." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1716;I just saw a woman. A very sexy one at that, but still just a woman.")
            else:
                textbutton "Flirty response." text_style "chatreplygood" action AddToSet(chat_lexi,"0;0;1716;I just saw a woman. A very sexy one at that, but still just a woman.")
    elif chat_temp2 == "1709":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1710;I can't deny that I'm getting good vibes from you. Let's make this a summer to remember.")
    elif chat_temp2 == "1710":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I would love that." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1711;I would love that. Sweet dreams to you.")
    elif chat_temp2 == "1711":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1712;You too, hun.")
    elif chat_temp2 == "1712":
        $ chat_showexit = False
        frame:
            background Frame("chat_bg_exit",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Exit Conversation." text_style "chatreply" action AddToSet(chat_lexi,"1;0;1713;Oh, before I forget...")
    elif chat_temp2 == "1713":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action (AddToSet(chat_lexi,"1;1;1714;ep3_leximsg1"), AddToSet(cam_gallery,"ep3_leximsg1"), SetVariable("phGallNotify",True))
    elif chat_temp2 == "1714":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Beautiful eyes." text_style "chatreply" action (AddToSet(chat_lexi,"0;0;1715;There we are again with those beautiful eyes. :-*"), SetVariable("ep3RespondedLexiEyes",True))
            else:
                textbutton "Beautiful eyes." text_style "chatreplygood" action (AddToSet(chat_lexi,"0;0;1715;There we are again with those beautiful eyes. :-*"), SetVariable("ep3RespondedLexiEyes",True))
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Thank her for the picture." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1715;Fantastic picture. I love it.")
    elif chat_temp2 == "1715":
        if not ep3RespondedLexi:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep3RespondedLexi",True), SetVariable("ep3RespondedLexiExtended",True), SetVariable("ep3PhoneEventLexi",False), Call("norollback"))
    elif chat_temp2 == "1716":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1717;Way too many hours of dancing is bound to tighten the body up somehow. :p Maybe I can teach you?")
    elif chat_temp2 == "1717":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Show me, then maybe." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1718;Tell you what. You show me those dance moves, and then I'll decide. :D")
    elif chat_temp2 == "1718":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1719;Who knows, maybe I will. Let's make this a summer to remember.")
    elif chat_temp2 == "1719":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "I would love that." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1720;I would love that. Sweet dreams to you.")
    elif chat_temp2 == "1720":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_lexi,"1;0;1721;You too, hun.")
    elif chat_temp2 == "1721":
        $ chat_showexit = False
        frame:
            background Frame("chat_bg_exit",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Exit Conversation." text_style "chatreply" action AddToSet(chat_lexi,"1;0;1722;Oh, before I forget...")
    elif chat_temp2 == "1722":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action (AddToSet(chat_lexi,"1;1;1723;ep3_leximsg2"), AddToSet(cam_gallery,"ep3_leximsg2"), SetVariable("phGallNotify",True))
    elif chat_temp2 == "1723":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Breathtaking." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1724;Breathtaking as always. You just melted my screen.")
            else:
                textbutton "Breathtaking." text_style "chatreplygood" action AddToSet(chat_lexi,"0;0;1724;Breathtaking as always. You just melted my screen.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Thank her for the picture." text_style "chatreply" action AddToSet(chat_lexi,"0;0;1724;Fantastic picture. I love it.")
    elif chat_temp2 == "1724":
        if not ep3RespondedLexi:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep3RespondedLexi",True), SetVariable("ep3RespondedLexiExtended",True), SetVariable("ep3PhoneEventLexi",False), Call("norollback"))
    elif chat_temp2 == "1801":
        if ep3PhoneEventChris:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Still excited about tomorrow?" text_style "chatreply" action AddToSet(chat_chris,"0;0;1802;Still excited about tomorrow?")
    elif chat_temp2 == "1802":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1803;Of course I am! And my bag broke...")
    elif chat_temp2 == "1803":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Don't overthink it." text_style "chatreply" action AddToSet(chat_chris,"0;0;1804;Don't overthink it. Let's just go there and have the time of our life.")
    elif chat_temp2 == "1804":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1805;Thanx man. That actually helped a bit.")
    elif chat_temp2 == "1805":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Sleep tight." text_style "chatreply" action AddToSet(chat_chris,"0;0;1831;Sleep tight dude. We'll pick you up at around 11.")
        if "ep3_leximsg1" in cam_gallery:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Send the picture of Lexi." text_style "chatreply" action AddToSet(chat_chris,"0;1;1808;ep3_leximsg1")
                else:
                    textbutton "Send the picture of Lexi." text_style "chatreplygood" action AddToSet(chat_chris,"0;1;1808;ep3_leximsg1")
        elif "ep3_leximsg2" in cam_gallery:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 780
                has hbox
                if MenuChoice == "HintsNone":
                    textbutton "Send the picture of Lexi." text_style "chatreply" action AddToSet(chat_chris,"0;1;1808;ep3_leximsg2")
                else:
                    textbutton "Send the picture of Lexi." text_style "chatreplygood" action AddToSet(chat_chris,"0;1;1808;ep3_leximsg2")
    elif chat_temp2 == "1807":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1805;Ok, now I'm nervous again!")
    elif chat_temp2 == "1808":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1809;Ok, now I'm nervous again!")
    elif chat_temp2 == "1809":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Sleep tight." text_style "chatreply" action AddToSet(chat_chris,"0;0;1831;Sleep tight dude. We'll pick you up at around 11.")
    elif chat_temp2 == "1831":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_chris,"1;0;1832;I'll be ready.")
    elif chat_temp2 == "1832":
        if not ep3RespondedChris:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep3RespondedChris",True), SetVariable("ep3PhoneEventChris",False), Call("norollback"))
    elif chat_temp2 == "1902":
        if ep3PhoneEventKira:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Me too!" text_style "chatreply" action AddToSet(chat_kira,"0;0;1903;Me too! I just got a message from Lexi (you know the one that definitely won't call me after one meeting).")
    elif chat_temp2 == "1903":
        $ chat_showexit = False
        if not ep3RejectedKira:
            if not ep2RejectedRobin:
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1904;OK. OK. You got me on that one. But thank you for today. I haven't been fucked like that ever. And Robin tells me to say the same about the other night when you two were getting it on. :-*")
            else:
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1904;OK. OK. You got me on that one. But thank you for today. I haven't been fucked like that ever. Robin got all hot when I told her. :-*")
        else:
            if not ep2RejectedRobin:
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1904;OK. OK. You got me on that one. Robin just told me the deets about you two the other day. She literally talked me into an orgasm. :-*")
            else:
                frame:
                    background Frame("reply_action",10,10)
                    xmaximum 336
                    xminimum 336
                    xpos 804
                    ypos 700
                    has hbox
                    textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1904;OK. OK. You got me on that one. But you know what that means, right? It means she must really like you. :-*")
    elif chat_temp2 == "1904":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Moving on..." text_style "chatreply" action AddToSet(chat_kira,"0;0;1905;Ok... Moving on... :p So, Lexi's plane lands on the airport by 11:30 tomorrow. So we have to be there around then. Preferably a bit earlier.")
    elif chat_temp2 == "1905":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1906;Sure thing, tiger. We'll be there.")
    elif chat_temp2 == "1906":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "See you tomorrow." text_style "chatreply" action AddToSet(chat_kira,"0;0;1907;See you both tomorrow, and Sweet dreams.")
    elif chat_temp2 == "1907":
        $ chat_showexit = False
        if Impact_KiraRobin:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1908;Oh, I will dream sexy dreams alright. But not before Robin finishes eating me out.")
        else:
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_kira,"1;0;1908;You too.")
    elif chat_temp2 == "1908":
        if not ep3RespondedKira:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep3RespondedKira",True), SetVariable("ep3PhoneEventKira",False), Call("norollback"))
    elif chat_temp2 == "2001":
        if ep4StephImpactTextOpen:
            $ chat_showexit = False
            frame:
                background Frame("reply_action",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2002;Hey " + name + ". Yes, I'm up. How are you?")
    elif chat_temp2 == "2002":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "I found your letter today." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2003;I just wanted to tell you that I found your letter today. It didn't really explain much, but it still meant a lot to me.")
            else:
                textbutton "I found your letter today." text_style "chatreplygood" action AddToSet(chat_stephanie,"0;0;2003;I just wanted to tell you that I found your letter today. It didn't really explain much, but it still meant a lot to me.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Is there any chance we can meet some day?" text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2005;I hope you can meet me someday soon and explain the whole situation. I don't know why you decided to hide it all, but I want to meet up and talk about it.")
    elif chat_temp2 == "2003":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2004;You found it now? I'm sorry, I should have known. I mean, when I saw you the other day.")
    elif chat_temp2 == "2004":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "It was quite cryptic anyway." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2005;It was quite cryptic anyway. But if you're interested, I hope we can meet up one day to talk a bit.")
    elif chat_temp2 == "2005":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2006;I would love that. But... I'm out of town right now. Don't know really when I'll be back.")
    elif chat_temp2 == "2006":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Same here." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2007;Same here. But I think you owe me. At least I hope you think so too.")
    elif chat_temp2 == "2007":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2008;It's not that easy. But if you really want to, I will. But honestly, you should just move on.")
    elif chat_temp2 == "2008":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "I can't move on until you tell me." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2009;I can't move on until I know. I've tried, but ... I have to know.")
            else:
                textbutton "I can't move on until you tell me." text_style "chatreplygood" action AddToSet(chat_stephanie,"0;0;2009;I can't move on until I know. I've tried, but ... I have to know.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Don't start that again. You owe me." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2009;Don't start that again. You owe me. I have to know.")
    elif chat_temp2 == "2009":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2010;Ok... But, I'm staying with a friend of mine now. Let me work something out, and I'll text you tomorrow.")
    elif chat_temp2 == "2010":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            if MenuChoice == "HintsNone":
                textbutton "Thank you." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2016;Ok. That works for me. Thank you.")
            else:
                textbutton "Thank you." text_style "chatreplygood" action AddToSet(chat_stephanie,"0;0;2016;Ok. That works for me. Thank you.")
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 780
            has hbox
            textbutton "Do you still love me?" text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2011;Can you just answer one question now... Do you still love me?")
    elif chat_temp2 == "2011":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2012;I'm sorry. I ... have to go now. My friend is starting to give me weird looks.")
    elif chat_temp2 == "2012":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "You're about to cry, aren't you." text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2013;You're about to cry, aren't you.")
    elif chat_temp2 == "2013":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2014;I never cry...")
    elif chat_temp2 == "2014":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Good night" text_style "chatreply" action AddToSet(chat_stephanie,"0;0;2015;Text me when you have a chance. I'll be waiting. Good night.")
    elif chat_temp2 == "2015":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2017;Good night, " + name + ".")
    elif chat_temp2 == "2016":
        $ chat_showexit = False
        frame:
            background Frame("reply_action",10,10)
            xmaximum 336
            xminimum 336
            xpos 804
            ypos 700
            has hbox
            textbutton "Wait for reply" text_style "chatreply" action AddToSet(chat_stephanie,"1;0;2015;I ... have to go now. My friend is starting to give me weird looks.")
    elif chat_temp2 == "2017":
        if ep4StephImpactTextOpen:
            $ chat_showexit = False
            frame:
                background Frame("chat_bg_exit",10,10)
                xmaximum 336
                xminimum 336
                xpos 804
                ypos 700
                has hbox
                textbutton "Exit Conversation." text_style "chatreply" action (SetVariable("ep4StephImpactTextOpen",False), Call("norollback"))



    if chat_showexit:
        $ renpy.block_rollback()
        imagebutton:
            focus_mask True
            idle Transform("ph_ic_back")
            hover Transform("ph_ic_back_h")
            action (Hide("phone_chat_single"), Show("phone_chat"))
            xpos 760
            ypos 860

        imagebutton:
            focus_mask True
            idle Transform("ph_ic_exit")
            hover Transform("ph_ic_exit_h")
            action Hide("phone_chat_single")
            xpos 910
            ypos 860


    $ renpy.block_rollback()

screen phone_chat_picture:
    tag phone_chat_picture
    modal True
    key custom_phone_key action (Hide("phone_chat_picture"), SetVariable("chat_picture",""))
    imagebutton:
        focus_mask True
        idle Transform(chat_picture)
        hover Transform(chat_picture)
        action (Hide("phone_chat_picture"), SetVariable("chat_picture",""))
        xpos 0
        ypos 0
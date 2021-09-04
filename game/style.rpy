init 500:

    style say_dialogue:
        outlines [(2, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"

        color "#ffffff"

    style choice_button_text:
        outlines [(2, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"

        color "#ffffff"

    style say_label:
        outlines [(2, "#222222", 0, 0)]

        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"








    style contactlist:
        color "#ffffff"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_me:
        color "#49f145"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ce:
        color "#9f91f9"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ch:
        color "#3ac5ff"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_cr:
        color "#ffffff"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ho:
        color "#fe3b3b"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ja:
        color "#ffffff"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ki:
        color "#3ae0d2"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_le:
        color "#fffc00"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_li:
        color "#ff4280"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ma:
        color "#4e6bff"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_ro:
        color "#f9a491"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style contactlist_st:
        color "#f145ef"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"
        size 30

    style chat_other:
        color "#ffffff"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#777777"

        size 20
        font "HelveticaNeueLt.ttf"

    style chat_me:
        color "#ffffff"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#008ec2"

        size 20
        font "HelveticaNeueLt.ttf"

    style chat_comment:
        color "#000000"
        size 18
        font "HelveticaNeueLt.ttf"

    style chatreply:
        color "#ffffff"
        outlines [(2, "#001180", 0, 0)]
        hover_color "ffff00"
        size 20
        font "HelveticaNeueMed.ttf"

    style chatreplygood:
        color "#00FF00"
        outlines [(2, "#001180", 0, 0)]
        hover_color "ffff00"
        size 20
        font "HelveticaNeueMed.ttf"

    style task_op_ok:
        color "#000000"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#027802"
        size 20
        font "HelveticaNeueLt.ttf"

    style task_op_uk:
        color "#000000"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#737301"
        size 20
        font "HelveticaNeueLt.ttf"

    style task_op_na:
        color "#000000"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#770101"
        size 20
        font "HelveticaNeueLt.ttf"

    style task_op_notify:
        color "#ffffff"
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#010177"
        size 18
        font "HelveticaNeueLt.ttf"

    style task_general_notify:
        color "#ffffff"
        outlines [(2, "#222222", 0, 0)]
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#010177"
        size 22
        font "HelveticaNeueLt.ttf"

    style music_credits:
        color "#ffffff"
        hover_color "ffff00"
        outlines [(2, "#222222", 0, 0)]
        drop_shadow [(-0.5, -0.5)]
        drop_shadow_color "#010177"
        size 22
        font "HelveticaNeueLt.ttf"

    style ic:
        color "#ffaaaa"
        outlines [(1, "#222222", 0, 0)]
        drop_shadow [(2.5, 2.5)]
        drop_shadow_color "#000000"
        hover_color "ffff77"

    style popup:
        xpadding 2
        ypadding 2

    style popup is button:

        background "#70707f"
        hover_background "#90909f"
        xmaximum 250
        xfill True

    style popup_text is text:
        size 22
        hover_color "#ffffff"
        outlines [(0, "#000000", 0, 0)]
        color "#000000"
        font "HelveticaNeueLt.ttf"

    style popupclosed:
        xpadding 2
        ypadding 2

    style popupclosed is button:

        background "#ff0000"
        hover_background "#ff0000"
        xmaximum 250
        xfill True

    style popupclosed_text is text:
        size 22
        hover_color "#ffffff"
        outlines [(0, "#000000", 0, 0)]
        color "#ffcccc"
        font "HelveticaNeueLt.ttf"

    style midscreentxt:
        size 50
        color "#4ab5b5"
        font "RalewayBold.ttf"

    style betatxt:
        size 50
        color "#ff4444"
        font "RalewayBold.ttf"

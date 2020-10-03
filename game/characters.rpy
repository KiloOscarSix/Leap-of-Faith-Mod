define mod = Character("OscarSix", color="#0f0")

define me = DynamicCharacter("name", color="#49f145")
define mel = DynamicCharacter("sname", color="#49f145")


define ch = Character("Chris", color="#3ac5ff")
define ma = Character("Matt", color="#6b4eff")
define ml = Character("Melvin", color="#4e6bff")

define ce = Character("Cece", color="#9f91f9")
define ki = Character("Kira", color="#3ae0d2")
define le = Character("Lexi", color="#fffc00")
define li = Character("Linda", color="#ff4280")
define ro = Character("Robin", color="#f9a491")
define st = Character("Stephanie", color="#f145ef")
define ho = Character("Holly", color="#fe3b3b")


define uk = Character("???", color="#aaaaaa")
define carr = Character("Courier", color="#aaaaaa")
define bart = Character("Bartender", color="#aaaaaa")
define inte = Character("Intercom", color="#aaaaaa")
define pr = Character("Priscilla", color="#aaaaaa")
define he = Character("Helen", color="#aaaaaa")
define clerk = Character("Clerk", color="#aaaaaa")
define ke = Character("Kevin", color="#aaaaaa")
define ja = Character("Jane", color="#aaaaaa")
define cr = Character("Christine", color="#aaaaaa")
define nd = Character("Night Dawg", color="#000000")

define evaluationRight = Character("", window_ypos=0.4, window_xpos=0.94, what_xmaximum=650)
define evaluationLeft = Character("", window_ypos=0.4, window_xpos=0.318, what_xmaximum=650)

screen toprightmsg:
    tag toprightmsg
    modal False
    imagebutton at show_hide_dissolve:
        idle "bg_toprightmsg"
        xalign 0.9825
        yalign -0.01
        action NullAction()
    text "[msgToDisplay]" at show_hide_dissolve:
        xalign 0.97
        yalign 0.018
        size 31
        color "#ffffff"
transform show_hide_dissolve:
    on show:
        alpha .0
        linear 1.0 alpha 1.0
    on hide:
        alpha 1.0
        linear 1.0 alpha .0
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

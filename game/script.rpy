label norollback:
$ renpy.block_rollback()
return

label start:
define MenuChoiceCece = False
define MenuChoiceLinda = False
define MenuChoiceLexi = False
define MenuChoiceKira = False
define MenuChoiceRobin = False
define MenuChoiceStephanie = False
define MenuChoiceKiraRobin = False
define MenuChoiceKiraRobin = False
define MenuChoiceAllGirls = "NoGirls"
define MenuChoiceAllGirlsTest = False
define MenuChoiceBestChoiceStats = "HintsStats"
define MenuChoiceBestChoiceStatsTest = True
define MenuChoiceTemp = ""
define MenuInfo = ["HintsNone","#00FF00","#F08080","#00BFFF","#FFA500"]
define Best = MenuInfo[1]
define Worst = MenuInfo[2]
define Good = MenuInfo[3]
define Bad = MenuInfo[4]
define CF = "{/color}"
define abPersName = ""
define abNotTelling = ""
define ceFamMenu = ""
define MenuChoice = " "

call screen MenuScreen nopredict

$ MenuChoice = _return[0]
$ Best = "{color=" + _return[1] + "}"
$ Worst = "{color=" + _return[2] + "}"
$ Good = "{color=" + _return[3] + "}"
$ Bad = "{color=" + _return[4] + "}"

label SetMenuVariables:
if MenuChoice == "HintsNone":
    call MenusHintsNone
elif MenuChoice == "HintsStatsAllGirls":
    call MenusHintsStatsAllGirls
elif MenuChoice == "HintsAllGirls":
    call MenusHintsAllGirls
elif MenuChoice == "HintsStatsCece":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsCece
elif MenuChoice == "HintsStatsLexi":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsLexi
elif MenuChoice == "HintsStatsLinda":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsLinda
elif MenuChoice == "HintsStatsKira":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsKira
elif MenuChoice == "HintsStatsRobin":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsRobin
elif MenuChoice == "HintsStatsStephanie":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsStephanie
elif MenuChoice == "HintsStatsKiraRobin":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsKiraRobin
elif MenuChoice == "HintsCece":
    call MenusHintsAllGirls
    call MenusHintsCece
elif MenuChoice == "HintsLexi":
    call MenusHintsAllGirls
    call MenusHintsLexi
elif MenuChoice == "HintsLinda":
    call MenusHintsAllGirls
    call MenusHintsLinda
elif MenuChoice == "HintsKira":
    call MenusHintsAllGirls
    call MenusHintsKira
elif MenuChoice == "HintsRobin":
    call MenusHintsAllGirls
    call MenusHintsRobin
elif MenuChoice == "HintsStephanie":
    call MenusHintsAllGirls
    call MenusHintsStephanie
elif MenuChoice == "HintsKiraRobin":
    call MenusHintsAllGirls
    call MenusHintsKiraRobin
else:
    call MenusHintsNone
jump MenusInitialized

label MenuRefresh:
if MenuChoice == "HintsNone":
    call MenusHintsNoneNoVar
elif MenuChoice == "HintsStatsAllGirls":
    call MenusHintsStatsAllGirls
elif MenuChoice == "HintsAllGirls":
    call MenusHintsAllGirls
elif MenuChoice == "HintsStatsCece":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsCece
elif MenuChoice == "HintsStatsLexi":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsLexi
elif MenuChoice == "HintsStatsLinda":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsLinda
elif MenuChoice == "HintsStatsKira":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsKira
elif MenuChoice == "HintsStatsRobin":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsRobin
elif MenuChoice == "HintsStatsStephanie":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsStephanie
elif MenuChoice == "HintsStatsKiraRobin":
    call MenusHintsStatsAllGirls
    call MenusHintsStatsKiraRobin
elif MenuChoice == "HintsCece":
    call MenusHintsAllGirls
    call MenusHintsCece
elif MenuChoice == "HintsLexi":
    call MenusHintsAllGirls
    call MenusHintsLexi
elif MenuChoice == "HintsLinda":
    call MenusHintsAllGirls
    call MenusHintsLinda
elif MenuChoice == "HintsKira":
    call MenusHintsAllGirls
    call MenusHintsKira
elif MenuChoice == "HintsRobin":
    call MenusHintsAllGirls
    call MenusHintsRobin
elif MenuChoice == "HintsStephanie":
    call MenusHintsAllGirls
    call MenusHintsStephanie
elif MenuChoice == "HintsKiraRobin":
    call MenusHintsAllGirls
    call MenusHintsKiraRobin
else:
    call MenusHintsNone
return

label MenusInitialized:

$ todayIs = 1
stop music fadeout 10
scene bg empty
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_title with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause()
scene bg empty with fade
"Dreams are weird."
"You can go a long time without dreaming of anything."
"Then suddenly, out of nowhere, you have the most vivid dream."
"And it doesn't even make sense, because it's a flash from the past."
"Someone you haven't thought about in a long time, and somehow they come back."
"Or maybe they never left at all."
$ name = renpy.input("What is your name? (leave blank for James)")
$ name = name.strip()
if name == "":
    $ name = "James"
scene ep1_steph_blur1 with fade
play music ep1_dream
$ nowPlayingArtist = "Jenny Penkin"
$ nowPlayingTitle = "Side Road - Instrumental Version"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
uk "[name]?"
me "Huh?"
scene bg empty with fade
me "That voice, so familiar."
scene ep1_steph_blur1 with fade
me "It can't be. She's gone."
me "But it has to be. I can even smell that perfume. The distinct smell of Rose and Jasmine."
scene ep1_steph_blink with Dissolve(2.5)
me "Steph?"
me "But what..."
scene ep1_steph_mlook_talk with dissolve
st "Long time no see..."
scene ep1_steph_mlook_listen with dissolve
me "Very long time."
me "What...Why are you here?"
scene ep1_steph_mlook_talk with dissolve
st "Why did you give up on me?"
scene ep1_steph_blink with dissolve
me "I never gave up on you."
me "You left me."
scene ep1_steph_mlook_talk with dissolve
st "You gave up on me."
scene ep1_steph_mlook_listen with dissolve
me "I have no idea what you're talking about."
me "We were having the time of our life."
me "Or so I thought."
me "Because, the next day you were gone."
scene ep1_steph_dlook_listen with dissolve
me "You disappeared without a trace..."
me "...without a word, or hint."
me "I searched everywhere."
scene ep1_steph_dlook_talk with dissolve
st "Then you gave up on me."
scene ep1_steph_blink with dissolve
me "What was I supposed to do?"
scene ep1_steph_mlook_talk with dissolve
st "It's not important..."
st "...this is your dream, we don't have to talk..."
scene ep1_steph_slook with dissolve
st "...when there's so many other things we can do."
$ renpy.music.set_pause(True, channel="music")
play sound doorbell
scene ep1_waking_up_sleeping
"*doorbell*"
"(...)"
scene ep1_steph_blur2 with dissolve
me "Nonono, please. Come back."
$ renpy.music.set_pause(False, channel="music")
scene ep1_steph_started1 with Dissolve(2, alpha=True)
me "(phew.)"
me "Oh, you started..."
me "..."
scene ep1_steph_started2 with dissolve
st "Don't mind me, I'm just getting warmed up."
st "So, you want to watch or join in?"
me "Not all the doorbells in the world could keep me away from you now."
me "(Wait, what? Doorbells?)"
stop music fadeout 0
play sound doorbell
scene ep1_waking_up_front
$ renpy.pause(1)
scene ep1_waking_up_awake with hpunch
me "(Dammit.)"
me "(Oh well, that dream is long gone now.)"
play sound doorbell
me "Yeyeye, hold your horses. I'm on my way."
play music ep1_intro
$ nowPlayingArtist = "Young Rich Pixies"
$ nowPlayingTitle = "A Good Mood"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep1_sleepydoor_a with fade
$ renpy.pause(0.5)
scene ep1_sleepydoor_b with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_sleepydoor_c with Dissolve(0.5, alpha=True)
uk "Hi there. [name]?"
scene ep1_courier_listen with dissolve
me "Yes, that's me?"
scene ep1_courier_speak1 with dissolve
carr "I have a package for you here. If you could just sign for it and show some ID, and I'll be on my way."
scene ep1_courier_listen with dissolve
me "(Must be my new phone)"
me "Of course, sure thing."
scene ep1_courier_speak2 with dissolve
carr "That's all I need. Have a nice day now."
scene ep1_courier_leave1 with dissolve
me "The package?"
scene ep1_courier_leave2 with dissolve
carr "By your feet."
carr "Good bye."
scene ep1_courier_done with dissolve
me "(I'll check out my phone after a quick shower. I'm reeking.)"
scene ep1_shower_side with fade
"(Ah, best way to start the day. Freshly showered.)"
"(But that dream. Why would I dream of Steph?)"
scene ep1_shower_behind with fade
"(I haven't seen her in...almost 2 years now?)"
"(Not since she disappeared. Or left without a trace that is.)"
scene ep1_shower_side with fade
"(I guess that's how dreams work anyway. And I shouldn't put too much into it.)"
"(But what I should do is try to get out more. I've been spending way too much time indoors lately.)"
scene ep1_shower_mirror with fade
"(On the positive side, I've gotten into pretty good shape.)"
"(No girlfriend means lots of time for training.)"
"(And for who I am as a person...)"
$ gen_notify = "Shape your personality:\n\nWhat you do ingame, shapes your personality. These will not shape your outcome, but add some flavor to the story. Or in some cases, add completely new scenes.\n\nThis first one is a freebie, later ones come as a result of your actions."
show screen general_notify
menu:
    "[M_01_001a]": # "Flirty (F)":
        hide screen general_notify
        $ meFlirty += 1
        show screen flvl with dissolve
        "(My quick comebacks are always charming.)"
        hide screen flvl with dissolve
        jump afterPersonality
    "[M_01_001b]": # "Romantic (R)":
        hide screen general_notify
        $ meRomantic += 1
        show screen rlvl with dissolve
        "(I know how to treat women, and they seem to appreciate that.)"
        hide screen rlvl with dissolve
        jump afterPersonality
    "[M_01_001c]": # "Athletic (S)":
        hide screen general_notify
        $ meSporty += 1
        show screen slvl with dissolve
        "(What's the reason for training for that body if you don't show or use it.)"
        hide screen slvl with dissolve
        jump afterPersonality
    "{color=#0f0}\[Mod\]{/color} All three": # "All three +1" if MenuChoice != "HintsNone":
        hide screen general_notify
        $ meFlirty += 1
        show screen flvl with dissolve
        "(My quick comebacks are always charming.)"
        hide screen flvl with dissolve
        $ meRomantic += 1
        show screen rlvl with dissolve
        "(I know how to treat women, and they seem to appreciate that.)"
        hide screen rlvl with dissolve
        $ meSporty += 1
        show screen slvl with dissolve
        "(What's the reason for training for that body if you don't show or use it.)"
        hide screen slvl with dissolve
        jump afterPersonality
label afterPersonality:
"(So there's really nothing holding me back, other than myself.)"
$ clockis = [[todayIs],1,2,4,7]
"(Anyway, I should check out the phone and set it up properly.)"
scene ep1_phone_tut_checking with fade
"Your phone logs your story as you progress. Characters and their infos are added automatically."
"If you want to, you can skip the phone tutorial."
menu:
    "[M_01_002a]": # "Skip the phone tutorial":
        jump skippedPhoneTutorial
    "[M_01_002b]": # "Let's do the phone tutorial":
        jump doPhoneTutorial
label doPhoneTutorial:

play sound phone_notify_sound
show screen phone_notify
$ phMusiOpen = True
$ phTaskOpen = True
$ phContOpen = True
$ phContNotify = True
$ contact_notify_me = True
$ contact_text_me += "\n\nMy new phone arrived. It is a bit empty right now, but I will add new contacts and photos as I meet new people."
$ contact_stephanie = True
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nI dreamt about her. No idea why. I haven't even thought about her in years."
"Sometimes it will notify you. You can click on the phone to access it."









hide screen phone_notify
show screen phone_tut
show screen phone
"Other times the phone is hidden but still available. Hover the mouse over the spot shown on the screen to see it, or click '{b}[custom_phone_key]{/b}' on your keyboard to toggle the phone screen. '{b}[custom_phone_key]{/b}' also works as back/exit while using the phone."
"As you might have noticed, the phone also shows the current time. Remember this when you have tasks or opportunities with a deadline."
hide screen phone_tut
"Sometimes you can use the camera for capturing those special moments."
hide screen phone
show screen phone_camop
$ phone_camop_screen = "ep1_photoop_tut"
"Those moments are shown by the phone popping up with this notification."
"Most times you can skip them, though some times you will have to take a photo to progress. Let's try it."
label phonecamreq_loop:
    "Click on the phone or press '{b}[custom_phone_key]{/b}'."
    jump phonecamreq_loop
label phonecamreq_a:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_photoop_tut_a"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_photoop_tut_a with Fade(0, 0, 0.5, color="#ffffff")
jump phonecamreq_done
label phonecamreq_b:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_photoop_tut_b"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_photoop_tut_b with Fade(0, 0, 0.5, color="#ffffff")
jump phonecamreq_done
label phonecamreq_c:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_photoop_tut_c"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_photoop_tut_c with Fade(0, 0, 0.5, color="#ffffff")
jump phonecamreq_done
label phonecamreq_done:
"A true masterpiece indeed."
"Every picture you take, or receive, is saved in the gallery on your phone."
"That concludes the tutorial. Enjoy the story."
jump afterPhoneTutorial

label skippedPhoneTutorial:
$ phMusiOpen = True
$ phTaskOpen = True
$ phContOpen = True
$ phContNotify = True
$ contact_notify_me = True
$ contact_text_me += "\n\nMy new phone arrived. It is a bit empty right now, but I will add new contacts and photos as I meet new people."
$ contact_stephanie = True
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nI dreamt about her. No idea why. I haven't even thought about her in years."
jump afterPhoneTutorial

label afterPhoneTutorial:
$ clockis = [[todayIs],1,2,5,9]
$ phCameOpen = True
$ phGallOpen = True
scene ep1_phone_tut_done with fade
show screen phone
me "(Well, enough goofing around, I'm hungry.)"

play sound call_sound
$ call_id = "caller_chris"
$ call_jump = "ep1_chris_call_home"
hide screen phone
show screen phone_call_notify

scene ep1_phone_tut_incomming with dissolve
"*phone ringing*"
"(I should answer it)"
label call_homecris_loop:
    play sound call_sound
    "*phone ringing* (Click on the phone or press '{b}[custom_phone_key]{/b}' to answer it)"
    jump call_homecris_loop
label ep1_chris_call_home:
scene ep1_chris_phone_speak with fade
show hello_chris_na at imgSlideIntroName
ch "Hey man. Finally got your phone, eh?"
hide hello_chris_na
scene ep1_phone_talk with dissolve
me "Hey Chris. As we speak actually. I just turned it on."
scene ep1_phone_listening with dissolve
ch "Well, I have some {b}very{/b} important news for you!"
scene ep1_phone_talk with dissolve
me "What?"
scene ep1_chris_phone_speak with dissolve
ch "This is big news ok?"
scene ep1_chris_phone_listen with dissolve
me "..."
me "...and?"
me "...hello?"
scene ep1_phone_tut_incomming with dissolve
$ renpy.pause()
scene ep1_phone_listening with dissolve
$ renpy.pause(1)
scene ep1_chris_phone_speak with dissolve
ch "I'm waiting for you to guess..."
scene ep1_phone_talk with dissolve
me "Will you spill it already?"
scene ep1_phone_listening with dissolve
ch "That new place, Metronome, is having a pre-opening tomorrow."
scene ep1_phone_talk with dissolve
me "I know, but there is no way we can get tickets to..."
scene ep1_chris_phone_talk_happy with dissolve
ch "And I got us two tickets!"
scene ep1_phone_talk with dissolve
me "Really? Are you sure it's actual tickets and not some fake black market shit?"
scene ep1_chris_phone_speak with dissolve
ch "You know me, I always get the best stuff."
scene ep1_chris_phone_listen with dissolve
me "Well, yes. That's why I'm making sure."
scene ep1_chris_phone_talk_happy with dissolve
ch "Haha. Don't worry. We were doing some electrical installation there and they gave my boss some tickets."
ch "I had to work the graveyard shift though, but it's so worth it."
scene ep1_chris_phone_listen with dissolve
me "Wow. I'm impressed!"
scene ep1_chris_phone_speak with dissolve
ch "So you want to be my date for the evening?"
$ ep1_acceptedMetronome = False
scene ep1_phone_talk with dissolve
menu:
    "[M_01_003a]": # "I'm in!":
        $ ep1_acceptedMetronome = True
        $ XPchris += 20
        me "I'm in."
        me "If you stop referring to it as a date, that is."
        scene ep1_chris_phone_speak with dissolve
        ch "Sure thing, honey."
    "[M_01_003b]": # "Not sure.":
        $ XPchris += 17
        me "I'm not sure. Don't really feel like it."
        scene ep1_chris_phone_speak with dissolve
        ch "Bro. It won't be the same without you. And when was the last time we did something like this?"
        ch "Pre-Opening!"
        scene ep1_chris_phone_listen with dissolve
        me "I'll think about it."
        scene ep1_chris_phone_speak with dissolve
        ch "You'd better be thinking about all the chicks you will miss out on."
ch "By the way, I'm about to stuff my face. I could eat a horse right now. You want to join in?"
scene ep1_phone_talk with dissolve
me "Sure. I was just about to raid the fridge anyway."
me "Eating out sounds better though. The usual spot?"
scene ep1_chris_phone_speak with dissolve
ch "Let's try the new MaKenzie instead. You know where, right?"
scene ep1_phone_talk with dissolve
me "Sure, see you there in a few."
stop music fadeout 3
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ phContNotify = True
$ contact_chris = True
$ contact_notify_chris = True
$ contact_text_chris += "\n\nHe got tickets for us to the pre-opening of Metronome."
$ clockis = [[todayIs],1,3,3,9]
play music ep1_burger
$ nowPlayingArtist = "Ian Post"
$ nowPlayingTitle = "DuDa"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
show screen phone
scene ep1_meet_chris with fade
me "(There he is)"
scene ep1_meet_chris2 with dissolve
me "Hey man."
scene ep1_chris_hairstare_up with dissolve
ch "Bro."
ch "Your hair."
me "Nice eh?"
me "I went to the hairdresser and asked her to do something trendy."
scene ep1_chris_hairstare_down with dissolve
ch "It's gray."
scene ep1_chris_hairstare_up with dissolve
me "...silver..."
scene ep1_chris_hairstare_both with dissolve
ch "I can't stop staring at it now."
scene ep1_chris_hairstare_up with dissolve
me "..."
scene ep1_chris_hairstare_down with dissolve
ch "You are taking the whole fifty shades of gray thing to a completely new level."
scene ep1_chris_hairstare_up with dissolve
ch "Chris and his trusty companion, the gray fox..."
scene ep1_chris_hairstare_down with dissolve
ch "It's a gray zone."
scene ep1_spot_kira_unclear with dissolve
me "*laughs* Are you done yet?"
me "Just...order me a regular meal, will you?"
ch "Hey waiter, there's a gray hair in my soup."
ch "There's some good food in here, though."
me "You mean cheap food."
scene ep1_spot_kira_clear with dissolve
ch "Yeah, that too."
ch "One regular for you, and a triple deluxe for me."



show hello_kira_bg at imgSlide_bg
show hello_kira_sp at imgSlide_sp
show hello_kira at imgSlide
if intro_showname:
    show hello_kira_na at imgSlide_na
$ renpy.pause()
ch "[name]?"
scene ep1_stare_kira with hpunch
hide hello_kira_bg
hide hello_kira_sp
hide hello_kira
hide hello_kira_na
ch "[name]!"
me "Sorry, got lost in that hot chick on my 12."
me "Don't look."
scene ep1_chris_look_blur with dissolve
ch "Your eagle eye is spot on, my friend."
scene ep1_chris_look_caught with dissolve
ch "Good catch."
me "..."
me "That's not what {b}don't look{/b} means."
scene ep1_chris_afterstare_blur with dissolve
ch "Why would I not look?"
scene ep1_spot_kira_noticed with dissolve
me "She's very nice though."
ch "There, food's ordered."
me "How much?"
ch "Nah, food's on me. Let's go find a place while we wait for it."
$ clockis = [[todayIs],1,3,4,7]
scene ep1_burg_chris_talk1 with fade
ch "Why don't you have a chat with her."
scene ep1_burg_chris_blink with dissolve
me "That girl back there? Nah, this isn't the time or the place."
me "And my confidence is at an all time low at the moment."
me "Since Steph, it's been kinda downhill for me."
scene ep1_burg_chris_talk2 with dissolve
ch "Yeah, look... I'm going to be honest with you man."
scene ep1_burg_chris_talk1 with dissolve
ch "You know it's been several years since Steph. And I'm saying this with all the best intentions bro."
ch "You got to move on."
scene ep1_burg_chris_blink with dissolve
me "I have..."
scene ep1_burg_chris_talk4 with dissolve
ch "And how many girls have you been with since Steph?"
scene ep1_burg_chris_blink with dissolve
me "...none."
scene ep1_burg_chris_talk4 with dissolve
ch "Thank you for proving my point."
ch "Anyway, how long were you with her? 3 years?"
scene ep1_burg_chris_blink with dissolve
me "2 years, 10 months and 3 days."
scene ep1_burg_chris_talk3 with dissolve
ch "Really, dude? You know the exact number of days..."
me "Yeah, I know. I don't forget these things so easily."
scene ep1_burg_chris_talk4 with dissolve
ch "Deep down inside you are waiting for her, you know? There's this part of you that hopes that some day you'll meet her somewhere completely random."
ch "Then you will look into each others eyes, the world will melt away, and it will go back to the way things were."
scene ep1_burg_chris_talk1 with dissolve
ch "But I'm telling you, that is not going to happen. Even if it does, it won't right the past."
ch "And right now, it's really cramping your style."
scene ep1_burg_chris_blink with dissolve
me "You are brutally honest by the way."
scene ep1_burg_chris_talk4 with dissolve
ch "That's how you tell good friends from bad ones."
scene ep1_burg_chris_blink with dissolve
me "I appreciate it. I really do. But for now, let's just have a nice meal."
scene ep1_burg_chris_talk1 with dissolve
ch "As I see it, you have a golden opportunity here."
scene ep1_burg_chris_point_kira with dissolve
ch "...that girl you were ogling just now."
scene ep1_burg_chris_blink with dissolve
me "The burger chick..."
scene ep1_burg_chris_talk2 with dissolve
ch "Exactly. I'll help you catch up on your women-skills. Loosen you up a bit."
me "Chris..."
scene ep1_burg_chris_talk4 with dissolve
ch "But you deserve some fun bro. You're single, handsome and fun. Live a little."
ch "You know, let me help you a bit. And I'm not taking no for an answer."
scene ep1_burg_chris_blink with dissolve
me "Naaah, I'm fine. Let's just..."
me "This is not a good moment for me to get feelings for anybody."
me "Who knows if she's got an angry boyfriend somewhere."
me "And lastly, you and the words women-skills do not belong in the same sentence."
scene ep1_burg_chris_talk5 with dissolve
ch "You lost me at Naaah."
scene ep1_burg_chris_point_kira with dissolve
ch "But seriously, there's a hot chick right over there."
ch "I'm not talking about feelings, or sex or whatever. Just get out of that cave and enjoy yourself."
ch "Meet new people. Open up a little. Have some fun you know."
scene ep1_burg_chris_blink with dissolve
me "I'll pass."
scene ep1_burg_chris_talk5 with dissolve
ch "That sounds like a yes to me."
ch "Don't worry, Chris' got your back."
ch "You can thank me later."
scene ep1_chris_leave_table with dissolve
ch "Excuse me, miss?"
scene ep1_chris_left_table with dissolve
me "(What is he doing?)"
scene ep1_chris_kira_talk with fade
me "(Oh no...)"
scene ep1_chris_kira_looktalk with dissolve
me "(Really, Chris?)"
scene ep1_chris_kira_look with Dissolve(0.1, alpha=True)
$ renpy.pause()
scene ep1_kira_walking_over with dissolve
$ renpy.pause()
scene ep1_kira_talk_welcome with fade
uk "So?..."
scene ep1_burg_kira_listen_blink with dissolve
menu:
    "[M_01_004a]": # "Explain to her that Chris is an idiot":
        $ kiraMeetConvOpt = 1
        $ XPkira += 8
        me "I'm sorry miss. My friend isn't quite right in the head."
        me "He tried to set me up with you."
        scene ep1_burg_kira_question with dissolve
        uk "Did he now. And you didn't want him to?"
        scene ep1_burg_kira_listen_blink with dissolve
        me "..."
        me "Aren't you supposed to say, that is totally a creepy thing to do."
        scene ep1_burg_kira_question with dissolve
        uk "...it's tempting."
        scene ep1_burg_kira_listen_blink with dissolve
        me "I am going to admit that you look very nice, but I'd still say the setting is kinda awkward."
        me "...and me not knowing if you are single or not..."
        me "...and to be honest I'm not really that confident..."
        me "...and this is where you work and stuff."
        scene ep1_kira_check with dissolve
        uk "..."
        me "I'm talking way too much, aren't I."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "*laughs* Some people think that's a cute trait."
        scene ep1_burg_kira_listen_blink with dissolve
        me "So, are you saying that I'm only going to attract weirdos?"
        scene ep1_burg_kira_question with dissolve
        uk "Are you saying that I'm a weirdo?"
        scene ep1_burg_kira_annoyed with dissolve
        me "No... I... just painted myself into a corner now, didn't I."
        scene ep1_kira_talk_welcome3 with dissolve
        uk "And I'm pulling your leg."
        scene ep1_kira_check_a with dissolve
        me "I'm [name]."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "Thank you for the compliment, [name]."
        scene ep1_burg_kira_listen_blink with dissolve
        me "And you?..."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "...need to get back to work now."
        scene ep1_burg_kira_aftertalk with dissolve
        uk "Enjoy the view then, [name]."
        scene ep1_burg_kira_walkingback with dissolve
        me "(Wait, I'm confused.)"
        me "(Did that go well, or not.)"
        jump afterTalkWithKira
    "[M_01_004b]": # "Try charming her":
        $ kiraMeetConvOpt = 2
        $ XPkira += 5
        $ XPchris += 1
        me "I haven't seen you around here before."
        scene ep1_burg_kira_annoyed with dissolve
        uk "Really, you wanted me to come to your table to tell me that."
        scene ep1_burg_kira_listen_blink with dissolve
        me "I can't help it miss, you are truly beautiful."
        uk "(Oh well, the customer is always right)"
        scene ep1_burg_kira_question with dissolve
        uk "Thank you very much for the compliment."
        uk "But if everything is in order, I have to get back to work now."
        scene ep1_burg_kira_listen_blink with dissolve
        me "I didn't catch your name."
        scene ep1_kira_check_b with dissolve
        uk "I didn't give it."
        scene ep1_kira_check_a with dissolve
        me "I'm [name]."
        scene ep1_burg_kira_aftertalk with dissolve
        uk "Enjoy your meal, [name]."
        scene ep1_burg_kira_walkingback with dissolve
        me "(That could have gone better)"
        jump afterTalkWithKira
    "[M_01_004c]" if meFlirty >= 1: # "Excuse Chris' joke and compliment her (F)" if meFlirty >= 1:
        $ kiraMeetConvOpt = 3
        $ XPkira += 10
        $ XPchris += 1
        $ gotKiraName = True
        show screen fshw with dissolve
        me "I'm sorry miss. I believe you've been caught up in my friends mischief, just as I have."
        me "He is trying to set me up with you."
        hide screen fshw with dissolve
        scene ep1_kira_talk_welcome3 with dissolve
        uk "Interesting."
        scene ep1_kira_check with dissolve
        me "He is right on one account though. You look stunning."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "*laughs* This is the most common burgershop in the world which happen to be the place that I work."
        uk "I'm probably smelling like greasy fries and burgers, wearing industrially matched clothing that ensures to remove any individualism I might have."
        uk "And you still find me fascinating?"
        scene ep1_kira_check with dissolve
        me "It's not about the clothes or place. It's how you light up your surroundings by just being here."
        scene ep1_kira_talk_welcome3 with dissolve
        uk "Flattering complete strangers is walking a thin line between cute and creepy though."
        scene ep1_kira_check with dissolve
        me "I meant no offence at all, miss."
        scene ep1_kira_check_b with dissolve
        me "I just wanted you to know that you put a smile on my face, and hopefully by me saying so, will put a smile on yours aswell."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "I'll give you the benefit of the doubt though, and say you're not a creep."
        uk "Thank you for your nice words. And you're not so bad yourself either."
        uk "Although, I'll have to get back to the counter now."
        scene ep1_kira_check with dissolve
        me "No problem, and can you just slap my friend Chris on the way there? Just tell him it's from [name]."
        scene ep1_kira_talk_welcome2 with dissolve
        uk "Tempting, [name]. Real tempting. But I need this job. *laughs*"
        show hello_kira_na at imgSlideIntroName
        ki "And the name's Kira by the way."
        hide hello_kira_na
        me "Nice to meet you, Kira."
        scene ep1_burg_kira_aftertalk with dissolve
        ki "Tada."
        scene ep1_burg_kira_walkingback with dissolve
        me "(That went ok, I guess)"
        me "(But Chris is right, maybe I should play my flirty side a bit more.)"
        me "(It's a part of my personality after all.)"
        jump afterTalkWithKira
label afterTalkWithKira:
scene ep1_burg_chris_back with fade
$ clockis = [[todayIs],1,3,5,2]
ch "So..."
ch "...how did it go."
scene ep1_burg_chris_blink with dissolve
if kiraMeetConvOpt == 2:
    me "Not too good I think. I cramped up."
    me "Told you I'm out of practice."
    scene ep1_burg_chris_chatsmile2 with dissolve
    ch "If it's any comfort, I got a kick out of it."
    me "Yeah, that's very comforting."
else:
    me "To be honest? I have no idea."
    me "It's hard to get a read on her. But I guess it went as good as it can go, considering the circumstances."
    scene ep1_burg_chris_talk2 with dissolve
    ch "Well, she didn't slap you."
    me "Ye, and there's that."
scene ep1_burg_chris_blink with dissolve
me "But I guess the real question is..."
me "What on earth did you say to her?"
scene ep1_burg_chris_chatsmile with dissolve
ch "Now wouldn't you like to know."
scene ep1_burg_chris_blink with dissolve
me "You aren't going to tell me, are you?"
scene ep1_burg_chris_talk5 with dissolve
ch "Nope."
scene ep1_burg_chris_chatsmile with dissolve
if gotKiraName == True:
    me "Anyway, her name is Kira, and she seems really nice."
    me "But she didn't give me any means of contacting her though."
else:
    me "Anyway, she seems really nice, but she didn't want to give me her name it seems."
    me "Or any other means on how to contact her."
scene ep1_burg_chris_temp with dissolve
ch "Don't worry, you know where she works."
scene ep1_burg_chris_point_kira with dissolve
ch "Or I could just head over to her again and..."
me "No... Just no. I'll fucking handcuff you to the table."
scene ep1_burg_chris_chatsmile with dissolve
ch "Kinky."
me "*laughs* Yeah, I knew that would get your juices flowing."
scene bg empty with fade
$ renpy.pause(0.5)
scene ep1_burg_chris_talk4 with fade
$ clockis = [[todayIs],1,4,3,9]
ch "I'm so full, I'm starting to feel a bit cheesy."
scene ep1_burg_chris_blink with dissolve
me "No wonder. You went for the triple deluxe."
scene ep1_burg_chris_talk2 with dissolve
ch "If it fills you up, it's good in my book."
scene ep1_burg_chris_lookkira with Dissolve(1, alpha=True)
ch "Hmmm..."
ch "Are you an ass-man, or breast man?"
me "Seriously?"
scene ep1_burg_chris_talk1 with dissolve
ch "I've got to know your M.O."
ch "This is a pivotal moment, so I know what we have to work with here."
me "..."
ch "Just humor me."
ch "So, are you an ass-man, or breast man?"
$ abNTsignal = 0
label chooseAssesOrBreasts:
$ abPersName = "Personality"
$ abNotTelling = "Not telling you that"
call MenuRefresh
if AssesOrBreasts == 3:
    $ abPersName = "I think it's pointless to repeat Personality"
if abNTsignal == 1:
    $ abNotTelling = "I'm still not telling you that, Chris"
    call MenuRefresh
scene ep1_burg_chris_blink with dissolve
menu:
    "[M_01_005a]": # "I prefer asses":
        $ XPchris += 1
        $ AssesOrBreasts = 1
        me "I'd choose asses over breasts."
    "[M_01_005b]": # "I prefer breasts":
        $ XPchris += 1
        $ AssesOrBreasts = 2
        me "Can't go wrong with breasts."
        jump afterAssesOrBreasts
    "[M_01_005c]" if AssesOrBreasts != 3: # "[abPersName]" if AssesOrBreasts != 3:
        $ AssesOrBreasts = 3
        me "I prefer their personality."
        scene ep1_burg_chris_talk1 with dissolve
        ch "Of course. But this is a conversation between men. So, Asses or Breasts?"
        jump chooseAssesOrBreasts
    "[M_01_005d]": # "[abNotTelling]":
        if abNTsignal == 1:
            $ XPchris -= 1
            $ AssesOrBreasts = 1
            me "Nope. I'm still not telling you that. It's personal."
            scene ep1_burg_chris_talk1 with dissolve
            ch "Doesn't matter."
            ch "...I've seen the way you stare at women's asses."
            jump afterAssesOrBreasts
        else:
            $ XPchris -= 1
            me "Nope. Not telling you that."
            scene ep1_burg_chris_talk1 with dissolve
            ch "Look, we're bros. I'm not asking just to joke around. I've got good intentions. You trust me, right?"
            ch "...{b}right{/b}?"
            $ abNTsignal = 1
            jump chooseAssesOrBreasts
label afterAssesOrBreasts:
scene ep1_burg_chris_chatsmile3 with dissolve
ch "Got it."
if not ep1_acceptedMetronome:
    scene ep1_burg_chris_talk1 with dissolve
    ch "Before I forget. You are coming along to Metronome tomorrow, right?"
    scene ep1_burg_chris_blink with dissolve
    me "I have a feeling I don't have much choice."
    scene ep1_burg_chris_talk1 with dissolve
    ch "Don't be that guy man. It's going to be fun. And you know it!"
    scene ep1_burg_chris_temp with dissolve
    me "Ok, sure. I'm in."
    scene ep1_burg_chris_chatsmile with dissolve
    ch "Fuck yeah!"
else:
    scene ep1_burg_chris_blink with dissolve
    me "I'm looking forward to Metronome tomorrow."
    scene ep1_burg_chris_chatsmile with dissolve
    ch "Fuck yeah. It's going to be the event of the century."
scene ep1_burg_chris_talk1 with dissolve
ch "Oh, and can you hold on to the tickets?"
ch "You know me... I'll probably lose them."
me "Sure thing."
scene ep1_burg_chris_talk2 with dissolve
ch "But anyway, I need to hit the can."
scene ep1_burg_chris_blink with dissolve
me "Yeah, I'd better get going too. But why don't you drop by my place tomorrow before we go for some starter-beers?"
scene ep1_burg_chris_talk1 with dissolve
ch "Sure. Around 8?"
scene ep1_burg_chris_blink with dissolve
$ phone_task_append_item1 = "1;2;2;0;0;0;Chris;Be home at;Chris is coming over.;1"
$ phone_task_append_item2 = "1;2;2;0;0;0;Chris;Be home at;Chris is coming over.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True





me "Works for me. Later."
scene ep1_burg_chris_talk5 with dissolve
ch "Laters"
$ phone_taskadd = "New task\nChris is coming over tomorrow at 20:00."
show screen phone_taskadded
$ renpy.pause()
hide screen phone_taskadded
$ clockis = [[todayIs],1,5,0,1]
if gotKiraName:
    scene bg empty with fade
    ki "Leaving?"
    scene ep1_burg_kira_counter_blink with fade
    me "Hey, Kira."
    me "As much as I'd like to stay here with you for the rest of the day, I really should get going."
    scene ep1_burg_kira_counter_talk with dissolve
    ki "Things to do, places to see?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "It's more about the smell of burgers and fries getting overwhelming after a while."
    scene ep1_burg_kira_counter_talk with dissolve
    ki "Don't remind me. I still got a few hours of work left."
    scene ep1_burg_kira_counter_blink with dissolve
    me "Hey, at least you've got FapFrappys. They are the highlight of your menu."
    scene ep1_burg_kira_counter_talk with dissolve
    ki "And still you didn't order one?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "Cute face {b}and{/b} observant!"
    scene ep1_burg_kira_counter_talk with dissolve
    ki "*laughs* You got a soft spot for sweet stuff, eh?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "It's a male thing I guess."
    scene ep1_burg_kira_counter_givecoffee1 with dissolve
    ki "Hang on a second."
    ki "A little present for you."
    scene ep1_burg_kira_counter_givecoffee2 with dissolve
    ki "One FapFrappy on me, for the road."
    scene ep1_burg_kira_counter_blink with dissolve
    me "Thank you very much."
else:
    scene bg empty with fade
    uk "Leaving already?"
    scene ep1_burg_kira_counter_blink with fade
    me "Hey, you."
    me "As much as I'd like to stay here with you for the rest of the day, I really should get going."
    scene ep1_burg_kira_counter_talk with dissolve
    uk "Things to do, places to see?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "It's more about the smell of burgers and fries getting overwhelming after a while."
    scene ep1_burg_kira_counter_talk with dissolve
    uk "Don't remind me. I still got a few hours of work left."
    scene ep1_burg_kira_counter_blink with dissolve
    me "Hey, at least you've got FapFrappys. They are the highlight of your menu."
    scene ep1_burg_kira_counter_talk with dissolve
    uk "And still you didn't order one?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "Cute face {b}and{/b} observant!"
    scene ep1_burg_kira_counter_talk with dissolve
    uk "*laughs* You got a soft spot for sweet stuff, eh?"
    scene ep1_burg_kira_counter_blink with dissolve
    me "It's a male thing I guess."
    scene ep1_burg_kira_counter_givecoffee1 with dissolve
    uk "Hang on a second."
    uk "A little present for you."
    scene ep1_burg_kira_counter_givecoffee2 with dissolve
    uk "One FapFrappy on me, for the road."
    scene ep1_burg_kira_counter_blink with dissolve
    me "Thank you very much. That's so kind of you, eh..."
    scene ep1_burg_kira_counter_talk with dissolve
    show hello_kira_na at imgSlideIntroName
    ki "It's Kira."
    hide hello_kira_na
    scene ep1_burg_kira_counter_blink with dissolve
    me "Thank you Kira."
$ contact_notify_chris = True
$ contact_text_chris += "\n\nChris tried setting me up with this girl, Kira, at the burgershop."
scene ep1_burg_kira_counter_talk with dissolve
stop music fadeout 5
ki "Stay in touch, will you?"
scene ep1_burg_kira_counter_blink with dissolve
me "Of course."
scene ep1_me_walking1 with fade
$ clockis = [[todayIs],1,5,3,4]
play music ep1_afterburger
$ nowPlayingArtist = "Folk Love"
$ nowPlayingTitle = "Campagna"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "(Hmmm.)"
me "(I should have tried talking a bit more with her.)"
me "(She didn't seem to be bothered by me hitting on her at least.)"
me "(Or it might have been that she really wanted to slap me.)"
scene ep1_me_walking_cup1 with dissolve
me "(Why would she give me a freebie then.)"
me "(...unless she is just very friendly of course.)"
me "(I'm overthinking things as usual.)"
play sound phone_notify_sound
show screen phone_notify_chat
$ phChatCanReplyChris = True
$ phChatOpen = True
$ phChatNotify = True
$ chat_chris_item = "1;0;1;Hey man. You there?"
if chat_chris_item not in chat_chris:
    $ chat_chris.append(chat_chris_item)
$ phone_task_append_item1 = "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;1"
$ phone_task_append_item2 = "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
        $ chat_notify_chris = True

$ renpy.pause()
hide screen phone_notify_chat
me "(Time to lift the head and smile a bit more.)"
scene ep1_me_walking2 with dissolve
me "Afternoon, ladies."
scene ep1_me_walking3 with dissolve
uk "Afternoon yourself."
scene ep1_me_walking_cup2 with dissolve
me "(I'm really looking forward to Metronome now.)"
me "(And with Chris by my side, it's bound to get interesting.)"
me "(Wait, what's this?)"
scene ep1_me_walking_cup3 with dissolve
me "(Is that?)"
$ contact_kira = True
$ chat_bowling_required = True
$ chat_kira_item = "2;0;101;New contact added"
if chat_kira_item not in chat_kira:
    $ chat_kira.append(chat_kira_item)

$ phone_task_append_item1 = "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;1"
$ phone_task_append_item2 = "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
        $ phContNotify = True
        $ contact_notify_kira = True

$ contact_text_kira += "\n\nShe left me her number on a FapFrappy cup. I should send her a message."
$ chat_stephanie_item = "2;0;201;Unable to show older messages"
if chat_stephanie_item not in chat_stephanie:
    $ chat_stephanie.append(chat_stephanie_item)

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "You can {b}Chat{/b} with Stephanie on your phone now.\nYou can {b}Chat{/b} with Kira on your phone now."
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################

me "*laughs* (That was a nice surprise. Must be Kira.)"
$ phone_taskadd = "New task\nGet in touch with Kira."
show screen phone_taskadded
me "(Maybe I should send her a message.)"
hide screen phone_taskadded
scene ep1_me_walking1 with dissolve
me "(...or I could go back for another FapFrappy)"
me "(Nah...)"

if MenuChoice != "HintsNone":
    ### Hide Hint ########################################################################################################################################
    hide screen general_notifytop with dissolve
    ### Hide Hint ########################################################################################################################################

scene ep1_home_mid_arrive with fade
$ clockis = [[todayIs],1,6,4,7]
me "(Home sweet home.)"
me "(It's not much, but I like it. Small and cosy. And it's all mine.)"
me "(Bought it about a year ago. It was a real shithole.)"
me "(But after a few months of hard interior work, it was like brand new again.)"
scene ep1_home_mid_sofa2 with dissolve
me "(Though, I should buy myself a new couch. This is so bad, it's tragic.)"
scene ep1_home_mid_sofa1 with dissolve
$ renpy.choice_for_skipping()
me "(I should check out my phone)"
me "(Or maybe...time for a little nap. I'm drowsing here.)"
me "(Maybe...will...dream...again...zzz)"
$ eveningStrollMusic = False
scene bg empty with fade

$ phone_reminder = False
$ phone_task_check_item = "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;2"
if phone_task_check_item not in phone_task_list:
    $ phone_reminder = True
$ phone_reminder = False
$ phone_task_check_item = "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;2"
if phone_task_check_item not in phone_task_list:
    $ phone_reminder = True
if phone_reminder:
    "{i}{size=22}{color=#ffff77}While almost falling asleep, you think to yourself that you should check your tasks on your phone. Who knows what opportunities you might miss out on if you forget a task...{/color}{/size}{/i}"
    $ phone_reminder = False

if chat_bowling_required:
    menu:
        "[M_01_006a]": # "Reply to Kira's message (Required)":
            $ chat_bowling_required = False
            $ chat_notify_kira = False
            $ chat_sel_name = "Kira"
            $ chat_sel_icon = "cont_kira"
            call screen phone_chat_single

$ renpy.pause()
scene ep1_home_mid_sofa1 with fade
$ clockis = [[todayIs],2,0,1,5]
$ phone_task_append_item1 = "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;1"
$ phone_task_append_item2 = "1;1;2;0;0;0;Chris;Reply to Chris before;Chris has sent me a message.;0"
if phone_task_append_item1 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
$ phone_task_append_item1 = "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;1"
$ phone_task_append_item2 = "2;1;2;0;0;0;Kira;Message Kira before;Get in touch with Kira;0"
if phone_task_append_item1 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if d1_responded_kira == "1":
    play sound phone_notify_sound
    show screen phone_notify_chat
    $ chat_kira_item = "1;0;301;So... mr. Secret admirer. You busy?"
    if chat_kira_item not in chat_kira:
        $ chat_kira.append(chat_kira_item)
        $ phChatNotify = True
        $ chat_notify_kira = True
    $ phone_task_append_item1 = "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;1"
    $ phone_task_append_item2 = "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;2"
    if phone_task_append_item1 not in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.append(phone_task_append_item1)
            $ phTaskNotify = True
    jump afterKiraIncMessage
elif d1_responded_kira == "2":
    play sound phone_notify_sound
    show screen phone_notify_chat
    $ chat_kira_item = "1;0;302;Well, you try writing secretly in front of a guy you've just met, who's staring at your ass."
    if chat_kira_item not in chat_kira:
        $ chat_kira.append(chat_kira_item)
        $ chat_notify_kira = True
    $ phone_task_append_item1 = "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;1"
    $ phone_task_append_item2 = "3;1;2;0;1;5;Kira;Answer Kira before;Get to know Kira;2"
    if phone_task_append_item1 not in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.append(phone_task_append_item1)
            $ phTaskNotify = True
    jump afterKiraIncMessage
else:
    jump beforeEveningStroll
label afterKiraIncMessage:
me "(Message...again.)"
me "(Wow, I've slept for 2 hours.)"
me "(And my neck informs me, that was not a good idea. Ouch.)"
menu:
    "[M_01_007a]": # "Check the message":
        $ chat_notify_kira = False
        $ chat_sel_name = "Kira"
        $ chat_sel_icon = "cont_kira"
        call screen phone_chat_single




label goingOutWithKira:
scene ep1_home_mid_sofa1 with dissolve
me "(Well, that was a lovely surprise. Seems I got plans for tonight then.)"
me "(But 30 minutes. I should really get going.)"
scene ep1_bowling_intro0 with fade
$ clockis = [[todayIs],2,0,5,5]
$ wentBowlingKira = True
me "(Hopefully this is right. Big red door at the top of the Plaza.)"
scene ep1_bowling_intro1 with dissolve
me "(There she is.)"
me "(And with her friend it seems.)"
show hello_robin_bg at imgSlide_rob_bg
show hello_robin at imgSlide_rob
show hello_robin_sp at imgSlide_rob_sp
show hello_robin_na at imgSlide_rob_na
$ renpy.pause()
hide hello_robin_na
hide hello_robin_sp
hide hello_robin_bg
hide hello_robin
scene ep1_bowling_intro2 with dissolve
me "Hi there, Kira."
scene ep1_bowling_meet0 with dissolve
ki "Mr. Frappy."
menu:
    "[M_01_008a]": # "Greet with handshake":
        scene ep1_bowling_handshake with dissolve
        $ renpy.pause()
        jump afterKiraBowlingGreeting
    "[M_01_008b]": # "Give her a hug":
        $ XPkira += 2
        scene ep1_bowling_greet3 with dissolve
        $ renpy.pause(0.5)
        scene ep1_bowling_greet with Dissolve(0.5, alpha=True)
        $ renpy.pause(0.5)
        scene ep1_bowling_greet3 with Dissolve(0.5, alpha=True)
        $ renpy.pause(0.5)
        scene ep1_bowling_meet1 with Dissolve(1, alpha=True)
        jump afterKiraBowlingGreeting
    "[M_01_008c]": # "Give her a kiss on the cheek":
        $ XPkira += 1
        scene ep1_bowling_greet3 with dissolve
        $ renpy.pause(0.5)
        scene ep1_bowling_greet2 with Dissolve(0.5, alpha=True)
        $ renpy.pause(0.5)
        scene ep1_bowling_greet3 with Dissolve(0.5, alpha=True)
        $ renpy.pause(0.5)
        scene ep1_bowling_meet1 with Dissolve(1, alpha=True)
        ki "Well, aren't you a courageous one."
        jump afterKiraBowlingGreeting
label afterKiraBowlingGreeting:
ki "Glad you could join me."
scene ep1_bowling_meet2 with dissolve
ki "This hottie is Robin, the backbone of my life. Robin, meet [name]."
ki "[name] here gave me points for a charming personality at work today."
$ phContNotify = True
$ contact_robin = True
$ contact_notify_robin = True
$ chat_robin_item = "2;0;401;New contact added"
if chat_robin_item not in chat_robin:
    $ chat_robin.append(chat_robin_item)
menu:
    "[M_01_009a]": # "Take a quick sneak at Kira's boobs":
        $ ep1LookedKiraBoobs = True
        $ XPkira += 2
        $ XProbin += 1
        scene ep1_kira_closeb with dissolve
        $ renpy.pause()
        ro "*laughs* I believe [name] here just gave you two more points, and neither of those were for your charming personality."
        scene ep1_bowling_boobgreet1 with dissolve
        ki "Oh."
        scene ep1_bowling_boobgreet2 with dissolve
        ki "You mean these puppies?"
        ki "I think they are worth more than two points though."
        me "Who doesn't like puppies?"
        me "If I got to know them better, I'm sure we would become breast friends."
        scene ep1_bowling_boobgreet3 with dissolve
        ki "..."
        me "I rate them a decent 10..."
        me "...each..."
        me "...making them a big part of you i-ten-titties."
        ro "*laughs* That's so bad..."
        scene ep1_bowling_boobgreet1 with dissolve
        ki "Go hug Robin, before she has a seizure."
        jump robinGreeting
    "[M_01_009b]": # "Say Hi to Robin":
        jump robinGreeting
label robinGreeting:
scene ep1_bowling_robin1 with dissolve
me "Nice to meet you Robin."
scene ep1_bowling_rhug2 with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_rhug3 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep1_bowling_rhug2 with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_robin1 with dissolve
me "Pleasure is all mine, [name]."
scene ep1_bowling_krm_kt with dissolve
ki "So, I invited him for an evening of bowling."
scene ep1_bowling_krm_rt with dissolve
ro "Sure thing, knock yourselves out."
ro "The points system is offline though, so you'll have to play for fun or keep tabs manually."
scene ep1_bowling_krm1 with dissolve
me "Thank heavens for that."
scene ep1_bowling_krm2 with dissolve
ki "Bowling not for you?"
scene ep1_bowling_krm1 with dissolve
me "Who knows, I've actually never tried it before."
scene ep1_bowling_krm2 with dissolve
ki "Don't worry about it. We'll just do a few rounds just for the fun of it."
scene ep1_bowling_krm1 with dissolve
me "I have to give you credit though. This place is awesome."
scene ep1_bowling_krm3 with dissolve
ro "I've put a lot of money and work into it, and now it's finally down to the home stretch."
ro "We're opening in two days. So feel free to drop by."
scene ep1_bowling_krm1 with dissolve
$ phone_task_append_item1 = "5;3;2;0;0;0;Robin;Attend opening;Plaza Bowling is opening.;1"
$ phone_task_append_item2 = "5;3;2;0;0;0;Robin;Attend opening;Plaza Bowling is opening.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_taskadd = "New task\nPlaza Bowling opens in 2 days at 20:00."
show screen phone_taskadded
me "Don't mind if I do. As long as Kira here can teach me the moves today, I won't look like a complete fool then."
hide screen phone_taskadded
scene ep1_bowling_krm2 with dissolve
ki "No sweat. You'll be a bowling pro in no time with me in your corner."
ki "And we won't play for points anyway."
if ep1LookedKiraBoobs:
    scene ep1_bowling_krm1 with dissolve
    me "Well, I already gave you like 20 boob points, and some personality ones, so you're miles ahead on points anyway."
    scene ep1_bowling_boobgreet1 with dissolve
    ki "Don't worry. You got some points yourself already, and there's plenty more to play for."
scene ep1_bowling_robin2 with fade
$ clockis = [[todayIs],2,1,0,5]
me "Was nice meeting you Robin, and thank you for letting us play."
scene ep1_bowling_robin1 with dissolve
ro "No problem really, [name]."
ro "By the way, you want a drink?"
scene ep1_bowling_robin2 with dissolve
me "Oh, that sounds nice."
scene ep1_bowling_robin3 with dissolve
ro "He'll be right there, Kira."
scene ep1_bowling_robin1 with dissolve
ro "You can tell a lot about the man by the drinks he orders."
ro "Cocktail or Mocktail? On the house."
$ ep1OrderedBeer = False
$ ep1OrderedMocktail = False
$ ep1OrderedDrink = 0
scene ep1_bowling_robin2 with dissolve
menu:
    "[M_01_010a]": # "Cocktail":
        $ XProbin += 2
        me "A Cocktail sounds perfect right now."
        jump afterCocktailQ
    "[M_01_010b]": # "Mocktail":
        $ XProbin += 1
        $ ep1OrderedMocktail = True
        me "I'll just go with a Mocktail."
        scene ep1_bowling_robin1 with dissolve
        ro "Careful guy, faithful. Not really looking to do to anything stupid. Or afraid to."
        scene ep1_bowling_robin2 with dissolve
        me "Wait, did you just assess me by ordering non alcoholic?"
        scene ep1_bowling_robin1 with dissolve
        ro "Yup."
        jump afterCocktailQQ
    "[M_01_010c]": # "Beer?":
        $ ep1OrderedBeer = True
        me "Got any beer behind that counter?"
        scene ep1_bowling_robin1 with dissolve
        ro "Sure, but let me at least try my bartender skills by mixing you up a Cocktail first."
        scene ep1_bowling_robin2 with dissolve
        me "Of course."
        jump afterCocktailQ
label afterCocktailQ:
scene ep1_bowling_robin1 with dissolve
ro "Which one?"
scene ep1_bowling_robin2 with dissolve
menu:
    "[M_01_011a]": # "Kamikaze":
        $ XProbin += 1
        $ ep1OrderedDrink = 1
        me "Can't go wrong with Kamikaze."
        scene ep1_bowling_robin1 with dissolve
        ro "Trendy guy, likes that people praise him for his good taste. Doesn't mind hooking up for a one-nighter."
        scene ep1_bowling_robin2 with dissolve
        me "That was your assessment based upon my drink of choice?"
        scene ep1_bowling_robin1 with dissolve
        ro "Yup."
        jump afterCocktailQQ
    "[M_01_011b]": # "Strawberry Daiquiri":
        $ XProbin += 1
        $ ep1OrderedDrink = 2
        me "Let me try your version of Strawberry Daiquiri."
        scene ep1_bowling_robin1 with dissolve
        ro "Not very adventurous. Got hots for sweet stuff and sticks to what works. Hopes he finds an ex or earlier one-nighter for some fun."
        scene ep1_bowling_robin2 with dissolve
        me "That was your assessment based upon my drink of choice?"
        scene ep1_bowling_robin1 with dissolve
        ro "Yup."
        jump afterCocktailQQ
    "[M_01_011c]": # "Surprise me":
        $ XProbin += 3
        $ ep1OrderedDrink = 3
        me "Surprise me."
        scene ep1_bowling_robin1 with dissolve
        ro "Ah, good answer."
        scene ep1_bowling_robin2 with dissolve
        me "Wait, were you trying to assess me by my drink of choice?"
        scene ep1_bowling_robin1 with dissolve
        ro "Indeed. Which you dodged brilliantly by the way."
        jump afterCocktailQQ
label afterCocktailQQ:
scene ep1_bowling_robin3 with dissolve
ro "Kira! You want Cock or Mock?"
ki "Cock!"
scene ep1_bowling_robin4 with dissolve
ro "Of course she does..."
scene ep1_bowling_robin1 with dissolve
ro "So [name], you seem like a good guy?"
scene ep1_bowling_robin2 with dissolve
me "At least I try to be. Is it working?"
scene ep1_bowling_robin1 with dissolve
ro "Well, you're charming, so that's a good start."
ro "But jokes aside...."
ro "You see, me and Kira go back quite a while, and we've always been very straightforward."
ro "With each other and everybody else."
ro "So you answer one question, and I'll give you the best advice you can possibly get about her."
ro "Sounds fair?"
scene ep1_bowling_robin_drink1 with dissolve
me "No harm in that I suppose. Shoot."
scene ep1_bowling_robin_drink2 with dissolve
ro "Ok, that's a promise then."
scene ep1_bowling_robin_drink3 with dissolve
me "I guess it is."
scene ep1_bowling_robin_drink4 with dissolve
ro "Do you want to fuck Kira today?"
scene ep1_bowling_robin2 with dissolve
me "Whoa... That's...straight to the point."
scene ep1_bowling_robin1 with dissolve
ro "Don't back up now, big boy. Isn't this so much more fun than chatting about the weather."
scene ep1_bowling_robin2 with dissolve
me "For you maybe, asking the questions."
scene ep1_bowling_robin2 with dissolve
menu:
    "[M_01_012a]": # "Of course!":
        $ XProbin -= 1
        $ meSporty += 1
        $ ep1RobMeConversation = 1
        scene ep1_bowling_robin_drink6 with dissolve
        show screen slvl with dissolve
        me "Of course I'd like to fuck her. I'm looking to have a bit of fun without commitments, and she seems to want that too."
        hide screen slvl with dissolve
        scene ep1_bowling_robin_drink4 with dissolve
        ro "Hm... Ok, I'll play along..."
        scene ep1_bowling_robin_drink7 with dissolve
        me "Huh?"
        scene ep1_bowling_robin1 with dissolve
        ro "Never mind."
        scene ep1_bowling_robin2 with dissolve
        me "But what's the advice?"
        jump afterRobmeConversation
    "[M_01_012b]": # "First date too early.":
        $ XProbin += 1
        $ meRomantic += 1
        $ ep1RobMeConversation = 2
        scene ep1_bowling_robin_drink6 with dissolve
        show screen rlvl with dissolve
        me "I like her, but I'm not the 'wham-bam thank-you-mam' kind of guy."
        hide screen rlvl with dissolve
        me "To be honest, I'm not even sure this counts as a date. I met her just earlier today, and a few hours later she asked me if I wanted to hang out with her."
        scene ep1_bowling_robin_drink4 with dissolve
        ro "Then my advice covers itself."
        scene ep1_bowling_robin_drink7 with dissolve
        me "I'd still like to hear your wording."
        jump afterRobmeConversation
    "[M_01_012c]": # "This isn't a date.":
        $ XProbin += 1
        $ ep1RobMeConversation = 3
        scene ep1_bowling_robin_drink6 with dissolve
        me "This isn't a date. I'm just here to have fun bowling with nice company."
        scene ep1_bowling_robin_drink4 with dissolve
        ro "Just be nice to her."
        scene ep1_bowling_robin_drink7 with dissolve
        me "That was the advice?"
        scene ep1_bowling_robin1 with dissolve
        ro "No, here comes the advice..."
        jump afterRobmeConversation
    "[M_01_012d]": # "I kinda like you, to be honest.":
        $ XProbin += 2
        $ meFlirty += 1
        $ ep1RobMeConversation = 4
        $ ep1SaidLikedRobin = True
        scene ep1_bowling_robin_drink6 with dissolve
        me "This isn't a date or anything. She just asked me if I wanted to hang out for a while."
        me "And if I am going to be completely honest..."
        scene ep1_bowling_robin_drink4 with dissolve
        ro "You said you would be..."
        scene ep1_bowling_robin_drink7 with dissolve
        show screen flvl with dissolve
        me "I think I might be attracted to you."
        hide screen flvl with dissolve
        scene ep1_bowling_robin1 with dissolve
        ro "Thank you for your honesty. I like that."
        ro "But now you are here with her."
        ro "So, just be nice to her."
        scene ep1_bowling_robin2 with dissolve
        me "That was the advice?"
        scene ep1_bowling_robin1 with dissolve
        ro "No, here comes the advice..."
        jump afterRobmeConversation
label afterRobmeConversation:
scene ep1_bowling_robin1 with dissolve
ro "If you find out that you really like her, say no today."
scene ep1_bowling_robin_drink8 with dissolve
ro "Anyway, here's the drinks. 2 cocktails. Enjoy yourself, [name]."
if ep1OrderedMocktail:
    scene ep1_bowling_robin2 with dissolve
    me "I ordered a mocktail."
    scene ep1_bowling_robin1 with dissolve
    ro "I know, but that's not what you wanted. So enjoy my little surprise drink."
scene ep1_bowling_robin2 with dissolve
me "Thanks Robin."
me "And also for that piece of advice. I can tell you care a lot about her."
scene ep1_bowling_robin1 with dissolve
ro "Yes...I do care a lot about Kira."
scene ep1_bowling_robin_drinkleave with dissolve
ro "{size=20}But believe me...{/size}"
ro "{size=20}...that advice was with your best interest in mind, not hers.{/size}"
scene ep1_bowling_down_kira1 with fade
$ clockis = [[todayIs],2,1,1,0]
$ phContNotify = True
$ contact_notify_robin = True
$ contact_text_robin += "\n\nShe told me to be nice to Kira before bowling."
me "Ready to kick my ass?"
ki "You betcha."
scene ep1_bowling_down_kira2 with dissolve
me "Here's one drink for you."
scene ep1_bowling_down_kira3 with dissolve
me "Cheers then!"
ki "Cheers."
scene ep1_bowling_down_talk1 with dissolve
ki "So you've never bowled before?"
scene ep1_bowling_down_blink with dissolve
me "Nope, never. But I thought it was a good time as ever to try something new."
me "Worst case scenario, I make a fool out of myself."
scene ep1_bowling_down_talk2 with dissolve
ki "I promise I will not laugh."
ki "Unless you really fuck up."
ki "And who knows, you might be a natural."
scene ep1_bowling_down_listen with dissolve
me "Normally I'm a fast learner, but babysteps please."
me "You bowled a lot?"
scene ep1_bowling_down_talk1 with dissolve
ki "I used to bowl all the time. My family owned a bowling alley, and I spent a lot of time there growing up."
ki "Then I moved to the city, and it kinda died out."
scene ep1_bowling_down_blink with dissolve
me "Well, I'll try to be a good student. It looks fun though, I've always wanted to try."
scene ep1_bowling_down_talk1 with dissolve
stop music fadeout 3
ki "Sure. Come here and let's get started. We wont play for points anyway."
scene ep1_bowling_kira_music1 with dissolve
ki "Oh, before I forget, let me put on some good music."
play music ep1_bowling
$ phMusiOpen = True
$ nowPlayingArtist = "Lexi Dimante"
$ nowPlayingTitle = "Crazy"
$ nowPlayingRealArtist = "Lance Conrad"
$ nowPlayingRealTitle = "Born to Drive Me Crazy"
ki "I love Lexi!"
me "(Lexi who?)"
scene ep1_bowling_kira_music2 with dissolve
ki "Come on. Let's bowl."
scene ep1_bowling_kira_down_getball with dissolve
ki "So... Find yourself a bowling ball where the holes fit your fingers, and you are comfortable with its weight."
scene ep1_bowling_kira_down_showball with dissolve
ki "Next, you try to find the optimal starting position about 3 steps from the line. And you hold the ball up like this."
ki "Then, move forward, left foot first. And during those 3 steps forward you bring the bowling ball back, forth, and throw on 3."
me "Uhum."
scene ep1_bowling_kira_down_showball2 with dissolve
ki "You will get it in a few tries, I promise."
scene ep1_bowling_down_bowl1 with dissolve
ki "Let me show you."
ki "And pay attention to my movement, not my ass."
menu:
    "[M_01_013a]": # "Of course":
        scene ep1_bowling_kira_closeup with dissolve
        me "Of course."
        jump AfterBowlingAss
    "[M_01_013b]": # "Of course (whistle)":
        scene ep1_bowling_kira_closeup with dissolve
        play sound whistle
        $ XPkira += 1
        $ meSporty += 1
        show screen slvl with dissolve
        me "Of course."
        hide screen slvl with dissolve
        scene ep1_bowling_kira_down_showball2 with dissolve
        ki "Are you trying to distract me?"
        scene ep1_bowling_kira_closeup with dissolve
        me "Maybe..."
        jump AfterBowlingAss
label AfterBowlingAss:
scene ep1_bowling_down_bowl1 with dissolve
ki "Ok, here we go."
scene ep1_bowling_down_bowl2 with dissolve
ki "One..."
scene ep1_bowling_down_bowl3 with dissolve
ki "Two..."
scene ep1_bowling_down_bowl4 with dissolve
ki "Three..."
scene ep1_bowling_kira_ball1 with Dissolve(0.25, alpha=True)
play sound bowlroll
$ renpy.pause(0.5)
scene ep1_bowling_kira_ball2 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_kira_ball3 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_kira_ball4 with Dissolve(0.25, alpha=True)
play sound bowlhit
$ renpy.pause(0.5)
scene ep1_bowling_kira_strike with dissolve
ki "Strrrrrrrike!"
me "Sounds hard, looks easy."
scene ep1_bowling_kira_youreup with dissolve
ki "You're next."
scene ep1_bowling_kira_meup with dissolve
me "(...something with three steps, and let go of the ball...)"
scene ep1_bowling_me_ball1 with Dissolve(0.25, alpha=True)
play sound bowlroll
$ renpy.pause(0.5)
scene ep1_bowling_me_ball2 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_me_ball3 with Dissolve(0.25, alpha=True)
stop sound fadeout 2
$ renpy.pause(0.5)
scene ep1_bowling_me_ball4 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_bowling_me_cheering1 with dissolve
me "Nailed it!"
scene ep1_bowling_me_cheering2 with dissolve
ki "*laughs* Are you ok?"
me "I'll live."
me "Scarred for life though."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_bowling_kira_youreup with fade
$ clockis = [[todayIs],2,2,3,2]
ki "A little break?"
me "Yes please!"
scene ep1_bowling_down_talk2 with dissolve
ki "I hope you're enjoying yourself."
scene ep1_bowling_down_blink with dissolve
me "I am actually. Nice company, good drinks, learning something new."
me "And you?"
scene ep1_bowling_down_talk2 with dissolve
ki "I didn't quite know what to think, when you came up with that lame pickup line earlier."
scene ep1_bowling_down_talk1 with dissolve
ki "But I thought why not have a little fun."
scene ep1_bowling_down_talk2 with dissolve
ki "And you know, you're not so bad [name]. And no groping the ass or breasts yet, or indecent propositions."
if ep1LookedKiraBoobs:
    scene ep1_bowling_down_listen with dissolve
    me "You're forgetting me staring at your boobs."
    scene ep1_bowling_down_talk2 with dissolve
    ki "No, I didnt. Men reacts to boobs. You didn't stare."
    ki "You took a peak, and I'm ok with that."
else:
    scene ep1_bowling_down_listen with dissolve
    me "Maybe I've been looking at your boobs."
    scene ep1_bowling_down_talk2 with dissolve
    ki "Men reacts to boobs. At least you don't stare. You take a peak, and that's fine."
scene ep1_bowling_down_talk1 with dissolve
ki "The problem is when you have to wave your arms to get eye-contact."
scene ep1_bowling_down_talk2 with dissolve
ki "And it's not like I'm not peaking at your sexy ass anyway."
scene ep1_bowling_down_listen with dissolve
me "I don't have a sexy ass."
scene ep1_bowling_down_talk2 with dissolve
ki "No. You don't have confidence. But you do have a sexy ass."
scene ep1_bowling_down_blink with dissolve
me "Glad you like it then."
scene ep1_bowling_down_talk1 with dissolve
ki "Not bad for a first time bowling by the way, you're improving fast."
scene ep1_bowling_down_blink with dissolve
me "Yeah, that's kinda my trademark. I tend to learn quickly."
scene ep1_bowling_down_talk2 with dissolve
ki "That also apply to sex?"
scene ep1_bowling_down_listen with dissolve
me "..."
scene ep1_bowling_down_talk1 with dissolve
ki "Sorry, these drinks hit me hard. I'm overstepping."
scene ep1_bowling_down_blink with dissolve
me "Nono, don't worry. I find you refreshing."
$ BowlDiscussMePast = False
menu:
    "[M_01_014a]": # "It's been a while.":
        $ BowlDiscussMePast = True
        me "But I guess you can probably say I'm out of practice."
        scene ep1_bowling_down_talk2 with dissolve
        ki "So...boy meets girl, great relationship, girl leaves boy, boy grieves for way too long?"
        scene ep1_bowling_down_blink with dissolve
        me "You could say that."
        me "But then the day comes when you decide to move on."
        scene ep1_bowling_down_talk1 with dissolve
        ki "You mean, today?"
        scene ep1_bowling_down_blink with dissolve
        me "It's that obvious, huh."
        jump AfterBowlingSexConversation
    "[M_01_014b]": # "I don't know.":
        me "But I have no idea what my skill level is in the bedroom."
        scene ep1_bowling_down_talk1 with dissolve
        ki "You can't tell by the way a woman reacts?"
        scene ep1_bowling_down_blink with dissolve
        me "Sure."
        me "But I don't know how that stacks up with other people and the norm though."
        scene ep1_bowling_down_talk1 with dissolve
        ki "Any exes or friends with benefits?"
        scene ep1_bowling_down_blink with dissolve
        me "No. Ex moved somewhere, and no friends with benefits."
        scene ep1_bowling_down_talk2 with dissolve
        ki "Bad breakup?"
        scene ep1_bowling_down_blink with dissolve
        me "Kinda. Suddenly she was gone. But that's years in the past."
        jump AfterBowlingSexConversation
label AfterBowlingSexConversation:
$ clockis = [[todayIs],2,2,4,4]
me "How about you? I hardly know anything about you."
scene ep1_bowling_down_talk2 with dissolve
ki "You actually know more than you think. Got that crappy job you already know of, which pays way too little."
ki "Meaning, I compensate by working shitloads to cover my expenses."
ki "My off work hours I try to meet new people and do fun stuff."
scene ep1_bowling_down_listen with dissolve
me "Not one for cuddling under the blanket with an evening of Flix eh?"
scene ep1_bowling_down_talk2 with dissolve
ki "Sure, that too. But most of the time I'm searching for anything fun."
ki "Anything from camping, hanging out with friends, meeting new ones, clubbing..."
scene ep1_bowling_down_listen with dissolve
me "Like Metronome tomorrow?"
scene ep1_bowling_down_talk2 with dissolve
ki "*laughs* Yeah, like any normal person would ever get a hold of those tickets."
label ep1AfterKiraMetroTalk:
scene ep1_bowling_down_listen with dissolve
me "Are you saying I'm not normal?"
scene ep1_bowling_down_talk2 with dissolve
ki "Sure. You are pulling my leg."
me "..."
scene ep1_bowling_down_talk1 with dissolve
ki "Holy shit. You are {b}not{/b} pulling my leg."
ki "I am sooo envious right now."
scene ep1_bowling_down_blink with dissolve
me "Chris did some work there, and got tickets."
scene ep1_bowling_down_talk2 with dissolve
ki "That goofy friend from earlier?"
scene ep1_bowling_down_blink with dissolve
me "That's the one. Yeah, I know he's goofy. He's got a heart of gold though."
me "I can try talking to him and see if he might have an extra ticket for you if you'd like?"
scene ep1_bowling_down_talk2 with dissolve
ki "You would do that for me?"
me "Sure, I'll message him right away."
ki "I hope he got an extra. I'll pay even."
scene ep1_bowling_down_blink with dissolve
me "He'll never accept any payment though."
show ep1_phone_nosignal_plaza
me "(Damn. No signal.)"
me "(I can try connecting to that hotspot though.)"
me "(Connecting.)"
me "(Connecting..)"
me "(Connecting...)"
me "(Connecting....)"
me "(Nah, this is taking too long.)"
hide ep1_phone_nosignal_plaza
me "No signal in here. I'll have to message him afterwards."
scene ep1_bowling_down_talk2 with dissolve
ki "It's getting a bit late after all. We should probably call it."
scene ep1_bowling_kira_down_getball with dissolve
ki "I'll just do one more before we head out. And you can get another look at my cute behind."
scene ep1_bowling_down_bowl1 with dissolve
hide screen phone
show screen phone_camop
$ phone_camop_screen = "ep1_bowling"
me "I would never."
label phonecambowl_loop:
    "Click on the phone or press '{b}[custom_phone_key]{/b}'."
    jump phonecambowl_loop
label photoop_ep1_bowling:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_bowling_kira_closeup"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_bowling_kira_closeup with Fade(0, 0, 0.5, color="#ffffff")
jump phonecambowl_done
label phonecambowl_done:
$ phGallNotify = True
show screen phone
scene ep1_bowling_down_bowl2 with dissolve
$ renpy.pause(0.5)
scene ep1_bowling_down_bowl3 with dissolve
$ renpy.pause(0.5)
scene ep1_bowling_down_bowl5 with dissolve
ki "What the..."
play sound bowlroll
scene ep1_bowling_kira_bigass1 with dissolve
stop sound fadeout 2
ki "[name]?"
scene ep1_phone_fumbling_plaza with dissolve
me "Oh, someone kill me..."
scene ep1_bowling_me_fumbling3 with dissolve
me "..."
scene ep1_bowling_kira_bigass2 with dissolve
ki "*laughs* ... *makes dark voice*...'I would never'..."
scene ep1_bowling_kira_bigass3 with dissolve
me "Yeah, listen. I'm sorry about that."
me "Let me help you up."
scene ep1_bowling_kira_hugkiss1
ki "Apology accepted."
menu:
    "[M_01_015a]": # "Kiss her":
        $ ep1KissedKiraBowling = True
        scene ep1_bowling_kira_hugkiss3 with dissolve
        $ renpy.pause()
        scene ep1_bowling_kira_hugkiss4 with dissolve
        $ XPkira += 1
        ki "That's..."
        ki "...a bunch of points, mr."
        ki "(Shit, I'm getting horny.)"
        scene ep1_bowling_kira_awkward with dissolve
        ki "Listen..."
        me "Don't... I just made this awkward."
        jump AfterBowlingKissOp
    "[M_01_015b]": # "Hug her":
        scene ep1_bowling_kira_hugkiss2 with dissolve
        ki "(He smells so nice.)"




        jump AfterBowlingKissOp
label AfterBowlingKissOp:
$ clockis = [[todayIs],2,3,1,2]
scene ep1_bowling_kira_awkwardsave with dissolve
me "That is one humongous butt though."
ki "Will you... *punches*"
me "Ouch..."
scene ep1_bowling_finishing with dissolve
me "Anyway, now that I've obviously connected my phone to the big screen..."
me "Maybe we should take a more decent picture?"
ki "We should."
$ ep1_bowling_normalselfie = True
menu:
    "[M_01_016a]": # "Friendly selfie.":
        me "Say cheese!"
        play sound camerashutter
        $ cam_gallery_append_item1 = "ep1_bowling_kira_me_selfie_nice"
        if cam_gallery_append_item1 not in cam_gallery:
            $ cam_gallery.append(cam_gallery_append_item1)
        show bg_empty
        scene ep1_bowling_kira_me_selfie_nice with Fade(0, 0, 0.5, color="#ffffff")
        $ renpy.pause()
        jump AfterBowlingPicture
    "[M_01_016b]": # "Goofy selfie.":
        $ ep1_bowling_normalselfie = False
        me "Goofytime!"
        play sound camerashutter
        $ cam_gallery_append_item1 = "ep1_bowling_kira_me_selfie_goof"
        if cam_gallery_append_item1 not in cam_gallery:
            $ cam_gallery.append(cam_gallery_append_item1)
        show bg_empty
        scene ep1_bowling_kira_me_selfie_goof with Fade(0, 0, 0.5, color="#ffffff")
        $ renpy.pause()
        jump AfterBowlingPicture
label AfterBowlingPicture:
$ phGallNotify = True
if ep1_bowling_normalselfie:
    scene ep1_bowling_leaving_nice with dissolve
else:
    scene ep1_bowling_leaving_goofy with dissolve
stop music fadeout 5
menu:
    "[M_01_017a]": # "Walk you home?":
        $ ep1KiraWalkHome = True
        me "Would you like me to walk you home?"
        ki "I'd love that."
        scene bg empty with fade
        $ eveningStrollMusic = True
        play music ep1_stroll
        $ nowPlayingArtist = "Ziv Moran"
        $ nowPlayingTitle = "Seven Wonders"
        $ nowPlayingRealArtist = ""
        $ nowPlayingRealTitle = ""
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        scene ep1_bowling_walkhome1 with fade
        $ clockis = [[todayIs],2,3,2,9]
        ki "This is me."
        scene ep1_bowling_walkhome_blink with dissolve
        me "Thanks again for the bowling lesson."
        me "I hope you had as much fun as I did."
        scene ep1_bowling_walkhome_prekiss1 with dissolve
        me "Good night, Kira."
        scene ep1_bowling_walkhome_prekiss2 with dissolve
        me "..."
        scene ep1_bowling_afterkiss with dissolve
        $ renpy.pause()
        scene ep1_bowling_walkhome_prekiss1 with dissolve
        ki "Would you like to..."
        ki "...come in?"
        menu:
            "[M_01_018a]": # "Yes":
                $ ep1RejectedKira = False
                me "Yes, I'd like that."
                scene ep1_bowling_kira_worried with dissolve
                ki "Fuck..."
                ki "My desires got the best of me."
                ki "I shouldn't have...not tonight."
                me "It's ok. But thank you for the vote of confidence."
            "[M_01_018b]": # "No":
                scene ep1_bowling_walkhome_blink with dissolve
                me "I want to, but I shouldn't. I don't want to be that kind of guy."
                scene ep1_bowling_kira_worried with dissolve
                ki "That ... makes sense."
                me "Don't get me wrong, but me saying no just means I respect you."
        scene ep1_bowling_walkhome_prekiss1 with dissolve
        ki "Good night, [name]."
        scene ep1_bowling_afterkiss_regret with fade
        ki "{size=20}(What the fuck am I doing.){/size}"
        ki "{size=20}(A few drinks with a nice guy, and I forget everything...){/size}"
        ki "{size=20}(...everyone.){/size}"
        jump eveningStroll
    "[M_01_017b]": # "Say goodnight.":
        me "Good night Kira. I had a really good time tonight. Have a safe journey home, and sleep tight."
        ki "You too [name]."
        jump eveningStroll

label beforeEveningStroll:
$ clockis = [[todayIs],2,3,1,9]
scene ep1_home_mid_sofa1 with dissolve
me "(Oh, wow. I've slept all through the evening.)"
stop music fadeout 3
me "(There's no use in going to bed now. I'll never be able to sleep.)"
me "(I think I'll take a little walk through the city.)"
label eveningStroll:
$ todayIs = 2
$ clockis = [[todayIs],0,0,0,1]
if wentBowlingKira:
    if ep1KiraWalkHome:
        if ep1RejectedKira:
            $ phContNotify = True
            $ contact_notify_me = True
            $ contact_text_me += "\n\nI had a nice evening bowling with Kira. She kissed me goodbye when I walked her home and invited me in. It didn't feel right to jump right into it that early."
            $ contact_notify_kira = True
            $ contact_text_kira += "\n\nShe seemed to enjoy herself bowling with me. Even kissed me goodbye when I walked her home and invited me in. I didn't accept her advances."
        else:
            $ phContNotify = True
            $ contact_notify_me = True
            $ contact_text_me += "\n\nI had a nice evening bowling with Kira. She kissed me goodbye when I walked her home and invited me in. I really wanted that, but she changed her mind."
            $ contact_notify_kira = True
            $ contact_text_kira += "\n\nShe seemed to enjoy herself bowling with me. Even kissed me goodbye when I walked her home and invited me in. But for some reason, she changed her mind after I agreed."
    else:
        if ep1KissedKiraBowling:
            $ phContNotify = True
            $ contact_notify_me = True
            $ contact_text_me += "\n\nI had a nice evening bowling with Kira. I kissed her, which she seemed to enjoy, but then it got awkward. I didn't walk her home."
            $ contact_notify_kira = True
            $ contact_text_kira += "\n\nShe seemed to enjoy herself bowling with me. Even when we kissed, but then it got awkward. I didn't walk her home."
        else:
            $ phContNotify = True
            $ contact_notify_me = True
            $ contact_text_me += "\n\nI had a nice evening bowling with Kira. It never got further than that though. I didn't walk her home."
            $ contact_notify_kira = True
            $ contact_text_kira += "\n\nShe seemed to enjoy herself bowling with me. It never got further than that though. I didn't walk her home."
if not eveningStrollMusic:
    play music ep1_stroll
    $ nowPlayingArtist = "Ziv Moran"
    $ nowPlayingTitle = "Seven Wonders"
    $ nowPlayingRealArtist = ""
    $ nowPlayingRealTitle = ""
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_street_walk0 with dissolve
if wentBowlingKira:
    me "(I had a nice evening with Kira.)"
    if ep1KissedKiraBowling:
        me "(...even got to kiss her. Not bad for a lazy evening of bowling.)"
        scene ep1_street_walk1 with dissolve
        if ep1KiraWalkHome:
            if ep1RejectedKira:
                me "(Getting invited to stay was a nice surprise, but it's too early for me.)"
                me "(We just met this morning.)"
            else:
                me "(Getting invited to stay was a nice surprise, but why the sudden changed of mind?)"
                me "(Maybe it's because before this morning she didn't even know who I was.)"
        else:
            me "(Maybe I should have walked her home. Or that might just have been a bad hint at something more.)"
            me "(Nothing would have happened anyway. Before this morning she didn't even know who I was.)"
    else:
        if ep1KiraWalkHome:
            me "(...even got to kiss her. Not bad for a lazy evening of bowling.)"
            scene ep1_street_walk1 with dissolve
            if ep1RejectedKira:
                me "(Getting invited to stay was a nice surprise, but it's too early for me.)"
                me "(We just met this morning.)"
            else:
                me "(Getting invited to stay was a nice surprise, but why the sudden changed of mind?)"
                me "(Maybe it's because before this morning she didn't even know who I was.)"
        else:
            me "(...maybe I should have kissed her...)"
            scene ep1_street_walk1 with dissolve
            me "(...or at least offered to walk her home. Or that might just have been a bad hint at something more.)"
    me "(Hmmm. I'll sit down at the bus stop for a bit.)"
    me "(Can just enjoy the sounds of the city, or jump on the bus if there's one coming.)"
else:
    me "(It's nice and quiet on the evenings mid week)"
    me "(Not too many people out, and you just get the background noises of the city itself.)"
    scene ep1_street_walk1 with dissolve
    me "(It's calming.)"
    me "(I think I'll just sit down and soak it in for a moment.)"
    me "(Or jump on a bus if there's any coming.)"
scene ep1_street_seecece1 with dissolve
me "(Oh, there's someone here.)"
scene ep1_street_seecece2 with dissolve
$ renpy.pause()
scene ep1_street_bench with dissolve
me "(I'll just sit down. Hope I'm not intruding.)"
scene ep1_street_introtalk1 with dissolve
me "(There's something about her though. Can't quite put my finger on it.)"
me "(Like she has this black cloud over her head.)"
scene ep1_street_introtalk5 with dissolve
me "(I'll try talking with her I guess. Hopefully she doesn't find me intimidating.)"
scene ep1_street_introtalk1 with dissolve
me "Nice evening."
scene ep1_street_introtalk2 with dissolve
uk "Huh?"
me "Sorry. Didn't mean to scare you. I was only looking for a little chat."
uk "..."
scene ep1_street_introtalk6 with dissolve
uk "It's ok."
uk "I like it too."
scene ep1_street_introtalk2 with dissolve
me "I've always enjoyed the atmosphere in the evenings. The perfect way to calm down."
scene ep1_street_introtalk1 with dissolve
uk "..."
me "(She seems quiet. Maybe she doesn't want me to speak to her.)"
me "(But something tells me I should.)"
menu:
    "[M_01_019a]": # "Keep chit-chatting":
        $ XPcece += 2
        me "Evenings makes me feel less awkward. Not too many people out. And those who are out, are too drunk to notice you anyway."
        uk "..."
        scene ep1_street_introtalk2 with dissolve
        me "And of course, looking at all the drunk people doing stupid stuff always gets me smiling."
        uk "..."
        menu:
            "[M_01_020a]": # "Keep chit-chatting":
                $ XPcece += 2
                scene ep1_street_introtalk1 with dissolve
                me "The weather is so nice this time of year. Like winter finally letting go and sun is warm again."
                uk "..."
                scene ep1_street_introtalk2 with dissolve
                me "Flowers starting to bloom, leaves growing back on trees. It's a good time to be alive."
                scene ep1_street_introtalk3 with dissolve
                uk "..."
                jump talkWithCece2
            "[M_01_020b]": # "Ask where she's going":
                $ XPcece += 1
                me "Where are you heading?"
                uk "..."
                scene ep1_street_introtalk6 with dissolve
                uk "Nowhere really."
                scene ep1_street_introtalk3 with dissolve
                me "You're not in trouble, are you?"
                uk "No."
                jump talkWithCece2
    "[M_01_019b]": # "Ask where she's going":
        $ XPcece += 1
        me "Where are you heading?"
        uk "..."
        scene ep1_street_introtalk6 with dissolve
        uk "Nowhere really."
        scene ep1_street_introtalk1 with dissolve
        me "You are not in trouble, are you?"
        uk "No."
        menu:
            "[M_01_021a]": # "Keep chit-chatting":
                $ XPcece += 2
                scene ep1_street_introtalk1 with dissolve
                me "Evenings makes me feel less awkward. Not too many people out. And those who're out, are too drunk to notice you anyway."
                uk "..."
                scene ep1_street_introtalk3 with dissolve
                me "And of course, looking at all the drunk people doing stupid stuff always gets me smiling."
                uk "..."
                jump talkWithCece2
            "[M_01_021b]": # "Waiting for someone?":
                $ XPcece += 1
                me "Waiting for someone?"
                uk "..."
                scene ep1_street_introtalk6 with dissolve
                uk "You do ask a lot of questions."
                scene ep1_street_introtalk3 with dissolve
                me "I guess it sounded a bit like an interrogation."
                uk "..."
                jump talkWithCece2
label talkWithCece2:
$ clockis = [[todayIs],0,0,1,4]
scene ep1_street_introtalk3 with dissolve
$ renpy.pause(0.5)
scene ep1_street_introtalk4 with dissolve
$ renpy.pause(0.5)
scene ep1_street_cece_walkover1 with dissolve
$ renpy.pause(0.5)
scene ep1_street_cece_walkover2 with dissolve
$ renpy.pause(0.5)
scene ep1_street_cece_sitdown1 with dissolve
$ renpy.pause(0.5)
scene ep1_street_cece_sitdown2 with dissolve
$ renpy.pause(1.5)
scene ep1_street_cece_sitting_blink with dissolve
$ renpy.pause(1.5)
me "You know, I'm awful at small talk."
scene ep1_street_cece_sitting1 with dissolve
uk "That much I could tell."
me "Thank you for letting me practice on you though."
scene ep1_street_cece_sit_slightsmile with dissolve
uk "*small laugh*"
scene ep1_street_cece_sitting_blink with dissolve
me "I have to admit that there is this little instinct inside me that just wants to make sure you're ok."
uk "..."
scene ep1_street_cece_sitting1 with dissolve
uk "I know I seem a bit off."
scene ep1_street_cece_sitting_blink with dissolve
me "Anything I can help with?"
scene ep1_street_cece_sitting1 with dissolve
uk "No..."
uk "...but I'm ok...now."
uk "So you already helped."
uk "And your voice is soothing, so feel free to say whatever."
scene ep1_street_cece_sitting_blink with dissolve
menu:
    "[M_01_022a]": # "Keep chit-chatting":
        $ XPcece += 1
        me "I can relate to that. Sometimes it's the company, and not the words that matter."
        jump midTalkWithCece
    "[M_01_022b]": # "Ask if she needs money":
        $ XPcece += 1
        me "You know..."
        me "...if you need money for the bus, just say so. I have some cash on me."
        scene ep1_street_cece_sitting1 with dissolve
        uk "Nah. I'm fine."
        me "All good then. Just say so if there's anything I can help with."
        uk "Thank you."
        jump midTalkWithCece
label midTalkWithCece:
scene ep1_street_cece_sitting1 with dissolve
uk "ehm... This might come completely out of the blue..."
scene ep1_street_cece_sit_talk with dissolve
uk "You wouldn't happen to have any booze?"
me "Sorry, I don't."
scene ep1_street_cece_sitting1 with dissolve
uk "I had some plans, but now I feel like getting wasted instead."
scene ep1_street_cece_sitting_blink with dissolve
menu:
    "[M_01_023a]": # "You can get a drink at a nightclub":
        me "There's always nightclubs you can go for plenty of booze."
        scene ep1_street_cece_sitting1 with dissolve
        uk "Too many people."
    "[M_01_023b]": # "Probably not a good time for a drink":
        me "But if something is troubling you, it's probably better to stay sober."
        me "Things tend to escalate when drinking."
        scene ep1_street_cece_sitting1 with dissolve
        uk "Depends....but maybe..."
scene ep1_street_cece_sitting_blink with dissolve
uk "..."
scene ep1_street_cece_wonderous1 with dissolve
uk "Have you ever been really, really depressed?"
uk "Not like sad about something, but so overwhelming that you don't even know how to feel?"
scene ep1_street_cece_wonderous2 with dissolve
me "Everybody has depression at some point."
me "If they say otherwise, they would be lying."
uk "..."
scene ep1_street_cece_wonderous4 with dissolve
uk "So I have this friend. She means the world to me."
uk "She even sacrifices her own well being, just to make sure I'm good."
scene ep1_street_cece_wonderous5 with dissolve
me "Sounds like a good friend."
scene ep1_street_cece_wonderous4 with dissolve
uk "Yes, she is. But sometimes I wish she would just forget about me for a second, and do something for herself."
uk "Like the other day, we were going shopping because she needed new shoes."
show hello_cece_na at imgSlideIntroName
ce "And she goes, 'but these shoes are perfect for you Cece, I'm buying them for you'"
hide hello_cece_na
scene ep1_street_cece_shoes with dissolve
ce "So I end up with new shoes, and she goes home empty handed, smiling like she'd won the lottery."
me "I'm sure she treasures you just as much as you do her."
scene ep1_street_cece_wonderous3 with dissolve
ce "I guess."
scene ep1_street_cece_wonderous5 with dissolve
me "Cece, is it?"
ce "Yes."
scene ep1_street_cece_face1 with dissolve
me "Beautiful name. I'm [name]."
me "By the way, it's a good look on you."
ce "What is?"
me "Your smile."
scene ep1_street_cece_face2 with dissolve
ce "..."
scene ep1_street_cece_face3 with dissolve
ce "What's the catch?"
me "Me saying your smile looks good on you, doesn't come with a catch."
me "It means you have a beautiful smile."
scene ep1_street_cece_face2 with dissolve
ce "Thank you..."
me "But whatever is going on with you and your friend."
me "I hope you figure it out, and stay well."
scene ep1_street_cece_face1 with dissolve
me "There it is again."
scene ep1_street_cece_yawn with dissolve
ce "*yawns*"
me "...and I'm boring you."
scene ep1_street_cece_face2 with dissolve
ce "No, you're not."
ce "It's just been a long day."
ce "...and your voice is really soothing."
scene ep1_street_cece_face3 with dissolve
$ ep1OfferedCeceStay = False
menu:
    "[M_01_024a]": # "Bid your farewell":
        me "Yeah, I probably should start walking home and get some shuteye myself."
        me "I don't think there's a bus coming anyway."
        jump afterTalkWithCece
    "[M_01_024b]": # "Offer her to stay at your place":
        $ ep1OfferedCeceStay = True
        me "If you don't have a place to stay, I can help you. You can spend the night at my place if you need to."
        scene ep1_street_cece_face5 with dissolve
        ce "No...I..."
        ce "...I don't do that."
        scene ep1_street_cece_face3 with dissolve
        me "Fuck me. I didn't mean it that way. But you're right, it came out all wrong."
        me "Sorry."
        scene ep1_street_cece_face2 with dissolve
        ce "It's fine, but I should get going."
        me "Me too. I don't think there's a bus coming anyway."
        jump afterTalkWithCece
label afterTalkWithCece:
$ clockis = [[todayIs],0,0,3,8]
scene ep1_street_cece_face4 with dissolve
ce "There isn't. Last bus of the day was at midnight, just before you came."
me "Oh, you weren't waiting for the bus?"
scene ep1_street_cece_face1 with dissolve
ce "Nah. Just relaxing."
scene ep1_street_cece_bye with dissolve
$ phContNotify = True
$ contact_cece = True
$ contact_notify_cece = True
$ chat_cece_item = "2;0;501;New contact added"
if chat_cece_item not in chat_cece:
    $ chat_cece.append(chat_cece_item)
stop music fadeout 3
me "Like me then. Maybe I'll meet you again some day."
ce "Maybe."
me "Take care."
scene bg empty
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ clockis = [[todayIs],1,0,0,0]
scene ep1_waking_up_front with fade
play sound phonealarm
$ renpy.pause(1)
stop sound fadeout 3
scene ep1_waking_up_awake with hpunch
play music ep1_inbetween
$ nowPlayingArtist = "Young Rich Pixies"
$ nowPlayingTitle = "A Good Mood"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "(Here we go again.)"
scene ep1_home_inbetween_kitchen1 with dissolve
$ clockis = [[todayIs],1,0,2,3]
me "(At least no dream of Steph this night. That must be good... or?)"
$ ep1CeceSituation = 0
$ ep1KiraRepliedMsg = False
$ ep1KiraRepliedMsgTickets = False
if wentBowlingKira:
    me "(But I had fun bowling with Kira yesterday.)"
    scene ep1_home_inbetween_kitchen2 with dissolve
    me "(Made a fool out of myself, but she didn't seem to mind.)"
    me "(If anything, she seemed charmed by it.)"
    scene ep1_home_inbetween_kitchen3 with dissolve
    play sound phone_notify_sound
    show screen phone_notify_chat
    if ep1KiraWalkHome:
        $ chat_kira_item = "1;0;601;Listen...about last night. I had a lot of fun, and I'm sorry about the way the evening ended. For forcing myself onto you, just to leave you hanging...just wanted to let you know."
    else:
        if ep1KissedKiraBowling:
            $ chat_kira_item = "1;0;602;Listen...about last night. I had a lot of fun, and I'm sorry I made you feel that your sweet kiss was awkward. It wasn't...just wanted to let you know."
        else:
            $ chat_kira_item = "1;0;603;Listen...about last night. I had a lot of fun...just wanted to let you know."
    if chat_kira_item not in chat_kira:
        $ chat_kira.append(chat_kira_item)
        $ phChatNotify = True
        $ chat_notify_kira = True
    $ phone_task_append_item1 = "4;2;1;2;0;0;Kira;Answer Kira before;Metronome tickets for Kira;1"
    $ phone_task_append_item2 = "4;2;1;2;0;0;Kira;Answer Kira before;Metronome tickets for Kira;2"
    if phone_task_append_item1 not in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.append(phone_task_append_item1)
            $ phTaskNotify = True
    me "(Speaking of...)"
    me "..."
    $ renpy.pause()
    if not ep1KiraRepliedMsg:
        menu:
            "[M_01_025a]": # "Check Kira's message":
                $ chat_notify_kira = False
                $ chat_sel_name = "Kira"
                $ chat_sel_icon = "cont_kira"
                call screen phone_chat_single
else:
    me "(That girl on the bus-stop I met last night. There was something special about her.)"
    scene ep1_home_inbetween_kitchen2 with dissolve
    menu:
        "[M_01_026a]": # "She was cute, I want to meet her again.":
            $ ep1CeceSituation = 1
            me "(I have to go by the bus stop again sometime. I want to meet her again.)"
            jump ep1WhatAboutKiraChoseChris
        "[M_01_026b]": # "Not into her, but I want to make sure she's alright.":
            $ ep1CeceSituation = 2
            me "(Maybe I should go by the bus-stop again, to make sure she's alright.)"
            jump ep1WhatAboutKiraChoseChris
        "[M_01_026c]": # "I hope she's alright.":
            $ ep1CeceSituation = 3
            me "(I hope she's alright, and whatever troubled her is ok now.)"
            jump ep1WhatAboutKiraChoseChris
label ep1WhatAboutKira:
hide screen phone
scene ep1_home_inbetween_kitchen4 with dissolve
me "(At least she ignored the 24 hour rule. That must be good news for me.)"





me "(But I haven't texted Chris yet.)"
$ ep1LiedToChris = False
menu:
    "[M_01_027a]": # "Text Chris":

        me "(Maybe he can get a hold of that extra ticket.)"
        $ chat_chris_item = "0;0;701;Yo man, you there? Wakie, wakie."
        if chat_chris_item not in chat_chris:
            $ chat_chris.append(chat_chris_item)
            $ phChatNotify = True
            $ chat_notify_chris = False
            $ chat_sel_name = "Chris"
            $ chat_sel_icon = "cont_chris"
            call screen phone_chat_single












label ep1WhatAboutKira2:
scene ep1_home_inbetween_kitchen3 with dissolve
if ep1KiraRepliedMsgTickets:
    me "(Well, that settles it. No extra tickets unfortunately.)"
else:
    me "(I didn't ask him about the extra tickets, but I know the answer already.)"
me "(I'd better get back to Kira.)"
if ep1KiraWalkHome:
    $ chat_kira_item = "0;0;611;You have nothing to apologize for. I had a lot of fun last night as well, and for what happened after...it was a nice thing. :)"
else:
    if ep1KissedKiraBowling:
        $ chat_kira_item = "0;0;612;You have nothing to apologize for. I had a lot of fun last night as well, and you shouldn't feel awkward. After all lots of people have huge asses. :)"
    else:
        $ chat_kira_item = "0;0;613;I had a lot of fun last night as well. Maybe we could do it again sometime. :)"
if chat_kira_item not in chat_kira:
    $ chat_kira.append(chat_kira_item)
    $ phChatNotify = True
    $ chat_notify_kira = True
menu:
    "[M_01_028a]": # "Tell her, no Metronome tickets":
        $ chat_notify_kira = False
        $ chat_sel_name = "Kira"
        $ chat_sel_icon = "cont_kira"
        call screen phone_chat_single
label ep1WhatAboutKiraChoseChris:
show screen phone
scene ep1_home_inbetween_kitchen2 with dissolve
stop music fadeout 5
me "(That settles that. Now I just got to kill time until he gets here.)"
scene bg empty
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
jump ep1MetroWithChris
label ep1MetroWithChris:
$ clockis = [[todayIs],2,0,0,7]
play music ep1_homevs
$ nowPlayingArtist = "Yanivi"
$ nowPlayingTitle = "Rock This Joint"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep1_home_vs_intro1 with fade
$ renpy.pause(0.5)
scene ep1_home_vs_intro2 with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_home_vs_intro3 with Dissolve(0.5, alpha=True)
ch "I come bearing gifts..."
scene ep1_home_vs_intro4 with dissolve
ch "...I mean, a shitload of beer!"
me "We're going all in?"
ch "You bet ya."
scene ep1_home_vs_intro5 with dissolve
me "That is an interesting choice of attire."
ch "Amazing, right? And a bargain at the 10-buck store."
me "I bet."
me "Two for one offer maybe?"
scene ep1_home_vs_beer1 with dissolve
ch "Oh shut up and drink, gray fox."
me "Don't mind if I do."
scene ep1_home_vs_beer2 with dissolve
ch "I'll go put these in the fridge."
scene ep1_home_vs_beer3 with dissolve
me "That is one smooth beer though."
ch "I know. We're going to get hammered."
scene ep1_home_vs_beer4 with dissolve
me "How much do I owe you for the beer?"
ch "Fuck you man. Friends don't charge for beer."
ch "...although, you might have to carry me home later on."
scene ep1_home_vs_introtalk with dissolve
$ clockis = [[todayIs],2,0,1,3]
if wentBowlingKira:
    ch "So... you and Kira eh?"
    scene ep1_home_vs_chrisblink with dissolve
    me "It was a nice evening."
    scene ep1_home_vs_christalk with dissolve
    ch "Oh no... You're not getting away that easily."
    scene ep1_home_vs_chrisdrink with dissolve
    me "*laughs* Was worth a try."
    me "Well, it started with me leaving MaKenzie yesterday after our lunch..."
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep1_home_vs_chrisblink with fade
    if ep1KiraWalkHome:
        me "...and then I walked her home, and ... well ... we might just have kissed."
    else:
        if ep1KissedKiraBowling:
            me "...and at the end of the night we ... well ... just might have kissed."
        else:
            me "...and that was that. Nothing happened afterwards. A hug, but nothing more."
    scene ep1_home_vs_christalk with dissolve
    ch "You have no idea how glad I am to hear that, man."
    ch "I thought I lost you there for a while, but damn, it's good to see you back."
    scene ep1_home_vs_chrisdrink with dissolve
    me "Guess so."
    scene ep1_home_vs_christalk with dissolve
    ch "So, you want to take it further with Kira, or this just a fling-thing?"
    scene ep1_home_vs_chrisblink with dissolve
    menu:
        "[M_01_029a]": # "I like her":
            $ ep1ToldChrisKiraSituation = 1
            me "I like her. Or I think I do, so I'm not ruling anything out."
            scene ep1_home_vs_christalk with dissolve
            ch "I get ya."
            ch "But... probably, don't rush head first into the first woman you see."
            ch "There's many nice women out there. Enjoy this moment of single-life while you can."
        "[M_01_029b]": # "I'm not into her like that":
            $ ep1ToldChrisKiraSituation = 2
            me "Probably nothing serious. But new friends doesn't hurt."
            scene ep1_home_vs_christalk with dissolve
            ch "I hear you."
        "[M_01_029c]": # "Friends with benefits potential":
            $ ep1ToldChrisKiraSituation = 3
            me "Don't think we'll become a thing. But she's got a hot body, and seems willing. So maybe friends with benefits material."
            scene ep1_home_vs_christalk2 with dissolve
            ch "*laughs* Yep, you're definitely back."
        "[M_01_029d]": # "No idea":
            $ ep1ToldChrisKiraSituation = 4
            me "I have no idea. We just met yesterday."
            scene ep1_home_vs_christalk with dissolve
            ch "Yeah, whatever comes, comes."
    ch "A toast for you man, and the new and improved you."
    scene ep1_home_vs_chrisdrink with dissolve
    me "Cheers."
else:
    ch "So... anything exiting happening yesterday after MaKenzie?"
    scene ep1_home_vs_chrisblink with dissolve
    me "Not really... unless..."
    scene ep1_home_vs_christalk with dissolve
    ch "Unless what."
    scene ep1_home_vs_chrisblink with dissolve
    me "I was out walking late at night yesterday."
    me "And as I'm about to pass the bus stop on 34th, I decide to take a little breather."
    me "But there's a woman there."
    scene ep1_home_vs_christalk with dissolve
    ch "Oh, hot chick?"
    scene ep1_home_vs_chrisblink with dissolve
    me "I mean. Yeah, sure, she was beautiful. But there was something off about her. Like she wasn't all there."
    me "So I decided to start my awkward small-talk routine, and somehow she eased down."
    scene ep1_home_vs_chrisdrink with dissolve
    me "And suddenly she opens up to me completely, and starts talking about everything."
    scene ep1_home_vs_chrisblink with dissolve
    me "But I think that somehow I prevented something bad from happening, right then and there."
    me "Some really dark shit."
    scene ep1_home_vs_christalk with dissolve
    ch "Well, you know me. I'm not especially good with emotions and feelings and whatnot."
    ch "But depression is real, and comes in so many shapes. Everyone seems to struggle in some way or another these days."
    ch "And nobody is handling it, because we're too busy posting perfect-pretty-pictures on social media of how good everything is."
    scene ep1_home_vs_chrisblink with dissolve
    me "For someone claiming to be not good with feelings Chris, I think you just aced that."
    scene ep1_home_vs_chrisdrink with dissolve
    ch "Let's drink to that."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_home_vs_stage2_2 with fade
$ clockis = [[todayIs],2,1,1,5]
ch "...then she says..."
ch "'maybe we should take a break'..."
ch "...and two days later she calls me and freaks out because I never call or visit her..."
scene ep1_home_vs_stage2_1 with dissolve
me "...women..."
scene ep1_home_vs_stage2_2 with dissolve
ch "Can't live with them..."
scene ep1_home_vs_stage2_1 with dissolve
me "...can't live without them..."
scene ep1_home_vs_stage2_3 with dissolve
$ renpy.pause()
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_home_vs_stage3_1 with fade
$ clockis = [[todayIs],2,1,4,8]
me "Chris, get your ass into gear. The taxi's already here. Meter's running."
scene ep1_home_vs_stage3_2 with dissolve
ch "But I just opened a new beer. I can't just {b}not{/b} drink it."
scene ep1_home_vs_stage3_1 with dissolve
me "Chug it or leave it."
scene ep1_home_vs_chrishold with dissolve
ch "..."
scene ep1_home_vs_chrisdrink with dissolve
$ renpy.pause()
me "But remember what happened last time you chugged."
ch "..."
scene ep1_home_vs_chrisdrinktoofast with dissolve
ch "..."
me "Oh boy."
scene ep1_home_vs_chrishold with dissolve
stop music fadeout 3
ch "I think I got it."
scene ep1_home_vs_christalk2 with dissolve
ch "I'm ready!"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep1_metronome
$ nowPlayingArtist = "FASSounds"
$ nowPlayingTitle = "Drop the Beat"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],2,2,3,3]
show ep1_lexi_performing_01
show ep1_lexi_curtain_still
show ep1_lexi_crowd2
show ep1_metro_chrisintro1
ch "Holy shit. We're really here!"
ch "This is awesome."
hide ep1_metro_chrisintro1
show ep1_metro_chrisintro3
me "So what's the plan."
hide ep1_metro_chrisintro3
show ep1_metro_christalk1
ch "First we'll need more to drink."
hide ep1_metro_christalk1
show ep1_metro_chrisintro3
me "Relax amigo. We just had a whole case of beer at my place."
hide ep1_metro_chrisintro3
show ep1_metro_christalk1
ch "Are you saying we're ready to go scout out the girls then?"
hide ep1_metro_christalk1
show ep1_metro_chrisintro3
me "Good point."
hide ep1_metro_chrisintro3
hide ep1_lexi_crowd2
hide ep1_lexi_curtain_still
hide ep1_lexi_performing_01
scene ep1_metro_bartender1 with dissolve
me "Some liquid courage for me and my friend, please."
scene ep1_metro_bartender2 with dissolve
bart "Two beer coming right up."
ch "I guess you get a lot of action as a bartender, eh?"
scene ep1_metro_bartender3 with dissolve
bart "Sir, this is a very serious establishment. I suggest you rethink your wording..."
show ep1_lexi_performing_01
show ep1_lexi_curtain_still
show ep1_lexi_crowd2
show ep1_metro_chrisbackoff
ch "..."
hide ep1_metro_chrisbackoff
hide ep1_lexi_crowd2
hide ep1_lexi_curtain_still
hide ep1_lexi_performing_01
scene ep1_metro_bartender4 with dissolve
bart "Of course I do!"
show ep1_lexi_performing_01
show ep1_lexi_curtain_still
show ep1_lexi_crowd2
show ep1_metro_chrisintro1
ch "*laughs* Damn, you got me there."
hide ep1_metro_chrisintro1
hide ep1_lexi_crowd2
hide ep1_lexi_curtain_still
hide ep1_lexi_performing_01
scene ep1_metro_bartender2 with dissolve
bart "This is the Metronome, my friend. We do more than the others, better than the others."
show ep1_lexi_performing_01
show ep1_lexi_curtain_still
show ep1_lexi_crowd2
show ep1_metro_chrisintro2
stop music fadeout 3
ch "This place is beyond cool."
ch "Cheers my friend."
me "Bottoms up."
hide ep1_metro_chrisintro2
hide ep1_lexi_crowd2
hide ep1_lexi_curtain_still
hide ep1_lexi_performing_01
play music ep1_lexi
$ nowPlayingArtist = "Lexi Dimante"
$ nowPlayingTitle = "Love Automatic"
$ nowPlayingRealArtist = "Katrina Stone"
$ nowPlayingRealTitle = "Love Automatic"
show ep1_lexi_performing
show ep1_lexi_curtain_move
show ep1_lexi_crowd
hide ep1_metro_christalk2
show ep1_metro_christalk1
ch "Oh. I love this song. It's the new one from Lexi."
me "Lexi who?"
hide ep1_metro_christalk1
show ep1_metro_christalk2
ch "You serious?"
me "..."
hide ep1_metro_christalk2
show ep1_metro_christalk1
ch "You must be the only person in the world that doesn't know who Lexi is."
ch "Lexi Dimante?"
ch "The hottest thing to walk this planet ever?"
hide ep1_metro_christalk1
show ep1_metro_christalk2
me "And who's that chick over there singing her song?"
hide ep1_metro_christalk2
show ep1_metro_christalk3
ch "..."
ch "OH MY GOD!"
hide ep1_metro_christalk3
show ep1_metro_christalk4
ch "That's Lexi Dimante singing the new one from Lexi Dimante!"
hide ep1_metro_christalk4
show ep1_metro_christalk5
ch "Eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeek!"
hide ep1_metro_christalk5
show ep1_metro_christalk6
me "Are you ok?"
hide ep1_metro_christalk6
show ep1_metro_christalk7
ch "I'm fan-girling so much right now."
hide ep1_metro_christalk7
show ep1_metro_christalk6
me "*laughs* Need a paper bag?"
hide ep1_metro_christalk6
show ep1_metro_christalk8
ch "{b}I LOVE YOU LEXI!{/b}"
hide ep1_metro_christalk8
show ep1_metro_christalk9
ch "{size=20}...marry me please...{/size}"
ch "Get..."
ch "...picture..."
ch "...my hands are shaking too much."
hide screen phone
show screen phone_camop
$ phone_camop_screen = "ep1_metro_lexi"
me "Sure thing."
label phonecamleximet_loop:
"Click on the phone or press '{b}[custom_phone_key]{/b}'."
jump phonecamleximet_loop
label photoop_ep1_lexi1:
hide ep1_lexi_performing
hide ep1_lexi_curtain_move
hide ep1_lexi_crowd
hide ep1_metro_christalk9
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexi_op1"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexi_op1 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause()
jump photoop_ep1_lexidone
label photoop_ep1_lexi2:
hide ep1_lexi_performing
hide ep1_lexi_curtain_move
hide ep1_lexi_crowd
hide ep1_metro_christalk9
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexi_op2"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexi_op2 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause()
jump photoop_ep1_lexidone
label photoop_ep1_lexidone:
show screen phone
$ phGallNotify = True
show ep1_lexi_performing
show ep1_lexi_crowd
show ep1_metro_christalk9
me "Got it."
ch "This is so cool. Let's just enjoy it for a little bit...."
$ renpy.pause()
stop music fadeout 3
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep1_metrointer
$ nowPlayingArtist = "Lexi Dimante"
$ nowPlayingTitle = "Lovely Piece"
$ nowPlayingRealArtist = "DayFox"
$ nowPlayingRealTitle = "Lovely Piece"
$ clockis = [[todayIs],2,3,2,8]
scene ep1_metro_afterlexi1 with fade
ch "Holy shit, that was intense."
scene ep1_metro_afterlexi2 with dissolve
me "Damn, that girl can perform."
scene ep1_metro_afterlexi3 with dissolve
ch "Right?"
ch "But I got to go drain the lizard. Hold my seat."
scene ep1_metro_bartender1 with dissolve
bart "She is really something, isn't she."
me "She sure is."
scene ep1_metro_bartender_running with dissolve
bart "Oh, got a situation here. Gotta run. I'll be right back."
scene ep1_metro_bar_empty with dissolve
me "(I have to think of a way to repay Chris for this evening.)"
me "(I'd forgotten how nice this was. Going out. Partying. Drinking.)"
bart "{size=20}I'm sorry ladies, but Miss Dimante will be back later.{/size}"
uk "{size=20}But I just wanted a selfie with her.{/size}"
bart "{size=20}She will be back a little later on.{/size}"
me "(I can't imagine how it is to be that famous, and everyone wanting a piece of you.)"
uk "Mind if I join you?"
me "Well..."
scene ep1_metro_bar_lexi01 with dissolve
me "..."
me "...of course not."
scene ep1_metro_bar_lexi03 with dissolve
le "Thank you."
scene ep1_metro_bar_empty with dissolve
me "(Holy shit.)"
me "(Ok now [name], stay calm...)"
me "(...the woman next to you is famous beyond all possibility, and just about the hottest thing alive...)"
scene ep1_metro_bar_lexi02 with dissolve
$ renpy.pause()
scene ep1_metro_bar_empty with dissolve
me "(...{b}the{/b} hottest thing alive.)"
me "(I should buy her a drink.)"
me "(Ok. Here goes. Deep breath...)"
scene ep1_metro_bar_lexi02 with dissolve
me "If you don't mind, I would like to offer you a drink. My treat."
le "..."
scene ep1_metro_bar_lexi03 with dissolve
le "You don't have to do that. I can pay for it myself."
scene ep1_metro_bar_lexi04 with dissolve
me "I'm sure you can. Although, let me have the pleasure of treating you."
le "..."
scene ep1_metro_bar_lexi02 with dissolve
le "Sure."
scene ep1_metro_bar_lexi_bartender2 with dissolve
me "Give me a good bottle of wine and two glasses to share, please."
me "{size=20}...not the most expensive bottle, I'm kinda on a budget here.{/size}"
scene ep1_metro_bar_lexi_bartender1 with dissolve
bart "Here you go. One excellent Chateau Brane Cantenac Margaux 2010 to share."
bart "{size=20}...ticking in at $119.{/size}"
me "{size=20}*hidden thumbs up* Perfect.{/size}"
scene ep1_metro_bar_lexi08 with dissolve
le "..."
scene ep1_metro_bar_lexi05 with dissolve
me "There we go."
scene ep1_metro_bar_lexi10 with dissolve
le "Let's hope you know your wine, and don't serve me any of that cheap crap."
me "*gulp*"
scene ep1_metro_bar_lexi11 with dissolve
le "Hmmm."
le "Best $119 wine I've ever had."
me "Oh... you heard."
scene ep1_metro_bar_lexi09 with dissolve
le "*laughs* Yes I did."
le "What do you think I am, some kind of spoiled rich bimbo?"
scene ep1_metro_bar_lexi_blink
me "Yeah, nerves got the best of me I guess."
scene ep1_metro_bar_lexi07 with dissolve
le "So how did you get access to the VIP-bar?"
le "You're not at all like the normal VIP-clientele."
scene ep1_metro_bar_lexi_blink
me "Oh... This is the VIP-bar? That explains a lot."
me "The nice view of the stage. The lack of people here. The superb bartender-service..."
bart "You're welcome."
me "...sharing a bottle of wine with Lexi."
scene ep1_metro_bar_lexi13 with dissolve
le "Well, that's on me. It's not a part of the vip-package."
le "But you're way more fun than the normal stiffs that think I am."
scene ep1_metro_bar_lexi_blink with dissolve
me "Yeah, this is not my normal routine... and come to think of it..."
scene ep1_metro_bar_lexi07 with dissolve
le "Hmmm?"
scene ep1_metro_bar_lexi_blink with dissolve
$ clockis = [[todayIs],2,3,4,2]
menu:
    "[M_01_030a]": # "Ask for a picture of the two of you":
        $ XPlexi += 10
        me "You probably get asked this all the time and are sick and tired of it, but do you mind taking a selfie with me?"
        scene ep1_metro_bar_lexi13 with dissolve
        le "Sure. Got to return that $119 bottle of wine favor."
        me "Let me set this up."
        play sound camerashutter
        $ cam_gallery_append_item1 = "ep1_metro_bar_selfie01"
        if cam_gallery_append_item1 not in cam_gallery:
            $ cam_gallery.append(cam_gallery_append_item1)
        show bg_empty
        scene ep1_metro_bar_selfie01 with Fade(0, 0, 0.5, color="#ffffff")
        $ renpy.pause()
        me "Approved."
        le "You look drunk though."
        me "Just slightly, and very happy."
        scene ep1_metro_bar_lexi07 with dissolve
        le "Are you here alone tonight?"
        scene ep1_metro_bar_lexi_blink with dissolve
        me "No, I'm here with my pal, Chris. He should return any second now."
        me "He's a huge fan of yours."
        scene ep1_metro_bar_lexi07 with dissolve
        le "What? You're not?"
        scene ep1_metro_bar_lexi_blink with dissolve
        me "I am now!"
    "[M_01_030b]": # "Ask her to take a picture with Chris":
        $ XPlexi += 5
        $ XPchris += 2
        $ ep1AskedLexiForChris = True
        me "The only reason I'm here today, is because my best friend got me the tickets."
        me "And you see... He absolutely adores you, and I wonder if you would want to take a picture with him when he returns? He should be here any minute."
        scene ep1_metro_bar_lexi07 with dissolve
        le "That is so sweet of you. Of course I'll do that."
        scene ep1_metro_bar_lexi_blink with dissolve
        me "I really appreciate it. There's a huge chance he will pass out though, but I'll deal with that if that happens."
        me "And he'll almost certainly say something insanely embarrasing in the process."
        scene ep1_metro_bar_lexi07 with dissolve
        le "I think I've heard just about everything from all kinds of people."
        scene ep1_metro_bar_lexi_blink with dissolve
        me "*laughs* You haven't met Chris yet."
scene ep1_metro_bar_lexi12 with dissolve
$ clockis = [[todayIs],2,3,4,9]
le "Is your friend by any chance wearing a ... suit of some kind?"
me "Sounds about right but..."
scene ep1_metro_bar_lexichris01 with dissolve
me "...yes, that's him."
me "Why are you standing over there, Chris?"
scene ep1_metro_bar_lexichris05 with dissolve
$ renpy.pause()
scene ep1_metro_bar_lexichris01 with dissolve
$ renpy.pause(0.5)
scene ep1_metro_bar_lexichris02 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_bar_lexichris03 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_bar_lexichris04 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_bar_lexichris05 with dissolve
le "Come on over."
scene ep1_metro_bar_chrisgreet1 with dissolve
le "I heard that you're quite the fan."
ch "You're Lexi..."
le "Yes, I am. Happy to meet you."
ch "{size=20}I'm so very happy to meet you too and nervous and I had this whole list of things I was going to say but I forgot them all and now the words are just rambling out of my mouth and I just might start crying for joy...{/size}"
scene ep1_metro_bar_chrisgreet2 with dissolve
le "[name] here just told me all about you."
ch "I'm sooo nervous..."
scene ep1_metro_bar_chrisgreet1 with dissolve
le "Don't be."
if ep1AskedLexiForChris:
    le "How about a picture?"
    ch "Of you and me?"
    le "If you want to of course."
    ch "Yes, that would be fantastic."
    scene ep1_metro_bar_chrisgreet2 with dissolve
    le "[name], would you do the honors?"
    me "Of course."
    play sound camerashutter
    $ cam_gallery_append_item1 = "ep1_metro_bar_selfie03"
    if cam_gallery_append_item1 not in cam_gallery:
        $ cam_gallery.append(cam_gallery_append_item1)
    show bg_empty
    scene ep1_metro_bar_selfie03 with Fade(0, 0, 0.5, color="#ffffff")
    $ renpy.pause()
else:
    le "You enjoying the show?"
    ch "Absolutely. You're killing it."
    ch "..."
    ch "I'm holding on to your hand for way to long, aren't I."
    le "Probably."
    ch "I need a drink."
scene ep1_metro_bar_lexi12 with dissolve
uk "Miss Dimante, they are expecting you on stage now."
scene ep1_metro_bar_lexi07 with dissolve
le "That's my cue, I'm afraid. Breaks are small and rare in this profession."
le "But thank you [name], for being a normal person, and for treating me like one as well."
le "...and for sharing a glass of your wonderful wine."
scene ep1_metro_bar_lexi05 with dissolve
le "You too, Chris. Was nice meeting you. Short but sweet."
scene ep1_metro_bar_lexi07 with dissolve
le "So, do I look ready?"
scene ep1_metro_bar_lexi_blink with dissolve
menu:
    "[M_01_031a]": # "Beautiful":
        $ XPlexi += 2
        $ saidLexiWasBeautiful = True
        me "You look beautiful."
        scene ep1_metro_bar_lexileaving2 with dissolve
        le "..."
    "[M_01_031b]": # "Joke":
        $ XPlexi += 1
        me "Approved. But your hair is all over the place."
        scene ep1_metro_bar_lexileaving1 with dissolve
        le "Damn hair..."
scene ep1_metro_bar_facedesk1 with dissolve
$ contact_lexi = True
$ contact_notify_me = True
$ contact_text_me += "\n\nAt the Metronome I met Lexi. We shared a bottle of wine and talked for a little while. She was a very down to earth kind of popstar."
$ contact_notify_lexi = True
$ contact_text_lexi += "\n\nI met her at the Metronome. We shared a bottle of wine and talked for a little while. She liked my company and thought I was cute."
$ chat_lexi_item = "2;0;801;New contact added"
if chat_lexi_item not in chat_lexi:
    $ chat_lexi.append(chat_lexi_item)
$ todayIs = 3
$ clockis = [[todayIs],0,0,0,4]
ch "My life is complete."
ch "Nothing will ever top this."
me "You'll be fine."
stop music fadeout 3
me "If I get you another beer, will that top this?"
ch "...maybe."
play music ep1_bowling
$ nowPlayingArtist = "Lexi Dimante"
$ nowPlayingTitle = "Crazy"
$ nowPlayingRealArtist = "Lance Conrad"
$ nowPlayingRealTitle = "Born to Drive Me Crazy"
me "..."
me "And Lexi's on the stage again..."
scene ep1_metro_bar_empty
show ep1_lexi_performing
show ep1_lexi_crowd
show ep1_metro_christalk3
ch "Hell yeah!"
hide ep1_metro_christalk3
show ep1_metro_christalk9
$ renpy.pause()
hide ep1_metro_christalk9
show ep1_metro_chrisintro2
ch "Let's go dance and pick up some girls. You game?"
me "After you, sensei."
me "Just want to close my tab before we get down there."
hide ep1_metro_chrisintro2
hide ep1_lexi_crowd
hide ep1_lexi_performing
scene ep1_metro_bartender1 with dissolve
bart "Your tab is settled. You don't owe me anything for the whole evening."
me "But how..."
scene ep1_metro_bartender2 with dissolve
bart "Lexi slipped me her card while you weren't watching."
me "And tip?"
bart "Also settled. Handsomely I might add."
me "(wow...)"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_metro_lexiperforming_dance1 with fade
me "These?"
scene ep1_metro_lexiperforming_dance0 with dissolve
ch "Go for it man..."
scene ep1_metro_lexiperforming_dance1 with dissolve
me "Holy shit, this is great."
scene ep1_metro_lexiperforming_me1 with dissolve
me "{b}GOGO LEXI!{/b}"
scene ep1_metro_lexiperforming_me2 with dissolve
hide screen phone
show screen phone_camop
$ phone_camop_screen = "ep1_photoop_lexiperform"
$ renpy.choice_for_skipping()
me "If I'm quick, I can get a picture."
jump photoop_ep1_lexiperf_done
label photoop_ep1_lexiperf1:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexiperforming_op4"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexiperforming_op4 with Fade(0, 0, 0.5, color="#ffffff")
me "Damn crowd pushing me all over the place."
jump photoop_ep1_lexiperf_done
label photoop_ep1_lexiperf2:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexiperforming_op3"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexiperforming_op3 with Fade(0, 0, 0.5, color="#ffffff")
me "Good picture."
jump photoop_ep1_lexiperf_done
label photoop_ep1_lexiperf3:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexiperforming_op2"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexiperforming_op2 with Fade(0, 0, 0.5, color="#ffffff")
me "Oh well, at least it's memorable in some way..."
jump photoop_ep1_lexiperf_done
label photoop_ep1_lexiperf4:
play sound camerashutter
$ cam_gallery_append_item1 = "ep1_metro_lexiperforming_op1"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep1_metro_lexiperforming_op1 with Fade(0, 0, 0.5, color="#ffffff")
me "Ok, that wasn't even close."
jump photoop_ep1_lexiperf_done
label photoop_ep1_lexiperf_done:
scene ep1_metro_lexiperforming_dance1 with dissolve
hide screen phone_camop
$ phone_camop_screen = ""
show screen phone
ch "Everything is perfect..."
ch "...the sounds ... the feeling..."
scene ep1_metro_dancing_01 with dissolve
me "...even that smell..."
me "...rose..."
scene ep1_metro_dancing_02 with dissolve
me "...jasmine..."
me "..."
scene ep1_metro_dancing_03 with dissolve
me "No..."
me "...it can't be."
scene ep1_metro_dancing_04 with dissolve
me "..."
scene ep1_metro_dancing_05 with dissolve
$ renpy.pause(0.5)
scene ep1_metro_dancing_06 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_dancing_08 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_dancing_09 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_dancing_10 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_metro_dancing_11 with Dissolve(0.25, alpha=True)
$ renpy.pause()
scene ep1_metro_dancing_10 with Dissolve(0.25, alpha=True)
"My place..."
"Now!"
$ stephClosure = False
$ stephRejected = False
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_metro_chrishunt_d02 with fade
ch "[name], these girls want a word with you."
scene ep1_metro_chrishunt_d01 with dissolve
ch "[name]?"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep1_metro_chrishunt_b01 with fade
ch "Did you happen to see where my friend went?"
bart "I saw him leave with a curly haired woman in a red dress a few minutes ago. If you hurry, you might catch up with him."
ch "Left? He would never do that."
ch "Wait... Curly hair?"
ch "Let me find a picture on my phone."
scene ep1_metro_chrishunt_b02 with dissolve
ch "Is this is the woman he left with?"
bart "That does indeed resemble her strongly, yes."
scene ep1_metro_chrishunt_done with dissolve
$ phContNotify = True
$ contact_notify_chris = True
$ contact_text_chris += "\n\nWe went to the Metronome and had a good time. I ran into Stephanie, and left with her without telling him. I wonder what he felt about that."
$ contact_notify_me = True
$ contact_text_me += "\n\nI went to the Metronome with Chris and had a good time. I ran into Stephanie, and left with her."
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nI met her at the Metronome. Saw her, and the whole world faded away. I think she felt it like that aswell, because we left immediately."
ch "Fuck..."
$ renpy.pause()
stop music fadeout 3
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
label stephlewd:
$ clockis = [[todayIs],0,0,4,9]
play music ep1_stephlewd
$ nowPlayingArtist = "SLPSTRM"
$ nowPlayingTitle = "Believe the Hype"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
show ep1_steph_app_intro_bg at imgSlideH1_bg
show ep1_steph_app_intro_painting at imgSlideH1_sp
show ep1_steph_gettinghot1 at imgSlideH1
me "Steph..."
menu:
    "[M_01_032a]": # "We need to talk...":
        jump StephSlider2
    "[M_01_032b]": # "I love you":
        $ ep1ToldStephLove = True
        jump StephSlider2
label StephSlider2:
hide screen phone
hide ep1_steph_app_intro_bg
show ep1_steph_app_intro_bg at imgSlideH2_bg
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideH2_sp
show ep1_steph_gettinghot2 at imgSlideH2 with Dissolve(0.25, alpha=True)
hide ep1_steph_gettinghot1
st "Shhh..."
st "After...but now I need you."
menu:
    "[M_01_033a]" if not ep1ToldStephLove: # "Stop her..." if not ep1ToldStephLove:
        $ stephRejected = True
        jump StephSlider3
    "[M_01_033b]": # "Give in":
        jump StephSlider4
label StephSlider3:
hide ep1_steph_gettinghot2
show ep1_refuse_steph01 with Dissolve(0.25, alpha=True)
me "No Steph! I'm serious."
me "Two years ago you suddenly disappeared."
me "Not a word, no hint, no rational or even irrational explanation - no nothing."
hide ep1_steph_app_intro_bg
show ep1_steph_app_intro_bg at imgSlideH3_bg
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideH3_sp
show ep1_refuse_steph02 at imgSlideH3 with Dissolve(0.25, alpha=True)
hide ep1_refuse_steph01 with Dissolve(0.25, alpha=True)
st "Don't ruin the mood now."
st "We'll have plenty of time to talk after..."
hide ep1_steph_app_intro_bg
show ep1_steph_app_intro_bg at imgSlideH4_bg
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideH4_sp
show ep1_refuse_steph03 with Dissolve(0.25, alpha=True)
hide ep1_refuse_steph02
$ renpy.pause(0.15)
hide ep1_refuse_steph03
show ep1_refuse_steph04 at imgSlideH4 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.10)
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideHD_sp with hpunch
me "Listen to me."
me "Do you know how much pain and suffering you caused me?"
me "2 years, and now you act like you never left at all."
hide ep1_refuse_steph04
show ep1_refuse_steph05 with Dissolve(0.25, alpha=True)
st "Dammit [name]."
st "I would have told you if I could."
hide ep1_refuse_steph05
show ep1_refuse_steph06 with Dissolve(0.25, alpha=True)
me "..."
hide ep1_refuse_steph06 with Dissolve(0.25, alpha=True)
show ep1_refuse_steph07 with Dissolve(0.25, alpha=True)
st "..."
scene ep1_steph_walkaway01 with dissolve
st "[name]?"
me "I was searching your eyes for some kind of..."
me "...empathy...emotion...anything..."
me "...but realized I was looking at a complete stranger."
menu:
    "[M_01_034a]": # "Emotionless goodbye":
        me "Goodbye Steph."
        jump StephSlider41
    "[M_01_034b]": # "Closure":
        $ stephClosure = True
        me "Thank you for the closure."
        jump StephSlider41
label StephSlider41:
scene ep1_steph_walkaway02 with dissolve
st "Don't walk out on me."
st "I did what I did to save you!"
st "[name]?"
scene ep1_steph_walkaway03 with dissolve
st "[name]!"
scene ep1_steph_walkaway04 with dissolve
me "..."
if meSporty >= 2:
    show ep1_steph_shoeinc at imgSlideShoeCatch
    $ renpy.pause(0.25)
    scene ep1_steph_walkaway06
    hide ep1_steph_shoeinc
    stop music fadeout 3
    show screen sshw with dissolve
    me "Throwing shoes now? Really?"
    hide screen sshw with dissolve
else:
    show ep1_steph_shoeinc at imgSlideShoe
    $ renpy.pause(0.25)
    scene ep1_steph_walkaway05
    hide ep1_steph_shoeinc
    stop music fadeout 3
    me "..."
    scene ep1_steph_walkaway07 with dissolve
    me "Throwing shoes now? Really?"
scene ep1_steph_walkaway08 with dissolve
st "{size=20}...I'm sorry.{/size}"
jump afterStephPlaceAlt
label StephSlider4:
hide ep1_steph_app_intro_bg
show ep1_steph_app_intro_bg at imgSlideH3_bg
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideH3_sp
show ep1_steph_gettinghot3 at imgSlideH3 with Dissolve(0.25, alpha=True)
hide ep1_steph_gettinghot2
st "I've waited for this for so long..."
st "...your touch, your lips, your..."
hide ep1_steph_app_intro_bg
show ep1_steph_app_intro_bg at imgSlideH4_bg
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideH4_sp
show ep1_steph_gettinghot4 at imgSlideH4 with Dissolve(0.25, alpha=True)
hide ep1_steph_gettinghot3
$ renpy.pause(0.25)
hide ep1_steph_app_intro_painting
show ep1_steph_app_intro_painting at imgSlideHD_sp with hpunch
me "(That smell.)"
me "(So wonderfully overwhelming.)"
me "(God, I've missed her.)"
hide ep1_steph_app_intro_bg
hide ep1_steph_app_intro_painting
hide ep1_steph_gettinghot4
label StephSlider05:
show ep1_steph_seduce_bg at imgSlide05_bg
show ep1_steph_seduce at imgSlide05
$ renpy.pause()
hide ep1_steph_seduce_bg
hide ep1_steph_seduce
scene ep1_steph_hand with dissolve:
    size (config.screen_width, config.screen_height)
$ renpy.pause()
scene bg empty
scene ep1_steph_ask with dissolve
label ep1StephLewdSelector1:
menu:
    "[M_01_035a]": # "Keep stroking...":
        scene ep1_steph_hand with dissolve:
            size (config.screen_width, config.screen_height)
        $ renpy.pause()
        jump ep1StephLewdSelector1
    "[M_01_035b]": # "Lose the panties":
        jump ep1StephLewdSelector2
label ep1StephLewdSelector2:
scene bg empty with fade
scene ep1_steph_leg1 with dissolve
st "Those panties looked good on me though."
scene ep1_steph_leg2 with Dissolve(0.25, alpha=True)
$ renpy.pause(0.5)
scene ep1_steph_leg3 with Dissolve(0.25, alpha=True)
me "You look damn good without them too."
scene ep1_steph_standing:
    size (config.screen_width, config.screen_height)
$ renpy.pause()
label ep1StephLewdSelector3:
menu:
    "[M_01_036a]": # "Keep going...":
        scene ep1_steph_standing:
            size (config.screen_width, config.screen_height)
        $ renpy.pause()
        jump ep1StephLewdSelector3
    "[M_01_036b]": # "Move to the couch":
        jump ep1StephLewdSelector4
label ep1StephLewdSelector4:
scene ep1_steph_lewd_behind1 with dissolve
me "You're perfect."
scene ep1_steph_lewd_behind4a with Dissolve(0.1, alpha=True)
st "Shut up and fuck me."
scene ep1_steph_lewd_behind1 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep1_steph_lewd_behind2 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep1_steph_lewd_behind3 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep1_steph_lewd_behind4 with Dissolve(0.1, alpha=True)
$ renpy.pause()
scene ep1_steph_lewd_behind1a with Dissolve(0.1, alpha=True)
$ renpy.pause(0.25)
scene ep1_steph_lewd_behind2a with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep1_steph_lewd_behind3a with Dissolve(0.1, alpha=True)
st "Oh, fuck yeah."
scene ep1_steph_behind:
    size (config.screen_width, config.screen_height)
$ renpy.pause()
label ep1StephLewdSelector5:
menu:
    "[M_01_037a]": # "Keep going...":
        scene ep1_steph_behind:
            size (config.screen_width, config.screen_height)
        $ renpy.pause()
        jump ep1StephLewdSelector5
    "[M_01_037b]": # "Turn around":
        jump ep1StephLewdSelector6
label ep1StephLewdSelector6:
scene bg empty with fade
scene ep1_steph_legup with dissolve
st "You've been working out."
scene ep1_steph_laying:
    size (config.screen_width, config.screen_height)
$ renpy.pause()
label ep1StephLewdSelector7:
menu:
    "[M_01_038a]": # "Keep going...":
        scene ep1_steph_laying:
            size (config.screen_width, config.screen_height)
        $ renpy.pause()
        jump ep1StephLewdSelector7
    "[M_01_038b]": # "Move on? (end scene)":
        jump ep1StephLewdEnd
label ep1StephLewdEnd:
scene ep1_steph_resist5 with fade
$ clockis = [[todayIs],0,1,3,2]
st "You're grinding ... the right spot ... perfectly."
inte "Steph. You home?"
scene ep1_steph_resist1 with dissolve
st "Oh, fucking hell."
st "We have to stop, right now."
inte "Never mind. I found the spare keys."
menu:
    "[M_01_039a]": # "Continue":
        me "I don't care who that is. There's no way I'm stopping."
        scene ep1_steph_resist2 with dissolve
        st "I'm not kidding, get the fuck off me."
        menu:
            "[M_01_040a]": # "Continue":
                $ ep1StephOrg = True
                $ meSporty += 1
                show screen slvl with dissolve
                me "No fucking chance, deal with it!"
                hide screen slvl with dissolve
                inte "*keys turning the lock*"
                st "Get the ..."
                scene ep1_steph_resist3 with dissolve
                st "... fuck ... I'm ..."
                scene ep1_steph_resist4 with dissolve
                st "...cumming!"
                scene ep1_steph_resist4 with Fade(0, 0, 0.5, color="#ffffff")
                st "*hnghah*"
                scene ep1_steph_resist5 with dissolve
                st "*exhales* ... have ... to ... go ..."
                st "Please..."
                scene ep1_steph_resist6 with dissolve
                st "He'll kill you ... my husband."
                inte "*door opens* Honey?"
                jump quitSteph
            "[M_01_040b]": # "Stop":
                $ meFlirty += 1
                show screen flvl with dissolve
                me "Fuck..."
                hide screen flvl with dissolve
                scene ep1_steph_resist2 with dissolve
                st "You have to get out of here this instant. It's my husband, he'll kill you."
                inte "*door opens* Honey?"
                jump quitSteph
    "[M_01_039b]": # "Stop":
        $ meRomantic += 1
        show screen rlvl with dissolve
        me "Shit."
        hide screen rlvl with dissolve
        scene ep1_steph_resist2 with dissolve
        st "You have to get out of here this instant. It's my husband, he'll kill you."
        inte "*door opens* Honey?"
        jump quitSteph
label quitSteph:
scene ep1_steph_escape01 with dissolve
me "Dafuq?"
me "Husband?"
st "I give it 12 seconds before he comes through that door."
st "Jump out the window, {b}now{/b}!"
scene ep1_steph_escape02 with dissolve
st "I'll be right there, Melvin honey. Hang on a sec."
ml "Don't worry sweetheart. I'll be right up."
me "It's fucking two stories down to the ground."
st "You'll survive. Might break a leg, but you won't survive him."
if ep1StephOrg:
    st "Fucking orgasm, my legs are all jelly."
ml "*stomps up stairs* We have visitors? I hear voices."
st "It's just the tv."
$ renpy.end_replay()
scene ep1_steph_escape03 with dissolve
me "{size=20}My clothes.{/size}"
st "{size=20}I got that.{/size}"
stop music fadeout 3
scene ep1_steph_escape04 with fade
st "{size=20}Here...{/size}"
st "{size=20}...and...{/size}"
st "{size=20}...I'm sorry.{/size}"
scene ep1_steph_escape05 with fade
st "Hey hun."
ml "What the hell?"
st "{size=22}...{/size}"
ml "{size=20}You're naked.{/size}"
st "{size=18}So what. It's not like you haven't seen me naked before.{/size}"
me "(I'm getting out of here.)"
jump afterStephPlace
label afterStephPlaceAlt:
play music ep1_lastwalk
scene ep1_walk_05 with fade
show screen phone_nobatt
$ clockis = [[todayIs],0,1,2,1]
$ contact_notify_me = True
$ contact_text_me += "\n\nAt her place, I rejected her advances and confronted her. I never got an answer and left."
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nAt her place, I rejected her advances and confronted her. She didn't have an answer and I left."
me "(Why do I always lose all sense of myself when I see Steph.)"
me "(Aimlessly following her every command. Maybe I thought there would be some answers.)"
me "(She's nothing like the fantastic woman she once used to be.)"
me "(I even left Chris without a word. I need to call him.)"
show screen phone_full_nobatt
me "..."
me "(Fuck.)"
jump afterStephBus
label afterStephPlace:
play music ep1_lastwalk
scene ep1_walk_03 with fade
show screen phone_nobatt
$ clockis = [[todayIs],0,1,3,2]
$ contact_notify_me = True
$ contact_text_me += "\n\nAt her place, we fucked. Until her husband came home."
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nAt her place, we fucked. Until her husband came home."
me "Shit, shit, shit."
me "(At least I didn't break my legs. All good, if you don't count blue balls.)"
me "(Why do I always lose all sense of myself when I see Steph.)"
me "(And when did she get back? I have so many questions.)"
scene ep1_walk_01 with dissolve
me "(...and why did I even go with her?)"
me "(I need to call Chris.)"
show screen phone_full_nobatt
me "..."
me "(Fuck.)"
scene ep1_walk_02 with dissolve
me "(At least all my clothes are here. I should head home, or back to Metro, or... I don't know what to do.)"
scene ep1_walk_04 with dissolve
me "(Her shoe. It must have been tangled into my clothes.)"
scene ep1_walk_05 with dissolve
me "..."
jump afterStephBus
label afterStephBus:
scene ep1_street_walk0 with fade
me "(The bus stop. I should walk by the bus stop.)"
scene ep1_street_walk1 with dissolve
me "(Maybe she's here...)"
scene ep1_street_nocece1 with dissolve
me "(Oh...)"
me "(...she's not here.)"
scene ep1_street_bench with dissolve
me "(What am I doing. Did I walk here just for her?)"
scene ep1_bench_sequel01 with dissolve
me "(...some part of me definitely wanted to go here...)"
me "(...it's not even on my way home.)"
scene ep1_bench_sequel02 with dissolve
me "(Would have been nice to see her again, though.)"
me "(I'll try coming back here tomorrow.)"
scene ep1_bench_sequel01 with dissolve
me "(I guess it's time to head home. I really need to clear my head. Fix my mess.)"
scene ep1_bench_sequel03 with dissolve
if stephRejected:
    me "(It's kinda funny... I hope to see her again for years, then I walk out of ... probably the fuck of my life.)"
else:
    me "(Come to think about it. Steph married a guy named Melvin. That is kinda funny.)"
me "(Yep, I'm definitely tired...)"
scene ep1_bridge1 with fade
me "(I'll call Chris once I get home.)"
scene ep1_bridge2 with dissolve
me "(Hopefully he's not too pissed at me.)"
uk "*humming a tune*"
me "Hmm?"
scene ep1_bridge_cece01 with fade
me "(Oh shit. There's somebody there.)"
me "(Wait ... that's...)"
me "Cece?"
scene ep1_bridge_cece02 with dissolve
$ renpy.pause()
scene ep1_bridge_cece03 with dissolve
ce "Hmm?"
scene ep1_bridge_cece05 with dissolve
ce "[name]?"
scene ep1_bridge_cece06 with dissolve
ce "Stop, please."
scene ep1_bridge_cece05 with dissolve
me "(No, tell me this isn't what I think it is.)"
me "What's going on?"
scene ep1_bridgecece_02 with dissolve
ce "I'm just enjoying this nice moment."
ce "I hope you want to enjoy it with me?"
scene ep1_bridgecece_01 with dissolve
me "Please, get down from there so we can talk properly?"
scene ep1_bridgecece_07 with dissolve
me "It's got to be 50 meters down, and those shoes are not meant for rail climbing."
scene ep1_bridgecece_04 with dissolve
ce "62.5 meters."
scene ep1_bridgecece_06 with dissolve
ce "And they are nice shoes. My friend bought them for me."
scene ep1_bridgecece_02 with dissolve
me "She must be worried sick about you now."
me "Are you drunk?"
scene ep1_bridgecece_03 with dissolve
ce "Sure..."
ce "And I took some pills."
ce "I think they were sleeping pills."
scene ep1_bridgecece_05 with dissolve
ce "I'm just so tired."
me "Careful..."
scene ep1_bridgecece_04 with dissolve
me "Please come down from there, Cece."
scene ep1_bridgecece_05 with dissolve
ce "No!"
ce "Don't you see? There's nothing for me on that part of the fence."
ce "I am going to go this way."
scene ep1_bridgecece_01 with dissolve
me "I'm certain there's nothing good for you on that other part of the fence either."
me "At least on this side, you have me."
scene ep1_bridge_cece07 with dissolve
ce "Are you trying to convince me you actually care?"
ce "Nobody cares!"
ce "I've seen you for 15 minutes in my life."
scene ep1_bridgecece_01 with dissolve
me "I do care. At least I think I do. Because I thought about you earlier today."
me "And for some reason..."
scene ep1_bridgecece_02 with dissolve
me "...I went to our special bus-stop today just now, looking for you."
scene ep1_bridge_cece_fin01 with dissolve
ce "..."
ce "You're a good guy, [name]. I really think so."
ce "And a part of me is very happy you were the last thing I laid eyes on in this life."
me "...please."
scene ep1_bridge_cece_fin02 with dissolve
ce "You have a very soothing voice. And a very sweet smile."
ce "But I am so tired of everything. So very very tired."
ce "And it's time for me to go to sleep now."
scene ep1_bridge_cece_fin03 with dissolve
ce "Good night [name]."
me "{b}No!{/b}"
scene ep1_bridge_cece_fin04 with dissolve
me "(You always hear stories...)"
scene ep1_bridge_cece_fin05 with dissolve
me "(...of when you're forced to act quickly and by instinct...)"
scene ep1_bridge_cece_fin06 with dissolve
me "(...it's the same thing; 'It was like time was standing still'...)"
scene ep1_bridge_cece_fin07 with dissolve
me "(...and that's really the truth, even though everything happened at once...)"
scene ep1_bridge_jumpgrip1 with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_bridge_jumpgrip2 with Dissolve(0.5, alpha=True)
$ renpy.pause(0.5)
scene ep1_bridge_jumpgrip3 with Dissolve(0.5, alpha=True)
me "{b}Got ya!{/b}"
scene ep1_bridge_jumpgrip5 with dissolve
ce "No."
scene ep1_bridge_jumpgrip4 with dissolve
ce "Why."
me "There is nothing for you down there."
scene ep1_bridge_jumpgrip5 with dissolve
me "I am not letting go. But I can't lift you up either, unless you help me."
me "Let me help you up! Grab my hand please."
me "Please..."
me "...trust me."
scene ep1_bridge_jumpgrip6 with Dissolve(1.5, alpha=True)
ce "..."
scene ep1_ending1 with fade
stop music fadeout 5
ce "You don't have to hold me. I'm fine now."
me "I'm not letting you go."
scene ep1_ending2 with dissolve
ce "Not complaining. Feels like a good hug."
hide screen phone_nobatt
scene ep1_ending3 with dissolve
$ contact_notify_me = True
$ contact_text_me += "\n\nWhile heading home from Stephanie, I went past the bus-stop looking for Cece. She wasn't there."
$ contact_text_me += "\n\nBut I saw her on the bridge. She told me she was ending her life, and jumped. I saved her."
$ contact_notify_cece = True
$ contact_text_cece += "\n\nI saw her on the bridge. She told me she was ending her life, and jumped. I saved her."
ce "{size=22}Thank you...{/size}"
play music ep1_afterburger
scene ep1_titlescreen with Dissolve(2.5, alpha=True)
$ renpy.pause(2.5)
scene ep1_ending with Dissolve(2.5, alpha=True)
$ renpy.pause(2.5)

show screen ep1_endscreen
$ renpy.pause()
label ch1End:
hide screen ep1_endscreen
$ renpy.pause(0.5)
$ renpy.pause(0.5)
stop music fadeout 3
scene bg empty with fade
$ renpy.pause(2)
$ renpy.pause(2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

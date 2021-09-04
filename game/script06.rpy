label ch6Start:
call MenuRefresh
if persistent.chapter6 is None:
    $ persistent.chapter6 = True

if ep4SetupChrisWith == 3:
    $ phone_task_append_item1 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris needs your help;1"
    $ phone_task_append_item2 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris and Robin, sitting in a tree...?;2"
    if phone_task_append_item1 in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if ep4SetupChrisWithLi:
    $ phone_task_append_item1 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris needs your help;1"
    $ phone_task_append_item2 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris and Linda, sitting in a tree...?;2"
    if phone_task_append_item1 in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if ep4SetupChrisWith == 4:
    $ phone_task_append_item1 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris needs your help;1"
    $ phone_task_append_item2 = "10;9;2;3;5;9;Chris;Set Chris up with someone before;Chris and Holly, sitting in a tree...?;2"
    if phone_task_append_item1 in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
$ todayIs = 12
$ clockis = [[todayIs],0,9,0,0]
$ phone_camop_screen = ""
stop music fadeout 3
scene bg empty
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_prologue
$ nowPlayingArtist = "Chris Mason"
$ nowPlayingTitle = "Piece of My Heart"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_prologue01 with fade
ce "..."
scene ep6_prologue02 with dissolve
ce "(Don't...)"
scene ep6_prologue03 with dissolve
ce "(Not now...)"
scene ep6_prologue04 with dissolve
ce "(Not when they are here...)"
scene ep6_prologue05 with dissolve
ce "(Another day...)"
scene ep6_prologue06 with dissolve
ce "(Okay?)"
scene ep6_prologue07 with dissolve
"*giggles*"
scene ep6_prologue08 with dissolve
ce "Huh?"
scene ep6_prologue09 with dissolve
ce "What the heck are you doing?"
ls "Uhm..."
scene ep6_prologue10 with dissolve
ls "Looking... out... for... you... and..."
scene ep6_prologue11 with dissolve
ls "..."
scene ep6_prologue10 with dissolve
ls "...making... sure... you're... okay?"
scene ep6_prologue12 with dissolve
ce "Well, sit your ass down then and don't stand there like a dork."
scene ep6_prologue13 with dissolve
ce "And how many times have I told you to knock before you come into my room?"
scene ep6_prologue14 with dissolve
ls "But I did knock."
ls "Just like you always say."
scene ep6_prologue15 with dissolve
ls "I knocked three times."
ls "But there was no reply."
ls "Then I knocked three more times."
ls "And still nothing."
scene ep6_prologue16 with dissolve
ls "Then I entered, and went 'Hi Cece'"
scene ep6_prologue17 with dissolve
ls "But you just sat there in your own thoughts like Buddha, meditating or some shit like that."
ce "Hey, no swearing."
ls "Ok, Ghandi."
scene ep6_prologue18 with dissolve
ce "Aaaaaaaaaaaa..."
scene ep6_prologue19 with dissolve
ce "...tchooo!"
ls "God bless."
scene ep6_prologue20 with dissolve
ce "Thank you."
scene ep6_prologue21 with dissolve
ce "So, what kind of shenanigans have you been up to lately."
ls "You are so judgemental, you know that?"
scene ep6_prologue22 with dissolve
ce "I just know you, and you did not just stand here because you thought I was Buddha."
scene ep6_prologue23 with dissolve
ls "So judgemental."
ce "Am not."
ls "Are too."
scene ep6_prologue22 with dissolve
ls "I just care about my dorky big sister. Is that not allowed?"
scene ep6_prologue21 with dissolve
ce "Sure, I'll let it slide this time."
scene ep6_prologue22 with dissolve
ls "I'm just a caring little..."
scene ep6_prologue24 with dissolve
ce "Aaaaaaaaa..."
ls "...sister."
scene ep6_prologue25 with dissolve
ce "...tchooo!"
ls "..."
scene ep6_prologue26 with dissolve
ls "God bless."
ce "Thank you..."
ce "...again."
scene ep6_prologue27 with dissolve
ce "What's wrong with me. Why do I keep sneezing?"
scene ep6_prologue28 with dissolve
ls "You're probably getting a cold."
ls "So now you can't move out until you know that you're 100%% okay."
scene ep6_prologue29 with dissolve
ce "We've already had this talk, sis."
scene ep6_prologue30 with dissolve
ce "I can't stay here. For reasons you... can't understand yet."
ce "It's better for everybody if I go away for a bit."
scene ep6_prologue31 with dissolve
ce "I'm terrified that I'll do some dumb shit that will affect you in some way."
ce "And you'll end up remembering that for the rest of your life."
scene ep6_prologue32 with dissolve
ce "Or maybe you would get ideas. Ideas that you shouldn't even know exist."
ce "So it's best if I move out."
scene ep6_prologue33 with dissolve
ce "Me and Linda are going to move to the city and find us a place there."
ce "It's about time I moved out anyway. I'm not 10 anymore."
scene ep6_prologue34 with dissolve
ce "But I'll send a message to you every day."
ce "..."
scene ep6_prologue48 with dissolve
ce "Have mom and dad said anything?"
scene ep6_prologue35 with dissolve
ls "Mom is crying and going on with the 'my little girl is moving out' thing."
scene ep6_prologue47 with dissolve
ce "And dad?"
ls "Same. But more in the 'I got something stuck in my eye' type of crying."
scene ep6_prologue33 with dissolve
ce "And bro?"
scene ep6_prologue35 with dissolve
ls "He's just happy you're moving out. Now he thinks he'll get your room so we won't have to share anymore."
ls "But this room is mine!"
scene ep6_prologue36 with dissolve
ce "If you're going to fight over it, then I want to watch."
scene ep6_prologue37 with dissolve
ce "Aaaaaaaaa..."
scene ep6_prologue38 with dissolve
ce "...thooooo!"
ls "God bless."
scene ep6_prologue39 with dissolve
ce "Thank you."
ls "And wow..."
scene ep6_prologue40 with dissolve
ce "Huh?"
ls "That booger came flying out your nose at a hundred miles an hour."
scene ep6_prologue41 with dissolve
ce "No way!"
ls "Way!"
ls "It flew right out the window."
ls "Beware of flying boogers."
scene ep6_prologue42 with dissolve
ce "That is so gross and cool at the same time."
scene ep6_prologue43 with hpunch
ls "I'm going to miss you."
ce "..."
scene ep6_prologue44 with dissolve
ce "I'm going to miss you too, sis. So much."
scene ep6_prologue45 with dissolve
ls "And you said shit too."
ce "I know. I'm horrible."
ls "I love you!"
ce "I love you too."
ce "Even if I know you're just saying it so that I will let you get the room."
ls "..."
ls "Maybe..."
scene ep6_prologue46 with dissolve
ce "..."
ce "Sis?"
ls "Yes?"
scene ep6_prologue50 with dissolve
ce "Why is there a pepper shaker next to your foot?"
ls "Eh..."
scene ep6_prologue49 with dissolve
ls "Because I thought you were maybe eating a sandwich and..."
ls "...needed some pepper on it and..."
scene ep6_prologue50 with dissolve
ls "...I wanted to be the good sister and bring you some..."
scene ep6_prologue51 with dissolve
ce "So... 'good sister'..."
scene ep6_prologue52 with dissolve
ls "Hmm?"
scene ep6_prologue53 with dissolve
ce "Did you by any chance put a lot of pepper in my hair so I would sneeze a lot?"
ls "Ehmmm..."
ce "I hope you've warmed up, because I am going to..."
scene ep6_prologue54 with dissolve
ce "...kill you!"
ls "No, no. Moooooom... Daaaaaad..."
scene ep6_prologue55 with dissolve
lb "Jeez, will you watch it!"
ls "Heeeelp..."
ce "You are so dead!"
scene ep6_prologue56 with dissolve
lb "I'm walking here!"
ls "..."
lb "And can I borrow your pad?"
ce "Sure."
scene ep6_prologue57 with dissolve
lb "Yessssss!"
ce "I'll be too busy kicking your sister's butt."
lb "Double-yessssss!"
scene ep6_prologue58 with dissolve
lb "*chants* FIFA! FIFA!"
scene ep6_prologue59 with dissolve
lb "*sings* Football's coming home!"
scene ep6_prologue60 with dissolve
lb "Huh?"
scene ep6_prologue61 with dissolve
lb "What's that?"
scene ep6_prologue62 with dissolve
lb "..."
scene ep6_cecetitle03 with dissolve
$ renpy.pause(1.5)
scene ep6_cecetitle02 with dissolve
$ renpy.pause(1.5)
scene ep6_cecetitle01 with Fade(0, 0, 1.5, color="#ffffff")
$ renpy.pause(1.5)
stop music fadeout 3
scene ep6_cecetitle00 with Dissolve(2, alpha=True)
$ renpy.pause()
scene ep6_cecemorning01 with Dissolve(4, alpha=True)
show screen phone
$ clockis = [[todayIs],1,0,1,3]
play music ep6_cecemorning
$ nowPlayingArtist = "Elad Perez"
$ nowPlayingTitle = "Everest"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
if ep4NightChoose == 1:
    me "Morning beautiful."
else:
    me "You're snoring."
ce "Mhhh..."
scene ep6_cecemorning02 with dissolve
ce "Just five more minutes."
scene ep6_cecemorning03 with dissolve
me "I'll be counting those minutes."
scene ep6_cecemorning04 with dissolve
ce "I won't."
scene ep6_cecemorning03 with dissolve
me "You're just like a dog, you know."
me "Sleeping with your tongue out like that."
scene ep6_cecemorning04 with dissolve
ce "Every time you say something, I'm adding five minutes."
menu:
    "[M_06_001a]": # "Look down.":
        $ ep6CeceLookTit = True
        scene ep6_cecemorning05 with dissolve
        me "Where's your bra."
        scene ep6_cecemorning04 with dissolve
        ce "Slept without it. Like it better that way."
        if ep4NightChoose == 1:
            me "Me too. Gets me thinking..."
            ce "That's another five minutes."
        else:
            ce "Unless you're uncomfortable by it of course."
            me "No, I'm not complaining."
            ce "I didn't think so."
        jump ep6GetUpMorning
    "[M_06_001b]": # "Don't look down.":
        jump ep6GetUpMorning
label ep6GetUpMorning:
ce "Your hand is on my thigh by the way."
scene ep6_cecemorning06 with dissolve
if ep4NightChoose == 1:
    me "I like it between your thighs."
    ce "Sweet talker."
    me "And it's not like you're giving me a lot of space here."
else:
    me "Sorry. But you're not giving me a lot of space here."
ce "What's that supposed to mean. You're the one taking all the space."
scene ep6_cecemorning07 with dissolve
me "Of course."
if ep4NightChoose == 1:
    me "But unless you want to have your way with me right now, I think I'm going to get up and get some coffee."
    ce "You should be safe..."
    ce "...for now."
    me "For now?"
    ce "That's another five minutes."
    me "Whatever..."
else:
    me "I'll get out of your face then so you can have some more space."
    me "And make myself some coffee."
ce "..."
scene ep6_cecemorning08 with dissolve
$ clockis = [[todayIs],1,0,3,1]
ce "Make one for me too?"
me "Sure."
me "(So, what's on the agenda for today.)"
$ ep6MorningListLi = True
$ ep6MorningListKi = True
$ ep6MorningListRo = True
$ ep6MorningListSt = True
if not Impact_Steph:
    $ ep6MorningListSt = False


$ ep6MorningListLe = True
$ ep6MorningListCh = True
$ ep6MorningListCe = True
$ ep6MorningListEnd = False
$ ep6DayOrder = 0
$ ep6MsgKira = True
$ ep6MsgRobin = True
label ep6MorningMenuStart:
if not ep6MorningListKi:
    if not ep6MorningListRo:
        if not ep6MorningListCh:
            $ ep6MorningListEnd = True
menu:
    "[M_06_002a]" if ep6MorningListLi: # "Linda" if ep6MorningListLi:
        scene ep6_cecemorning11 with dissolve
        me "(Cece told me Linda won't be back until tonight or tomorrow. Guess I'll have to wait until then to talk to her.)"
        me "(It was some kind of surprise.)"
        $ ep6MorningListLi = False
        jump ep6MorningMenuStart
    "[M_06_002b]" if ep6MorningListKi: # "Kira" if ep6MorningListKi:
        scene ep6_cecemorning11 with dissolve
        me "(I told Kira I'd come visit her after I got home. She should be working now.)"
        scene ep6_cecemorning12 with dissolve
        me "(I'll text her.)"
        scene ep6_cecemorning20 with dissolve
        menu:
            "[M_06_003a]": # "'That offer of a free Frappe still on the table?'":
                $ chat_kira_item = "0;0;3301;That offer of a free Frappe still on the table?"
            "[M_06_003b]": # "'Got some time to meet up and talk?'":
                $ chat_kira_item = "0;0;3305;Got some time to meet up and talk?"
            "[M_06_003c]" if ep4NightChoose == 3: # "'Miss you.'" if ep4NightChoose == 3:
                $ chat_kira_item = "0;0;3306;Miss you."
        label ep6TextKiraStart:
        if chat_kira_item not in chat_kira:
            $ chat_kira.append(chat_kira_item)
        $ chat_sel_name = "Kira"
        $ chat_sel_icon = "cont_kira"
        call screen phone_chat_single
        me "(...)"
        if not ep6MorningListKi:
            jump ep6TextKiraStart
        label ep6TextKiraEnd:
        scene ep6_cecemorning12 with dissolve
        me "(Meet up with Kira. Ok.)"
        $ ep6MorningListKi = False
        jump ep6MorningMenuStart
    "[M_06_002c]" if ep6MorningListRo: # "Robin" if ep6MorningListRo:
        scene ep6_cecemorning11 with dissolve
        me "(Robin was acting all weird before they left.)"
        scene ep6_cecemorning12 with dissolve
        me "(I'll text her.)"
        scene ep6_cecemorning20 with dissolve
        menu:
            "[M_06_004a]": # "'Would you like to meet up?'":
                $ chat_robin_item = "0;0;3401;Hey Robin. I'm back in town. Would you like to meet up?"
            "[M_06_004b]" if ep4NightChoose == 4: # "'Hey Sexy. Missed me?'" if ep4NightChoose == 4:
                $ chat_robin_item = "0;0;3411;Hey Sexy. I'm back. Missed me?"
        label ep6TextRobinStart:
        if chat_robin_item not in chat_robin:
            $ chat_robin.append(chat_robin_item)
        $ chat_sel_name = "Robin"
        $ chat_sel_icon = "cont_robin"
        call screen phone_chat_single
        me "(...)"
        if not ep6MorningListRo:
            jump ep6TextRobinStart
        label ep6TextRobinEnd:
        scene ep6_cecemorning12 with dissolve
        me "(That's Robin sorted.)"
        $ ep6MorningListRo = False
        jump ep6MorningMenuStart
    "[M_06_002d]" if ep6MorningListSt: # "Steph" if ep6MorningListSt:
        $ ep6TriedCallingSteph = True
        scene ep6_cecemorning11 with dissolve
        me "(I wonder how it went with Steph yesterday.)"
        menu:
            "[M_06_005a]": # "I should call her.":
                scene ep6_cecemorning13 with dissolve
                hide screen phone
                play sound phone_outgoing_answer
                scene bg empty with fade
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                stop sound
                scene ep6_stephcall09 with fade
                if ep4NightChoose == 7:
                    st "Hey babe."
                    me "Hey Hon. Just thought I should check in with you and hear how it went yesterday. With your dad and all."
                else:
                    st "Hey [name]."
                    me "Hey Steph. Just thought I should check in with you and hear how it went yesterday. With your dad and all."
                scene ep6_stephcall01 with dissolve
                st "My dad. Well... it was a total shitshow. He kinda freaked out and in the end I just couldn't take it anymore and left."
                scene ep6_stephcall02 with dissolve
                me "I'm so sorry to hear that."
                scene ep6_stephcall02b with dissolve
                st "Can't blame him though, I brought it on myself. You're not the only one I had to hide from for two years, you know."
                scene ep6_stephcall03 with dissolve
                me "Shit, I never thought about it like that."
                scene ep6_stephcall02b with dissolve
                st "Well, nothing more to do than give him some space I guess. Hope he comes around."
                scene ep6_stephcall03 with dissolve
                me "And your job?"
                scene ep6_stephcall04 with dissolve
                st "Listen... I don't really want to talk about it right now. I'm dead tired."
                me "Couldn't sleep last night?"
                scene ep6_stephcall06 with dissolve
                st "Didn't try. I just got in the car and drove all night."
                me "..."
                me "Hang on... You're driving where exactly?"
                scene ep6_stephcall08 with dissolve
                st "Home."
                me "Home? You mean here?"
                st "*laughs* Yes."
                me "Fuck's sake Steph. I'm sure you could have used Lexi's pl..."
                st "I know, she said so. But I needed the trip. So I just rented a car."
                me "So when are you back?"
                scene ep6_stephcall07 with dissolve
                st "In a few days. I'm taking the scenic route."
                if ep4NightChoose == 7:
                    me "Be careful, Darling. Ok? Come see me right away when you're back. I'll be waiting with that massage of mine that you love."
                    me "And get some sleep now."
                    st "Don't worry, Honey. I will. I prefer driving at night anyway."
                    st "I... miss you."
                    me "I love you too, Steph."
                else:
                    me "Be careful, ok? And get some sleep now."
                    st "I will. I prefer driving at night anyway."
                    me "Have a nice trip."
                    st "Thank you."
                scene ep6_cecemorning12 with dissolve
                show screen phone
                me "(Jesus, Steph. What is with you and always choosing the path of most resistance.)"
            "[M_06_005b]": # "She'll call me at some point.":
                me "(She said she'd call. I'll wait for it.)"
        $ ep6MorningListSt = False
        jump ep6MorningMenuStart
    "[M_06_002e]" if ep6MorningListLe: # "Lexi" if ep6MorningListLe:
        scene ep6_cecemorning11 with dissolve
        me "(She's probably busy with her schedule.)"
        if ep4NightChoose == 2:
            me "(I can try calling her. Unless she's going to feel I'm disturbing her, or being too clingy.)"
            menu:
                "[M_06_006a]": # "I should call her.":
                    $ ep6TriedCallingLexi = True
                    scene ep6_cecemorning13 with dissolve
                    hide screen phone
                    play sound phone_outgoing_answer
                    scene bg empty with fade
                    $ renpy.pause(0.5)
                    $ renpy.pause(0.5)
                    $ renpy.pause(0.5)
                    $ renpy.pause(0.5)
                    stop sound
                    scene ep6_cecemorning12 with dissolve
                    me "Hmmm. No answer."
                    show screen phone
                "[M_06_006b]": # "I shouldn't disturb her.":
                    me "(I'm sure she'll call me when she's got a break in her schedule.)"
        me "(Hope she's ok though..)"
        $ ep6MorningListLe = False
        jump ep6MorningMenuStart
    "[M_06_002f]" if ep6MorningListCh: # "Chris" if ep6MorningListCh:
        scene ep6_cecemorning11 with dissolve
        me "(I should call Chris about this thing with Matt.)"
        scene ep6_cecemorning13 with dissolve
        hide screen phone
        play sound phone_outgoing_answer
        scene bg empty with fade
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        stop sound
        scene ep6_chrisphone01 with fade
        ch "Yo man, you home yet?"
        scene ep6_cecemorning14 with dissolve
        me "I am. Got home late last night. You busy?"
        scene ep6_cecemorning15 with dissolve
        ch "Kinda."
        scene ep6_cecemorning14 with dissolve
        me "I can call back."
        scene ep6_chrisphone02 with dissolve
        ch "No, not busy like that. We have this trainee here and he might have blown a fuse or something. It's all dark."
        ch "But how did it go with your dad?"
        scene ep6_chrisphone03 with dissolve
        me "All fine I guess. Just met the guy and talked for a bit. And it turns out I have a sister."
        scene ep6_chrisphone04 with dissolve
        ch "No way..."
        me "Or sibling or something. My dad's side only."
        ch "..."
        scene ep6_chrisphone05 with dissolve
        ch "So... she hot?"
        scene ep6_chrisphone06 with dissolve
        me "Dude!"
        scene ep6_chrisphone05 with dissolve
        ch "That's a perfectly valid question!"
        me "Nope, I'm not going to give you any reason to go simping on new sister."
        scene ep6_chrisphone07 with dissolve
        ch "What's her name?"
        me "Sea."
        scene ep6_chrisphone02 with dissolve
        ch "Sea what?"
        me "No, just Sea. Like... you know... ocean. Just Sea instead?"
        ch "Who calls their daughter, Sea."
        scene ep6_chrisphone07 with dissolve
        me "Hell if I know."
        me "She's cute though."
        scene ep6_chrisphone04 with dissolve
        ch "HAH. Made you admit it."
        if ep4NightChoose == 1:
            me "Anyway, subject change."
            ch "How did it go back home then? The girls all right?"
            if ep4SetupChrisWithLi:
                me "Well, your girl is off somewhere, fixing some surprise."
            else:
                me "Well, Linda is off somewhere, fixing some surprise."
            ch "Yeah, she was super happy about that for some reason. No idea what it is."
            scene ep6_chrisphone04 with dissolve
            ch "At least you got some alone time with your girl then."
            scene ep6_chrisphone05 with dissolve
            me "I got a very good welcome back hug."
            ch "*laughs* Somebody's smiling extra wide today then."
            menu:
                "[M_06_007a]": # "Tell him she's great in bed.":
                    $ ep6MorningToldChrisLewd = True
                    scene ep6_chrisphone03 with dissolve
                    me "No, nothing like that. Just enjoyed the night in the same bed."
                    me "That doesn't change the fact that she's just as amazing in bed as she's otherwise."
                    scene ep6_chrisphone07 with dissolve
                    ch "*laughs* Like we didn't hear you everywhere at Lexi's place."
                    scene ep6_chrisphone03 with dissolve
                    me "You did?"
                    me "So much for a subtle approach."
                "[M_06_007b]": # "Tell him you just slept.":
                    scene ep6_chrisphone03 with dissolve
                    me "No, nothing like that. Just enjoyed the night in the same bed."
            scene ep6_chrisphone02 with dissolve
            ch "Happy for you, man. You two are great together."
        scene ep6_cecemorning14 with dissolve
        me "By the way, you want to come over to my place tonight?"
        scene ep6_cecemorning15 with dissolve
        ch "That thing about Matt?"
        scene ep6_cecemorning14 with dissolve
        me "Yeah."
        scene ep6_chrisphone02 with dissolve
        ch "Sure thing, I'll be there around 9."
        me "Perfect."
        scene ep6_chrisphone07 with dissolve
        ch "Good. And..."
        ch "Let there be light!"
        scene ep6_chrisphone08 with dissolve
        ch "Nailed it."
        scene ep6_chrislight with dissolve
        ch "..."
        ch "Or not."
        ch "Anyway, got to fix this mess here. See you later on."
        me "See you."
        scene ep6_chrisphone04 with dissolve
        ch "Get it? 'Sea' you?"
        me "Bye!"
        if ep6MorningToldChrisLewd:
            scene ep6_cecemorning21 with dissolve
            ce "You have a really small apartment."
            scene ep6_cecemorning16 with dissolve
            me "You're complaining about my apartment not being big enough now?"
            scene ep6_cecemorning22 with dissolve
            ce "Nope."
            ce "I just wanted to tell you that I can hear every word you're saying."
            scene ep6_cecemorning17 with dissolve
            ce "About you and me and... that thing... and not telling anyone..."
            scene ep6_cecemorning18 with dissolve
            me "Shit, I'm so sorry. I just... really like you and... guys talk... and I... shouldn't have."
            scene ep6_cecemorning22 with dissolve
            ce "It's ok, really."
            scene ep6_cecemorning23 with dissolve
            me "Wait... what?"
            scene ep6_cecemorning22 with dissolve
            me "Really?"
            ce "*laughs*"
            me "So you want to change our status on Nuke now?"
            ce "That's five more minutes."
        show screen phone
        scene ep6_cecemorning12 with dissolve
        $ ep6MorningListCh = False
        jump ep6MorningMenuStart
    "[M_06_002g]" if ep6MorningListCe: # "Cece" if ep6MorningListCe:
        scene ep6_cecemorning09 with dissolve
        me "(Make coffee, check.)"
        $ ep6MorningListCe = False
        jump ep6MorningMenuStart
    "[M_06_002h]" if ep6MorningListEnd: # "Take a shower" if ep6MorningListEnd:
        hide screen phone
        stop music fadeout 3
        scene ep6_cecemorning10 with dissolve
        if ep6MorningListCe:
            me "(I have a feeling I forgot something...)"
            me "(I'll remember soon enough.)"
        else:
            me "(At least I remembered to put on the coffee.)"
        show screen phone
        jump ep6MorningMenuEnd
label ep6MorningMenuEnd:
scene bg empty with fade
$ clockis = [[todayIs],1,1,0,7]
play music ep6_cecetable
$ nowPlayingArtist = "Casey Parnell"
$ nowPlayingTitle = "Different Ways"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_cecemorning24 with fade
me "Oh, you're up."
scene ep6_cecemorning25 with dissolve
ce "Hey. Sure am."
if ep6MorningListCe:
    scene ep6_cecemorning26 with dissolve
    ce "And the coffee you were supposed to make is over there."
    scene ep6_cecemorning27 with dissolve
    me "You made."
    ce "I made."
    scene ep6_cecemorning28 with dissolve
    me "I knew I forgot something."
else:
    me "Tell me you didn't drink all the coffee."
    ce "Of course I did."
    ce "But I made more for you."
    scene ep6_cecemorning26 with dissolve
    ce "Over there."
    scene ep6_cecemorning27 with dissolve
    ce "Refreshing shower?"
    me "Very."
    ce "You used all the hot water?"
    scene ep6_cecemorning28 with dissolve
    me "No, that's your job. Should be plenty left."
scene ep6_cecemorning29 with dissolve
me "Oh, and Cece?"
ce "Hmm?"
if ep4NightChoose == 1:
    me "I know I have a nice ass. Feel free to look closer."
else:
    me "You are staring at my ass."
scene ep6_cecemorning30 with dissolve
ce "I wasn't."
me "Sure."
me "I can do some cool ass moves if you're interested."
scene ep6_cecemorning31 with dissolve
ce "No, thank you. I'll be fine."
scene ep6_cecemorning32 with fade
ce "..."
scene ep6_cecemorning33 with dissolve
ce "..."
me "*laughs* My ass is over here."
scene ep6_cecemorning34 with dissolve
$ clockis = [[todayIs],1,1,1,4]
ce "Ok, smartass. Game's on."
ce "I'm going to make you choke on that coffee before we're done here."
me "No chance. But by all means, try."
scene ep6_cecemorning35 with dissolve
me "So you were staring!"
ce "Whatever..."
scene ep6_cecemorning36 with dissolve
ce "You got any plans for today?"
scene ep6_cecemorning37 with dissolve
me "Well... First, coffee."
if ep6DayOrder == 1:
    me "Then I'm heading over to MaKenzie for a Frappe and a chat with Kira."
    me "Afterwards I'm heading over to see Robin at her bowling alley."
else:
    me "Then I'm heading over to Robin's bowling alley to have a chat with her."
    me "Afterwards I'm heading over to MaKenzie to meet up with Kira. I believe she had a Frappe for me."
me "I think the two of them needs a middle man. I think they might be having problems or something like that."
if ep4NightChoose == 3:
    scene ep6_cecemorning38 with dissolve
    ce "Aren't you supposed to be Kira's boyfriend?"
    scene ep6_cecemorning39 with dissolve
    me "I think I am."
    me "But I feel more like a wedge between them. I have to make that right. Then I'll have to see what happens afterwards."
elif ep4NightChoose == 4:
    scene ep6_cecemorning38 with dissolve
    ce "Aren't you supposed to be Robin's boyfriend?"
    scene ep6_cecemorning39 with dissolve
    me "I think I am."
    me "But I feel more like a wedge between them. I have to make that right. Then I'll have to see what happens afterwards."
elif ep4NightChoose == 5:
    scene ep6_cecemorning38 with dissolve
    ce "Aren't you supposed to be their boyfriend?"
    scene ep6_cecemorning39 with dissolve
    me "I think I am."
    me "But I feel more like a wedge between them. I have to make that right. Then I'll have to see what happens afterwards."
else:
    scene ep6_cecemorning38 with dissolve
    ce "They are having relationship problems?"
    scene ep6_cecemorning39 with dissolve
    me "I think so. Hopefully I'll find a way to bring them together again."
scene ep6_cecemorning37 with dissolve
me "Why don't you tag along?"
scene ep6_cecemorning36 with dissolve
ce "Can't. I have some plans of my own."
scene ep6_cecemorning44 with dissolve
me "Oh?"
scene ep6_cecemorning45 with dissolve
ce "I'll tell you about it later."
scene ep6_cecemorning44 with dissolve
$ clockis = [[todayIs],1,1,2,4]
me "And by the way, Chris is dropping by tonight at 9. We have to talk to Matt about that whole situation with Linda."
ce "Mhmmm..."
me "By the way, how are you feeling?"
scene ep6_cecemorning45 with dissolve
ce "Fine."
scene ep6_cecemorning44 with dissolve
me "You know, one day you're going to have to open up a bit more about... well, you know."
scene ep6_cecemorning40 with dissolve
me "Maybe we can sit down and talk a bit later today?"
ce "..."
scene ep6_cecemorning42 with dissolve
ce "Can we just drop it?"
ce "That's not what I'm worried about."
scene ep6_cecemorning41 with dissolve
me "Then what are you worried about?"
ce "..."
me "Ok, let's drop it."
scene ep6_cecemorning42 with dissolve
ce "And how are you doing?"
scene ep6_cecemorning39 with dissolve
me "Me? I'm doing just fine."
ce "..."
scene ep6_cecemorning38 with dissolve
ce "See? It's what everybody says when someone asks how they're doing."
ce "Doesn't mean it's true."
scene ep6_cecemorning39 with dissolve
me "Honestly, I'm fine."
scene ep6_cecemorning38 with dissolve
ce "You weren't fine that day on the bridge."
scene ep6_cecemorning45 with dissolve
ce "I could see it from a mile away."
scene ep6_cecemorning44 with dissolve
me "Yeah, you know there was a lot going on back then. With Steph and everything, but from that point on, it's been all good."
if stephRejected:
    me "And as you said, if I hadn't run into Steph that day, you wouldn't have been here now."
else:
    me "And as you said, if Steph hadn't thrown me out the window, butt naked, you wouldn't have been here now."
    scene ep6_cecemorning43 with dissolve
    ce "...and just why did you have to jump out the window from Steph's place butt naked?"
    scene ep6_cecemorning44 with dissolve
    me "Ehm... I never told you that detail, did I."
    scene ep6_cecemorning45 with dissolve
    ce "Hmmm."
    if ep4NightChoose == 1:
        scene ep6_cecemorning37 with dissolve
        me "That's your reaction?"
        scene ep6_cecemorning36 with dissolve
        ce "So what. You had sex before me. I never took you for a virgin."
$ clockis = [[todayIs],1,1,3,3]
scene ep6_cecemorning37 with dissolve
me "Anyway, subject change. How was girls night?"
scene ep6_cecemorning36 with dissolve
ce "Me and Linda?"
scene ep6_cecemorning56 with dissolve
ce "It was fun."
ce "She taught me how to eat pussy."
scene ep6_cecemorning57 with dissolve
me "*coughs*"
scene ep6_cecemorning58 with dissolve
ce "Told ya I'd make you choke on that coffee."
scene ep6_cecemorning59 with dissolve
me "I've got coffee in my nose!"
scene ep6_cecemorning55 with dissolve
me "..."
me "Hang on... Did you..."
scene ep6_cecemorning52 with dissolve
ce "That's the cool thing about sexual innuendos..."
if ep4NightChoose == 1:
    scene ep6_cecemorning51 with dissolve
    ce "*kiss*"
scene ep6_cecemorning53 with dissolve
me "..."
if ep4NightChoose == 1:
    scene ep6_cecemorning46 with dissolve
    me "..."
scene ep6_cecemorning47 with dissolve
me "Wait, what's cool about sexual innuendos?"
scene ep6_cecemorning48 with dissolve
ce "That you stop worrying about how I'm doing."
ce "Have fun today."
scene ep6_cecemorning49 with dissolve
ce "And now excuse me while I go rub one out in the shower."
scene ep6_cecemorning50 with dissolve
me "..."
scene ep6_cecemorning55 with dissolve
$ clockis = [[todayIs],1,1,4,0]
me "(That was another sexual innuendo, wasn't it...)"
if ep4NightChoose == 1:
    me "(Was it?)"
    me "(I have to admit she's got a point though. I'm not worried anymore.)"
else:
    me "(I have to admit she's got a point though. Not that I would cheat on my girl, but at least I'm not worried anymore.)"
if ep6DayOrder == 1:
    me "(Time to finish up this coffee and head over to Kira.)"
    jump ep6DayKira
else:
    me "(Time to finish up this coffee and head over to Robin.)"
    jump ep6DayRobin
label ep6DayKira:
stop music fadeout 10
scene bg empty with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,2,1,1]
else:
    $ clockis = [[todayIs],1,6,3,3]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)

scene ep6_kirawork01 with fade
me "(Oh, there's a lot of people here today.)"
scene ep6_kirawork02 with dissolve
me "Excuse me."
scene ep6_kirawork03 with dissolve
me "Coming through."
scene ep6_kirawork04 with dissolve
me "(There she is.)"
scene ep6_kirawork05 with dissolve
me "Ladies..."
scene ep6_kirawork06 with dissolve
me "(She looks stressed.)"
scene ep6_kirawork07 with dissolve
me "(Maybe that's what she meant by everything going wrong today.)"
scene ep6_kirawork08 with dissolve
me "Busy day, eh?"
scene ep6_kirawork09 with dissolve
ki "You wouldn't believe."
scene ep6_kirawork10 with dissolve
ki "*whistles* 247 done."
scene ep6_kirawork11 with dissolve
ki "Come get it."
scene ep6_kirawork12 with dissolve
ki "*exhales*"
me "Don't worry about that Frappe. I'd rather enjoy it some day you have a few minutes to sit down and enjoy it with me."
scene ep6_kirawork13 with dissolve
ki "No, I'll fix you right up with it."
ki "Unfortunately, I have to keep running today. Sorry for having you over for nothing."
scene ep6_kirawork13b with dissolve
ki "One of the cooks didn't show today, and the other got pissed off because of it and left."
scene ep6_kirawork13c with dissolve
me "You saying you're all alone here today, doing everything?"
scene ep6_kirawork13b with dissolve
ki "That's very accurate."
ki "I've ridden storms like these before though, so I'll pull through."
scene ep6_kirawork14 with dissolve
me "Ok, that just won't do at all."
me "I'll cook."
ki "You can't just come here and cook. You don't even know the recipes."
me "I'll have you know that I am an excellent cook, and the center of every barbeque party. Burger master-chef at your service."
ki "No, really. You don't have to do that."
me "Ok, I think you need convincing."
me "I didn't want to do this, but you leave me with no other choice."
play music ep6_makenzie
$ nowPlayingArtist = "Leva"
$ nowPlayingTitle = "In the Saddle"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_mcfootwork1 with dissolve
ki "Huh. What..."
me "..."
scene ep6_mcfootwork2 with dissolve
ki "No-no-no-no-no."
me "Look at that hipwork."
scene ep6_mcfootwork3 with dissolve
ki "Seriously. Stop."
me "Oh, I got more woman."
scene ep6_kirawork19 with dissolve
ki "..."
scene ep6_kirawork19b with dissolve
ki "Ok..."
scene ep6_kirawork19 with dissolve
me "Ok, what?"
scene ep6_kirawork19b with dissolve
ki "Ok, you can cook."
ki "Just stop that thing you're doing."
scene ep6_kirawork19 with dissolve
me "You've seen nothing yet."
scene ep6_mcfootwork4 with dissolve
me "..."
scene ep6_kirawork19b with dissolve
ki "Someone kill me."
scene ep6_kirawork20 with dissolve
ki "Kitchen is that way."
me "You won't regret this."
scene ep6_kiraworking01 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,2,2,7]
else:
    $ clockis = [[todayIs],1,6,4,5]
me "(Oh boy do I regret this.)"
me "(Ok, blabbermouth. What now. You've never grilled anything in your whole life.)"
scene ep6_kiraworking46 with dissolve
ki "Burgers are in the freezer on your right. Oven is already heated."
scene ep6_kiraworking01 with dissolve
me "Coming right up."
scene ep6_kiraworking02 with dissolve
me "(Ok, burgers found. Now to grill them.)"
scene ep6_kiraworking03 with fade
me "(Everything going well so far.)"
scene ep6_kiraworking46 with dissolve
ki "Salad, tomatoes, pickles in the fridge. Buns in the cupboard next to it."
scene ep6_kiraworking09 with dissolve
me "You don't have to tell me everything..."
me "(Thank you for telling me everything...)"
scene ep6_kiraworking10 with dissolve
me "(Buns...)"
scene ep6_kiraworking11 with dissolve
me "(...salad...)"
scene ep6_kiraworking12 with dissolve
me "(...tomatoes...)"
scene ep6_mcchopping with dissolve
me "(And we're on a roll.)"
me "(...)"
me "(This is easy. Now there's only one thing missing.)"
me "(A kitchen mascot.)"
scene ep6_kiraworking19 with dissolve
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,2,3,5]
else:
    $ clockis = [[todayIs],1,6,5,8]
me "Why, hello Miss. I didn't see you there."
scene ep6_kiraworking20 with dissolve
me "What's that... If I can help you with a haircut?"
scene ep6_kiraworking21 with dissolve
me "Of course I can. Do you think I got this great hair just by accident?"
me "No such thing, Miss. This was the work of an expert developer."
scene ep6_kiraworking22 with dissolve
me "I should just call you Samantha? That I can do."
me "We'll have you looking great in no time, Samantha."
me "And if you don't mind me saying so, you have beautiful ears. Simply adoring."
scene ep6_kiraworking23 with dissolve
me "Voila. A true masterpiece if I have to say so myself."
scene ep6_kiraworking24 with dissolve
me "And again, such nice ears."
scene ep6_kirawork48b with dissolve
ki "Is that goofing around I'm hearing?"
show ep6_kiraworking27c
show ep6_kiraworking27b
me "Nooo?"
hide ep6_kiraworking27b
show ep6_kiraworking27a at imgSlide_ep6Samantha
show ep6_kiraworking27b
$ renpy.pause(1)
$ renpy.pause(1)
$ renpy.pause(1)
$ renpy.pause(1)
scene ep6_kiraworking26
hide ep6_kiraworking27c
hide ep6_kiraworking27c
hide ep6_kiraworking27c
me "*whispers* She said hear, not ear."
scene ep6_kiraworking25 with dissolve
me "..."
scene ep6_kiraworking26 with dissolve
me "*whispers* You have beautiful ears."
scene ep6_kiraworking25 with dissolve
ki "I need 10 MaKenzie's and 10 Cheezie's."
scene ep6_kiraworking07 with dissolve
me "So bossy."
scene ep6_kiraworking06 with dissolve
$ renpy.pause(0.6)
scene ep6_kiraworking08 with dissolve
me "(Yes!)"
scene ep6_kiraworking28 with dissolve
me "High five!"
sa "..."
scene ep6_kiraworking29 with dissolve
me "Don't worry. We'll work on it."

scene ep6_kiraworking46 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,2,4,9]
else:
    $ clockis = [[todayIs],1,7,1,2]
ki "Listen, you really don't need to do this if you feel uncomfortable back there."
ki "I can make the burgers."
scene ep6_kiraworking48 with dissolve
ki "The customers are beginning to become a bit restless..."
scene ep6_kiraworking49 with dissolve
me "Here you go."
ki "Whoa... Impressive."
scene ep6_kiraworking51 with dissolve
me "Don't thank me. Couldn't have done it without Samantha."
scene ep6_kiraworking50 with dissolve
ki "..."
ki "Without who?"
scene ep6_kiraworking52 with dissolve
me "High five!"
scene ep6_kiraworking50 with dissolve
ki "..."
me "We'll work on it."

scene ep6_kiraworking31 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,3,0,7]
else:
    $ clockis = [[todayIs],1,7,2,7]
me "What's that?"
scene ep6_kiraworking32 with dissolve
sa "..."
scene ep6_kiraworking31 with dissolve
me "I couldn't agree more."
me "And for that we need a bit of..."
scene ep6_kiraworking30 with dissolve
me "JD!"

scene ep6_kiraworking33 with fade
ki "How are the burgers coming along?"
me "Pretty much perfect."
me "They just need a little dash of..."
scene ep6_kiraworking34 with dissolve
me "..."
scene ep6_flammable1 with dissolve
me "..."
scene ep6_kiraworking36 with dissolve
me "Soon done..."
scene ep6_kiraworking37 with dissolve
me "Well done..."
scene ep6_kiraworking38 with dissolve
me "..."

scene ep6_kiraworking17 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,3,5,9]
else:
    $ clockis = [[todayIs],1,7,4,9]
me "I just wanted you to know that I normally don't do this so soon after meeting someone."
scene ep6_kiraworking18 with dissolve
me "But I can feel that we have something special here."
me "And I sense that you're reacting to my touch as well."
scene ep6_kiraworking16 with dissolve
me "Can you feel me slide back and forth."
me "It's all in the touch. You start real slow to get the juices flowing."
me "Just feel those fingers working all your sensitive parts."
me "Mmmm... I feel you're getting closer. So if I just put my finger here..."

scene ep6_kiraworking43 with fade
uk "Excuse me?"
ki "Yes?"
scene ep6_kiraworking44 with dissolve
uk "I have to give compliments to the Chef."
uk "The burger was so much more juicy and tender than it normally is."
ki "You're joking, right?"
scene ep6_kiraworking39 with dissolve
uk "..."
scene ep6_kiraworking40 with dissolve
ki "I mean, thank you very much. I'll pass the message."
uk "Do you think I can speak to him directly? I mean, the Chef's a 'He' right?"
scene ep6_kiraworking39 with dissolve
ki "He is indeed a he. I can check if he's available."
uk "There's something so sexy about a man cooking."
ki "Got to agree with you on that..."
scene ep6_kiraworking41 with dissolve
ki "..."
scene ep6_kiraworking42 with dissolve
ki "I'm sorry, but I just remembered that he said that he didn't want to be disturbed today."
scene ep6_workmassage1 with dissolve
ki "He's really into it when he's cooking."
uk "That's a real shame."
scene ep6_kiraworking44 with dissolve
ki "But feel free to come back some other time. Maybe he'll be here then."
scene ep6_kiraworking43 with dissolve
ki "Byebye sweetie."
scene ep6_kiraworking46 with dissolve
ki "Congratulations, [name]. You just found the one thing in the world that does not turn me on."
if ep4NightChoose == 3 or ep4NightChoose == 5:
    scene ep6_workmassage2 with dissolve
    ki "..."
    scene ep6_kiraworking47 with dissolve
    ki "..."
    scene ep6_workmassage3 with dissolve
    $ renpy.pause(3)
    ki "..."
    scene ep6_kiraworking63 with dissolve
    me "..."
    scene ep6_kiraworking64 with dissolve
    ki "Damn you."
else:
    scene ep6_kiraworking47 with dissolve
    ki "..."

scene ep6_kiraworking65 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,5,4,2]
else:
    $ clockis = [[todayIs],1,8,5,5]
ki "You can relax now if you want. Feel free to take 5 minutes."
scene ep6_kiraworking67 with dissolve
me "No can do. I've got the whole queue system set up now. Everything from cutting the salad to frying the fries."
scene ep6_kiraworking66 with dissolve
ki "[name]?"
scene ep6_kiraworking68 with dissolve
ki "..."
scene ep6_kiraworking71 with dissolve
me "Come here."
scene ep6_kiraworking72 with dissolve
ki "I really needed a mood boost today. Thank you so much. Really."
if ep4NightChoose == 3 or ep4NightChoose == 4 or ep4NightChoose == 5:
    me "Hey, I'd do it again any day."
    scene ep6_kiraworking73 with dissolve
    if ep4NightChoose == 3:
        ki "You know how to make a woman feel special."
        me "Because you are."
    else:
        ki "So Robin's not your girl anymore?"
        me "Of course she is. But even in our special kind of relationship, there's time for each other on a personal level, don't you think?"
    ki "Got to say that you tenderizing that meat... got me all worked up."
    ki "If I hadn't been at work right now..."
    me "But Robin..."
    ki "...doesn't mind!"
    me "How do you know that?"
    ki "Because I wouldn't mind you doing her."
    if ep6DayOrder == 1:
        $ clockis = [[todayIs],1,5,4,9]
    else:
        $ clockis = [[todayIs],1,9,0,5]
    menu:
        "[M_06_008a]": # "Go for it.":
            $ ep6HadSexWithKira = True
            scene ep6_kiraworking74 with dissolve
            me "Ok, woman. You just said the magic words."
            ki "What?"
            scene ep6_kiraworking75 with dissolve
            me "A man's gotta do..."
            scene ep6_kiraworking76 with dissolve
            me "...what a man's..."
            scene ep6_kiraworking77 with dissolve
            me "...gotta do."
            scene ep6_kiraworking78 with dissolve
            ki "I love this!"
            me "I've wanted to rip this skirt off you for quite some time now."
            scene ep6_kiraworking81 with dissolve
            me "*whispers* I'm not overdoing it, am I?"
            ki "You saying your girl is the jealous kind?"
            me "My girl?"
            scene ep6_kiraworking82 with dissolve
            ki "Yeah, your girl."
            me "Oh, her. No we have a very open relationship."
            scene ep6_kiraworking79 with dissolve
            ki "Then do you job, Tiger. Go ahead and f..."
            scene ep6_kiraworking80 with dissolve
            ki "...oooohmygod!"
            ki "..."
            scene ep6_kira01bend with dissolve
            ki "I forget... how big... you are... every... single... time!"
            me "So, go easy?"
            ki "Go hard!"
            ki "You have 2 minutes."
            ki "Make them count!"
            me "..."
            me "Lose the shirt."
            me "I want to see you."
            scene ep6_kira02back_end
            if ep6DayOrder == 1:
                $ clockis = [[todayIs],1,5,5,1]
            else:
                $ clockis = [[todayIs],1,9,0,7]
            $ renpy.movie_cutscene("imov/ep6/ep6_kira02back.webm", delay=None, loops=0, stop_music=False)
            me "You're gorgeous."
            ki "1 minute."
            me "So much pressure."
            ki "YES! MORE PRESSURE!"
            scene ep6_kira01back with dissolve
            ki "..."
            ki "I LOVE YOU!"
            me "Shit, they are going to hear you!"
            ki "I don't care, I'm so close!"
            me "You and me both."
            scene ep6_kiraworking87 with dissolve
            uk "Excuse me, is anybody working here?"
            scene ep6_kiraworking88 with dissolve
            ki "YES!"
            scene ep6_kiraworking87 with dissolve
            me "Crap..."
            scene ep6_kiraworking88 with dissolve
            me "...time?"
            scene ep6_kiraworking89 with dissolve
            ki "Fuck no!"
            scene ep6_kiraworking90 with dissolve
            ki "Keep slamming..."
            scene ep6_kiraworking91 with dissolve
            ki "...that pussy..."
            scene ep6_kiraworking92 with dissolve
            ki "I'm going..."
            scene ep6_kiraworking93 with dissolve
            ki "...to cum..."
            scene ep6_kiraworking94 with dissolve
            ki "..."
            scene ep6_kirafall with dissolve
            ki "..."
            scene ep6_kiraworking97 with fade
            ki "*pants* Shit, are you ok?"
            scene ep6_kiraworking98 with dissolve
            me "*pants* If I'm ok?"
            me "You're the one that landed..."
            scene ep6_kiraworking990 with dissolve
            ki "...on something hard, yes I know."
            ki "I'm very ok!"
            uk "Anybody?"
            scene ep6_kiraworking99 with dissolve
            ki "One..."
            me "...minute!"
            scene ep6_kiraworking991 with dissolve
            me "Kira. I came."
            ki "Good!"
            ki "It's not like I'm fucking other guys than you."
            ki "Can't let the good stuff go to waste."
            scene ep6_kiraworking97 with dissolve
            ki "And don't worry, you're safe."
            ki "Now where did I put my clothes."
            scene ep6_kiraworking86 with fade
            ki "That was just what I needed."
            scene ep6_kiraworking84 with dissolve
            ki "..."
            scene ep6_kiraworking85 with dissolve
            ki "You are just what I need."
            ki "But now I have to get back."
            scene ep6_kiraworking69 with dissolve
            ki "With lots of new energy."
            me "And Kira?"
            scene ep6_kiraworking48 with dissolve
            ki "Yes?"
            scene ep6_kiraworking992 with dissolve
            me "You're leaking the good stuff."
            ki "Ssssssssssssh.. I know!"
        "[M_06_008b]": # "Maybe not such a good idea.":
            me "I don't think that's a good idea."
            ki "You're probably right, there's customers waiting."
            me "No, I mean, with Robin."
            ki "Yeah, and that. Not that she would care."
else:
    me "No problem at all. It's not like I had a full schedule of other things to do anyway."

scene ep6_kiraworking48 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,6,2,0]
else:
    $ clockis = [[todayIs],1,9,4,1]
ki "You got a new batch of burgers back there? We're running out."
scene ep6_kiraworking49 with dissolve
me "Here you go."
ki "You're killing it."
scene ep6_kiraworking51 with dissolve
me "Don't thank me. Couldn't have done it without Samantha."
scene ep6_kiraworking50 with dissolve
ki "All thanks to Sam, eh?"
me "You got it."
scene ep6_kiraworking52 with dissolve
me "High five!"
scene ep6_kiraworking53 with dissolve
stop music fadeout 3
me "Nooooooooooooooooo!"
me "What have you done!"
scene ep6_kiraworking54 with dissolve
me "But why!"
me "You were my everything!"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_makenziefin
$ nowPlayingArtist = "Dazeychain"
$ nowPlayingTitle = "Call it"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_kirafin01 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,6,5,3]
    ki "Thank god evening shift showed up. This is a well deserved rest."
else:
    $ clockis = [[todayIs],2,0,1,6]
    ki "Thank god night shift showed up. This is a well deserved rest."
scene ep6_kirafin02 with dissolve
me "I'd say we were a damn good team though."
ki "You certainly surprised me."
me "Honestly, I surprised myself more I think."
me "I've never grilled a burger in my life before."
ki "I knew it!"
scene ep6_kirafin01 with dissolve
ki "..."
scene ep6_kirafin02 with dissolve
me "Sam was a good help."
scene ep6_kirafin03 with dissolve
ki "Oh, I don't know about that."
ki "But I know one thing."
scene ep6_kirafin04 with dissolve
ki "She has delicious ears."
scene ep6_kirafin05 with dissolve
me "Yeah... I kept telling her."
scene ep6_kirafin06 with dissolve
me "She passed away before her time."
scene ep6_kirafin07 with dissolve
ki "..."
me "What?"
ki "Hm?"
me "You're looking at me."
scene ep6_kirafin08 with dissolve
ki "Of course I am. You're so completely different from the first time I saw you here."
ki "And Chris had to help you with that horrible pickup line."
scene ep6_kirafin07 with dissolve
me "He never told me what he said to you that day."
me "What did he say exactly."
scene ep6_kirafin08 with dissolve
ki "'My friend over there really needs a mood boost. Can you go over there and pretend he's cute so he'll get something to smile about?'"
scene ep6_kirafin07 with dissolve
me "Really... He said that?"
scene ep6_kirafin08 with dissolve
ki "Yeah. I thought he was joking. But it turns out he was right."
scene ep6_kirafin07 with dissolve
me "Well, I guess you could say I needed that boost."
scene ep6_kirafin08 with dissolve
ki "No, not that. The cute part. You really are. Not just by looks, but by being who you are."
scene ep6_kirafin09 with dissolve
me "You're different too, you know. From that day."
scene ep6_kirafin08 with dissolve
ki "I wear a different makeup."
scene ep6_kirafin07 with dissolve
me "No. You're uncertain about something. And I'm betting my Frappe it's Robin."
scene ep6_kirafin10 with dissolve
ki "*sigh*"
ki "She came over to my place yesterday."
ki "I thought we were going to relax and have a good time."
scene ep6_kirafin13 with dissolve
ki "Not like that... just enjoy being the two of us for the first time since before we went to Lexi."
me "And?"
scene ep6_kirafin12 with dissolve
ki "She wanted to break up with me."
if ep6DayOrder == 1:
    me "Really?"
else:
    me "..."
scene ep6_kirafin11 with dissolve
ki "Something about her not being good enough for me. Not being able to give me what I want."
ki "I have no idea what she's on about."
if ep6DayOrder == 1:
    me "Maybe she meant a normal family?"
else:
    me "I think she means a normal family?"
scene ep6_kirafin14 with dissolve
ki "Fuck normal family!"
ki "I was living in the most normal family in the world."
ki "Until I told them I was not normal."
ki "Then I wasn't good enough."
scene ep6_kirafin15 with dissolve
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,7,0,1]
else:
    $ clockis = [[todayIs],2,0,2,7]
me "Kira, have you looked at the world you live in."
me "We're way past judging normality by sexuality."
scene ep6_kirafin16 with dissolve
me "And if someone is still doing so..."
me "...it's because they don't know any better."
scene ep6_kirafin21 with dissolve
me "I used to be a bit more judgemental. Not really knowing why people would want to be with someone of their own sex."
me "Not that I really thought all that much about it. But you know, was a bit stuck in old traditional ways."
scene ep6_kirafin22 with dissolve
me "Then I met you two, and somehow you showed me that it's perfectly normal."
me "You helped me see that love is love."
me "So don't talk about not being normal."
scene ep6_kirafin20 with dissolve
me "It's one of the great things about you."
me "Heck, I even talk to my gay neighbor now. I didn't do that before."
me "And she has blue hair for christ's sake."
scene ep6_kirafin21 with dissolve
ki "..."
ki "Fuck!"
me "Huh?"
ki "The makeup, the piercing, the hair color..."
scene ep6_kirafin22 with dissolve
me "What about it?"
scene ep6_kirafin18 with dissolve
ki "I was so damn busy trying to show everyone I was different, when all I wanted was to be normal."
ki "That's why I chose this lipstick, got a piercing, dyed my hair."
scene ep6_kirafin17 with dissolve
me "I'm pretty sure people don't judge normality by hair color either you know."
me "Lexi doesn't even go by her normal hair color."
me "And the woman next door from me with blue hair, nobody even raises an eyebrow..."
ki "..."
scene ep6_kirafin18 with dissolve
ki "I miss her you know."
if ep6DayOrder == 1:
    scene ep6_kirafin17 with dissolve
    $ clockis = [[todayIs],1,7,1,7]
    me "Listen, I'm heading over to the bowling alley to meet Robin now. Let me talk to her."
    me "I'll get her side of the story and see where you mismatch."
    me "I've seen you two thriving all summer. There's no way she's letting that go because of an uncertainty."
    scene ep6_kirafin18 with dissolve
    ki "I hope so."
else:
    scene ep6_kirafin17 with dissolve
    $ clockis = [[todayIs],2,0,4,4]
    me "Listen, I was just at the bowling alley with Robin, and..."
    if ep6HadSexWithRobin:
        scene ep6_kirafin19 with dissolve
        ki "You fucked, I know."
        scene ep6_kirafin20 with dissolve
        me "Wait, how..."
        ki "You got her smell all over you."
        ki "I love her smell."
        if ep6HadSexWithRobin:
            me "And now I did you..."
            ki "I'd call that a pretty good day, wouldn't you?"
    else:
        scene ep6_kirafin19 with dissolve
        ki "I know. You've got her perfume all over you."
        ki "I love that perfume."
    scene ep6_kirafin17 with dissolve
    me "Well, what I was trying to say is that I think you're going to be ok."
    scene ep6_kirafin18 with dissolve
    ki "How do you know?"
    scene ep6_kirafin17 with dissolve
    me "You're just going to have to trust me on that."
    me "And give me a day or two."
    me "But I have to get going now. Chris is coming over at 9."
    scene ep6_kirafin18 with dissolve
    ki "That Linda thing?"
    scene ep6_kirafin17 with dissolve
    me "Yeah. We need to have a talk about it at least."
    scene ep6_kirafin19 with dissolve
    ki "Better hurry up then. It's in 15 minutes."
scene ep6_kirafin19 with dissolve
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,7,2,2]
else:
    $ clockis = [[todayIs],2,0,4,5]
ki "Thank you for the help today."
scene ep6_kirafin17 with dissolve
me "Don't mention it."
stop music fadeout 3
scene ep6_kirafin18 with dissolve
ki "And tell Cece I'll be there."
scene ep6_kirafin17 with dissolve
me "Be where?"
scene ep6_kirafin19 with dissolve
ki "You'll have to ask her about that."
if ep6DayOrder == 1:
    jump ep6DayRobin
else:
    jump ep6Backyard
label ep6DayRobin:
stop music fadeout 10
scene bg empty with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,7,3,5]
else:
    $ clockis = [[todayIs],1,2,1,3]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_bowling02 with fade
me "(She said she'd be here all day.)"
scene ep6_bowling03 with dissolve
me "(But she's not at the bar.)"
scene ep6_bowling01 with dissolve
me "Robin?"
scene ep6_bowling04 with dissolve
ro "[name]! Down here, by the lanes."
scene ep6_bowling05 with dissolve
me "There you are. How's things?"
scene ep6_bowling06 with dissolve
ro "Better now, actually."
if ep4NightChoose == 4 or ep4NightChoose == 5:
    scene ep6_bowling07 with dissolve
    me "Missed you."
    ro "Oh... I..."
    scene ep6_bowling08 with dissolve
    ro "...missed you too."
    ro "It's so good to hold you again."
scene ep6_bowling09 with dissolve
me "What are you doing here. Are the repair people coming?"
scene ep6_bowling11 with dissolve
ro "Yeah, right. They called to tell me they are delayed by two more weeks."
me "So, you're just here to... polish the bowling balls?"
scene ep6_bowling13 with dissolve
ro "No, I thought I'd test out the lanes and see if I could get it working in any way."
me "Did you?"
scene ep6_bowling14 with dissolve
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,7,3,8]
else:
    $ clockis = [[todayIs],1,2,1,6]
ro "Well, the machinery seems to be working just fine. Pins are put back into place and everything. But the balls don't return."
ro "I'd hoped it would just be a quick fix, but I have no idea what it could be."
ro "I'm back to square one."
me "Let me help out then."
scene ep6_bowling11 with dissolve
ro "And... you know anything about bowling machinery?"
me "I have about 24 years of experience assembling IKEA furniture."
scene ep6_bowling13 with dissolve
ro "That's not even remotely similar."
me "I know... It's way harder. Have you ever tried assembling one of those things?"
scene ep6_bowling15 with dissolve
ro "No, but..."
me "Exactly. IKEA!"
ro "..."
me "So where's the machine room?"
scene ep6_bowling12 with dissolve
ro "Ok. The door's right over there by the end. Lane 1."
ro "You head back there into the machine room, and I'll throw balls from here."
scene ep6_bowling16 with dissolve
ro "Maybe you can spot something from there which I can't see from this position."
me "..."
scene ep6_bowling18 with dissolve
ro "Lane 1..."
me "..."
scene ep6_bowling17 with dissolve
ro "...over there."
scene ep6_bowling19 with dissolve
me "On my way. I just had a flashback."
me "Time to do a bit of detective work."
play music ep6_robinearly
$ nowPlayingArtist = "Ian Post"
$ nowPlayingTitle = "True Detectives"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_bowling20 with fade
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,7,4,7]
else:
    $ clockis = [[todayIs],1,2,2,5]
me "Ok, so I'm ready. You can throw a ball now."
ro "What?"
me "I SAID I'M READY, YOU CAN THROW A BALL NOW!"
ro "..."
scene ep6_bowling21 with dissolve
me "What am I looking for exactly?"
scene ep6_bowling22 with dissolve
ro "Just observe and see if anything is out of the ordinary."
scene ep6_bowling21 with dissolve
me "Which would be?"
scene ep6_bowling22 with dissolve
ro "Just look."
ro "Oh, and there's tools there by the machinery."
scene ep6_bowling21 with dissolve
me "Got it."
scene ep6_bowling22 with dissolve
ro "Bomb's away."
scene ep6_bowling42 with dissolve
$ renpy.pause(0.2)
scene ep6_bowling43 with Dissolve(0.1, alpha=True)
play sound bowlroll
$ renpy.pause(1.5)
scene ep6_bowling44 with Dissolve(0.1, alpha=True)
play sound bowlhit
$ renpy.pause(1)
scene ep6_bowlingend01
$ renpy.movie_cutscene("imov/ep6/ep6_bowling01ball.webm", delay=None, loops=0, stop_music=False)
me "I think I see the problem."
ro "Really?"
me "Yeah, the ball doesn't have enough speed to get all the way back to you."
ro "Any obvious reason to why?"
me "Not really."
me "I mean, there's a loose screw so the whole rail is a bit wobbly, but that's not the problem."
scene ep6_bowling28 with dissolve
me "Hang on. There's a service door here. Let me look."
scene ep6_bowling33 with dissolve
ro "Be careful ok? Read the warning labels."
scene ep6_bowling36 with dissolve
me "Don't worry. Men have ignored warning labels for ages, and we're still here."
scene ep6_bowling48 with dissolve
ro "That doesn't make any sense..."
scene ep6_bowling35 with dissolve
me "What's that?"
scene ep6_bowling50 with dissolve
ro "Nothing..."
scene ep6_bowling29 with dissolve
me "Ok, I'm looking at some kind of controls."
me "There's a knob with values ranging from low to max. It's at medium now."
ro "Oh, I know what that is. I read through the 4,000 page manual yesterday."
ro "It's the air pressure driving the ball forward."
me "So I just adjust the pressure by turning that knob?"
ro "You can try it."
me "Ok, let's crank up this bad boy."
$ ep6PressureValve = 2
$ ep6PressureValveState = 0
$ ep6PressureHoseFix = False
$ ep6PressureMaxOpen = True
$ ep6PressureMaxUsed = False
$ ep6PressureMaxUsedDestroy = False
### Show Hint #################################################################################################################################
$ gen_notify = "Turn know to Max, try it.\nConnect the hose, turn knob to high, then try it."
show screen general_notifytop with dissolve
### Show Hint #################################################################################################################################

label ep6KnobTurn:
if ep6PressureValve == 4:
    scene ep6_bowling32 with dissolve
    $ renpy.pause(0.1)
    call screen knob_max
elif ep6PressureValve == 3:
    scene ep6_bowling31 with dissolve
    $ renpy.pause(0.1)
    call screen knob_high
elif ep6PressureValve == 2:
    scene ep6_bowling29 with dissolve
    $ renpy.pause(0.1)
    call screen knob_med
else:
    scene ep6_bowling32 with dissolve
    $ renpy.pause(0.1)
    call screen knob_low
label ep6KnobTurnLow:
if ep6PressureValve == 4:
    $ ep6PressureValve = 3
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 3:
    $ ep6PressureValve = 2
    scene ep6_bowling29 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 2:
    $ ep6PressureValve = 1
    scene ep6_bowling30 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValveState == 0:
    me "(Ok, that's not cranking it up, but let's see if there's any improvements.)"
jump ep6KnobTurnReady
label ep6KnobTurnMed:
if ep6PressureValve == 4:
    $ ep6PressureValve = 3
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 3:
    $ ep6PressureValve = 2
    scene ep6_bowling29 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 1:
    $ ep6PressureValve = 2
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
jump ep6KnobTurnReady
label ep6KnobTurnHigh:
if ep6PressureValve == 4:
    $ ep6PressureValve = 3
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 1:
    $ ep6PressureValve = 2
    scene ep6_bowling29 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 2:
    $ ep6PressureValve = 3
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
jump ep6KnobTurnReady
label ep6KnobTurnMax:
if ep6PressureValve == 1:
    $ ep6PressureValve = 2
    scene ep6_bowling29 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 2:
    $ ep6PressureValve = 3
    scene ep6_bowling31 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValve == 3:
    $ ep6PressureValve = 4
    scene ep6_bowling32 with Dissolve(0.1, alpha=True)
    $ renpy.pause(0.3)
if ep6PressureValveState == 0:
    me "(Might as well go all the way.)"
jump ep6KnobTurnReady
label ep6KnobTurnReady:
ro "Ready to test?"
menu:
    "[M_06_009a]": # "Sure, let's try.":
        jump ep6KnobTurnCheck
    "[M_06_009b]": # "Hang on, let me do some adjustments.":
        jump ep6KnobTurn
label ep6HoseCheck:
me "Hang on. There's a loose cable here."
me "I think I can re-attach it."
$ ep6PressureHoseFix = True
jump ep6KnobTurnReady
label ep6KnobTurnCheck:
scene ep6_bowling34 with dissolve
if ep6PressureValveState == 0:
    $ ep6PressureValveState = 1
me "Ok, try again now."
scene ep6_bowling42 with dissolve
$ renpy.pause(0.2)
scene ep6_bowling43 with Dissolve(0.1, alpha=True)
play sound bowlroll
$ renpy.pause(1.5)
scene ep6_bowling44 with Dissolve(0.1, alpha=True)
play sound bowlhit
$ renpy.pause(1)
if not ep6PressureHoseFix:
    if ep6PressureValve == 4:
        $ ep6PressureMaxUsed = True
    scene ep6_bowlingend01
    $ renpy.movie_cutscene("imov/ep6/ep6_bowling01ball.webm", delay=None, loops=0, stop_music=False)
    $ renpy.pause(0.1)
    $ renpy.pause(0.1)
    $ renpy.pause(0.1)
    $ renpy.pause(0.1)
    if ep6PressureValveState > 0:
        me "Still nothing."
    else:
        me "Yeah, that didn't do jack shit."
    if ep6PressureMaxUsed:
        scene ep6_bowling35 with dissolve
        me "I have no idea what to do though."
        me "I've cranked this bad boy up to max, and still nothing."
        scene ep6_bowling32 with dissolve
        ro "Anything else in there you can adjust?"
        me "No buttons or knobs at least. Let me check."
        call screen knob_hose
    else:
        scene ep6_bowling33 with dissolve
        me "Let me check again."
    jump ep6KnobTurn
else:
    if ep6PressureValve == 4:
        $ ep6PressureMaxUsed = True
        $ ep6PressureMaxUsedDestroy = True
        $ ep6PressureMaxOpen = False
        scene ep6_bowlingend04
        $ renpy.movie_cutscene("imov/ep6/ep6_bowling04ball.webm", delay=None, loops=0, stop_music=False)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        play sound ep6_crash1
        scene ep6_bowlingadd05 with dissolve
        $ renpy.pause(0.3)
        stop sound
        play sound ep6_crash5
        scene ep6_bowlingadd01 with dissolve
        $ renpy.pause(0.3)
        stop sound
        play sound ep6_crash3
        scene ep6_bowlingadd02 with dissolve
        $ renpy.pause(0.3)
        stop sound
        play sound ep6_crash6
        scene ep6_bowlingadd03 with dissolve
        $ renpy.pause(1)
        stop sound
        scene ep6_bowlingadd04 with dissolve
        me "Are you ok?"
        scene ep6_bowlingadd06 with dissolve
        ro "Well, that's going to leave a mark."
        scene ep6_bowling52 with dissolve
        ro "Yeah, I'm fine. And you?"
        me "Don't worry, all good here."
        scene ep6_bowling49 with dissolve
        ro "Any chance you can turn that down a bit?"
        scene ep6_bowling35 with dissolve
        me "On it."
        jump ep6KnobTurn
    elif ep6PressureValve == 3:
        ### Hide Hint ##################################################################################################################################
        hide screen general_notifytop with dissolve
        ### Hide Hint ##################################################################################################################################
        scene ep6_bowlingend03
        $ renpy.movie_cutscene("imov/ep6/ep6_bowling03ball.webm", delay=None, loops=0, stop_music=False)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        scene ep6_bowling38 with dissolve
        me "YES!"
        scene ep6_bowling39 with dissolve
        me "WE DID IT!"
        ro "Holy shit, it worked!"
        ro "That's amazing!"
        jump ep6KnobTurnEnd
    elif ep6PressureValve == 2:
        scene ep6_bowlingend02
        $ renpy.movie_cutscene("imov/ep6/ep6_bowling02ball.webm", delay=None, loops=0, stop_music=False)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        me "I think it's better now."
        me "The ball had more speed."
        scene ep6_bowling46 with dissolve
        ro "Really? That's great."
        ro "Whatever you did, keep doing it."
        scene ep6_bowling33 with dissolve
        me "Hang on."
        jump ep6KnobTurn
    else:
        scene ep6_bowlingend01
        $ renpy.movie_cutscene("imov/ep6/ep6_bowling01ball.webm", delay=None, loops=0, stop_music=False)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        $ renpy.pause(0.1)
        scene ep6_bowling33 with dissolve
        me "Let me try something else."
        jump ep6KnobTurn
label ep6KnobTurnEnd:
scene ep6_bowling40 with dissolve
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,8,4,1]
else:
    $ clockis = [[todayIs],1,4,2,5]
me "Now to fix that loose screw, before the whole rail falls apart."
ro "I'm just going to test it one more time."
scene ep6_bowling41 with dissolve
me "What's that?"
scene ep6_bowling42 with dissolve
$ renpy.pause(0.2)
scene ep6_bowling43 with Dissolve(0.1, alpha=True)
play sound bowlroll
$ renpy.pause(1.5)
scene ep6_bowling44 with Dissolve(0.1, alpha=True)
play sound bowlhit
$ renpy.pause(1)
stop music fadeout 3
scene ep6_bowling01ballsend
$ renpy.movie_cutscene("imov/ep6/ep6_bowling01balls.webm", delay=None, loops=0, stop_music=False)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_bowling53 with Dissolve(3, alpha=True)
play music ep6_robinlate
$ nowPlayingArtist = "Lightboys"
$ nowPlayingTitle = "Sleepwalking"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
if ep6DayOrder == 1:
    $ clockis = [[todayIs],1,9,3,5]
else:
    $ clockis = [[todayIs],1,5,5,1]
ro "Are you ok?"
me "Hang on. Everything's blurry."
scene ep6_bowling54 with Dissolve(3, alpha=True)
ro "That didn't look good."
scene ep6_bowling55 with dissolve
me "It's getting better. Should be fine soon."
scene ep6_bowling56 with dissolve
me "Your ice bag really helps."
scene ep6_bowling60 with dissolve
ro "I'm so sorry, I didn't know you were standing over the rails."
scene ep6_bowling61 with dissolve
me "It's not your fault. I was just going to tighten that last screw, and I didn't hear the ball coming."
me "So relax. It's nothing that a little bit of time can't fix."
scene ep6_bowling58 with dissolve
ro "At least I think we got the bowling alley fixed up."
scene ep6_bowling59 with dissolve
me "And we can talk a bit about why I came here in the first place."
scene ep6_bowling63 with dissolve
me "You've been acting all weird the last few days. Even at Lexi's place."
if ep4NightChoose == 4 or ep4NightChoose == 5:
    me "You didn't even say goodbye to me before leaving."
if ep4NightChoose == 3:
    me "I mean, it's understandable if it's because of me and Kira, but talk to me."
scene ep6_bowling62 with dissolve
ro "I'm not good at these things, ok?"
ro "Goodbyes and such."
scene ep6_bowling63 with dissolve
me "Maybe so, but there's more, isn't it."
ro "..."
scene ep6_bowling65 with dissolve
ro "What if there is?"
ro "What if I feel I can't give Kira the thing she wants the most in the whole world."
scene ep6_bowling66 with dissolve
ro "To be normal."
me "You don't think she's normal?"
ro "No, she is! But you don't get it."
scene ep6_bowling67 with dissolve
ro "I see her staring at those people when they walk past us on the street."
ro "Those normal couples."
ro "Don't you see?"
ro "I can't give her any of those things."
ro "Shit, I even robbed her of her own family."
ro "And every day I'm with her, is another day she has to go without that."
scene ep6_bowling68 with dissolve
me "Robin, she's been with you for a long time now. It's her choice."
me "And from what you both have shown me since I met you is that you really love each other."
me "So what if she gets feelings when she looks at those people."
me "She already decided that the grass is greener on your side."
me "If it wasn't, she'd tell you already."
me "So no, you didn't rob her of anything. Just ask her, and you'll notice how much you've given."
if ep4NightChoose == 3 or ep4NightChoose == 4 or ep4NightChoose == 5:
    scene ep6_bowling60 with dissolve
    ro "So what about that other obvious thing?"
scene ep6_bowling61 with dissolve
me "You two have to talk to each other."
me "Figure things out."
if ep4NightChoose == 3 or ep4NightChoose == 4 or ep4NightChoose == 5:
    me "Right now I just feel like a huge wedge."
    if ep4SetupChrisWith == 3:
        me "And that goes for Chris too."
        scene ep6_bowling60 with dissolve
        ro "Yeah, he told me."
scene ep6_bowling60 with dissolve
ro "I think she's pissed at me anyway."
scene ep6_bowling61 with dissolve
me "I haven't seen Kira pissed once since I met her."
me "Try disappointed instead."
scene ep6_bowling60 with dissolve
ro "But what would you have done?"
ro "When you love someone so much you want to do what you know is best for her."
ro "Even if she doesn't know it herself."
scene ep6_bowling61 with dissolve
if ep4NightChoose == 1:
    me "That sounds familiar, but..."
me "Just talk to her."
me "You might be surprised."
ro "Crap..."
scene ep6_bowling65 with dissolve
ro "I miss her."
scene ep6_bowling64 with dissolve
me "I know you do."
if ep6DayOrder == 1:
    $ clockis = [[todayIs],2,0,0,5]
else:
    $ clockis = [[todayIs],1,6,2,7]
if ep4SetupChrisWith <> 3:
    if ep4NightChoose == 3 or ep4NightChoose == 4 or ep4NightChoose == 5:
        scene ep6_bowling69 with dissolve
        ro "Anyway, how's your balls."
        me "Much better."
        scene ep6_bowling70 with dissolve
        me "Pretty much numbed down by now."
        scene ep6_bowling71 with dissolve
        ro "Good enough for a quickie?"
        scene ep6_bowling74 with dissolve
        me "Well, believe me... you wouldn't enjoy that at all."
        me "Cold stuff tends to shrink things."
        scene ep6_bowling73 with dissolve
        ro "Ok..."
        scene ep6_bowling74 with dissolve
        ro "Wait, what?"
        ro "It shrinks?"
        scene ep6_bowling75 with dissolve
        me "Let's just say... it's not a pretty sight."
        ro "You're actually serious..."
        scene ep6_bowling76 with dissolve
        ro "I have to see this."
        me "No you don't."
        scene ep6_bowling77 with dissolve
        ro "Yes, I have to see this."
        me "*sigh* When it comes to all the bad shit I've been through in my life..."
        scene ep6_bowling78 with dissolve
        me "...this ranks right up there."
        me "Top five, easily."
        scene ep6_bowling80 with dissolve
        ro "Awwwwwwwwwwwwww."
        scene ep6_bowling79 with dissolve
        ro "The poor little fella."
        me "Or top three."
        scene ep6_bowling80 with dissolve
        ro "It's the most sorry thing I've seen all my life."
        ro "Little peenie..."
        scene ep6_bowling79 with dissolve
        me "Top two..."
        ro "Are you sure you're not a girl?"
        scene ep6_bowling82 with dissolve
        me "Ok, that's enough of the freakshow."
        scene ep6_bowling81 with dissolve
        ro "Relax, I know just the thing."
        scene ep6_bowling83 with dissolve
        me "That is... surprisingly comfortable."
        ro "C-c-c-c-c-cold."
        me "So soft and comfy."
        scene ep6_bowling84 with dissolve
        ro "..."
        ro "Now you I recognize."
        scene ep6_robin01tit with dissolve
        ro "That didn't take long at all."
        scene ep6_bowling85 with dissolve
        ro "Welcome back."
        scene ep6_bowling86 with dissolve
        ro "So how about that quickie?"
        scene ep6_bowling88 with dissolve
        me "Robin..."
        menu:
            "[M_06_010a]": # "Go for it.":
                $ ep6HadSexWithRobin = True
                scene ep6_bowling87 with dissolve
                me "..."
                scene ep6_bowling88 with dissolve
                ro "..."
                scene ep6_bowling86 with dissolve
                me "Let me lose the clothes."
                scene ep6_robinlewd01 with fade
                ro "I love to watch..."
                scene ep6_robinlewd02 with dissolve
                ro "...and feel you..."
                scene ep6_robinlewd03 with dissolve
                ro "...going in."
                scene ep6_robinlewd04 with dissolve
                ro "Too bad I can't see you from this position."
                ro "But I can definitely feel you."
                scene ep6_robin01taken with dissolve
                me "I got an idea."
                me "You can thank Kira for it."
                ro "Mmmmh..."
                me "Look left."
                scene ep6_robinlewd05 with dissolve
                ro "..."
                ro "Oh my god..."
                ro "That is so fucking hot."
                scene ep6_robin01back with dissolve
                ro "..."
                ro "I could watch that all day."
                ro "..."
                ro "Fuck, I'm getting close."
                me "Can't have you orgasm quite yet."
                ro "You know I can do more than one."
                me "Then bend over."
                scene ep6_robinlewd06 with fade
                ro "You close?"
                scene ep6_robinlewd08 with dissolve
                me "I can push..."
                scene ep6_robinlewd07 with dissolve
                ro "Don't..."
                ro "I want to see who can go the longest without cumming."
                scene ep6_robinlewd09 with dissolve
                me "You're going down!"
                scene bg empty with fade
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                scene ep6_robinlewd10 with fade
                ro "Nghhh..."
                me "I win?"
                scene ep6_robinlewd11 with dissolve
                ro "Never!"
                scene bg empty with fade
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                scene ep6_robinlewd11 with fade
                ro "*pants* Can you push?"
                me "..."
                ro "I need to be carried..."
                scene bg empty with fade
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                scene ep6_robin02stand with fade
                ro "..."
                ro "I meant to the sofa..."
                ro "...after..."
                ro "...but this is..."
                ro "...just as good..."
                ro "..."
                ro "Please push... pretty please..."
                scene ep6_robin02standend
                $ renpy.movie_cutscene("imov/ep6/ep6_robin01stand.webm", delay=None, loops=0, stop_music=False)
                ro "I'm cum..."
                scene ep6_robinlewd18 with dissolve
                me "Me too..."
                menu:
                    "[M_06_011a]": # "Pull out.":
                        scene ep6_robinlewd19 with dissolve
                        me "..."
                        scene ep6_robinlewd22 with dissolve
                        me "..."
                    "[M_06_011b]": # "Don't pull out.":
                        $ ep6RobinCreampie = True
                        scene ep6_robinlewd19 with dissolve
                        me "..."
                        scene ep6_robinlewd20 with dissolve
                        me "..."
                scene ep6_robinlewd17 with dissolve
                ro "Holy shit..."
                scene ep6_robinlewd15 with dissolve
                ro "..."
                if ep4NightChoose == 4:
                    me "You're beautiful."
                    scene ep6_robinlewd12 with dissolve
                    ro "..."
                    scene ep6_robinlewd15 with dissolve
                    ro "You're beautiful too."
                else:
                    me "And about Kira..."
                    scene ep6_robinlewd12 with dissolve
                    ro "..."
                    scene ep6_robinlewd13 with dissolve
                    ro "Yes?"
                    me "We'll find a solution."
                    scene ep6_robinlewd14 with dissolve
                    ro "I hope so."
                scene bg empty with fade
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
                $ renpy.pause(0.5)
            "[M_06_010b]": # "Don't.":
                me "We probably shouldn't."
                ro "Maybe not..."
                me "Talk to Kira first."
                ro "Maybe..."
else:
    scene ep6_bowling73 with dissolve
    ro "Anyway, how's it going down there."
    me "Much better."
    scene ep6_bowling74 with dissolve
    me "Pretty much numbed down by this thing."
    if not ep2RejectedRobin:
        ro "Too bad we gave up on the whole friends with benefits thing."
    else:
        ro "Too bad we didn't do the friends with benefits thing."
    me "Well, believe me... you wouldn't enjoy that at all."
    me "Cold stuff tends to shrink things."
    scene ep6_bowling73 with dissolve
    ro "Ok..."
    scene ep6_bowling74 with dissolve
    ro "Wait, what?"
    ro "It shrinks?"
    scene ep6_bowling75 with dissolve
    me "Let's just say... it's not a pretty sight."
    ro "You're actually serious..."
    scene ep6_bowling76 with dissolve
    ro "I have to see this."
    me "No you don't."
    ro "Can I? Please?"
    me "Not happening!"
    ro "Awww..."
if ep6DayOrder == 1:
    scene ep6_bowling57 with dissolve
    me "You know, I was just over at MaKenzie. With Kira."
    if ep6HadSexWithKira:
        scene ep6_bowling58 with dissolve
        ro "Yeah, you fucked. I know."
        me "..."
        me "And what made you come to that conclusion?"
        scene ep6_bowling60b with dissolve
        ro "Oh, just something a little bird told me."
        scene ep6_bowling58b with dissolve
        $ renpy.pause()
        ro "See anyone familiar?"
        scene ep6_bowling58 with dissolve
        ro "*giggles* She sent it to me."
        scene ep6_bowling57 with dissolve
        me "Well, I..."
        scene ep6_bowling58 with dissolve
        ro "If there's one thing about Kira, she doesn't disappoint."
        scene ep6_bowling60b with dissolve
        ro "Here, I'll send it..."
        play sound phone_notify_sound
        show screen phone
        $ chat_robin_item = "1;1;3500;ep6_kiraworkcam"
        if chat_robin_item not in chat_robin:
            $ chat_robin.append(chat_robin_item)
        $ cam_gallery_append_item1 = "ep6_kiraworkcam"
        if cam_gallery_append_item1 not in cam_gallery:
            $ cam_gallery.append(cam_gallery_append_item1)
        $ phGallNotify = True
        $ phChatNotify = True
        $ chat_notify_robin = True
        scene ep6_bowling61 with dissolve
        me "..."
        me "Thanks."
        if ep6HadSexWithRobin:
            me "And still you wanted a quickie with me."
            scene ep6_bowling58 with dissolve
            ro "Of course I did."
            ro "Beats collecting stamps."
    else:
        scene ep6_bowling57 with dissolve
        me "She was alone at work, so I volunteered as a cook."
        scene ep6_bowling58 with dissolve
        ro "That girl is going to work herself to death."
        ro "It was sweet of you to help her though."
        ro "...and me."
    scene ep6_bowling57b with dissolve
    me "Anyway, I have to get going now. Chris is coming over at 9."
    scene ep6_bowling58 with dissolve
    ro "That thing with Linda?"
    scene ep6_bowling57b with dissolve
    me "Yup. We got to go speak with Matt at some point."
    scene ep6_bowling58 with dissolve
    ro "Better get going then. It's almost 9."
else:
    scene ep6_bowling57b with dissolve
    me "You know, I'm about to head over to Kira now."
    scene ep6_bowling60 with dissolve
    ro "Tell her..."
    ro "...or actually don't."
    ro "I have to tell her myself. If I can make myself do it."
    scene ep6_bowling61 with dissolve
    me "Just talk to her."
scene ep6_bowling58 with dissolve
ro "And give Cece a hug from me."
ro "Tell her I'll be there."
scene ep6_bowling57b with dissolve
me "Be where?"
scene ep6_bowling58 with dissolve
ro "Oh, you don't know?"
ro "Well, I'm not about to tell you anything."
scene ep6_bowling57b with dissolve
stop music fadeout 3
me "Nobody does, it seems."
scene ep6_bowlingexit01 with dissolve
me "Bye, Robin."
scene ep6_bowlingexit02 with dissolve
ro "See you around, [name]."
if not ep6PressureMaxOpen:
    scene ep6_bowlingexit03 with dissolve
    me "Huh?"
    scene ep6_bowlingexit04 with dissolve
    me "Crap..."
    scene ep6_bowlingexit05 with dissolve
    me "Ehm... Did I do that?"
    scene ep6_bowlingexit06 with dissolve
    ro "No, it's my new decoration."
    me "..."
    ro "Of course you did that."
    scene ep6_bowlingexit05 with dissolve
    me "Sorry... I'll fix that."
    ro "Bring a hammer one day, and we'll fix it together."
    ro "We make quite a team."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
if ep6DayOrder == 2:
    jump ep6DayKira
else:
    jump ep6Backyard
label ep6Backyard:
scene ep6_backyard01 with fade
play music ep6_backyard
$ nowPlayingArtist = "Micheal Shynes"
$ nowPlayingTitle = "Dark"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],2,1,1,2]
me "(He's here already.)"
scene ep6_backyard02 with dissolve
me "Hey guys. Sorry I'm late."
scene ep6_backyard03 with dissolve
ch "Don't sweat it. I'm in good company here."
scene ep6_backyard04 with dissolve
ce "Chris just told me you play the guitar?"
me "Really, Chris? You told her?"
scene ep6_backyard05 with dissolve
ch "Well, somebody had to."
me "I know one song."
scene ep6_backyard03 with dissolve
ce "I haven't even seen a guitar."
me "It's in the closet."
ce "So you're going to play?"
me "Nope. I have terrible stage fright."
ce "Aww...."
scene ep6_backyard06 with dissolve
ce "Anyway, how was your day?"
scene ep6_backyard12 with dissolve
me "I'm beat!"
me "Kira was alone at MaKenzie, so I volunteered as a cook."
me "I have no idea how many burgers I've made today."
me "And at Robin's bowling alley we fixed her machinery."
scene ep6_backyard06 with dissolve
ce "Really? You fixed it?"
scene ep6_backyard08 with dissolve
me "Yup. I only had to sacrifice a testicle to the bowling ball gods, and that was it."
ce "..."
scene ep6_backyard09 with dissolve
ce "You dropped a bowling ball on your..."
me "Not quite, but close enough."
scene ep6_backyard03 with dissolve
ch "Man, stop it. I'm hurting just hearing about it."
scene ep6_backyard10 with dissolve
ce "Ok, this is a guy discussion. I'll be inside."
scene ep6_backyard11 with dissolve
$ clockis = [[todayIs],2,1,2,0]
me "You brought beer?"
ch "No, this was your turn?"
scene ep6_backyard13 with dissolve
me "Crap, forgot all about it."
ch "Don't sweat it. I think I've had my share of alcohol this summer."
me "Yeah, you're right about that."
scene ep6_backyard20 with dissolve
ch "And we'll get a refill soon anyway."
me "Refill?"
scene ep6_backyard14 with dissolve
ch "Oh..."
me "Hang on, both Kira and Robin said something about Cece."
scene ep6_backyard21 with dissolve
ch "My lips are sealed."
ch "Ask Cece."
me "I thought you were supposed to be my friend."
scene ep6_backyard16 with dissolve
ch "Yeah, guilt tripping is not going to work."
scene ep6_backyard14 with dissolve
me "Anyway, do you remember that day at MaKenzie when we met Kira for the first time?"
scene ep6_backyard15 with dissolve
ch "You mean, when I had to drag her over to our table?"
me "..."
scene ep6_backyard16 with dissolve
me "Today she told me what you said to her, to get her over to me."
scene ep6_backyard17 with dissolve
ch "Well, damn you Kira..."
scene ep6_backyard18 with dissolve
me "Just wanted to say thank you for it. For always having my back."
scene ep6_backyard21 with dissolve
ch "Hey, don't make this weird now. Being weird is my trademark, not yours."
ch "And no, I'm still not telling about that thing with Cece."
scene ep6_backyard20 with dissolve
me "Damn... Was worth a try."
scene ep6_backyard22 with dissolve
ch "She has a way of making people smile, hasn't she."
me "She does."
scene ep6_backyard23 with dissolve
ch "I hate being the one to say this, but you know she needs help, right?"
ch "Professional help."
scene ep6_backyard24 with dissolve
me "I think she's getting better though."
ch "Probably. But you never know."
scene ep6_backyard25 with dissolve
ch "You still think about that day... on the bridge?"
me "I'll never forget it."
scene ep6_backyard26 with dissolve
me "It was one of the most intense things I've ever experienced."
me "There's something I don't quite understand though. Something she told me about it later on."
$ clockis = [[todayIs],2,1,3,5]
if ep4NightChoose == 1:
    scene ep6_backyard28 with dissolve
    me "But I know I love her."
else:
    scene ep6_backyard27 with dissolve
    me "I can't help but care a lot for her."
if ep4SetupChrisWith == 3:
    scene ep6_backyard20 with dissolve
    me "What happened with you and Robin?"
    scene ep6_backyard17 with dissolve
    ch "I think it was a summer fling."
    scene ep6_backyard18 with dissolve
    me "So, it's over?"
    scene ep6_backyard15 with dissolve
    ch "Dunno. It started with the whole friends with benefits speech. It was a lot of fun in the start."
    ch "But now I feel like I'm fucking things over between her and Kira."
    scene ep6_backyard14 with dissolve
    ch "It feels wrong in a way."
    if ep4NightChoose == 3:
        me "I know what you mean."
        me "I feel responsible myself, being with Kira."
    me "But you like Robin?"
    scene ep6_backyard15 with dissolve
    ch "Stupid question, man. Of course I do. I'm her Batman."
elif ep4SetupChrisWithHo:
    scene ep6_backyard20 with dissolve
    me "What happened with you and Holly?"
    if ep5HollyComplete == 1 or ep5HollyComplete == 2:
        scene ep6_backyard18 with dissolve
        ch "You fucked her, that's what happened."
        me "Eh..."
        scene ep6_backyard21 with dissolve
        ch "Don't sweat it, we were never a thing anyway."
        ch "I would have done the same."
        me "No you wouldn't."
    else:
        scene ep6_backyard14 with dissolve
        ch "Nothing really. Not while we were at Lexi's place."
        scene ep6_backyard21 with dissolve
        ch "But we started messaging last night."
        ch "And somehow ended up talking on the phone until early morning today."
        scene ep6_backyard20 with dissolve
        me "Nice, man."
elif ep4SetupChrisWithLi:
    scene ep6_backyard20 with dissolve
    me "How's it going with you and Linda?"
    scene ep6_backyard21 with dissolve
    ch "Duude, she's awesome."
    ch "And by the way, can you try and fish a bit about where she's been."
    scene ep6_backyard20 with dissolve
    me "Will do. She told Cece she would come here later. Probably very late. I can try talking to her then."
    ch "..."
    me "She will probably spend the night here."
    ch "..."
    me "You know we sleep in the same bed, right."
    scene ep6_backyard25 with dissolve
    ch "Just keep your privates away from her privates."
    me "And she always sleeps topless."
    scene ep6_backyard21 with dissolve
    ch "Ok, just stop it!"
scene ep6_backyard14 with dissolve
me "But Matt..."
scene ep6_backyard15 with dissolve
ch "Why don't we just get it over with. Head over there right now. It's just a few blocks away."
scene ep6_backyard14 with dissolve
me "Do you think he did anything to Linda?"
scene ep6_backyard17 with dissolve
ch "He's been an asshole to us since forever, but I never took him for anyone that would stoop that low."
me "But if he did..."
scene ep6_backyard18 with dissolve
ch "Then he's toast."
scene ep6_backyard17 with dissolve
me "I'm getting sick to my stomach just thinking about it."
scene ep6_backyard19 with dissolve
ch "And angry. If he says one wrong thing about that, I don't know what I'll do."
scene ep6_backyard29 with dissolve
$ clockis = [[todayIs],2,1,4,7]
me "..."
ma "Guys..."
scene ep6_backyard30 with dissolve
ma "Can I have a word with you?"
scene ep6_backyard31 with dissolve
me "Matt?"
me "What the hell are you doing here."
scene ep6_backyard32 with dissolve
ma "I don't want any trouble."
ch "We've been saying that to you for a decade."
scene ep6_backyard33 with dissolve
ma "I'll make it quick and then get out of your face."
ma "But I really want to apologize to both of you for being a complete asshole."
scene ep6_backyard34 with dissolve
me "..."
scene ep6_backyard35 with dissolve
ch "..."
scene ep6_backyard36 with dissolve
ma "I just wanted to let you know that I won't give you any trouble again, ever."
ma "And I'm very sorry for all the shit I put you through."
scene ep6_backyard33 with dissolve
me "Well, excuse me for taking that with a grain of salt."
scene ep6_backyard37 with dissolve
ma "That's fair. But I'm done with that bullshit. I promise."
scene ep6_backyard39 with dissolve
me "I haven't got any business with you."
me "But Linda told me you two used to be very good friends."
me "And you'd better answer me right now, do you have that ring of hers?"
scene ep6_backyard38 with dissolve
ma "I do..."
scene ep6_backyard43 with dissolve
ch "And just how the flying fuck did you end up with her clit ring?"
scene ep6_backyard41 with dissolve
ma "..."
ma "Her cl..."
ma "Oh fuck, this is bad."
scene ep6_backyard42 with dissolve
me "Did you..."
scene ep6_backyard41 with dissolve
ma "No! NO!"
ma "Listen, I've done some bad shit in my life."
ma "But I would never do anything bad to Linda."
ma "Or that, to anyone!"
scene ep6_backyard44 with dissolve
ma "I found that ring on the bathroom floor, and all those shitty things from school came back."
ma "I took the ring and hightailed out of there. I shouldn't have, but I did."
scene ep6_backyard39 with dissolve
ch "So what's up with the message you sent her a few weeks ago?"
scene ep6_backyard38 with dissolve
ma "I took a picture of the ring and sent it to her, with a message that I wanted to give it back."
scene ep6_backyard41 with dissolve
ma "Hear me out, I never did anything to Linda."
ma "I never even knew about the... other thing."
scene ep6_backyard45 with dissolve
$ clockis = [[todayIs],2,1,5,4]
ce "Hey Matt."
me "..."
ma "Cece."
scene ep6_backyard46 with dissolve
ce "I take it you listened to what I said, and there's no more stupid shit."
ma "Yes, Miss."
scene ep6_backyard47 with dissolve
ce "Then come over here."
scene ep6_backyard48 with dissolve
me "Cece..."
scene ep6_backyard49 with dissolve
ce "It's ok."
scene ep6_backyard50 with fade
ma "You were right. I'm sorry."
ma "I really am. And I didn't..."
scene ep6_backyard52 with dissolve
ce "Look at me."
ma "..."
scene ep6_backyard51 with dissolve
ce "I'll talk to Linda."
ma "..."
ce "And I'm glad you listened."
ma "Thank you."
scene ep6_backyard53 with dissolve
ce "..."
scene ep6_backyard54 with dissolve
ce "..."
scene ep6_backyard55 with dissolve
ce "*hums* O-ah... o-ah... o-o-o-ahh, o-ah... o-ah... o-o-o-ahh."
scene ep6_backyard56 with dissolve
me "..."
scene ep6_backyard57 with dissolve
ch "..."
scene ep6_backyard56 with dissolve
me "..."
scene ep6_backyard58 with dissolve
ch "..."
scene bg empty with fade
$ clockis = [[todayIs],2,2,0,8]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_backyard59 with fade
me "..."
scene ep6_backyard60 with dissolve
me "Yeah... I got nothing..."
ch "Me neither."
scene ep6_backyard61 with dissolve
me "So... I guess that's settled."
ch "The look on his face though."
scene ep6_backyard62 with dissolve
me "What do you think of his excuse."
ch "I mean, it could be plausible."
scene ep6_backyard63 with dissolve
ch "It doesn't excuse him locking me in the locker room for a night."
me "Or not backing up when Linda asked him to."
scene ep6_backyard62 with dissolve
ch "Exactly."
ch "But she invited him there in the first place."
me "True."
ce "*singing* Gina works the diner all daaaaaaaaaay."
scene ep6_backyard64 with dissolve
me "Let me guess. You talked to Cece about 80's music before I got here?"
ch "Well..."
scene ep6_backyard66 with dissolve
ch "I might have mentioned the glorious hair they all had back then."
scene ep6_backyard67 with dissolve
me "Oh, don't mention hair please. I'm still struggling with the gray syndrome."
me "'Arctic White' my ass."
scene ep6_backyard68 with dissolve
ch "No. Arctic White is the nickname of my ass. Ain't nothing whiter."
me "Need to know basis, Chris. Need to know only."
scene ep6_backyard69 with fade
ch "So this is it, eh?"
scene ep6_backyard70 with dissolve
me "Come again?"
ch "The end of the perfect summer."
me "Pretty much I guess. We had some fun at Lexi's, that's for sure."
scene ep6_backyard69 with dissolve
ch "..."
ch "So why do I feel there's a thunderstorm coming?"
me "Don't say that."
ch "I know you feel it too."
scene ep6_backyard59 with dissolve
$ clockis = [[todayIs],2,2,1,9]
stop music fadeout 5
me "..."
ce "*singing* Liiiiviiin' on a prayer!"
scene ep6_backyard61 with dissolve
me "There she goes again."
ch "I think that's my cue to head off. It's going to be a long day tomorrow."
me "Have fun, man. Thanks for coming over."
scene bg empty with fade
$ clockis = [[todayIs],2,2,2,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_ceceevening
$ nowPlayingArtist = "Owls and Lions"
$ nowPlayingTitle = "Love and Energy"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_ceceapartment01 with fade
me "So, Cece. How about we talk a bit about what happened out there with Matt."
scene ep6_ceceapartment02 with dissolve
ce "I've got a better idea."
ce "How about movie night."
me "Movie night?"
ce "Yeah, I have the perfect movie picked out."
scene ep6_cecetap with dissolve
ce "Come watch with me?"
me "Sure. So let me guess..."
me "...Sleepless in Seattle?"
me "...Dirty Dancing?"
me "...Bridget Jones Diary?"
scene ep6_ceceapartment05 with dissolve
ce "I think you'll be surprised."
me "I should warn you, I might fall asleep though. It's been a long day."
scene ep6_ceceapartment06 with dissolve
me "So, which is it?"
scene ep6_ceceapartment07 with dissolve
me "..."
scene ep6_ceceapartment08 with dissolve
me "No way!"
me "No retreat, No surrender?"
scene ep6_ceceapartment09 with dissolve
me "How did you even know of it."
ce "I have a dad, remember? He showed me all the classics."
scene ep6_ceceapartment10 with dissolve
me "I'd even forgotten it existed. Can't remember last time I watched it."
me "Little known fact, the US version was called Karate Tiger..."
me "...which was fitted with a completely different soundtrack, inspired by the metal scene..."
scene ep6_ceceapartment11 with dissolve
ce "...but the European counterpart version with it's euro-pop synth soundtrack made it's way back to the US..."
ce "...giving the real movie of 'No Retreat, No Surrender', cult status."
if ep4NightChoose == 4:
    me "I adore you so much right now."
else:
    me "You are officially my new favorite person in the world."
me "How do you even know these things. That's not even on the internet."
ce "Like I said, I have a dad."
scene ep6_ceceapartment15 with dissolve
$ clockis = [[todayIs],2,2,2,8]
me "I'm definitely not falling asleep to this one."
scene ep6_ceceapartment13 with dissolve
ce "But hush, it's starting now."
scene ep6_ceceapartment14 with dissolve
me "You know this is streaming, right? There's no 'starting now'."
scene ep6_ceceapartment13 with dissolve
ce "Hush."
scene ep6_ceceapartment12 with dissolve
me "..."
scene ep6_ceceapartment14 with dissolve
me "Crap."
scene ep6_ceceapartment13 with dissolve
ce "What?"
scene ep6_ceceapartment14 with dissolve
me "I forgot to ask Matt about the ring."
scene ep6_ceceapartment13 with dissolve
ce "Linda's ring?"
scene ep6_ceceapartment14 with dissolve
me "Yeah."
scene ep6_ceceapartment12 with dissolve
me "..."
scene ep6_ceceapartment14 with dissolve
me "I think she's a bit overly nostalgic about that ring though."
me "It's not even a real ring. Just something from a cereal box."
scene ep6_ceceapartment13 with dissolve
ce "Nostalgia is a very strong feeling. It can keep you going when things gets dark. Like you said about my hair."
scene ep6_ceceapartment14 with dissolve
me "It tickles me when you sleep and slobber all over me."
scene ep6_ceceapartment13 with dissolve
ce "Exactly... Minus the slobbering... It's not the ring itself, but the feeling she felt that day you gave it to her."
ce "It could be nuts and bolts for all she cares, but she'll never forget the feeling."
scene ep6_ceceapartment14 with dissolve
me "I'd forgotten all about it."
scene ep6_ceceapartment13 with dissolve
ce "And still to her, she'll remember it for the rest of her life."
ce "Funny, isn't it."
scene ep6_ceceapartment14 with dissolve
me "Kind of. But I still think she's overdoing it."
scene ep6_ceceapartment13 with dissolve
ce "It's like this movie."
ce "It's not Oscar material, the acting isn't great, the script is trope after trope."
ce "And still we love it. Because of the feeling we got when we saw it the first time."
scene ep6_ceceapartment14 with dissolve
me "That... does make sense though."
scene ep6_ceceapartment12 with dissolve
ce "..."
scene ep6_ceceapartment13 with dissolve
ce "Ok, so I know this guy is supposed to play the asshole, but he's kinda hot though."
scene ep6_ceceapartment14 with dissolve
me "Hush."
scene ep6_ceceapartment13 with dissolve
ce "Really?"
scene ep6_ceceapartment14 with dissolve
me "Sssssssssssssssssssssssssssssssshhhhhhhhhh."
hide screen phone
scene bg empty with fade
$ clockis = [[todayIs],2,3,2,7]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_ceceapartment16 with fade
ce "Waaaaait for it..."
me "..."
scene ep6_ceceapartment17 with dissolve
ce "And down he goes."
scene ep6_ceceapartment18 with dissolve
ce "That's gotta hurt."
scene ep6_ceceapartment19 with dissolve
ce "..."
scene ep6_ceceapartment20 with dissolve
me "..."
scene ep6_ceceapartment23 with dissolve
ce "'Definitely not falling asleep.'"
scene ep6_ceceapartment22 with dissolve
ce "*sigh*"
if ep4NightChoose == 1:
    scene ep6_ceceapartment21 with dissolve
    ce "Of course you're falling asleep, now that I'm horny!"
scene ep6_ceceapartment24 with dissolve
ce "..."
scene ep6_ceceapartment25 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.4)
scene ep6_ceceapartment24 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.3)
scene ep6_ceceapartment25 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.6)
scene ep6_ceceapartment24 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.3)
scene ep6_ceceapartment26 with Dissolve(0.1, alpha=True)
ce "Bedtime it is."
scene bg empty with fade
$ clockis = [[todayIs],2,3,4,0]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_ceceapartment34 with fade
ce "*exhales*"
scene ep6_ceceapartment35 with dissolve
ce "Christ, you're heavy."
ce "What was your diet those two years Steph was away."
ce "A ton of Protein Powder?"
scene ep6_ceceapartment27 with dissolve
ce "And you're calling me a heavy sleeper."
scene ep6_ceceapartment28 with dissolve
ce "..."
scene ep6_ceceapartment28b with Dissolve(1, alpha=True)
ce "..."
scene ep6_ceceapartment29 with dissolve
$ renpy.pause(0.4)
scene ep6_ceceapartment30 with dissolve
$ renpy.pause(0.4)
scene ep6_ceceapartment29 with dissolve
$ renpy.pause(0.4)
scene ep6_ceceapartment30 with dissolve
$ renpy.pause(0.4)
scene ep6_ceceapartment31 with dissolve
ce "Hmmm..."
scene ep6_ceceapartment32 with dissolve
ce "Oh, don't look at me like that.\nIt's not like you haven't had to make a choice like this before."
scene ep6_ceceapartment33 with dissolve
stop music fadeout 3
if ep4NightChoose == 1:
    ce "Get out of here, you'll get yours tomorrow."
else:
    ce "Get out of here, let me have my fun."
scene bg empty with fade
$ clockis = [[todayIs],0,1,2,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_lindanight
$ nowPlayingArtist = "Jane & The Boy"
$ nowPlayingTitle = "Hostage"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_nightinter01 with fade
$ renpy.pause(0.6)
scene ep6_nightinter02 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter03 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter04 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter05 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter06 with dissolve
$ renpy.pause(2)

scene ep6_nightinter07 with dissolve
$ renpy.pause(2)


scene ep6_nightinter08 with dissolve
$ renpy.pause(2)
show ep6_nightinter09 at imgSlide_ep6LindaHome_a
show ep6_nightinter10 at imgSlide_ep6LindaHome_b
$ renpy.pause(6)


scene ep6_nightinter11
hide ep6_nightinter10
hide ep6_nightinter09
$ renpy.pause(4)


scene ep6_nightinter12 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter13 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter14 with dissolve
$ renpy.pause(3)
scene ep6_nightinter16 with fade
$ renpy.pause(3)

scene ep6_nightinter15 with dissolve
$ renpy.pause(1.5)

scene ep6_nightinter17 with dissolve
$ renpy.pause(1.5)

scene ep6_nightinter18 with dissolve
$ renpy.pause(1.5)

scene ep6_nightinter19 with dissolve
$ renpy.pause(2)

scene ep6_nightinter20 with dissolve
$ renpy.pause(2)
scene ep6_nightinter21 with dissolve
li "That's one way to make a buck...{w=3}{nw}"
scene ep6_nightinter22 with dissolve
$ renpy.pause(2)

scene ep6_nightinter23 with dissolve
$ renpy.pause(2)

scene ep6_nightinter24 with dissolve
$ renpy.pause(0.6)
scene ep6_nightinter25 with dissolve
$ renpy.pause(2)
scene ep6_nightinter26 with dissolve
li "The things I do for you.{w=3}{nw}"
scene ep6_nightinter27 with dissolve
$ renpy.pause(2)
scene ep6_nightinter28 with dissolve
$ renpy.pause(2)
scene ep6_nightinter29 with dissolve
$ renpy.pause(1)
scene ep6_nightinter30 with dissolve
li "..."
stop music fadeout 4
scene ep6_nightinter31 with fade
li "(This makes it worth it though.)"
scene ep6_nightinter32 with dissolve
li "(Oh, and...)"
scene ep6_nightinter33 with dissolve
li "(Don't eat Cece's hair.)"
scene ep6_nightinter34 with dissolve
me "Snore..."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ todayIs = 13
$ clockis = [[todayIs],1,0,0,4]
$ nukeStoriesAdd = "27;OfficialLexi;ep6_lexicece2;I miss this gorgeous ponytail sweetie."
if nukeStoriesAdd not in nukeStories:
    $ nukeStories.append(nukeStoriesAdd)
$ nukeCommentsAdd = "27;2701;SixFeetUnder;Miss you too, Lexi! <3"
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "27;2702;OfficialLexi;omg..."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "27;2703;OfficialLexi;OMG!"
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "27;2704;Exotic Titan;Oh, I'm getting all kinds of custom ideas now."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeStoriesAdd = "28;OfficialLexi;ep6_lexicece;Shit, I sent the wrong picture. How to delete. CECE! HELP!"
if nukeStoriesAdd not in nukeStories:
    $ nukeStories.append(nukeStoriesAdd)
$ nukeCommentsAdd = "28;2801;Kirasmatic;Swipe right and there's a delete thing..."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "28;2802;OfficialLexi;I did. There was a share, and now it's on PonyGram too."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "28;2803;SixFeetUnder;Looooooool."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "28;2804;AssesAndBreasts;Keep going. I've got popcorn."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
show screen phone
scene ep6_lindamorning01 with fade
play music ep6_lindamorning
$ nowPlayingArtist = "Brick Fields"
$ nowPlayingTitle = "Gotta Sing Your Song"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
li "..."
me "I know you're awake."
scene ep6_lindamorning02 with dissolve
li "How did you know?"
me "You stopped snoring."
scene ep6_lindamorning03 with dissolve
li "Oh, really? Have you heard yourself snoring?"
me "No. I'm sleeping when I snore."
if ep4NightChoose == 6:
    scene ep6_lindamorning02 with dissolve
    me "Missed you."
    scene ep6_lindamorning03 with dissolve
    li "Missed you too."
    me "And Linda?"
    li "Mhmm?"
    me "What are you not telling me?"
    scene ep6_lindamorning04 with dissolve
    li "Not telling?"
    me "You've been gone for two nights and a day. The day I can understand, but not the two nights."
    li "I had an errand."
    me "That makes even less sense."
    scene ep6_lindamorning05 with dissolve
    li "If I tell, it ruins the surprise."
    me "Mhmmm. But if something is wrong, tell me."
    li "Okay."
    me "Promise?"
    li "Promise! Jeez."
    me "Also... I'm a bit moody."
    scene ep6_lindamorning04 with dissolve
    li "Pissed?"
    me "No, other kind of moody."
    scene ep6_lindamorning03 with dissolve
    li "Oh, that kind of moody."
    li "Why don't we just cuddle for a bit instead?"
    li "We might wake Cece."
    me "Ok, who are you, and what have you done to my Linda."
    scene ep6_lindamorning06 with dissolve
    me "Also, Cece's in the shower."
    scene ep6_lindamorning07 with dissolve
    li "I just want to have your arm around me right now."
    me "Yeah, that works too."
    scene ep6_lindamorning08 with dissolve
    li "You sound disappointed."
    me "Not really."
    scene ep6_lindamorning09 with dissolve
    li "Here... Enjoy yourself."
    li "Hopefully it's just as good as Cece's?"
    me "Cece's?"
    me "This is a trick question, isn't it."
    scene ep6_lindamorning10 with dissolve
    li "You were spooning, and cupping her naked breast last night when I got here."
    me "Shit, I didn't mean to do that. It must have been a..."
    li "...reflex? *laughs* It was funny and cute though."
    me "I hope she thought that too."
    li "She did."
    scene ep6_lindamorning09 with dissolve
    me "She said that?"
    li "No, she was holding your hand closer."
    scene ep6_lindamorning10 with dissolve
    me "Honestly, I still worry she's going to sneak out in the middle of the night."
    li "It's fine, really. You're cute showing your protective side."
    ce "Christ, I've been in the shower for a full hour just so you two would have enough time to do your thing, and you haven't even started yet?"
    scene ep6_lindamorning11 with dissolve
else:
    scene ep6_lindamorning03 with dissolve
    me "..."
    me "Linda?"
    li "Mhmm?"
    me "What's the surprise."
    scene ep6_lindamorning04 with dissolve
    li "Surprise?"
    me "Cece said you'd been out because of some surprise."
    me "Honestly, I was a bit worried."
    me "You've been gone for two nights and a day. The day I can understand, but not the two nights."
    scene ep6_lindamorning05 with dissolve
    li "I had an errand."
    me "That makes even less sense."
    scene ep6_lindamorning15 with dissolve
    li "If I tell, it ruins the surprise."
    me "Mhmmm. But if something is wrong, tell me."
    li "Okay."
    scene ep6_lindamorning12 with dissolve
    me "Promise?"
    li "Promise! Jeez."
    if ep4NightChoose == 1:
        scene ep6_lindamorning13 with dissolve
        li "I see you and Cece are doing just fine."
        me "I think we are."
        me "And you could see that from us sleeping?"
        li "You were spooning and cupping her naked breast."
        li "I know she likes it."
        scene ep6_lindamorning14 with dissolve
        me "She said so?"
        li "No, but she was holding your hand closer."
        me "Part of me is still worried she might walk out that door in the middle of the night, I guess."
        li "You've always had a protective side. It shows even when you sleep."
        scene ep6_lindamorning13 with dissolve
        li "And do you have hair in your mouth, by any chance?"
        me "Now that you mention it..."
        scene ep6_lindamorning14 with dissolve
        li "That's what you get for eating her hair."
        me "Well, I love her hair too."
    else:
        scene ep6_lindamorning13 with dissolve
        li "Also, how was Cece's breast?"
        me "..."
        me "This is a trick question, isn't it."
        scene ep6_lindamorning12 with dissolve
        li "You were spooning and cupping her naked breast when I got home last night."
        me "Shit... That must have been a..."
        li "...reflex? *laughs* It was funny and cute though."
        me "I hope she thought so too."
        li "She did."
        scene ep6_lindamorning14 with dissolve
        me "She said that?"
        li "No, she was holding your hand closer."
        me "Honestly, I think I still worry she's going to sneak out in the middle of the night."
        li "You've always had a protective side. It shows even when you sleep."
        me "..."
        me "Think you could maybe not tell..."
        scene ep6_lindamorning13 with dissolve
        if ep4NightChoose == 2:
            li "...Lexi about it?"
            me "I mean, it was not like I cheated on her."
            li "It would make for a great party story..."
            li "...or truth or dare."
            me "How about I throw in a massage as a bargaining chip?"
            li "Deal."
            scene ep6_lindamorning14 with dissolve
            me "But then you would have to not tell her about the massage."
            if ep4SetupChrisWithLi:
                me "And Chris."
            li "So, another massage to add to that?"
            me "..."
            me "This is getting out of hand, fast."
            li "Calm down, I won't tell. Even if it was just cute."
        elif ep4NightChoose == 3:
            li "...Kira about it?"
            scene ep6_lindamorning14 with dissolve
            me "Never mind, Kira would think it was cute too."
        elif ep4NightChoose == 4:
            li "...Robin about it?"
            scene ep6_lindamorning14 with dissolve
            me "Never mind, I don't think Robin would care about it."
        elif ep4NightChoose == 5:
            li "...Kira and Robin about it?"
            scene ep6_lindamorning14 with dissolve
            me "Never mind. They would have laughed and then Nuked it."
        elif ep4NightChoose == 7:
            li "...Steph about it?"
            li "She wouldn't care. She's just as protective as you are."
            me "So you're saying she'd spoon Cece and cup her breast if she was here instead of me?"
            li "More like standing guard by the door."
            scene ep6_lindamorning14 with dissolve
            me "True."
    ce "Christ, I've been in the shower for a full hour and you're still in bed?"
    scene ep6_lindamorning16 with dissolve
$ clockis = [[todayIs],1,0,2,4]
me "Morning, Cece."
me "And wow, you look amazing."
scene ep6_lindamorning17 with dissolve
ce "Like it?"
scene ep6_lindamorning18 with dissolve
li "I love it! But you never wear dresses."
ce "It's because of my enormous thighs and weird ass."
me "Yeah... right..."
scene ep6_lindamorning19 with dissolve
li "You should definitely wear more of these."
ce "Will you... put on something?"
scene ep6_lindamorning20 with dissolve
li "So cute!"
ce "Waving those around without a care in the world."
scene ep6_lindamorning21 with dissolve
li "Yeah, yeah. I'll put something on. I have just the dress in mind."
li "Then lets go out and enjoy the nice weather."
ce "You coming, [name]?"
li "He'll need a few minutes."
ce "No blood in your arms again?"
scene ep6_lindamorning23 with dissolve
me "Yeah..."
scene ep6_lindamorning24 with dissolve
me "..."
scene ep6_lindamorning23 with dissolve
me "All the blood is somewhere else."
scene ep6_lindamorning22 with dissolve
ce "I don't get it."
li "Morning wood, Cece."
ce "Oh, that."
if ep4NightChoose == 1:
    ce "It's nothing I haven't seen before anyway."
    li "Hang on... You've fucked haven't you."
    ce "Of course."
    li "Can you take the full size of his dick? It's not like he's small."
    scene ep6_lindamorning25 with dissolve
    ce "How do you know what size he is."
    li "We used to play around in school a lot. So I know perfectly well how big he is."
    scene ep6_lindamorning26 with dissolve
    ce "You fucked him?"
    li "No, just experimented a lot with him."
    li "I enjoyed it. And I think he enjoyed it more."
    li "But that dick is a mouthful."
    scene ep6_lindamorning27 with dissolve
    me "Ok, can you not talk about my dick like it's the most natural conversation topic in the world?"
    me "This is so weird."
    scene ep6_lindamorning25 with dissolve
    ce "..."
    li "..."
    ce "Best way is to just slide him in bit by bit so you get adjusted."
    scene ep6_lindamorning26 with dissolve
    ce "Then go nuts afterwards."
    li "I'm impressed."
    me "..."
elif ep4NightChoose == 6:
    ce "I mean, it shows that well? He's not that big, is he?"
    li "He is!"
    ce "So it hurts?"
    scene ep6_lindamorning25 with dissolve
    li "I mean, he hits bottom every single stroke."
    li "It's like pain, that becomes pleasure."
    ce "Pleasure-pain!"
    scene ep6_lindamorning26 with dissolve
    li "Exactly."
    li "But when he starts going all in, then boy..."
    scene ep6_lindamorning27 with dissolve
    me "Ok, can you not talk about my dick like it's the most natural conversation topic in the world?"
    me "This is so weird."
    scene ep6_lindamorning25 with dissolve
    li "..."
    ce "..."
    li "And then you have anal, which is a totally different story altogether."
    scene ep6_lindamorning26 with dissolve
    ce "You took all of that up your ass?"
    me "..."
else:
    ce "I mean, it shows that well? He's not that big, is he?"
    li "He is!"
    ce "How do you know what size he is."
    li "We used to play around in school a lot. So I know perfectly well how big he is."
    scene ep6_lindamorning25 with dissolve
    ce "You fucked him?"
    li "No. But I learned blowjobs on him."
    scene ep6_lindamorning26 with dissolve
    li "I got to do a whole lot of practicing..."
    li "I mean, it was like three times a week at times."
    scene ep6_lindamorning27 with dissolve
    me "Ok, can you not talk about my dick like it's the most natural conversation topic in the world?"
    me "This is so weird."
    scene ep6_lindamorning25 with dissolve
    ce "..."
    li "..."
    ce "So what's your best blowjob tip."
    scene ep6_lindamorning26 with dissolve
    li "Let your tongue work the frenulum, while your hands work the shaft and testies. Then go as deep as you can manage."
    ce "Frenulum?"
    me "..."
    scene ep6_lindamorning25 with dissolve
    me "(Frenulum?)"
scene bg empty with fade
$ clockis = [[todayIs],1,2,2,1]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_lindamorning30 with fade
me "(It's really nice weather today.)"
scene ep6_lindamorning29 with dissolve
me "(That gives me the perfect idea for where we can go.)"
me "..."
scene ep6_lindamorning28 with dissolve
me "(If they ever get ready, that is.)"
li "You ready?"
scene ep6_lindamorning31 with dissolve
me "..."
scene ep6_lindamorning32_main
show ep6_lindamorning33 at imgSlide_ep6HomeOut_a
show ep6_lindamorning32 at imgSlide_ep6HomeOut_b
$ renpy.pause(3)
me "Finally. You sure took your sweet time."
scene ep6_lindamorning34_main with dissolve
hide ep6_lindamorning33
hide ep6_lindamorning32
li "Did he... just complain about how long it took for us to get ready?"
ce "He sure did."
li "Like he thinks this just happens all by itself?"
ce "He does not know the struggles."
scene ep6_lindamorning36 with dissolve
me "I mean..."
scene ep6_lindamorning35 with dissolve
ce "He means?"
li "He means to say that 'he's been ready for ages', and anytime soon he'll say something like 'let's go', followed by '2 minutes... I just need to get my jacket'."
scene ep6_lindamorning36 with dissolve
li "Men..."
scene ep6_lindamorning37 with dissolve
stop music fadeout 4
ce "*giggles*"
me "..."
scene ep6_lindamorning36 with dissolve
me "I'll be right there."
scene bg empty with fade
$ clockis = [[todayIs],1,4,2,0]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_hike03 with fade
me "So, like the spot?"
scene ep6_hike06 with dissolve
ce "Like it? I love trips like these."
scene ep6_hike07 with dissolve
li "I mean, you're overestimating my fitness level."
li "I'm beat."
scene ep6_hike02 with dissolve
me "We can take a break."
li "No, I'm better now. But that hill back there."
scene ep6_hike02 with dissolve
li "And why are you wearing that age old jacket."
me "These jackets will never go out of fashion."
scene ep6_hike01 with dissolve
li "Here we are dressing up in nice new dresses and you..."
me "...put on jeans and a jacket. Perks of being a guy."
scene ep6_hike04 with dissolve
li "Phew."
ce "Just smell this nice air."
scene ep6_hike05 with dissolve
ce "We used to go hiking all the time back home."
scene ep6_hike01 with dissolve
ce "We always complained about it when mom and dad said it was time to go."
ce "But when we got there, it was all worth it and then some."
me "Well, Ladies. Hook up your arms with mine..."
scene ep6_hike08 with dissolve
me "...because we're almost there."
li "That's such a bad trick to get us both in your arms."
me "Well, it worked, didn't it?"
scene ep6_hike09 with fade
me "We're here."
scene ep6_hike10 with dissolve
li "Ok, this is nice."
scene ep6_hike11 with dissolve
ce "Nice?"
scene ep6_hike12 with dissolve
ce "It's fantastic!"
scene ep6_hike13 with dissolve
me "And there she goes."
li "..."
scene ep6_CeceRunRight with dissolve
ce "Yaaaaaaayyyy."
me "She's never going to stop doing those thing, is she."
li "I hope not."
scene ep6_CeceRunLeft with dissolve
ce "I love this!"
ce "Look at that water!"
scene ep6_hike22 with dissolve
me "..."
scene ep6_hike21 with dissolve
ce "Oh, fuck this. I'm doing it."
scene ep6_hike23 with dissolve
li "What is she..."
scene ep6_hike24 with dissolve
$ renpy.pause(0.5)
scene ep6_hike23 with dissolve
$ renpy.pause()
scene ep6_hike31 with dissolve
$ renpy.pause()
$ clockis = [[todayIs],1,4,5,5]
play music ep6_hikedip
$ nowPlayingArtist = "CustomMelody"
$ nowPlayingTitle = "Go Win It"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_hike23
$ renpy.movie_cutscene("imov/ep6/ep6_cece01bath.webm", delay=None, loops=0, stop_music=False)
li "Cece!"
li "What are you doing?"
scene ep6_hike32 with dissolve
ce "What does it look like I'm doing?"
li "You're going to... wade?"
scene ep6_CeceShirtDrop with dissolve
ce "Yeah, right..."
scene ep6_hike36 with dissolve
ce "Skinny dipping!"
scene ep6_hike35 with dissolve
ce "..."
scene ep6_hike24 with dissolve
li "..."
scene ep6_hike25 with dissolve
li "Wait for me!"
scene ep6_hike26 with dissolve
me "Maybe I should join them."
menu:
    "[M_06_012a]": # "Yeah, join them.":
        if ep4NightChoose == 7:
            scene ep6_hike27 with dissolve
            me "Yeah, because Steph would be absolutely thrilled if I went skinny dipping with them."
            scene ep6_hike28 with dissolve
            me "I'll just sit here and watch."
        elif ep4NightChoose == 2:
            scene ep6_hike27 with dissolve
            me "Yeah, because Lexi would be absolutely thrilled if I went skinny dipping with them."
            scene ep6_hike28 with dissolve
            me "I'll just sit here and watch."
        else:
            scene ep6_hike27 with dissolve
            me "You know what... I'll take a managerial decision here."
            me "Let's just have the girls have some fun without having any dicks around for once."
            me "I think it'll be good for them."
            scene ep6_hike28 with dissolve
            me "I'll just sit here and watch. If they want me, they'll call for me."
    "[M_06_012b]": # "Sit and watch.":
        scene ep6_hike28 with dissolve
        me "I'll just sit here and watch. If they want me, they'll call for me."
scene ep6_hike29 with dissolve
me "After all, I've got the best view in the world right here."
if ep4NightChoose == 7:
    me "Sorry, Steph."
elif ep4NightChoose == 2:
    me "Sorry, Lexi."
scene ep6_hike37 with dissolve
ce "Come get some, Linda."
li "I'm on my way."
li "In a slow and safe manner."
li "This is sooo cold."
ce "Yeah, you come right here and I'll dip you under."
$ renpy.movie_cutscene("imov/ep6/ep6_hike01both.webm", delay=None, loops=0, stop_music=False)
ce "Only tiny little scared bitches complain about some water being too cold."
li "Is that so?"
li "Well, get ready slut."
li "Because here comes Linda, DIVINE GODDESS OF THE THUNDERING QUAKES!"
scene ep6_hike38 with dissolve
ce "OH{w=1} MY{w=1} GO{w=1}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{nw}"
scene ep6_hike39 with dissolve
ce "O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{nw}"
scene ep6_hike40 with dissolve
ce "O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{w=0.01}O{nw}"
scene ep6_hike41 with dissolve
$ renpy.pause(1)
scene ep6_hike42 with fade
ce ".{w=0.1}.{w=0.1}.{w=0.4}D{w=0.1}."
scene ep6_hike43 with dissolve
ce "..."
scene ep6_hike44 with dissolve
ce "That was the most terrifying experience I've had in my whole life."
scene ep6_hike45 with dissolve
ce "Let's do it again!"
scene ep6_hike46 with dissolve
li "There's some advantages about being chiseled the way I am."
scene ep6_hike47 with dissolve
li "And you were saying something about dipping me under?"
ce "Yeah, fuck that. I'm out of here."
scene ep6_lindacecedip with dissolve
$ renpy.pause()
scene ep6_hike48 with dissolve
li "Look at him, enjoying the view."
scene ep6_hike49 with dissolve
me "..."
scene ep6_hike50 with dissolve
ce "Don't you be looking at Linda's tiddies."
scene ep6_hike51 with dissolve
$ renpy.pause(0.5)
scene ep6_hike53 with dissolve
li "Speak for yourself..."
scene ep6_hike54 with dissolve
li "You keep your eyes on those great tiddies."
scene ep6_hike65 with fade
$ renpy.pause(1)
scene ep6_hike62 with dissolve
$ renpy.pause(0.5)
scene ep6_hike63 with dissolve
$ renpy.pause(0.5)
scene ep6_hike62 with dissolve
$ renpy.pause(1.5)
scene ep6_hike64 with dissolve
$ renpy.pause(1.5)
scene ep6_hike55 with dissolve
$ renpy.pause(1)
scene ep6_hike56 with dissolve
li "What the..."
scene ep6_hike57 with dissolve
ce "Yesss!"
scene ep6_hike58 with dissolve
ce "Tiddies overboard!"
scene ep6_hike59 with dissolve
ce "What do you say, [name]. Victory?"
scene ep6_hike66 with dissolve
me "First one to give the good old Bamboobzled wins."
scene ep6_hike60 with dissolve
ce "Huh?"
scene ep6_hike61 with dissolve
ce "What the heck is Bamboobzled?"
scene ep6_Bamboobzled with dissolve
me "..."
stop music fadeout 3
ce "IMMA BITE THOSE NIPPLES RIGHT OFF!"
scene bg empty with fade
$ clockis = [[todayIs],1,7,0,1]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_hikesit
$ nowPlayingArtist = "The Lighthearts"
$ nowPlayingTitle = "Without You"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_hike69 with fade
ce "You don't like to skinny dip?"
me "Sure I do, but I thought you two could get some alone time out there."
scene ep6_hike71 with dissolve
ce "He's jealous."
li "Can you sit still please? I'm trying to fix your hair here."
if ep4NightChoose == 6:
    scene ep6_hike72 with dissolve
    li "Keep your head down, and don't move."
    li "So I can look at the handsome guy over there."
    li "And tell him how cute he is."
    scene ep6_hike75 with dissolve
    ce "One thing I don't get though."
    scene ep6_hike75 with dissolve
    ce "Why don't you say the words?"
    li "Huh?"
    scene ep6_hike79 with dissolve
    ce "You've been going on and on about him since I met you."
    me "Cece..."
    scene ep6_hike81 with dissolve
    ce "No, she needs to hear this."
    scene ep6_hike80 with dissolve
    ce "You always said you loved him and you were basically a couple since the day you met."
    ce "But you never said those words, did you. Not then, not now."
    scene ep6_hike79 with dissolve
    li "I never even thought..."
    ce "Come on, Linda. It's three words... I... Love... You..."
    ce "Even now, after all this time you're having problems saying the words."
    scene ep6_hike80 with dissolve
    ce "Crap, that sounded worse than I wanted. I'm sorry."
    li "Don't be. You're right."
    me "*cough* ..."
elif ep4NightChoose == 1:
    scene ep6_hike69 with dissolve
    li "Keep your head forward, and don't move."
    li "Look at the handsome guy over there."
    scene ep6_hike70 with dissolve
    ce "That's awkward, you know."
    scene ep6_hike71 with dissolve
    li "Then look at me."
    ce "But you said..."
    scene ep6_hike76 with dissolve
    li "Let down that guard of yours."
    li "You know that enormous wall you're hiding behind?"
    li "I know what you feel about him."
    scene ep6_hike77 with dissolve
    li "You don't have to hide it from anyone."
    li "Least of all yourself."
    scene ep6_hike78 with dissolve
    li "Not all feelings are bad. Let them out."
    me "*cough* ..."
else:
    scene ep6_hike72 with dissolve
    li "Keep your head down, and don't move."
    li "So I can look at dorky over there."
    scene ep6_hike73 with dissolve
    ce "Linda... I have to tell you something."
    scene ep6_hike74 with dissolve
    ce "I hate myself for it, but I have to."
    scene ep6_hike75 with dissolve
    ce "You have to let go."
    scene ep6_hike79 with dissolve
    li "Huh?"
    scene ep6_hike80 with dissolve
    ce "You are going to ruin your life if you don't let yourself fall for anyone else, just because of him."
    me "Cece..."
    scene ep6_hike81 with dissolve
    ce "No, she needs to hear this."
    if ep4SetupChrisWithLi:
        scene ep6_hike80 with dissolve
        ce "You've got this great guy in Chris, and still you look like you're waiting for [name] to be single again."
        ce "It doesn't work like that."
    else:
        scene ep6_hike80 with dissolve
        ce "You have to go your own way. Find your own guy."
        ce "Your long lost high school love is a wonderful memory, but you need to move on."
    scene ep6_hike79 with dissolve
    ce "I'm sorry."
    li "Don't be."
    li "...and you're right."
    me "*cough* ..."
scene ep6_hike82 with dissolve
$ clockis = [[todayIs],1,7,2,4]
me "Let's just drop it..."
scene ep6_hike83 with dissolve
me "And just enjoy the scenery."
scene ep6_hike84 with dissolve
li "You were right, Cece."
scene ep6_hike85 with dissolve
li "It was a pain getting here..."
scene ep6_hike86 with dissolve
li "...but it was all worth it."
ce "I know."
li "Hair done... And now I really need to pee."
me "There's toilet everywhere."
scene ep6_hike87 with dissolve
ce "Off she goes."
scene ep6_hike88 with dissolve
me "You know you don't have to run all the way home?"
li "Fuck you!"
li "I just need somewhere with a... bush or... some moss... or something!"
scene ep6_hike89 with dissolve
me "Girl problems."
scene ep6_hike90 with dissolve
me "..."
ce "What's wrong?"
me "..."
ce "Don't freak me out now."
me "No, it's just you... you're..."
scene ep6_hike92 with dissolve
if ep4NightChoose == 1:
    me "...stunningly beautiful."
else:
    me "...glowing."
me "It's like you're a completely different woman than what you were back there... at the bridge."
scene ep6_hike94 with dissolve
ce "..."
if ep4NightChoose == 1:
    me "I love you. Don't ever leave me, Cece."
else:
    me "Please don't ever do that again, Cece."
me "No matter how dark things get, know that I'll always be there."
me "There's light at the end of the tunnel. Things will get better soon."
scene ep6_hike93 with dissolve
ce "And that's what you have to keep saying when things go bad for yourself too."
ce "When you stand in front of the mirror in the morning, and you don't feel like going outside."
ce "'There's light at the end of the tunnel. Things will get better soon.'"
scene ep6_hike92 with dissolve
me "I'm fine, you know. You helped me get there. So let me help you get there too."
scene ep6_hike95 with dissolve
li "So you guys ready to head back now?"
ce "Yup. It's about that time."
scene bg empty with fade
$ clockis = [[todayIs],2,0,3,3]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_streetwalk01 with fade
me "Your feet ok?"
li "I'm not complaining."
me "Yeah, I know that."
me "If somebody killed your cat, you would have said something like..."
scene ep6_streetwalk02 with dissolve
li "...It would have died in 7 years anyway."
me "Exactly."
li "..."
if ep4NightChoose == 6:
    scene ep6_streetwalk03 with dissolve
    me "What Cece said back there..."
    li "I'll work on it."
    me "Work on what?"
    li "Being better at letting you know my feelings."
    me "No, I didn't mean that."
    li "..."
    me "You talked about me often?"
    scene ep6_streetwalk04 with dissolve
    li "Well, yeah... I think she was sick and tired of hearing about you in the end."
    me "I know I took the blame for not reaching out to you, and I stand by that, but..."
    me "...why didn't you call me?"
    li "Would it have mattered?"
    scene ep6_streetwalk05 with dissolve
    me "I don't know."
    li "See?"
    me "'I don't know' doesn't answer if you did the right thing."
    li "I'd say we got the happy ending anyway."
    me "Yeah... You're right, we did."
elif ep4NightChoose == 1:
    scene ep6_streetwalk03 with dissolve
    me "What you said back there..."
    li "She loves you. She really does."
    li "It's not hard to see you love her back."
    me "..."
    li "For years I've been hoping for you to love me."
    li "Even when you were with Steph."
    scene ep6_streetwalk04 with dissolve
    li "Cece made me realize that I have to stop that."
    li "I could never do that to her, just the thought of it makes me sick."
    if ep4SetupChrisWithLi:
        li "And you both made me see how amazing Chris is."
        me "He cares a whole lot for you."
        li "I know. I'm going to head over to him now."
        scene ep6_streetwalk05 with dissolve
        li "I need to tell him."
        me "Tell him what."
        li "That I realized, I love him."
    else:
        li "I'm going to call Steph and have a chat with her. I think she still has that old place of hers."
        if Impact_Steph:
            li "Maybe I can live with her for a while."
        else:
            li "Maybe I can live there for a while."
        li "Figure out what I want in life."
        li "Reset myself for a bit."
        scene ep6_streetwalk05 with dissolve
        me "You can stay with me for as long as you like."
        li "No offense, but I can't do that living in your apartment."
    li "I have to move on."
    me "..."
    me "We're still friends?"
    li "Until I kick the bucket."
else:
    scene ep6_streetwalk03 with dissolve
    me "What Cece said back there..."
    li "She was right."
    li "I've loved you for so long I don't even remember how it's like not to."
    me "I'm sorry."
    scene ep6_streetwalk04 with dissolve
    li "For not returning the feelings? Don't be. Love doesn't work like that."
    li "She just made me see that."
    if ep4SetupChrisWithLi:
        li "And I think she made me see how amazing Chris is."
        me "He cares a whole lot for you."
        scene ep6_streetwalk05 with dissolve
        li "I know. I'm going to head over to him now."
        li "I need to tell him."
        me "Tell him what."
        li "That I realized, I love him."
    else:
        li "I'm going to call Steph and have a chat with her. I think she still has that old place of hers."
        if Impact_Steph:
            li "Maybe I can live with her for a while."
        else:
            li "Maybe I can live there for a while."
        li "Figure out what I want in life."
        li "Reset myself for a bit."
        scene ep6_streetwalk05 with dissolve
        me "You can stay with me for as long as you like."
        li "No offense, but I can't do that living in your apartment."
        if ep4NightChoose <> 1:
            me "And Cece?"
            li "You'll have to ask her what she wants."
    li "I have to move on."
    me "We're still friends?"
    li "Until I kick the bucket."
scene ep6_streetwalk06 with dissolve
me "She still sleeping?"
li "Like a baby."
scene ep6_streetwalk07 with dissolve
me "We're here, Cece."
ce "...just five more minutes."
me "Not home... Here!"
scene ep6_streetwalk08 with dissolve
ce "Oh my god. I'm awake, I'm awake."
scene ep6_streetwalk09 with dissolve
li "What do you mean here. We're not home yet."
scene ep6_streetwalk10 with dissolve
ce "No, here... As in..."
scene ep6_streetwalk11 with dissolve
stop music fadeout 8
me "Our old school."
ce "Now you can show me all the places you've been telling me stories about."
li "Oh boy..."
scene ep6_streetwalk12 with dissolve
ce "Go on..."
li "This is going to be weird."
me "I haven't been here in ages."
scene ep6_streetwalk13 with dissolve
ce "Hold up [name]. Come here for a second."
scene ep6_streetwalk14 with dissolve
ce "Here..."
scene ep6_streetwalk15 with dissolve
me "How..."
ce "Now go."
ce "And head down to the gym afterwards, ok."
me "Ehm... Ok?"
scene bg empty with fade
$ clockis = [[todayIs],2,0,5,8]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_lindabench
$ nowPlayingArtist = "Evening Traveler"
$ nowPlayingTitle = "Trade a Moment"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_hall01 with fade
me "I can't believe we're back here."
li "..."
scene ep6_hall02 with dissolve
me "I mean, I walk past here every so often, but I never thought of going in here."
scene ep6_hall03 with dissolve
me "There's so many good memories from these halls."
scene ep6_hall04 with dissolve
me "Things are almost exactly the same as they used to be."
scene ep6_hall05 with dissolve
li "The bench."
scene ep6_hall06 with dissolve
me "Wow, even that is still here."
scene ep6_hall07 with dissolve
me "A bit more worn, but still here."
scene ep6_hall08 with dissolve
me "Want to head over to the classrooms and see if the fire extinguisher is still there?"
scene ep6_hall09 with dissolve
me "Linda?"
scene ep6_hall10 with dissolve
li "Can we just get out of here?"
scene ep6_hall11 with dissolve
me "What's going on. Talk to me."
scene ep6_hall12 with dissolve
li "I don't have any good memories from school, ok?"
li "In fact, I hated it."
me "But you always talk about..."
li "I talk about {b}you{/b}, not school."
me "I thought you'd like coming back here. Even our bench is still here..."
li "'Our' bench?"
li "It used to be our bench. Mine, the guy I loved, and his best friend."
li "Then along came a girl that became my best friend."
li "And before you know it, I had to walk past 'our' bench..."
scene ep6_hall13 with dissolve
li "...where the love of my life and my best friend were making out..."
li "...every single day."
me "I don't know what to say."
me "But I'm not going to say sorry."
scene ep6_hall14 with dissolve
li "..."
me "I mean I'm sorry I brought you here today. I didn't know you had such feelings towards the place."
me "But I'm not sorry for what happened at school."
scene ep6_hall15 with dissolve
me "When I met you, I really liked you. I had such a crush on you."
me "Not to mention all those other things we did."
scene ep6_hall16 with dissolve
me "But we decided to move on. Both of us. We agreed on it."
me "I had no idea you still felt something, because you never said, or showed anything."
scene ep6_hall17 with dissolve
me "I honestly thought you were ok with it."
scene ep6_hall18 with dissolve
me "Later on, when Steph arrived, I still had no idea you felt like you did."
me "I was just a teenage kid without a girlfriend that fell in love with someone."
scene ep6_hall19 with dissolve
me "And that someone fell in love with me."
scene ep6_hall20 with dissolve
me "I can't apologize for that."
scene ep6_hall21 with dissolve
$ clockis = [[todayIs],2,1,1,2]
me "So when I look around this place now, I get a lot of feelings."
scene ep6_hall22 with dissolve
me "I remember Matt giving me a wedgie, but I also remember me giving him a wedgie."
scene ep6_hall23 with dissolve
me "Then there's the time you emptied the fire extinguisher."
scene ep6_hall24 with dissolve
me "And the time we had our first beer, hidden under the stairs."
scene ep6_hall25 with dissolve
me "I remember that wonderful girl with the long curly hair when she walked into the classroom for the first time."
me "And I remember her leaving me on prom night."
scene ep6_hall28 with dissolve
if ep4SetupChrisWithLi:
    scene ep6_lindaoldschool1
    me "Then there's the goofy guy who somehow ended up becoming my best friend."
else:
    scene ep6_lindaoldschool2
    me "Then there's that girl who stood over there by the pillar, that I had such a big crush on."
scene ep6_hall32 with dissolve
li "..."
scene ep6_hall31 with dissolve
scene ep6_lindaoldschool3
me "And loosing one of my best friends, because she had to move away."
scene ep6_hall29 with dissolve
li "..."
me "All of those experiences is a part of what made me who I am today."
me "Good and bad."
me "And I'm happy I experienced them. Without them I'd be a poorer guy."
scene ep6_hall33 with dissolve
if ep4NightChoose == 7:
    me "But I can't apologize for loving Steph."
    me "Even after two years apart, I still do."
else:
    me "But I can't apologize for loving Steph back then."
if ep4NightChoose == 6:
    me "And if that ruins this thing we've started now, then it's my loss."
scene ep6_hall34 with hpunch
me "..."
if ep4NightChoose == 6:
    scene ep6_hall35 with dissolve
    li "I love you!"
    me "I love you too!"
else:
    scene ep6_hall35 with dissolve
    li "..."
scene ep6_hall37 with fade
$ clockis = [[todayIs],2,1,2,0]
li "So, we're doing this tour of our school with Cece?"
me "Huh? I thought you wanted to leave?"
scene ep6_hall36 with dissolve
li "Let's just say I had a change of heart."
scene ep6_hall38 with dissolve
li "I can't wait to show her the classroom..."
li "Maybe try out the fire extinguisher?"
me "So you don't need that ring any more?"
scene ep6_hall36 with dissolve
li "Fuck the ring. I want to check out the place."
scene ep6_hall39 with dissolve
me "So I should just throw it in the bin then?"
li "..."
scene ep6_hall40 with dissolve
li "You... you... you... you..."
scene ep6_hall41 with dissolve
me "Your... precious?"
scene ep6_hall42 with dissolve
$ renpy.pause(0.6)
scene ep6_hall41 with dissolve
$ renpy.pause(0.2)
scene ep6_hall42 with dissolve
$ renpy.pause(2)
scene ep6_hall43 with hpunch
$ renpy.pause(0.5)
scene ep6_hall44 with dissolve
$ renpy.pause(0.5)
scene ep6_hall45 with dissolve
li "Thank you."
scene ep6_hall46 with dissolve
me "I guess it does mean a lot to you after all."
li "I think I was so accustomed to having lost it, I didn't realize how much I wanted it back."
me "Do me a little favor though."
li "Favor?"
if ep4NightChoose == 6:
    me "Don't put it back where you used to have it, please. Now that Matt has had it for such a long time."
    me "Let me buy you a new one."
    scene ep6_hall48 with dissolve
    li "Don't worry. I don't need to carry it around anymore."
    li "I'll find a nice box to put it in instead. Then we can add more mementos as time passes."
    scene ep6_hall49
    $ renpy.movie_cutscene("imov/ep6/ep6_hall01bench.webm", delay=None, loops=0, stop_music=False)
    li "*pants*"
    scene ep6_hall50 with dissolve
    me "Linda?"
    scene ep6_hall52 with dissolve
    li "Yeah?"
    scene ep6_hall50 with dissolve
    me "You're really horny now, aren't you."
    scene ep6_hall49 with dissolve
    li "You... have no idea..."
    scene ep6_hall50 with dissolve
    li "If it hadn't been for the fact that Cece is right around the corner then I would have..."
    scene ep6_hall51 with dissolve
    me "Cece! Oh fuck, I forgot all about it?"
    scene ep6_hall53 with dissolve
    li "Huh? Forgot about what?"
    scene ep6_hall54 with dissolve
    stop music fadeout 10
    me "Never mind. But we have to get down to the gym."
    li "The gym? But I always hated..."
    scene ep6_hall56 with dissolve
    li "Oh..."
    li "OH!"
    li "Yes baby, I'm coming!"
    scene ep6_hall57 with dissolve
    me "Well, I had this idea."
    li "I like it already."
    scene ep6_hall59 with dissolve
    me "There's nobody down at the gym right now."
    li "I always fantasized about this."
    scene ep6_hall61 with dissolve
    me "And you know, since neither of us had a real prom..."
    li "Yes, please!"
    scene ep6_hall63 with dissolve
    me "Hang on, let me check."
    li "Hurry!"
    me "Ok, should be good."
    me "Now close your eyes."
    scene ep6_hall64 with dissolve
    li "You're killing me here!"
    me "Shhh. Close your eyes."
    li "Yes master."
    stop music fadeout 5
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    me "Now open your eyes."
    scene ep6_prom03 with fade
    li "I'm so horny, I want to..."
    me "OPEN!"
    li "No need to shout, I can't open my legs when I'm standing."
else:
    me "If you're going to... like... you know... put it back where you used to have it..."
    me "...at least give it a real cleanup... like acid type cleanup."
    scene ep6_hall45 with dissolve
    li "I'm not going to put it back anywhere. I don't need that anymore."
    li "It's a nice memento of that time you gave it to me."
    scene ep6_hall47 with dissolve
    li "..."
    scene ep6_hall46 with dissolve
    if ep4SetupChrisWithLi:
        li "But me and Chris will have to make our own from here on."
    else:
        li "But I will have to make my own with someone else from now on."
    scene ep6_hall49 with dissolve
    li "What's taking Cece so long."
    scene ep6_hall50 with dissolve
    me "She should be right around the..."
    scene ep6_hall51 with dissolve
    me "Cece! Oh fuck, I forgot all about it?"
    scene ep6_hall53 with dissolve
    li "Huh? Forgot about what?"
    scene ep6_hall54 with dissolve
    stop music fadeout 10
    me "Never mind. But we have to get down to the gym."
    li "The gym? But I always hated the gym."
    scene ep6_hall55 with dissolve
    me "Come on. You'll enjoy it."
    li "Doubt it. In fact, every gym class I used the same excuse that I had my period."
    li "My teacher probably thought I was bleeding to death by the end of the year."
    scene ep6_hall58 with dissolve
    me "We're not going to have gym class."
    li "Thank god for that."
    scene ep6_hall60 with dissolve
    me "There's nobody down at the gym right now."
    li "And?"
    scene ep6_hall62 with dissolve
    me "Well, you know, since neither of us had a real prom..."
    li "Can you be a little more cryptic?"
    scene ep6_hall63 with dissolve
    me "Hang on, let me check first."
    li "What's going on."
    me "Ok, should be good."
    me "Now close your eyes."
    li "Seriously?"
    me "Yes, close your eyes."
    stop music fadeout 5
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    me "Now open your eyes."
    scene ep6_prom03 with fade
    li "I can't see jack shit."
    me "I SAID, OPEN YOUR EYES."
    li "They are open."
"*whispers* {i}hit the switch{/i}"
if Impact_Steph:
    scene ep6_prom02 with dissolve
else:
    scene ep6_prom02 with dissolve
"*whispers* {i}both of them{/i}"
scene ep6_prom03 with dissolve
"*whispers* {i}for crying out loud, will you hit the sw...{/i}"
play music ep6_prom
$ nowPlayingArtist = "Michael Shynes"
$ nowPlayingTitle = "Homecoming"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
if Impact_Steph:
    scene ep6_prom01 with dissolve
else:
    scene ep6_prom01b with dissolve
$ clockis = [[todayIs],2,2,3,1]
"SURPRISE!"
scene ep6_prom04 with dissolve
li "Holy shit."
li "What... why... when..."
ch "Matt, you had one job."
ma "I lost track of the switch and couldn't find it again in the dark. And now the switch won't stay on."
if Impact_Steph:
    scene ep6_prom05 with dissolve
    st "Linda, darling!"
    li "Steph. But... I had no idea..."
else:
    scene ep6_prom05b with dissolve
    ki "Come here, let me squeeze one out of you."
    li "Kira. But... I had no idea..."
    me "Holy shit. I didn't even know."
if Impact_Steph:
    scene ep6_prom06 with dissolve
    st "That's the whole point of a surprise isn't it."
    me "Holy shit. I didn't even know."
else:
    scene ep6_prom06b with dissolve
    li "I had no idea..."
    ki "Don't look at me, I had no idea either."
    ki "I was told to come here today, and I was sure glad I did."
if Impact_Steph:
    scene ep6_prom07 with dissolve
    li "When did you get back?"
    st "Literally 2 minutes ago. I had to dive into my dress head first."
    st "Please tell me if it's on backwards."
else:
    scene ep6_prom07b with dissolve
    li "Where's your makeup."
    ki "All gone, baby."
if Impact_Steph:
    scene ep6_prom08 with dissolve
    li "But Lexi's here..."
    li "...and MATT?"
    st "Will you calm down before you pass out."
    ma "You called?"
else:
    scene ep6_prom08b with dissolve
    li "But Lexi's here..."
    ki "We're all here."
if Impact_Steph:
    if ep4NightChoose == 2:
        scene ep6_prom19b with dissolve
        me "(Better go say hello.)"
        scene ep6_prom20b with dissolve
        me "..."
    else:
        if ep4NightChoose == 3 or ep4NightChoose == 4:
            scene ep6_prom18 with dissolve
            ki "Hey sweetie."
        else:
            scene ep6_prom19 with dissolve
            ki "Hey [name]."
        scene ep6_prom19 with dissolve
        me "Kira."
        ki "Got to go squeeze a hug out of Linda, but talk to you later on."
        scene ep6_prom20 with dissolve
        ki "And thank you for yesterday."
else:
    scene ep6_prom19b with dissolve
    me "(Better go say hello.)"
    scene ep6_prom20b with dissolve
    me "..."
scene ep6_prom21 with dissolve
me "Holly. I can't believe you're here."
scene ep6_prom22 with dissolve
ho "Me neither. That flight..."
me "And Cece, sorry we took a bit of time."
scene ep6_prom23 with dissolve
ce "Did you give it?"
me "Yeah, I did. She freaked out."
scene ep6_prom25 with dissolve
ce "I knew she would. I should have hidden somewhere and Nuked it."
if ep4NightChoose == 6:
    me "Probably was for the best you didn't."
scene ep6_prom28 with dissolve
ce "Linda is really surprised."
me "Yeah I think she almost had a heart attack."
me "Same as me to be honest."
scene ep6_prom23 with dissolve
me "But what the hell, Cece. I thought this was just me, Chris, Linda, Kira and Robin."
scene ep6_prom24 with dissolve
ho "Yeah, thank you for that."
ce "The more, the merrier. Right?"
me "You know what I mean, Holly."
scene ep6_prom25 with dissolve
ce "Holly is telling me everything about that yacht trip of yours."
if ep4NightChoose == 2:
    if ep5HollyComplete == 1 or ep5HollyComplete == 2:
        scene ep6_prom26 with dissolve
        ho "Well, not everything..."
        menu:
            "[M_06_013a]": # "Tell her no regrets about what happened. (I)":
                $ ep6ToldHollyNoRegrets = True
                scene ep6_prom29 with dissolve
                me "It was a very nice trip, Holly."
                me "No regrets..."
                ho "..."
            "[M_06_013b]": # "Don't tell her.":
                scene ep6_prom25 with dissolve
else:
    ho "We were flashing boobs."
scene ep6_prom25 with dissolve
ho "He was fishing."
if ep4NightChoose == 7:
    scene ep6_prom28 with dissolve
    ce "[name]. Your girl is coming."
    scene ep6_prom30 with dissolve
    if not ep6MorningListSt:
        me "So good to see you home in one piece."
        me "You must be dead tired after all that driving."
    else:
        me "Finally, you're back."
    scene ep6_prom31 with dissolve
    st "It's so good to be home again. For real this time."
    st "God, I love you!"
    scene ep6_prom32 with dissolve
    ce "So this is love..."
    ho "Yup. Hard earned love."
    scene ep6_prom33 with dissolve
    ce "..."
    scene ep6_prom34 with dissolve
    ho "..."
    scene ep6_prom35 with dissolve
    ho "Come on, Cece. Let the lovebirds have their fun."
    ce "How's it possible. That thing is so firm, it's unbelievable."
    ho "Many, many, many hours in the gym, Cece."
    scene ep6_prom36 with dissolve
    me "Hey Steph... it's... you can loosen the grip slightly now."
    st "Maybe I don't want to."
    me "...so I can breathe properly."
    scene ep6_prom37 with dissolve
    st "..."
    me "You ok?"
    scene ep6_prom38 with dissolve
    st "I am now."
else:
    if ep4NightChoose == 2:
        scene ep6_prom27 with dissolve
        if ep6ToldHollyNoRegrets:
            ce "But your girl is over there, [name]. Don't stand here with us. Go see her."
        else:
            ce "But Lexi is over there, [name]. Don't stand here with us. Go see her."
        me "Good idea."
        if Impact_Steph:
            scene ep6_prom09 with dissolve
        else:
            scene ep6_prom09b with dissolve
        me "Lexi! I'm so glad you could make it."
        le "Hey [name]."
        le "I wouldn't miss it for the world."
        me "I know how busy you are, so it means a lot to me. To all of us."
        le "Yes, unfortunately I don't have all that many hours before I have to hightail."
        scene ep6_prom10 with dissolve
        le "I missed you."
        if ep6MorningListLe:
            me "And I missed you. I tried calling you..."
            scene ep6_prom11 with dissolve
            le "I saw it last night, and I was going to call you back, but I thought you were sleeping."
            me "It's fine. I probably were."
        else:
            me "And I missed you. I was going to call you..."
            scene ep6_prom11 with dissolve
            le "Mhmm. Me too. But then I rememberd it was the middle of the night. You were probably sleeping."
            me "It's fine. I probably were."
        le "See? We've been away from each other for a couple of days, and already I keep..."
        scene ep6_prom13 with dissolve
        me "Hey..."
        scene ep6_prom12 with dissolve
        me "Like I said on the plane..."
        me "It's not a problem for me at all, so don't make it into one."
        le "Maybe... you would like to come with me when I leave later on?"
        me "I would love to, but I have a few things I need to take care of here at home before I can go away again."
        le "Yeah, I understand that."
        me "But I'll be coming soon, that's a promise."
        scene ep6_prom14 with dissolve
        ho "Hey, lovebirds."
        scene ep6_prom16 with dissolve
        me "I still can't believe you're here, Holly. I know you don't like flying."
        ho "Lexi took one for the team on the yacht, I figured I had to return the favor."
        scene ep6_prom15 with dissolve
        le "She filled a whole bag, and I had to stroke her hair while..."
        ho "Whatever... But you're not going to believe this."
        ho "Lexi went asking Jan if there was an opening for her to be a part of this."
        ho "And he cancelled her morning appearance on Howard Stern, so she could go. Like literally cancelled it!"
        me "So... he's pissed at me for ruining her schedule, eh?"
        ho "That's just it, he's not. He's like a kitten."
        scene ep6_prom16 with dissolve
        me "Sorry for cutting it short, but I have to make the rounds."
        me "We'll catch up later on, Holly."
        scene ep6_prom15 with dissolve
        me "You too, Babe."
        scene ep6_prom17 with dissolve
        ho "Lexi, what the hell are you doing? That's your boyfriend right there."
        le "I know... I... This is just so strange. I don't know what to do at a prom."
        ho "Well, you never went to your own prom. Just do what you normally do. You thrive in this sort of stuff. Be yourself."
        le "Lexi or Alexandra?"
        ho "I don't know. Pick one."
        ho "Right now you're the Anastasia, the apathetic ice queen."
        an "..."
        an "You're right."
        ho "And he called you Babe. That's so sweet."
    else:
        scene ep6_prom27 with dissolve
        ce "Lexi's here too, [name]. You should go say hi."
        me "Good idea."
        if Impact_Steph:
            scene ep6_prom09 with dissolve
        else:
            scene ep6_prom09b with dissolve
        me "Lexi! I'm so glad you could make it."
        le "Hey [name]."
        le "I wouldn't miss it for the world."
        me "I know how busy you are, so it means a lot to me. To all of us."
        le "Yes, unfortunately I don't have all that many hours before I have to hightail."
        scene ep6_prom10 with dissolve
        if ep6MorningListLe:
            me "I tried calling you..."
            scene ep6_prom11 with dissolve
            le "I saw it last night, and I was going to call you back, but I thought you were sleeping."
            me "It's fine. I probably were. And you're a busy woman, I know that."
        else:
            me "So how are you doing otherwise?"
            le "Just fine. Back to working again. It's not too bad when you get into it."
        scene ep6_prom14 with dissolve
        ho "So where's the alcohol in this place?"
        scene ep6_prom16 with dissolve
        me "I still can't believe you're here, Holly. I know you don't like flying."
        ho "Lexi took one for the team on the yacht, I figured I had to return the favor."
        scene ep6_prom15 with dissolve
        le "She filled a whole bag, and I had to stroke her hair while..."
        ho "Whatever... But you're not going to believe this."
        ho "Lexi asked Jan if there was an opening for her to be a part of this."
        ho "And he cancelled her morning appearance on Howard Stern, so she could go. Like literally cancelled it!"
        me "So... he's pissed at me for ruining her schedule, eh?"
        ho "That's just it, he's not. He's like a kitten."
        scene ep6_prom16 with dissolve
        me "Sorry for cutting it short, but I have to make the rounds."
        me "We'll catch up later on, Holly."
        scene ep6_prom15 with dissolve
        me "And you, Lexi."
        scene ep6_prom17 with dissolve
        ho "Lexi, what's going on. You're not yourself."
        le "I know... I... This is just so strange. I don't know what to do at a prom."
        ho "Well, you never went to your own prom. Just do what you normally do. You thrive in this sort of stuff. Be yourself."
        le "Lexi or Alexandra?"
        ho "I don't know. Pick one."
        ho "Right now you're the Anastasia, the apathetic ice queen."
        an "..."
        an "You're right."
if ep4NightChoose == 7:
    scene ep6_prom40 with fade
else:
    scene ep6_prom39 with fade
$ clockis = [[todayIs],2,2,4,7]
ch "If I can just have everyone's attention for a bit, please."
ch "I just wanted to inform you that the table's set and food is served."
ch "So if you want warm food, we should go eat first, then talk after."
ma "Sounds good to me... I'm starving."
scene ep6_prom42 with fade
me "Enjoying the surprise?"
li "You are insane."
scene ep6_prom43 with dissolve
me "It wasn't me, really. Chris here was the brains of the operation together with Cece."
scene ep6_prom44 with dissolve
ch "You're joking, right? Do I look like a man with a plan to you?"
ch "Cece did all the organizing, calling everyone. The food is sponsored by Kira's boss, as a return favor for you helping out."
scene ep6_prom45 with dissolve
ch "Lexi's manager pulled a few strings to get a hold of the stage, and a stage crew came and built it in no time."
ch "I just poured the beer."
scene ep6_prom43 with dissolve
me "Wow... But just one question..."
if Impact_Steph:
    scene ep6_prom49 with dissolve
    me "Why the empty chair?"
    scene ep6_prom46 with dissolve
    ch "Oh, that's for our guest of honor..."
else:
    scene ep6_prom48 with dissolve
    me "Why the empty chairs?"
    scene ep6_prom46 with dissolve
    ch "Oh..."
    scene ep6_prom48 with dissolve
    ch "I just counted on my fingers how many we were, and by instinct, I counted Steph. Sorry about that."
    me "And the other chair?"
    ch "Our guest of honor."
me "Guest of honor?"
scene ep6_prom47 with dissolve
uk "Did someone say guest of honor?"
scene ep6_prom50 with dissolve
ch "Hey, Maria."
uk "So good to see so many familiar faces."
if Impact_Steph:
    scene ep6_prom52 with dissolve
    uk "And unfamiliar ones."
    st "Hey Maria."
    uk "Steph, my favorite student."
    scene ep6_prom53 with dissolve
    va "For those that do not know me, I am Maria Vasquez."
    scene ep6_prom54 with dissolve
    va "I had the great honor of watching these people grow into the beautiful people they are today."
    va "And hopefully teaching them some important lessons in life..."
    scene ep6_prom55 with dissolve
    va "Like manners."
    scene ep6_prom56 with dissolve
    ma "..."
else:
    scene ep6_prom51 with dissolve
    uk "And unfamiliar ones."
    scene ep6_prom53b with dissolve
    va "For those that do not know me, I am Maria Vasquez."
    scene ep6_prom54 with dissolve
    va "I had the great honor of watching these people grow into the beautiful people they are today."
    scene ep6_prom55b with dissolve
    va "Like manners."
    scene ep6_prom56b with dissolve
    ma "..."
scene ep6_prom73 with dissolve
va "So, Chris. Now that I'm here..."
scene ep6_prom57 with dissolve
ch "It's time to eat. Let the prom we all need begin!"
scene ep6_prom79 with dissolve
me "(And just like that, Chris... you hit the nail right on the head again, without even knowing it.)"
me "(Because when I think about it, none of us had a real prom.)"
scene ep6_prom77 with dissolve
me "(Every single one of us missed it, because we all had some kind of reason for not going...)"
scene ep6_prom71 with dissolve
me "(...)"
scene ep6_prom70 with dissolve
me "(Some were too busy feeding their own hate...)"
scene ep6_prom72 with dissolve
me "(...or in too much of a hurry to reach adulthood.)"
if Impact_Steph:
    scene ep6_prom58 with dissolve
    $ renpy.pause(1.5)
    scene ep6_prom59 with dissolve
    me "(Some were running away to protect their love...)"
    scene ep6_prom60 with dissolve
    me "(...or too busy partying somewhere.)"
else:
    scene ep6_prom58b with dissolve
    $ renpy.pause(1.5)
    scene ep6_prom60c with dissolve
    me "(Some were running away...)"
    scene ep6_prom60b with dissolve
    me "(...or too busy partying somewhere.)"
scene ep6_prom61 with dissolve
$ renpy.pause(1.5)
scene ep6_prom62 with dissolve
me "(Some were too busy fighting their inner demons to even think about prom...)"
scene ep6_prom63 with dissolve
me "(...or so caught up in work, they never even considered going.)"
scene ep6_prom64 with dissolve
$ renpy.pause(1.5)
scene ep6_prom65 with dissolve
me "(Maybe they didn't dare go...)"
scene ep6_prom66 with dissolve
me "(...because they were too afraid of being judged by who they are.)"
scene ep6_prom67 with dissolve
me "(...)"
scene ep6_prom68 with dissolve
me "(Some didn't go because it was too painful.)"
if ep4SetupChrisWithLi:
    scene ep6_prom69 with dissolve
me "(And some were too busy being a friend...)"
scene ep6_prom79 with dissolve
me "(...of that person that lost his love on prom night.)"
scene ep6_prom77 with dissolve
me "(And in the middle of all this, someone noticed all this.)"
me "(That none of us really got a proper start of adulthood.)"
scene ep6_prom76 with dissolve
me "(You...)"
scene ep6_prom75c with dissolve
me "(You saw it...)"
me "(...didn't you.)"
scene ep6_prom75b with Dissolve(0.1, alpha=True)
stop music fadeout 5
$ renpy.pause(0.1)
scene ep6_prom75 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.3)
scene ep6_prom75b with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep6_prom75c with Dissolve(0.1, alpha=True)
ce "..."
scene bg empty with Dissolve(3, alpha=True)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_promgo
$ nowPlayingArtist = "I am Fowler"
$ nowPlayingTitle = "Cash"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],2,3,3,8]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
if Impact_Steph:
    scene ep6_pdance01 with dissolve
    me "Well, that escalated quickly."
else:
    scene ep6_pdance02 with dissolve
    me "Well, that escalated quickly."
scene ep6_pdance03 with dissolve
ch "Who cares, just look at them go."
scene ep6_pdance04 with dissolve
me "I'm quite sure Vasquez is a vampire."
ch "..."
me "You didn't really fuck her did you..."
ch "What do you think."
menu:
    "[M_06_014a]": # "Nah, you didn't.":
        scene ep6_pdance03 with dissolve
        ch "Exactly! But the look on your faces though."
    "[M_06_014b]": # "You did?":
        scene ep6_pdance03 with dissolve
        ch "Ask her."
ch "But can you explain to me again why we're standing here while all the girls are dancing?"
scene ep6_pdance04 with dissolve
me "Because not all the girls are dancing."
scene ep6_pdance05 with dissolve
ch "..."
scene ep6_pdance08 with dissolve
ki "..."
scene ep6_pdance06 with dissolve
ch "..."
scene ep6_pdance14 with dissolve
ro "..."
scene ep6_pdance04 with dissolve
ch "So, we're doing this?"
me "Damn sure we are."
if ep4NightChoose == 3:
    ch "You're not forgetting that you and Kira got a thing going, right?"
    me "Still doing it."
elif ep4NightChoose == 4:
    ch "You're not forgetting that you and Robin got a thing going, right?"
    me "Still doing it."
elif ep4NightChoose == 5:
    ch "You're not forgetting that you got a thing going with them, right?"
    me "Still doing it."
if ep4SetupChrisWith == 3:
    me "And you're sure?"
    ch "Hell yeah."
    me "You know you and Robin are probably going to be a thing of the past, right?"
    ch "Not worth it, if it means wedging them apart."
ch "So, choose your pray?"
menu:
    "[M_06_015a]": # "Kira.":
        me "Let me go get Kira."
        ch "Then I'll get Robin."
        jump ep6DanceSequenceMCKira
    "[M_06_015b]": # "Robin.":
        me "Let me go get Robin."
        ch "Then I'll get Kira."
        jump ep6DanceSequenceMCRobin
label ep6DanceSequenceMCKira:
scene ep6_pdance09 with dissolve
me "Wanna dance?"
ki "No, I'm good."
scene ep6_pdance10 with dissolve
me "Ok!"
ki "Heeeeeeeey."
me "Remember my dance at MaKenzie?"
scene ep6_pdance11 with dissolve
ki "..."
scene ep6_pdance18 with dissolve
ch "So I was thinking..."
ro "No dance."
scene ep6_pdance19 with dissolve
ch "OOOOOOOOH WHYYYYY YOU GOT TO GO TEAR MY HEART INTO ITTY BITTY TINY LITTLE PIECES, AND..."
ro "If I say yes, will you stop then?"
ch "Yep."
ch "...I CAN'T TAKE IT ANYMORE..."
ro "Let's go."
scene ep6_pdance20 with dissolve
ch "I'll show you all the right dance feelings."
ro "Now I just feel... dismay... regret... terror..."
scene ep6_pdance21 with dissolve
ki "Did you know that you can't dance for shit?"
scene ep6_pdance22 with dissolve
me "I try not to notice myself. It's more fun that way."
me "But there's one thing I'm good at."
scene ep6_pdance23 with dissolve
ki "Cleaning your apartment?"
scene ep6_pdance29 with dissolve
me "The twirl."
scene ep6_pdance30 with dissolve
stop music fadeout 1
me "And stop."
jump ep6DanceSequenceDone
label ep6DanceSequenceMCRobin:
scene ep6_pdance16 with dissolve
me "Wanna dance?"
ro "No. Just noooo..."
scene ep6_pdance17 with dissolve
ro "Give me strength."
scene ep6_pdance12 with dissolve
ch "*whistles*"
scene ep6_pdance13 with dissolve
ch "*whistles*"
scene ep6_pdance11 with dissolve
ch "*whistles*"
scene ep6_pdance24 with dissolve
ro "Should I be afraid?"
scene ep6_pdance25 with dissolve
me "What do you mean?"
scene ep6_pdance26 with dissolve
ro "You're all over the place."
scene ep6_pdance27 with dissolve
me "Let's throw you all over the place then."
stop music fadeout 1
scene ep6_pdance28 with dissolve
me "And stop."
jump ep6DanceSequenceDone
label ep6DanceSequenceDone:
play music ep6_makeup
$ nowPlayingArtist = "Christopher Young"
$ nowPlayingTitle = "GOOD X BACK"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],2,3,5,5]
scene ep6_pdance36 with fade
ro "..."
ki "..."
scene ep6_pdance37 with dissolve
ro "You're not wearing your usual makeup."
ki "Don't need that anymore."
ro "..."
ki "That's all you have to say?"
scene ep6_pdance38 with dissolve
ro "I can't stand seeing you miserable anymore."
ki "Miserable? Are you insane?"
ro "I see how you look at the normal couples when we're walking down the street."
ki "I always react like that when I see people in love. You know that."
ro "But I also see those tears forming in the corner of your eyes when you look at their kids."
scene ep6_pdance39 with dissolve
ro "I know how badly you want a child, Kira."
ki "So what if I can't have a child. I've made my peace with that a long time ago."
ro "But you don't need to. Literally any man in the world can give you that."
ro "I can't."
ki "You're severely overestimating the power of dick, Robin."
ro "It's human anatomy."
scene ep6_pdance40 with dissolve
ki "And my anatomy says I can't have a child... period."
ro "..."
ki "When I was younger, I got a bacterial infection."
ki "It got really bad, and I barely pulled through."
ro "You told me."
ki "But it destroyed me down there, ok?"
ro "Oh, Kira..."
scene ep6_pdance41 with dissolve
ro "Why didn't you tell me that part?"
ki "Would it have mattered?"
ro "No."
ki "People have been looking at me like I was damaged goods for a long time."
ki "I couldn't stand looking into your eyes too, seeing the same... pity... that I see in everyone else's eyes."
ki "So ok, I'm damaged. But that's just the way I am."
ro "Kira... If you say those words one more time, I'm going to slap you so hard."
ro "You're perfect, just the way you are."
ki "Then can you please stop with the bullshit, and start acting normal again?"
ro "Yes."
ki "So you open your gorgeous eyes and look at me the same way you've always looked at me. I don't want any pity or tears."
ro "Yes, Ma'am."
scene ep6_pdance42 with dissolve
ki "I think we have an audience."
scene ep6_pdance35 with dissolve
ro "They have no idea what we're talking about, do they."
scene ep6_pdance43 with dissolve
ki "Not the slightest clue."
scene ep6_pdance35 with dissolve
ro "Want to pretend we're fighting?"
ki "Would have been fun..."
scene ep6_pdance34 with dissolve
$ renpy.pause(0.1)
scene ep6_pdance33 with dissolve
$ renpy.pause(0.1)
scene ep6_pdance32 with dissolve
$ renpy.pause(0.1)
scene ep6_pdance31 with dissolve
$ renpy.pause()
scene ep6_pdance43 with dissolve
ki "On the other hand, that is a much better idea."
scene ep6_pdance44 with dissolve
ro "..."
scene ep6_pdance45 with dissolve
$ todayIs = 14
$ clockis = [[todayIs],0,0,1,2]
ch "Nailed it."
if ep4NightChoose == 3 or ep4NightChoose == 4 or ep4NightChoose == 5:
    if ep4SetupChrisWith == 3:
        me "You know we probably just became single again, right?"
        ce "Don't care. Not when I saw that look on their face."
    else:
        ce "But you know you probably just became single again, right?"
        me "Sure, but looking at them now... Worth it."
if ep4NightChoose == 2:
    me "But now, I want to dance with someone."
    me "Lexi, come back here."
    scene ep6_pdance46 with fade
    me "So, this party must be a bit underwhelming for you?"
    scene ep6_pdance47 with dissolve
    le "Are you kidding me? I've had so much fun!"
    le "I never went to my own prom."
    me "I figured as much. I never got to go to mine either."
    me "And now I'm dancing with the prom queen of all prom queens."
    scene ep6_pdance46 with dissolve
    le "Keep going, smooth talker."
    scene ep6_pdance47 with dissolve
    me "Maybe I should drop by Metronome real fast and pick up a $119 bottle of wine for us to share. I still owe you."
    scene ep6_pdance48 with dissolve
    le "Unfortunately, I've only got about 20 minutes left before I have to go."
    le "We just finished scheduling the next tour. I got the full list yesterday. It's going to be a big one."
    me "And how are you coping with that?"
    scene ep6_pdance49 with dissolve
    le "What do you mean?"
    me "When we arrived at your place earlier this summer, you told me... that when you get those tour lists, you cry."
    scene ep6_lexi01list160
    $ renpy.movie_cutscene("imov/ep6/ep6_lexi01list.webm", delay=None, loops=0, stop_music=False)
    le "Honestly, when I got that list this time, I almost collapsed."
    scene ep6_lexi02list320
    $ renpy.movie_cutscene("imov/ep6/ep6_lexi02list.webm", delay=None, loops=0, stop_music=False)
    le "So I guess I came here half way expecting to end this."
    scene ep6_pdance48 with dissolve
    me "Lexi..."
    le "Seeing that list reminded me of how long time I have to be away from you. Because of you it was much worse than it used to be."
    le "But this party, here with you guys, changed my mind."
    me "..."
    scene ep6_pdance49 with dissolve
    le "I'm cutting down on touring."
    me "I don't want you to do that for me."
    scene ep6_pdance50 with dissolve
    le "I'm doing it for us."
    me "Now I feel guilty."
    le "Don't be..."
    scene ep6_pdance51 with dissolve
    le "And can we please stop talking about this?"
    le "So I can get enjoy these last 16 minutes before I have to go, making out with the one I love?"
    me "I think that can be arranged."
    scene ep6_pdance52 with dissolve
    me "..."
    scene ep6_pdance50 with dissolve
    me "We got eyes on us."
    le "Paparazzi?"
    scene ep6_pdance53 with dissolve
    le "Who cares. They can watch."
    me "No, not Paparazzi."
    scene ep6_kirarobinrevenge with dissolve
    me "A batshit crazy lesbian couple."
    scene ep6_pdance53 with dissolve
    le "*laughs* Guess we deserve that."
    le "Well what the heck, they can watch too. Because we're down to 14 minutes, and I don't care anymore."
    scene ep6_pdance54 with dissolve
    "..."
elif ep4NightChoose == 7:
    me "But now, I want to dance with my special lady."
    me "Steph?"
    scene ep6_pdance57 with fade
    st "We finally got it."
    me "Prom you mean?"
    st "Yes."
    me "And I didn't even know you were coming."
    scene ep6_pdance58 with dissolve
    st "Not a bad surprise I take it?"
    me "No, a very very good one."
    me "I should have wore a tux."
    scene ep6_pdance57 with dissolve
    st "You look fine just the way you are."
    me "So what happened back home. Spill."
    scene ep6_pdance59 with dissolve
    st "It didn't go well. But then again, deep down inside I didn't expect it to."
    if ep6TriedCallingSteph:
        me "Yeah, you told me on the phone."
        me "Basically, I needed to think things over for a bit."
    else:
        st "You're not the only one I had to ghost for two years, you know..."
        me "Shit, I didn't even think of that."
        st "So I needed to think things over for a bit."
    st "That's why I drove all the way back here."
    st "But I took a detour on the way. I drove to that house I lived in for a year, while in WitSec."
    st "In some ways it was so much easier living there. Getting away from everyone."
    st "I wasn't drawn in all directions at once."
    scene ep6_pdance60
    $ renpy.movie_cutscene("imov/ep6/ep6_steph01walk.webm", delay=None, loops=0, stop_music=False)
    st "But then you called."
    st "Suddenly things wasn't so bad. Because I know you're there with me."
    st "You took me back after all this time, so I know you always will be."
    st "So I realized I'm only drawn in one direction."
    st "To you."
    me "Steph?"
    scene ep6_pdance61 with dissolve
    st "Yes, darling?"
    me "Did you practice that speech in the car all the way home?"
    st "No..."
    scene ep6_pdance58 with dissolve
    st "Only the last 25 miles or so."
    st "Did I pass?"
    scene ep6_pdance57 with dissolve
    me "With flying colors."
    me "And let's visit your dad together some day."
    scene ep6_pdance58 with dissolve
    st "How is that supposed to help?"
    me "No idea. But I have something I want to tell him face to face."
    st "What's that?"
    me "That's between me and him."
    scene ep6_pdance60 with dissolve
    me "But now I just want to enjoy the prom dance I never got, with my prom queen."
    scene ep6_pdance61 with dissolve
    st "That sounds like a great idea."
elif ep4NightChoose == 6:
    me "But now, I'm going to go find Linda."
    me "I want to dance."
    scene ep6_pdance62 with fade
    me "So... How's prom?"
    scene ep6_pdance63 with dissolve
    li "I can't believe you went ahead and did this."
    me "I didn't honestly. Cece planned it all."
    me "It was just supposed to be a little reunion between me, you, and Chris, showing Cece our old school."
    me "Everything else is her doing."
    scene ep6_pdance64 with dissolve
    li "I guess I have to thank her later then."
    me "You should."
    li "But after tonight, where do we go from there?"
    me "My apartment is still ready for you."
    me "And when it comes to Cece..."
    scene ep6_pdance63 with dissolve
    li "...she should stay."
    li "I think you're helping her. She's look better than I've ever seen her."
    me "Hopefully."
    scene ep6_pdance67 with dissolve
    li "..."
    scene ep6_pdance66 with dissolve
    me "You're still horny, aren't you."
    li "I am."
    li "And I have something I want to show you."
    me "Let me guess. It's a surprise?"
    li "No surprise. I have a special place on this school. We're going to go there, and we are going to have amazing sex."
    scene ep6_pdance64 with dissolve
    li "So, how about it?"
    me "Tough question. Do I have any lifelines?"
    li "Really?"
    stop music fadeout 4
    me "I mean, should I ask the audience, or is there a 50-50, or..."
    me "...maybe I could phone a friend."
    scene ep6_pdance66 with dissolve
    li "You already won the prize. Now you just need to collect."
    me "Lead the way."
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    play music ep6_lindaroof
    $ nowPlayingArtist = "Micheal Shynes"
    $ nowPlayingTitle = "Break Me"
    $ nowPlayingRealArtist = ""
    $ nowPlayingRealTitle = ""
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep6_linda11 with fade
    li "Here we are."
    scene ep6_linda12 with dissolve
    me "This is the roof."
    li "Cool isn't it."
    me "You used to spend time here?"
    li "I did."
    scene ep6_linda13 with dissolve
    li "Come here, there's more."
    scene ep6_linda14 with fade
    me "Wow, careful there. It's a long way down."
    scene ep6_linda15 with dissolve
    li "You're such a pussy."
    scene ep6_linda16 with dissolve
    me "Am not. But we've had something to drink."
    scene ep6_linda14 with dissolve
    li "I used to sit here when I got bored, or had some spare time."
    li "It's so weird seeing those little people strolling along with all their problems."
    me "And?"
    li "And from up here, those problems are little problems."
    li "So, one day I saw you sneaking away..."
    scene ep6_linda15 with dissolve
    li "...with Steph."
    me "Oh... That time."
    scene ep6_linda14 with dissolve
    li "The two of you snuck around in the alley."
    li "I was just about to call out for you, when you got on with it."
    li "And I mean, you two really got on with it."
    scene ep6_linda16 with dissolve
    me "Linda..."
    menu:
        "[M_06_016a]": # "Stop.":
            me "...this is weird, please stop."
            scene ep6_linda15 with dissolve
            li "Don't worry, the hard part is over."
            li "That speech you had on the bench a bit earlier made me realize that you two back then wasn't a real problem."
            scene ep6_linda14 with dissolve
            li "A little one, sure. Like from up here, I didn't really care that you two got it on. I kind of got a kick out of it and thought it was funny."
            scene ep6_linda15 with dissolve
            li "When I was closer to you, or we were hanging out all of us, it was worse."
            scene ep6_linda16 with dissolve
            me "So what's your point."
            scene ep6_linda15 with dissolve
            li "And now it's all in the past. And the problem is even smaller. In fact it's not a problem at all."
            scene ep6_linda14 with dissolve
            me "It's still slightly weird that you saw me and Steph."
            scene ep6_linda15 with dissolve
            li "Oh, shush... You didn't have a problem with me blowing you several times a week."
            scene ep6_linda17 with dissolve
            me "True."
        "[M_06_016b]": # "Go on...":
            $ ep6HeardLindasFantasy = True
            me "Go on..."
            scene ep6_linda15 with dissolve
            li "You fucked that woman like there was no tomorrow."
            scene ep6_linda14 with dissolve
            li "I remember wondering why I wasn't more hurt by it."
            li "Seeing you two together."
            li "Maybe it was because you were so far away, that I didn't really see the problem in it."
            scene ep6_linda15 with dissolve
            li "Instead, I got horny."
            li "So very horny."
            me "Really?"
            scene ep6_linda14 with dissolve
            li "In the end I couldn't take it anymore, and I started rubbing myself."
            li "I kept my eyes peeled at you and followed your movements."
            li "In... Out... In... Out..."
            li "In the end I came harder than I've ever have before."
            li "I almost blacked out and fell forward."
            me "Holy shit, Linda."
            li "Yeah, that would have been an embarassing way to go."
            scene ep6_linda15 with dissolve
            li "But I'm just saying, that when you had that speech on the bench a bit earlier, I remembered."
            li "It changed the way I feel about everything that happened before."
            scene ep6_linda16 with dissolve
            me "Well, just be careful you don't do any masturbating on high places again, please."
            me "You got some powerful orgasms."
            me "Call for me instead, and I'll take care of them for you."
            scene ep6_linda17 with dissolve
            li "Sounds like a good deal."
    scene ep6_linda18 with dissolve
    li "So you're not a fan of heights?"
    me "I don't have a problem with heights."
    scene ep6_linda19 with dissolve
    me "It's just that I don't want to accidentally fall off a building before I get the amazing sex part you mentioned earlier."
    li "Mhmm..."
    scene ep6_linda20 with dissolve
    li "So [name]..."
    show ep6_linda20d at imgSlide_ep6LindaRoof_c
    show ep6_linda20c at imgSlide_ep6LindaRoof_b
    show ep6_linda20b at imgSlide_ep6LindaRoof_a
    li "Come do your duty and fuck me then."
    scene ep6_linda21 with dissolve
    hide ep6_linda20d
    hide ep6_linda20c
    hide ep6_linda20b
    me "Linda, you look amazing."
    li "I know we had our fair share of fun this summer."
    scene ep6_linda22 with dissolve
    li "But this time, I feel like we're finally there."
    scene ep6_linda23 with dissolve
    li "And I can claim the prize."
    scene ep6_linda24 with dissolve
    li "So get out of your pants, cowboy. And give me that prize."
    scene ep6_linda25 with dissolve
    li "Give it to me real good..."
    scene ep6_linda26 with dissolve
    li "...from the top of the school building I used to hate."
    scene ep6_linda27 with dissolve
    li "And fuck me like there's no tomorrow."
    scene ep6_linda28 with hpunch
    uk "..."
    scene ep6_linda29 with dissolve
    uk "What the..."
    scene ep6_linda30 with dissolve
    uk "*sniffs*"
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep6_linda31
    $ renpy.movie_cutscene("imov/ep6/ep6_linda01ride.webm", delay=None, loops=0, stop_music=False)
    me "Fucking hell, Linda."
    me "Where did all this confidence come from."
    li "Keep going."
    scene ep6_linda01roof with dissolve
    $ renpy.pause()
    scene ep6_linda32 with dissolve
    me "Got to say, I think I like this new Linda."
    scene ep6_linda33 with dissolve
    li "And you're perfect just the way you are."
    scene ep6_linda01roof with dissolve
    me "How about we..."
    li "Say no more..."
    scene ep6_linda34 with dissolve
    li "Hurry."
    me "Hurry? We need to get back?"
    scene ep6_linda35 with dissolve
    li "No, not that. I'm close, and I want to cum."
    scene ep6_linda01bend with dissolve
    me "Damn close myself."
    li "In that case..."
    scene ep6_linda36 with dissolve
    li "Cum!"
    scene ep6_linda37 with dissolve
    me "Linda..."
    scene ep6_linda38 with hpunch
    me "..."
    scene ep6_linda39 with hpunch
    li "..."
    scene ep6_linda40 with dissolve
    $ renpy.pause()
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep6_linda41 with dissolve
    li "This is perfect."
    scene ep6_linda42 with dissolve
    me "I wonder why we didn't do this before?"
    scene ep6_linda41 with dissolve
    li "You want me to spell out the name of the reason?"
    scene ep6_linda42 with dissolve
    me "Probably best not to."
    scene ep6_linda41 with dissolve
    li "Exactly."
    scene ep6_linda43 with dissolve
    li "This is it, you know."
    li "My happy ending."
    scene ep6_linda44 with dissolve
    me "It's my happy ending too."
    me "I'm just sorry it took so long to realize it."
    li "..."
    me "We should head back down to the others, shouldn't we."
    li "You're probably right."
    li "I have to catch Steph. We agreed I follow her home."
    scene ep6_linda45 with dissolve
    li "Guess I'll just have to miss this guy for the rest of the night."
    me "..."
    li "Jeez, you ever not ready?"
    me "The way you're fondling me, probably not."
    scene ep6_linda44 with dissolve
    li "You just stay ready 'til I come back."
    me "Will do."
    stop music fadeout 12
else:
    me "But now, I want to dance with someone."
    me "Lexi, you're not getting away from me that easily. Come back here."
    scene ep6_pdance46 with fade
    me "So, this party must be a bit underwhelming for you?"
    scene ep6_pdance47 with dissolve
    le "Are you kidding me? I'm having so much fun!"
    le "I never went to my own prom."
    me "I figured. I never got to go to mine either."
    scene ep6_pdance49 with dissolve
    if ep4NightChoose == 5:
        le "So why are you dancing with me and not your prom queens?"
    else:
        le "So why are you dancing with me and not your prom queen?"
    me "Knowing you and your busy schedule, I'm thinking you're just about on your way to leave already."
    me "So I had to steal a dance before you left."
    scene ep6_pdance47 with dissolve
    le "True. Unfortunately I have to go in about 20 minutes."
    le "New tour coming up. I'll get you guys tickets if you want. Just ask."
    me "Be careful, will you? Don't want you to have a burnout now."
    le "I know my limits."
    scene ep6_pdance48 with dissolve
    me "I think you do. But if what you told me is right, and you're looking for love..."
    me "...you probably won't find it if you're touring all the time."
    scene ep6_pdance47 with dissolve
    le "Good point. Unless another interesting guy shows up in the VIP area at Metronome."
    me "You never know. Might set you back $119 though."
    le "Plus tip, even."
    if ep4NightChoose == 1:
        le "Your girlfriend over there is looking at us and smiling."
        me "That's probably my cue to head over to her."
    else:
        le "Cece is looking at us and smiling."
        me "I'll head over to her then."
    scene ep6_pdance49 with dissolve
    le "Just one thing. Is she... how do I say this... ok?"
    me "I think she's getting there."
    me "Depression doesn't go away over night, or even a summer."
    me "But hopefully with time, she's going to get there."
    le "I know professional institutions that can help if you want to."
    le "That, or anything else she might need, and you give me a call, ok?"
    le "Anything at all, and I'll cover any cost."
    me "..."
    le "Promise me!"
    me "I promise."
    scene ep6_pdance50 with dissolve
    le "And [name]... I had a blast all summer with you. I'll always remember it."
    me "So did I. Maybe we can have a reunion next summer."
    le "Hopefully."
scene bg empty with fade
$ clockis = [[todayIs],0,1,3,3]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_pdance68 with dissolve
me "So, how's the mastermind behind all this doing?"
scene ep6_pdance69 with dissolve
ce "You're giving me way to much credit for this."
ce "I just called them. They are the ones who showed up and did everything."
me "Seeing all of us happy. It helps you, doesn't it."
scene ep6_pdance70 with dissolve
ce "It helps everybody."
scene ep6_pdance71 with dissolve
me "..."
me "I can see that you're still struggling."
ce "It just gets tougher to deal with it when I tire."
ce "On long days, like this."
me "Then let's call it a day, and get some well earned rest."
scene ep6_pdance72 with dissolve
ce "There's still a party going on."
me "It's nearing its end. People have started doing some minor cleaning up."
me "I can come back tomorrow with Chris and we'll do the rest of the cleanup then."
scene ep6_pdance75 with dissolve
ce "I wish it could last longer. I don't want the day to end."
me "That's proof of a successful prom, right there."
scene ep6_pdance74 with dissolve
me "You did good, Cece."
me "Now let's get you home."
ce "Home..."
scene ep6_pdance73 with dissolve
ce "I miss my family. I write them every day."
me "Then how about me and you visit them one day. Just say when and I'll drive you."
ce "Can you tell them I had a lot of fun this summer?"
ce "I'm not good at saying those things."
me "Of course. There's a lot of nice things about you I want to tell them."
ce "Good."
me "Then let's head home."
scene ep6_pdance74 with dissolve
stop music fadeout 3
ce "Just give me a moment to say goodbye to everyone first."
scene bg empty with fade
$ clockis = [[todayIs],0,2,1,4]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_evening01 with fade
play music ep6_cecetell
$ nowPlayingArtist = "Michael McQuaid"
$ nowPlayingTitle = "Bones"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "So... you doing better?"
scene ep6_evening02 with dissolve
ce "Of course."
me "I mean, we could dig up another good old classic movie and watch it if you'd like or just call it a night."
me "It is getting quite late."
scene ep6_evening03 with dissolve
ce "*exhales*"
scene ep6_evening04 with dissolve
me "You're not really ok, are you."
ce "I'm never really ok, you know that."
scene ep6_evening05 with dissolve
ce "But why today of all days. This was... supposed to be special."
scene ep6_evening06 with dissolve
me "It was."
scene ep6_evening08 with dissolve
ce "I just wanted it to be perfect."
me "Cece... Open up to me."
me "Tell me how it is to be you."
ce "You don't want to know."
me "I do."
scene ep6_evening09 with dissolve
ce "I'll... hurt you."
me "How can I do what's best for you if I don't know what you feel."
me "Tell me."
ce "I can't."
me "Bullshit."
scene ep6_evening10 with dissolve
ce "You really want to know?"
me "Yes!"
ce "You won't like it."
me "That's up to me to decide."
ce "Fine..."
scene ep6_evening11 with dissolve
ce "Close your eyes."
me "What?"
scene ep6_evening12 with dissolve
ce "Just... close your eyes."
hide screen phone
scene bg empty with fade
ce "And just listen to my voice."
ce "..."
ce "Imagine that you feel something. Anything at all. Then imagine it is strongly amplified."
ce "It can be anything. Good or bad. It doesn't matter."
ce "Like feeling bad because you let someone down, or even think you do."
ce "Then there's real feelings, like nausea."
scene ep6_evening13 with dissolve
ce "They gets amplified too."
scene ep6_evening14 with dissolve
ce "Even the simplest tasks becomes hell on earth to manage."
scene ep6_evening16 with dissolve
ce "Like going to the store. Because you need food, right?"
scene ep6_evening18 with dissolve
ce "So you're going to the store, or making yourself, because you know what will happen."
ce "Once you're there, some child is shouting something, making you jump. That is amplified too."
scene ep6_evening17 with dissolve
ce "Your heart is racing, and it just doesn't slow down. Because you react to the jumpscare stronger than you should."
ce "Then you start panicking, knowing you have to move fast if you're going to manage to finish without running out the front door."
ce "You begin to shake, and that get's amplified."
ce "You see someone in front of you."
scene ep6_evening19 with dissolve
ce "In panic you try to hide somewhere. Finding some completely random different thing to look at."
scene ep6_evening20 with dissolve
ce "You cold sweat, feeling their eyes on you. Nausea kicks in. You get dizzy."
scene ep6_evening22 with dissolve
ce "You want to be anywhere but there, but you have to follow through."
scene ep6_evening24 with dissolve
ce "You feel them talking about you."
scene ep6_evening23 with dissolve
ce "Even if deep down inside, you know they're not."
scene ep6_evening25 with dissolve
ce "Finally they leave."
scene ep6_evening21 with dissolve
ce "You draw your breath and prepare to continue. By now your head is hurting. And that gets amplified."
scene ep6_evening27 with dissolve
ce "And that bag of chips you really, really want..."
scene ep6_evening26 with Dissolve(3, alpha=True)
ce "...it could just as well have been on another planet, because by now your legs are so weak you can barely walk."
ce "You end up picking up a few random things that's within reach, while silently hoping that there's no queue at the checkout."
scene ep6_evening28 with dissolve
ce "But that never happens. The queue is as long as it always is."
ce "So you stand there in queue. About a million different emotions going through your head, and none of them any good."
ce "You want to ask the one in front of you to talk a bit lower..."
ce "...and that guy behind you that just smells a bit odd..."
ce "...or the tiny girl that's looking at you for some reason..."
ce "...all of it is amplified."
ce "Maybe you've seen someone like that once too. Some young girl standing in the queue at your local store looking completely lost."
ce "That girl that wanted to skip ahead of you in the queue, that you denied doing so, because you want to get home earlier."
ce "Maybe that girl went through hell right then and there."
ce "Finally you get home, you made it. And you sit down, exhausted. So disappointed, because you know you're not working properly."
ce "And you cry."
ce "And all of those feelings are amplified too."
ce "They tear you apart."
me "..."
scene ep6_evening29 with dissolve
ce "Then there's good feelings too."
ce "You meet someone who you really like. Someone that seems to care so much for you."
scene ep6_evening30 with dissolve
ce "But you can't tell them who you really are."
ce "Because that person will either not like you anymore, or..."
scene ep6_evening31 with dissolve
ce "...be hurt by what you're telling him."
ce "In the end, you know you'll just end up hurting him even more."
scene ep6_evening32 with dissolve
ce "Because he thinks he can fix you."
ce "But he can't..."
scene ep6_evening33 with dissolve
ce "And he doesn't even seem to know that the only reason I'm here, is because of him."
stop music fadeout 4
scene ep6_evening35 with dissolve
ce "See? I never should have told you anything."
scene ep6_evening36 with dissolve
ce "Now when you think about this day, you'll remember this."
ce "Not everything else I wanted you to remember."
scene ep6_evening37 with dissolve
ce "I knew I would hurt..."
scene ep6_evening38 with dissolve
ce "...you."
scene ep6_evening39 with dissolve
ce "..."
scene ep6_evening40 with dissolve
ce "..."
me "Close your eyes."
ce "..."
me "Just close your eyes."
scene bg empty with fade
$ clockis = [[todayIs],0,2,4,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep6_mcguitar
$ nowPlayingArtist = "Will van de Crommert"
$ nowPlayingTitle = "Sovereign Hearts"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
scene ep6_evening44c with dissolve
$ renpy.pause()
scene ep6_evening44b at imgSlide_ep6CeceRelax2
$ renpy.pause()
scene ep6_evening41 with dissolve
$ renpy.pause()
scene ep6_evening42 with dissolve
$ renpy.pause()
scene ep6_evening43 with dissolve
$ renpy.pause()
scene ep6_evening44 at imgSlide_ep6CeceRelax
$ renpy.pause()
scene ep6_evening45 with dissolve
$ renpy.pause()
scene ep2_endbench10 with Dissolve(3, alpha=True)
me "{i}I connected with my feelings again.{/i}"
scene ep2_endbench09 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep2_endbench08 with Dissolve(0.1, alpha=True)
$ renpy.pause()
if ep4NightChoose == 1:
    scene ep4_mccecenight10 with Dissolve(1.5, alpha=True)
    ce "{i}I thought you said good memories...{/i}"
    scene ep4_mccecenight45 with dissolve
    ce "{i}You are going to talk about feelings again, aren't you.{/i}"
    scene ep4_mccecenight_blink with dissolve
    me "{i}No...{/i}"
    me "{i}I'm going to enjoy them.{/i}"
    scene ep4_mccecenight42 with dissolve
    ce "{i}...{/i}"
    scene ep5_cecewake32 with dissolve
    ce "{i}I want you.{/i}"
    show ep4_cecemoment01_bg at imgSlide_ep6CeceRemember_b
    show ep4_cecemoment01 at imgSlide_ep6CeceRemember_a
    $ renpy.pause(5)
    scene bg empty with fade
    $ renpy.pause(0.5)
    hide ep4_cecemoment01
    hide ep4_cecemoment01_bg
else:
    scene ep4p2_aftersteph42 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
    scene ep4p2_party_cecelexi20 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
    scene ep4_partystarted32 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
    scene ep4_partystarted22 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
    scene ep3_lexis26 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
    scene ep4_stephcon48 with Dissolve(1, alpha=True)
    $ renpy.pause(1.5)
scene ep2_endbench08 with Dissolve(0.1, alpha=True)
me "{i}So you see... Feelings aren't a bad thing.{/i}"
scene ep2_endbench14 with Dissolve(2, alpha=True)
ce "{i}...{/i}"
me "{i}And you shouldn't be ashamed for having them, or be afraid of them.{/i}"
scene ep2_endbench15 with Dissolve(2, alpha=True)
me "{i}It's when you embrace them, you start to... heal.{/i}"
scene ep2_endbench16 with dissolve
ce "{i}...{/i}"
scene ep6_evening46b with Dissolve(3, alpha=True)
$ renpy.pause()
scene ep6_evening47 with dissolve
$ renpy.pause()
stop music
scene ep6_evening48 with dissolve
me "Ok, it's far from perfect, but it's the one I know how to play and..."
play music ep6_mcguitarafter
$ nowPlayingArtist = "Joy Hanna"
$ nowPlayingTitle = "Carry You"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_evening49 with dissolve
me "..."
scene ep6_evening50 with dissolve
$ clockis = [[todayIs],0,2,5,0]
ce "And still it was perfect for me."
if ep4NightChoose == 2:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I have a girlfriend, you know."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "Duh, you've got this rich superstar girlfriend. Anybody sane would have jumped right on that plane."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think about her."
    scene ep6_epilogue73 with dissolve
    me "I think I'm a bit worried about us. I think she's having problems tackling the distance between us."
    ce "Sure, I think that's a good point."
    ce "But you know what she told me?"
    ce "That day you first met her..."
    scene ep6_lexiend07 with dissolve
    ce "...her manager had told her to go pick up a guy."
    ce "Something about getting some extra publicity."
    scene ep6_lexiend08 with dissolve
    ce "They even argued a bit and she said that she wasn't going to do that just because he wanted it."
    me "Not sure how I feel about that guy."
    scene ep6_lexiend01 with dissolve
    ce "Well, either way you look at it, she decided to do it anyway."
    scene ep6_lexiend02 with dissolve
    ce "So she started looking around for someone interesting."
    scene ep6_lexiend03 with dissolve
    ce "Then she saw you at the bar."
    scene ep6_lexiend04 with dissolve
    ce "She even told me that you were even that cute by first glance."
    scene ep6_lexiend05 with dissolve
    ce "But you were the only one there."
    scene ep6_lexiend06 with dissolve
    ce "So she went for it."
    scene ep1_metro_bar_lexi02 with dissolve
    ce "And in the 15 minutes you two had together."
    scene ep1_metro_bar_lexi03 with dissolve
    ce "You made quite the impression."
    scene ep1_metro_bar_lexi08 with dissolve
    ce "I don't think she even registered herself."
    scene ep1_metro_bar_lexi13 with dissolve
    ce "Not until later."
    scene ep6_lexiend11 with fade
    ce "When she was trying to sleep."
    scene ep6_lexiend12 with dissolve
    ce "Something she had no problems with earlier."
    scene ep6_lexiend13 with dissolve
    ce "But this time she couldn't."
    scene ep6_lexiend10 with dissolve
    ce "Because she was thinking about you."
    ce "And somehow she missed you, even if you'd just met."
    scene ep6_lexiend09 with dissolve
    ce "She had never experienced anything like it before."
    scene ep6_lexiend14 with dissolve
    ce "And the more she thought about it, the more she missed you."
    ce "So she decided she would do something she normally would never do."
    scene ep6_lexiend15 with dissolve
    ce "She decided she would call you."
    scene ep6_epilogue73 with dissolve
    ce "I guess what I'm trying to say is..."
    ce "Maybe there's always a reason for something to happen."
    ce "..."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
elif ep4NightChoose == 3:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I don't think sex..."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "You could have gone with Kira. Should have. To talk at least."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think for a bit."
    me "I think that thing is done and over now anyway."
    scene ep6_kiraend09 with dissolve
    ce "I had troubles getting a read on Kira at first."
    scene ep6_kiraend01 with dissolve
    ce "And I didn't really see the two of you fit together."
    scene ep6_kiraend02 with dissolve
    ce "It was like she tried to fit in a role to match her own description of normal."
    scene ep6_kiraend03 with dissolve
    ce "But when she kissed me at Lexi's place I realized how fantastic she is."
    ce "And she is hiding under so many layers, it's hard to spot the real Kira."
    scene ep6_kiraend04 with dissolve
    ce "You need to show her something."
    scene ep6_kiraend05 with Dissolve(1, alpha=True)
    ce "Show her that she doesn't have to fit any role."
    scene ep6_kiraend06 with dissolve
    ce "Not the role of a daughter, friend, lover or restaurant worker."
    scene ep6_kiraend07 with Dissolve(1, alpha=True)
    ce "Show her that she can do whatever she wants. And she might just find..."
    scene ep6_kiraend08 with Dissolve(2, alpha=True)
    ce "...her own version of normal."
    scene ep6_epilogue73 with dissolve
    ce "I guess what I'm trying to say is..."
    ce "Don't give up on her. There's something she needs. And you can give it."
    ce "..."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
elif ep4NightChoose == 4:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I don't think sex..."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "You could have gone with Robin. Should have. To talk at least."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think for a bit."
    me "I think that thing is done and over now anyway."
    scene ep6_robinend01 with dissolve
    ce "I could never get a read on why you and Robin became a thing."
    me "I can't help who I fall for."
    ce "No, I meant why she would fall for you. I doubted it for a while. Thinking she did it for Kira."
    scene ep6_robinend02 with dissolve
    ce "But then I saw it."
    ce "Those hidden small looks she gave you every once in a while."
    scene ep6_robinend03 with dissolve
    ce "Always when you're not looking."
    scene ep6_robinend05 with dissolve
    ce "I think the whole competition thing is just something she enjoys doing."
    scene ep6_robinend06 with dissolve
    ce "Something that connects the two of you."
    scene ep6_robinend07 with dissolve
    ce "Being challenged in ways Kira can't, because she's a different type of person."
    scene ep6_robinend08 with dissolve
    ce "I don't know where you stand with her now, after what happened tonight."
    scene ep6_robinend10 with dissolve
    ce "But I think that maybe..."
    scene ep6_robinend11 with dissolve
    ce "...deep down inside she realizes..."
    scene ep6_robinend13 with dissolve
    ce "...she loves you more than she loves Kira."
    scene ep6_epilogue71 with dissolve
    ce "I guess what I'm trying to say is, some choices doesn't make sense."
    ce "And they might break somebody's heart."
    scene ep6_epilogue73 with dissolve
    ce "But it's still the right thing to do."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
elif ep4NightChoose == 5:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I don't think sex..."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "You could have gone with Robin and Kira. Should have. To talk at least."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think for a bit."
    ce "Robin and Kira... They both offered themselves to you."
    scene ep6_epilogue72 with dissolve
    ce "You said it was meant to be a fun thing, right?"
    me "That's what they said. And it was. But now I'm not sure."
    scene ep6_kiraend09 with dissolve
    ce "I had troubles getting a read on Kira at first."
    scene ep6_kiraend01 with dissolve
    ce "And I didn't really see the two of you fit together."
    scene ep6_kiraend02 with dissolve
    ce "It was like she tried to fit in a role to match her own description of normal."
    scene ep6_kiraend03 with dissolve
    ce "But when she kissed me at Lexi's place I realized how fantastic she is."
    ce "And she is hiding under so many layers, it's hard to spot the real Kira."
    scene ep6_kiraend04 with dissolve
    ce "You need to show her something."
    scene ep6_kiraend05 with Dissolve(1, alpha=True)
    ce "Show her that she doesn't have to fit any role."
    scene ep6_kiraend06 with dissolve
    ce "Not the role of a daughter, friend, lover or restaurant worker."
    scene ep6_kiraend07 with Dissolve(1, alpha=True)
    ce "Show her that she can do whatever she wants. And she might just find her own version of normal."
    scene ep6_robinend02 with fade
    ce "And Robin. I've seen the looks she gives you."
    scene ep6_robinend03 with dissolve
    ce "Always when you're not looking."
    scene ep6_robinend05 with dissolve
    ce "I think the whole competition thing is just something she enjoys doing."
    scene ep6_robinend06 with dissolve
    ce "Something that connects the two of you, even if you're three."
    scene ep6_robinend07 with dissolve
    ce "So, if you feel like you're a wedge between them."
    scene ep6_robinend08 with dissolve
    ce "Then you're forgetting the most important part."
    scene ep6_robinend09 with dissolve
    ce "Even if it by no means is a normal relationship..."
    scene ep6_robinend10 with dissolve
    $ renpy.pause(1)
    scene ep6_robinend11 with dissolve
    $ renpy.pause(1)
    scene ep6_robinend13 with dissolve
    ce "...you, Robin..."
    scene ep6_robinend12 with dissolve
    ce "...and Kira..."
    scene ep6_robinend14 with Dissolve(2, alpha=True)
    ce "...and that problem they are having..."
    scene ep6_robinend15 with dissolve
    ce "...you might just be the solution to that."
    scene ep6_epilogue71 with dissolve
    ce "I guess what I'm trying to say is, if you look past the sex part."
    scene ep6_epilogue73 with dissolve
    ce "You might be able to build the most beautiful thing in the world."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
elif ep4NightChoose == 6:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I have a girlfriend, you know."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "Duh, you've got this girlfriend that's longing for you. She'd do anything."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think about her."
    scene ep6_epilogue66 with dissolve
    me "I'm certain that she's 100%% ok with me being here with you."
    ce "Still, she should be your first choice."
    scene ep6_lindaend13 with fade
    ce "You know, when I met her we got along instantly."
    scene ep6_lindaend14 with dissolve
    ce "I think she thought she was helping me, but I think we both helped each other."
    scene ep6_lindaend05 with dissolve
    ce "She was always talking about you, Steph and Chris."
    scene ep6_lindaend07 with dissolve
    ce "She remembered the smallest details, even from the day she met you."
    scene ep6_lindaend08 with dissolve
    ce "Or the day Steph walked into the classroom for the first time."
    scene ep6_lindaend09 with dissolve
    ce "And how they became the best of friends."
    scene ep6_lindaend10 with dissolve
    ce "..."
    scene ep6_lindaend11 with dissolve
    ce "She thought all the signs she saw..."
    scene ep6_lindaend12 with hpunch
    ce "...was you liking her."
    scene ep6_lindaend01 with dissolve
    ce "Until one day she realized..."
    scene ep6_lindaend02 with dissolve
    ce "...she had it all wrong."
    scene ep6_lindaend03 with dissolve
    ce "You liked someone else."
    scene ep6_lindaend04 with dissolve
    ce "It nearly broke her."
    scene ep6_epilogue71 with dissolve
    ce "I guess what I'm trying to say is, don't break her heart again."
    ce "Even if you didn't know you did the first time."
    scene ep6_epilogue73 with dissolve
    ce "I'm afraid of what will happen if you do."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
elif ep4NightChoose == 7:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening52 with dissolve
    $ renpy.pause()
    ce "Come join me in bed. I want to give you something."
    me "I have a girlfriend, you know."
    ce "It's not that."
    ce "Come..."
    scene ep6_epilogue65 with fade
    ce "See?"
    me "Feels good."
    ce "Exactly."
    scene ep6_epilogue66 with dissolve
    me "You're good with your hands."
    ce "I know."
    scene ep6_epilogue67 with dissolve
    me "But you don't have to do this. I'm fine without it."
    scene ep6_epilogue68 with dissolve
    ce "Will you just relax..."
    scene ep6_epilogue66 with dissolve
    ce "But I have to ask, why did you go here with me tonight."
    me "I can't just leave you alone."
    scene ep6_epilogue72 with dissolve
    ce "Duh, you've got this girlfriend you haven't seen in a long time."
    me "Guess I feel a bit connected to you."
    scene ep6_epilogue71 with dissolve
    ce "Well, stop that. Right now."
    ce "Just close your eyes and think about Steph."
    scene ep6_epilogue66 with dissolve
    me "I've thought about her for two years."
    me "Part of me hasn't even realized she's back."
    scene ep6_epilogue73 with dissolve
    ce "You know what she told me?"
    me "What?"
    scene ep6_stephend01 with fade
    ce "That day she joined your school."
    me "You mean pretend join?"
    ce "Sure."
    scene ep6_stephend02 with dissolve
    ce "She told me she walked into class, like it was a job just like any other."
    scene ep6_stephend03 with dissolve
    ce "It was just going to be a quick job. One week. Two at the most."
    scene ep6_stephend04 with dissolve
    ce "She was going to find an opening, talk to you, then report back and quit."
    scene ep6_stephend05 with dissolve
    ce "But the moment she saw you..."
    scene ep6_stephend06 with dissolve
    ce "...she forgot everything."
    ce "And she probably didn't tell you this, but..."
    scene ep3_prologue_blink with fade
    ce "...that last day on the beach you two had."
    ce "She had already been arrested then. She wrote a letter to you at the airport while waiting to board the plane."
    ce "Then she escaped, because she had to see you one more time."
    scene ep1_metro_dancing_03 with dissolve
    ce "And that time at the metro..."
    scene ep1_metro_dancing_05 with dissolve
    $ renpy.pause(0.5)
    scene ep1_metro_dancing_06 with Dissolve(0.25, alpha=True)
    $ renpy.pause(0.5)
    scene ep1_metro_dancing_08 with Dissolve(0.25, alpha=True)
    ce "...was just like seeing you that first time. It all came back."
    scene ep6_stephend07 with fade
    ce "And when you walked home later on..."
    scene ep6_stephend09 with dissolve
    ce "...she still had no clue what to do about it."
    scene ep6_stephend08 with dissolve
    ce "There was regret she had jumped you earlier..."
    scene ep6_stephend12 with dissolve
    ce "...and all these feelings about her job and her cover."
    scene ep6_stephend10 with dissolve
    ce "Knowing that one simple mistake, and she would probably have to leave town again."
    scene ep6_stephend11 with dissolve
    ce "But the moment you took her hand..."
    scene ep6_stephend13 with dissolve
    ce "...it didn't matter any more."
    scene ep6_stephend14 with dissolve
    ce "She was going to make it a night to remember."
    scene ep6_stephend15 with dissolve
    ce "But end up ruining it instead."
    scene ep6_epilogue73 with dissolve
    ce "I guess what I'm trying to say is..."
    ce "Maybe there's always a reson for something to happen."
    ce "..."
    scene ep6_epilogue74 with dissolve
    ce "[name]?"
    scene ep6_epilogue75 with dissolve
    ce "Really?"
    ce "..."
    ce "Sweet dreams."
    jump ep6EndThoughts
else:
    ce "I know what you mean now. It doesn't have to be perfect."
    ce "No one is."
    scene ep6_evening51 with dissolve
    $ renpy.pause()
    scene ep6_cecel30 with fade
    $ renpy.pause(1)
    scene ep6_cecel28 with dissolve
    $ renpy.pause(1)
    scene ep6_cecel29 with dissolve
    $ renpy.pause(1)
    scene ep6_cecel31 with fade
    $ renpy.pause(1)
    scene ep6_cecel32 with dissolve
    $ renpy.pause(1)
    scene ep6_cecel33 with dissolve
    $ renpy.pause(1)
    scene ep6_cece02 with fade
    ce "[name]."
    scene ep6_cece01 with dissolve
    ce "Look into my eyes."
    scene ep6_cece02
    $ renpy.movie_cutscene("imov/ep6/ep6_cece01wall_b.webm", delay=None, loops=0, stop_music=False)
    ce "You are so..."
    scene ep6_cece03
    $ renpy.movie_cutscene("imov/ep6/ep6_cece01wall.webm", delay=None, loops=0, stop_music=False)
    ce "...beautiful."
    scene ep6_cece04
    $ renpy.movie_cutscene("imov/ep6/ep6_cece02wall.webm", delay=None, loops=0, stop_music=False)
    $ renpy.pause()
    scene ep6_cecel03 with dissolve
    ce "Can we get down on the bed."
    ce "I need to see you."
    scene ep6_cecel04 with dissolve
    ce "That, and I'm afraid I'll cum to fast."
    scene ep6_cece05 with fade
    $ renpy.pause(0.1)
    scene ep6_cece01ride with dissolve
    ce "Much better."
    ce "Now I can see you."
    scene ep6_cece06
    $ renpy.movie_cutscene("imov/ep6/ep6_cece02ride.webm", delay=None, loops=0, stop_music=False)
    $ renpy.pause(0.05)
    scene ep6_cece02ride with dissolve
    ce "And tease you a little bit."
    me "It feels amazing."
    scene ep6_cece05
    $ renpy.movie_cutscene("imov/ep6/ep6_cece04ride.webm", delay=None, loops=0, stop_music=False)
    $ renpy.pause(0.05)
    scene ep6_cece01ride with dissolve
    ce "I thought you would have thrust forward by now."
    me "It did cross my mind..."
    scene ep6_cecel06 with dissolve
    ce "Seem's I have to..."
    scene ep6_cecel07 with dissolve
    ce "...do it for you."
    scene ep6_cece01ontop with dissolve
    $ renpy.pause()
    ce "[name]..."
    scene ep6_cecel08 with dissolve
    ce "I'm getting close again..."
    scene ep6_cecel09 with fade
    ce "You're so... happy now."
    scene ep6_cecel10 with dissolve
    me "And you're just as gorgeous as ever."
    me "Perhaps a little more tonight."
    me "But this time I'm the one getting close."
    scene ep6_cecel11 with dissolve
    ce "Tell you what..."
    scene ep6_cecel12 with dissolve
    ce "...race you to the finish?"
    scene ep6_cecel13 with dissolve
    ce "Oh, holy sweet mother of..."
    scene ep6_cecel15 with dissolve
    ce "...Go... GO!"
    scene ep6_cece01fin with dissolve
    $ renpy.pause()
    me "I'm..."
    scene ep6_cecel14 with hpunch
    ce "..."
    scene ep6_cecel16 with dissolve
    ce "I'm not complaining, but..."
    scene ep6_cecel17 with dissolve
    ce "Been saving up long?"
    me "*pants* Exhausted..."
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep6_cecel18 with fade
    ce "I understand now."
    ce "Everything doesn't have to be perfect, for it to seem perfect."
    scene ep6_cecel19 with dissolve
    me "It's what you remember."
    scene ep6_cecel18 with dissolve
    ce "Exactly."
    scene ep6_cecel19 with dissolve
    me "Still, I'd say it was as close to perfect as it could be."
    me "You're amazing, Cece."
    scene ep6_cecel20 with dissolve
    me "Never forget that."
    scene ep6_cecel21 with dissolve
    ce "Perceptions."
    ce "Broken isn't perfect."
    scene ep6_cecel19 with dissolve
    me "Beauty is in the eye of the beholder."
    me "You might not think you are."
    scene ep6_cecel22 with dissolve
    me "But you are to me and many others in the world."
    scene ep6_cecel23 with dissolve
    ce "You know, I was never interested in sex at all."
    ce "I mean, you see dicks and pussies all over the internet."
    ce "But it didn't appeal to me."
    ce "When I felt you in the pool that night at Lexi's place."
    ce "You tore down a wall."
    scene ep6_cece01stroke with dissolve
    ce "Now, when I touch you. Feel you getting harder. See your reaction."
    scene ep6_cece11stroke with dissolve
    ce "..."
    scene ep6_cece12stroke100
    $ renpy.movie_cutscene("imov/ep6/ep6_cece12stroke.webm", delay=None, loops=0, stop_music=False)
    ce "All sorts of things happen inside my body."
    scene ep6_cece13stroke100
    $ renpy.movie_cutscene("imov/ep6/ep6_cece13stroke.webm", delay=None, loops=0, stop_music=False)
    ce "I want to please you."
    ce "Let me please you."
    scene ep6_cece01bj with dissolve
    me "Cece..."
    me "That's beyond amazing."
    ce "*muffled sounds*"
    me "No, like really really amazing."
    ce "*muffled sounds*"
    me "No, really, really good. Like..."
    scene ep6_cecel24 with hpunch
    $ renpy.pause(0.6)
    scene ep6_cecel24 with hpunch
    $ renpy.pause(0.6)
    scene bg empty with fade
    $ renpy.pause(0.1)
    stop music fadeout 6
    scene ep6_cecel25 with fade
    ce "Ok, so maybe a little warning would have been nice."
    scene ep6_cecel27 with dissolve
    me "..."
    scene ep6_cecel26 with dissolve
    ce "Glad you enjoyed it."
    scene ep6_cecel27 with dissolve
    me "..."
    jump ep6EndThoughts
label ep6EndThoughts:
scene bg empty with fade
$ clockis = [[todayIs],0,3,2,1]
stop music fadeout 10
$ renpy.pause(0.5)
$ renpy.pause(0.5)
me "And that was it... My perfect summer."
me "That summer when everything was going my way."
me "All the girls seemed to like me."
me "It was like I could pick and choose."
me "And everything else I did turned out to be a hole in one."
me "Even the goofy things."
if Impact_Steph:
    me "I reunited with the one I thought I lost."
    me "Got an old friend back."
else:
    me "I got an old friend back."
me "Spent the summer with a pop star."
me "It would be the summer I would always remember."
me "..."
me "But not because of any of those things."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene warning with fade
$ renpy.pause()
menu:
    "[M_06_017a]": # "I understand, and I want to see the scenes.":
        $ ep6AcceptedWarningScreen = True
        jump ep6finale
    "[M_06_017b]": # "I do not want to see the scenes at this time.":
        play music ep4_loftheme
        jump ch6end
label ep6finale:
$ clockis = [[todayIs],0,3,3,6]
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
if ep4NightChoose == 1:
    scene ep6_epilogue52 with fade
else:
    scene ep6_epilogue54b with fade
ce "I know you're sleeping, but I want to say something."
ce "This summer has been such a strange feeling."
ce "Ever since I met you for the first time, I saw you struggling."
ce "Maybe you didn't even know it yourself, but I saw."
ce "Then meeting everyone else. I saw their struggles."
if ep4NightChoose == 1:
    scene ep6_epilogue53 with dissolve
else:
    scene ep6_epilogue53b with dissolve
ce "..."
if ep4NightChoose == 1:
    scene ep6_epilogue52 with dissolve
else:
    scene ep6_epilogue54b with dissolve
play music ep6_finale
$ nowPlayingArtist = "Caleb Etheridge"
$ nowPlayingTitle = "The Way Forward"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
ce "{fast}But you're fine now...{w=2}{nw}"
ce "{fast}...you all are.{w=2}{nw}"
if ep4NightChoose == 1:
    scene ep6_epilogue53 with dissolve
else:
    scene ep6_epilogue53b with dissolve
$ renpy.pause(1)
if ep4NightChoose == 1:
    scene ep6_epilogue54 with dissolve
else:
    scene ep6_epilogue54b with dissolve
ce "{fast}And even if you almost had me convinced...{w=3}{nw}"
ce "{fast}...it's something I can never be...{w=3}{nw}"
if ep4NightChoose == 1:
    scene ep6_epilogue53 with dissolve
else:
    scene ep6_epilogue53b with dissolve
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue54 with dissolve
else:
    scene ep6_epilogue54b with dissolve
ce "{fast}...fine.{w=1}{nw}"
if ep4NightChoose == 1:
    scene ep6_epilogue54 with dissolve
else:
    scene ep6_epilogue54b with dissolve
$ renpy.pause(2)
if ep4NightChoose == 1:
    scene ep6_epilogue55 with dissolve
else:
    scene ep6_epilogue55b with dissolve
ce "{fast}*whispers* It's time for me to go now.{w=4}{nw}"
if ep4NightChoose == 1:
    scene ep6_epilogue56 with dissolve
else:
    scene ep6_epilogue56b with dissolve
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue55 with dissolve
else:
    scene ep6_epilogue55b with dissolve
ce "{fast}Please forgive me.{w=3}{nw}"
if ep4NightChoose == 1:
    scene ep6_epilogue57 with dissolve
else:
    scene ep6_epilogue57b with dissolve
$ renpy.pause(1)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_epilogue58 with dissolve
$ renpy.pause(2.5)
scene ep6_epilogue59 with dissolve
$ renpy.pause(2)
scene ep6_epilogue60 with dissolve
$ renpy.pause(1)
scene ep6_epilogue61 with dissolve
$ renpy.pause(1)
if ep4NightChoose == 1:
    scene ep6_epilogue43 with dissolve
else:
    scene ep6_epilogue43b_b with dissolve
$ renpy.pause(0.1)
scene ep6_dream01t with Dissolve(2, alpha=True)
$ renpy.pause(2)
if ep4NightChoose == 1:
    scene ep6_headtoss1 with Dissolve(2, alpha=True)
else:
    scene ep6_headtoss1_b with Dissolve(2, alpha=True)
$ renpy.pause(1)
scene ep6_epilogue36 with dissolve
$ renpy.pause(2)
scene ep6_epilogue37 with dissolve
$ renpy.pause(1)
scene ep6_epilogue38 with Dissolve(2, alpha=True)
$ renpy.pause(1)
scene ep6_epilogue39 with dissolve
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue44 with dissolve
else:
    scene ep6_epilogue44b_b with dissolve
$ renpy.pause(0.1)
scene ep6_dream02t with Dissolve(2, alpha=True)
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_headtoss2 with Dissolve(2, alpha=True)
else:
    scene ep6_headtoss2_b with Dissolve(2, alpha=True)
$ renpy.pause(1)
scene ep6_epilogue63 with dissolve
$ renpy.pause(1.5)
scene ep6_epilogue64 with dissolve
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue45b with dissolve
else:
    scene ep6_epilogue45b_b with dissolve
$ renpy.pause(0.1)
scene ep6_dream03t with Dissolve(2, alpha=True)
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_headtoss3 with Dissolve(2, alpha=True)
else:
    scene ep6_headtoss3_b with Dissolve(2, alpha=True)
$ renpy.pause(1)
scene ep6_epilogue40 with dissolve
$ renpy.pause(1.5)
scene ep6_epilogue42 with dissolve
$ renpy.pause(1.5)
scene ep6_epilogue41 with dissolve
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue46 with dissolve
else:
    scene ep6_epilogue46b_b with dissolve
$ renpy.pause(0.1)
scene ep6_dream04t with Dissolve(2, alpha=True)
$ renpy.pause(1.5)
if ep4NightChoose == 1:
    scene ep6_epilogue46 with Dissolve(0.5, alpha=True)
    $ renpy.pause(0.1)
    scene ep6_epilogue47 with Dissolve(0.5, alpha=True)
    $ renpy.pause(2)
    scene ep6_epilogue47b with Dissolve(0.5, alpha=True)
else:
    scene ep6_epilogue46b_b with Dissolve(0.5, alpha=True)
    $ renpy.pause(0.1)
    scene ep6_epilogue47b_b with Dissolve(0.5, alpha=True)
    $ renpy.pause(2)
    scene ep6_epilogue47b_bb with Dissolve(0.5, alpha=True)
$ renpy.pause(1)
scene ep6_epilogue48 with fade
me "{fast}Cece?{w=3}{nw}"
scene ep6_epilogue49 with dissolve
$ renpy.pause(2.5)
scene ep6_epilogue51 with Dissolve(2, alpha=True)
$ renpy.pause(2.5)
if ep4SetupChrisWith == 4:
    scene ep6_epilogue18 with fade
else:
    scene ep6_epilogue19 with fade
ch "{fast}It's the middle of the night...{w=2}{nw}"
scene ep6_epilogue50 with Dissolve(1, alpha=True)
me "{fast}Vincent Bridge... NOW!{w=2}{nw}"
if ep4SetupChrisWith == 4:
    scene ep6_epilogue20 with dissolve
else:
    scene ep6_epilogue21 with dissolve
$ renpy.pause(0.5)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_epilogue00
$ renpy.movie_cutscene("imov/ep6/ep6_bridge01jump.webm", delay=None, loops=0, stop_music=False)
stop music fadeout 3
scene bg empty with Dissolve(3, alpha=True)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
me "(Things changes fast.)"
me "(One moment everything is perfect...)"
play music ep6_cece
$ nowPlayingArtist = "Ben Winwood"
$ nowPlayingTitle = "Ireland"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "(The next, it's all chaos...)"
me "(But we've been here before.)"
me "(We can do it again.)"
me "..."
me "(Right?...)"
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep6_bridge02 with fade
ce "No..."
ce "NO! You motherf..."
me "Got ya!"
scene ep6_bridge03 with dissolve
ce "[name]?"
ce "How."
scene ep6_bridge04 with dissolve
me "Cece, look at me. We can do this. Just hold on to my hand."
ce "..."
scene ep6_bridge03 with dissolve
ce "I can't..."
scene ep6_bridge01 with dissolve
ce "I don't have the strength to go on any more."
scene ep6_bridge05 with dissolve
me "Don't think about that right now, just grab a hold. We'll fix this."
scene ep6_bridge06 with dissolve
me "Come home. We'll just do whatever you want."
scene ep6_bridge07 with dissolve
me "We don't even need to go to the hospital, I know you hate that."
scene ep6_bridge08 with dissolve
ce "I'm just so tired. So very tired."
scene ep6_bridge09 with dissolve
me "Then we'll sleep. I'll hold you. Make you safe."
me "You can stay in bed for as long as you want. However many more minutes you want."
scene ep6_bridge18 with dissolve
me "I told you last time, there's nothing for you down there."
scene ep6_bridge10 with dissolve
me "Just hold on to my hand and we'll fix this."
scene ep6_bridge11 with dissolve
me "Please, Cece. I don't know how much longer I can hold on."
scene ep6_bridge12 with dissolve
ce "I can't."
ce "If you just knew the pain..."
ce "...every single day..."
ce "...you wouldn't have asked me."
if ep4NightChoose == 1:
    scene ep6_bridge17 with dissolve
    me "I love you, Cece. Don't do this to me."
    me "Please, just hold on."
    scene ep6_bridge13 with dissolve
    ce "Love..."
    ce "I don't even know what that means."
    ce "I feel for you... deeply..."
    ce "...but the only thing Love does for me, is hurt me."
    scene ep6_bridge17 with dissolve
    me "That is how love works. It can be painful, but the rewards are wonderful."
else:
    scene ep6_bridge17 with dissolve
    me "I can help you. Fix you."
    scene ep6_bridge13 with dissolve
    ce "Some things can't be fixed."
    ce "They are just broken."
    scene ep6_bridge17 with dissolve
    me "But still beautiful. They still don't need to die."
    scene ep6_bridge13 with dissolve
    ce "There's an end for everything... everyone..."
scene ep6_bridge14 with dissolve
ce "Listen to me very carefully."
ce "You have to be strong. Live your life like you want to live it."
ce "I'll always be with you in spirit."
scene ep6_bridge17 with dissolve
me "I can't do that."
scene ep6_bridge14 with dissolve
ce "[name]..."
scene ep6_bridge15 with dissolve
stop music fadeout 6
ce "It's ok..."
ce "You can let go now..."
scene ep6_bridge16 with dissolve
me "CECE, NO, PLEASE..."
scene ep6_bridge15 with dissolve
ce "Be strong..."
play music ep6_epilogue
$ nowPlayingArtist = "Narrow Skies"
$ nowPlayingTitle = "Auld Lang Syne"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep6_bridge01fall with dissolve
me "NOOO!{w=6}{nw}"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.movie_cutscene("imov/ep6/ep6_hmnobeat.webm", delay=None, loops=0, stop_music=False)
$ renpy.pause(0.5)
$ renpy.pause(0.5)

scene ep6_epiloguesiren02 with fade
$ renpy.pause(2.2)


scene ep6_epiloguesiren01 with dissolve
$ renpy.pause(1.1)


scene ep6_epiloguesiren03 with dissolve
$ renpy.pause(1.1)


scene ep6_epiloguesiren04 with dissolve
$ renpy.pause(2.2)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
hide ep6_epiloguesiren04

scene ep6_epilogue10 with fade
"{i}Suicide...{/i}"
scene ep6_epilogue13 with dissolve
"{i}...always comes out of nowhere.{/i}"
scene ep6_epilogue12 with dissolve
"{i}Lurking.{/i}"
scene ep6_epilogue11 with Fade(0, 0, 1.5, color="#ffffff")
"{i}Then striking when you least expect it.{/i}"
show ep6_epilogue05c at imgSlide_ep6KiraSorrow_c
show ep6_epilogue05b at imgSlide_ep6KiraSorrow_b
show ep6_epilogue05a at imgSlide_ep6KiraSorrow_a
$ renpy.pause(5)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
hide ep6_epilogue05a
hide ep6_epilogue05b
hide ep6_epilogue05c
$ renpy.movie_cutscene("imov/ep6/ep6_hmnobeat.webm", delay=None, loops=0, stop_music=False)

scene ep6_epilogue06 with fade
"{i}It doesn't differenciate.{/i}"
scene ep6_epilogue07 with dissolve
"{i}By how famous you are.{/i}"
scene ep6_epilogue08 with dissolve
"{i}Or how much money you have.{/i}"
show ep6_epilogue09 at imgSlide_ep6LexiSorrow_a
show ep6_phonefall at imgSlide_ep6LexiSorrow_b
$ renpy.pause(5)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
hide ep6_phonefall
hide ep6_epilogue09
if ep4SetupChrisWith == 4:

    scene ep6_epilogue16 with fade
    "{i}It doesn't matter if you were close to the person or not.{/i}"
    scene ep6_epilogue17 with Fade(0, 0, 1.5, color="#ffffff")
    "{i}You will be affected.{/i}"
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    scene ep6_epilogue69 with fade
    "{i}Hearing about someone you've spent time with, passing.{/i}"
    scene ep6_epilogue70 with Fade(0, 0, 1.5, color="#ffffff")
    "{i}Will impact you either way.{/i}"
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
else:

    scene ep6_epilogue14 with fade
    "{i}It doesn't matter if you were close to the person or not.{/i}"
    scene ep6_epilogue15 with Fade(0, 0, 1.5, color="#ffffff")
    "{i}You will be affected.{/i}"
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
$ renpy.movie_cutscene("imov/ep6/ep6_hmnobeat.webm", delay=None, loops=0, stop_music=False)
if ep4NightChoose <> 6:

    scene ep6_epilogue22 with fade
    "{i}Some think those left behind are on the loosing end.{/i}"
    scene ep6_epilogue23 with dissolve
    "{i}They get to experience the loss.{/i}"
    scene ep6_epilogue24 with dissolve
    "{i}But those who end their life...{/i}"
    scene ep6_epilogue25 with dissolve
    "{i}...loose everything.{/i}"
    scene ep6_epilogue26 with dissolve
    "{i}But one thing is for certain...{/i}"
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
else:

    scene ep6_epilogue27 with fade
    "{i}Hearing about someone you've spent time with, passing.{/i}"
    scene ep6_epilogue28 with dissolve
    "{i}Will impact you either way.{/i}"
    scene ep6_epilogue29 with dissolve
    "{i}And you deal with it the only way you know how.{/i}"
    show ep6_epilogue30 at imgSlide_ep6StephSorrow_a
    $ renpy.pause(5)
    scene bg empty with fade
    $ renpy.pause(0.5)
    $ renpy.pause(0.5)
    hide ep6_epilogue30

    scene ep6_epilogue32 with fade
    scene ep6_epilogue35 with dissolve
    "{i}Some think those left behind are on the loosing end.{/i}"
    scene ep6_epilogue33 with dissolve
    "{i}They get to experience the loss.{/i}"
    scene ep6_epilogue34 with dissolve
    "{i}But those who end their life... loose everything.{/i}"
    scene ep6_epilogue31b with dissolve
    "{i}But one thing is for certain...{/i}"
scene ep6_epilogue31 with fade
"{i}There are no winners.{/i}"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
centered "{=midscreentxt}I still hear you, telling me those words.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}'You should write a story.'{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}And the laughter that followed...{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}...the kind of laughter it's impossible to not be affected by.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}So I join in, laughing.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}Then you move to the hallway to proceed with the daily rituals before leaving.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}It doesn't matter that the shoes are half a size too small. They are the right brand.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}You stand in front of the mirror and give your hair a light ruffle before giving your reflection an approving nod.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}Pre 'going out with friends' rituals are done, and you stand in the doorway... waiting.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}I know what you want. You never leave without it.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}We hug.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}It's a good hug.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}You look at me and say your final words. Your laughter is real. Your smile genuine.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}Then you leave. Walking like you're on a pink cloud. Humming your favorite song.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}You're looking better than you have in a long time.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}Just another teenager on her way to meet friends and have a good time.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}I didn't know it would be the last time I would see you alive.{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}But I'll never forget your last words...{/=midscreentxt}"
scene bg empty with dissolve
centered "{=midscreentxt}'No really, dad... {w=1.5}you should write a story.'{/=midscreentxt}"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
"{i}Life sucks sometimes...{/i}"
scene ep6_epilogue99 with fade
$ renpy.pause(0.5)
scene bg empty with Dissolve(5, alpha=True)
$ renpy.pause(0.5)
$ renpy.pause(0.5)






"{i}...but this is just a game.{/i}"
$ renpy.movie_cutscene("imov/ep6/ep6_hmbeat.webm", delay=None, loops=0, stop_music=False)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
"{i}To be continued...{/i}"

queue music [ep4_loftheme]
scene bg empty with Dissolve(1, alpha=True)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
jump ch6end

$ renpy.pause()
$ renpy.pause()
$ renpy.pause()
$ renpy.pause()
$ renpy.pause()

label ch6end:
scene bg empty with Dissolve(2.5, alpha=True)
call credits6 from _call_credits6
show screen ep6_endscreen with Dissolve(2.5, alpha=True)
$ renpy.pause(0.5)
$ renpy.pause()
stop music fadeout 3
scene bg empty with fade
$ renpy.pause(2)
$ renpy.pause(2)

label ch3Start:
if persistent.chapter3 is None:
    $ persistent.chapter3 = True

$ todayIs = 5
$ phone_camop_screen = ""
stop music fadeout 5
scene bg empty
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep3_prologue
$ nowPlayingArtist = "Joy Hanna"
$ nowPlayingTitle = "Goodnight"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "(Dreams are weird...)"
me "(Wait...)"
me "(That was another time and place.)"
me "(But sometimes things are so good, you feel like you are dreaming.)"
me "(And you never want them to stop.)"
scene ep3_prologue01 with Dissolve(5, alpha=True)
$ renpy.pause(5)
scene bg empty with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep3_prologue01 with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene bg empty with Dissolve(0.1, alpha=True)
$ renpy.pause(0.1)
scene ep3_prologue_blink with Dissolve(1, alpha=True)
me "..."
$ ep3ProlCheckedPhone = False
show screen phone_sml
scene ep3_prologue02 with dissolve
play sound ep3_water
st "I think you fell alseep."
scene ep3_prologue_blink with dissolve
me "Was hard not to."
me "It's not like we got a whole lot of sleep last night."
scene ep3_prologue03 with dissolve
st "I didn't hear a lot of complaints."
scene ep3_prologue_blink with dissolve
me "I have nothing to complain about."
me "Not then, not now."
scene ep3_prologue03 with dissolve
st "I love watching you sleep."
scene ep3_prologue_blink with dissolve
me "That's kinda creepy, just saying."
scene ep3_prologue02 with dissolve
st "Are you calling me a creep now?"
scene ep3_prologue04 with dissolve
me "Definitely. Weird fluffy murderous toy-doll."
scene ep3_prologue03 with dissolve
st "Sure..."
st "...I'll be your fluffy toy-doll..."
st "...with bunny ears."
scene ep3_prologue_blink with dissolve
me "..."
scene ep3_prologue03 with dissolve
st "What..."
scene ep3_prologue04 with dissolve
me "I love you, Steph. You are the best thing that's ever happened to me."
scene ep3_prologue05 with dissolve
st "And I ... adore you."
me "Not a big fan of the L-word are you?"
scene ep3_prologue06 with dissolve
st "It's not just a word ... it's..."
st "...when it's said, it seals the deal."
me "I thought I had you in the bag already."
st "You do."
scene ep3_prologue07 with dissolve
st "...so you want me to seal the deal, eh?"
st "I'll seal the deal..."
scene ep3_prologue08b with dissolve
st "*makes stuttering sound* I luh, luh, luh, luh, luh..."
st "...like you!"
scene ep3_prologue10b with dissolve
me "Just horrible..."
me "1 of 10."
scene ep3_prologue09b with dissolve
st "Be careful of what you're saying mr."
st "I got all the control in the world up here."
scene ep3_prologue10b with dissolve
me "Not unless I use my super secret special forces counter attack."
scene ep3_prologue09b with dissolve
st "Nothing can get me off my throne. I'd like to see you..."
scene ep3_prologue11b with dissolve
st "...tryyyyyyyyyeeehhhhhhh."
scene ep3_prologue12b with dissolve
me "Mhhhmfmmhs?"
st "Oh my god, are you..."
scene ep3_prologue15b with dissolve
st "...ok?"
scene ep3_prologue14b with dissolve
me "It seemed like a good idea at the time."
scene ep3_prologue13b with dissolve
st "..."
scene ep3_prologue15b with dissolve
st "You know... I really, really, really..."
scene ep3_prologue16b with dissolve
$ renpy.pause(3)
scene ep3_prologue15b with dissolve
st "...like you."
scene ep3_prologue14b with dissolve
me "And I love the way you smell. You always smell amazing."
scene ep3_prologue15b with dissolve
st "That reminds me... I need a bath."
scene ep3_prologue17 with dissolve
st "Last one in..."
hide screen phone_sml
if ep3ProlCheckedPhone:
    scene ep3_prologue19 with dissolve
    me "That's not even close..."
    scene ep3_prologue19b with dissolve
    me "...to being fair!"
else:
    scene ep3_prologue19 with dissolve
    me "That's not even close to being fair!"
scene ep3_prologue18 with dissolve
st "Lo-hooooo-se-heeerr."
scene ep3_prologue20 with dissolve
if ep3ProlCheckedPhone:
    me "..."
else:
    show screen phone_smlwet
    me "..."
scene ep3_prologue44 with dissolve
st "Did you come to claim your prize?"
scene ep3_prologue23 with dissolve
me "I thought I lost?"
scene ep3_prologue44 with dissolve
st "You won me."
scene ep3_prologue22 with dissolve
st "Provided you catch me!"
scene ep3_prologue24 with dissolve
me "What is it with you and unfair starts."
scene ep3_prologue25 with dissolve
st "How's the view, back there?"
scene ep3_prologue26 with dissolve
me "Hold on, let me check..."
scene ep3_prologue27 with dissolve
st "What are you...?"
show ep3_prologue28big_a at imgSlide_prologue_steph
show ep3_prologue28big_e at imgSlide_prologue_steph_bubble1
show ep3_prologue28big_d at imgSlide_prologue_steph_bubble2
$ renpy.pause(10)
scene ep3_prologue46 with dissolve
hide ep3_prologue28big_a
hide ep3_prologue28big_e
hide ep3_prologue28big_d
st "Uaaahhh..."
scene ep3_prologue29 with dissolve
st "*sings* I believe I can fly..."
scene ep3_prologue30 with dissolve
me "...I believe I can..."
scene ep3_prologue31 with dissolve
stop sound fadeout 3
me "*bubble noises*"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
show ep3_prologue35 at imgSlide_prologue_top
hide screen phone_smlwet
show screen phone_smlblanked
me "I can't believe it's the last day of school tomorrow."
me "And here I am with you, feeling I've got the best start in life I can get."
st "..."
st "...I have to tell you something..."
st "...but I'm terrified of what will happen when I do..."
me "..."
me "Your name used to be Todd, and you had gender change?"
scene ep3_prologue40b with dissolve
hide ep3_prologue35
st "Right there... That's why."
me "Hmm?"
st "That's just one of the many reasons why you're the most amazing man in the world."
st "...your exceptional way of being just... so ... breathtaking ... it's just one of the thousands of reasons why I love y..."
scene ep3_prologue41b with dissolve
st "..."
me "Now that wasn't so bad, was it?"
scene ep3_prologue42b with dissolve
me "And I don't care if you use those exact words. I can feel your love, Steph."
me "Every day."
me "And I can see that something is eating at you."
me "Whatever it is, I hope you can share it some day."
me "Whenever you feel you can, or are ready for it, I'm right here."
scene ep3_prologue43b with dissolve
me "..."
me "And it seems like you just sealed the deal.."
me "...and made me feel like the happiest man alive."
scene ep3_prologue36b with dissolve
st "I love you so much it hurts..."
scene ep3_prologue37b with dissolve
me "Hold on now. That's two times you've said it this month. Calm down already."
scene ep3_prologue38b with dissolve
st "Shut up."
scene ep3_prologue39b with dissolve
$ renpy.pause()
scene ep3_prologue35 with dissolve
st "You always know what to say, don't you."
scene ep3_prologue32b with dissolve
me "Most of the times, I know it all of the times."
scene ep3_prologue33b with dissolve
me "...or you might say that you're an excellent source of inspiration."
scene ep3_prologue45b with dissolve
st "..."
hide screen phone_smlblanked
scene ep3_prologue34b with dissolve
$ renpy.pause()
scene ep3_prologue_titleb with Dissolve(5, alpha=True)
$ renpy.pause()
stop music fadeout 5
scene ep3_prologue_title2 with Dissolve(5, alpha=True)
$ renpy.pause()
play music ep3_homeinter
$ nowPlayingArtist = "Brick Fields"
$ nowPlayingTitle = "This Time Coming Soon"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_homeinter01 with fade
$ clockis = [[todayIs],0,7,3,1]
$ ep3MusicDownload = True
$ phone_task_append_item0 = "7;4;2;1;0;0;Lexi;Find a way to contact Lexi before;Contact Lexi.;1"
$ phone_task_append_item1 = "7;4;2;3;5;9;Lexi;Find a way to contact Lexi before;Contact Lexi.;1"
$ phone_task_append_item3 = "7;5;2;1;0;0;Lexi;Find a way to contact Lexi;Contact Lexi.;1"
$ phone_task_append_item4 = "7;5;2;3;5;9;Lexi;Find a way to contact Lexi;Contact Lexi.;1"
$ phone_task_append_item2 = "7;4;2;3;5;9;Lexi;Find a way to contact Lexi;Contact Lexi.;0"
if phone_task_append_item0 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item0)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if phone_task_append_item1 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item1)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if phone_task_append_item3 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item3)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if phone_task_append_item4 in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.remove(phone_task_append_item4)
        $ phone_task_list.append(phone_task_append_item2)
        $ phTaskNotify = True
if not ep2LexiReply:
    $ contact_notify_me = True
    $ contact_text_me += "\n\nI didn't get Lexi's number! Hopefully Chris has got me covered."
    $ nukeCommentsAdd = "3;309;AssesAndBreasts;I sent you a PM @OfficialLexi. At least I hope I did."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
show screen phone
me "(...ok. I'm giving up.)"
scene ep3_homeinter02 with dissolve

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "Go to {b}Music{/b} on your phone and download Lexi's music.\nSet your {b}ringtone{/b} to a Lexi song"
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################

me "(Today I'm going to buy a new couch no matter what.)"
me "(...)"
scene ep3_homeinter01 with dissolve
me "(I'm so happy for Cece. I can't help but feel that yesterday was a big step forward for her.)"
me "(She seemed to finally let her guard down for a bit.)"
me "(Somehow I think the problem is connected to her dealing with emotions.)"

if MenuChoice != "HintsNone":
    ### Hide Hint ########################################################################################################################################
    hide screen general_notifytop with dissolve
    ### Hide Hint ########################################################################################################################################

scene ep3_homeinter02 with dissolve
me "(But that kiss...)"
me "(...it would have been rude to reject her...)"
me "(...because she wanted it, right?)"
me "(Or did I?)"
scene ep3_homeinter01 with dissolve
me "(Then there's what Linda did. In the dressing room.)"
if not ep2RejectedRobin:
    me "(And me and Robin the other day.)"
    me "(But that was all friends with benefit based.)"
    me "(She said so herself...)"
if ep2KiraReply:
    me "(And Kira...)"
    me "(But she was acting all weird yesterday.)"
else:
    me "(And Kira...)"
    me "(But I forgot to text her back.)"
me "(...)"
scene ep3_homeinter02 with dissolve
me "(...I'm confused.)"
me "(Well, no use laying here soaking up back pain.)"
scene ep3_homeinter03 with dissolve
me "(...are they still sleeping?)"
scene ep3_homeinter04 with dissolve
me "(Yup...)"
me "(Hehe... Cece, has stolen the covers.)"
me "(I have to say, that's quite a rear end you've got there, Linda.)"
scene ep3_homeinter05 with dissolve
me "(Oh...)"
me "(No bra...)"
me "(Maybe I should go in for a better view.)"
me "(Christ, what am I even thinking.)"
show ep3_homeinter06 with dissolve
me "(That's not why I invited them to stay at my place.)"
me "(...)"
me "(What should I do? It's too early to go outside.)"
scene ep3_homeinter07 with dissolve
me "(Hmm.)"
scene ep3_homeinter08 with dissolve
$ clockis = [[todayIs],0,7,3,9]
li "(...)"
scene ep3_homeinter09 with Dissolve(0.2, alpha=True)
$ renpy.pause(0.1)
scene ep3_homeinter10 with Dissolve(0.2, alpha=True)
$ renpy.pause(0.1)
scene ep3_homeinter11 with Dissolve(0.2, alpha=True)
li "(Huh...)"
scene ep3_homeinter10 with Dissolve(0.2, alpha=True)
li "(Oh, that's right. I'm at [name]'s place.)"
li "(Feels good waking up in a proper bed.)"
li "(...)"
li "(Wait... is he...)"
scene ep3_homeinter12 with dissolve
li "(Watching me?)"
scene ep3_homeinter13 with dissolve
li "(...)"
scene ep3_homeinter06 with dissolve
li "(No...)"
scene ep3_homeinter12 with dissolve
li "(...but he's right there.)"
li "(...why am I getting horny...)"
scene ep3_homeinter14 with dissolve
li "(I always had an exhibitionistic side I guess...)"
li "(...so very horny.)"
li "(I guess it wouldn't hurt to...)"
scene ep3_homeinter24 with dissolve
me "(...check out that news article Chris told me about. With that picture of me and Lexi.)"
me "(It's probably my 15 minutes of fame moment.)"
scene ep3_homeinter24b with dissolve
if ep2LexiReply:
    me "(I can't wait to talk to her though. I hope she hasn't forgot about calling me.)"
    scene ep3_homeinter24 with dissolve
    me "(What should I say though?"
else:
    me "(It would have been nice to talk to her again under different circumstances.)"
    scene ep3_homeinter24 with dissolve
    me "(I have no idea what we could talk about though, coming from two completely different worlds.)"
me "(I guess...)"
scene ep3_homeinter39 with dissolve
li "(...it wouldn't hurt to play around for a bit.)"
scene ep3_homeinter15 with dissolve
$ renpy.pause(1)
scene ep3_homeinter16 with dissolve
li "(If he catches me...)"
li "(...I can live with that.)"
scene ep3_homeinter17 with dissolve
li "(Because I absolutely need to touch myself, right now!)"
li "(Oh. My. God. Even the smallest touch sends shivers down my spine..."
scene ep3_homeinter38 with dissolve
li "(...from my toes to the...)"
scene ep3_homeinter17 with dissolve
li "(...top of my head.)"
scene ep3_homeinter20 with dissolve
li "(This is amazing. I'm lost... There's no way I can stop this.)"
scene ep3_homeinter34 with dissolve
li "(Even Cece is in the very same bed as me.)"
scene ep3_homeinter20 with dissolve
li "(But she's a heavy sleeper.)"
li "(Mmmmm. [name]. I want you to...)"
scene ep3_homeinter23 with dissolve
me "(...sit down and play a game or two.)"
scene ep3_homeinter23b with dissolve
me "(It's not like there's anything exciting going on right now.)"
scene ep3_homeinter23 with dissolve
$ clockis = [[todayIs],0,7,4,2]
me "(I know. Candie Squash Saga. Got to collect my daily bonus.)"
scene ep3_homeinter21 with dissolve
me "(Watching ads, watching ads. Such fun.)"
me "(And why do I get the same ad over and over.)"
me "(I wish...)"
scene ep3_homeinter22 with dissolve
li "(...you would just drop those pants right now and ram your glorious...)"
scene ep3_homeinter21 with dissolve
me "(...daily dose of diamonds. Finally. I can buy that booster.)"
me "(Take that SquashMaster4739. You are going down. I'm going to...)"
scene ep3_homeinter36 with dissolve
li "(...fuck me so hard.)"
li "(Pull my hair, and keep slamming that...)"
scene ep3_homeinter25 with dissolve
me "(...pussy! You god damn pussy, SquashMaster4739. I know you're not accepting my challenge because you know I've got boosters.)"
me "(Trashtalk incoming...)"
scene ep3_homeinter26 with dissolve
me "('If you don't accept my challenge, I'm going to take your own phone and ram it so far down'...)"
scene ep3_homeinter32 with dissolve
li "(...my throat that I can't even breathe.)"
li "(Oh my...)"
li "(I can almost feel him going down.)"
scene ep3_homeinter20 with dissolve
li "(I have to stop...)"
li "(I'm going to explode, and there's no way I can hold back anything.)"
scene ep3_homeinter26 with dissolve
li "(...)"
scene ep3_lindajoy with dissolve
li "(Fuck no. I'm not stopping. This orgasm deserves to live.)"
li "(Mmmmmmmhh.... This is just...)"
scene ep3_homeinter25 with dissolve
me "(...retarded.)"
me "(Ah, fuck it. This game is no good for my nerves.)"
me "(I just...)"
scene ep3_homeinter29 with dissolve
li "(...can't hold back anymore...)"
li "(Here we go...)"
scene ep3_homeinter32 with dissolve
li "(...oh god... help ... me ...)"
scene ep3_homeinter32 with hpunch
$ renpy.pause(1)
scene ep3_homeinter35 with hpunch
$ renpy.pause(1)
scene ep3_homeinter29 with hpunch
$ renpy.pause(1)
scene ep3_homeinter27 with hpunch
me "(Huh?...)"
me "(Earthquake?...)"
scene ep3_homeinter28 with dissolve
me "(...or thunderstorm?)"
me "(...)"
scene ep3_homeinter31 with dissolve
me "(Nah... I'm imagining things.)"
scene ep3_homeinter29 with dissolve
li "*snorts*"
scene ep3_homeinter31 with dissolve
me "(Haha. I heard you Linda. You're snoring.)"
scene ep3_homeinter29 with dissolve
li "*pants* ( I ... have ... no idea ...)"
scene ep3_homeinter30 with dissolve
$ clockis = [[todayIs],0,7,5,4]
li "(...how I ... managed to keep ... that one in.)"
scene ep3_homeinter33 with dissolve
$ phone_task_append_item1 = "7;8;2;3;5;9;SquashMaster4739;Beat SquashMaster4739, one way or another before;Beat SquashMaster4739.;1"
$ phone_task_append_item2 = "7;8;2;3;5;9;SquashMaster4739;Beat SquashMaster4739, one way or another before;Beat SquashMaster4739.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_taskadd = "New task\nBeat SquashMaster4739, one way or another."
show screen phone_taskadded
me "(I'm heading out, and I'm going to find the hardest bench in the world just to prove it's better than my couch.)"
scene ep3_homeinter37 with dissolve
hide screen phone_taskadded
stop music fadeout 5
me "(So the girls can have some relaxing alone time.)"
me "(I guess they...)"
scene ep3_homeinter09 with dissolve
li "(...need to sleep a bit more...)"
scene ep3_homeinter08 with dissolve
li "(...)"
play music ep3_outside
$ nowPlayingArtist = "Michael Shynes"
$ nowPlayingTitle = "Rundown Streetlights"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],0,9,4,4]
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_outside01 with fade
$ nukeStoriesAdd = "12;Kira;ep3_nuke_kirastreet;New dress."
if nukeStoriesAdd not in nukeStories:
    $ nukeStories.append(nukeStoriesAdd)
$ nukeCommentsAdd = "12;1201;Robin4739;You look smashing as always, darling."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "12;1202;Janice;Aw, you're so sweet."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "12;1203;AshleyAmazing;Need to talk to you sis. Call me."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
ki "You're being silly, Kira..."
ki "You can't fall head over heels after spending one evening with a guy."
scene ep3_outside02 with dissolve
ki "That's not how you are."
ki "..."
ki "...and why are you talking to yourself in third person."
scene ep3_outside03 with dissolve
ki "(But there was some chemistry there, right?)"
if ep1KiraWalkHome:
    if ep1RejectedKira:
        ki "(He didn't want to do the horizontal boogie. But he said it was because he respected me...)"
        ki "(*sigh* ... so romantic...)"
        ki "(Oh, stop it Kira. You don't even have a romantic side.)"
        ki "(...)"
        ki "(*sigh*)"
    else:
        ki "(I should have fucked him. He seemed eager.)"
        ki "(Lord knows I was...)"
        ki "(*sigh* ... why didn't I...)"
        ki "(Oh, stop it Kira. You're going to get turned on by continuing.)"
else:
    ki "(I had so much fun at the bowling.)"
    ki "(And truth be told, I've not been able to get him out of my head ever since.)"
    ki "(I should have just invited him back home.)"
scene ep3_outside04 with dissolve
ki "(It was supposed to be fun. Bringing in a guy to spice things up...)"
ki "(...but Robin...)"
ki "(Does she like him like that too?)"
scene ep3_outside05 with dissolve
ki "(This is just getting messed up anyway.)"
ki "(I have to talk to her about it.)"
scene ep3_outside06 with dissolve
ki "(I'll just have to avoid [name] until then...)"
scene ep3_outside07 with dissolve
ki "..."
ki "(...aced that...)"
scene ep3_outside08 with dissolve
ki "(Leaving...)"
scene ep3_outside09 with dissolve
$ renpy.pause(5)
scene ep3_outside07 with dissolve
$ clockis = [[todayIs],0,9,5,7]
ki "(Or... I can just have a little look...)"
scene ep3_outside10 with dissolve
ki "(...I mean, talk...)"
ki "(...)"
scene ep3_outside11 with dissolve
ki "(No, I should leave before he wakes up.)"
scene ep3_outside12 with dissolve
ki "(Or...)"
scene ep3_outside13 with dissolve
ki "(Oh. My. God. Make up your mind already.)"
scene ep3_outside09 with dissolve
$ renpy.pause(0.1)
scene ep3_outside14 with Dissolve(3, alpha=True)
$ clockis = [[todayIs],1,0,1,9]
$ renpy.pause(1)
scene ep3_outside15 with dissolve
ki "(Why am I'm such a sucker for a handsome body...)"
scene ep3_outside16 with dissolve
ki "(...I mean, personality.)"
scene ep3_outside18 with dissolve
ki "..."
ki "Careful in the sun there, Tiger. You might get a sunburn."
scene ep3_outside19 with fade
me "(Huh?)"
me "(Is that Kira?)"
menu:
    "[M_03_001a]": # "Flex a bit and show off.":
        $ XPkira += 1
        $ meSporty += 1
        scene ep3_outside17 with dissolve
        show screen slvl with dissolve
        ki "..."
        scene ep3_outside20 with dissolve
        me "Oh, I didn't know anyone was here."
        hide screen slvl with dissolve
        jump ep3AfterFlexChoice
    "[M_03_001b]": # "Get up.":
        $ meRomantic += 1
        scene ep3_outside20 with dissolve
        show screen rlvl with dissolve
        me "Oh, hey Kira. What a wonderful surprise."
        hide screen rlvl with dissolve
        jump ep3AfterFlexChoice
label ep3AfterFlexChoice:
scene ep3_outside21 with dissolve
ki "Mind if I join you?"
scene ep3_outside20 with dissolve
me "Depends. Is that Frappy for me?"
scene ep3_outside21 with dissolve
ki "It might be. Or I might just walk away and drink it myself."
ki "If you don't move over that is."
scene ep3_outside22 with dissolve
me "You had me at 'It', or whatever your first word was."
scene ep3_outside23 with dissolve
ki "I'm sure you're just laying around here showing off anyway."
scene ep3_outside24 with dissolve
me "Well, did it work?"
scene ep3_outside25 with dissolve
ki "I think so. That sweet old lady that went past you was sending some lustful looks."
ki "If you're quick, you might catch up with her."
scene ep3_outside24 with dissolve
me "Oh, Mrs. Peterson in 47? No, we only get down and dirty on Tuesdays and Thursdays."
scene ep3_outside36 with dissolve
ki "*laughs* Oh... kay..."
if ep2KiraReply:
    scene ep3_outside37 with dissolve
    me "Yeah, but lay it on me..."
    scene ep3_outside27 with dissolve
    ki "What?"
    scene ep3_outside38 with dissolve
    me "You were kinda odd in the messages yesterday. So... pour..."
    scene ep3_outside40 with dissolve
    ki "Yeah, I was..."
    ki "Listen, I really enjoyed myself on our... date, or whatever we call it."
else:
    scene ep3_outside38 with dissolve
    me "Listen, I was going to reply to your text, but there's been so much going on..."
    scene ep3_outside40 with dissolve
    ki "Oh, never mind that..."
    ki "But I wanted to tell you that I really had a good time on our... date, or whatever we call it."
scene ep3_outside38 with dissolve
menu:
    "[M_03_002a]": # "Agree and hint you like her":
        $ ep3KiraOutsideLikeHer = True
        me "I did too. You are a wonderful woman, Kira."
        scene ep3_outside27 with dissolve
        ki "...and if I'm going to be completely honest, I really like you."
        scene ep3_outside26 with dissolve
        me "Thank you for thinking so. Really."
        me "And I really like you too."
        jump afterKiraLikeherOutside
    "[M_03_002b]": # "Agree but don't mention you might like someone else":
        me "I did too. And finally got to learn some bowling."
        jump afterKiraLikeherOutside
label afterKiraLikeherOutside:
scene ep3_outside28 with dissolve
$ clockis = [[todayIs],1,0,2,4]
ki "...anyway, so I heard Robin had a fucked up opening night at her bowling, and I went by her place..."
ki "And I saw you were there."
scene ep3_outside38 with dissolve
if not ep2RejectedRobin:
    me "(Oh...)"
me "Yeah, I went by the bowling alley to help her out, and got the full rundown."
me "So I decided to help her cheer up a bit, and we went to her place after."
me "We shared a bottle of Vodka, and played videogames."
ki "..."
scene bg empty with fade
$ renpy.pause(0.5)
scene ep3_outsideflashback00 with fade
ki "The way she was grinding you, looked like you were doing more than videogames."
scene ep3_outsideflashback01 with dissolve
$ renpy.pause(2)
scene ep3_outsideflashback02 with dissolve
$ renpy.pause(2)
scene ep3_outsideflashback03 with dissolve
$ renpy.pause(2)
scene ep3_outsideflashback04 with dissolve
$ renpy.pause(2)
scene ep3_outsideflashback05 with dissolve
$ renpy.pause(2)
scene bg empty with fade
$ renpy.pause(0.5)
$ ep3KiraSexTalk = 0
scene ep3_outside26 with fade
menu:
    "[M_03_003a]" if ep2RejectedRobin: # "Tell her nothing happened." if ep2RejectedRobin:
        $ ep3KiraSexTalk = 1
        $ XPkira += 12
        me "Ah... Now I get it."
        me "But long story short, you arrived at the worst possible time then."
        me "Things got a bit out of hand, and we kissed."
        me "But we both realized it was not a good idea."
        scene ep3_outside38 with dissolve
        ki "..."
        me "*laughs* If you don't believe me, I'm sure Robin can confirm."
        scene ep3_outside28 with dissolve
        ki "Wow... I'm such an idiot."
        jump ep3AfterKiraSexQuestion
    "[M_03_003b]" if ep2RejectedRobin: # "Ask her to get the story from Robin." if ep2RejectedRobin:
        $ ep3KiraSexTalk = 2
        $ XPkira += 12
        me "Ah... I see."
        me "Well, I take it you haven't talked to Robin about it yet."
        scene ep3_outside27 with dissolve
        ki "No."
        scene ep3_outside26 with dissolve
        me "You should."
        jump ep3AfterKiraSexQuestion
    "[M_03_003c]" if not ep2RejectedRobin and ep3KiraOutsideLikeHer: # "Tell her you had sex with Robin." if not ep2RejectedRobin and ep3KiraOutsideLikeHer:
        $ ep3KiraSexTalk = 3
        $ XPkira += 10
        me "Ok... I'm not going to lie about this."
        me "We did had a good time talking, drinking, and playing videogames."
        $ XPkira += 2
        me "Look, I feel awful. Because I really like you."
        me "But I can't lie about something I've done."
        me "What I'm trying to say is that eventually one thing led to another, and..."
        ki "..."
        me "...I don't normally do these friends with benefit. In fact I have never..."
        scene ep3_outside40 with dissolve
        ki "So you like her, right?"
        scene ep3_outside39 with dissolve
        me "..."
        me "I think we'd both say it was based on a spur of the moment 'let's have fun' kind of thing."
        me "I'm sorry."
        scene ep3_outside27 with dissolve
        ki "Don't be."
        jump ep3AfterKiraSexQuestion
    "[M_03_003d]" if not ep2RejectedRobin and not ep3KiraOutsideLikeHer: # "Tell her you had sex with Robin." if not ep2RejectedRobin and not ep3KiraOutsideLikeHer:
        $ ep3KiraSexTalk = 3
        $ XPkira += 10
        me "Ok... I'm not going to lie about this."
        me "We did had a good time talking, drinking, and playing videogames."
        me "Look, I can't lie about something I've done."
        me "What I'm trying to say is that eventually one thing led to another, and..."
        ki "..."
        me "...I don't normally do these friends with benefit things. In fact I have never..."
        scene ep3_outside40 with dissolve
        ki "So you like her, right?"
        scene ep3_outside39 with dissolve
        me "..."
        me "I think we'd both say it was based on a spur of the moment 'let's have fun' kind of thing."
        me "I'm sorry."
        scene ep3_outside27 with dissolve
        ki "Don't be."
        jump ep3AfterKiraSexQuestion
    "[M_03_003e]" if not ep2RejectedRobin: # "Ask her to get the story from Robin" if not ep2RejectedRobin:
        $ ep3KiraSexTalk = 4
        $ XPkira += 10
        me "I feel uncomfortable talking about it, if I'm going to be honest."
        me "I would suggest you talk it over with Robin."
        scene ep3_outside40 with dissolve
        ki "Fair, I guess."
        jump ep3AfterKiraSexQuestion
label ep3AfterKiraSexQuestion:
scene ep3_outside28 with dissolve
$ clockis = [[todayIs],1,0,2,9]
ki "You see... Me and Robin both have the same stance on sex."
ki "Like it's a hobby or something fun to do."
scene ep3_outside39 with dissolve
me "Yeah, she told me the whole hobby-story."
scene ep3_outside40 with dissolve
ki "I think that's why we have amazing sex already."
ki "And even though we're in a relationship together, we decided we would bring in a guy..."
ki "...so we could enjoy it even more. Even if it was with someone else."
ki "I just didn't realize that ... I might actually end up liking the guy..."
ki "...very much..."
scene ep3_outside38 with dissolve
me "Wait. You're lesbians?"
scene ep3_outside25 with dissolve
ki "Bi, if you're going to be technical."
ki "...and it's rather funny that you found {b}that{/b} to be the most important part of everything I've said."
scene ep3_outside24 with dissolve
me "I'm just flabbergasted."
scene ep3_outside25 with dissolve
ki "It's alright."
ki "It just caught me off guard."
scene ep3_outside24 with dissolve
me "Me too, I guess."
me "I'm kinda lost for words at the moment."
scene ep3_outside27 with dissolve
ki "And you? Are you mad at me? Or us rather."
scene ep3_outside26 with dissolve
if ep1ToldChrisKiraSituation == 1:
    me "Not really. But playing with someone's feelings is never a smart thing. Both your own and theirs."
    scene ep3_outside24 with dissolve
    ki "You're right."
elif ep1ToldChrisKiraSituation == 3:
    me "Not really. And if I'm going to admit something. I wasn't really looking for a relationship."
    if ep3KiraOutsideLikeHer:
        me "...initially."
    scene ep3_outside24 with dissolve
    ki "Hmmm..."
else:
    me "Not really."
scene ep3_outside29 with dissolve
$ clockis = [[todayIs],1,0,3,4]
me "(I think I need to cheer her up a bit...)"
me "Oh my god. Stop it. Please."
me "That is just too cute."
scene ep3_outside30 with dissolve
ki "Mmm?"
me "Too late. Now you've done it. Cuteness overload."
me "I'm melting."
scene ep3_outside31 with dissolve
ki "Mwhuat?"
me "The way you are drinking with a straw."
scene ep3_outside30 with dissolve
me "It's just too adorable."
scene ep3_outside32 with dissolve
ki "Can you stop it."
ki "I'm drinking normally. Nothing adorable about it."
scene ep3_outside33 with dissolve
me "Ok, ok. Whatever floats your boat."
me "But it's still cute."
ki "..."
scene ep3_outside25 with dissolve
$ clockis = [[todayIs],1,0,3,9]
ki "So... I was wondering."
scene ep3_outside23 with dissolve
ki "Hypothetically speaking, from a guy's point of view..."
scene ep3_outside25 with dissolve
ki "If you were into me. Would you be ok with me still being Robin's lover?"
$ ep3KiraConvExplainMore = False
$ ep3KiraConvExplainMoreCounter = 0
$ gen_notify = "You've just encountered your first {b}Impact Choice{/b}.\n\n{b}Impact choices{/b} are decisions you take that in some form or way will have a ripple-effect that will run it's course until the very end of the story. These choices heavily influence the different character endings (even if they are not your main romantic interest).\n\nGive them some thought before choosing."
show screen general_notifytop with dissolve
label ep3KiraStartImpactChoice:
menu:
    "[M_03_004a]" if not ep3KiraConvExplainMore: # "Can you explain it a bit more?" if not ep3KiraConvExplainMore:
        $ ep3KiraConvExplainMoreCounter += 1
        if ep3KiraConvExplainMoreCounter == 4:
            $ ep3KiraConvExplainMore = True
            hide screen general_notifytop
            show ep3_kira_eat_bg at imgSlide_outside_krobin_bg
            show ep3_kira_eat at imgSlide_outside_krobin
            $ renpy.pause(5)
            ki "You're thinking about me going down on Robin, aren't you..."
            me "Huh?"
            ki "Moving on..."
            hide ep3_kira_eat_bg
            hide ep3_kira_eat
            show screen general_notifytop
        else:
            if ep3KiraConvExplainMoreCounter == 3:
                scene ep3_outside41 with dissolve
                ki "Pay attention, will you?"
                scene ep3_outside40 with dissolve
                me "Ok. But you are talking about you and Robin having sex, right?"
            elif ep3KiraConvExplainMoreCounter == 2:
                scene ep3_outside24 with dissolve
                me "Do you mean, if we were a couple, you would actually be ok with me having sex with you or Robin?"
            else:
                scene ep3_outside24 with dissolve
                me "Do you mean, if we were a couple, and you would still see her on the side?"
            if ep3KiraConvExplainMoreCounter == 3:
                scene ep3_outside41 with dissolve
                ki "A bit more involved ... nevermind."
            elif ep3KiraConvExplainMoreCounter == 2:
                scene ep3_outside25 with dissolve
                ki "Well, as I said, maybe a bit more involved than that."
            else:
                scene ep3_outside25 with dissolve
                ki "No... more involved than that."
            scene ep3_outside24 with dissolve
            me "Threesomes?"
            if ep3KiraConvExplainMoreCounter == 3:
                scene ep3_outside33 with dissolve
                ki "Yes, me going down on Robin and eating her out while you slam into me from behind..."
            elif ep3KiraConvExplainMoreCounter == 2:
                scene ep3_outside25 with dissolve
                ki "Bingo."
            else:
                scene ep3_outside25 with dissolve
                ki "Yes."
            if ep3KiraConvExplainMoreCounter == 1:
                scene ep3_outside25 with dissolve
                ki "Or maybe you would have something against lesbian actions in general."
            scene ep3_outside24 with dissolve
            if ep3KiraConvExplainMoreCounter <=2:
                me "I see."
            else:
                me "Wow."
        jump ep3KiraStartImpactChoice
    "[M_03_004b]": # "Yes, I'd be ok with a two girls relationship (I)":
        $ Impact_KiraRobin = True
        scene ep3_outside24 with dissolve
        me "You're talking about a two girls and a guy relationship."
        scene ep3_outside25 with dissolve
        ki "Yes."
        scene ep3_outside24 with dissolve
        me "Of course I wouldn't mind that."
        jump ep3KiraEndImpactChoice
    "[M_03_004c]": # "No, that wouldn't feel right for me (I)":
        scene ep3_outside24 with dissolve
        me "Not really, no."
        me "Even if you are both beautiful, and such a situation would arise, I'm still too much of a monogamy kind of guy."
        scene ep3_outside23 with dissolve
        ki "I see."
        jump ep3KiraEndImpactChoice
label ep3KiraEndImpactChoice:
hide screen general_notifytop with dissolve
scene ep3_outside25 with dissolve
ki "Anyway, I'm supposed to meet Robin now at Luca's. Want to tag along?"
scene ep3_outside37 with dissolve
me "Sure thing. Why not."
scene ep3_outside25 with dissolve
ki "Great."
scene ep3_outside32 with dissolve
ki "Let me just finish this."
ki "And not a word about me drinking weirdly."
scene ep3_outside37 with dissolve
me "I may or may not say a word."
scene ep3_outside32 with dissolve
ki "Go with may not. Or I may or may not throw something at you."
scene ep3_outside29 with dissolve
$ renpy.pause(3)
scene ep3_outside30 with dissolve
ki "..."
me "I didn't say anything..."
scene ep3_outside34 with dissolve
ki "..."
show screen phone_camop
$ phone_camop_screen = "ep3KiraStraw"
me "(Should I?)"
hide screen phone_camop
$ photoop_ep3KiraStrawNuke = False
jump photoop_ep3KiraStrawEnd
label photoop_ep3KiraStraw:
play sound camerashutter
$ photoop_ep3KiraStrawNuke = True
$ cam_gallery_append_item1 = "ep3_outside30"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_outside30 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
label photoop_ep3KiraStrawEnd:
$ phone_camop_screen = ""
hide screen phone_camop
me "Cute!"
scene ep3_outside35 with dissolve
stop music fadeout 3
$ renpy.pause()
scene bg empty with fade
$ clockis = [[todayIs],1,1,0,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep3_restaurant
$ nowPlayingArtist = "Katrina Stone"
$ nowPlayingTitle = "You and the Summer"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
$ renpy.pause(0.5)
ki "There she is."
scene ep3_cafe04 with fade
ki "Always reading something."
scene ep3_cafe05 with dissolve
me "Robin."
scene ep3_cafe27 with dissolve
ro "[name]."
scene ep3_cafe06 with dissolve
ro "Ki."
scene ep3_cafe08 with dissolve
$ renpy.pause(1)
scene ep3_cafe07 with dissolve
$ renpy.pause(1)
scene ep3_cafe09 with dissolve
ro "What's gotten into your pants?"
scene ep3_cafe26 with dissolve
if ep3KiraSexTalk == 1:
    ki "I'm just in a good mood, honey."
    ki "But I heard you and [name] had a good time the other evening."
    scene ep3_cafe10 with dissolve
    ro "He's not too bad. I was way off on my first impression."
    ro "Don't play videogames with him though. He's cheating."
    scene ep3_cafe11a with dissolve
    me "Wait, what first impression?"
    scene ep3_cafe10 with dissolve
    ro "Oh, nothing."
    scene ep3_cafe_robinwink with dissolve
    me "..."
elif ep3KiraSexTalk == 2:
    ki "Nothing."
    ki "Although, I suspect someone's gotten into yours."
    scene ep3_cafe10 with dissolve
    ro "You mean [name] here?"
    ro "No, he's as gentleman as they come."
    scene ep3_cafe11a with dissolve
    me "What?"
    scene ep3_cafe26 with dissolve
    ki "And you gave him the whole hobby-story as well, right?"
    scene ep3_cafe29 with dissolve
    ro "Yes. And he still resisted."
    scene ep3_cafe13 with dissolve
    ro "Iron will on this one."
    scene ep3_cafe_robinwink with dissolve
    me "..."
elif ep3KiraSexTalk == 3:
    ki "Nothing."
    ki "Although, I know who's gotten into yours."
    scene ep3_cafe13 with dissolve
    ro "Really? You told her?"
    scene ep3_cafe12 with dissolve
    me "...it was those eyes. I couldn't resist."
    scene ep3_cafe29 with dissolve
    ro "I know what you mean."
    scene ep3_cafe26 with dissolve
    ki "So... How was he?"
    scene ep3_cafe29 with dissolve
    ro "5 of 6."
    scene ep3_cafe26 with dissolve
    ki "Nice."
    scene ep3_cafe11a with dissolve
    me "Ok. First of all, I'm right here. I can hear you!"
    me "...second... I'm so confused right now."
    me "...and third... 5 of 6? What was I lacking?"
    scene ep3_cafe13 with dissolve
    ro "Breasts and a pussy."
    scene ep3_cafe_robinwink with dissolve
    me "..."
    scene ep3_cafe15 with dissolve
    ki "Aw... You're so sweet."
elif ep3KiraSexTalk == 4:
    ki "Nothing."
    ki "Although, I suspect someone's gotten into yours."
    scene ep3_cafe13 with dissolve
    ro "Really? You told her?"
    scene ep3_cafe12 with dissolve
    me "Nope, but I suspect you gave it all away now."
    scene ep3_cafe29 with dissolve
    ro "Well played, Ki."
    scene ep3_cafe26 with dissolve
    ki "So... How was he?"
    scene ep3_cafe29 with dissolve
    ro "5 of 6."
    scene ep3_cafe26 with dissolve
    ki "Nice."
    scene ep3_cafe11a with dissolve
    me "Ok. First of all, I'm right here. I can hear you!"
    me "...second... I'm so confused right now."
    me "...and third... 5 of 6? What was I lacking?"
    scene ep3_cafe13 with dissolve
    ro "Breasts and a pussy."
    scene ep3_cafe_robinwink with dissolve
    me "..."
    scene ep3_cafe15 with dissolve
    ki "Aw... You're so sweet."
scene ep3_cafe11a with dissolve
me "You two are something else."
scene ep3_cafe14 with dissolve
ki "Mhmm."
if not ep2RejectedRobin:
    scene ep3_cafe11a with dissolve
    me "And you honestly don't care at all that I fucked Robin."
    scene ep3_cafe14 with dissolve
    ki "Nope."
scene ep3_cafe11a with dissolve
me "Ok, so if I get you right, you are both very open minded when it comes to sex."
scene ep3_cafe13 with dissolve
ro "Isn't that the norm nowadays?"
scene ep3_cafe11a with dissolve
$ clockis = [[todayIs],1,1,1,3]
menu:
    "[M_03_005a]" if Impact_KiraRobin: # "How about a little challenge?" if Impact_KiraRobin:
        me "Well, how about a little challenge?"
        scene ep3_cafe14 with dissolve
        ki "Oooooooooh. That sounds like fun."
        scene ep3_cafe12 with dissolve
        ro "Sure, I'm game."
        scene ep3_cafe11a with dissolve
        me "Ok. Show me a kiss between you two."
        me "And I'm not talking about a little peck on the cheek."
        me "Something that really gets you all riled up."
        scene ep3_cafe10 with dissolve
        ro "That is kinda unfair."
        scene ep3_cafe11a with dissolve
        me "Why?"
        scene ep3_cafe12 with dissolve
        ro "Well, for one. Girls' on-button, don't really come with an off-function."
        ro "I'll be horny for the rest of the day."
        scene ep3_cafe14 with dissolve
        ki "I'm in!"
        scene ep3_cafe26 with dissolve
        ki "Robin, you can go home to your dildo collection and finish off after."
        scene ep3_cafe29 with dissolve
        ro "Yeah, if you only knew."
        scene ep3_cafe15 with dissolve
        ki "Ok, let's do this."
        scene ep3_cafe16 with dissolve
        $ renpy.pause(2)
        scene ep3_cafe17 with dissolve
        ki "That's better. I always get lost in those eyes."
        scene ep3_cafe18 with dissolve
        $ renpy.pause(2)
        scene ep3_cafe19 with dissolve
        $ renpy.pause(2)
        scene ep3_cafe22 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe23 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe24 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe25 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe19 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe20 with dissolve
        $ renpy.pause(2)
        scene ep3_cafe21 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe30 with dissolve
        $ renpy.pause(2)
        scene ep3_cafe19 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe28 with dissolve
        $ renpy.pause(1)
        scene ep3_cafe02 with dissolve
        ro "Approved?"
        me "Approved."
        menu:
            "[M_03_006a]": # "Look at Robin":
                $ XPkira += 1
                scene ep3_cafe_robineyes with dissolve
                ro "..."
                jump ep3EndOfCafeChallenge
            "[M_03_006b]": # "Look at Kira":
                $ XProbin += 1
                $ renpy.movie_cutscene("imov/ep3/ep3_kirasuckfinger.webm", delay=None, loops=0, stop_music=False)
                scene ep3_cafe31
                ki "Not much of a challenge."
                jump ep3EndOfCafeChallenge
    "[M_03_005b]": # "Continue":
        me "Still, I'd say it's a bit more daring than most."
        scene ep3_cafe16 with dissolve
        me "Not that it really matters though."
        jump ep3EndOfCafeChallenge
label ep3EndOfCafeChallenge:
scene ep3_cafe55 with fade
$ clockis = [[todayIs],1,1,2,5]
me "By the way, have you started thinking about your bowling situation?"
scene ep3_cafe32 with dissolve
ro "Yes, I'm heading over to the bank now to have a talk with them."
scene ep3_cafe33 with dissolve
ro "I don't think it's going to solve anything though, but it's worth a try."
scene ep3_cafe55 with dissolve
me "Well, as I've already said, if you need to brainstorm it, I'm here."
scene ep3_cafe32 with dissolve
ro "I'm not really that good at accepting help, but thank you for trying."
scene ep3_cafe55 with dissolve
me "It's brainstorming. Not a million dollars."
scene ep3_cafe34 with dissolve
ki "And you know I'll help with anything I can as well."
scene ep3_cafe34 with dissolve
ch "[name]."
scene ep3_cafe35 with dissolve
"..."
scene ep3_cafe36 with dissolve
me "Ah, this is my friend Chris."
me "Chris, meet..."
ch "Burgerchick."
scene ep3_cafe37 with dissolve
ki "Pussytickler."
scene ep3_cafe38 with dissolve
me "And this is Robin."
ch "Nice to meet you. Where's Batman?"
ro "..."
ch "Because... Batman and Robin?"
scene ep3_cafe39 with dissolve
ro "That is the worst icebreaker I've ever heard."
scene ep3_cafe40 with dissolve
ro "[name], please. Your friend needs some serious help on the pickups."
scene ep3_cafe52 with dissolve
ch "Dude..."
scene ep3_cafe53 with dissolve
ch "...help me."
scene ep3_cafe46 with dissolve
menu:
    "[M_03_007a]": # "Flirty.":
        "*looks at Robin*."
        scene ep3_cafe_robinpickup with dissolve
        me "Hi there, I'm [name]."
        ro "Hello. Robin..."
        me "Nice to meet you, Robin. And thank you."
        ro "For?"
        me "For saying hello, so I could look at you and be reminded of what true beauty really is."
        scene ep3_cafe50 with dissolve
        $ XProbin += 1
        $ meFlirty += 1
        show screen flvl with dissolve
        ro "Slightly better than Chris."
        hide screen flvl with dissolve
        scene ep3_cafe52 with dissolve
        ch "Dude..."
        jump ep3AfterCafePickup
    "[M_03_007b]": # "Cheeky.":
        me "Sure, let me see if I got this."
        scene ep3_cafe_robinpickup with dissolve
        me "That's a wonderful pair of legs you have there. What time do they open?"
        scene ep3_cafe51 with dissolve
        ro "I can't rate any of you. You are equally bad."
        ki "Would have worked on me..."
        scene ep3_cafe53 with dissolve
        ch "Oh, I'm definitely going to use that at some point."
        jump ep3AfterCafePickup
    "[M_03_007c]": # "Nope, you're on your own Chris.":
        "Nope, you're on your own Chris."
        jump ep3AfterCafePickup
label ep3AfterCafePickup:
scene ep3_cafe53 with dissolve
ro "Don't just stand there. Sit down for a coffee."
scene ep3_cafe54 with dissolve
ch "Sure thing. I got a few minutes."
scene ep3_cafe41 with dissolve
ch "*whispers* Pussytickler?"
scene ep3_cafe42 with dissolve
me "*laughs* I wonder why..."
scene ep3_cafe43 with dissolve
ki "So you're that friend I've heard so much about."
scene ep3_cafe44 with dissolve
ch "Only good things, I hope."
scene bg empty with fade
$ clockis = [[todayIs],1,1,4,1]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_cafe56 with fade
ro "Time is flying. I need to head off if I'm to get to that bank appointment in time."
scene ep3_cafe57 with dissolve
ro "Wish me luck."
scene ep3_cafe58 with dissolve
ki "Good luck, sexy."
scene ep3_cafe59 with dissolve
ro "*whispers* Go for it."
scene ep3_cafe60 with dissolve
ki "*whispers* You sure?"
scene ep3_cafe59 with dissolve
ro "*whispers* Yes. I want you to."
scene ep3_cafe61 with dissolve
ch "Yeah, I'm off as well."
ch "I have to get back to work."
scene ep3_cafe62 with dissolve
me "I'll catch up with you later on."
scene ep3_cafe66 with dissolve
ki "Really? You're going to go dressed like this?"
ki "You hobo."
ki "Show some skin, and you might win the bank dude over..."
ki "...or bank girl."
scene ep3_cafe65 with dissolve
ro "Whatever."
scene ep3_cafe64 with dissolve
ro "You coming too, Batman?"
scene ep3_cafe63 with dissolve
ch "Yeah, let me walk you over."
scene ep3_cafe67 with dissolve
ro "See you later, [name]."
scene ep3_cafe68 with dissolve
ch "So... Batman and Robin, right?"
ro "That thing fails on so many levels."
scene ep3_cafe69 with dissolve
ch "How come? Everyone knows Batman and Robin."
ro "Yeah, but seriously. Nobody in their right mind would ever want to be Robin in that scenario."
ch "But what if... Robin was a chick."
scene ep3_cafe70 with dissolve
$ renpy.pause(0.5)
scene ep3_cafe71 with dissolve
$ renpy.pause(0.5)
scene ep3_cafe72 with dissolve
$ renpy.pause(0.5)
ch "...mindblooooooown..."
scene ep3_cafe74 with dissolve
ro "Then everybody would want to do Robin. Not be Robin."
ch "Exactly."
scene ep3_cafe77 with dissolve
me "They are never going to give up that thing, are they."
scene ep3_cafe78 with dissolve
ki "Doubt it."
scene ep3_cafe80 with dissolve
ki "Oh, I completely forgot. You were going to tell me about Lexi!"
scene ep3_cafe88 with dissolve
me "*laughs* Yes. She was at metro."
scene ep3_cafe85 with dissolve
ki "Did she perform? You talked to her? Was she nice?"
scene ep3_cafe87 with dissolve
me "Yes, yes, and yes."
scene ep3_cafe85 with dissolve
ki "What happened?"
scene ep3_cafe88 with dissolve
stop music fadeout 5
me "So, I was drinking at the bar and I heard this voice behind asking if I was ok with some company."
me "And that company was Lexi."
scene ep3_cafe86 with dissolve
ki "No way!"
scene ep3_cafe88 with dissolve
me "Yes. And we shared a bottle of wine and had a nice chat."
me "Actually, I've been waiting for her to call me."
scene ep3_cafe85 with dissolve
ki "Well, that's a bit optimistic, don't you think? I mean, that she'll call you like out of the blue just because you shared a bottle of wine, mister."
scene ep3_cafe87 with dissolve
me "No, really..."
scene ep3_cafe84 with dissolve
ki "...wow. You met Lexi. You are so lucky."
me "*sigh*"
$ clockis = [[todayIs],1,1,4,7]
play sound call_sound
$ call_id = "caller_unknown"
$ call_jump = "ep3_lexicall"
hide screen phone
show screen phone_call_notify
scene ep3_cafe89 with dissolve
if ep3LexiRingTone <> 0:
    $ XPkira += 1
    ki "*laughs* Is that a Lexi ringtone?"
    me "Eh..."
me "Let me take this. I don't recognize the number."
label ep3_lexicall_loop:
    if ep3LexiRingTone == 0:
        play sound call_sound
    me "..."
    jump ep3_lexicall_loop
label ep3_lexicall:
stop sound
scene ep3_cafe89 with dissolve
ki "Sure. Maybe it's Lexi..."
scene ep3_cafe90 with dissolve
play music ep3_lexicalling
$ nowPlayingArtist = "Lance Conrad"
$ nowPlayingTitle = "Perfect Smile"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "Hello?"
scene ep3_airplanecall01 with dissolve
le "Hi, this is Lexi Dimante speaking. Is this the phone of [name]?"
scene ep3_airplanecall02 with dissolve
me "Oh hi Lexi. Yes indeed, this is [name] speaking."
scene ep3_cafe83 with dissolve
ki "*laughs*"
scene ep3_airplanecall01 with dissolve
le "I'm so glad I caught you. I wanted to call you earlier but I didn't have your number, and it's been really hectic on my side."
scene ep3_airplanecall02 with dissolve
me "No problem at all. I'm just very glad you got the time to call me at all."
scene ep3_cafe82 with dissolve
me "I really wanted to thank you properly for taking the time to spend a few minutes with me at Metronome."
scene ep3_airplanecall04 with dissolve
le "No, the pleasure was all mine."
le "And, apologies if that paparazzi picture made you feel uncomfortable."
scene ep3_cafe91 with dissolve
me "The picture of me and you? No, that picture hasn't brought me any discomfort at all. Honestly, I'm just glad somebody did take a picture."
scene ep3_airplanecall06 with dissolve
le "The paparazzi will never change anyway, so might as well throw them a bone for them to chase every once in a while."
scene ep3_cafe91 with dissolve
me "Luckily I don't have a problem with photographers sneaking around in my back yard."
scene ep3_airplanecall03 with dissolve
me "Or, there's this weird guy living on the first floor. I don't know what his hobbies are."
scene ep3_airplanecall11 with dissolve
le "*laughs* I'd consider moving then."
scene ep3_airplanecall10 with dissolve
le "But the reason I called... I have some time off, because I just finished my tour. So I'm flying home soon."
scene ep3_airplanecall05 with dissolve
le "And I know you might have your own plans of course, so I'll just throw it out there and feel free to say no if it's inappropriate."
scene ep3_airplanecall04 with dissolve
le "But, would you like to come visit me at my house in LA?"
menu:
    "[M_03_008a]": # "Hell yes.":
        $ XPlexi += 1
        scene ep3_cafe91 with dissolve
        me "Hell yes!"
        le "Huh?"
        scene ep3_cafe90 with dissolve
        me "I said that with way too much enthusiasm, and way too fast, didn't I."
        le "*laughs*"
        scene ep3_airplanecall05 with dissolve
        le "Maybe. But I'm not complaining."
        me "Is it ok if I bring a friend? You remember Chris from Metronome..."
        jump ep3AfterLexiAccept
    "[M_03_008b]": # "Cece's 'situation'.":
        scene ep3_cafe90 with dissolve
        me "I would love to. And I don't want to seem unappreciative, but I have two friends living at my place now and they are going through a rough time."
        scene ep3_airplanecall05 with dissolve
        le "Ah, I understand. It was a long shot anyway."
        me "No sorry, I didn't make myself clear. What I meant to say was that I'm not really comfortable leaving them here alone..."
        me "...and though I hate to ask you, is there any possibility that they could come as well? I think it will do them good."
        jump ep3AfterLexiAccept
label ep3AfterLexiAccept:
scene ep3_airplanecall04 with dissolve
le "Of course you can bring some friends. Although I've only got 10 bedrooms, but maybe we can get some extra beds..."
scene ep3_cafe90 with dissolve
me "That is more than enough. I was thinking more in the lines of 6 friends tops?"
scene ep3_airplanecall10 with dissolve
le "Bring them. Let's have some fun."
scene ep3_airplanecall03 with dissolve
me "You just say the when and where, and we book our flight tickets as soon as possible."
scene ep3_airplanecall01 with dissolve
le "Well, aren't you sweet."
le "Because you don't need to buy any tickets. My plane is landing at your airport tomorrow at around 11. Think you'll be ready until then?"
scene ep3_airplanecall02 with dissolve
me "A hundred percent sure. We'll be ready."
scene ep3_airplanecall03 with dissolve
le "Good. I'll be seeing you then. Looking forward to it."
$ ep3LexiEndCallKira = False
menu:
    "[M_03_009a]": # "Goodbye.":
        scene ep3_cafe91 with dissolve
        me "Me too. And have a nice flight."
        scene ep3_airplanecall06 with dissolve
        le "Goodbye [name]."
        scene ep3_airplanecall07 with dissolve
        $ renpy.pause(1)
        scene ep3_airplanecall08 with dissolve
        $ renpy.pause(1)
        scene ep3_airplanecall09 with dissolve
        $ renpy.pause()
        scene ep3_cafe98 with dissolve
        me "So that was Lexi..."
        ki "..."
        scene ep3_cafe97 with dissolve
        ki "You are serious aren't you?"
        jump ep3AfterLexiGoodbye
    "[M_03_009b]": # "Can you say hello to my friend here?":
        $ ep3LexiEndCallKira = True
        scene ep3_cafe91 with dissolve
        me "Me too. But can I ask you for a very small favor before we hang up?"
        scene ep3_airplanecall06 with dissolve
        le "Sure thing, darling. What's the favor?"
        scene ep3_cafe91 with dissolve
        me "Can I put you on speaker so that my friend sitting at the other side of the table believes I'm talking to you?"
        le "Of course."
        scene ep3_cafe92 with dissolve
        me "Ok, you're on speaker now. Lexi, my friend Kira. Kira meet Lexi."
        le "Hi, hun. This is Lexi. I hope you're having a wonderful day."
        scene ep3_cafe93 with dissolve
        ki "Lexi?"
        le "Yes, sweetheart?"
        scene ep3_cafe94 with dissolve
        ki "Oh my god, it's really you isn't it. I adore you."
        le "Thank you so much, love. I take it you're having a wonderful day."
        scene ep3_cafe93 with dissolve
        ki "My day just got much better, let me assure you."
        le "I'm so glad to hear that. But unfortunately it's late night in Japan right now and it's the end of a very long day for me."
        scene ep3_cafe95 with dissolve
        ki "I understand. Thank you for saying hi. You just made my month. And have sexy dreams."
        le "*laughs* Who knows, maybe I will. Bye bye Kira. And [name], See you tomorrow."
        scene ep3_airplanecall07 with dissolve
        $ renpy.pause(1)
        scene ep3_airplanecall08 with dissolve
        $ renpy.pause(1)
        scene ep3_airplanecall09 with dissolve
        $ renpy.pause()
        scene ep3_cafe96 with dissolve
        ki "*facepalms* Sexy dreams? Tell me I didn't say that out loud?"
        me "Don't worry. At least you made an impression."
        ki "Stupid, stupid, stupid."
        scene ep3_cafe97 with dissolve
        ki "Wait... Why did she say... 'See you tomorrow'?"
        jump ep3AfterLexiGoodbye
label ep3AfterLexiGoodbye:
scene ep3_cafe98 with dissolve
show screen phone
me "Well, the thing is..."
me "She kinda invited me to her place."
me "...and she kinda said I could bring some friends..."
me "...then went on to kinda say she could pick us up in her private plane tomorrow morning..."
me "...so..."
me "You want to come?"
ki "..."
scene ep3_cafe99 with dissolve
ki "YES!"
scene bg empty with fade
$ contact_notify_me = True
$ contact_text_me += "\n\nI met Kira outside in the morning. Seemingly she had seen me with Robin when I was at her place."
$ contact_text_me += " She also told me that they were in a relationship together, and that they had agreed to bring in a guy from outside to spice up their sex life."
if ep2RejectedRobin:
    $ contact_text_me += "\n\nI could only say the truth that I didn't have sex with Robin, which Robin confirmed a bit later when we met up with her at Luca's."
else:
    $ contact_text_me += "\n\n.The fact that I had sex with Robin made the situation kinda weird when we met up with Robin after. Even weirder when they started discussing the details."
$ contact_notify_kira = True
$ contact_text_kira += "\n\nShe ran into me outside the house in the morning. She confessed that she had seen me with Robin. She also confessed she was ok with that. And that they had agreed to bring in a guy from outside to spice up their sex life."
$ contact_notify_robin = True
$ contact_text_robin += "\n\nI met up with her together with Kira the day after. She is Kira's girlfriend."
$ contact_notify_lexi = True
$ contact_text_lexi += "\n\nLexi called me from the plane. She even invited me and my friends to come home to her place in LA. How could I refuse such an offer."
$ clockis = [[todayIs],1,2,1,8]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_cafe75 with fade
ki "..."
me "Why are you looking at me like that?"
scene ep3_cafe76 with dissolve
ki "Because I like what I'm looking at."
ki "And if I'm going to be honest. I really would like to do a whole lot more than just look."
scene ep3_cafe75 with dissolve
me "..."
scene ep3_cafe76 with dissolve

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "Which ever woman you pick,\nthe other gets a missed opportunity.\n\nPick wisely."
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################

ki "So, what do you say. Do you want to head out of here and fuck like rabbits?"
menu:
    "[M_03_010a]": # "Go with Kira.":
        $ XPkira += 5
        if XPkira > 25:
            $ XPkira = 25
        if Impact_KiraRobin:
            $ XProbin += 2
            if XProbin > 25:
                $ XProbin = 25
        $ ep3RejectedKira = False
        stop music fadeout 3
        scene ep3_cafe75 with dissolve
        me "Yes please. I'd like a Kira to go."

        if MenuChoice != "HintsNone":
            ### Hide Hint ########################################################################################################################################
            hide screen general_notifytop with dissolve
            ### Hide Hint ########################################################################################################################################

        jump ep3KiraLewd
    "[M_03_010b]": # "Head home.":
        $ XPcece += 3
        if XPcece > 25:
            $ XPcece = 25
        scene ep3_cafe82 with dissolve
        me "As tempting as that sounds, I should be heading home now."
        me "I have to speak to a few people about the trip tomorrow."
        scene ep3_cafe84 with dissolve
        ki "Oh damn. That's right. I almost forgot. Can I ask Robin too?"
        scene ep3_cafe87 with dissolve
        stop music fadeout 3
        me "Of course you can. I was about to ask you to."
        me "And be ready for tomorrow morning. I'll text you the details later on."
        scene ep3_cafe84 with dissolve
        ki "I'm as ready as I'll ever be. See you tomorrow then."

        if MenuChoice != "HintsNone":
            ### Hide Hint ########################################################################################################################################
            hide screen general_notifytop with dissolve
            ### Hide Hint ########################################################################################################################################

        jump ep3CeceHome
label ep3KiraLewd:
$ contact_notify_me = True
$ contact_text_me += "\n\nKira invited me home to her place after the Cafe, to 'fuck like rabbits'. And that was just what we did."
$ contact_notify_kira = True
$ contact_text_kira += "\n\nShe invited me home to her place after the Cafe, to 'fuck like rabbits'. And that was just what we did."
$ clockis = [[todayIs],1,2,3,5]
scene bg empty with fade
play music ep3_kirahome
$ nowPlayingArtist = "D Fine Us"
$ nowPlayingTitle = "Howling at the Moon"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_kiramain22 with fade
me "So this is your place, eh?"
scene ep3_kiramain23 with dissolve
ki "Uhm... Yes."
me "Nice."
scene ep3_kiramain24 with dissolve
ki "Tell you what..."
ki "...let me give you the V.I.P. tour..."
scene ep3_kiramain01 with dissolve
me "(What have I got myself into.)"
scene ep3_kiramain02 with dissolve
me "(She's kinda frightening.)"
scene ep3_kiramain03 with dissolve
ki "I've thought a lot about you since the other day..."
ki "...I..."
scene ep3_kiramain04 with dissolve
ki "...should stop talking..."
scene ep3_kiramain05 with dissolve
ki "...and get you out of these."
scene ep3_kiramain06 with dissolve
me "...about Robin..."
ki "She's ok with this, I promise."
scene ep3_kiramain07 with dissolve
ki "So let's relax and have..."
scene ep3_kiramain08 with dissolve
ki "...a lot..."
scene ep3_kiramain09 with dissolve
ki "...of fun."
scene ep3_kiramain10 with dissolve
me "...."
scene ep3_kiramain15 with dissolve
me "What if I do this?"
scene ep3_kiramain14 with dissolve
ki "I'd say..."
scene ep3_kiramain13 with dissolve
ki "...keep doing..."
scene ep3_kiramain12 with dissolve
ki "...just that."
scene ep3_kiramain11 with dissolve
$ renpy.pause(1)
scene ep3_kiramain16 with hpunch
me "..."
scene ep3_kiramain17 with dissolve
me "You're a wild one."
ki "What ever makes you thrust harder, Tiger."
scene ep3_kiramain21 with dissolve
ki "Because I've wanted you since I saw you."
scene ep3_kiramain20 with dissolve
ki "So I'm going to enjoy this..."
scene ep3_kiramain19 with dissolve
ki "...as much as I can."
scene ep3_kiramain18 with dissolve
ki "And let me start with my party trick..."
scene ep3_kiramain25 with dissolve
ki "Nice..."
scene ep3_kiramain26 with dissolve
ki "Can I please suck your cock?"
scene ep3_kiramain27 with dissolve
me ".."
scene ep3_kiramain28 with dissolve
me "That's the weirdest question I've ever been asked."
scene ep3_kiramain27 with dissolve
me "Because there's two things you never ever have to ask for permission to do."
scene ep3_kiramain29 with dissolve
me "One, give a blowjob, and two..."
scene ep3_kiramain30 with dissolve
ki "Thank you."
scene ep3_kiramain31 with dissolve
me "..."
scene ep3_kiramain32 with dissolve
me "Oh..."
scene ep3_kiramain33 with dissolve
me "...my..."
scene ep3_kiramain34 with dissolve
me "...god..."
scene ep3_kira_bjblink
$ renpy.pause(0.5)
scene ep3_kiramain34
$ renpy.pause(0.5)
scene ep3_kiramain35 with dissolve
$ renpy.pause(0.5)
scene ep3_kiramain36 with dissolve
$ renpy.pause(0.5)
scene ep3_kiramain37 with dissolve
$ renpy.pause(0.5)
scene ep3_kiramain36 with dissolve
$ renpy.pause(0.5)
scene ep3_kiramain35 with dissolve
$ renpy.pause()
label ep3KiraBj:
scene ep3_kirabj with dissolve
me "..."
me "Damn you're good."
me "..."
scene ep3_kiramain26 with dissolve
ki "Want more?"
scene ep3_kiramain31 with dissolve
menu:
    "[M_03_011a]": # "Keep going.":
        jump ep3KiraBj
    "[M_03_011b]": # "Move on.":
        jump ep3KiraBjEnd
label ep3KiraBjEnd:
scene ep3_kiramain26 with dissolve
ki "And that was the tour of the hallway."
scene bg empty with fade
$ clockis = [[todayIs],1,2,4,7]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_kiramain39 with fade
ki "This is the kitchen..."
ki "...where I..."
scene ep3_kiramain40 with dissolve
$ renpy.pause(1)
scene ep3_kiramain41 with dissolve
$ renpy.pause(1)
scene ep3_kiramain42 with dissolve
$ renpy.pause(1)
scene ep3_kiramain43 with dissolve
ki "Cock."
ki "Mmmm..."
me "Cook, you mean?"
scene ep3_kiramain45 with dissolve
ki "Cook..."
ki "...whatever."
scene ep3_kiramain46 with dissolve
ki "Keep going."
ki "Or I'm going to bite you again."
label ep3KiraHard:
scene ep3_kirahard with dissolve
$ renpy.pause()
ki "Magnificent."
ki "You're hitting bottom every single stroke."
me "..."
scene ep3_kiramain43 with dissolve
ki "Fuck, I've missed a good cock!"
scene ep3_kiramain45 with dissolve
ki "And yours is just amazing."
scene ep3_kiramain46 with dissolve
ki "I love this."
menu:
    "[M_03_012a]": # "Keep going.":
        jump ep3KiraHard
    "[M_03_012b]": # "Move on.":
        jump ep3KiraHardEnd
label ep3KiraHardEnd:
scene bg empty with fade
$ clockis = [[todayIs],1,3,0,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_kiramain47 with fade
ki "And this is the living room."
scene ep3_kiramain48 with dissolve
ki "...and you are wonderful."
scene ep3_kiramain74 with dissolve
ki "...mmmmmmh."
scene ep3_kiramain49 with dissolve
me "We've been in the same room all along."
ki "Who cares. Just keep going."
scene ep3_kiramain47 with dissolve
ki "Fuck this is good."
label ep3KiraMain:
scene ep3_kiramain with dissolve
ki "..."
ki "I'm ... so ... close."
scene ep3_kiramain74 with dissolve
menu:
    "[M_03_013a]": # "Keep going.":
        jump ep3KiraMain
    "[M_03_013b]": # "Cum.":
        jump ep3KiraMainEnd
label ep3KiraMainEnd:
scene ep3_kiramain50 with dissolve
ki "Can't hold it any more."
scene ep3_kiramain51 with dissolve
ki "..."
me "Holy shit. Watching you..."
scene ep3_kiramain52 with dissolve
me "I can't hold back."
scene ep3_kiramain53 with dissolve
ki "Then don't..."
ki "Aaahhh..."
ki "Cum ... in ... me."
scene ep3_kiramain55 with dissolve
me "But..."
ki "Pill ... ok."
scene ep3_kiramain56 with dissolve
ki "Fill ... me."
scene ep3_kiramain54 with hpunch
me "..."
scene ep3_kiramain57 with hpunch
ki "..."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_kiramain58 with fade
$ clockis = [[todayIs],1,3,0,9]
"..."
scene ep3_kiramain59 with dissolve
me "And that concludes the tour..."
scene ep3_kiramain60 with dissolve
ki "Damn, you know how to make a mess."
if ep2RejectedRobin and stephRejected:
    ki "How long have you been saving up."
    scene ep3_kiramain59 with dissolve
    me "A very, very, very long time..."
scene ep3_kiramain60 with dissolve
ki "I've got to hand it to you."
ki "You've got some stamina."
scene ep3_kiramain61 with dissolve
ki "But the real question is..."
ki "...you ready for another round?"
scene ep3_kiramain62 with dissolve
me "Well, by your professional opinion. Does it look like I'm ready to go again?"
scene ep3_kiramain63 with dissolve
ki "Nope..."
scene ep3_kiramain61 with dissolve
ki "So... What's your recharge timer at?"
scene ep3_kiramain62 with dissolve
me "..."
me "What are you. The energizer bunny?"
me "By the way. Are you ready for the trip tomorrow?"
scene ep3_kiramain64 with dissolve
ki "Holy shit."
scene ep3_kiramain65 with dissolve
ki "I need to text Robin..."
ki "She's going to freak out."
scene ep3_kiramain66 with dissolve
ki "...go shopping some new clothes."
scene ep3_kiramain67 with dissolve
ki "...see if I can get a hairdresser to do something about this fluffy mess of a hair..."
scene ep3_kiramain68 with dissolve
ki "...I need to get ready."
scene ep3_kiramain69 with dissolve
ki "...You need to get ready."
scene ep3_kiramain70 with dissolve
me "Ok. Now I'm ready."
scene ep3_kiramain76 with dissolve
ki "Huh?"
ki "Oh no you don't. Not now. I've got a lot of things to do."
scene ep3_kiramain75 with dissolve
me "Didn't you just ask me for another round?"
scene ep3_kiramain76 with dissolve
ki "That was before you reminded me of Lexi!"
scene ep3_kiramain73 with dissolve
me "*sigh* It's such a nice view though."
menu:
    "[M_03_014a]" if meRomantic >= 3: # "I think we have enough time. (R)" if meRomantic >= 3:
        $ XPkira += 1
        if XPkira > 25:
            $ XPkira = 25
        $ ep3KiraEndGame = 1
        show screen rshw with dissolve
        scene ep3_kiramain79 with dissolve
        me "You're probably right."
        me "I probably shouldn't be thinking about me positioning myself behind you."
        me "And sliding my dick up and down."
        me "Until it's glistering with the wetness that is you."
        scene ep3_kiramain80 with dissolve
        me "...and I put myself against you..."
        me "...putting just the slightest amount of pressure."
        me "...and gliding forward, until my hips meet your backside..."
        me "...feeling the inner walls of your pussy, clamping..."
        me "...as your body archs..."
        scene ep3_kiramain79 with dissolve
        ki "...I think we got time for another round!"
        hide screen rshw with dissolve
        jump ep3KiraEncoreEnd
    "[M_03_014b]" if meFlirty >= 3: # "But what about my party trick. (F)" if meFlirty >= 3:
        $ XPkira += 1
        if XPkira > 25:
            $ XPkira = 25
        $ ep3KiraEndGame = 2
        scene ep3_kiramain78 with dissolve
        show screen fshw with dissolve
        me "I never got to show you my party trick though."
        me "How it makes you feel when I do this..."
        scene ep3_kiramain77 with dissolve
        me "While doing this..."
        me "...and don't forget about this little twirl..."
        me "...right there..."
        scene ep3_kiramain78 with dissolve
        ki "Let's..."
        ki "...put the whole Lexi thing on hold for a bit..."
        ki "...and you go twirl all you like..."
        hide screen fshw with dissolve
        jump ep3KiraEncoreEnd
    "[M_03_014c]" if meSporty >= 3: # "I don't need words to persuade you. (S)" if meSporty >= 3:
        $ XPkira += 1
        if XPkira > 25:
            $ XPkira = 25
        $ ep3KiraEndGame = 3
        scene ep3_kiramain81 with dissolve
        show screen sshw with dissolve
        me "I like them wild horses."
        me "You just need to slowly approach them."
        me "And while they let their guard down for just a tiny little bit."
        scene ep3_kiramain82 with dissolve
        me "You ease into position, and slowly..."
        me "...mount them..."
        scene ep3_kiramain83 with dissolve
        ki "..."
        ki "Enough talking..."
        ki "...more riding!"
        hide screen sshw with dissolve
        jump ep3KiraEncoreEnd
    "[M_03_014d]": # "You're right. I should get going.":
        me "But you're right. I should get going."
        jump ep3KiraEncoreEnd
label ep3KiraEncoreEnd:
scene bg empty with fade
stop music fadeout 3
$ clockis = [[todayIs],1,4,0,2]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_cecehome01 with fade
play music ep3_cecehomeinter
$ nowPlayingArtist = "Michael Shynes"
$ nowPlayingTitle = "Next to You"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "(...Well, that was intense. But where are the girls?)"
me "Hello. Anybody here?"
scene ep3_cecehome74 with dissolve
li "Try the shower."
scene ep3_cecehome72 with dissolve
me "Ah. You're here."
li "Just got back, yes."
scene ep3_cecehome73 with dissolve
li "..."
me "Any luck on the job hunt?"
scene ep3_cecehome75 with dissolve
li "Awful."
scene ep3_cecehome76 with dissolve
me "Well, I've got some good news."
li "Do tell."
me "Let's wait for Cece."
scene ep3_cecehome77 with dissolve
li "She's probably not far away."
scene ep3_cecehome78 with dissolve
li "Whoa... There you are."
ce "Can you knock first. I'm taking a shower here."
li "Who cares. I need to pee."
jump ep3AfterLewd
label ep3CeceHome:
$ contact_notify_me = True
$ contact_text_me += "\n\nKira invited me home to her place after the Cafe, to 'fuck like rabbits'. I declined, and went home instead."
$ contact_notify_kira = True
$ contact_text_kira += "\n\nShe invited me home to her place after the Cafe, to 'fuck like rabbits'. It seems she was ok with me rejecting her."
$ clockis = [[todayIs],1,2,4,9]
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_cecehome01 with fade
me "Linda? Cece?"
scene ep3_cecehome02 with dissolve
me "Anybody here?"
scene ep3_cecehome03 with dissolve
me "(Nobody here it seems.)"
scene ep3_cecehome08 with dissolve
me "(This is my chance to take a quick shower...)"
play music ep3_cecehome
$ nowPlayingArtist = "Guesthouse"
$ nowPlayingTitle = "Trendsetter"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep3_cecehome07 with dissolve
$ renpy.pause(1)
scene ep3_cecehome06 with dissolve
$ renpy.pause(1)
scene ep3_cecehome05 with dissolve
$ renpy.pause(1)
show ep3_cecehome04_bg at imgSlide_ep3_cecehome_bg
show ep3_cecehome04 at imgSlide_ep3_cecehome
$ renpy.pause(12)
show ep3_cecehome04b
hide ep3_cecehome04
$ renpy.pause(1)
show ep3_cecehome04c
hide ep3_cecehome04b
$ renpy.pause(1)
scene ep3_cecehome10 with fade
hide ep3_cecehome04c
hide ep3_cecehome04_bg
me "So..."
me "...I didn't see anything..."
scene ep3_cecehome11 with dissolve
me "..."
scene ep3_cecehome12 with dissolve
me "...of importance..."
scene ep3_cecehome13 with dissolve
me "...just wanted to let you know..."
scene ep3_cecehome14 with dissolve
me "...and I..."
scene ep3_cecehome15 with dissolve
me "..."
scene ep3_cecehome16 with dissolve
ce "Thank you for last night."
ce "I had a really good time."
scene ep3_cecehome17 with dissolve
me "Me too."
me "And how are you feeling?"
scene ep3_cecehome16 with dissolve
ce "I know you mean well, but not today please."
ce "And I'm feeling good."
scene ep3_cecehome17 with dissolve
me "Sure thing."
me "But you know, I was thinking about that Matt thing..."
scene ep3_cecehome16 with dissolve
ce "What about it?"
scene ep3_cecehome17 with dissolve
me "Well, for starters, like I said, you should really be careful around guys like him."
scene ep3_cecehome19 with dissolve
ce "You don't think I can handle myself?"
scene ep3_cecehome18 with dissolve
me "It's not about that. But you know, looking for trouble is never a good thing."
scene ep3_cecehome19 with dissolve
ce "In case you didn't notice, that thing was fixing trouble, not looking for it."
scene ep3_cecehome18 with dissolve
me "I agree, it worked out fine. But I'd like to teach you a little trick in case it doesn't."
scene ep3_cecehome20 with dissolve
ce "Can you get over the poor little girl that can't take care of herself thing?"
scene ep3_cecehome21 with dissolve
me "You seem capable of taking care of yourself alright. But if anything, just humor me."
me "It's nothing over complicated. And you get to learn something new."
scene ep3_cecehome22 with dissolve
ce "Sure, let's do this."
ce "Let me just put something on."
scene ep3_cecehome23 with dissolve
ce "Everything I have is in the washer though."
scene ep3_cecehome24 with dissolve
me "It's not that much really. Just a little trick..."
ce "Yeah, I'm not doing it while in a towel in any case."
ce "..."
ce "Come on, Linda. You bought me Yoga-pants?"
scene ep3_cecehome26 with dissolve
me "Doesn't sound so bad..."
ce "Ok. I'll give it a try."
scene ep3_cecehome25 with dissolve
ce "No peeking."
scene ep3_cecehome26 with dissolve
me "..."
ce "How am I supposed to get myself into these?"
ce "They are like made of nothing at all."
me "I'm sure you look amazing."
ce "Feels like I'm putting everything on display here."
me "..."
ce "Ok, this is horrible. I'm going to put them back."
me "No, please don't. Let me have a look."
me "You've already seen me without a towel on..."
ce "*sigh* {size=15}...here goes.{/size}"
scene ep3_cecehome27 with fade
$ clockis = [[todayIs],1,3,1,5]
me "You look great."
ce "Sure..."
me "No really, you look fantastic."
ce "..."
scene ep3_cecehome28 with fade
me "Wow..."
scene ep3_cecehome29 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_cecehome30 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_cecehome28 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_cecehome31 with dissolve
ce "Uhh... That was awful. I'm not cut out for this body on display stuff."
scene ep3_cecehome32 with dissolve
stop music fadeout 3
me "Come on. Let's get on with this..."
me "...and you look phenomenal by the way."
scene ep3_cecehome33 with dissolve
$ clockis = [[todayIs],1,3,3,4]
play music ep3_cecehomeinter
$ nowPlayingArtist = "Michael Shynes"
$ nowPlayingTitle = "Next to You"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "Ok ... so the trick is very simple."
me "But be careful you don't go too hard, or you might do some serious damage."
scene ep3_cecehome34 with dissolve
me "It's all about getting access to the pinky finger."
me "So you might go for the fast approach and just grab it, or be more subtle."
scene ep3_cecehome35 with dissolve
me "Like this."
ce "Mhmmm..."
scene ep3_cecehome36 with dissolve
me "And now you've won."
scene ep3_cecehome39 with dissolve
ce "That doesn't hurt at all."
scene ep3_cecehome38 with dissolve
me "It's not supposed to hurt right now."
me "It's when you squeeze it while retracting your thumb the pain sets in."
me "That pain is intense, and it will keep being so for as long as you apply pressure."
me "And that pain will bring down a 500 pound piece of muscle."
me "Much worse than a kick in the groin."
scene ep3_cecehome39 with dissolve
ce "Do it..."
scene ep3_cecehome40 with dissolve
me "I don't really want to."
scene ep3_cecehome39 with dissolve
ce "I can take it. I'm really good with handling pain. So I want to test how it feels."
scene ep3_cecehome40 with dissolve
me "This is going to hurt."
scene ep3_cecehome36 with dissolve
ce "Don't hold back."
scene ep3_cecehome37 with dissolve
ce "..."
scene ep3_cecehome41 with hpunch
ce "*sucks in air* aouwwww... Okokokokokletgo!"
scene ep3_cecehome43 with dissolve
me "I'm so sorry!"
scene ep3_cecehome44 with dissolve
me "I know how much it hurts."
scene ep3_cecehome45 with dissolve
ce "..."
scene ep3_cecehome46 with dissolve
ce "Can I try?"
scene ep3_cecehome33 with dissolve
me "Sure. Give it a go."
scene ep3_cecehome47 with dissolve
ce "..."
me "That is good. Play on your flirty side so the person don't get that you are trying to access the finger."
scene ep3_cecehome48 with dissolve
me "Mhmmm. Keep going."
scene ep3_cecehome50 with dissolve
ce "..."
scene ep3_cecehome51 with dissolve
ce "...I..."
me "You're doing good, almost there. It's all about getting to that finger."
scene ep3_cecehome52 with dissolve
ce "*breathes audible*"
scene ep3_cecehome49 with dissolve
me "...and ... there you have it."
scene ep3_cecehome52 with dissolve
me "And now you just apply pressure like I showed you."
me "But please don't, I already know how much it hurts."
scene ep3_cecehome53 with dissolve
ce "Shhh..."
me "..."
me "Great job on the breathing, that draws attention from what you are doing with the finger."
scene ep3_cecehome49 with dissolve
ce "Really now? Great job on the breathing?"
scene ep3_cecehome54 with dissolve
me "Yes, I mean it. You did gr..."
scene ep3_cecehome55 with dissolve
me "Oh sweet mother of ... the pain ..."
scene ep3_cecehome56 with dissolve
me "What the heck did you do that for? I told you not to."
scene ep3_cecehome57 with dissolve
ce "You deserved it."
ce "We had a moment, and you ruined it!"
scene ep3_cecehome56 with dissolve
me "Moment? What are you on about. What moment."
scene ep3_cecehome58 with dissolve
ce "Hrmmmf..."
me "I don't get it."
ce "Men..."
me "Moment?"
scene ep3_cecehome59 with dissolve
ce "And I can perfectly well take care of myself without your finger trick."
scene ep3_cecehome60 with dissolve
me "How, if you don't mind me asking?"
scene ep3_cecehome59 with dissolve
ce "You know what? I will show you."
ce "Close your eyes..."
scene ep3_cecehome60 with dissolve
me "Do I need to cover my privates?"
scene ep3_cecehome59 with dissolve
ce "No."
scene ep3_cecehome60 with dissolve
me "Are you going to pour water on me?"
scene ep3_cecehome59 with dissolve
ce "Close your eyes."
scene bg empty with fade
me "Ok."
me "Now what?"
ce "Now you open them."
scene ep3_cecehome62 with fade
$ clockis = [[todayIs],1,3,4,8]
me "..."
me "Whoa..."
scene ep3_cecehome61 with dissolve
ce "Hi..."
scene ep3_cecehome63 with dissolve
me "Holy shit!"
ce "Nice eh? I've been doing Taekwondo since I was 6."
scene ep3_cecehome67 with dissolve
me "You are really flexible."
ce "Go ahead, lift my foot higher. I won't break."
scene ep3_cecehome64 with dissolve
me "So you see, you might think twice about ruining the moment with me."
play sound ep3_rip
scene ep3_cecehome65 with dissolve
"*riiiiiiiiiiip*"
scene ep3_cecehome68 with dissolve
ce "{size=20}...that was so embarrassing...{/size}"
scene ep3_cecehome69 with dissolve
me "Now {b}that's{/b} a moment!"
scene ep3_cecehome70 with dissolve
ce "*yells* That is {b}sooooo{/b} not a moment!"
scene ep3_cecehome69 with dissolve
me "We should Nuke it."
scene ep3_cecehome70 with dissolve
ce "{size=20}...hmmmmrffhh...{/size}"
scene ep3_cecehome71 with dissolve
$ clockis = [[todayIs],1,4,0,2]
li "What's with the commotion."
scene ep3_cecehome72 with dissolve
me "I think you'd better ask Cece about that."
scene ep3_cecehome73 with dissolve
li "..."
me "Any luck on the job hunt?"
scene ep3_cecehome75 with dissolve
li "Awful."
scene ep3_cecehome76 with dissolve
me "Well, I've got some good news."
li "Do tell."
me "Let's wait for Cece."
scene ep3_cecehome77 with dissolve
li "She's probably not far away."
me "You should probably wait..."
scene ep3_cecehome78 with dissolve
li "Whoa... There you are."
ce "Can you knock first. I'm changing."
li "Who cares. I need to pee."
$ contact_notify_me = True
$ contact_text_me += "\n\nCece was at home, and we shared a moment. And I got to show her the Pinky thing. Linda arrived home shortly after."
$ contact_notify_cece = True
$ contact_text_cece += "\n\nThe following afternoon I spent some time with her at home, where we shared a moment."
jump ep3AfterLewd
label ep3AfterLewd:
scene bg empty with fade
$ clockis = [[todayIs],1,5,0,5]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_cecehome79 with fade
me "So... I've got some good news."
scene ep3_cecehome80 with dissolve
if ep3RejectedKira:
    ce "And I'm still pissed at you by the way."
    li "Hmm?"
    me "Moving on..."
me "You know Lexi, right?"
scene ep3_cecehome81 with dissolve
li "Who?"
scene ep3_cecehome82 with dissolve
ce "I think it's that actor that used to date Nite Dawg."
scene ep3_cecehome83 with dissolve
li "Oh, I love Nite Dawg. And his new single 'The End' is smashing..."
me "No, that's not Lexi, she's an artist..."
ce "I know, right?"
me "(...they are going to go on forever now...)"
$ clockis = [[todayIs],1,5,3,3]
scene ep3_cecehome82 with dissolve
show screen phone_nointeractive
$ renpy.pause(1)
hide screen phone_nointeractive
$ clockis = [[todayIs],1,5,3,4]
show screen phone_nointeractive
scene ep3_cecehome83 with dissolve
$ renpy.pause(1)
hide screen phone_nointeractive
$ clockis = [[todayIs],1,5,3,5]
show screen phone_nointeractive
scene ep3_cecehome82 with dissolve
$ renpy.pause(1)
hide screen phone_nointeractive
$ clockis = [[todayIs],1,5,3,6]
show screen phone_nointeractive
scene ep3_cecehome84 with dissolve
$ renpy.pause(1)
hide screen phone_nointeractive
$ clockis = [[todayIs],1,5,3,7]
show screen phone_nointeractive
scene ep3_cecehome83 with dissolve
$ renpy.pause(1)
hide screen phone_nointeractive
$ clockis = [[todayIs],1,5,3,8]
show screen phone_nointeractive
scene ep3_cecehome82 with dissolve
$ renpy.pause(1)
hide screen phone_nointeractive
scene ep3_cecehome84 with dissolve
ce "...hip hop rules..."
scene ep3_cecehome85 with dissolve
me "*sigh* So, if you're done talking about Goodnight Dawg now..."
"*laughs*"
scene ep3_cecehome86 with dissolve
me "...what I was about to tell you..."
me "...Lexi Dimante called me earlier today..."
me "*waits for response*"
me "*no response*"
me "...and she invited me to come to her place in Los Angeles, and said I could bring some friends."
me "So... Do you want to come?"
me "She's picking us up in her private jet tomorrow."
scene ep3_cecehome87 with dissolve
li "Los Angeles?"
ce "We're going to LA?"
me "Yes, if you want to come of course."
scene ep3_cecehome88 with dissolve
ce "We're going to LA!"
me "Eh ... with Lexi..."
scene ep3_cecehome89 with dissolve
li "Los Angeles!"
scene ep3_cecehome90 with dissolve
$ contact_notify_linda = True
$ contact_text_linda += "\n\nShe had been out all day again. Luckyly I had some good news - about us being invited to Lexi's place. She seemed overjoyed by it."
$ contact_notify_cece = True
$ contact_text_cece += "\n\nAfterwards, I told her about us being invited to Lexi, or ... LA, and she was delighted."
stop music fadeout 3
me "...oh kay..."
me "...you two have fun while I go break the news to Chris..."
me "(I wonder how he's going to take it...)"
scene bg empty with fade
$ clockis = [[todayIs],1,6,5,5]
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep3_chrishome
$ nowPlayingArtist = "Ziv Moran"
$ nowPlayingTitle = "Fantastico"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_chris_bag with fade
$ contact_notify_chris = True
$ contact_text_chris += "\n\nChris gets easily exited. And he loves Lexi. Put those two together, and you get quite a reaction to telling him that that we were invited to her place."
$ contact_text_chris += " Of course he was overjoyed."
me "..."
me "If it's any comfort, you're taking it way better than I thought you would..."
scene ep3_chrisnews04 with dissolve
ch "..."
scene ep3_chris_bag with dissolve
me "..."
scene ep3_chrisnews06 with dissolve
ch "Ok..."
ch "I'm good now."
scene ep3_chrisnews07 with dissolve
ch "Holy shit. She really called you didn't she."
scene ep3_chrisnews08 with dissolve
me "She really did."
scene ep3_chrisnews07 with dissolve
ch "And just to be sure, you weren't joking about us being invited to her place."
scene ep3_chrisnews08 with dissolve
me "Nope."
me "I don't think it's quite dawned on me as well."
me "But she seemed happy about it to be honest."
scene ep3_chrisnews07 with dissolve
ch "You know what that means, right?"
ch "It means she likes you."
scene ep3_chrisnews10 with dissolve
ch "My friend is going to date the hottest popstar in the business."
scene ep3_chrisnews08 with dissolve
me "I don't know about that."
scene ep3_chrisnews07 with dissolve

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "Which ever woman you pick,\nthe others gets a missed opportunity.\n\nPick wisely."
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################
    
$ clockis = [[todayIs],1,7,0,3]
ch "What... You don't like her?"
menu:
    "[M_03_015a]": # "Of course I like her.":
        $ ep3ToldChrisWhoMcLike = 1
        scene ep3_chrisnews08 with dissolve
        me "Of course I like her. How could I not."
        me "She's the most beautiful woman I've ever seen."
        me "And she seems super nice."
        me "And the way I feel when she looks at me is just..."
        scene ep3_chrisnews07 with dissolve
        ch "Say no more man. I've seen that look on your face before."
        jump ep3AfterChrisHomeConv
    "[M_03_015b]": # "I haven't given it any thought.":
        scene ep3_chrisnews08 with dissolve
        me "I haven't given it any thought at all."
        me "But I know that we're going to have a hell of a good time."
        scene ep3_chrisnews07 with dissolve
        ch "I hear you, man."
        jump ep3AfterChrisHomeConv
    "[M_03_015c]": # "I think my heart belongs to someone else.":
        scene ep3_chrisnews08 with dissolve
        me "She's gorgeous alright. But..."
        me "...there's already someone else."
        scene ep3_chrisnews07 with dissolve
        ch "Now you made me curious man, spill..."
        ch "And I'll try and help you in any way I can."
        scene ep3_chrisnews08 with dissolve
        menu:
            "[M_03_016a]": # "Cece":
                $ ep3ToldChrisWhoMcLike = 2
                me "Cece."
                scene ep3_chrisnews09 with dissolve
                ch "I did not see that coming."
                scene ep3_chrisnews07 with dissolve
                ch "But I understand you."
                scene ep3_chrisnews08 with dissolve
                me "I feel this bond with her. I can't explain it."
                scene ep3_chrisnews07 with dissolve
                ch "Let's see what we can do on this trip to hook you up with her.."
                jump ep3AfterChrisHomeConv
            "[M_03_016b]": # "Kira.":
                $ ep3ToldChrisWhoMcLike = 3
                me "Kira."
                scene ep3_chrisnews07 with dissolve
                ch "Hah. You are soooo going to have to thank me in your wedding speech."
                ch "'...and then my buddy here set me up with Kira...'"
                scene ep3_chrisnews08 with dissolve
                me "'...and to top it off, he took a picture of her ... and sent it to me.'"
                scene ep3_chrisnews07 with dissolve
                ch "Ok, let's leave that part out."
                jump ep3AfterChrisHomeConv
            "[M_03_016c]": # "Robin.":
                $ ep3ToldChrisWhoMcLike = 4
                me "Robin."
                scene ep3_chrisnews07 with dissolve
                ch "Really? I never would have thought."
                ch "You can always borrow my Batman suit if you want."
                scene ep3_chrisnews08 with dissolve
                me "You have a Batman suit?"
                scene ep3_chrisnews09 with dissolve
                ch "Ehm... Can you just forget that I even said that for like ... forever?"
                me "Not a chance."
                jump ep3AfterChrisHomeConv
            "[M_03_016d]" if Impact_KiraRobin: # "Kira and Robin." if Impact_KiraRobin:
                $ ep3ToldChrisWhoMcLike = 7
                scene ep3_chrisnews08 with dissolve
                me "Kira and Robin."
                scene ep3_chrisnews07 with dissolve
                ch "I knew it! They're bi, aren't they?"
                scene ep3_chrisnews08 with dissolve
                if not ep2RejectedRobin and not ep3RejectedKira:
                    me "Yes. And let's not forget that I fucked them both already."
                    scene ep3_chrisnews07 with dissolve
                    ch "You monster!"
                    ch "That's my dude."
                else:
                    me "Yes. And I'm pretty sure they both like me."
                    scene ep3_chrisnews07 with dissolve
                    ch "You sure you can handle two women?"
                    scene ep3_chrisnews08 with dissolve
                    me "Yes!"
                    scene ep3_chrisnews07 with dissolve
                    ch "That's my dude."
                jump ep3AfterChrisHomeConv
            "[M_03_016e]": # "Linda.":
                $ ep3ToldChrisWhoMcLike = 5
                me "Linda."
                scene ep3_chrisnews07 with dissolve
                ch "Wow... Linda?"
                scene ep3_chrisnews08 with dissolve
                me "Yes?"
                scene ep3_chrisnews07 with dissolve
                ch "But... the whole past thing. You dated 'you know who' while we were back in school."
                scene ep3_chrisnews08 with dissolve
                me "Ok, I haven't told you this, but she flirted quite heavily with me in the dressing room at Ashley's, when you were sleeping."
                scene ep3_chrisnews07 with dissolve
                ch "*laughs* I kinda suspected it... That would make for such a good story."
                ch "[name] and Linda."
                ch "Yes!"
                jump ep3AfterChrisHomeConv
            "[M_03_016f]" if not ep2ChrisConvOverSteph == 1: # "...you know who..." if not ep2ChrisConvOverSteph == 1:
                $ ep3ToldChrisWhoMcLike = 6
                me "*sigh* You know who..."
                scene ep3_chrisnews09 with dissolve
                ch "You really can't get her out of your head, can you."
                me "..."
                scene ep3_chrisnews07 with dissolve
                ch "I just want the best for you man, if that's your choice..."
                ch "...I won't stop you."
                ch "But we are going to talk about this again."
                jump ep3AfterChrisHomeConv
            "[M_03_016g]": # "...":
                scene ep3_chrisnews08 with dissolve
                me "..."
                scene ep3_chrisnews07 with dissolve
                ch "It's ok, man. You don't have to say anything."
                ch "...yet."
                jump ep3AfterChrisHomeConv
label ep3AfterChrisHomeConv:
$ clockis = [[todayIs],1,8,0,8]

if MenuChoice != "HintsNone":
    ### Hide Hint ########################################################################################################################################
    hide screen general_notifytop with dissolve
    ### Hide Hint ########################################################################################################################################

scene ep3_chrisnews10 with dissolve
ch "We're really going to Lexi's place, aren't we."
scene ep3_chrisnews08 with dissolve
me "Yes we are!"
me "Provided you can get time off from your work, that is."
scene ep3_chrisnews07 with dissolve
ch "Shouldn't be any problem."
ch "I've got lots of vacation I can cash in, even on short notice. My boss is actually quite cool."
ch "And he's a Lexi fan, so I can bribe him with a Lexi autograph."
scene ep3_chrisnews08 with dissolve
me "Good."
me "So you all ready for tomorrow?"
scene ep3_chrisnews07 with dissolve
ch "When are we leaving?"
scene ep3_chrisnews08 with dissolve
me "Oh, I didn't tell you that part."
me "We're getting picked up in Lexi's private jet."
scene ep3_chrisnews09 with dissolve
me "And Lexi's going to be there as well."
ch "..."
scene ep3_chris_bagfast with dissolve
me "You were doing so good there for a while."
stop music fadeout 3
scene ep3_chrisnews11 with dissolve
me "*laughs* We'll pick you up in the morning. Be ready. 11 o'clock sharp."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
play music ep3_eveninghome
$ nowPlayingArtist = "James Forest"
$ nowPlayingTitle = "Big White Ship"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_eveninghome02 with fade
$ clockis = [[todayIs],1,9,4,2]
me "..."
me "What's with the lack of clothes?"
scene ep3_eveninghome01 with dissolve
li "We're getting ready for tomorrow. Packing."
li "Have you packed?"
me "I just need 10 minutes for that. I'll do it in the morning."
scene ep3_eveninghome03 with dissolve
li "You'll forget something."
me "..."
scene ep3_eveninghome04 with dissolve
ce "Do you know where the mascara is?"
li "Should be out there."
li "...and the primer, concealer, foundation, powder, bronzer..."
ce "You take care of that then, I'll get the clothes."
li "...blush, contour, highlighter, setting spray, eye primer, eyeshadow, brushes, eyeliner, cleanser, lipstick..."
ce "The pink one."
li "...toner, brightener, moisturiser, lip gloss..."
ce "You already said lip gloss."
li "No, I said lipstick."
ce "..."
li "...panties, tampons, bathing suit, yogapants..."
if ep3RejectedKira:
    ce "Yeah, about that..."
    li "Hm?"
    ce "Nevermind."
scene ep3_eveninghome05 with dissolve
ce "Move your ass."
ce "You're in the way."
scene ep3_eveninghome06 with dissolve
me "Ok, ok..."
ce "*hums* duh duh duh... '{i}muuuuve your ass{/i}' ..."
scene ep3_eveninghome07 with dissolve
me "Women..."
li "*cough*..."
li "You're in the way."
scene ep3_eveninghome08 with dissolve
me "I'm feeling very unwanted right now."
li "Tell you what... Lay down on the bed and relax. We'll do the packing."
me "No, you got the bed. I'll take the couch."
scene ep3_eveninghome09 with dissolve
li "Ok... you stop the bullshit right now."
scene ep3_eveninghome10 with dissolve
li "That's your bed, so you get your ass down on it."
ce "*hums* ... '{i}hyper, hyper{/i}' ..."
scene ep3_eveninghome11 with dissolve
li "And don't move a muscle."
me "Yes, ma'am."
scene ep3_eveninghome12 with dissolve
li "How can you like Scooter, Cece."
li "They were popular from, like, before we were even born."
ce "Don't care. They are still cool, ok?"
li "*hums* ... '{i}hyper, hyper{/i}' ..."
scene ep3_eveninghome13 with dissolve
$ clockis = [[todayIs],2,0,4,2]

$ ep3RespondedKira = False
$ ep3RespondedLexi = False
$ ep3RespondedChris = False
$ ep3PhoneEventKira = True
$ ep3PhoneEventChris = True
$ ep3PhoneEventLexi = True
$ ep3ChrisMsg1 = "1;0;1310;30 minutes then."
$ ep3ChrisMsg2 = "1;0;1801;30 minutes then."
if ep3ChrisMsg1 in chat_chris:
    $ chat_chris.remove(ep3ChrisMsg1)
    $ chat_chris.append(ep3ChrisMsg2)
$ phChatNotify = True
$ chat_notify_lexi = True
$ chat_lexi_item = "1;0;1701;Hi there " + name + ". I just wanted to fill you in on the details for tomorrow. Plane lands at 11:30, and we're hoping to take off at 12. Is that ok for you?"
if chat_lexi_item not in chat_lexi:
    $ chat_lexi.append(chat_lexi_item)
$ chat_notify_kira = True
$ chat_kira_item = "1;0;1901;We're ready!"
if chat_kira_item not in chat_kira:
    $ chat_kira.append(chat_kira_item)
$ chat_kira_item = "1;1;1902;ep3_kiramsg1"
if chat_kira_item not in chat_kira:
    $ chat_kira.append(chat_kira_item)
    $ cam_gallery.append("ep3_kiramsg1")
    $ phGallNotify = True
$ nukeStoriesAdd1 = "8;You;ep3_outside30;Look at this. Isn't it adorable?"
$ nukeStoriesAdd2 = "9;You;ep3_outside30;Someone please teach her how to drink from a straw."
if nukeStoriesAdd1 in nukeStories:
    $ nukeCommentsAdd = "8;801;Robin4739;It IS."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "8;802;Janice;OMG. That is so adorable."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "8;803;Janice;Wait... Who took the picture?"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "8;804;Robin4739;It says so right there at the top Janice."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "8;805;Janice;OMG. I'm so curious right now. Tell me. Please."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
if nukeStoriesAdd2 in nukeStories:
    $ nukeCommentsAdd = "9;901;Robin4739;My thoughts exactly."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "9;902;Janice;OMG. That is so adorable."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "9;903;Janice;Wait... Who took the picture?"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "9;904;Robin4739;It says so right there at the top Janice."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "9;905;Janice;OMG. I'm so curious right now. Tell me. Please."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
$ nukeStoriesAdd = "13;Stephanie;ep3_nuke_stephstreet;Moving on. New life, new possibilities. If you read this, you'll be forever in my heart."
if nukeStoriesAdd not in nukeStories:
    $ nukeStories.append(nukeStoriesAdd)
$ nukeCommentsAdd = "13;1301;Verd;Best of luck to you. Good journey."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "13;1302;Hollywood;Call me when you get here sweetie. <3"
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "13;1303;BlackBeauty;I miss you. Best of luck to you."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "13;1304;Swole;For what it's worth, you have my eternal respect. It was nice working with you. Good luck."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ ep3CanReplySteph = True
play sound phone_notify_sound
show screen phone_notify_chat

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "Check Stephanie's {b}Nuke{/b} message"
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################

me "(...)"
me "(Ok, I admit it. I've missed the bed.)"
me "(This is so nice, I might actually fall asleep.)"
me "(...)"

if MenuChoice != "HintsNone":
    ### Hide Hint ########################################################################################################################################
    hide screen general_notifytop with dissolve
    ### Hide Hint ########################################################################################################################################

if not ep3RespondedKira:
    me "(I'd better text Kira and Robin before I do.)"
if not ep3RespondedLexi:
    me "(And answer Lexi.)"
me "(...)"
label ep3PhoneCheck:
$ ep3PhoneCheckOK = True
if not ep3RespondedKira:
    $ ep3PhoneCheckOK = False
if not ep3RespondedLexi:
    $ ep3PhoneCheckOK = False
if not ep3PhoneCheckOK:
    menu:
        "[M_03_017a]" if not ep3RespondedKira: # "I still need to reply to Kira" if not ep3RespondedKira:
            $ chat_notify_kira = False
            $ chat_sel_name = "Kira"
            $ chat_sel_icon = "cont_kira"
            call screen phone_chat_single
            "..."
            jump ep3PhoneCheck
        "[M_03_017b]" if not ep3RespondedLexi: # "I still need to reply to Lexi" if not ep3RespondedLexi:
            $ chat_notify_lexi = False
            $ chat_sel_name = "Lexi"
            $ chat_sel_icon = "cont_lexi"
            call screen phone_chat_single
            "..."
            jump ep3PhoneCheck
label ep3PhoneCheckEnd:
hide screen phone_notify_chat
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_eveninghome13 with fade
$ photoop_ep3KiraStrawNuke = False
$ ep3PhoneEventKira = False
$ ep3PhoneEventRobin = False
$ ep3PhoneEventChris = False
$ ep3PhoneEventLexi = False
$ todayIs = 6
$ clockis = [[todayIs],0,8,4,2]
hide screen phone
if ep3RespondedLexiExtended:
    $ XPlexi += 3
    if XPlexi > 25:
        $ XPlexi = 25
if "ep3_leximsg1" in cam_gallery:
    $ XPlexi += 3
    if XPlexi > 25:
        $ XPlexi = 25
me "(...)"
me "(Oh.)"
me "(I fell asleep.)"
me "(Wonder what time it is.)"
scene ep3_eveninghome16 with dissolve
me "(This was a pleasant way of waking up.)"
me "(The way their hair slightly tickles my arms, and the calming sound of their breathing.)"
me "(I could get used to this...)"
$ ep3LookedLinda = False
$ ep3LookedCece = False
label ep3LookMenu:
menu:
    "[M_03_018a]" if not ep3LookedLinda: # "Look at Linda." if not ep3LookedLinda:
        $ ep3LookedLinda = True
        scene ep3_eveninghome14 with dissolve
        me "(We had so many good times in school didn't we, Linda.)"
        me "(All the cool things we did. And the experimenting...)"
        scene ep3_eveninghome17 with dissolve
        me "(I don't think I really noticed how beautiful you've become.)"
        me "(Having you back in my arm feels very right.)"
        scene ep3_eveninghome16 with dissolve
        jump ep3LookMenu
    "[M_03_018b]" if not ep3LookedCece: # "Look at Cece." if not ep3LookedCece:
        $ ep3LookedCece = True
        scene ep3_eveninghome15 with dissolve
        me "(Cece...)"
        scene ep3_eveninghome18 with dissolve
        me "(I wouldn't have dreamt of this just a few days ago, when you were standing on the railing.)"
        scene ep3_eveninghome15 with dissolve
        me "(Now you're so close I can almost feel your lips against mine.)"
        me "(Whatever goes on in your head, I hope it's all positive now.)"
        scene ep3_eveninghome16 with dissolve
        jump ep3LookMenu
    "[M_03_018c]": # "Relax for a bit.":
        scene ep3_eveninghome16 with dissolve
        jump ep3AfterLookMenu
label ep3AfterLookMenu:
me "(I don't know what the time is, but I hope we have time to relax here some more.)"
play sound phonealarm
scene ep3_eveninghome19 with dissolve
$ clockis = [[todayIs],0,9,0,0]
if ep3RespondedLexiExtended:
    $ contact_notify_lexi = True
    $ contact_text_lexi += "\n\nLexi texted me a bit the night before we were to meet. She got a good impression by it."
    $ contact_notify_me = True
    $ contact_text_me += "\n\nI spent some time texting Lexi the night before we were to meet. I really like her, she's cool."
show screen phone
me "(Or not.)"
li "Whooo...."
li "What kind of alarm is that."
li "Shit, we have to get up."
scene ep3_eveninghome20 with dissolve
ce "*mumbles* ...just 2 more minutes..."
li "I know your 2 minutes turn into 2 hours if I don't drag your ass up right now."
scene ep3_eveninghome21 with dissolve
ce "Whatever, bitch."
li "I heard that."
scene ep3_eveninghome22 with dissolve
li "You too [name]. Rise and shine."
scene ep3_eveninghome23 with dissolve
me "Give me two minutes while the blood returns to my arms."
li "Huh?"
me "I can't feel my arms right now. You used them as pillows for a whole night."
scene ep3_eveninghome24 with fade
$ clockis = [[todayIs],1,0,0,9]
li "Ready?"
me "As ready as can b... Hang on."
scene ep3_eveninghome25 with dissolve
me "Just need to fetch my summer shirt."
scene ep3_eveninghome26 with dissolve
me "Now I'm ready."
me "Remember, we have to pick up Chris on the way."
li "What?"
stop music fadeout 3
me "I didn't tell you?"
li "*sigh*"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airport12 with fade
play music ep3_airportarrive
$ nowPlayingArtist = "Ian Post"
$ nowPlayingTitle = "Breathe"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],1,1,1,6]
ch "Wow. That's Lexi's plane? That is so cool."
ch "But where is she?"
me "Probably inside. But there's Robin and Kira. Seems they beat us to it."
ch "Can I talk to you for a second before we head over there?"
scene ep3_airport13 with dissolve
me "You two just go ahead, and we'll be right over."
ce "Sure."
ce "{size=20}Nerves?{/size}"
li "{size=20}Probably.{/size}"
scene ep3_airport14 with dissolve
me "Ok, they are over there. We are over here."
scene ep3_airport15 with dissolve
me "What's up man."
me "Don't tell me you need a paper bag..."
scene ep3_airport17 with dissolve
ch "Nah, don't worry. I'm fine. But I was thinking..."
ch "We're at an airport..."
scene ep3_airport16 with dissolve
me "Mhmm..."
scene ep3_airport17 with dissolve
ch "And how many people get to walk on the very runway of an airport?"
scene ep3_airport18 with dissolve
ch "This very airport."
scene ep3_airport19 with dissolve
ch "And there's a plane right over there..."
scene ep3_airport20 with dissolve
ch "We have to do it!"
scene ep3_airport21 with dissolve
me "Have to do what?"
scene ep3_airport22 with dissolve
ch "Do the Top Gun walk!"
scene ep3_airport21 with dissolve
me "Well..."
me "We're not pilots and we're not on an aircraft carrier."
scene ep3_airport22 with dissolve
ch "Mhmmm."
scene ep3_airport21 with dissolve
me "We don't have helmets and those cool flight suits and..."
scene ep3_airport22 with dissolve
ch "But we have the next best thing."
scene bg empty with fade
hide screen phone
$ ep3MusicDownload = False
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ clockis = [[todayIs],1,1,2,1]
me "Are you sure about this?"
ch "This is a once in a lifetime opportunity."
scene ep3_airport06 with dissolve
me "Yeah, that didn't answer my question."
scene ep3_airport07 with dissolve
ch "..."
scene ep3_airport08 with dissolve
ch "Of course I'm sure."
scene ep3_airport07 with dissolve
me "..."
scene ep3_airport06 with dissolve
me "Then let's do this."
scene ep3_airport05 with dissolve
me "Suit up, Maverick"
scene ep3_airport04 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airport03 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airport02 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airport09 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airport10 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airport11 with Dissolve(1, alpha=True)
$ renpy.pause(1)
$ renpy.movie_cutscene("imov/ep3/ep3_airportstroll.webm", delay=None, loops=0, stop_music=False)
show ep3_airport_walk03 at imgSlide_airport_dudes
show ep3_airport_walk02 at imgSlide_airport_dudes
show ep3_airport_walk01 at imgSlide_airport_dudes
show ep3_airportgirls at imgSlide_airport_girls
$ renpy.pause(5.5)
hide ep3_airport_walk01 with Dissolve(1, alpha=True)
$ renpy.pause(4.5)
hide ep3_airport_walk02 with Dissolve(1, alpha=True)
$ renpy.pause(5)
stop music fadeout 3
scene ep3_airportlexidoor07 with Dissolve(1, alpha=True)
hide ep3_airport_walk03
$ renpy.pause(1)
play music ep3_airport
$ nowPlayingArtist = "MARLOE"
$ nowPlayingTitle = "The Future Is Now"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep3_airportlexidoor06 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airportlexidoor05 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airportlexidoor04 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airportlexidoor03 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airportlexidoor02 with Dissolve(1, alpha=True)
$ renpy.pause(1)
scene ep3_airportlexidoor01 with Dissolve(1, alpha=True)
$ renpy.pause(0.5)
show ep3_hello_lexi_bg at imgSlide_airport_lexibg
show ep3_hello_lexi at imgSlide_airport_lexi
$ renpy.pause(15)
$ renpy.pause(2)
scene ep3_lexiairport00 with fade
$ renpy.pause(1)
scene ep3_lexiairport90
$ renpy.movie_cutscene("imov/ep3/ep3_lexiairport.webm", delay=None, loops=0, stop_music=False)
hide ep3_hello_lexi_bg
hide ep3_hello_lexi
hide ep3_hello_lexi_top
scene ep3_airport24 with dissolve
$ clockis = [[todayIs],1,1,2,7]
show screen phone
le "Hey guys."
scene ep3_airport23 with dissolve
le "And girls, you look amazing."
scene ep3_airport25 with dissolve
le "If you went for that grand entrance, you surely made an impression."
scene ep3_airport27 with dissolve
me "Good to see you again, Lexi."
le "Good to see you too, [name]. You look..."
scene ep3_airport26 with dissolve
le "...good."
scene ep3_airport28 with dissolve
le "And you too, Chris. You seem more relaxed."
scene ep3_airport29 with dissolve
ch "Appearances can be deceiving."
scene ep3_airport30 with dissolve
le "Feel free to climb aboard."
le "Our pilots said that we have a departure clearance in 12 minutes, so we have to be quick on the introductions."
le "Otherwise we'll be stranded here for at least an hour."
ch "I have no idea what that means..."
me "It means we get inside and continue introductions there, Chris."
ch "Sounds good to me."
scene ep3_airport31 with dissolve
ki "Hi, I'm Kira."
if ep3LexiEndCallKira:
    le "Ah. The sexy dreams girl. Nice to meet you."
    scene ep3_airport32 with dissolve
    ki "Oh... Never mention that again to anybody, please."
    ki "It just slipped out..."
else:
    le "Nice to meet you Kira. You look great in hotpants."
    scene ep3_airport32 with dissolve
    ki "Oh... Now you're making me blush."
    ki "I didn't think that was possible."
le "*laughs* Don't worry. It's a good first impression."
le "Climb aboard, and make yourself at home."
scene ep3_airport34 with dissolve
if Impact_KiraRobin:
    ro "I'm Robin. Kira's girlfriend."
    scene ep3_airport33 with dissolve
    le "Lexi. And that's so beautiful. Much love to you two."
else:
    ro "I'm Robin. Kira's friend."
    scene ep3_airport33 with dissolve
    le "Lexi. A warm welcome to you."
scene ep3_airport35 with dissolve
li "I'm Linda. Long time friend of [name]."
le "Lexi. And you look beautiful."
scene ep3_airport36 with dissolve
li "*laughs* No, I'm just... me."
le "No, you're absolutely gorgeous, love. I mean it."
le "And welcome."
scene ep3_airport37 with dissolve
ce "Oh my god..."
ce "You're..."
le "Lexi..."
ce "No, I mean, you're that girl from Nite Dawg's song 'The End'."
scene ep3_airport38 with dissolve
le "Oh, him. Yes, I know Dawg."
ce "That song was so amazing."
scene ep3_airport39 with dissolve
le "Then I'll take that as a compliment sweetheart, because I wrote the song."
ce "No way!"
le "Way!"
ce "Oh, I'm Cece..."
le "That's a beautiful name, Cece. And welcome."
scene ep3_airport40 with dissolve
$ clockis = [[todayIs],1,1,4,1]
le "[name], we're just waiting for you now."
me "(Time to get aboard.)"
show screen phone_camop
$ phone_camop_screen = "ep3AirplaneSelfie"
me "(Or should I take a selfie?)"
hide screen phone_camop
$ photoop_ep3AirplaneSelfie = False
jump ep3EnterPlane
label photoop_ep3AirplaneSelfie:
play sound camerashutter
$ photoop_ep3AirplaneSelfie = True
$ cam_gallery_append_item1 = "ep3_airplaneselfie"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_airplaneselfie with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
label photoop_ep3AirplaneSelfieEnd:
hide screen phone_camop
scene ep3_airport40 with dissolve
$ cam_gallery_single = "ep3_airplaneselfie"
call screen phone_gallery_single
$ renpy.pause()
jump ep3EnterPlane
label ep3EnterPlaneNuked:
"*lots of notification noises*"
ki "*laughs* We can see your Nükes, [name]!"
le "...and yes, we're just waiting for you now!"
le "Come on, sweetheart."
label ep3EnterPlane:
$ phone_camop_screen = ""
scene ep3_airport40 with dissolve
me "Coming..."
me "(This is going to be awesome.)"
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplaneoutside01 with fade
$ renpy.pause(1)
show ep3_airplaneoutside02d at imgSlide_ep3_airplaneoutside_bg
show ep3_airplaneoutside_meanim01 at imgSlide_ep3_airplaneoutside_sp_me
show ep3_airplaneoutside_lianim at imgSlide_ep3_airplaneoutside_sp_li
show ep3_airplaneoutside_roanim at imgSlide_ep3_airplaneoutside_sp_ro
show ep3_airplaneoutside_fg at imgSlide_ep3_airplaneoutside_fg
$ renpy.pause(20)
hide ep3_airplaneoutside02d
hide ep3_airplaneoutside_meanim01
hide ep3_airplaneoutside_lianim
hide ep3_airplaneoutside_roanim
hide ep3_airplaneoutside_fg
show ep3_airplaneoutside02e at imgSlide_ep3_airplaneoutside_bg
show ep3_airplaneoutside_meanim02 at imgSlide_ep3_airplaneoutside_sp_me
show ep3_airplaneoutside_kianim at imgSlide_ep3_airplaneoutside_sp_ki
show ep3_airplaneoutside_leanim at imgSlide_ep3_airplaneoutside_sp_le
show ep3_airplaneoutside_fg at imgSlide_ep3_airplaneoutside_fg
$ renpy.pause(20)
hide ep3_airplaneoutside02e
hide ep3_airplaneoutside_meanim02
hide ep3_airplaneoutside_kianim
hide ep3_airplaneoutside_leanim
hide ep3_airplaneoutside_fg
show ep3_airplaneoutside02f at imgSlide_ep3_airplaneoutside_bg
show ep3_airplaneoutside_meceanim03 at imgSlide_ep3_airplaneoutside_sp_ce
show ep3_airplaneoutside_fg at imgSlide_ep3_airplaneoutside_fg
$ renpy.pause(20)
hide ep3_airplaneoutside02f
hide ep3_airplaneoutside_meceanim03
hide ep3_airplaneoutside_fg
scene bg empty with fade
stop music fadeout 3
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplane01 with fade
$ clockis = [[todayIs],1,1,5,8]
me "Are you ready, Chris?"
scene ep3_airplane02 with dissolve
ch "No."
scene ep3_airplane01 with dissolve
me "Wait. You've never flown before?"
scene ep3_airplane02 with dissolve
ch "No."
scene ep3_airplane01 with dissolve
me "You're in for a treat then..."
play music ep3_takeoff
$ nowPlayingArtist = "Jay Denton"
$ nowPlayingTitle = "Summer Again"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
me "...because here ... we ... go!"
play sound ep3_jetsound
scene ep3_airplane03 with dissolve
$ renpy.pause(2)
scene ep3_airplane04 with dissolve
$ renpy.pause(2)
scene ep3_airplane05 with dissolve
$ renpy.pause(2)
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplane06 with fade
$ clockis = [[todayIs],1,2,2,0]
ch "That was ... amazing."
ch "So, we're flying now?"
scene ep3_airplane08 with dissolve
me "Cruising at 45.000 feet, according to the flight screen."
scene ep3_airplane07 with dissolve
me "Open the blinds and have a look."
scene ep3_airplane09 with dissolve
me "You're like a kid at a candy store, you know that?"
scene ep3_airplane10 with dissolve
ch "Wow..."
ch "So high."
$ ep3TimePassed = 0
scene ep3_airplane22 with dissolve
me "...and he's going to be looking out that window for quite a while."
ch "{size=20}I can see the wing...{/size}"
scene ep3_airplane23 with dissolve
me "...as said..."
scene ep3_airplane24 with dissolve
$ clockis = [[todayIs],1,2,2,3]
ce "Thank you for this."
scene ep3_airplane25 with dissolve
me "Don't thank me. Thank Lexi."
scene ep3_airplane26 with dissolve
ce "Not just that... I mean... Everything, you know..."
scene ep3_airplane25 with dissolve
me "No, thank you ... for hanging in there."
scene ep3_airplane24 with dissolve
ce "Did you know that Lexi knows Nite Dawg?"
scene ep3_airplane26 with dissolve
me "Who now?"
scene ep3_airplane24 with dissolve
ce "Nite Dawg! That rapper..."
scene ep3_airplane26 with dissolve
me "Ah, the one you were talking about yesterday."
scene ep3_airplane28 with dissolve
ce "Come here..."
me "Hmmm?"
scene ep3_airplane_cececloser with dissolve
ce "Shhh. Come."
scene ep3_airplane30c with dissolve
ce "*whispers* Do you think you can ask Lexi to get Nite Dawg's autograph?"
scene ep3_airplane31c with dissolve
me "I'm sure you can ask her yourself. She'll probably be happy to help if she can."
scene ep3_airplane30c with dissolve
ce "But you've known her longer than me."
scene ep3_airplane31c with dissolve
me "About 30 minutes longer..."
scene ep3_airplane30c with dissolve
ce "And you're more daring than me."
scene ep3_airplane26 with dissolve
me "You really don't want to ask her yourself?"
scene ep3_airplane27 with dissolve
ce "Pleeeeeeeease?"
me "Sure thing."
scene ep3_airplane24 with dissolve
$ phone_task_append_item1 = "7;8;2;3;5;9;Cece;Ask if Lexi can help Cece with a Nite Dawg autograph before;Get Nite Dawg's autograph.;1"
$ phone_task_append_item2 = "7;8;2;3;5;9;Cece;Ask if Lexi can help Cece with a Nite Dawg autograph before;Get Nite Dawg's autograph.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_task_append_item1 = "7;8;2;3;5;9;Cece;(BONUS) Find a way to get Nite Dawg's autograph before;Get Nite Dawg's autograph.;1"
$ phone_task_append_item2 = "7;8;2;3;5;9;Cece;(BONUS) Find a way to get Nite Dawg's autograph before;Get Nite Dawg's autograph.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_taskadd = "New task\nHelp Cece get an autograph from Nite Dawg by asking Lexi or by some other way."
show screen phone_taskadded
ce "Thankyouthankyouthankyou."
hide screen phone_taskadded
scene ep3_airplane25 with dissolve
$ gen_notify = "You just got a {b}Bonus Opportunity{/b}. It can be solved by asking Lexi when the opportunity presents itself (failing the bonus version), or finding a way to get the autograph by other means (rewarding relationship points with Cece and a bonus scene)."
show screen general_notifytop with dissolve
me "I can't promise anything though, but I will try."
hide screen general_notifytop with dissolve
scene ep3_airplane26 with dissolve
me "I'm going to go make myself a drink. Do you want something?"
scene ep3_airplane24 with dissolve
ce "I don't have any clue about drinks. But mix me up something. I want to try."
scene ep3_airplane22 with dissolve
stop music fadeout 3
me "Chris, keep the lady company will you."
ch "One excellent company, coming right up."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplane32 with fade
play music ep3_airplaneduring
$ nowPlayingArtist = "Sajan Nauriyal"
$ nowPlayingTitle = "Guide"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
$ clockis = [[todayIs],1,2,4,9]
me "Girls."
scene ep3_airplane33 with dissolve
le "[name]. Come join us."
scene ep3_airplane34 with dissolve
ki "Don't mind me, I need to check something with Robin."
scene ep3_airplane35 with dissolve
le "Have fun, sweetheart."
scene ep3_airplane_lexiblink with dissolve
me "It's very nice to see you again, Lexi."
me "Thanks again for calling. I really appreciate it. To be honest, I know we all do."
scene ep3_airplane37 with dissolve
le "No trouble at all. In fact, I'm very glad you could come."
le "I really want to let loose and enjoy myself for a bit after this long tour. So you, and your friends, were a blessing right now."
le "I'm sure we'll get along just fine and have a good time."
scene ep3_airplane38 with dissolve
me "Looking forward to it."
me "But I feel I need to tell you a little secret."
me "It's been on my mind for some days now, and I can't really let it go."
scene ep3_airplane37 with dissolve
le "Oh?"
$ ep3ActiveTrait = "Romantic"
$ ep3ActiveTraitValue = meRomantic
if meSporty >= ep3ActiveTraitValue:
    $ ep3ActiveTrait = "Sporty"
    $ ep3ActiveTraitValue = meSporty
if meFlirty >= ep3ActiveTraitValue:
    $ ep3ActiveTrait = "Flirty"
    $ ep3ActiveTraitValue = meFlirty
if ep3ActiveTrait == "Romantic":
    scene ep3_airplane38 with dissolve
    show screen rshw with dissolve
    me "You see, I bought a beautiful woman a bottle of wine. And the two of us shared that wine and a tender moment."
    me "But that woman, no matter how beautiful she is, decided to pick up the tab behind my back."
    scene ep3_airplane39 with dissolve
    me "Surely you, seeming like a woman of exquisite taste and excellent manners can now see my predicament."
    hide screen rshw with dissolve
elif ep3ActiveTrait == "Flirty":
    scene ep3_airplane38 with dissolve
    show screen fshw with dissolve
    me "You see, I bought a bottle of wine to this gorgeous woman I once met, that we shared while the sun was setting somewhere in the world."
    me "But that woman, no matter how gorgeous she is, decided to pick up the tab behind my back."
    scene ep3_airplane39 with dissolve
    me "And you seem like a woman of the world, so I want to ask you how you would address the situation?"
    hide screen fshw with dissolve
elif ep3ActiveTrait == "Sporty":
    scene ep3_airplane38 with dissolve
    show screen sshw with dissolve
    me "You see, I bought this hot sexy woman a bottle of wine."
    me "But that woman, no matter how hot and sexy she is, decided to pick up the tab behind my back."
    scene ep3_airplane39 with dissolve
    me "A woman such as yourself can surely see the error of her ways, and offer tips on how to punish her for it."
    hide screen sshw with dissolve
scene ep3_airplane40 with dissolve
le "I'm sure that woman is fine with having paid for that wine. Or she wouldn't have done it."
scene ep3_airplane41 with dissolve
le "And in my personal, very professional opinion about that woman, is that she probably had a very good time with a charming handsome man."
scene ep3_airplane42 with dissolve
me "..."
scene ep3_airplane41 with dissolve
me "...damn... I promised myself I wouldn't choke up. But..."
menu:
    "[M_03_019a]": # "...":
        me "..."
        me "Sorry. I got lost in your eyes there for a momemt."
        scene ep3_airplane44 with dissolve
        le "I have a little something I want to show you. Come see me in the back of the plane in a few minutes, ok?"
        jump ep3AfterLexiPlaneConv
    "[M_03_019b]": # "...you are just too sweet.":
        me "...you are just too sweet."
        scene ep3_airplane44 with dissolve
        le "That reminds me. I have something I want to show you. Come see me in the back of the plane in a few minutes, ok?"
        jump ep3AfterLexiPlaneConv
    "[M_03_019c]" if not saidLexiWasBeautiful: # "...your hair got in the way." if not saidLexiWasBeautiful:
        $ XPlexi += 2
        if XPlexi > 25:
            $ XPlexi = 25
        me "...your hair got in the way."
        scene ep3_airplane39 with dissolve
        le "*laughs* U-huh. It's horrible."
        scene ep3_airplane44 with dissolve
        le "I should probably go fix it. But come see me in the back of the plane in a few minutes, ok? I got a little surprise for you."
        jump ep3AfterLexiPlaneConv
label ep3AfterLexiPlaneConv:
$ clockis = [[todayIs],1,3,0,5]
$ phone_task_append_item1 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;1"
$ phone_task_append_item2 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_taskadd = "New task\nSee Lexi in the back of the plane before 13:30, and bring her a drink she might enjoy."
show screen phone_taskadded
le "And can you be a darling and bring me a drink? The bar is at the front of the plane."
hide screen phone_taskadded
scene ep3_airplane_lexiblink with dissolve
me "Of course. Any requests? Not sure if they have wine in this shabby place."
scene ep3_airplane39 with dissolve
le "*laughs* ... of all the gin joints in all the towns in all the world, I'm glad you're in mine..."
scene ep3_airplane40 with dissolve
le "But, surprise me. Let's see if you bring something tasty."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplane49b with fade
$ clockis = [[todayIs],1,3,0,7]
me "Robin. Can you mix me up a few drinks. One for me, Cece and Lexi."
scene ep3_airplane49a with dissolve
ro "Sure thing. Anything in particular?"
me "You're the expert here. Hook us up with something good."
scene ep3_airplane49c with dissolve
ro "You got it. And Linda?"
scene ep3_airplane49b with dissolve
me "She definitely needs a cock."
scene ep3_airplane51a with dissolve
li "What the..."
me "A stiff one."
scene ep3_airplane51b with dissolve
ro "Of course. But which one."
scene ep3_airplane50a with dissolve
li "*laughs* Ah..."
li "Yes, please. Can you do a Martinez?"
scene ep3_airplane50b with dissolve
ro "Will do, honey."
scene ep3_airplane_lindablink with dissolve
me "Sitting here alone, eh?"
scene ep3_airplane55 with dissolve
li "I am. Just soaking in the good atmosphere."
scene ep3_airplane_lindablink with dissolve
me "We never really had a chance to catch up did we. Just you and me."
scene ep3_airplane55 with dissolve
li "I guess so. We always seem to get interrupted somehow."
li "But you seem to be doing good [name]. Life's been treating you well?"
scene ep3_airplane_lindablink with dissolve
me "Well, both yes and no. But I was thinking more about you. How's life been treating you?"
scene ep3_airplane55 with dissolve
li "I can't complain..."
scene ep3_airplane56 with dissolve
me "I know you well enough to know that you wouldn't complain if someone dropped a bomb on your favorite pet."
scene ep3_airplane55 with dissolve
li "You can't enjoy the present if you're stuck in the past."
scene ep3_airplane57 with dissolve
me "But they can scar..."
me "Ok, don't look now, but I think Kira and Robin are getting warmed up..."
scene ep3_airplane58 with dissolve
me "I said don't look..."
me "(I never learn...)"
scene ep3_planekirarobin with dissolve
li "(...that looks kinda hot...)"
scene ep3_airplane58 with dissolve
menu:
    "[M_03_020a]": # "Call out for Linda.":
        $ clockis = [[todayIs],1,3,1,2]
        me "Linda?"
        scene ep3_airplane62 with dissolve
        li "Huh..."
        li "Yes, they seem to be enjoying themselves."
        jump ep3GettingDrinks
    "[M_03_020b]": # "Stay silent.":
        $ ep3LindaWatchRK = True
        $ ep3TimePassed += 1
        $ clockis = [[todayIs],1,3,1,7]
        scene ep3_planekirarobin with dissolve
        li "(...shit, what's wrong with me. It takes nothing at all to get me going these days...)"
        scene ep3_airplane59 with dissolve
        li "(Mmmm...)"
        scene ep3_airplane60b with dissolve
        li "(...it's been way too long...)"
        me "You're getting turned on, aren't you..."
        scene ep3_airplane62 with dissolve
        li "And you're not?"
        scene ep3_airplane61 with dissolve
        jump ep3GettingDrinks
label ep3GettingDrinks:
menu:
    "[M_03_021a]": # "Go fetch the drinks.":
        me "I should go get the drinks."
        scene ep3_airplane69 with dissolve
        me "(Where did they go?)"
        scene ep3_airplane70 with dissolve
        me "(At least Robin finished making the drinks.)"
        scene ep3_airplane72 with dissolve
        me "(Oh, I can see where they are...)"
        menu:
            "[M_03_022a]": # "Peek":
                $ ep3TimePassed += 1
                if ep3TimePassed == 1:
                    $ clockis = [[todayIs],1,3,1,8]
                else:
                    $ clockis = [[todayIs],1,3,2,3]
                me "(This is too good to miss. And honestly, I don't think they care if they see me.)"
                scene ep3_airplane71 with dissolve
                ki "Mmmmh... Right there, right there, right there."
                ro "My god you taste amazing."
                if Impact_KiraRobin:
                    ki "And you feel amazing. I love you."
                else:
                    ki "And you feel amazing."
                jump ep3AfterPeek
            "[M_03_022b]": # "Don't peek":
                jump ep3AfterPeek
        label ep3AfterPeek:
        scene ep3_airplane70 with dissolve
        me "(I'll leave them to it...)"
        scene ep3_airplane73 with dissolve
        me "Here you go mademoiselle. One Martinez."
        scene ep3_airplane74 with dissolve
        li "You remembered."
        scene ep3_airplane68 with dissolve
        li "But do you know what drink is for rest of them?"
        scene ep3_airplane67 with dissolve
        me "Well, the Highball is obviously for me. It's a manly drink... I think... It's got scotch, so probably."
        me "The Mojito is a typical drink for those new to cocktails."
        me "And the Cosmopolitan is the all time classical woman's guilty pleasure, right?"
        scene ep3_airplane68 with dissolve
        li "Don't look at me. You're on your on on this."
        jump ep3AfterGettingDrinks
    "[M_03_021b]": # "Stay silent.":
        $ ep3TimePassed += 1
        if ep3TimePassed == 1:
            $ clockis = [[todayIs],1,3,1,8]
        else:
            $ clockis = [[todayIs],1,3,2,3]
        scene ep3_airplane63 with dissolve
        li "Let me get the drinks..."
        scene ep3_airplane64 with dissolve
        li "(...there's the drinks...)"
        li "(...but what if I...)"
        scene ep3_airplane65 with dissolve
        li "(...)"
        scene ep3_airplane66 with dissolve
        li "Drinks ahoy."
        scene ep3_airplane68 with dissolve
        li "The Martinez is for me. The rest I have no clue about."
        scene ep3_airplane67 with dissolve
        me "Well, the Highball is obviously for me. It's a manly drink... I think. It's got scotch, so probably."
        me "The Mojito is a typical drink for those new to cocktails."
        me "And the Cosmopolitan is the all time classical woman's guilty pleasure, right?"
        scene ep3_airplane68 with dissolve
        li "As said, don't look at me. You're on your own on this."
        jump ep3AfterGettingDrinks
label ep3AfterGettingDrinks:
if ep3TimePassed == 2:
    $ clockis = [[todayIs],1,3,2,9]
elif ep3TimePassed == 1:
    $ clockis = [[todayIs],1,3,2,3]
else:
    $ clockis = [[todayIs],1,3,1,8]
me "What... You don't want to get 'mixed' up in this?"
li "*laughs* You'll become an great dad some day."
me "Huh?"
li "You're already nailing the dad jokes."
me "I probably invented some of them."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_airplane75 with fade
me "(Hopefully I got the drinks right.)"
scene ep3_airplane76 with dissolve
me "Drinks incoming."
ch "What. No beer?"
me "You were too busy staring out the window, but there's probably some in the bar at the front of the plane."
scene ep3_airplane78 with dissolve
me "But I have one for you."
menu:
    "[M_03_023a]": # "Let her choose one":
        $ ep3TimePassed += 1
        $ ep3CeceDrinkMojito = False
        me "Which do you want? Your choice."
        scene ep3_airplane77 with dissolve
        if ep3TimePassed == 3:
            $ clockis = [[todayIs],1,3,3,0]
        elif ep3TimePassed == 2:
            $ clockis = [[todayIs],1,3,2,5]
        else:
            $ clockis = [[todayIs],1,3,2,3]
        ce "It's so hard to decide. I've never tried a cocktail before."
        scene ep3_airplane78 with dissolve
        ce "..."
        scene ep3_airplane77 with dissolve
        if ep3TimePassed == 3:
            $ clockis = [[todayIs],1,3,3,1]
        elif ep3TimePassed == 2:
            $ clockis = [[todayIs],1,3,2,7]
        else:
            $ clockis = [[todayIs],1,3,2,4]
        ce "The pink one looks awesome. But I'm not sure I like the smell."
        scene ep3_airplane78 with dissolve
        ce "..."
        scene ep3_airplane77 with dissolve
        if ep3TimePassed == 3:
            $ clockis = [[todayIs],1,3,3,2]
        elif ep3TimePassed == 2:
            $ clockis = [[todayIs],1,3,2,9]
        else:
            $ clockis = [[todayIs],1,3,2,5]
        ce "That green one smells good, but looks awful."
        scene ep3_airplane79 with dissolve
        if ep3TimePassed == 3:
            $ clockis = [[todayIs],1,3,3,3]
        elif ep3TimePassed == 2:
            $ clockis = [[todayIs],1,3,3,1]
        else:
            $ clockis = [[todayIs],1,3,2,6]
        ce "I'll go with the pink one. At least it looks good."
        jump ep3GiveCeceDrinkEnd
    "[M_03_023b]": # "Give her the Mojito":
        $ XPcece += 1
        if XPcece > 25:
            $ XPcece = 25
        if ep3TimePassed == 2:
            $ clockis = [[todayIs],1,3,3,1]
        elif ep3TimePassed == 1:
            $ clockis = [[todayIs],1,3,2,6]
        else:
            $ clockis = [[todayIs],1,3,2,0]
        me "One Mojito for you."
        scene ep3_airplane80 with dissolve
        ce "Thank you. Hope it tastes better than it looks."
        jump ep3GiveCeceDrinkEnd
    "[M_03_023c]": # "Give her the Cosmopolitan":
        $ ep3CeceDrinkMojito = False
        me "One Cosmopolitan for you."
        scene ep3_airplane79 with dissolve
        ce "Thank you. At least it looks good."
        jump ep3GiveCeceDrinkEnd
label ep3GiveCeceDrinkEnd:
if ep3CeceDrinkMojito:
    scene ep3_airplane81 with dissolve
    ce "{size=20}Yum... This tastes great...{/size}"
else:
    scene ep3_airplane82 with dissolve
    ce "{size=20}Eww. It looks better than it tastes..{/size}"
me "(...Lexi told me to come back here.)"
if ep3TimePassed >= 2:
    $ phone_task_append_item1 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;1"
    $ phone_task_append_item2 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;0"
    if phone_task_append_item1 in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.remove(phone_task_append_item1)
            $ phone_task_list.append(phone_task_append_item2)
            $ phTaskNotify = True
    scene ep3_airplane83 with dissolve
    me "(There she is.)"
    scene ep3_airplane84 with dissolve
    me "Here's a drink for you. Hope it's the right one."
    if ep3CeceDrinkMojito:
        scene ep3_airplane86 with dissolve
    else:
        scene ep3_airplane85 with dissolve
    le "Highball. My favorite."
    scene ep3_airplane87 with dissolve
    le "That is perfect."
    if ep3CeceDrinkMojito:
        scene ep3_airplane88 with dissolve
        le "And you're going with ... the Cosmo?"
        me "Eh... Yes. Real men wear Pink, right?"
        le "Ehm... Ok."
        scene ep3_airplane91 with dissolve
        me "Well, Cheers then."
        le "Salud."
    scene ep3_airplane88 with dissolve
    me "You had something you wanted to show me?"
    scene ep3_airplane87 with dissolve
    le "Yes. But you kinda took a while getting here."
    me "..."
    le "Don't worry, I'll show you back home."
    play sound call_sound_others
    "*Lexi's phone ringing in the background*"
    scene ep3_airplane89 with dissolve
    le "I'm sorry, I have to take this. I'll be with you right after."
    scene ep3_airplane90 with dissolve
    me "Sure thing."
    if ep3CeceDrinkMojito:
        le "Oh wait, that Cosmo was for me, wasn't it?"
        scene ep3_airplane92 with dissolve
        me "*laughs*"
elif ep3TimePassed == 1:
    $ XPlexi += 2
    if XPlexi > 25:
        $ XPlexi = 25
    $ phone_task_append_item1 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;1"
    $ phone_task_append_item2 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;2"
    if phone_task_append_item1 in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.remove(phone_task_append_item1)
            $ phone_task_list.append(phone_task_append_item2)
            $ phTaskNotify = True
    $ ep3SawLexiDress = True
    scene ep3_airplane93 with dissolve
    me "(Hopefully I'm not interrupting anything.)"
    if ep3CeceDrinkMojito:
        scene ep3_airplane94 with dissolve
    else:
        scene ep3_airplane94m with dissolve
    me "..."
    scene ep3_airplane97 with dissolve
    le "What do you think?"
    $ ep3ActiveTrait = "Romantic"
    $ ep3ActiveTraitValue = meRomantic
    if meSporty >= ep3ActiveTraitValue:
        $ ep3ActiveTrait = "Sporty"
        $ ep3ActiveTraitValue = meSporty
    if meFlirty >= ep3ActiveTraitValue:
        $ ep3ActiveTrait = "Flirty"
        $ ep3ActiveTraitValue = meFlirty
    if ep3ActiveTrait == "Romantic":
        show screen rshw with dissolve
        me "You are one breathtaking woman, Lexi."
        hide screen rshw with dissolve
    elif ep3ActiveTrait == "Sporty":
        show screen sshw with dissolve
        me "Holy shit... You look amazing."
        hide screen sshw with dissolve
    elif ep3ActiveTrait == "Flirty":
        show screen fshw with dissolve
        me "Wow. Just wow. I'm speechless."
        hide screen fshw with dissolve
    le "I mean, look at it. It's glowing."
    me "You should take a picture of this. It's so cool."
    show screen phone_camop
    $ phone_camop_screen = "ep3LexiPlaneBathroom"
    le "Yes, good idea. Can you take a picture please? And send it to me after."
    hide screen phone_camop
    jump photoop_ep3LexiGlowingEndNP
    label photoop_ep3LexiGlowing1:
    play sound camerashutter
    $ cam_gallery_append_item1 = "ep3_airplane96"
    if cam_gallery_append_item1 not in cam_gallery:
        $ cam_gallery.append(cam_gallery_append_item1)
    show bg_empty
    scene ep3_airplane96 with Fade(0, 0, 0.5, color="#ffffff")
    $ renpy.pause(0.5)
    jump photoop_ep3LexiGlowingEndPP
    label photoop_ep3LexiGlowing2:
    play sound camerashutter
    $ cam_gallery_append_item1 = "ep3_airplane97"
    if cam_gallery_append_item1 not in cam_gallery:
        $ cam_gallery.append(cam_gallery_append_item1)
    show bg_empty
    scene ep3_airplane97 with Fade(0, 0, 0.5, color="#ffffff")
    $ renpy.pause(0.5)
    jump photoop_ep3LexiGlowingEndPP
    label photoop_ep3LexiGlowingEndNP:
    hide screen phone_camop
    $ phone_camop_screen = ""
    le "No?"
    le "*laughs* You're cute when you blush by the way."
    jump photoop_ep3LexiGlowingEnd
    label photoop_ep3LexiGlowingEndPP:
    hide screen phone_camop
    le "Nice!"
    $ ep3LexiPhoto = True
    jump photoop_ep3LexiGlowingEnd
    label photoop_ep3LexiGlowingEnd:
    if ep3CeceDrinkMojito:
        scene ep3_airplane99 with dissolve
        le "And you brought me my favorite drink. I love Highball."
        le "Hope you enjoyed the view, [name]."
        me "Honestly, I loved it."
        scene ep3_airplane991 with dissolve
        me "(I need a drink...)"
        scene ep3_airplane992 with dissolve
        me "..."
        scene ep3_airplane993 with dissolve
        me "Yuck..."
    else:
        scene ep3_airplane99m with dissolve
        le "And you brought me my favorite drink. I love Highball."
        le "Hope you enjoyed the view, [name]."
        me "Honestly, I loved it."
        scene ep3_airplane991 with dissolve
        me "(I need a drink...)"
        scene ep3_airplane992m with dissolve
        me "..."
        scene ep3_airplane993m with dissolve
        me "Not too bad."
    scene ep3_airplane90 with dissolve
    me "(She is one beautiful woman.)"
    me "(And I got a good picture.)"
else:
    $ XPlexi += 2
    if XPlexi > 25:
        $ XPlexi = 25
    $ phone_task_append_item1 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;1"
    $ phone_task_append_item2 = "7;6;1;3;3;0;Lexi;See Lexi in the back of the plane before;Lexi's surprise.;2"
    if phone_task_append_item1 in phone_task_list:
        if phone_task_append_item2 not in phone_task_list:
            $ phone_task_list.remove(phone_task_append_item1)
            $ phone_task_list.append(phone_task_append_item2)
            $ phTaskNotify = True
    $ ep3SawLexiTopless = True
    scene ep3_airplane93 with dissolve
    me "(Hopefully I'm not interrupting anything.)"
    scene ep3_airplane95 with dissolve
    me "..."
    scene ep3_airplane98 with dissolve
    le "You were a bit early. But it's fine. What do you think?"
    $ ep3ActiveTrait = "Romantic"
    $ ep3ActiveTraitValue = meRomantic
    if meSporty >= ep3ActiveTraitValue:
        $ ep3ActiveTrait = "Sporty"
        $ ep3ActiveTraitValue = meSporty
    if meFlirty >= ep3ActiveTraitValue:
        $ ep3ActiveTrait = "Flirty"
        $ ep3ActiveTraitValue = meFlirty
    if ep3ActiveTrait == "Romantic":
        show screen rshw with dissolve
        me "You are one breathtaking woman, Lexi."
        hide screen rshw with dissolve
    elif ep3ActiveTrait == "Sporty":
        show screen sshw with dissolve
        me "Holy shit... You look amazing."
        hide screen sshw with dissolve
    elif ep3ActiveTrait == "Flirty":
        show screen fshw with dissolve
        me "Wow. Just wow. I'm speechless."
        hide screen fshw with dissolve
    le "I mean, look at it. It's glowing."
    if ep3CeceDrinkMojito:
        scene ep3_airplane990 with dissolve
        le "And you brought me my favorite drink. I love Highball."
        le "Hope you enjoyed the view, [name]."
        me "I did. But I'm sorry I arrived before you were fully dressed."
        le "Not to worry. I'm pretty sure you didn't see anything I didn't already show in my last music video."
        scene ep3_airplane991 with dissolve
        me "..."
        me "Oh. I'm pretty sure I did."
        scene ep3_airplane991 with dissolve
        le "*laughs*"
        me "(I need a drink...)"
        scene ep3_airplane992 with dissolve
        me "..."
        scene ep3_airplane993 with dissolve
        me "Yuck..."
    else:
        scene ep3_airplane990m with dissolve
        le "And you brought me my favorite drink. I love Highball."
        le "Hope you enjoyed the view, [name]."
        me "I did. But I'm sorry I arrived before you were fully dressed."
        le "Not to worry. I'm pretty sure you didn't see anything I didn't already show in my last music video."
        me "Oh. I'm pretty sure I did."
        scene ep3_airplane991 with dissolve
        le "*laughs*"
        me "(I need a drink...)"
        scene ep3_airplane992m with dissolve
        me "..."
        scene ep3_airplane993m with dissolve
        me "Not too bad."
    scene ep3_airplane90 with dissolve
    me "(Wow.)"
    me "(She's not shy, that's for sure.)"
scene ep3_airplane995 with dissolve
$ ep3PlanePartyReady = True
$ ep3PlanePartySpeakers = False

if MenuChoice != "HintsNone":
    ### Show Hint #######################################################################################################################################
    $ gen_notify = "Check {b}Music{/b} on your phone to start the party!"
    show screen general_notifytop with dissolve
    ### Show Hint #######################################################################################################################################

ce "Well, look at sleepyhead here."
me "Not sleepy, just soaking it all in."
scene ep3_airplane994 with dissolve
me "(Maybe I can find some way to turn this into a party?)"
scene ep3_planeparty01 with dissolve
me "(...)"
me "(Either that or I might actually get some sleep.)"
jump ep3PlaneLanded
label ep3PlaneParty:

if MenuChoice != "HintsNone":
    ### Hide Hint ########################################################################################################################################
    hide screen general_notifytop with dissolve
    ### Hide Hint ########################################################################################################################################

hide screen phone_music
scene bg empty with fade
stop music fadeout 1
$ renpy.pause(0.5)
$ renpy.pause(0.5)
if ep3PlaneSong == 2:
    play music ep1_lexi
    $ nowPlayingArtist = "Lexi Dimante"
    $ nowPlayingTitle = "Love Automatic"
    $ nowPlayingRealArtist = "Katrina Stone"
    $ nowPlayingRealTitle = "Love Automatic"
else:
    play music ep1_bowling
    $ nowPlayingArtist = "Lexi Dimante"
    $ nowPlayingTitle = "Crazy"
    $ nowPlayingRealArtist = "Lance Conrad"
    $ nowPlayingRealTitle = "Born to Drive Me Crazy"
$ ep3PlaneParty = True
$ ep3PlanePartyReady = False
me "(This ought to live things up a bit.)"
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_planeparty04 with fade
ch "Wait... Did you just..."
ch "You did, didn't you!"
scene ep3_airplane996 with dissolve
ce "See? I told you. That's the song from Lexi."
li "I love that song."
"*hears singing in the background*"
scene ep3_planeparty06 with dissolve
ce "No way!..."
li "!..."
scene ep3_planeparty05 with dissolve
ch "Hell yeah!!!"
scene ep3_planeparty03 with dissolve
$ renpy.pause()
scene ep3_planeparty02 with dissolve
ch "Oh, you're in for a ride now, [name]."
scene ep3_planeparty07 with dissolve
me "..."
scene ep3_planeparty08 with dissolve
$ renpy.pause(1)
scene ep3_planeparty08b
$ renpy.pause(1)
scene ep3_planeparty09 with dissolve
$ renpy.pause(1)
scene ep3_planeparty09b
$ renpy.pause(1)
scene ep3_planeparty10 with dissolve
$ renpy.pause(0.1)
scene ep3_planeparty10b with Dissolve(3, alpha=True)
$ renpy.pause(1)
scene ep3_planeparty11 with dissolve
me "(She's amazing.)"
scene ep3_planeparty12 with dissolve
me "(Everything she does. From the way she moves to that look in her eye.)"
scene ep3_planeparty13 with dissolve
me "(!...)"
scene ep3_planeparty14 with dissolve
le "[name]..."
le "...let loose..."
me "(Wow...)"
scene ep3_planeparty15 with dissolve
me "(This is like an on stage performance.)"
me "(Orchestrated down to the smallest detail.)"
scene ep3_planeparty16 with dissolve
le "I..."
le "...really like you..."
le "...and..."
scene ep3_planeparty17 with dissolve
le "...that tickles!"
scene ep3_planeparty18 with dissolve
le "*laughs*"
scene ep3_planeparty17 with dissolve
le "Stop it, stop it! I'm so ticklish."
scene ep3_planeparty19 with dissolve
le "..."
$ ep3DancedWithCece = False
$ ep3DancedWithLinda = False
label ep3PlanePartySelector:
menu:
    "[M_03_024a]" if not ep3DancedWithCece: # "Dance with Cece" if not ep3DancedWithCece:
        $ ep3DancedWithCece = True
        scene ep3_planeparty37 with fade
        me "Come dance with me, Cece."
        scene ep3_planeparty38 with dissolve
        ce "Nope! Not happening!"
        me "*laughs* Does it look like I'm asking?"
        scene ep3_planeparty39 with dissolve
        ce "Oh, fuck. I'm out of here."
        ch "Go get her, man!"
        me "On it!"
        scene ep3_planeparty40 with dissolve
        me "We're on a plane."
        ce "Eeeeeeek."
        scene ep3_planeparty41 with dissolve
        me "...aaaaaaaand, you're cornered."
        scene ep3_planeparty42 with dissolve
        me "So, about that dance."
        scene ep3_planeparty43 with dissolve
        ce "*laughs* There's no way."
        scene ep3_planeparty44 with dissolve
        me "One way or another, I'll get that dance."
        scene ep3_planeparty45 with dissolve
        me "So how about y..."
        scene ep3_planeparty46 with dissolve
        ce "..."
        scene ep3_planeparty47 with dissolve
        me "..."
        scene bg empty with fade
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        $ renpy.pause(0.5)
        me "(...)"
        me "(Wow...)"
        me "(...and she stopped kissing me...)"
        scene ep3_planeparty48 with dissolve
        me "Huh?"
        scene ep3_planeparty49 with fade
        ce "So much for cornered, eh?"
        scene ep3_planeparty50 with dissolve
        me "That won't work every time, you know."
        ce "*laughs*"
        jump ep3PlanePartySelector
    "[M_03_024b]" if not ep3DancedWithLinda: # "Dance with Linda" if not ep3DancedWithLinda:
        $ ep3DancedWithLinda = True
        scene ep3_planeparty24 with fade
        me "Linda... A dance?"
        scene ep3_planeparty25 with dissolve
        li "No. I'm perfectly fine here thank you."
        scene ep3_planeparty26 with dissolve
        me "*whispers* nuh-uh... Not happening."
        scene ep3_planeparty20 with dissolve
        ce "..."
        scene ep3_planeparty21 with dissolve
        me "Linda!"
        scene ep3_planeparty22 with dissolve
        li "Uaawhhhh"
        scene ep3_planeparty23 with dissolve
        me "I'm not taking no for an answer."
        me "Come move that sexy booty."
        ce "He's right!"
        scene ep3_planeparty28 with fade
        li "See? I'm dancing now. Happy?"
        scene ep3_planeparty27 with dissolve
        me "Aren't you?"
        scene ep3_planeparty29 with dissolve
        li "..."
        li "I am..."
        scene ep3_planeparty27 with dissolve
        me "Then I'm happy too."
        scene ep3_planeparty28 with dissolve
        li "Do you remember our special dance?"
        scene ep3_planeparty27 with dissolve
        me "I'm quite sure I do."
        scene ep3_planeparty30 with dissolve
        li "Show me what you've got then."
        scene ep3_planeparty31 with dissolve
        me "..."
        scene ep3_planeparty32 with dissolve
        li "Oh, I feel you alright."
        li "And for the grand finale..."
        scene ep3_planeparty33 with dissolve
        li "Hit it baby..."
        scene ep3_planeparty36 with hpunch
        me "..."
        scene ep3_planeparty34 with dissolve
        li "Hnngh..."
        scene ep3_planeparty35 with dissolve
        li "You {b}did{/b} remember..."
        jump ep3PlanePartySelector
    "[M_03_024c]": # "End Scene":
        jump ep3PlaneLanding
label ep3PlaneLanding:
if Impact_KiraRobin:
    scene ep3_planeparty51 with dissolve
    ki "{size=20}...yes...{/size}"
    ki "...yes..."
    ki "...{b}yes{/b}..."
    ki "...{b}Mile high club, Baby!{/b}"
$ ep3PlanePartyReady = False
label ep3PlaneLanded:
$ ep3PlanePartyReady = False
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ nukeStoriesAdd1 = "10;You;ep3_airplaneselfie;Having the time of my life."
$ nukeStoriesAdd2 = "11;You;ep3_airplaneselfie;Yes, this is Lexi's plane. Yes, she's inside. Yes, I'm the luckiest guy alive."
if nukeStoriesAdd1 in nukeStories:
    $ nukeCommentsAdd = "10;1001;OfficialLexi;Come one hun, just waiting for you now. <3"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "10;1002;AssesAndBreasts;Did you by any chance bring any motion sickness tablets? Nvm, I'll ask you when you get in here."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "10;1003;BlackBeauty;And yes, I'm fucking envious right now. Knock one back for me."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "10;1004;Drifty;I have I feeling you're in for an adventure. Have fun. :)"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
if nukeStoriesAdd2 in nukeStories:
    $ nukeCommentsAdd = "11;1101;OfficialLexi;And yes, we're just waiting for you now. <3"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "11;1102;AssesAndBreasts;Did you by any chance bring any motion sickness tablets? Nvm, I'll ask you when you get in here."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "11;1103;BlackBeauty;And yes, I'm fucking envious right now. Knock one back for me."
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
    $ nukeCommentsAdd = "11;1104;Drifty;I have I feeling you're in for an adventure. Have fun. :)"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
scene ep3_landing02 with fade
$ clockis = [[todayIs],1,5,3,7]
$ contact_notify_me = True
$ contact_text_me += "\n\nIt was a nice trip on the plane. I got to spend a bit of time with everyone."
if ep3TimePassed == 1:
    $ contact_text_me += " Lexi showed me her new ... neon dress. Somehow, I feel that what she really wanted to show me was the parts the dress didn't cover."
elif ep3TimePassed == 0:
    $ contact_text_me += " Lexi showed me her new ... neon dress. But I arrived a bit early, so she hadn't fully dressed yet. She didn't seem to mind at all."
    $ contact_text_me += " Though, somehow I feel that what she really wanted to show me was what the 'dress' didn't cover."
if ep3PlaneParty:
    $ contact_text_me += "\n\nI also put on some Lexi music on the plane's main speakers, which brought us some good fun."
$ contact_notify_cece = True
$ contact_text_cece += "\n\nShe really seem to like this Nite Dawg, and on the plane she asked me to somehow get his autograph. From Lexi."
$ contact_notify_lexi = True
$ contact_text_lexi += "\n\nIt's very easy to talk to Lexi, she's very used to socializing. At least she's not shy."
if ep3TimePassed == 1:
    $ contact_text_lexi += " Further emphasized by the fact that she showed off her ... dress ... for me. That thing did not cover a lot."
elif ep3TimePassed == 0:
    $ contact_text_lexi += " Further emphasized by the fact that she showed off her ... dress ... for me. The fact that she was topless didn't seem to bother her either."
stop music fadeout 7
ch "Is that..."
scene ep3_landing03 with dissolve
le "...our ride, yes."
scene ep3_landing04 with dissolve
le "Kevin! So good to see you again."
ke "Miss Dimante. You're breathtaking as always."
scene ep3_landing07 with dissolve
me "Don't tell me... Limo, right?"
ch "...not just any limo..."
scene ep3_landing05 with dissolve
me "Wow..."
le "...and how many times have I told you, call me Lexi."
ke "As you wish, Lexi."
scene ep3_landing06 with dissolve
le "Kevin, this is my friend [name]."
ke "A pleasure to meet you, Sir."
if meRomantic >= 2:
    $ ep3SaidHiToKevin = True
    show screen rshw with dissolve
    $ XPlexi += 2
    if XPlexi > 25:
        $ XPlexi = 25
    scene ep3_landing08 with dissolve
    me "A pleasure to meet you too, Kevin. And use [name] please."
    ke "That I can do, [name]."
    hide screen rshw with dissolve
scene ep3_landing10 with dissolve
me "Wow. What a car..."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_limo01 with fade
$ clockis = [[todayIs],1,6,1,5]
le "We need some good music in here."
scene ep3_limo02 with dissolve
ro "How about ... Michael Shynes?"
scene ep3_limo03 with dissolve
ch "Yes! That guy is a national treasure. If he doesn't get the mood up, nobody will."
scene ep3_limo04 with dissolve
ki "Don't shame the Shynes."
scene ep3_limo05 with dissolve
$ gen_notify = "Feel free to watch them sing the intro to the song, or advance as you normally would.\n\nSpace or Click to start."
show screen general_notifytop with dissolve
li "Ok, let me see if I got this right."
hide screen general_notifytop with dissolve
play music ep3_limo
$ nowPlayingArtist = "Michael Shynes (feat. Wholm and Cageman)"
$ nowPlayingTitle = "235 Are You Alive"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""

$ renpy.pause(1.95)
scene ep3_song01_ki01_i with dissolve
$ renpy.pause(0.30)
scene ep3_song01_ki02_ee_unclap
$ renpy.pause(0.45)
scene ep3_song01_ki03_m
$ renpy.pause(0.15)
scene ep3_song01_ki02_ee_unclap
$ renpy.pause(0.45)
scene ep3_song01_ki03_m
$ renpy.pause(0.15)
scene ep3_song01_ki02_ee
$ renpy.pause(0.20)
scene ep3_song01_ki04_o
$ renpy.pause(0.30)
scene ep3_song01_ki04_o_unclap
$ renpy.pause(0.55)
scene ep3_song01_ki04_o
$ renpy.pause(0.60)
scene ep3_song01_ki04_o_unclap
$ renpy.pause(0.55)
scene ep3_song01_ki04_o
$ renpy.pause(0.60)
scene ep3_song01_ki04_o_unclap
$ renpy.pause(0.30)

scene ep3_song02_le01_a
$ renpy.pause(0.50)
scene ep3_song02_le02_o
$ renpy.pause(0.30)
scene ep3_song02_le03_ee
$ renpy.pause(0.50)
scene ep3_song02_le04_i
$ renpy.pause(0.30)
scene ep3_song02_le05_a
$ renpy.pause(2.70)

scene ep3_song03_ro01_ee
$ renpy.pause(0.50)
scene ep3_song03_ro02_ou
$ renpy.pause(0.30)
scene ep3_song03_ro03_fi
$ renpy.pause(0.40)
scene ep3_song03_ro04_ee
$ renpy.pause(0.70)
scene ep3_song03_ro05_of
$ renpy.pause(0.70)
scene ep3_song03_ro05_uu
$ renpy.pause(2.10)

scene ep3_song04_me02_a
$ renpy.pause(0.30)
scene ep3_song04_me01_thi
$ renpy.pause(0.30)
scene ep3_song04_me02_a
$ renpy.pause(0.30)
scene ep3_song04_me03_b
$ renpy.pause(0.30)
scene ep3_song04_me04_e
$ renpy.pause(0.30)
scene ep3_song04_me05_ou
$ renpy.pause(0.30)
scene ep3_song04_me06_are
$ renpy.pause(4.90)

scene ep3_song05_li01_two
$ renpy.pause(0.30)
scene ep3_song05_li02_three
$ renpy.pause(0.30)
scene ep3_song05_li03_five
$ renpy.pause(0.60)
scene ep3_song05_li04_are
$ renpy.pause(0.30)
scene ep3_song05_li05_you
$ renpy.pause(0.30)
scene ep3_song05_li06_alive
$ renpy.pause(0.60)
scene ep3_song05_li07_end
$ renpy.pause(2.10)

scene ep3_song06_ki01_four
$ renpy.pause(0.60)
scene ep3_song06_ki02_six
$ renpy.pause(0.60)
scene ep3_song06_ki03_how
$ renpy.pause(0.60)
scene ep3_song06_ki04_it
$ renpy.pause(2.80)

scene ep3_song07_ce01_seven
$ renpy.pause(0.60)
scene ep3_song07_ce02_two
$ renpy.pause(0.60)
scene ep3_song07_ce03_et
$ renpy.pause(0.50)
scene ep3_song07_ce03_you
$ renpy.pause(0.60)

scene ep3_song08_chrisfinal
ch "...is something I can't seem to do. *'slightly' out of tune*"
me "..."

scene ep3_limo06 with fade
show screen phone_camop
$ phone_camop_screen = "ep3LimoLinda"
$ ep3LimoLindaPic = True
$ renpy.pause()
hide screen phone_camop
jump photoop_ep3LimoLindaEnd
label photoop_ep3LimoLinda:
play sound camerashutter
$ XPlinda += 1
if XPlinda > 25:
    $ XPlinda = 25
$ cam_gallery_append_item1 = "ep3_limo06"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_limo06 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
jump photoop_ep3LimoLindaEnd
label photoop_ep3LimoLindaEnd:
$ phone_camop_screen = ""
hide screen phone_camop

scene ep3_limo07 with fade
show screen phone_camop
$ phone_camop_screen = "ep3LimoRobin"
$ ep3LimoRobinPic = True
$ renpy.pause()
hide screen phone_camop
jump photoop_ep3LimoRobinEnd
label photoop_ep3LimoRobin:
play sound camerashutter
$ cam_gallery_append_item1 = "ep3_limo07"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_limo07 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
jump photoop_ep3LimoRobinEnd
label photoop_ep3LimoRobinEnd:
$ phone_camop_screen = ""
hide screen phone_camop

scene ep3_limo08 with fade
show screen phone_camop
$ phone_camop_screen = "ep3LimoCece"
$ ep3LimoCecePic = True
$ renpy.pause()
hide screen phone_camop
jump photoop_ep3LimoCeceEnd
label photoop_ep3LimoCece:
play sound camerashutter
$ cam_gallery_append_item1 = "ep3_limo08"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_limo08 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
jump photoop_ep3LimoCeceEnd
label photoop_ep3LimoCeceEnd:
$ phone_camop_screen = ""
hide screen phone_camop

scene ep3_limo09 with fade
show screen phone_camop
$ phone_camop_screen = "ep3LimoLexi"
$ ep3LimoLexiPic = True
$ renpy.pause()
hide screen phone_camop
jump photoop_ep3LimoLexiEnd
label photoop_ep3LimoLexi:
play sound camerashutter
$ cam_gallery_append_item1 = "ep3_limo09"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_limo09 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
jump photoop_ep3LimoLexiEnd
label photoop_ep3LimoLexiEnd:
$ phone_camop_screen = ""
hide screen phone_camop

scene ep3_limo10 with fade
show screen phone_camop
$ phone_camop_screen = "ep3LimoKira"
$ ep3LimoKiraPic = True
$ renpy.pause()
hide screen phone_camop
jump photoop_ep3LimoKiraEnd
label photoop_ep3LimoKira:
play sound camerashutter
$ cam_gallery_append_item1 = "ep3_limo10"
if cam_gallery_append_item1 not in cam_gallery:
    $ cam_gallery.append(cam_gallery_append_item1)
show bg_empty
scene ep3_limo10 with Fade(0, 0, 0.5, color="#ffffff")
$ renpy.pause(0.5)
jump photoop_ep3LimoKiraEnd
label photoop_ep3LimoKiraEnd:
$ phone_camop_screen = ""
hide screen phone_camop

scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_lexis01 with fade
$ nukeStoriesAdd = "14;Lexi;ep3_nuke_lexilimo;This guy!"
if nukeStoriesAdd not in nukeStories:
    $ nukeStories.append(nukeStoriesAdd)
$ nukeCommentsAdd = "14;1401;Lexi's Panty Sniffer;Hook me up with the goods, will you?"
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "14;1402;Lexi4Life;Noooo. Lexi... Don't go find yourself a boyfriend now. You haven't even met me yet."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "14;1403;UnOfficialLexi;That is so sweet."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "14;1404;OfficialNDawg;You're awesome, girl. Best of luck."
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
$ nukeCommentsAdd = "14;1405;SixFeetUnder;OMG. Nite Dawg. You're amazing!"
if nukeCommentsAdd not in nukeComments:
    $ nukeComments.append(nukeCommentsAdd)
if ep3ReplySteph == 1:
    $ nukeCommentsAdd = "13;1307;StephPriv;@LeapOfFaith. Thank you. For what it's worth, I wish I'd handled things different. XO"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
if ep3ReplySteph == 2:
    $ nukeCommentsAdd = "13;1308;StephPriv;@LeapOfFaith. It's too late for me to offer anything else than apologies. I'm sorry. But I heard you're doing good now. That makes me happy. XO"
    if nukeCommentsAdd not in nukeComments:
        $ nukeComments.append(nukeCommentsAdd)
$ clockis = [[todayIs],1,7,0,1]
le "Well, this is my humble home. Welcome."
scene ep3_lexis02 with dissolve
me "I'm not sure humble is the right word you're looking for."
scene ep3_lexis03 with dissolve
ce "Wow. Come check out the pool!"
scene ep3_lexis04 with dissolve
li "This is a dream come true."
scene ep3_lexis05 with dissolve
ki "Looks delicious."
ch "Can't wait to bomb that pool."
scene ep3_lexis06 with dissolve
ro "Or just lay there for days, sipping on something good."
stop music fadeout 5
scene ep3_lexis07 with dissolve
le "Make yourself at home. Do as you would do at your own place."
le "My bedroom is upstairs, but all the guestrooms are downstairs."
le "The luggage should be down there already, so feel free to pick out rooms and get comfortable."
le "I'm going to crash here, while you guys get sorted out."
scene ep3_lexis08 with dissolve
le "[name], would you like to accompany me?"
play music ep3_lexicalm
$ nowPlayingArtist = "The Talbott Brothers"
$ nowPlayingTitle = "Ordinary"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
menu:
    "[M_03_025a]" if XPlexi >= 20: # "Aww ... now they get all the best beds." if XPlexi >= 20:
        $ ep3LexiToldMCToSleepInHerBed = True
        me "Awww ... now they get all the best beds."
        le "*laughs* Sleep in my bed then."
        scene ep3_lexis09 with dissolve
        me "I was joking ... wait what?"
        le "I was joking too..."
        le "...or was I?"
        me "..."
        me "(That is going to keep me awake all night...)"
        jump ep3AfterLexiBedTalk
    "[M_03_025b]": # "Of course":
        me "Of course."
        jump ep3AfterLexiBedTalk
label ep3AfterLexiBedTalk:
scene ep3_lexis09 with dissolve
le "I kinda feel like a bad host right now, but I'm shot. We should have a party or something."
me "I'm sure we'll manage just fine without a party right now. Jet-lag is going to set in any time anyway."
scene ep3_lexis10 with dissolve
$ clockis = [[todayIs],1,7,2,9]
le "Those boots are wonderful to put on, but so fantastic to get out of afterwards."
scene ep3_lexis11 with dissolve
me "You said you've been away for a full year?"
scene ep3_lexis12 with dissolve
le "Yes. Well, 364 days. But I'll count that as a year."
scene ep3_lexis11 with dissolve
me "Sounds exhausting."
scene ep3_lexis12 with dissolve
le "Not really. The tour itself is a blast. Time flies by, and you're surrounded by people who love you. Literally."
le "The exhausting part is getting the list of concerts you are going to do before the tour."
scene ep3_lexis17 with dissolve
le "When I see that list, I ... cry."
le "Some superstar, eh?"
scene ep3_lexis13 with dissolve
me "We come from two different worlds, Lexi. It's hard to imagine."
scene ep3_lexis15 with dissolve
le "Tell me a bit about yourself please. I would love to hear."
le "Any girlfriends?"
scene ep3_lexis_lexiblink with dissolve
me "Nope."
scene ep3_lexis15 with dissolve
le "Just nope?"
scene ep3_lexis_lexiblink with dissolve
me "I lost my girlfriend a few years ago. It took a long time to get over."
me "And haven't really found a new one yet. Although there's somebody peaking my interest though."
scene ep3_lexis18 with dissolve
le "Hmmm..."
le "And work?"
scene ep3_lexis_lexiblink with dissolve
me "I wish I could tell you something exciting. But most of my life is as boring as it gets."
me "Finished school and got a job straight away."
me "I've been working in the sewers for a few years. Let's just say it's most likely a whole lot less glamorous than what you are used to."
menu:
    "[M_03_026a]": # "Don't tell her you got fired.":
        jump ep3LexisAfterJobTalk
    "[M_03_026b]": # "Tell her you got fired.":
        $ ep3ToldLexiFired = True
        me "Although I got fired a few days back. So right now I'm actually not doing anything."
        me "..."
        scene ep3_lexis15 with dissolve
        le "What ... You thought I was going to think differently about you because you got fired?"
        scene ep3_lexis_lexiblink with dissolve
        me "I wasn't sure to be honest."
        scene ep3_lexis15 with dissolve
        $ meRomantic += 1
        show screen rlvl with dissolve
        le "And still you told me."
        le "If anything, that tells me a lot about you as a person. Much more then you going on about how normal your job is."
        hide screen rlvl with dissolve
        jump ep3LexisAfterJobTalk
label ep3LexisAfterJobTalk:
scene ep3_lexis15 with dissolve
le "It's not where you work that counts, but who you are as a person."
le "Although, it doesn't sound that pleasurable."
scene ep3_lexis_lexiblink with dissolve
me "It's not that bad really. You get used to it..."
scene ep3_lexis17 with dissolve
me "...and there's no Paparazzi down there."
scene ep3_lexis16 with dissolve
le "*laughs* Every job has its perks."
scene ep3_lexis18 with dissolve
le "Would you like to do me a tiny favor?"
me "..."
le "Can you close your eyes for just a little bit?"
me "Oh, now I'm terrified..."
le "I just want to test something..."
scene bg empty with fade
hide screen phone
$ renpy.pause(0.5)
$ gen_notify = "{b}Intimacy Control{/b}.\nClick on the words best suited to your feelings to advance the scene."
show screen general_notifytop with dissolve
$ renpy.pause()
hide screen general_notifytop with dissolve
label ep3RPLexiStart:
"{color=#ffff55}... as you close your eyes, you instantly feel {a=jump:ep3RPLexiNervous}nervous{/a}/{a=jump:ep3RPLexiCalm}calm{/a}.{/color}"
jump ep3RPLexiStart
label ep3RPLexiNervous:
"{color=#ffff55}Should you be doing this? Because you really like {a=jump:ep3RPLexiHer}her{/a}/{a=jump:ep3RPLexiOther}someone else{/a}.{/color}"
jump ep3RPLexiNervous
label ep3RPLexiCalm:
"{color=#ffff55}Lowering your shoulders, you accept the feeling... silently awaiting {a=jump:ep3RPLexiBreath}her next move{/a}.{/color}"
jump ep3RPLexiCalm
label ep3RPLexiHer:
"{color=#ffff55}Savoring the moment, and feeling the expectation of {a=jump:ep3RPLexiBreath}what comes next{/a}.{/color}"
jump ep3RPLexiHer
label ep3RPLexiOther:
"{color=#ffff55}But the sweet smell of her perfume is overwhelming, and you feel your whole {a=jump:ep3RPLexiBreath2}body relaxing.{/a}{/color}"
jump ep3RPLexiOther
label ep3RPLexiBreath:
"{color=#ffff55}Suddenly you can feel a small, almost unnoticeable breath of air against your lips, sending jolts of {a=jump:ep3RPLexiBrush}pleasure{/a} through the entirety of your spine.{/color}"
jump ep3RPLexiBreath
label ep3RPLexiBreath2:
"{color=#ffff55}Suddenly you can feel a small, almost unnoticeable breath of air against your lips, almost giving you a {a=jump:ep3RPLexiBrush2}jump scare{/a}.{/color}"
jump ep3RPLexiBreath2
label ep3RPLexiBrush2:
"{color=#ffff55}The breath of air gets warmer, until it is replaced by the softest lips you have ever felt. You instantly feel that this is {a=jump:ep3RPLexiRefused}wrong{/a}.{/color}"
jump ep3RPLexiBrush2
label ep3RPLexiBrush:
"{color=#ffff55}The breath of air gets warmer, until it is replaced by the softest lips you have ever felt. You just can't help {a=jump:ep3RPLexiAroused}being aroused{/a}/{a=jump:ep3RPLexiHorny}wanting more{/a}.{/color}"
jump ep3RPLexiBrush
label ep3RPLexiAroused:
"{color=#ffff55}Your lips part as her tongue slides past them, seeking yours. In eager anticipation, your own tongue meets hers and you do a sensual dance visual to nobody but the two of yours {a=jump:ep3RPLexiKiss}imagination{/a}/{a=jump:ep3RPLexiSexual}sexual desires{/a}.{/color}"
jump ep3RPLexiAroused
label ep3RPLexiRefused:
"{color=#ffff55}Knowing well you have feelings for someone else, you hesitate, and {a=jump:ep3RPLexiRefuseEnd}open your eyes{/a}.{/color}"
jump ep3RPLexiRefused
label ep3RPLexiHorny:
"{color=#ffff55}In eager anticipation, your tongue welcomes hers and intertwines. You can't help but {a=jump:ep3RPLexiSexual}getting harder{/a}/{a=jump:ep3RPLexiHoldback}feeling you should hold back{/a}.{/color}"
jump ep3RPLexiHorny
label ep3RPLexiSexual:
scene ep3_lexis37
$ renpy.movie_cutscene("imov/ep3/ep3_lexikiss.webm", delay=None, loops=0, stop_music=False)
"{color=#ffff55}Your arms seek her, as hers seeks you. You move your arms up her body, brushing her {a=jump:ep3RPLexiSexual2}breasts{/a}, until you feel them pressing against you.{/color}"
jump ep3RPLexiSexual
label ep3RPLexiSexual2:
scene ep3_lexis34 with dissolve
"{color=#ffff55}Moving towards her neck, where you embrace her, deepening {a=jump:ep3RPLexiNiceEnd}the kiss{/a}.{/color}"
jump ep3RPLexiSexual2
label ep3RPLexiHoldback:
scene ep3_lexis37
$ renpy.movie_cutscene("imov/ep3/ep3_lexikiss.webm", delay=None, loops=0, stop_music=False)
"{color=#ffff55}But you can't bring yourself to push her back. Soon you feel her {a=jump:ep3RPLexiHoldback2}breasts{/a} pressing against you.{/color}"
jump ep3RPLexiHoldback
label ep3RPLexiHoldback2:
scene ep3_lexis34 with dissolve
"{color=#ffff55}The {a=jump:ep3RPLexiNiceEnd}embrace{/a} is firm, as you explore her with your {a=jump:ep3RPLexiNiceEnd}senses{/a}.{/color}"
jump ep3RPLexiHoldback2
label ep3RPLexiKiss:
scene ep3_lexis37
$ renpy.movie_cutscene("imov/ep3/ep3_lexikiss.webm", delay=None, loops=0, stop_music=False)
"{color=#ffff55}You feel her arms moving up your body, her {a=jump:ep3RPLexiKiss2}breasts{/a} pressing gently against you.{/color}"
jump ep3RPLexiKiss
label ep3RPLexiKiss2:
scene ep3_lexis34 with dissolve
"{color=#ffff55}You're lost in her kiss. Your senses {a=jump:ep3RPLexiNiceEnd}overwhelmed{/a}, as they were caught completely off guard.{/color}"
jump ep3RPLexiKiss2
label ep3RPLexiNiceEnd:
scene ep3_lexis20 with dissolve
"{color=#ffff55}As the voices in the background gets louder, you both realize the others are coming back. You let go slowly, feeling her breath on your lips one more time.{/color}"
jump ep3RPLexiEnd
label ep3RPLexiRefuseEnd:
scene ep3_lexis20 with dissolve
"{color=#ffff55}You let go, trying to find a way to explain why. But the voices in the background gets louder, interrupting you.{/color}"
jump ep3RPLexiEnd
label ep3RPLexiEnd:
scene ep3_lexis35 with dissolve
"{color=#ffff55}And for a moment, you seem to spot the woman behind the superstar...{/color}"
scene ep3_lexis36 with Dissolve(3, alpha=True)
"{color=#ffff55}...and then it's gone.{/color}"
scene ep3_lexis19 with fade
le "Shame..."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
show screen phone
$ clockis = [[todayIs],1,7,3,6]
if ep3RejectedKira:
    scene ep3_lexis24 with dissolve
    ce "...then the guy goes... 'what moment...'"
    scene ep3_lexis25 with dissolve
    le "That sounds like a moment to me."
    scene ep3_lexis29 with dissolve
    li "Definitely a moment."
    scene ep3_lexis26 with dissolve
    ce "..."
    scene ep3_lexis27 with dissolve
    ch "What moment. I don't get it."
    scene ep3_lexis24 with dissolve
    ce "Men..."
else:
    scene ep3_lexis21 with fade
    ki "...then we both finish at the same time. Dual orgasm!"
    ki "And two minutes later, the guy's ready to go again!"
    scene ep3_lexis22 with dissolve
    ro "..."
    scene ep3_lexis23 with dissolve
    le "Sounds like a keeper to me."
    scene ep3_lexis28 with dissolve
    ch "..."
    scene ep3_lexis30 with dissolve
    ki "My thoughts exactly."
scene ep3_lexis31 with dissolve
$ contact_notify_me = True
$ contact_text_me += "\n\nWhen we finally got to Lexi's house in the evening - or mansion more like it, we had a little chat just the two of us."
$ contact_text_me += " For some reason she wanted to surprise kiss me, real french style. Even if it was ... enjoyable, I'm not too sure how I feel about it."
$ contact_notify_lexi = True
$ contact_text_lexi += "\n\nAt her place, she wanted some alone time just for the two of us. She kissed me."
$ clockis = [[todayIs],1,8,3,3]
me "I think I'll leave you with your moments. Just going to stretch my legs a bit."
scene ep3_lexis32 with dissolve
ch "You ok there, my dude?"
scene ep3_lexis33 with dissolve
me "Better than in a long time, man."
scene bg empty with fade
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_lexiledge13 with dissolve
me "(This place is fantastic. It's completely unreal.)"
me "(And she kissed me ... she's so sweet ... sensual ... flirty.)"
me "(Is it who she is, or does she want something more.)"
scene ep3_lexiledge14 with fade
me "(What a view)."
me "(But the smell...)"
scene ep3_lexiledge15 with dissolve
me "(Why have I been smelling rose and jasmin the whole day...)"
me "(Oh ... the shirt...)"
scene ep3_lexiledge16 with dissolve
me "(I guess she wore it last.)"
scene ep3_lookatmc01 with dissolve
ce "You're really good friends, aren't you."
scene ep3_lookatmc02 with dissolve
ch "We've been best buddies since school, my young lady."
scene ep3_lookatmc01 with dissolve
ce "Yeah, Linda told me. About all the crazy stuff you did."
scene ep3_lookatmc04 with dissolve
ch "Those years were the best. We did all kinds of weird things. Always having a blast. [name], me, Linda."
ce "...and Stephanie?"
scene ep3_lookatmc01 with dissolve
ch "..."
scene ep3_lookatmc03 with dissolve
ce "...why do I feel like there's something going on every time her name is mentioned."
scene ep3_lookatmc01 with dissolve
ch "No... It's about time I stopped dodging the bullet just because of her..."
scene ep3_lookatmc03 with dissolve
ce "Things were that bad?"
scene ep3_lookatmc02 with dissolve
ch "No. Things were great."
ch "They just ended badly."
scene ep3_lookatmc01 with dissolve
ch "One day suddenly she was gone."
ch "There was no preceding event to suggest she would leave. Still, suddenly she did. For two whole years."
scene ep3_lookatmc02 with dissolve
ch "I have no idea why she left. But the saddest thing is that knowing her, she probably had a good reason."
ch "I just wish she had said something before she left."
ce "..."
scene ep3_lookatmc01 with dissolve
ce "She loved him?"
ch "I know she did."
scene ep3_lookatmc03 with dissolve
ce "And he loved her?"
scene ep3_lookatmc02 with dissolve
ch "He did. They were perfect for each other."
ch "I honestly thought they would grow old together."
scene ep3_lookatmc04 with dissolve
ch "That many years from now we would sit at his porch talking about the good old times, while Steph would bring us both a refreshing cold one."
ch "She was compassionate, friendly, lovingly, nice... Always there. A {b}wonderful{/b} friend."
scene ep3_lookatmc01 with dissolve
ch "But she hurt my {b}best{/b} friend."
stop music fadeout 7
scene ep3_lookatmc05 with Dissolve(3, alpha=True)
ce "..."
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
$ renpy.pause(0.5)
scene ep3_lexiledge17 with dissolve
$ ep3CanReplySteph = False
$ clockis = [[todayIs],1,8,4,5]
me "..."
scene ep3_lexiledge31a with dissolve
me "Hmmm?"
scene ep3_lexiledge30a with dissolve
me "What's this?"
me "Oh, this has got to be old."
scene ep3_lexiledge25f with dissolve
me "Wonder what it is."
play music ep3_epilogue
$ nowPlayingArtist = "Faith Richards"
$ nowPlayingTitle = "Blue (Alternative Version)"
$ nowPlayingRealArtist = ""
$ nowPlayingRealTitle = ""
scene ep3_stephletter16 with Fade(0, 0, 1, color="#ffffff")
$ renpy.pause(3)
scene ep3_lexiledge25f with Fade(0, 0, 1, color="#ffffff")
$ renpy.pause(1)
scene ep3_lexiledge23f with dissolve
me "..."
scene ep3_stephletter05 with fade
st "My dear..."
scene ep3_stephletter03 with dissolve
st "I'm writing this letter, because I don't think I'll be able to say what I should have said a long time ago."
scene ep3_stephletter04 with dissolve
st "Not while looking into your beautiful eyes."
scene ep3_stephletter02 with dissolve
st "But I've made a really big mess, one I have to sort out."
scene ep3_stephletter01 with dissolve
st "*inhales*"
st "*exhales*"
scene ep3_stephletter06 with dissolve
st "It means I have to go away for a while. I don't know for how long. A month, two months, or even longer. Much longer."
scene ep3_stephletter07 with dissolve
st "I don't even know myself. And what I do know, I was not allowed to tell you. I shouldn't even write this letter, but I have to."
scene ep3_stephletter06 with dissolve
st "..."
scene ep3_stephletter07 with dissolve
st "I'm not afraid to show them how I really feel about you any more."
scene ep3_stephletter10 with dissolve
st "I love y..."
scene ep3_stephletter08 with dissolve
st "(dontcrydontcrydontcry...)"
scene ep3_stephletter09 with dissolve
st "..."
scene ep3_stephletter08 with dissolve
st "(keep going...)"
scene ep3_stephletter06 with dissolve
st "...more than you'll ever know. Knowing that I am hurting you is a burden almost too heavy to carry."
scene ep3_stephletter07 with dissolve
st "But I will do it again in a heartbeat, as long as you're safe."
scene ep3_stephletter13 with dissolve
st "I will return, and when I do I will explain everything. And I hope I can jump into your arms when I do."
scene ep3_stephletter11 with Dissolve(3, alpha=True)
st "I'm so, so, sorry baby."
scene ep3_stephletter12 with Dissolve(3, alpha=True)
st "Eternally yours."
scene ep3_stephletter14 with dissolve
st "..."
scene ep3_stephletter15 with dissolve
st "..."
scene ep3_lexiledge24f with fade
me "Stephanie."
scene ep3_lexiledge27f with dissolve
$ phone_task_append_item1 = "7;7;2;3;5;9;Stephanie;Hear Stephanie out before;You can't move forward, unless you close the past.;1"
$ phone_task_append_item2 = "7;7;2;3;5;9;Stephanie;Hear Stephanie out before;You can't move forward, unless you close the past.;2"
if phone_task_append_item1 not in phone_task_list:
    if phone_task_append_item2 not in phone_task_list:
        $ phone_task_list.append(phone_task_append_item1)
        $ phTaskNotify = True
$ phone_taskadd = "New task\nHear Stephanie out."
show screen phone_taskadded
$ contact_notify_me = True
$ contact_text_me += "\n\nLater I found... Stephs letter in my pocket. It seems she did tell me ... something, before she left. Judging from my own reaction, I should at least hear her out."
$ contact_notify_stephanie = True
$ contact_text_stephanie += "\n\nIt seems that on our last day together before she left, she put a letter in the pocket of my shirt."
$ contact_text_stephanie += " Probably expecting me to use that shirt like I had been for a long time. The letter didn't explain much though, but at at least it was something."
me "..."
hide screen phone_taskadded
hide screen phone
$ renpy.pause()

scene ep3_epilogue_steph with dissolve
$ renpy.pause(0.1)
scene ep3_epilogue_linda with Dissolve(1, alpha=True)
$ renpy.pause(0.1)
scene ep3_epilogue_robin with Dissolve(1, alpha=True)
$ renpy.pause(0.1)
scene ep3_epilogue_kira with Dissolve(1, alpha=True)
$ renpy.pause(0.1)
scene ep3_epilogue_lexi with Dissolve(1, alpha=True)
$ renpy.pause(0.1)
scene ep3_epilogue_cece with Dissolve(1, alpha=True)
$ renpy.pause(0.1)
scene bg empty with Dissolve(1, alpha=True)
$ renpy.pause(1)

show screen ep3_endscreen
$ renpy.pause()
label ch3End:
hide screen ep3_endscreen
$ renpy.pause(0.5)
$ renpy.pause(0.5)
stop music fadeout 3
scene bg empty with fade
$ renpy.pause(2)
$ renpy.pause(2)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc

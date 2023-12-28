# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define shera = Character("nameS", color=Color((108, 114, 161)), dynamic=True)
define basari = Character("Basari Narat", color=Color((108, 114, 161)))
define salemi = Character("Salemi Narat", color=Color((108, 114, 161)))
define ravie = Character("Ravie", color=Color((108, 114, 161)))
define kalie = Character("Kalie", color=Color((108, 114, 161)))
define lara = Character("Mr. Lara", color=Color((108, 114, 161)))
define lani = Character("Lani Farad", color=Color((108, 114, 161)))
define voli = Character("Voli", color=Color((108, 114, 161)))

default nameS = ""

default basariVal = 0
default salemiVal = 0
default ravieVal = 0
default kalieVal = 0

default route = ""

default townDone = False
default homeDone = False

default lastPoint = ""

default inventory = []

init python:
    
    base1 = {"look":"lookb1", 
            "n":"nb1", 
            "w":"wb1", 
            "e":"eb1", 
            "s":"sb1", 
            "talk to basari":"talkbab1", 
            "talk to salemi":"talksab1", 
            "look at basari":"lookbab1",
            "look at salemi":"looksab1",
            "special town":"townb1", 
            "special home":"homeb1", 
            "confused":"confused", 
            "cmd":"cmd", 
            "inventory":"inventory"}
    town1 = {"look":"lookt1", 
            "n":"nt1", 
            "w":"wt1", 
            "e":"et1", 
            "s":"st1", 
            "special home":"posttown", 
            "confused":"confused", 
            "cmd":"cmd", 
            "inventory":"inventory"}
    street1 = {"special town":"towns1", 
            "special cabin":"cabins1",
            "enter house":"homes1", 
            "look at house":"lookhomes1",
            "n":"ns1", 
            "w":"ws1", 
            "e":"es1", 
            "s":"ss1",
            "look":"looks1",
            "confused":"confused", 
            "cmd":"cmd", 
            "inventory":"inventory"}
    town2 = {"talk to ravie":"talkrat2", 
            "use baubles":"usebrt2", 
            "look at ravie":"lookrat2", 
            "look at shop":"looksht2",
            "enter shop":"shop1",
            "n":"nt2", 
            "w":"wt2", 
            "e":"et2", 
            "s":"st2",
            "look":"lookt2",
            "confused":"confused", 
            "cmd":"cmd", 
            "inventory":"inventory"}
    
    keys = {"base1":base1, "town1":town1, "street1":street1, "town2":town2}
    def takeInput(s, key):
        act = renpy.input(prompt=s)
        act = act.lower()
        lst = []
        index = 0;
        while (act != "" and index<len(act)):
            if (act[index]==" "):
                lst.append(act[:index])
                act = act[index+1:]
                index = 0
            index += 1
        lst.append(act)
        return readInput(lst, key)
        
    def readInput(s, key):
        #renpy.say(shera, s[0])
        if "cmd" in s:
            return parserGet("cmd", s[len(s)-1], key)
        if "look" in s and len(s)==1:
            return parserGet("look", s[len(s)-1], key)
        if "talk" in s:
            return parserGet("talk to", s[len(s)-1], key)
        if "use" in s:
            return parserGet("use", s[len(s)-1], key)
        if "enter" in s:
            return parserGet("enter", s[len(s)-1], key)
        if "inventory" in s:
            return parserGet("inventory", s[len(s)-1], key)
        if "look" in s and "at" in s:
            return parserGet("look at", s[len(s)-1], key)
        if "take" in s:
            return parserGet("take", s[len(s)-1], key)
        if "north" in s or "n" in s:
            return parserGet("n", s[len(s)-1], key)
        if "south" in s or "s" in s:
            return parserGet("s", s[len(s)-1], key)
        if "east" in s or "e" in s:
            return parserGet("e", s[len(s)-1], key)
        if "west" in s or "w" in s:
            return parserGet("w", s[len(s)-1], key)
        else:
            return parserGet("special", s[len(s)-1], key)
            
    def parserGet(act, obj, key):
        map = keys[key]
        if (act+" "+obj) in map:
            return map[act+" "+obj]
        elif act in map:
            return map[act]
        else:
            return map["confused"]
            
    
    
    def highestVal(b, s, r, k):
        if(b<0 or s<0 or r<0 or k<0):
            return -1
        if (highestOfTwo(b, s) > highestOfTwo(r, k)):
            return highestOfTwo(b, s)
        else if (highestOfTwo(r, k) > highestOfTwo(b, s)):
            return highestOfTwo(r, k)
        else:
            return -1
        
    def highestOfTwo(a, b):
        if (b>a):
            return b
        else if (a>b):
            return a
        else:
            return -1
            
    def closeInVal(a, b):
        return abs(a-b) > 3

# The game starts here.





label start:

    scene bg base
    show shera silhouette
    shera "My cousins came to live with me by chance. This arrangement began nearly half a year ago."
    shera "I picked them up at the base across the mountain path from town in the early evening."
    shera "It was a cold day, during the rainy season. I was eager to get back quickly since I had left an object in town for appraisal."
    $ nameS = "Shera"
    show shera normal at left
    show salemi normal at right
    show basari normal at offscreenright
    shera "Do you have everything?"
    salemi "I believe so."
    show salemi normal at offscreenright
    show basari normal at right
    basari "..."
    shera "Perfect, let's go then."
    shera "(I would prefer that they weren't forced to wait for me, but I do need to talk to Mr. Lara in town.)"
    $ nameS = ""
    shera "This game uses a text prompt feature. The prompter will display potential actions for Shera to decide between."
    shera "The prompter may accept other commands, some of which may affect gameplay. For a full list, type \"cmd\"."
    $ nameS = "Shera"
    $ renpy.jump("startact")
        
label startact:
    
    $ lastPoint = "startact"
    $ renpy.jump(takeInput("Town or home?", "base1"))
        
label confused:

    shera "(What?)"
    $ renpy.jump(lastPoint)
    
label cmd:

    $ nameS = ""
    shera "Commands: look, talk to, look at, use, take, enter, north, south, east, west, n, s, e, w, inventory"
    shera "To go to a location, enter the name of that location. Some directions will also prompt you to go to a location."
    shera "If you use the \"look\" command, interactables should be visible as bolded text."
    shera "Additionally, you can sometimes use some items from your inventory."
    $ nameS = "Shera"
    $ renpy.jump(lastPoint)
    
label inventory:
    
    $ nameS = ""
    if inventory:
        python:
            invString = ""
            for i in inventory:
                invString += i+"\n"
            renpy.say(shera, invString)
    else:
        shera "Inventory is empty!"
    $ nameS = "Shera"
    $ renpy.jump(lastPoint)
    
label lookb1:

    shera "(There's nothing worth looking at in this place. My cousins {b}Basari{/b} and {b}Salemi{/b} came here after living at a similar camp near our hometown in Thara for the last year.)"
    shera "(I don't really want to keep them any longer, but I am in a bit of a hurry to return to Mr. Lara in {b}town{/b}.)"
    shera "(If I take them {b}home{/b} right now, I suppose I could go tomorrow instead.)"
    jump startact
    
label nb1:

    shera "(To the north is Vetar Ba, the mountain I live on.)"
    shera "(I live in the village of Mien Ko. It's near the peak of the mountain. Most of the trade is mining.)"
    shera "(Vetar Ba is the neighboring mountain to Lat Ba, where the border camp is. This base is on the far edge of camp.)"
    jump startact
    
label wb1:

    shera "(The border with Thara is to the west. We all used to live there, somewhere in the faraway desert.)"
    shera "(Every day I'm thankful my family left, even though life here is much simpler than life in Bichet...)"
    shera "(At least we have our health.)"
    jump startact
    
label eb1:

    shera "(Vetar Ba continues east and dissolves into marshy foothills.)"
    shera "(Although most of the population in Mien Ko is Thara {i}uosi{/i}, nearly everyone east of us has been here for centuries.)"
    shera "(Most of the people in the foothills are farmers, although there are some logging and fishing towns.)"
    jump startact
    
label sb1:

    shera "(To the south are the neighboring peaks of the Ben Gi mountain range.)"
    shera "(Ben Gi is a relatively prosperous area. Vetar Ba produces good crafts and livestock.)"
    shera "(Then, of course, there's the border camp at Lat Ba, where we are now. Mitenken Uo as a nation has made the border efforts a priority in recent years.)"
    jump startact
    
label talkbab1:

    $ basariVal += 1
    show salemi normal at offscreenright
    show basari normal at right
    shera "Hey, little bro, what's up?"
    basari "..."
    basari "Hello."
    show basari normal at offscreenright
    show salemi normal at right
    salemi "<Be more polite. We aren't owed a place to stay.>"
    show salemi normal at offscreenright
    show basari normal at right
    basari "<I am being polite.>"
    basari "{i}Chaemanya.{/i}"
    show shera angry
    shera "No fighting."
    show shera normal at left
    shera "(We should leave soon. They both seem tired.)"
    jump startact
    
label talksab1:

    $ salemiVal += 1
    show salemi normal at right
    show basari normal at offscreenright
    shera "How's it going?"
    salemi "We're doing well. Thank you for your hospitality."
    shera "Of course. Anything for family."
    jump startact
    
label lookbab1:

    shera "(My younger cousin Basari.)"
    shera "(He looks terrible.)"
    jump startact

label looksab1:

    shera "(My cousin Salemi, the sweetest girl on the planet.)"
    shera "(The townspeople are going to love her.)"
    jump startact
    
label townb1:
    
    if not homeDone:
        shera "I need to make a quick stop in town first. Then we'll go get you settled in."
        shera "My house is about an hour away, but it's mostly flat."
    scene bg town
    show shera normal at left
    show ravie normal at offscreenright
    show kalie normal at offscreenright
    shera "(Nobody's here...)"
    show ravie normal at right with move
    ravie "It's you. Do you need something?"
    shera "Oh, Ravie. Nice to see you too."
    shera "Just my parcel. And maybe a smile if it's not too much to ask for."
    ravie "You charmer. I'll go get my dad."
    show ravie normal at offscreenright
    if not homeDone:
        show basari normal at right
        basari "<I thought you said there were {i}Tharava{/i} here.>"
        show shera happy at left
        shera "<There are. Mostly near the summit.>"
        shera "<Be nice to this family. They're important people.>"
        show shera normal at left
        show basari normal at offscreenright
    show kalie normal at right
    kalie "Hello, Shera! These are your cousins?"
    shera "Hello, Kalie. They certainly are! Would you care for an introduction?"
    kalie "Yes, of course!"
    show shera normal at offscreenleft
    show kalie normal at offscreenright
    show kalie left normal at left
    show salemi normal at right
    kalie "Nice to meet you. My name is Kalie Lara."
    salemi "It's a pleasure. My name is Salemi Narat. Shera's father is my uncle."
    if not homeDone:
        salemi "This is my younger half-brother, Basari."
        show salemi normal at offscreenright
        show basari normal at right 
        basari "..."
        show basari normal at offscreenright
    show salemi normal at offscreenright
    show lara normal at right
    lara "Shera! You've returned!"
    shera "Hello, Mr. Lara! These are my cousins who'll be staying with me."
    show lara normal at offscreenright
    show lara left normal at left
    show kalie left normal at offscreenleft
    show salemi normal at right
    lara "Nice to meet you! I hope you'll feel right at home here."
    lara "Kalie, why don't you run upstairs so I can give Shera her payment."
    show salemi normal at offscreenright
    show kalie normal at right
    kalie "Of course."
    show kalie normal at offscreenright
    $ nameS = ""
    shera "Received 3 golden baubles"
    $ inventory.append("3 golden baubles")
    $ nameS = "Shera"
    lara "Don't forget to come by anytime. Especially you newcomers."
    lara "Goodbye now!"
    show lara left normal at offscreenleft
    show shera normal at left
    show ravie normal at right
    ravie "Those were nice jewels. Where did you get them?"
    shera "In the caves near my shop."
    ravie "Hm. It figures. Not that I would know about dirty work like that."
    shera "Well, you're lucky that someone does, or you'd be out of trinkets to steal before your old man could say \"spoiled bitch.\""
    show ravie normal at offscreenright
    show ravie angry at right
    ravie "What did you just call me?"
    shera "So I'll see you at my shop later?"
    ravie "Not in a million years!"
menu:
    "Leave off":
        $ ravieVal += 1
        shera "Too bad. We have to go now, so just stop by if you change your mind."
    "Tease":
        shera "If you prefer, I could show you around the caves."
        ravie "What are you talking about?"
        ravie "I'm not like you or my sister."
        ravie "When you're not as big as a cow, you can afford to have standards!"
        
label endtown:

    show ravie angry at offscreenright
    shera "(There she goes. Definitely my favorite Lara twin by entertainment value, if not by personality.)"
    if not homeDone:
        show basari normal at right
        basari "Be nice to this family, huh."
        shera "Yeah, yeah. Come on, kid."
    $ townDone = True
    if not homeDone:
        jump townact
    else:
        jump posttown
    
label homeb1:
    
    shera "Well, let's go get you unpacked."
    scene bg home
    $ nameS = ""
    show shera silhouette at center
    if not townDone:
        shera "It was about an hour walk from the base to my house."
    shera "My sullen relatives set down their belongings and I began to help them unpack."
    $ nameS = "Shera"
    show shera normal at left
    shera "You can put your things on the floor for now."
    show salemi normal at right
    salemi "Thank you very much again. We hope not to be a burden to you."
    show shera happy at left
    shera "I'm telling you, you don't have to worry about it."
    shera "You can stay here as long as you can tolerate the noise. I'll be working in my shop from dawn to noon nearly every day."
    shera "I hope it doesn't bother you."
    show salemi normal at offscreenright
    show basari normal at right
    basari "It won't bother us."
    show basari normal at offscreenright
    $ nameS = ""
    show shera silhouette at center
    shera "I cleaned my own quarters for a few minutes as they unpacked silently."
    shera "When I went downstairs, the room I had prepared was populated with an assortment of clothes and the bare minimum of toiletries."
    scene bg sbroom
    shera "Salemi and Basari were sitting on the beds, facing one another, not saying anything."
    shera "When I entered the room, Basari got up in one swift motion and went outside."
    $ nameS = "Shera"
    show shera normal at left
    shera "Where's he off to?"
    show salemi normal at right
    salemi "He's probably going to go for a run. It's his normal habit."
    shera "Oh. That's fine, then."
    salemi "Sorry. He should be back before dark. He usually is, anyway."
    shera "It's no problem, really. Please treat this as your home while you're here in Mien Ko."
    salemi "Of course. Thank you again for having us."
    shera "So do you have any plans while you're here?"
    salemi "Well, I want to find a job. I don't think it would be good for Basari to have to worry about anything like that, though."
    shera "Sure. Well, I know someone who works at the border camp, if you want a position there."
    shera "Although I totally understand if you don't want any more of that sort of thing."
    show salemi normal at offscreenright
    show salemi happy at right
    salemi "No, I'll take anything you can offer. Thank you."
    shera "Great! I'll invite him over tomorrow, then."
    shera "Until then you should get some rest. Can your brother find his way back?"
    salemi "If he doesn't, I can find him."
    shera "Great. Good night then!"
    shera "(It's late... I can go into town tomorrow.)"
    $ homeDone = True
    jump streetact
    
label townact:

    $ lastPoint = "townact"
    $ renpy.jump(takeInput("Go home?", "town1"))
    
label lookt1:

    shera "That was all I needed from town. We can go {b}home{/b} now."
    basari "Let's go, then."
    jump townact

label nt1:

    shera "(My house is to the north, further up the mountain.)"
menu:
    "Go home":
        jump posttown
    "Stay here":
        jump townact

label et1:

    shera "(More shops are across the street.)"
    shera "(That noodle bar is pretty good... I should take my cousins there.)"
    jump townact

label wt1:

    shera "(The Laras live in an old, large, stately house.)"
    shera "(Downstairs, their shop sells luxury goods.)"
    shera "(I've heard they have a courtyard, but I've never been inside.)"
    jump townact

label st1:

    shera "(Further down the mountain path, there are smaller houses and gardens.)"
    jump townact





label streetact:

    scene bg street
    $ lastPoint = "streetact"
    $ nameS = ""
    show shera silhouette
    shera "I got up early the next morning and spent some time at the forge."
    shera "When it was time for shops to open, I still hadn't seen my cousins awake."
    $ nameS = "Shera"
    show shera normal at left
    shera "That's ok... they deserve some rest."
    if townDone:
        shera "Maybe I should stop by Lani's cabin and see if he can get Salemi a job."
    else:
        shera "I should go into town and pick up my payment. Then maybe I can stop by Lani's cabin and see if he can get Salemi a job."
    $ renpy.jump(takeInput("Where to?", "street1"))
        
label posttown:

    scene bg street
    $ nameS = ""
    show shera silhouette
    shera "We returned home quickly."
    $ nameS = "Shera"
    if homeDone:
        jump streetact
    else:
        jump homeb1

label homes1:

    scene bg home
    $ nameS = ""
    show shera silhouette
    shera "(When I went inside, Basari was standing in the kitchen.)"
    $ nameS = "Shera"
    show shera normal at left
    shera "Hey, you made it back!"

label lookhomes1:

    shera "(My house.)"
    shera "(The garden will be ready to harvest soon.)"
    jump streetact

label cabins1:

    scene bg cabin
    
    scene fb1

label ns1:
    shera "(I live pretty far up the mountain. All that's north of here is the mining site.)"
    jump streetact

label ws1:

    shera "(On this side of the street is my house.)"
    jump streetact

label es1:

    shera "(Lani's house is a little east of here.)"
menu:
    "Go to Lani's house":
        jump cabins1
    "Stay here":
        jump streetact

label ss1:
    shera "(Most of the buildings in town are to the south.)"
menu:
    "Go into town":
        jump towns1
    "Stay here":
        jump streetact

label looks1:
    if not townDone:
        shera "I should go into {b}town{/b} and get my payment."
    else:
        shera "Lani's {b}cabin{/b} is just up the road."
        shera ""
    jump streetact
    
label towns1:

    if not townDone:
        show salemi normal at right
        salemi "Good morning."
        shera "Oh, hey! I was just about to head into town!"
        shera "Do you want to come? Good opportunity to meet the locals."
        salemi "Sure, I don't have anything else to do."
        shera "Great!"
        jump townb1
    else:
        $ ravieVal += 1
        $ kalieVal += 1
        scene bg town
        show shera normal at left
        show ravie normal at right
        $ lastPoint = "towns1"
        $ renpy.jump(takeInput("Where to?", "town2"))
    
label lookt2:

    shera "I'm back at Lara Niv."
    shera "{b}Ravie{/b} is minding the store. Today I might take a look at the things further inside the {b}shop.{/b}"
    jump towns1

label nt2:

label et2:

label wt2:

label st2:

label talkrat2:

label usebrt2:

    $ravieVal += 1
    ravie "What, is this supposed to be an apology?"
    shera "Sure, if you want it to be."
    jump towns1

label lookrat2: 

    shera "()"

label looksht2:

label shop1:





label routes1c:

    scene bg cabin

label routes1s:

    scene bg town

label routes2r:

    scene bg rroom
    show shera normal at left
    show ravie normal at right
    shera "How's Kalie doing?"
    ravie "Still playing house with her gold digger boyfriend."
    shera "Wow, that almost sounds like an accusation."
    show ravie angry at right
    ravie "Well, it's true. He's only with her because he wants the house. But he's setting himself up for disappointment."
    ravie "He'll be stuck with her and left with nothing. She's never going to inherit Lara Niv."
    shera "Inherit? That's a long way off, don't you think?"
    show ravie normal at right
    ravie "Shera, our father is dying."
    ravie "He's dying and leaving the business to one of us."
    ravie "I was poised to inherit everything until she stuck her fat face into it."
    ravie "Her whole love affair is a sham. She just knows that if she can trick some poor idiot into marrying her, the house will go to the couple."
menu:
    "You could marry me":
        ravie "Yeah, right."
        ravie ""
    "You're so spiteful":
        shera "I knew you were jealous, but... wow."

label routes2k:

    scene bg shop

label routes2b:

    scene bg cabin

label routes2s:

    scene bg home
    show shera normal at left
    show salemi normal at right
    shera "Hey, little sister! What's up?"
    salemi "Oh, hello."
    salemi "...I was just going to make some tea."
    shera "Go for it. Make me a cup, too."
    salemi "Of course."
    shera "I'm just doing expenses."
    salemi "Hmm. Sounds boring."
    shera "Yup."
    salemi "..."
    salemi "Ok, tea's brewing."
    salemi "Actually, do you think I could ask you something?"
    shera "Of course. What is it?"
    salemi "In my room."
    scene bg sbroom
    salemi ""
    
label endings:
    if route=="Kalie":
        scene bg kroom
    if route=="Ravie":
        scene bg rcave
    if route=="Basari":
        scene bg cabin
    if route=="Salemi":
        scene bg forest

label kvwedding:

    scene kvwedding
    if route=="Kalie":
        show weddingL
        lara "Thank you all for coming."
        show weddingKF at right
        show weddingVK at left
        lara "Thank you for coming to celebrate the union of my younger daughter..."
        show weddingKF2
        lara "And the man I am proud to call my son-in-law."
        show weddingVK2
        lara "I'm so happy for them."
        show wedding3
        lara "I now pronounce you married!"
        show wedding4
        return
    if route=="Basari":
        show weddingK at right
        show weddingVK at left
    
label svwedding:

    scene svwedding
    if route=="Ravie":
        show weddingS at right
        show weddingVS at left
    if route=="Salemi":
        show weddingSP at right
        show weddingVS at left
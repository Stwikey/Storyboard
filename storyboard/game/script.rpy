define m = Character('Me', color="#2c3b2c")
define g = Character('Boyfriend', color="#616192") #tsundere
define s = Character('Shrimp', color="#9e5b21") #cocky, handsome, wears hawaiin shirt and holds a cocktail
define f = Character('Fish', color="#3a3a60") #business man, wears a suit and has a briefcase 
define b = Character('Bread', color="#58473a") #cute, yandere
define w = Character('Waiter', color="#c8c8ff")
default shrimp = True
label start:#uhhh fix prob

    scene bg restaurant

    "It's already 7:00pm. My boyfriend should have gotten here 1 hour ago... Did he forget?"

    "He never answered any of my recent text messages..."

    "Ugh I'm starving. Maybe I should order some food while I wait."

    m "Hey waiter! Can I order some food?"

    w "Sure! What would you like?"

    "Some moments later, the waiter arrives with plates of food."

    "They all smell so delicious...But my boyfriend still hasn't arrived yet."

    "..."

    "Maybe I'll just have a small bite..."

menu:
    
    "reach for the shrimp dish.":
        jump shrimpstart
    "reach for the fish dish.":
        jump fishstart
    "reach for the bread dish.":
        jump breadstart

label shrimpstart:
    s "Heh. I knew you'd choose me."

    "...Did that shrimp just speak?"

    s "Are you struck by my ultimate beauty? I know you want me. Lets go now darling."

    m "...Go where?"

    s "Go get married of course!"

    "..."
menu:
    "Go with him":
        jump shrimp_married_ending

    "No":
        jump shrimp_alternate

label fishstart:
    f "I'm surprised. But glad that you chose me."

    "...Did that fish just speak?"

    f "Indeed. I promise I will take good care of you. Will you marry me?"

    m "..."
menu:
    "I do":
        jump fish_married_ending

    "No":
        jump fish_alternate

label breadstart:
    b "I can't believe you chose me!! <3333 I promise I'll make you happy!!!"

    "...Did that bread just speak?"

    b "You're so silly!!!! Now here comes the big question."

    m "...?"

    b "Will you marry me?"

    "..."

menu:
    "Yes of course!!!!!":
        jump bread_married_ending

    "No thank you!!!!!":
        jump bread_alternate

label shrimp_married_ending:
    f "..."

    b "but you haven't even met the rest of us yet"

    s "she doesn't need to"

    "you and shrimp get married 1 day later while fish and bread watch enviously."

    "your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up for him."

    m "I would have never made such beautiful children with such a crazy alien."

    s "Alien? whats that?"

    m "Vorp?"

    return

label fish_married_ending:
    b "..."

    s "but you haven't even met the rest of us yet"

    f "don't worry. She doesn't need to"
    
    "you and fish get married 1 day later while fish and bread watch enviously."

    "your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up for him."

    m "I would have never made such beautiful children with such a crazy alien."

    f "Alien? whats that?"

    m "Vorp?"

    return

label bread_married_ending:
    f "..."

    s "but you haven't even met the rest of us yet"

    b "she doesn't need to"

    "you and bread get married 1 day later while fish and bread watch enviously."

    "your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up for him."

    m "I would have never made such beautiful children with such a crazy alien."

    b "Alien? whats that?"

    m "Vorp?"

    return

label shrimp_alternate:
    s "..."

    s "Playing hard to get I see."

    s "Hahahaha! I like that!"

    jump part_two

label fish_alternate:
    f "..."

    f "I'll offer you $100000"

    m "No."

    f "$10000000?"

    m "..."

    m "No."

    f "$10000000000?"

    m "..."

menu:
    "Okay fine.":
        jump fish_married_ending
    "I said no!":
        f "alright I understand."
        jump part_two

label bread_alternate:
    b "why not?!?!? :(("

    jump part_two

label part_two:
    s "Hmmmm maybe she is just not familiar with our game."

    f "You could be right. Lets introduce ourselves shall we?"

    b "I'll go first!! I'm Franklin"

    s "I'm Alecksander"

    "Alecksander winks at you."

    f "My name is Bartholomew, but you may call me Barty. I make 9 figures a year and I'll make you super rich"

label questions:
    s "Is there anything else you'd like to know about us?"

    "Alexcksander winks at you again."
menu:
    "Your hobbies":
        jump hobbies
    "What you like to eat":
        jump food
    "What's your type":
        jump _type
    "No":
        jump part_3

label hobbies:
    m "What are your hobbies?"

    s "Well personally I'm great on the dancefloor but it takes two to tango if you know what I mean."

    b "Dancing? Pfft. Thats nothing special."
    
    f "I might not look like it but I like to party too which is why they call me Barty."

    "Bartholomew starts shimmying in his plate."

    m "..."

    jump questions


label food:
    m "what kind of food do you like to eat?"

    s "My favourite food? I've got to say some tuna sandwiches."

    b "..."

    f "..."

    m "..."

    m "nevermind."

    jump questions

label _type:
    m "whats your type?"

    s "I'm looking at my type right now."

    "Alecksander winks at you."

    b "You of course !! <3333"

    f "It seems I have competition."

    m "..."

    m "nevermind."

    jump questions

label part_3:
    m "I think I've learned enough about you."

    b "what do we do now then?"

    f "you're boyfriend seems to not be coming."

    s "I think its time you leave."

    s "with me."

menu:
    "I want to wait for my boyfriend.":
        jump wait

    "I'm going to break up with my boyfriend.":
        jump break_up

label wait:
    m "I want to wait for my boyfriend."

    











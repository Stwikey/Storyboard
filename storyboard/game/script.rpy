define m = Character('Me', color="#2c3b2c")
define g = Character('Boyfriend', color="#616192") #tsundere
define s = Character('Shrimp', color="#9e5b21") #cocky, handsome, wears hawaiin shirt and holds a cocktail
define f = Character('Fish', color="#3a3a60") #business man, wears a suit and has a briefcase 
define b = Character('Bread', color="#58473a") #cute, yandere
define w = Character('Waitress', color="#c8c8ff")
define j = Character('Jimmy', color="#c8c8ff")
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

    m "I would have never made such beautiful children with such a crazy human."

    s "Human? whats that?"

    m "Vorp?"

    return

label fish_married_ending:
    b "..."

    s "but you haven't even met the rest of us yet"

    f "don't worry. She doesn't need to"
    
    "you and fish get married 1 day later while fish and bread watch enviously."

    "your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up for him."

    m "I would have never made such beautiful children with such a crazy human."

    f "Human? whats that?"

    m "Vorp?"

    return

label bread_married_ending:
    f "..."

    s "but you haven't even met the rest of us yet"

    b "she doesn't need to"

    "you and bread get married 1 day later while fish and bread watch enviously."

    "your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up for him."

    m "I would have never made such beautiful children with such a crazy human."

    b "Human? whats that?"

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

menu breakup:
    "I want to wait for my boyfriend.":
        jump wait

    "I'm going to break up with my boyfriend.":
        jump break_up

label wait:
    m "I want to wait for my boyfriend."

    "one hour passes."

    "another hour passes."

    b "I don't think your boyfriends coming."

    s "Yeah. You'd be much better of with me."

    f "I agree."

    m "..."

    jump breakup

label break_up:
    m "Alright."

    "I text my boyfriend. \"I'm breaking up with you.\""

    b "Did you do it? Yayyyyy!!!! <33"

    s "I'm proud of you darling."

    f "good job."

    jump choose

label choose:
    s "so..."

    b "which one of us will you choose?"


menu choice:
    "Alecksander":
        jump shrimp
    "Franklin":
        jump bread
    "Bartholomew":
        jump fish
    "None of you":
        jump none_ending

label none_ending:
    m "...None of you."

    s "What??"

    "Franklin starts sobbing. Mold begins to form at the edges of his crust."

    "Bartholomew doesn't say anything but you can tell that he is disappointed."

    m "Sorry guys. But I'm really hungry."

    "You start devouring the plates of food. You see the waitress walk towards you in the corner of your eye."

    w "How is it?"

    m "Really great."

    w "I know right! The hosts are fantastic. This is my favourite host and boyfriend, Jimmy!"

    j "Hey."

    m "...Hosts?"

    w "..."
    
    "The waitress looks at the empty plates on my table"

    w "DID YOU EAT OUR HOSTS???"

    m "...What?"

    m "You mean the plates of food?"

    w "NO OUR HOSTS YOU DUMMY THIS IS A HOST CAFÉ NOT A RESTAURANT"

    m "Vorp?"

    w "JIMMY! CALL THE POLICE!"

    "Jimmy nods."

    m "Humans are so weird."

    "You pull out your space ray gun blaster as Jimmy reaches for his phone."

    "A lazer fires from the space blaster and vaporizes Jimmy and the waiter."

    jump none

label none:
    "You spend the rest of your days living in solitary and in peace."
    return



label shrimp:
    s "Haha! I knew you'd choose me."

menu:
    "Let's get married.":
        jump shrimp_married_ending
    "Let's go on a date first.":
        jump shrimp_date

label bread:
    b "Yayyyy I can have you all to myself now!! <333"
menu:
    "Let's get married.":
        jump bread_married_ending
    "Let's go on a date first.":
        jump bread_date    

label fish:
    f "Good choice."
menu:
    "Let's get married.":
        jump fish_married_ending
    "Let's go on a date first.":
        jump fish_date

label fish_date:
    m "I'd like to go on a date first before we get married."

    f "Don't worry. My credit card is endless anyways."

    "The next day."

    f "Welcome to my private cruise."

    f "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."

    f "Here have some food."

    m "Oh thanks."

    "You look down and see Alecksander and Franklin shimmying on the plate."
menu:
    "Eat the food.":
        jump eat_the_food_fish

    "Don't eat the food":
        jump dont_eat_the_food_fish


label dont_eat_the_food_fish:
    m "Sorry I don't think I can eat this. I'll end the date here."

    f "I understand."

    jump choose

label eat_the_food_fish:
    
    "You shrug and dig in."

    f "How is it?"

    m "Delicious."

    f "I knew you'd like it. Now for the final act of our date night."

    "Bartholomew gets down on one knee."

    f "Will you marry me?"

    "You gasp. Pleasantly not surprised."

    

menu:
    "Of course!":
        jump fish_married_ending
    "No.":
        "Bartholomew is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        b "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        "You pick Bartholomew off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none





label bread_date:
    m "I'd like to go on a date first before we get married."
    
    b "Of course!"
    
    "The next day."

    b "Welcome to my private cruise!"

    b "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."

    b "Here have some food."

    m "Oh thanks."

    "You look down and see Alecksander and Bartholomew shimmying on the plate."
menu:
    "Eat the food.":
        jump eat_the_food_bread

    "Don't eat the food":
        jump dont_eat_the_food_bread

label eat_the_food_bread:
    "You shrug and dig in."

    b "How is it?"

    m "Delicious."

    b "I knew you'd like it. Now for the final act of our date night."

    "Franklin gets down on one knee."

    b "Will you marry me?"

    "You gasp. Pleasantly not surprised."

label dont_eat_the_food_bread:
    m "Sorry I don't think I can eat this. I'll end the date here."

    b "I understand."

    jump choose
menu:
    "Ofcourse!":
        jump bread_married_ending
    "No.":
        "Franklin is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        b "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        "You pick Franklin off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none






label shrimp_date:
    m "I'd like to go on a date first before we get married."
    
    s "Sure why not."

    "The next day."

    s "Welcome aboard my private cruise."

    s "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."
    
    s "Oh I was talking about you."

    m "..."

    s "Here have some food."

    m "Oh thanks."

    "You look down and see Franklin and Bartholomew shimmying on the plate."

menu:
    "Eat the food.":
        jump eat_the_food

    "Don't eat the food":
        jump dont_eat_the_food

label eat_the_food:
    "You shrug and dig in."

    s "How is it?"

    m "Delicious."

    s "I knew you'd like it. Now for the final act of our date night."

    "Alecksander gets down on one knee."

    s "Will you marry me?"

    "You gasp. Pleasantly not surprised."
label dont_eat_the_food:
    m "Sorry I don't think I can eat this. I'll end the date here."

    s "I understand."

    jump choose

menu:
    "Ofcourse!":
        jump shrimp_married_ending
    "No.":
        "Alecksander is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        s "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        "You pick Alecksander off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none







    




















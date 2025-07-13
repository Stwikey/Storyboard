define m = Character('Me', color="#2c3b2c")
define g = Character('Boyfriend', color="#616192") 
define s = Character('Shrimp', color="#9e5b21") 
define f = Character('Fish', color="#3a3a60") 
define b = Character('Bread', color="#58473a") 
define w = Character('Waitress', color="#7f7539")
define j = Character('Jimmy', color="#611c1c")
default shrimp = True
label start:#finished

    scene restaurant

    m "It's already 7:00pm. My boyfriend should have gotten here 1 hour ago... Did he forget about our date?"

    m "He never answered any of my recent text messages either..."

    m "Ugh I'm starving. Maybe I should order some food while I wait."

    m "Hey waiter! Can I order some food?"

    show waitress

    with dissolve

    w "Sure! What would you like?"

    m "Whatever you reccomend."

    w "Leave it to me!"

    hide waitress

    with dissolve

    "Some moments later, the waiter arrives with plates of food."

    show waitress

    with dissolve

    w "Here's your food."

    w "Enjoy!"

    hide waitress

    with dissolve

    m "They all smell so delicious...But my boyfriend still hasn't arrived yet."

    m "..."

    m "Maybe I'll just have a small bite..."

menu:#finished
    
    "reach for the shrimp dish.":
        jump shrimpstart
    "reach for the fish dish.":
        jump fishstart
    "reach for the bread dish.":
        jump breadstart

label shrimpstart:#finished

    show shrimp

    with dissolve

    show shrimp eyes

    s "Heh. I knew you'd choose me."

    show shrimp wink

    "The shrimp winks at you"

    m "...Did that shrimp just speak?"

    show shrimp

    s "Are you struck by my ultimate beauty? I know you want me. Lets go now darling."

    m "...Go where?"

    show shrimp eyes

    s "Go get married of course!"

    show shrimp wink

    "The shrimp winks at you again"

    m "..."

menu:#finished
    "Go with him":
        jump shrimp_married_ending

    "No":
        jump shrimp_alternate

label fishstart: #finished
    show fish 

    with dissolve

    f "I'm surprised. But glad that you chose me."

    m "...Did that fish just speak?"

    show fish rose

    f "Indeed. I promise I will take good care of you. Will you marry me?"

    m "..."
menu:#finished
    "I do":
        jump fish_married_ending

    "No":
        jump fish_alternate

label breadstart:#finished
    show bread 

    with dissolve

    b "I can't believe you chose me!! <3333 I promise I'll make you happy!!!"

    m "...Did that bread just speak?"

    b "You're so silly!!!! Now here comes the big question."

    m "...?"

    show bread hearts

    b "Will you marry me?"

    m "..."

menu:#finished
    "Yes of course!!!!!":
        jump bread_married_ending

    "No!!!!!":
        jump bread_alternate

label shrimp_married_ending: #finished
    hide shrimp

    show fish

    with dissolve

    f "..."

    hide fish

    show bread

    with dissolve

    b "But you haven't even met the rest of us yet :(("

    "The bread starts sobbing uncontrollably."
    
    hide bread

    show shrimp

    with dissolve

    s "She doesn't need to."

    scene wedding

    show shrimp

    with dissolve

    s "Will you make me the happiest shrimp in the entire world and marry me?"

    m "I do."

    hide shrimp

    with dissolve

    "You and the shrimp get married 1 day later after quickly breaking up with your boyfriend while the fish and the bread watch enviously."

    "You and your new husband proceed to buy a house soon after the wedding."

    scene house

    "Your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up with him."

    m "I would have never made such beautiful children with such a crazy human."

    show shrimp

    with dissolve

    s "Human? whats that?"

    "You look back at the family photo that was just recently taken with your newborn baby."

    m "Vorp?"

    hide shrimp

    show shrimp family 

    with dissolve

    "You continue to live with your shrimp husband and your child and live happily ever after."

    return

label fish_married_ending: #finished
    hide fish

    show bread

    with dissolve

    b "..."

    hide bread

    show shrimp

    with dissolve

    s "But you haven't even met the rest of us yet :(("

    "The shrimp starts sobbing uncontrollably."
    
    hide shrimp

    show fish

    with dissolve

    f "She doesn't need to."

    scene wedding

    show fish

    with dissolve

    f "Will you make me the happiest shrimp in the entire world and marry me?"

    m "I do."

    hide fish

    with dissolve

    "You and the fish get married 1 day later after quickly breaking up with your boyfriend while the shrimp and the bread watch enviously."

    "You and your new husband proceed to buy a house soon after the wedding."

    scene house

    "Your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up with him."

    m "I would have never made such beautiful children with such a crazy human."

    show fish

    with dissolve

    f "Human? whats that?"

    "You look back at the family photo that was just recently taken with your newborn baby."

    m "Vorp?"

    hide fish

    show fish family 

    with dissolve

    "You continue to live with your fish husband and your child and live happily ever after."

    return

label bread_married_ending:#finished
    hide bread

    show fish

    with dissolve

    f "..."

    hide fish

    show shrimp

    with dissolve

    s "But you haven't even met the rest of us yet :(("

    "The shrimp starts sobbing uncontrollably."
    
    hide shrimp

    show bread

    with dissolve

    b "She doesn't need to."

    scene wedding

    show bread

    with dissolve

    b "Will you make me the happiest bread in the entire world and marry me?"

    m "I do."

    hide bread

    with dissolve

    "You and the bread get married 1 day later after quickly breaking up with your boyfriend while the shrimp and the fish watch enviously."

    "You and your new husband proceed to buy a house soon after the wedding."

    scene house

    "Your ex-boyfriend is still no where to be found. It seems like he doesn't have one ounce of remorse."

    m "good thing I broke up with him."

    m "I would have never made such beautiful children with such a crazy human."

    show bread

    with dissolve

    b "Human? whats that?"

    "You look back at the family photo that was just recently taken with your newborn baby."

    m "Vorp?"

    hide bread

    show bread family 

    with dissolve

    "You continue to live with your bread husband and your child and live happily ever after."

    return
label shrimp_alternate: #finished
    s "..."

    s "Playing hard to get I see."

    s "Hahahaha! I like that!"

    jump part_two

label fish_alternate:#finished
    f "..."

    f "I'll offer you $100000"

    m "No."

    f "$10000000?"

    m "..."

    m "No."

    f "$10000000000?"

    m "..."

menu:#finished
    "Okay fine.":
        jump fish_married_ending
    "I said no!":
        f "alright I understand."
        jump part_two

label bread_alternate:#finished
    b "why not?!?!? :(("

    jump part_two

label part_two:#finished
    hide fish

    hide shrimp

    hide bread

    show shrimp

    with dissolve

    s "Hmmmm maybe she is just not familiar with our game."

    hide shrimp

    show fish

    with dissolve

    f "You could be right. Lets introduce ourselves shall we?"

    hide fish

    show bread

    with dissolve

    define b = Character('Franklin', color="#58473a") #cute, yandere

    b "I'll go first!! I'm Franklin"

    hide bread

    show shrimp

    with dissolve

    define s = Character('Alecksander', color="#9e5b21")

    hide shrimp

    show shrimp eyes

    s "I'm Alecksander"

    hide shrimp eyes

    show shrimp wink

    "Alecksander winks at you."

    hide shrimp wink

    show fish

    with dissolve

    define f = Character('Bartholomew', color="#3a3a60") 

    f "My name is Bartholomew, but you may call me Barty. I make 9 figures a year and I'll make you super rich."

    hide fish

    with dissolve

label questions: #finished

    show shrimp

    with dissolve

    hide shrimp

    show shrimp eyes

    s "Is there anything else you'd like to know about us?"

    hide shrimp eyes

    show shrimp wink

    "Alexcksander winks at you again."

    hide shrimp wink

    with dissolve
menu: #finished
    "Your hobbies.":
        jump hobbies
    "What you like to eat.":
        jump food
    "What's your type.":
        jump _type
    "No.":
        jump part_3

label hobbies:#finished

    m "What are your hobbies?"

    show shrimp

    with dissolve

    s "Well personally I'm great on the dancefloor but it takes two to tango if you know what I mean."

    hide shrimp

    show bread

    with dissolve

    b "Dancing? Pfft. Thats nothing special."

    hide bread

    show fish

    with dissolve
    
    f "I might not look like it but I like to party too which is why they call me Barty."

    hide fish

    show fish rose

    "Bartholomew starts shimmying in his plate."

    m "..."

    hide fish rose

    jump questions

label food:#finished
    m "what kind of food do you like to eat?"

    show shrimp
    
    with dissolve

    s "My favourite food? I've got to say some tuna sandwiches."

    hide shrimp

    show bread

    with dissolve

    b "..."

    hide bread

    show fish

    with dissolve

    f "..."

    m "..."

    m "nevermind."

    hide fish

    jump questions

label _type: #finished
    m "whats your type?"

    show shrimp

    with dissolve

    hide shrimp

    show shrimp eyes

    s "I'm looking at my type right now."

    hide shrimp eyes

    show shrimp wink

    "Alecksander winks at you."

    hide shrimp wink

    show bread

    with dissolve

    b "You of course !! <3333"

    hide bread

    show fish

    with dissolve

    f "It seems I have competition."

    m "..."

    m "nevermind."

    hide fish

    jump questions

label part_3: # inished
    m "I think I've learned enough about you."

    show bread

    with dissolve

    b "what do we do now then?"

    hide bread

    show fish

    with dissolve

    f "your boyfriend seems to not be coming."

    hide fish

    show shrimp

    with dissolve

    hide shrimp

    show shrimp eyes

    s "I think its time you leave."

    hide shrimp eyes

    show shrimp wink

    s "with me."

    hide shrimp wink

menu breakup: #finished
    "I want to wait for my boyfriend.":
        jump wait

    "I'm going to break up with my boyfriend.":
        jump break_up

label wait:#finished
    m "I want to wait for my boyfriend."

    "one hour passes."

    "another hour passes."

    show bread

    with dissolve

    b "I don't think your boyfriends coming."

    hide bread

    show shrimp

    s "Yeah. You'd be much better of with me."

    hide shrimp

    show fish

    with dissolve

    f "I agree."

    m "..."

    hide fish

    jump breakup

label break_up:#finished
    m "Alright."

    "I text my boyfriend. \"I'm breaking up with you.\""

    show bread

    with dissolve

    b "Did you do it? Yayyyyy!!!! <33"

    hide bread

    show shrimp

    with dissolve

    s "I'm proud of you darling."

    hide shrimp

    show fish

    with dissolve

    f "good job."

    hide fish

    jump choose

label choose:#finished

    scene restaurant

    show shrimp

    with dissolve

    s "so..."

    hide shrimp

    show bread
    
    with dissolve

    b "which one of us will you choose?"

    hide bread


menu choice:#finished
    "Alecksander":
        jump shrimp
    "Franklin":
        jump bread
    "Bartholomew":
        jump fish
    "None of you":
        jump none_ending

label none_ending:#finished
    m "...None of you."

    show shrimp

    with dissolve

    s "What??"

    hide shrimp

    show bread

    with dissolve

    "Franklin starts sobbing. Mold begins to form at the edges of his crust."

    hide bread

    show fish

    with dissolve

    "Bartholomew doesn't say anything but you can tell that he is disappointed."

    hide fish

    m "Sorry guys. But I'm really hungry."

    play sound "audio/eating.mp3"

    "You start devouring the plates of food. You see the waitress walk towards you in the corner of your eye."

    show waitress

    with dissolve

    w "How is it?"

    m "Really great."


    w "I know right! The hosts are fantastic. This is my favourite host and boyfriend, Jimmy!"

    hide waitress

    show apple

    with dissolve

    j "Hey."

    m "...Hosts?"

    hide apple

    show waitress

    with dissolve

    hide waitress

    show waitress speachless

    with dissolve

    w "..."
    
    "The waitress looks at the empty plates on my table"

    hide waitress speachless

    show waitress angry

    w "DID YOU EAT OUR HOSTS???"

    m "...What?"

    m "You mean the plates of food?"

    w "NO OUR HOSTS YOU DUMMY THIS IS A HOST CAFÉ NOT A RESTAURANT"

    m "Vorp?"

    w "JIMMY! CALL THE POLICE!"

    hide waitress angry

    show apple

    with dissolve

    "Jimmy nods."

    m "Humans are so weird."

    "You pull out your space ray gun blaster as Jimmy reaches for his phone."

    "A lazer fires from the space blaster and vaporizes Jimmy and the waiter."

    hide apple

    jump none

label none:#finished
    scene house

    show none

    with dissolve

    "You spend the rest of your days living in solitary and in peace."
    return



label shrimp:#finished

    show shrimp
    
    with dissolve

    s "Haha! I knew you'd choose me."

    hide shrimp

menu:#finished

    "Let's get married.":
        jump shrimp_married_ending
    "Let's go on a date first.":
        jump shrimp_date

label bread:#finished
    show bread

    with dissolve

    b "Yayyyy I can have you all to myself now!! <333"

    hide bread
menu:#finished
    "Let's get married.":
        jump bread_married_ending
    "Let's go on a date first.":
        jump bread_date    

label fish:#finished
    show fish

    with dissolve

    f "Good choice."

    hide fish
menu:#finished
    "Let's get married.":
        jump fish_married_ending
    "Let's go on a date first.":
        jump fish_date

label fish_date:#finished

    show fish

    with dissolve

    m "I'd like to go on a date first before we get married."

    hide fish

    show fish eye closed

    f "Don't worry. My credit card is endless anyways."

    hide fish eye closed 
    
    with dissolve

    scene cruise

    "The next day."

    show fish

    with dissolve

    f "Welcome to my private cruise."

    f "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."

    "You and Bartholomew walk around the cruise until you end up in a fancy looking restaurant."

    f "Here have some food."

    m "Oh thanks."

    "You look down and see Alecksander and Franklin shimmying on the plate."

    hide fish
menu:#finished
    "Eat the food.":
        jump eat_the_food_fish

    "Don't eat the food.":
        jump dont_eat_the_food_fish


label dont_eat_the_food_fish:#finished
    m "Sorry I don't think I can eat this. I'll end the date here."

    show fish eye closed

    with dissolve

    f "I understand."

    hide fish eye closed

    jump choose

label eat_the_food_fish:#finished

    play sound "audio/eating.mp3"
    
    "You shrug and dig in."

    show fish 

    with dissolve

    f "How is it?"

    m "Delicious."

    f "I knew you'd like it. Now for the final act of our date night."

    hide fish 

    with dissolve

    "Bartholomew gets down on one knee."

    show fish rose

    with dissolve

    f "Will you marry me?"

    "You gasp. Pleasantly not surprised."

    hide fish rose  

menu:#finished
    "Of course!":
        jump fish_married_ending
    "No.":

        show fish eye closed

        with dissolve

        "Bartholomew is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        b "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        play sound "audio/eating.mp3"

        hide fish eye closed

        "You pick Bartholomew off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none


label bread_date:#finished
    show bread

    with dissolve

    m "I'd like to go on a date first before we get married."

    hide bread

    show bread hearts

    b "Don't worry. My credit card is endless anyways."

    hide bread hearts
    
    with dissolve

    scene cruise

    "The next day."

    show bread

    with dissolve

    b "Welcome to my private cruise."

    b "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."

    "You and Franklin walk around the cruise until you end up in a fancy looking restaurant."

    b "Here have some food."

    m "Oh thanks."

    "You look down and see Alecksander and Bartholomew shimmying on the plate."

    hide bread
menu:#finished
    "Eat the food.":
        jump eat_the_food_bread

    "Don't eat the food":
        jump dont_eat_the_food_bread

label dont_eat_the_food_bread:#finished

    m "Sorry I don't think I can eat this. I'll end the date here."

    b "I understand."

    jump choose
label eat_the_food_bread:#finished
    play sound "audio/eating.mp3"

    "You shrug and dig in."

    show bread

    with dissolve

    b "How is it?"

    m "Delicious."

    b "I knew you'd like it. Now for the final act of our date night."

    hide bread

    "Franklin gets down on one knee."

    show bread hearts

    with dissolve

    b "Will you marry me?"

    "You gasp. Pleasantly not surprised."

    hide bread

menu:#finished
    "Of course!":
        jump bread_married_ending
    "No.":

        show bread

        with dissolve

        "Franklin is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        b "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        hide bread
        
        play sound "audio/eating.mp3"

        "You pick Franklin off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none

label shrimp_date:#finished
    show shrimp

    with dissolve

    m "I'd like to go on a date first before we get married."

    hide shrimp

    show shrimp wink

    s "Don't worry. My credit card is endless anyways."

    hide shrimp wink
    
    with dissolve

    scene cruise

    "The next day."

    show shrimp

    with dissolve

    s "Welcome to my private cruise."

    s "Isn't the view wonderful?"

    "You look around the cruise. It certainly costs a fortune. There is even a private chef and a private DJ."

    m "Yeah the cruise is nice."

    "You and Alecksander walk around the cruise until you end up in a fancy looking restaurant."

    s "Here have some food."

    s "Oh thanks."

    "You look down and see Franklin and Bartholomew shimmying on the plate."

    hide shrimp

menu:#finished
    "Eat the food.":
        jump eat_the_food

    "Don't eat the food":
        jump dont_eat_the_food

label dont_eat_the_food:#finished
    m "Sorry I don't think I can eat this. I'll end the date here."

    show shrimp

    with dissolve

    s "I understand."

    hide shrimp

    jump choose


label eat_the_food:#finished
    play sound "audio/eating.mp3"

    "You shrug and dig in."

    show shrimp

    with dissolve

    s "How is it?"

    m "Delicious."

    s "I knew you'd like it. Now for the final act of our date night."

    hide shrimp

    "Alecksander gets down on one knee."

    show shrimp eyes

    with dissolve

    s "Will you marry me?"

    hide shrimp eyes

    show shrimp wink

    "You gasp. Pleasantly not surprised."

    hide shrimp wink

menu:#finished
    "Of course!":
        jump shrimp_married_ending
    "No.":
        show shrimp

        with dissolve

        "Alecksander is disappointed."

        m "Truthfully, it's because you look too delicious to marry."

        s "I understand. I will do whatever it takes to make you happy."

        m "Thank you."

        hide shrimp
        
        play sound "audio/eating.mp3"

        "You pick Alecksander off his plate and eat him."

        "You burp."

        m "Yummy."

        jump none


    




















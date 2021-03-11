transform rightish:
    xcenter .2
    ypos 50

image school:
    zoom 1.5
    "bg school.png"
    
image road:
    zoom 1
    "bg road.png"
    
image dark:
    zoom 1.6
    "bg dark.png"
    
image home:
    zoom 1.2
    "bg home.png"
    
image ending:
    zoom 2.2
    "bg ending.png"
    xalign .5
    yalign .5
    
image end:
    "bg end.png"
    
define audio.birds = "audio/birds.mp3"
    
label start:
    define a = Character("Aisaka", color="#FF7F50")
    define h = Character("Hori", color="#800080")
    define you = Character("You", color="FFFFFF")
    scene school at truecenter
    play music birds
    you "Ah ..."
    you "What a wonderful morning!"
    you "It's my first day at the university... I should make new friends!"
    ". . ."
    show hori thinking:
        xcenter .4   
    show aisaka behind hori:
        xcenter .65
        zoom 1.3
    you "As expected there are plenty of gorgeous girls, I should make them my acquaintances."
    
menu:
    you "What should I do?"
    "Introduce yourself":
        jump input_name
    "Hit on them":
        you "Hi beauties, why don't you show me around here?"
        show hori thinking:
            xcenter .4
        show aisaka bored:
            xcenter .65
            zoom 1.1
        a "eh... no thank you ..."
        h "Goodbye."
        return
    
label input_name:
    python:
        name = renpy.input(_("What's your name?"))
        name = name.strip() or "You"
    define y = Character("[name]", color="#FFFFFF")
    y "Hi! My name is [name]"
    y "Let's be friends!"
    
    h "Hello, I am Hori. Nice to meet you."
    a "And I am Aisaka. Nice to meet you as well."
    
menu:
    "Are you girl first years as well?":
        jump freshmen
        
    "What year are you in?":
        jump sophomores
        
        
label freshmen:
    a "WHAAAAT?"
    h "How could you think this? We are already sophomores!"
    y "..ah I didn't mean it like this..."
    h "Don't mind Aisaka, she gets easily upset when she has a hangover."
    y "Oh.. I see"
    jump tour
    
label sophomores:
    a "We are aleady sophomores."
    jump tour
        
label tour:
    y "It's my first time here at the university..."
    y "Could you please give me a tour of the campus after the lectures?"
    h "Sure, why not."
    y "Let's meet at the same place then."
    
menu:
    "Ask Hori for her phone number":
        h "Sure, write it down (788 30 666)"
        y "See you soon!"
    "Leave":
        y "It's already late and no one came..."
        y "I think I got dumped..."
        y "..."
        return
        
label date:
    scene road at truecenter
    show hori happy:
        xcenter .4
    y "Glad to see you again!"
    y "but where is Aisaka?"
    h "She couldn't come. Some urgent work."
    y "It's a pity"
    h "Don't worry. I'm going to show and tell you everything"
    h "After all you're my beloved Kohai <3"
    y "..."
    h "Want to grab some ice cream? I know a good place not far away."
    
menu:
    "Can't disagree with Senpai":
        h "Follow me."
        menu:
            h "Do you like vanilla or fistic?"
            "I like vanilla":
                $ flag = True
                h "mmm...Me too"            
            "I love fistic":
                $ flag = False
                hide hori happy
                show ice cream:
                    yalign .3
                    xalign .5
                h "*giggles*"
                h "hehe... you look so merry <3"
    "What about the campus tour?":
        hide hori happy
        show angry hori:
            zoom 0.7
            xalign .5
            yalign .15
        h "...bruh"
        h "Can't get a hint? Can you?"
        h "I am leaving!"
        return
    
label ending:
    scene dark
    y "It's getting dark..."
    show hori happy:
        xcenter .4
    h "Could you walk me back home?"
    menu:
        "Walk her home":
            y "Yes! with great pleasure."
            h ":3"
        "Refuse":
            hide hori happy
            show sad hori:
                xcenter .5
                yalign 0.55
                zoom 0.7
            y "Sorry Senpai, I've got a lot of homework to do for tommorow."
            h "...oh well"
            h "Bye then!"
            return
   
    scene home
    h "We've arrived, my house is to the left."
    show hori happy:
        xcenter .4
    y "Looks spacious!"
    if flag:
        h "Thank you for walking me home"
        h "Very nice of you!"
        h "See you tommorow!"
        y "See you tommorow as well!"
        return
    menu:
        h "How about coming in for some coffee?"
        "Join her":
            y "Can't refuse you, Senpai."
            h "Come in. :3"
        
        "Refuse":
            hide hori happy
            show sad hori:
                xcenter .5
                yalign 0.55
                zoom 0.7
            y "Sorry Senpai, I've got a lot of homework to do for tommorow."
            h "...oh well"
            h "Bye then!"
            return
            
    scene ending
    show hori thinking:
        xcenter .4
    h "Hold on for a moment..."
    hide hori thinking
    y "What happened?"
    h "We're out of coffee..."
    h ":3"
    scene end
    "The night went on..."
    return
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
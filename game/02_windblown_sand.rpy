

#https://github.com/TheReal3rd/Reincarnation-of-the-caged/blob/dialogs/dialogs_dump/2.windblow_sand.txt
label windblown_sand:
    # *Alicea Original code.*
    scene image "introduction1.jpg"#Missing
    "-fragment of an audio recording."


    scene image "bg exterior sand.jpeg"#Mssing
    "the white creature and the girl in black arrive at a place entombed by sand. Sand streams down from towers covering most of the area."
    mama "Goodness look at all these rivers of sand! I wonder how such a thing came to pass."
    mama "Make sure you don't get any grit in your eyes!"
    mama "I wonder where all of this sand is going" #8:32
    mama "Let's head for the shiny black light up there" # Wasn't originally here in Alicea version.
    "going through the solitude place filled with ruins and sand the two eventually arrive at the source of the black light. It was emitted by a black statue, the two wanderes closely approach it"
    mama "These strange statues are scattered through The Cage. I don't know who made them but I call them dark Scarecrows."
    scene image "black statues.jpeg"#Working fine.
    mama "Anyways, this is the first one so we will start here"
    "the girl observes the black statue in front of her"
    menu first_scarecrow:
            "Enter the story within the unknown statue?"
            "I will enter":
                "You enter the scarecrows story."
            "I refuse":
                "You refuse to enter and turn to Mama"
                mama    "what's wrong, you should touch it."
                girl    "........."
                mama    "If you don't how will you ever reclaim everything that has been lost?"
                girl    "........."
                mama    "........."
                mama    "so be it then. Do know however you will come to regret this. "
                return
    "You enter the curious statue and come to find out there is a entire new place inside of it" # 9:34

    #Story 1 Shadown in the wastes: https://youtu.be/RbE-6D_dLPA?si=T5iuDBJOJ2762Kma&t=577
    scene image "rust1.png"#Missing
    "Story 1: Showdown in the Wastes"

    scene image "bg story1.jpg"
    "A pair of two peculiar men traverse a desert"
    "boy of good upbringing moves across a vast wasteland, and a taciturn
    man follows. They mind their surroundings with unease, almost as if they fear
    pursuit, until they finally reach a small, windswept town where they hope to
    shake the road from their weary bones."

    scene image "bg story1.jpg"
    "Most of the townsfolk merely observe the passing visitors with cautious eyes,
    but when they approach an eatery, a pack of hard men block their path.
    You royalty, boy? sneers one of them."
    "suddenly the story is interrupted"
    #10:56 Appears alicea has reworked the story a slit bit.

    scene image "bg story1error.jpg"
    mama "did you see the flock of black birds that possesed the bounty hunter"
    mama "They are nasty sorts who like to fly in and warp the story "
    mama "Well, we are not going to let that stand, are we?"
    mama "Your role is to defeat them and put the story back the way it's supposed to be"
    mama "But I suppose you already know that, don't you?"
    scene image "battle1.JPG"

    "you fight the bounty hunters and defeat them. The story continues."
    scene image "bg story1.jpg"
    "His companions all draw iron at
    the question, but the taciturn man is faster. After the foes run off into
    the dust, the man turns to the boy and asks a single question:"
    dimos "Are you hurt, My Prince?"
    rion  "I am well but you know I am no longer a prince.."#14:18 I feel some things can be added.
    "The pair then decides to take their leave of the town."

    #Story 2
    scene image "bg story1.jpg"
    "Story 2: The Prosthetic Woman"

    #Wasn't originally here.
    #storyman "Wherever people gather, stories come with them.
    #But saloons have a special ability to loosen even the tightest of lips.
    #Such rumors are what brings the woman with a mechanical arm and leg to this place.
    #For she is a bounty hunter in search of her prey."

    "A female bounty hunter with two mechanical limbs walks into a saloon and begins
    asking after certain individuals. Though the information she obtains is vague,
    it proves to be more than enough."# 18:16
    "She has caught the scent of her prey, and it leads her to the forest."

    #18:48
    "But as she makes to leave, another bounty hunter blocks her path. She is known
    for her success as a bounty hunter, and this man demands she hand over all
    her coin."
    "But the fight is over before it can begin; no mediocre highwayman
    could hope to stand against the fires of revenge that fuel the woman."
    "As her would-be assailant lies dying in the dust, she steps over him and continues on."


    #Story 3
    scene image "bg story 2.jpg"
    "Story 3: The Gunslinger"
    "In a forest near a ruined church, the man searches for food; he knows the boy
    must eat, but the pickings are slim indeed."
    "Eventually, he finds a single apple
    on the ground. But when he takes it up, a starving bear crashes through the
    underbrush and stares at the meal with hungry, desperate eyes."

    "After putting the bear to rout, the man returns to the boy, who lies safely 
    at the back of the chapel."# "to rout"?
    "Though he has always been sickly, this merciless
    journey has chipped away at what remains of his life—and when the man offers
    him the apple, his body is too weak to accept it."#25:20

    "The man cannot help the boy now.
    All he can do is stay by his side and wait for the end."

    #Story 4
    scene image "rust2.png"
    "Story 4: Journey's End"#27:48
    "The bounty hunter with prosthetic limbs arrives at the ruins of
    a once-proud church. The ceiling is collapsed, the walls mere suggestions; it is
    more shell than structure now."

    "Inside, she finds her targets: a deteriorated
    mechanical soldier and a corpse the size of a child."
    "But when she takes a single
    step forward, the clockwork man springs to life. With a howl that could be
    creaking joints or the wail of a dying soul, the man turns his gun on the woman." #TODO maybe add 30:04 About access files so it joins the text. -3rd

    "The boy died a century ago. After being chased from his homeland, he traveled
    with the clockwork man and tried to stop the war ravaging his kingdom, but his
    life was lost before he could accomplish his mission."
    "Yet the man continued to safeguard his charge, attacking any who dared approach the boy long after his once-proud body had fallen to rust."

    "But this is a place of respite now, and the clockwork man will not move again.
    The woman gives them a proper burial, then turns and leaves the forest
    without a sound."

    #
    scene image "characterstory1.jpg"
    "Former title: Chapter 1: Windblown Sand His Body,Rust."
    scene image "notes1.jpg"
    "Flow of the game"
    with fade
    scene image "bg exterior sand.jpeg"
    "The girl and the strange creature called Mama traverse the entire sandy area after a strenous
    expedition through all the black statues named Scarecrows, Mama explains"
    mama "Your task is to fix warped memories like this in order to restore complete stories"
    mama "But we also need to collect weapons like these"
    mama "Do you have a rough sense of what you are supposed to do now, child?"
    menu optional_name:
        "Do I understand what's asked of me?"
        "Nod":
            "I think to myself, this is probably for the best."
        "Shake head":
            "I think to myself, will this truly save me?"
            mama "Yes, I suppose it is a lot to wrap your mind around"
            mama "It will make sense as we find more stories. Don't be afraid to ask for help!"

    "They continue to traverse this unknown place until they reach a long pair of stairs"
    mama "My, what a beautiul place! I can't fathom how anyone managed to construct something so large."
    "as they go further into the building they encounter a strange bird, sitting on a pillar leading up to the bridge"
    mama "You will sometimes encounter black birds in The Cage and you should do what to shoo them all out."
    "mamas small figure shakes excitely"
    mama "If you do that, Mama will give you a nice surprise!"
    "You shoo the bird away like instructed"
    #scene image TODO fix this image.
    "They continue to make their way through the area to find all scattered scarecrows."
    mama "we collect stories in order to regain what you have lost"
    mama "but we also do it to make your wish come true"
    mama "So let's keep it up. Slow and steady wins this race!"
    "After a while of passing through a long pair of stairs, Mama breaks the silence"
    mama "Hmmm. I suppose I should tell you a little bit about The Cage"
    mama "It's a truly massive structure."
    mama "Where you woke up, and this sandy area, here are just small parts of it."
    mama "To be honest, a great deal of The Cage is a mystery."
    mama "I'm not even certain who gave it that name."
    #scene image
    "They arrive at the next scarecrow in front of a huge door."
    mama "To think that poor sick child had to travel the wastes in his condition"
    mama "Still, we have restored the third memory now."
    mama "If we can collect the next one, it will mark the end of the Staff's tale."
    "They make their way through to the last scarecrow."
    #scene image
    mama "Goodness,this place is nothing but stairs!I hope your little legs are okay."
    #32:33 TODO Maybe add in about the stairs so it doesn't cut from this to then next story.
    jump grains_of_sand


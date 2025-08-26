

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

    #Story 2 TODO Ask alicea if she happy with us adding the Storyman.
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
   

    #Story 3 TODO i stoped here -3rd
    scene image "bg story 2.jpg"
    "Story 3: The Gunslinger"
    "In a forest near a ruined church, the man searches for food; he knows the boy
    must eat, but the pickings are slim indeed." 
    "Eventually, he finds a single apple
    on the ground. But when he takes it up, a starving bear crashes through the
    underbrush and stares at the meal with hungry, desperate eyes."

    "After putting the bear to rout, the man returns to the boy, who lies safely
    at the back of the chapel."
    "Though he has always been sickly, this merciless
    journey has chipped away at what remains of his life—and when the man offers
    him the apple, his body is too weak to accept it."

    "The man cannot help the boy now.
    All he can do is stay by his side and wait for the end."
    scene image "rust2.png"
    "Story 4: Journey's End"
    "The bounty hunter with prosthetic limbs arrives at the ruins of
    a once-proud church. The ceiling is collapsed, the walls mere suggestions; it is
    more shell than structure now."
    
    "Inside, she finds her targets: a deteriorated
    mechanical soldier and a corpse the size of a child."
    "But when she takes a single
    step forward, the clockwork man springs to life. With a howl that could be
    creaking joints or the wail of a dying soul, the man turns his gun on the woman."

    "The boy died a century ago. After being chased from his homeland, he traveled
    with the clockwork man and tried to stop the war ravaging his kingdom, but his
    life was lost before he could accomplish his mission."
    "Yet the man continued to safeguard his charge, attacking any who dared approach the boy long after his once-proud body had fallen to rust."

    "But this is a place of respite now, and the clockwork man will not move again.
    The woman gives them a proper burial, then turns and leaves the forest
    without a sound."
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



    scene image "bg losttitle1.jpg"
    "First part"
    with fade
    scene image "bg loststory1.jpg"
    "In a lush and verdant land, two sisters hunt for their daily meals, ebon hair
    streaming behind them as they dash through the forest."

    "One day, as the elder sister is going about her usual routine, she hears her
    sister scream. Rushing to the sound, she finds the girl frozen in fear with
    a beast ready to attack."
    "A single arrow from the woman's bow drives the creature
    away, causing the younger to spill tears of relief." 
    "After embracing the girl,
    the woman quickly offers up her silver hairpin, a keepsake of their mother her
    younger sister has long desired. As her tears dry, the girls swears she will be
    the one to do the protecting next time."

    scene image "bg losttitle2.jpg"
    "Second part"
    "Their hunting complete, the sisters make for home. But when they exit the forest,
    they see smoke and flame rising in the distance." 
    "The woman immediately thinks of
    the war that is raging in a neighboring nation, and after telling her sister to
    stay put, makes her way to town."
    
    scene image "bg loststory3.jpg"
    "When she arrives, she finds herself surrounded by the incessant crackle of flames.
    The town is a slaughterhouse, with corpses on every corner." 
    "As she takes in the scene, her younger sister suddenly rushes up to her." 
    "She immediately grabs her
    and attempts to flee, but they are quickly surrounded by enemy soldiers and cut
    down. As her consciousness fades away, she hears her sister scream, followed by
    the voice of a soldier uttering two words:"

    "Sort them."

    scene image "bg losttitle3.jpg"
    "Third part"
    with fade
    "bg loststory4.png"
    "Thinking that she heard her sister, the woman opens her eyes and finds herself in
    a prison. Her body is now a stranger—one arm and one leg have been replaced by
    mechanical substitutes, and her ebon hair has turned white as new-fallen snow."

    "After breaking out of her cell, she dispatches a guard with ease. He cackles as
    he dies, gleefully informing her that the captives in this place are all sorted,
    experimented on, and turned into killing machines. He then tells her that she is
    one of the failures."

    "Her mind is filled with a single thought: Is my sister safe? She dashes
    from the prison, running faster and faster in an attempt to escape the terrible
    thoughts in her head and feeling in her chest."

    scene image "bg losttitle4.jpg"
    "Finale"
    with fade
    "bg loststory5.png"
    "When the woman exits the prison, she finds herself in a strange land of flames
    and blood. As she picks her way through the battlefield, she hears a child's
    voice and begins to run." 
    "Suddenly, the owner of the voice appears before her; it
    is her sister, twisted and warped as a result of the sorting."
    "The girl makes a sound—a desperate, terrible hiss that might be the woman's name—then chokes
    on her own blood as a soldier cuts her down like an animal.
    After this, her memory goes mercifully blank."

    "When she comes to, she finds the cold corpse of her sister surrounded by chunks
    of what used to be enemy soldiers. She gently embraces the girl and closes
    her eyes. From this day onward, revenge would be her only reason to live."
    scene image "blackscreen.jpg"
    "What was lost, completed."

    scene image "marionette1.png"
    "I was too much used to this feeling I had no name for, shattered memory data fragment."
    #-insert title screen here Determined hearts, the clockwork Man-
    "Deep beneath a castle, a mechanical soldier sits amidst the detritus of a
    storehouse. One day, a boy is brought to the room by soldiers and tossed to the
    floor."
    "As he stares at the boy, the man begins collecting junk to make
    a bed; when he is finished, the two sit upon it and tell each other their tales."

    "The name the man gives is that of the first model of machine soldiers. He explains
    how he was unable to carry out orders and therefore discarded as defective."

    "The name the boy gives is that of the kingdom's firstborn prince. After explaining
    how he has been cast aside because of his disease, the boy gives a wry smile at
    the similar circumstances they find themselves in."
    #-insert title screen, his song.-
    "The boy's condition worsens within the poor conditions of the storehouse, so the
    man searches around and finds a medicine bottle. But the bottle is empty, which
    causes the boy to chuckle." 
    "The man's concern gives him newfound energy,
    however, so he places a candle in the bottle and turns it into a small lamp."

    "In the soft glow of the lamp, the boy sings the tale of a hero who challenges
    evil in order to save his people."
    "As he listens to the beautiful melody, the man
    feels something change in his chest, and words of gratitude begin to spill from
    his lips—words clockwork men like him should not be able to say. Upon hearing
    this, a joyful smile spreads across the face of the boy."

    scene image "marionette2.png"
    #-insert screen, To Face a Father-
    "They hear soldiers gossiping on the other side of the door; the start of another
    war is upon them. The boy looks at the man and begins passionately speaking of
    his resolve to stop the war for the sake of his people." 
    "After a moment's thought, the man breaks down the door of the prison, beats back the guards,
    and accompanies the boy to the throne room."

    "Standing before the king like the bold hero of his song, the boy demands that
    the war be ended. But the king deems this act to be treason and orders his own
    son killed. The clockwork man cannot disobey his king's orders, and slowly aims
    his gun." 
    "But then he summons forth something new—a will of his own—and
    manages to defy the command. As soldiers rush into the room, the man seizes
    the boy's hand and flees the castle with his new charge in tow."
    "The pair runs through the village outside the castle with royal guards
    in pursuit."
    #-insert screen, The night it all began-
    "Though the villagers are in uproar over the impending war,
    they soon realize the boy is royalty and begin jeering at him, heaping their
    outrage against the monarchy on his head alone." 
    "But despite the words, fists,
    and more being hurled in their direction, the pair never stops running."

    "Finally, impossibly, they escape. As they look back on their former home,
    the boy swears to put an end to the war his father started." 
    "Upon hearing this,
    the clockwork man makes his own oath to guard the prince until his dying breath.
    With determination in their hearts, they take their first steps on the long and
    winding road to peace."

    "Determined hearts, the end."

    scene image "fleeting1.png"

    "In the darkness, the woman quietly listens to her master speak. He is a feudal
    lord, one to whom she has pledged fidelity. He praises her for her previous
    assassination, and commands her to move on to the next. From beyond the wall,
    she utters a single word:"

    "Understood."

    "As she walks through town, she is surrounded by the excited hum of life
    and the smiles of random people." 
    "These are things she can never know,
    and while she envies them, she usually pays them no mind—for she walks
    a different path, one set in a darkness illuminated only by the glinting
    of blades."
    "Today, however, the bright smile of a child she passes refuses to
    leave her mind. Even as she cuts down bandits on the road, the young one's
    carefree expression stays with her."

    "She recalls her days of training—training much too severe for a child.
    Every morning, she would ignore the pain of her exhausted body and bring herself
    to the flogging garden, where the adults would berate her for lateness
    and whip her." 
    "She was instructed to be always at her lord's side, and to serve
    him as a tool for eliminating his enemies. This had been the way of her family
    for time immemorial, and as one of them, she was burdened with the assassin's
    duty before she was even born."

    "But these are poor memories, and as she slips into the rainy forest, she banishes
    them from her mind."
    "Complaining will help nothing; all that matters is the mission.
    With her resolve restored, she kills a guard at the gate and enters the castle that looms before her."

    "Her target is the heir to an enemy territory. Killing this target within
    the supposed safety of the castle will cause panic, at which point she will
    to signal her lord's army to begin an all-out attack."

    "As she flies down the corridor and into the reception room, she discovers her
    target to be a small boy." 
    "But even when she presses the tip of her sword to the
    childs throat, he does not cry out. After studying his face for a moment,
    she realizes the child is not a boy at all, but a girl." 
    "When asked about her disguise, the girl replies" 
    "'I wish this house would fall. I am naught but a puppet
    who dances at my fathers tune. I'm no child to him—merely a tool to be used.'"
    scene image "fleeting2.png"
    "This resentment carries a familiar ring for the woman, who suddenly sees her
    younger self in the face and fate of the girl who waits before her."
    "As she struggles with her decision, the roar of the rain outside fades to a
    distant whisper in her ears."

    "After an uncountable amount of time, woman sheathes her blade and asks"
    akeha "Did you mean it when you said you wish your house would fall?" 
    "The girl nods, shaking from the strain of the moment, and the woman responds with a single
    word once more:"

    "Understood."

    "Behind her, soldiers suddenly burst into the room. Minutes later, they all
    lie dead on the floor—but the woman has sustained a fatal wound in the process."
    
    "She does not know why she has done this, save that she understands what it is
    like to suffer for the sake of one's family, but she does not regret her actions."
    "And though she knows saving one person is not enough to grant absolution,
    she figures it will make a nice gift to take with her into hell."

    scene image "mountain1.png"

    "A man makes his way along a mountain path buried in snow.
    There is no movement. No sound. Only a perfect wall of unbroken white.
    Though the sun is starting to set, the man's pace does not falter." 
    "When he encounters a crevice, he cuts down a tree to make a bridge. When the moon
    rises high in the sky, his footsteps do not slow." 
    "This mountain holds a wondrous
    charm for him, and no matter how dangerous it may be in the dark, he has absolute
    trust in his experience. Even when he finds himself surrounded by starving wolves,
    that trust does not waiver."

    "The man knows this to be a most precipitous mountain, one where no person has
    ever reached the summit. But he is an adventurer who has conquered many peaks
    in the past, and he eternally seeks the line between life and death within
    the harshest environments." 
    "This pursuit is his entire reason for living."

    "A blizzard sets in over the snowy mountain, as though attempting to refuse
    the man passage. The freezing wind and snow sting him, making his steps heavy.
    Finally, he catches glimpse of a small cave in the rocks and takes shelter from
    the elements." 
    "Once inside, he recalls the letter in his pocket. His daughter had
    given it to him before his climb, along with a charm. The thought of his daughter
    gives him renewed strength, and when the blizzard subsides,
    he begins his climb anew."

    "Halfway up the mountain, he comes across a lake with a corpse lying on its shore.
    There is no way to tell how long it has been there, but when he investigates
    the body, he finds a note in the pocket." 
    "The handwriting is shaky—perhaps from
    the cold, perhaps from grief—and it tells of the corpse's regret at having left
    his family behind to attempt the climb."

    "A tremendous cliff looms before the man—the final trial before the peak.
    If he can conquer this, the mountain will be his. He whispers encouraging words
    to himself, and though death lurks with every handhold and footfall, he finally
    reaches the top."

    "Though the mountain has supposedly never been climbed, he finds a ruined shrine
    waiting for him. He does not know how long it has been here or how old it is,
    but the sight of it stirs his adventurer's blood. But when he sets foot inside,
    he finds, impossibly, that his wife is waiting for him."

    "The baby is coming. she says, her words an echo in his mind. 
    Why did you leave us?"

    "He rubs at his eyes fiercely, and when he reopens them, he sees not his wife,
    but the frozen corpse of a pregnant woman holding an all-too-familiar charm.
    The sight solidifies his resolution to return home to his family, and he turns
    and departs without a second thought."

    "A lonely house sits in a forest of deep snow. As a pregnant woman minds the
    housework, a knock shudders the door, a small girl responds" 
    "Its Dad! -cries the womans daughter.
    as she leaps toward the door. But when she flings it open, the stoop is bare.
    A trick of the wind, perhaps."
    scene image "mountain2.png"
    "The two of them wait for the man to return home. They talk of how sad they are
    not to be with him, what they will do when he returns, and how their family is
    soon to be one member larger." 
    "Suddenly, the conversation is interrupted by
    the woman clutching her stomach in pain; the new life they were just speaking
    of is ready to be brought into the world."

    "The man awakens in the darkness to find himself lying at the bottom of the cliff
    just before the peak. I am already gone, he realizes with something
    approaching wonder." 
    "He never conquered the cliff, never saw a shrine; it was
    nothing but a fragment of a dream after he fell. Though he can no longer feel
    his fingers, he fumbles in his pocket to pull out the charm from his daughter.
    And with its faint warmth moving through his body, he slowly closes his eyes."

    return 
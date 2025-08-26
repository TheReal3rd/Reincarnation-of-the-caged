# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
define fio = Character ('Fio', color="#eba8dc")
define mama = Character ('Mama', color="#ff0800")
define levania = Character ('Levania', color="#0b0325")
define carrier = Character ('Carrier', color="#fcfcfc")
define rion = Character ('Rion', color="#a1754b")
define galia = Character ('Galia', color="#5f8062")
define dimos = Character ('Dimos', color="#7663b9" )
define akeha = Character ('Akeha', color="#830606" )
define argo = Character ('Argo', color="#182b68")
define prisoner063y = Character ('Prisoner063y', color="#7da19b")
define captivef66x = Character ('CaptiveF66x', color="#62ca81")
define lars = Character ('Lars', color="#81a5db")
define griff = Character ('Griff', color="#364d96")
define noelle = Character ('Noelle', color="#7738a1")
define hina = Character ('Hina', color="#f0d479")
define yuzuki = Character ('Yuzuki', color="#cfd2ff")
define saryu = Character ('Saryu', color="#602d64")
define marie = Character ('Marie', color="#a13864")
define priyet = Character ('Priyet', color="#e2e2e2")
define yurie = Character ('Yurie', color="#6d200d")
define sarafa = Character ('Sarafa', color="#c899e7")
define yudil = Character ('Yudil', color="#b34c4c")
define tenH = Character ('10H', color="#48425c")
define girl = Character ('Girl in Black', color="#1d1d1d")



# The game starts here.
label start:
    # *Alicea Original code.*
    #Prologue Start
    scene image "01_Opening_Scene/BG_disclaimer.jpg"
    "read first"
    with fade
    scene image "01_Opening_Scene/BG_Introduction_Quote.png"
    "-Quote end."
    with fade
    scene image "01_Opening_Scene/BG_CageEstablishingShot_1.png"

    "Massive stone towers pierce an empty sky. This enormous structure is called The Cage.
    In its shadow, a lone girl walks with purpose... And she will not leave until she has what she desires."
    with fade
    "The girl walks down a long path underground with giant black monoliths until she reaches a staircase bringing her to the surface. 
    Suddenly she collapses and finds herself in a cell upon awakening"
    "Walking alone once more along what appears to be inside of a castle she reaches another cell with a unknown being inside of it, the girl approaches it"

    scene image "bg interior 1.jpg"# Missing TODO find the image I can't find it i spent too much time trying to find it. Moving on to next image. Bounty reward = a kiss :3
    
    show fio normal at right
    mama "Well! Look whos finally up."
    show mama default at left
    girl "..........."
    mama "Oh dear. So you did lose your voice after all."
    menu speech:
        "Should I speak?"
        "Try to say something":
            "You try your hardest but no words come out"
        "Give up and stay silent":
            "You are unable to muster any strength"

    mama  "Don't worry. Mama is here to help"
    "The creature called Mama floats away to open the other side of the cell and calls out to you"
    mama "This way."
    mama  "You have lost more than your voice, but you already know that don't you?" # 5:01
    "the two make their way through the corridor until they reach a empty platform, suddenly a staircase descends from above"
    mama "You have lost so much, it's time to reclaim it all. Life will be much harder if you can't speak after all"
    mama "This staircase is the entrance to your prison, a place we call The Cage"
    "They take the stairs and enter the outside of this strange place and then...."
    #Prologue END
    jump grains_of_sand



    

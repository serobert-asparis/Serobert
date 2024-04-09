#Importing necessary modules.
#Importing 'random' will let me pick a random item from a list.
import random
#Importing 'Fore' will let me change text output colors. I used the Python Package Index to help me do this.
from colorama import Fore
#Here I am importing python's operating system and using it to hide pygame's welcome message.
#I used Darrel Lee's stackoverflow answer to help me do this.
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "exists"
import pygame

play_hangman=True
while play_hangman:

    pygame.init()

    #Set a screen, with dimensions 1000 pixels wide by 800 pixels long, using pygame's library for syntax help.
    screen=pygame.display.set_mode((1000,800))

    #Title the screen, using pygame's library for syntax help
    pygame.display.set_caption("Hang-Man!")

    #I used pygame's library for text syntax aid.
    buttontext=pygame.font.Font(None,50)

    #list containing rectangle attributes and text attributes.
    #Will be used to create rectangles with letters inside.
    buttons=(
        #I used pygame's library for rectange and text syntax aid.
        pygame.Rect((200, 500, 50, 50)), buttontext.render("A",True, (0,0,0)),
        pygame.Rect((260, 500, 50, 50)), buttontext.render("B",True, (0,0,0)),
        pygame.Rect((320, 500, 50, 50)), buttontext.render("C",True, (0,0,0)),
        pygame.Rect((380, 500, 50, 50)), buttontext.render("D",True, (0,0,0)),
        pygame.Rect((440, 500, 50, 50)), buttontext.render("E",True, (0,0,0)),
        pygame.Rect((500, 500, 50, 50)), buttontext.render("F",True, (0,0,0)),
        pygame.Rect((560, 500, 50, 50)), buttontext.render("G",True, (0,0,0)),
        pygame.Rect((620, 500, 50, 50)), buttontext.render("H",True, (0,0,0)),
        pygame.Rect((680, 500, 50, 50)), buttontext.render("I",True, (0,0,0)),
        pygame.Rect((740, 500, 50, 50)), buttontext.render("J",True, (0,0,0)),
        
        pygame.Rect((200, 560, 50, 50)), buttontext.render("K",True, (0,0,0)),
        pygame.Rect((260, 560, 50, 50)), buttontext.render("L",True, (0,0,0)),
        pygame.Rect((320, 560, 50, 50)), buttontext.render("M",True, (0,0,0)),
        pygame.Rect((380, 560, 50, 50)), buttontext.render("N",True, (0,0,0)),
        pygame.Rect((440, 560, 50, 50)), buttontext.render("O",True, (0,0,0)),
        pygame.Rect((500, 560, 50, 50)), buttontext.render("P",True, (0,0,0)),
        pygame.Rect((560, 560, 50, 50)), buttontext.render("Q",True, (0,0,0)),
        pygame.Rect((620, 560, 50, 50)), buttontext.render("R",True, (0,0,0)),
        pygame.Rect((680, 560, 50, 50)), buttontext.render("S",True, (0,0,0)),
        pygame.Rect((740, 560, 50, 50)), buttontext.render("T",True, (0,0,0)),
        
        pygame.Rect((320, 620, 50, 50)), buttontext.render("U",True, (0,0,0)),
        pygame.Rect((380, 620, 50, 50)), buttontext.render("V",True, (0,0,0)),
        pygame.Rect((440, 620, 50, 50)), buttontext.render("W",True, (0,0,0)),
        pygame.Rect((500, 620, 50, 50)), buttontext.render("X",True, (0,0,0)),
        pygame.Rect((560, 620, 50, 50)), buttontext.render("Y",True, (0,0,0)),
        pygame.Rect((620, 620, 50, 50)), buttontext.render("Z",True, (0,0,0)), )

    #This is my function to draw buttons of every letter, using the list 'buttons'.
    #Start and end are where in the list the buttons will be drawn.
    #left and down are the coordinates for the text to be drawn inside the rectangles.
    def make_buttons(start,end,left,down):
        x=start
        z=0
        while x<end:
            #I used pygame's library for text syntax aid.
            #Draws the rectangle on the screen, as white in rgb, using the attributes in the list 'buttons'.
            pygame.draw.rect(screen, (255,255,255), (buttons[x]))
            #I used pygame's library for text syntax aid.
            #Blit transfers the text attributes in the list buttons onto the screen.
            screen.blit(buttons[x+1], (left+30*z,down))
            x+=2
            z+=2

    #list containing letters of the alphabet.
    alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

    #Lists of words for different english and frecnh levels altered from a chatGPT generation.
    english_easy = ["house","star", "tree","leaf", "hello","sleep","cook","orange","apple","juice"]
    english_hard = ["jazzy","melancholy","cobweb","hockey","dizzy","acoustic","technology","ridiculous","stuffing","psychology"]
    french_easy = ["bonjour", "merci", "chat", "chien", "maison", "pomme","homme", "femme", "fleur", "soleil"]
    french_hard = ["avion", "ordinateur", "banane", "chocolat", "musique", "jardin", "citron", "trafic", "yaourt", "heureux"]

    #welcome message. I used the Python Package Index to make the text blue.
    print(Fore.BLUE + "Welcome to Hangman!")

    while True:
        #I ask the user for their desired language and difficulty level.
        #I made the typing options a different color than the rest to make a better user experience.
        #I used Fore  from the colorama module to make the text a different color, using the Python Package Index for syntax aid.
        level=input(Fore.BLUE + "Pick a level: type" + Fore.GREEN + "'A'" + Fore.BLUE + "for English easy," + Fore.GREEN + "'B'" + Fore.BLUE + "for English hard," + Fore.GREEN + "'C'" + Fore.BLUE + "for French easy, or" + Fore.GREEN + "'D'" + Fore.BLUE + "for French hard: ").strip().lower()
        #Based on the user's input, the list of their desired words is chosen. 
        if level == 'a':
            lang_skill=english_easy
            break
        elif level == 'b':
            lang_skill=english_hard
            break
        elif level == 'c':
            lang_skill=french_easy
            break
        elif level == 'd':
            lang_skill=french_hard
            break
        #If the user doesn't enter 'a', 'b', 'c', or 'd', the loop continues until they do.
        else:
            print(Fore.RED + "I'm sorry, it looks like you didn't enter a valid option! Please try again")

    #Based on the user's choice, a random word is picked from the list corresponding to their desired language and difficulty.
    word = random.choice(lang_skill)
    selectedword = []
    blankword = []

    for x in range(0,len(word)):
        #Making the list selectedword have an item for each letter of the random word.
        selectedword.append(word[x])
        #Making the list blankword have an item with an underscore for each letter of the random word.
        blankword.append("_ ")

    #Setting a variable for 7 lives (to be decreased).
    lives_left=7

    #Here I am importing 8 hangman drawings that I drew myself using Google Drawings.
    #I am reducing them to half their size.
    i7=pygame.image.load("7Hangman.png")
    width = i7.get_width() / 2
    height = i7.get_height() / 2
    seven=pygame.transform.scale(i7, (width,height))

    i6=pygame.image.load("6Hangman.png")
    six=pygame.transform.scale(i6, (width,height))

    i5=pygame.image.load("5Hangman.png")
    five=pygame.transform.scale(i5, (width,height))

    i4=pygame.image.load("4Hangman.png")
    four=pygame.transform.scale(i4, (width,height))

    i3=pygame.image.load("3Hangman.png")
    three=pygame.transform.scale(i3, (width,height))

    i2=pygame.image.load("2Hangman.png")
    two=pygame.transform.scale(i2, (width,height))

    i1=pygame.image.load("1Hangman.png")
    one=pygame.transform.scale(i1, (width,height))

    #In this drawing, I made the hangman perish to signify defeat.
    i0=pygame.image.load("0Hangman.png")
    zero=pygame.transform.scale(i0, (width,height))

    #I made a drawing for winning, where the hangman is freed. 
    iwon=pygame.image.load("WinHangman.png")
    win=pygame.transform.scale(iwon, (width,height))

    #I used pygame's library for font syntax aid.
    textfont=pygame.font.Font(None, 36)
    #I am displaying trext for correct guesses, incorrect guesses, already guessed, and if the word is completely guessed.
    #So far none of those things have happened, so I want the text to be blank.
    text=textfont.render(" ",True, (0,0,0))

    #I used pygame's library for sound syntax aid.

    #I incorporated the sound of 'Correct Blips' from freesound.org, created by 'CogFireStudios'.
    #This sound is licensed under Creative Commons Zero.
    #https://freesound.org/people/CogFireStudios/sounds/531510/
    correct_sound=pygame.mixer.Sound('correct.wav')

    #I incorporated the sound of 'negative_beeps.wav' from freesound.org, created by 'themusicalnomad'.
    #This sound is licensed under Creative Commons Zero.
    #https://freesound.org/people/themusicalnomad/sounds/253886/
    incorrect_sound=pygame.mixer.Sound('incorrect.wav')

    #I incorporated the sound of 'Click Generic Neutral Static Sound.wav' from freesound.org, created by 'Heshl'.
    #This sound is licensed under Creative Commons Attribution 3.0.
    #https://freesound.org/people/Heshl/sounds/269158/
    already_sound=pygame.mixer.Sound('already.wav')


    #Making an empty list that will contain letters selected by the user.
    alreadyguessed = []
    #This is the function for the user guessing a letter.
    def guessed (letter):
        #The text being displayed is changed globally, so it is not always blank.
        global text
        #The lives_left variable is changed globaly as well, so it can decreases.
        global lives_left
        #the play variable is changed globally when a word is fully guessed.
        global play
        
        #I check how many times the guessed letter has been put in the 'alreadyguessed' list.
        was_it_guessed=alreadyguessed.count(letter)
        #If the guessed letter has been put into 'alreadyguessed' more than once, it has been gusssed more than once.
        if was_it_guessed > 0:
            #I change text to say that the guessed letter has already been guessed.
            text=textfont.render("you have already guessed this letter, try again",True, (0,0,0))
            pygame.mixer.Sound.play(already_sound)
        #If the letter has not been put into 'alreadyguessed' more than once.
        else:
            #The guessed letter is added to the list of letters guessed.
            alreadyguessed.append(letter)
            #I count how many times the letter appears in the selectedword (where each letter is an item).
            letters_correct=selectedword.count(letter)
            #If the letter does not appear, the text is set to "Incorrect" and lives_left is decreased by one.
            if letters_correct == 0:
                text=textfont.render("Incorrect",True, (0,0,0))
                pygame.mixer.Sound.play(incorrect_sound)
                lives_left -=1
            #If the letter does appear, the text is set to "correct".
            #I complete the correct function for the amount of times the letter appears in selectedword.
            elif letters_correct == 1:
                text=textfont.render("Correct",True, (0,0,0))
                correct(1)
            elif letters_correct == 2:
                text=textfont.render("Correct",True, (0,0,0))
                correct(2)
            elif letters_correct == 3:
                text=textfont.render("Correct",True, (0,0,0))
                correct(3)
            
            #I see if all the underscores in blankword have been replaced.
            blanks_left=blankword.count('_ ')
            #If there are no underscores left, the word has been fully guessed and the text is set to say so.
            if blanks_left == 0:
                #I play a victory sound effect.
                
                #I incorporated the sound of 'Fanfare 3 - Rpg' from freesound.org, created by 'colorsCrimsonTears'.
                #This sound is licensed under Creative Commons Zero.
                #https://freesound.org/people/colorsCrimsonTears/sounds/607407/
                won_sound=pygame.mixer.Sound('won.wav')
                pygame.mixer.Sound.play(won_sound)
                
                #I reset the screen.
                screen.fill((150,200,255))
                #I display the winner drawing.
                lives_left = 8
                screen.blit(win, (0,100))
                #I display the full word.
                complete=wordfont.render((word), True, (0,0,0))
                screen.blit(complete, (300,200))
                #I set text to show the victory .
                text=textfont.render("Congratulations, you have guessed the word!",True, (0,0,0))
                screen.blit(text, (300,350))
                #I update the screen with all of the above changes.
                pygame.display.update()
                #After 5 seconds, I end the game by setting 'play' equal to 'False', thus stopping the game loop.
                pygame.time.delay(5000)
                play = False
                
    #My function for if the user guesses a letter correctly.
    def correct (a):
        pygame.mixer.Sound.play(correct_sound)
        #'a' will vary based on how many correct letters there are in the word.
        for x in range (0,int(a)):
            #The first index at which their is the guessed letter is found.
            index1=selectedword.index(guess,0,len(word))
            #Then, that letter is replaced by a period in 'selectedword', so that if there are letter repeats, the rest can be found.
            selectedword[index1]='.'
            #In blankword, which is the underscores dispayed to the user, an underscore is replaced with the correct letter.
            blankword[index1]=guess

    #I incorporated the sound of 'chill background music #2.wav' from freesound.org, created by 'ZHRØ'.
    #This sound is licensed under Creative Commons Attribution 4.0.
    #https://freesound.org/people/ZHRØ/sounds/703713/
    pygame.mixer.music.load('background.wav')
    #I play the audio file on repeat until the program stops.
    pygame.mixer.music.play(-1)

    #This is the game loop. It keeps running as long as play is equal to True.
    play = True
    while play:
        
        #I am filling the screen with a sky blue color, using pygame's library for syntax aid.
        screen.fill((150,200,255))
        
        #I used pygame's library for text syntax aid.
        welcome1=buttontext.render("Welcome to Hang-Man! Click on a letter to guess it!", True, (0,100,0))
        screen.blit(welcome1, (60,20))
        
        lives=buttontext.render(("Lives left: "+ str(lives_left)), True, (200,0,50))
        screen.blit(lives, (400, 60))
        
        #I display the blankword list with elements separated by a space.
        blankjoin=' '.join(blankword)
        wordfont=pygame.font.Font(None,80)
        blank=wordfont.render((blankjoin), True, (0,0,0))
        screen.blit(blank, (300,200))
        
        #I display text, which changes if the user guesses a letter correctly/incorrectly, repeats a guess, or wins/loses.
        screen.blit(text, (300,350))     
        
        #Calling 'make_buttons' function to make three rows of buttons.
        make_buttons(0,20,210,505)
        make_buttons(20,40,210,565)
        make_buttons(40,52,330,625)

        #Used pygame's library for event quit syntax aid.
        #If the user quits, 'play' is set to 'False' which stops the game loop.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = False
            
            #When the user presses on the mousepad, checks to see where the mouse is.
            #I used pygame's library for help with computer press event syntax.
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #I used pygame's library for help with computer press location syntax.
                mouse_position=pygame.mouse.get_pos()
                #Checks if the mouse overlaps with any of the rectangle attributes in the list 'buttons'
                #If so, the index of the rectange attributed is divided by 2
                #to find the index of the corresponding letter, as rectangles occur every two items in 'buttons'
                a=0
                while a<52:
                    #I used pygame's library for collision syntax
                    if buttons[a].collidepoint(mouse_position):
                        guess=str(alphabet[a//2])
                        guessed(guess)
                    a+=2
                    
        #Based on the amount of lives left, imported corresponding hangman drawing is used.
        if lives_left == 7:
            screen.blit(seven, (0,100))
        elif lives_left == 6:
            screen.blit(six, (0,100))
        elif lives_left == 5:
            screen.blit(five, (0,100))
        elif lives_left == 4:
            screen.blit(four, (0,100))
        elif lives_left == 3:
            screen.blit(three, (0,100))
        elif lives_left == 2:
            screen.blit(two, (0,100))
        elif lives_left == 1:
            screen.blit(one, (0,100))
            
        #When the user wins, lives_left is set to 8 to draw the winner drawing.
        elif lives_left == 8:
            screen.blit(win, (0,100))
            
        #If the user has no lives left, they lost.
        else:
            #I play a defeat sound effect.
            
            #I incorporated the sound of 'Video Game Death Sound Effect' from freesound.org, created by 'harrietniamh'.
            #This sound is licensed under Creative Commons Attribution 4.0.
            #https://freesound.org/people/harrietniamh/sounds/415079/
            lost_sound=pygame.mixer.Sound('lost.wav')
            pygame.mixer.Sound.play(lost_sound)
            
            #I reset the screen.
            screen.fill((150,200,255))
            #I display the correct word in grey.
            complete=wordfont.render(("The correct word was: "+''.join(word)), True, (125,125,125))
            screen.blit(complete, (50,500))
            #I display the progress made with the blank word.
            screen.blit(blank, (300,200))
            #I dispay the defeat drawing.
            screen.blit(zero, (0,100))
            #I set text to show the defeat.
            text=textfont.render("I'm sorry, you ran out of lives!",True, (0,0,0))
            screen.blit(text, (300,350))
            #I display the lives left (0).
            lives=buttontext.render("Lives left: 0", True, (200,0,50))
            screen.blit(lives, (400,60))
            #I update the screen with all of the above changes.
            pygame.display.update()
            #After 5 seconds, I end the game by setting 'play' equal to 'False', thus stopping the game loop.
            pygame.time.delay(5000)
            play = False
            
        #Everytime the game loop loops, the screen needs to be updated. I used pygame's library for updating screen syntax aid.
        pygame.display.update()

    #Making sure pygame and all its attributes quit when the game loop ends. Used pygame's library for syntax aid.
    pygame.quit()
    
    while True:
        game_over= input(Fore.YELLOW + "Would you like to play again? (Yes/No): ").lower().strip()
        if 'yes' in game_over:
            print("You got it!")
            break
        elif 'no' in game_over:
            print("Ok, I hope to see you again soon!")
            play_hangman=False
        else:
            print(Fore.MAGENTA + "I'm sorry, it looks like you didn't enter a valid option! Please try again.")

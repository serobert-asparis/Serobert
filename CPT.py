#AP Computer Science Principles Create Performance Task

import pygame
import random
pygame.init()


screen=pygame.display.set_mode((800,800))

pygame.display.set_caption("Hang-Man!")

#I used pygame's library for text syntax
#
buttontext=pygame.font.SysFont(None,50)

#list containing rectangle attributes and text attributes
#Will be used to create rectangles with letters inside
buttons=(
    pygame.Rect((100, 500, 50, 50)), buttontext.render("A",True, (0,0,0)),
    pygame.Rect((160, 500, 50, 50)), buttontext.render("B",True, (0,0,0)),
    pygame.Rect((220, 500, 50, 50)), buttontext.render("C",True, (0,0,0)),
    pygame.Rect((280, 500, 50, 50)), buttontext.render("D",True, (0,0,0)),
    pygame.Rect((340, 500, 50, 50)), buttontext.render("E",True, (0,0,0)),
    pygame.Rect((400, 500, 50, 50)), buttontext.render("F",True, (0,0,0)),
    pygame.Rect((460, 500, 50, 50)), buttontext.render("G",True, (0,0,0)),
    pygame.Rect((520, 500, 50, 50)), buttontext.render("H",True, (0,0,0)),
    pygame.Rect((580, 500, 50, 50)), buttontext.render("I",True, (0,0,0)),
    pygame.Rect((640, 500, 50, 50)), buttontext.render("J",True, (0,0,0)),
    
    pygame.Rect((100, 560, 50, 50)), buttontext.render("K",True, (0,0,0)),
    pygame.Rect((160, 560, 50, 50)), buttontext.render("L",True, (0,0,0)),
    pygame.Rect((220, 560, 50, 50)), buttontext.render("M",True, (0,0,0)),
    pygame.Rect((280, 560, 50, 50)), buttontext.render("N",True, (0,0,0)),
    pygame.Rect((340, 560, 50, 50)), buttontext.render("O",True, (0,0,0)),
    pygame.Rect((400, 560, 50, 50)), buttontext.render("P",True, (0,0,0)),
    pygame.Rect((460, 560, 50, 50)), buttontext.render("Q",True, (0,0,0)),
    pygame.Rect((520, 560, 50, 50)), buttontext.render("R",True, (0,0,0)),
    pygame.Rect((580, 560, 50, 50)), buttontext.render("S",True, (0,0,0)),
    pygame.Rect((640, 560, 50, 50)), buttontext.render("T",True, (0,0,0)),
    
    pygame.Rect((220, 620, 50, 50)), buttontext.render("U",True, (0,0,0)),
    pygame.Rect((280, 620, 50, 50)), buttontext.render("V",True, (0,0,0)),
    pygame.Rect((340, 620, 50, 50)), buttontext.render("W",True, (0,0,0)),
    pygame.Rect((400, 620, 50, 50)), buttontext.render("X",True, (0,0,0)),
    pygame.Rect((460, 620, 50, 50)), buttontext.render("Y",True, (0,0,0)),
    pygame.Rect((520, 620, 50, 50)), buttontext.render("Z",True, (0,0,0)), )

#This is my function to draw buttons of every letter, using the list 'buttons'
def make_buttons(start,end,down,left):
    x=start
    z=0
    while x<end:
        a=buttons[x]
        pygame.draw.rect(screen, (255,255,255), a)
        screen.blit(buttons[x+1], (left+30*z,down))
        x+=2
        z+=2

#list containing letters of the alphabet
alphabet=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')

#Lists of words altered from a chatGPT generation
english_easy = ["house","star", "tree","leaf", "hello","sleep","cook","orange","apple","juice"]
english_hard = ["jazzy","melancholy","cobweb","hockey","dizzy","acoustic","technology","ridiculous","stuffing","psychology"]
french_easy = ["bonjour", "merci", "chat", "chien", "maison", "pomme","homme", "femme", "feur", "soleil"]
french_hard = ["avion", "ordinateur", "banane", "chocolat", "musique", "jardin", "citron", "trafic", "yaourt", "heureux"]

#I ask the user for their desired language and difficulty level
level=input("Welcome to hangman! Pick a level: type 'A' for English easy, 'B' for English hard, 'C'  for French easy, or 'D' for French hard: ").strip().lower()
if 'a' in level:
    lang_skill=english_easy
elif 'b' in level:
    lang_skill=english_hard
elif 'c' in level:
    lang_skill=french_easy
elif 'd' in level:
    lang_skill=french_hard

#Based on the user's choice, a random word is picked from the list corresponding to their desired language and difficulty
word = random.choice(lang_skill)
selectedword = []
blankword = []
alreadyguessed = []
for x in range(0,len(word)):
    selectedword.append(word[x])
    blankword.append("_ ")
textfont=pygame.font.Font(None, 36)
text=textfont.render(" ",True, (0,0,0))

lives_left=7

i7=pygame.image.load("7Hangman.png")
seven=pygame.transform.scale(i7, (i7.get_width() / 2, i7.get_height() / 2))

i6=pygame.image.load("6Hangman.png")
six=pygame.transform.scale(i6, (i6.get_width() / 2, i6.get_height() / 2))

i5=pygame.image.load("5Hangman.png")
five=pygame.transform.scale(i5, (i5.get_width() / 2, i5.get_height() / 2))

i4=pygame.image.load("4Hangman.png")
four=pygame.transform.scale(i4, (i4.get_width() / 2, i4.get_height() / 2))

i3=pygame.image.load("3Hangman.png")
three=pygame.transform.scale(i3, (i3.get_width() / 2, i3.get_height() / 2))

i2=pygame.image.load("2Hangman.png")
two=pygame.transform.scale(i2, (i2.get_width() / 2, i2.get_height() / 2))

i1=pygame.image.load("1Hangman.png")
one=pygame.transform.scale(i1, (i1.get_width() / 2, i1.get_height() / 2))

i0=pygame.image.load("0Hangman.png")
zero=pygame.transform.scale(i0, (i0.get_width() / 2, i0.get_height() / 2))



def correct (a):
    b=int(a)
    for x in range (0,b):
        index1=selectedword.index(guess,0,len(word))
        selectedword[index1]='.'
        blankword[index1]=guess
    
def guessed (c):
    
    global text
    global lives_left
    
    alreadyguessed.append(c)
    was_it_guessed=alreadyguessed.count(c)
    if was_it_guessed > 1:
        text=textfont.render("you have already guessed this letter, try again",True, (0,0,0))
    else:
        letters_correct=selectedword.count(c)
        if letters_correct == 0:
            text=textfont.render("Incorrect",True, (0,0,0))
            lives_left -=1
        elif letters_correct == 1:
            text=textfont.render("Correct",True, (0,0,0))
            correct(1)
        elif letters_correct == 2:
            text=textfont.render("Correct",True, (0,0,0))
            correct(2)
        elif letters_correct == 3:
            text=textfont.render("Correct",True, (0,0,0))
            correct(3)
            
        bes=blankword.count('_ ')
        if bes == 0:
            text=textfont.render("Congratulations, you have guessed the word!",True, (0,0,0))
            
    
play = True
while play:
    
    blankjoin=' '.join(blankword)
    wordfont=pygame.font.Font(None,100)
    blank=wordfont.render(blankjoin, True, (0,0,0))
    screen.blit(blank, (50,50))
    
    screen.fill((0,200,200))
    welcome1=buttontext.render("Welcome to Hang-Man!", True, (255,50,0))
    welcome2=buttontext.render("Click on a letter to guess it!", True, (255,50,0))
    screen.blit(welcome1, (150,20))
    screen.blit(welcome2, (150,50))


    screen.blit(text, (200,350))     
    screen.blit(blank, (200,200))

    make_buttons(0,20,505,110)
    make_buttons(20,40,565,110)
    make_buttons(40,52,625,230)

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position=pygame.mouse.get_pos()
            
            a=0
            while a<52:
                if buttons[a].collidepoint(mouse_position):
                    guess=str(alphabet[a//2])
                    guessed(guess)
                a+=2
    
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
    elif lives_left == 0:
        screen.blit(zero, (0,100))
   
        
    pygame.display.update()
    
pygame.quit()
       
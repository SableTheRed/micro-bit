from microbit import *
import random


#define values of special cards
global Ace
Ace = 11
JACK = 10
QUEEN = 10
KING = 10

#changes value of Ace to 1 if player bust
def checkhigh(hand):
    score = sum(hand)
    if score > 21:
        if Ace in hand:
            hand[hand.index(Ace)] = 1
        score = sum(hand)
    return score


#Moves a card from the deck to the selected hand
def pickacard(deck,hand):
    newcard = random.choice(deck)
    hand.append(newcard)
    deck.remove(newcard)
    return deck,hand

def playgame():
    playerscore = 0
    computerscore = 0

    # array of cards in each suit
    Suit_order = [Ace,2,3,4,5,6,7,8,9,JACK,QUEEN,KING]
    deck = []

    for i in range(4):
        for card in Suit_order:
            deck.append(card)
    
    playerhand = []
    computerhand = []

    #set initial hands for player and computer

    display.scroll("THE CARDS ARE BEING DEALT!")
    x=0

    while x != 2:
        deck,playerhand = pickacard(deck, playerhand)
        deck,computerhand = pickacard(deck, computerhand)
        x = x + 1

    #Allow player to twist or stick
    draw = True
    while draw == True:
        playerscore = checkhigh(playerhand)
        if playerscore > 21:
            draw = False
        elif button_a.was_pressed():
            pickacard(deck,playerhand)
            display.show(Image.ARROW_W)
            sleep(500)
            display.clear()
            sleep(500)
        elif button_b.was_pressed():
            draw = False
            display.show(Image.ARROW_E)
            sleep(500)
            display.clear()
            sleep(500)
            
        else:
            display.scroll("YOUR SCORE IS:")
            display.scroll(playerscore)
            display.scroll("TWIST OR STICK?")
    
    #computer's turn
    display.scroll("COMPUTER'S TURN:")
    computerscore = checkhigh(computerhand)
    while computerscore <= 13:
        pickacard(deck,computerhand)
        computerscore = checkhigh(computerhand)
        display.show(Image.ARROW_W)
        sleep(250)
        display.clear()
        sleep(250)
    display.show(Image.ARROW_E)
    sleep(250)
    display.clear()
    sleep(250)

    #determine and print outcome:
   

    if playerscore > 21:
        display.scroll("BUST! YOU LOSE!")
    elif computerscore > 21:
        display.scroll("COMPUTER IS BUST! YOU WIN!")
    elif playerscore == 21:
        display.scroll("BLACKJACK! YOU WIN!")
    elif playerscore >= computerscore:
        display.scroll("YOUR HAND IS STRONGER! YOU WIN!")
    else:
        display.scroll("YOU LOSE")

    
        

display.scroll("WELCOME TO BLACKJACK!")
display.scroll("TWIST")
display.show(Image.ARROW_W)
sleep(500)
display.clear
sleep(250)
display.scroll("STICK",100)
display.show(Image.ARROW_E)
sleep(500)
display.clear
sleep(250)

playgame()
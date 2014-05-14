# Skeleton Program code for the AQA COMP1 Summer 2014 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA Programmer Team
# developed in the Python 3.2 programming environment
# version 2 edited 06/03/2014

import random
import datetime

NO_OF_RECENT_SCORES = 3

Ace_High = False
Same_Card = False
Change_Made = False

class TCard():
  def __init__(self):
    self.Suit = 0
    self.Rank = 0

class TRecentScore():
  def __init__(self):
    self.Name = ''
    self.Score = 0
    self.Date = "0/0/0"

Deck = [None]
RecentScores = [None]
Choice = ''
holding = ""
holding1 = ""
holding2 = ""

def GetRank(RankNo):
  Rank = ''
  if RankNo == 1:
    Rank = 'Ace'
  elif RankNo == 2:
    Rank = 'Two'
  elif RankNo == 3:
    Rank = 'Three'
  elif RankNo == 4:
    Rank = 'Four'
  elif RankNo == 5:
    Rank = 'Five'
  elif RankNo == 6:
    Rank = 'Six'
  elif RankNo == 7:
    Rank = 'Seven'
  elif RankNo == 8:
    Rank = 'Eight'
  elif RankNo == 9:
    Rank = 'Nine'
  elif RankNo == 10:
    Rank = 'Ten'
  elif RankNo == 11:
    Rank = 'Jack'
  elif RankNo == 12:
    Rank = 'Queen'
  elif RankNo == 13:
    Rank = 'King'
  return Rank

def GetSuit(SuitNo):
  Suit = ''
  if SuitNo == 1:
    Suit = 'Clubs'
  elif SuitNo == 2:
    Suit = 'Diamonds'
  elif SuitNo == 3:
    Suit = 'Hearts'
  elif SuitNo == 4:
    Suit = 'Spades'
  return Suit

def DisplayMenu():
  print()
  print('MAIN MENU')
  print()
  print('1. Play game (with shuffle)')
  print('2. Play game (without shuffle)')
  print('3. Display recent scores')
  print('4. Reset recent scores')
  print('5. Options')
  print()
  print('Select an option from the menu (or enter q to quit): ', end='')

def GetMenuChoice():
  Choice = input()
  Choice = Choice.lower()
  print()
  if Choice == 'quit':
    Choice = 'q'
  return Choice

def LoadDeck(Deck):
  CurrentFile = open('deck.txt', 'r')
  Count = 1
  while True:
    LineFromFile = CurrentFile.readline()
    if not LineFromFile:
      CurrentFile.close()
      break
    Deck[Count].Suit = int(LineFromFile)
    LineFromFile = CurrentFile.readline()
    Deck[Count].Rank = int(LineFromFile)
    Count = Count + 1
 
def ShuffleDeck(Deck):
  SwapSpace = TCard()
  NoOfSwaps = 1000
  for NoOfSwapsMadeSoFar in range(1, NoOfSwaps + 1):
    Position1 = random.randint(1, 52)
    Position2 = random.randint(1, 52)
    SwapSpace.Rank = Deck[Position1].Rank
    SwapSpace.Suit = Deck[Position1].Suit
    Deck[Position1].Rank = Deck[Position2].Rank
    Deck[Position1].Suit = Deck[Position2].Suit
    Deck[Position2].Rank = SwapSpace.Rank
    Deck[Position2].Suit = SwapSpace.Suit

def DisplayCard(ThisCard):
  print()
  print('Card is the', GetRank(ThisCard.Rank), 'of', GetSuit(ThisCard.Suit))
  print()

def GetCard(ThisCard, Deck, NoOfCardsTurnedOver):
    ThisCard.Rank = Deck[1].Rank
    ThisCard.Suit = Deck[1].Suit
    for Count in range(1, 52 - NoOfCardsTurnedOver):
      Deck[Count].Rank = Deck[Count + 1].Rank
      Deck[Count].Suit = Deck[Count + 1].Suit
    Deck[52 - NoOfCardsTurnedOver].Suit = 0
    Deck[52 - NoOfCardsTurnedOver].Rank = 0

    
def IsNextCardHigher(LastCard, NextCard, Choice):
  Higher = False
  if not Ace_High:
    if NextCard.Rank == LastCard.Rank and Same_Card == False:
      Higher = False
    elif NextCard.Rank == LastCard.Rank and Same_Card == True:
      Higher = True
    if NextCard.Rank > LastCard.Rank:
      Higher = True
  elif Ace_High:
    if NextCard.Rank == LastCard.Rank and Same_Card == False:
      Higher = False
    elif NextCard.Rank == LastCard.Rank and Same_Card == True:
      Higher = True
    if LastCard.Rank == 1:
      Higher == False
    elif NextCard.Rank == 1:
      Higher == True
    elif NextCard.Rank > LastCard.Rank:
      Higher = True
  return Higher

def GetPlayerName():
  print()
  PlayerName = input('Please enter your name: ')
  print()
  if PlayerName == '':
    print('please enter something for your name')
  else:
    count = 0
    ValidName = False
    while not ValidName:
      for each in PlayerName:
        check = ord(each)
        if check > 65 and check < 91:
          count+=1
        elif check > 97 and check < 123:
          count += 1
        elif check > 48 and check < 57:
          ValidName = False
      if count == len(PlayerName) or count == len(PlayerName)-1:
        ValidName = True
        print('Valid')
        return PlayerName
      elif ValidName == False:
        print('not Valid')
        GetPlayerName()

def AddToTableChoice():
  Acceptable = False
  PlayerChoice = input('do you want to add your score to the scoreboard: ')
  PlayerChoice = PlayerChoice.lower()
  while not Acceptable:
    if PlayerChoice not in ['y','n']:
      print('that is not a valid input')
      PlayerChoice = input('do you want to add your score to the scoreboard: ')
    elif PlayerChoice in ['y','n']:
      Acceptable = True
  return PlayerChoice

def GetChoiceFromUser():
  print('Do you think the next card will be higher than the last card(Y or N)?')
  print('or do you wish to (S)ave: ',end='')
  Choice = input('')
  Choice = Choice.lower()
  return Choice

def DisplayEndOfGameMessage(Score):
  print()
  print('GAME OVER!')
  print('Your score was', Score)
  if Score == 51:
    print('WOW! You completed a perfect game.')
  print()

def DisplayCorrectGuessMessage(Score):
  print()
  print('Well done! You guessed correctly.')
  print('Your score is now ', Score, '.', sep='')
  print()

def ResetRecentScores(RecentScores):
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores[Count].Name = ''
    RecentScores[Count].Score = 0

def DisplayRecentScores(RecentScores):
  print()
  print('Recent Scores: ')
  print()
  print('{0:<10}{1:<10}{2}'.format("Name", "Date", "Score"))
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    print("{0:<10}{1:<10}{2:<10}".format(RecentScores[Count].Name, RecentScores[Count].Date, RecentScores[Count].Score))
  print()
  print('Press the Enter key to return to the main menu')
  input()
  print()

def UpdateRecentScores(RecentScores, Score):
  PlayerChoice = AddToTableChoice()
  if PlayerChoice in ['yes','y']:
    PlayerName = GetPlayerName()
    FoundSpace = False
    Count = 1
    Date = datetime.datetime.now() 
    The_Date = Date.strftime("%d/%m/%y")
    while (not FoundSpace) and (Count <= NO_OF_RECENT_SCORES):
      if RecentScores[Count].Name == '':
        FoundSpace = True
      else:
        Count = Count + 1
    if not FoundSpace:
      for Count in range(1, NO_OF_RECENT_SCORES):
        RecentScores[Count].Name = RecentScores[Count + 1].Name
        RecentScores[Count].Score = RecentScores[Count + 1].Score
        RecentScores[Count].Date = RecentScores[Count + 1].Date
      Count = NO_OF_RECENT_SCORES
    RecentScores[Count].Name = PlayerName
    RecentScores[Count].Score = Score
    RecentScores[Count].Date = The_Date
  elif PlayerChoice in ['no','n']:
    print('ok not adding to list')
  SortScores(RecentScores)

def SortScores(RecentScores):
  for Count in range(1,NO_OF_RECENT_SCORES):
    if RecentScores[Count].Score >= RecentScores[Count+1].Score:
      pass
    elif RecentScores[Count].Score <= RecentScores[Count+1].Score:
      holding = RecentScores[Count]
      RecentScores[Count] = RecentScores[Count+1]
      RecentScores[Count+1] = holding
      
def PlayGame(Deck, RecentScores):
  LastCard = TCard()
  NextCard = TCard()
  GameOver = False
  print('Ace high is set to {0}'.format(Ace_High))
  print('same_card is set to {0}'.format(Same_Card))
  GetCard(LastCard, Deck, 0)
  DisplayCard(LastCard)
  NoOfCardsTurnedOver = 1
  while (NoOfCardsTurnedOver < 52) and (not GameOver):
    GetCard(NextCard, Deck, NoOfCardsTurnedOver)
    Choice = ''
    while Choice not in ['y','n','yes','no','save','s']:
      Choice = GetChoiceFromUser()
    if Choice in ['y','n','yes','no']:
      DisplayCard(NextCard)
      NoOfCardsTurnedOver = NoOfCardsTurnedOver + 1
      Higher = IsNextCardHigher(LastCard, NextCard, Choice)
      if (Higher and Choice == 'y') or (not Higher and Choice == 'n'):
        DisplayCorrectGuessMessage(NoOfCardsTurnedOver - 1)
        LastCard.Rank = NextCard.Rank
        LastCard.Suit = NextCard.Suit
      else:
        GameOver = True
    elif Choice in ['save','s']:
      pass
      
  if GameOver:
    DisplayEndOfGameMessage(NoOfCardsTurnedOver - 2)
    UpdateRecentScores(RecentScores, NoOfCardsTurnedOver - 2)
  else:
    DisplayEndOfGameMessage(51)
    UpdateRecentScores(RecentScores, 51)

def Get_Option_Choice(Ace_High, Same_Card):
  choice = input('')
  if choice == "1":
    choices = input('please enter your choice: ')
    choices = choices.lower()
    if choices in ['h']:
      Ace_High = True
    elif choices in ['l']:
      Ace_High = False
    elif choices not in ['h','l']:
      print('fine leaving the aces how they are')
  if choice == "2":
    Choice = input('please enter your choice')
    Choice = Choice.lower()
    if Choice in ['yes', 'y']:
      Same_Card = True
    elif Choice in ['yes', 'y']:
      Same_Card = False
    elif Choice in ['no','n']:
     print('ok leaving alone')
  return Ace_High, Same_Card

def Display_Option_Menu(Ace_High, Same_Card):
  print('')
  print('1. change aces to High or Low: ')
  print('2. Card of same score ends game')
  print('')
  Ace_High, Same_Card = Get_Option_Choice(Ace_High, Same_Card)
  return Ace_High, Same_Card

def Save_To_File(RecentScores):
  with open("skeleton_card_deck.txt", mode = 'w', encoding = 'utf-8') as my_file:
    for count in range (1, NO_OF_RECENT_SCORES):
      if RecentScores[count].Date != None:
        my_file.write("{0:<5}{1:<3}{2:<5}".format(RecentScores[count].Name, RecentScores[count].Score,RecentScores[count].Date )+"\n") 
      else:
        print()
        print("score number {0} couldn't be saved".format(count))
        print()
    print('Game saved')
    
if __name__ == '__main__':
  for Count in range(1, 53):
    Deck.append(TCard())
  for Count in range(1, NO_OF_RECENT_SCORES + 1):
    RecentScores.append(TRecentScore())
  Choice = ''
##  try:
##    Load_Recent_Scores()
##  except IOError:
##    Save_to_file(RecentScores)
  while Choice != 'q':
    DisplayMenu()
    Choice = GetMenuChoice()
    if Choice == '1':
      ##  Check_For_Games()
      LoadDeck(Deck)
      ShuffleDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '2':
      LoadDeck(Deck)
      PlayGame(Deck, RecentScores)
    elif Choice == '3':
      DisplayRecentScores(RecentScores)
    elif Choice == '4':
      ResetRecentScores(RecentScores)
    elif Choice == '5':
      Ace_High, Same_Card = Display_Option_Menu(Ace_High, Same_Card)
    elif Choice == '6':
      Save_To_File(RecentScores)
      
      

      

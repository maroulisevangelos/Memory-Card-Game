#για να παίξεις εκτελείς το προγραμμα με RUN και πληκτρολογείς playgame()
from random import shuffle

#κλάση για την τράπουλα


class Deck:
    #δημιουργεί μια τράπουλα σαν άδεια λίστα
    def __init__(self):
        self._deck = []

    #52 κάρτες με κάθε συνδιασμό σειράς( suits) και τιμής( values )
    def kartes52(self):
        #κούπα σπαθί καρό μπαστούνι
        for suit in ['♥', '♣', '♦', '♠']:
            #Jack = 11, Queen = 12, King = 13, Ace = 1
            for value in range(1, 14):
                if value == 11:
                    value = 'J'
                elif value == 12:
                    value = 'Q'
                elif value == 13:
                    value = 'K'
                elif value == 1:
                    value = 'A'
                #τα προσθέτει στην λίστα της τράπουλας
                self._deck.append(str(value) + '-' + suit)
# 40 κάρτες με 10 τιμές: Α(=1),2, 3, 4, 5, 6, 7, 8, 9, 10 για κάθε σειρά: κούπα, μπαστούνι, σπαθί καρό

    def kartes40(self):
        suit = ['♥', '♣', '♦', '♠']
        for x in suit:
            for value in range(1, 11):
                if value == 1:
                    value = 'A'
                self._deck.append(str(value) + x)
    #16 κάρτες

    def kartes16(self):
        suit = ['♥', '♣', '♦', '♠']
        val = ['10', 'J', 'Q', 'K']
        for x in suit:
            for value in val:
                self._deck.append(value + x)
    #η συνάρτηση shuffle αλλάζει τυχαία τη σειρά των καρτών στην τράπουλα

    def Shuffle(self):
        shuffle(self._deck)

    #το  μήκος της λίστας
    def len(self):
        return len(self._deck)


#κλάση για μία κάρτα
class Card:
    #constructor for  card
    def __init__(self, value, suit):
        self._value = value
        if (suit == 'κούπα' or suit == '♥'):
            self._suit = '♥'
        elif (suit == 'σπαθί' or suit == '♣'):
            self._suit = '♣'
        elif (suit == 'καρό' or suit == '♦'):
            self._suit = '♦'
        else:
            self._suit = '♠'

        self._card = self._value + self._suit
        self.state = 'X '
        if ((self._value == 'J') or (self._value == 'Q') or (self._value == 'K') or (self._value == '10')):
            self.axia = 10
        elif self._value == 'A':
            self.axia = 1
        else:
            self.axia = value

    def getvalue(self):
        return (self._value)

    def getaxia(self):
        return(self.axia)

    def equal(self, another):
        if (self._value == another.getvalue()):
            return True
        else:
            return False

    def info(self):
        print('καρτα:  ', self._card, ' αξία:',
              self.axia, ' κατάσταση:  ', self.state)

#κλάση για τον παίκτη


class Player:
    def __init__(self, fullname):
        self.fullname = fullname
        self.grades = 0


#main function για να παίξεις πληκτρολογείς playgame()
def playgame():

    #δημιουργεί 3 τράπουλες και τις ανακατεύει , μία με 16 κάρτες gamedeck1 , μία με 40 κάρτες gamedeck2, μία με 52 κάρτες gamedeck3
    gameDeck3 = Deck()
    gameDeck3.kartes52()
    gameDeck2 = Deck()
    gameDeck2.kartes40()
    gameDeck1 = Deck()
    gameDeck1.kartes16()
    gameDeck1.Shuffle()
    gameDeck2.Shuffle()
    gameDeck3.Shuffle()
    print()
    print('Καλώςήλθατε στο Matching Game')
    n = int(input('Δώστε αριθμό παικτών:  '))
    while n <= 0:
       n = int(input('Δώστε αριθμό παικτών >=1:  '))
    names = []
    for x in range(n):
        name = input('δωσε όνομα παίκτη:  ')
        names.append(name)
    names.sort()
    print()
    print()
    print('Δώστε επίπεδο δυσκολίας')
    print()
    print('Eπιπέδο δυσκολίας 1(Εύκολο): 16 κάρτες')
    currentCard = 0
    for row in range(4):
        print(gameDeck1._deck[currentCard]+'   ' + gameDeck1._deck[currentCard+1] +
              '   ' + gameDeck1._deck[currentCard+2]+'   ' + gameDeck1._deck[currentCard+3])
        print()
        currentCard += 4
    print()
    print('Eπίπεδο δυσκολίας 2(Μέτριο): 40 κάρτες τράπουλας')
    currentCard = 0
    for row in range(4):
        print(' | ' + gameDeck2._deck[currentCard]+' | '+' | ' + gameDeck2._deck[currentCard+1]+' | '+' | ' + gameDeck2._deck[currentCard+2]+' | '+' | ' + gameDeck2._deck[currentCard+3]+' | '+' | ' + gameDeck2._deck[currentCard+4]+' | ' +
              ' | ' + gameDeck2._deck[currentCard+5]+' | '+' | ' + gameDeck2._deck[currentCard+6]+' | '+' | ' + gameDeck2._deck[currentCard+7]+' | '+' | ' + gameDeck2._deck[currentCard+8]+' | '+' | ' + gameDeck2._deck[currentCard+9]+' | ')
        print()
        currentCard += 10
    print()
    print()
    print('Επιπέδο δυσκολίας 3(Δύσκολο): 52 κάρτες τράπουλας')
    currentCard = 0
    for row in range(4):
        print(gameDeck3._deck[currentCard]+'   ' + gameDeck3._deck[currentCard+1]+'   ' + gameDeck3._deck[currentCard+2]+'   ' + gameDeck3._deck[currentCard+3] + '   ' + gameDeck3._deck[currentCard+4]+'   ' + gameDeck3._deck[currentCard+5]+'   ' +
              gameDeck3._deck[currentCard+6]+'   ' + gameDeck3._deck[currentCard+7]+'   ' + gameDeck3._deck[currentCard+8]+'    ' + gameDeck3._deck[currentCard+9]+'   ' + gameDeck3._deck[currentCard+10]+'   ' + gameDeck3._deck[currentCard+11]+'    ' + gameDeck3._deck[currentCard+12])
        print()
        currentCard += 13
    print()

    state16 = 16*['X ']
    state40 = 40*['X ']
    state52 = 52*['X ']

    def ekt16():
       print("η τρέχουσα κατάσταση των 16 καρτών είναι: ('X'= κλειστές)")
       currentCard = 0
       for row in range(4):
         print(state16[currentCard]+'    ' + state16[currentCard+1] +
               '    ' + state16[currentCard+2]+'    ' + state16[currentCard+3])
         print()
         currentCard += 4

    def ekt40():
        print("η τρέχουσα κατάσταση των 40 καρτών είναι: ('X'= κλειστές)")
        currentCard = 0
        for row in range(4):
         print(state40[currentCard]+'  ' + state40[currentCard+1]+'  ' + state40[currentCard+2]+'  ' + state40[currentCard+3] + '  ' + state40[currentCard+4] +
               '  ' + state40[currentCard+5]+'  ' + state40[currentCard+6]+'  ' + state40[currentCard+7]+'  ' + state40[currentCard+8]+'  ' + state40[currentCard+9])
         print()
         currentCard += 10

    def ekt52():
        print("η τρέχουσα κατάσταση των 52 καρτών είναι: ('X'= κλειστές)")
        currentCard = 0
        for row in range(4):
         print(state52[currentCard]+'   ' + state52[currentCard+1]+'   ' + state52[currentCard+2]+'   ' + state52[currentCard+3] + '   ' + state52[currentCard+4]+'   ' + state52[currentCard+5]+'   ' + state52[currentCard+6] +
               '   ' + state52[currentCard+7]+'   ' + state52[currentCard+8]+'    ' + state52[currentCard+9]+'    ' + state52[currentCard+10]+'    ' + state52[currentCard+11]+'    ' + state52[currentCard+12])
         print()
         currentCard += 13

    epipedo = int(input(
        'Δώστε επίπεδο δυσκολίας: 1(εύκολο με 16 κάρτες) ή 2 (μέτριο με 40 κάρτες) ή 3(δύσκολο με 52 κάρτες) :   '))
    while epipedo != 1 and epipedo != 2 and epipedo != 3:
        epipedo = int(input('Δώστε επίπεδο δυσκολίας: 1 ή 2 ή 3 :   '))
    print()
    if epipedo == 1:
        ekt16()
    elif epipedo == 2:
        ekt40()
    else:
        ekt52()

    print()
    print('Θα παίξουν οι:  ', n, ' ακόλουθοι παίκτες κατά αλφαβητική σειρά : ')
    scor = []
    for i in range(1, n+1):
        print(str(i)+'os παίκτης: ', names[i-1])
        scor.append(0)
    print("αρχικοί πόντοι για τους παίκτες μας", scor)

    if epipedo == 1:
      if n != 1:
        found = 0
        paiktis = 1
        print("το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
        while found < 16:
            print()
            print("παίζει ο παίκτης κατά σειρά: ", paiktis)
            ekt16()
            firstpositiongr = int(
                input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
            firstpositionst = int(
                input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
            firstposition = (firstpositiongr-1)*4 + (firstpositionst-1)
            while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 5)) or state16[firstposition] != 'X ':
                print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                print()
                ekt16()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρταςστον πίνακα των καρτών από 1-4 "))
                firstposition = (firstpositiongr-1)*4 + (firstpositionst-1)
            state16[firstposition] = gameDeck1._deck[firstposition]
            ekt16()
            secondpositiongr = int(
                input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
            secondpositionst = int(
                input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
            secondposition = (secondpositiongr-1)*4 + (secondpositionst-1)
            while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 5)) or state16[secondposition] != 'X ' or firstposition == secondposition:
                print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                print()
                ekt16()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondposition = (secondpositiongr-1)*4 + (secondpositionst-1)
            state16[secondposition] = gameDeck1._deck[secondposition]
            ekt16()
            print("άνοιξες τις ακόλουθες κάρτες:")
            print(gameDeck1._deck[firstposition], '   ',
                  gameDeck1._deck[secondposition])
            if gameDeck1._deck[firstposition][0] == gameDeck1._deck[secondposition][0]:
                    state16[firstposition] = gameDeck1._deck[firstposition]
                    state16[secondposition] = gameDeck1._deck[secondposition]
                    found = found+2
                    print(
                       "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχετε βρει συνολικά είναι  ", found)
                    pontoi = 10
                    print("οι πόντοι που κερδίζει o ", str(
                        paiktis)+"ος", " παίκτης είναι: ", pontoi)
                    scor[paiktis-1] = scor[paiktis-1] + pontoi
                    print("οι πόντοι συνολικά είναι: ")
                    print(scor)
                    print("αντίστοιχα με τους παίκτες μας:")
                    print(names)
                    print()
                    ekt16()
                    print()
            elif ((gameDeck1._deck[firstposition][0] == 'Q' and gameDeck1._deck[secondposition][0] == 'K') or (gameDeck1._deck[firstposition][0] == 'K' and gameDeck1._deck[secondposition][0] == 'Q')):
                    print(
                    "άνοιξες μία ντάμα και ένα Ρήγα! Μπορείς να ανοίξεις και μια τρίτη κάρτα")
                    thirdpositiongr = int(
                    input("Δώσε γραμμή τρίτης κάρτας στον πίνακα των καρτών από 1-4 "))
                    thirdpositionst = int(
                    input("Δώσε στήλη τρίτης κάρταςστον πίνακα των καρτών από 1-4 "))
                    thirdposition = (thirdpositiongr-1)*4 + (thirdpositionst-1)
                    while (thirdpositiongr not in range(1, 5) or thirdpositionst not in range(1, 5)) or state16[thirdposition] != 'X ' or (firstposition == thirdposition or secondposition == thirdposition):
                        print(
                            "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                        print()
                        ekt16()
                        thirdpositiongr = int(
                            input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                        thirdpositionst = int(
                            input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                        thirdposition = (thirdpositiongr-1) * \
                            4 + (thirdpositionst-1)
                    state16[thirdposition] = gameDeck1._deck[thirdposition]
                    ekt16()
                    print("άνοιξες την ακόλουθη τρίτη κάρτα:")
                    print(gameDeck1._deck[thirdposition])
                    if (gameDeck1._deck[thirdposition][0] == 'Q' or gameDeck1._deck[thirdposition][0] == 'K'):
                        pontoi = 10
                        scor[paiktis-1] = scor[paiktis-1] + pontoi
                        print(
                            "κερδίζεις 10 πόντους γιατί με την τρίτη κάρτα πέτυχες δύο όμοιες κάρτες")
                        print(" οι πόντοι αντίστοιχα των παικτών είναι")
                        print(scor)
                        found = found+2
                        print("ανοίγουμε τις όμοιες κάρτες")
                        state16[thirdposition] = gameDeck1._deck[thirdposition]
                        if gameDeck1._deck[firstposition][0] == gameDeck1._deck[thirdposition][0]:
                            state16[firstposition] = gameDeck1._deck[firstposition]
                            state16[secondposition] = 'X '
                        else:
                            state16[secondposition] = gameDeck1._deck[secondposition]
                            state16[firstposition] = 'X '
                        ekt16()

                        if gameDeck1._deck[thirdposition][0] == 'K':
                            paiktis = paiktis+1
                            print(
                                "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), ο επόμενος παίκτης χάνει την σειρά του")
                    else:
                        state16[thirdposition] = 'X '
                        state16[firstposition] = 'X '
                        state16[secondposition] = 'X '

            else:
                state16[firstposition] = 'X '
                state16[secondposition] = 'X '

            if (gameDeck1._deck[firstposition][0] == 'J' and gameDeck1._deck[secondposition][0] == 'J'):
                print()
                print("Παίζει ξανά ο ίδιος παίκτης γιατί άνοιξε ταυτόχρονα δύο βαλέδες")
            elif (gameDeck1._deck[firstposition][0] == 'K' and gameDeck1._deck[secondposition][0] == 'K'):
                paiktis = paiktis+2
                print()
                print(
                    "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), ο επόμενος παίκτης χάνει την σειρά του")
                print()
            else:
                paiktis = paiktis+1
            if paiktis > n:
                if paiktis == n+1:
                    paiktis = 1
                else:
                    paiktis = 2
            if found < 16:
              print("...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
              print()

      else:
        scorpaikti = 0
        minescor = 0
        mem = ['', '', '', '', '']
        lpos = []
        import random
        found = 0
        paiktis = 1
        print("το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
        m = 0
        while found < 16:
          if m == 0:
            p = 0
            print()
            print("παίζεις εσύ")
            ekt16()
            firstpositiongr = int(
                input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
            firstpositionst = int(
                input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
            firstposition = (firstpositiongr-1)*4 + (firstpositionst-1)
            while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 5)) or state16[firstposition] != 'X ':
                print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                print()
                ekt16()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρταςστον πίνακα των καρτών από 1-4 "))
                firstposition = (firstpositiongr-1)*4 + (firstpositionst-1)
            state16[firstposition] = gameDeck1._deck[firstposition]
            ekt16()
            secondpositiongr = int(
                input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
            secondpositionst = int(
                input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
            secondposition = (secondpositiongr-1)*4 + (secondpositionst-1)
            while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 5)) or state16[secondposition] != 'X ' or firstposition == secondposition:
                print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                print()
                ekt16()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondposition = (secondpositiongr-1)*4 + (secondpositionst-1)
            state16[secondposition] = gameDeck1._deck[secondposition]
            ekt16()
            print("άνοιξες τις ακόλουθες κάρτες:")
            print(gameDeck1._deck[firstposition], '   ',
                  gameDeck1._deck[secondposition])
            if gameDeck1._deck[firstposition][0] == gameDeck1._deck[secondposition][0]:
                state16[firstposition] = gameDeck1._deck[firstposition]
                state16[secondposition] = gameDeck1._deck[secondposition]
                found = found+2
                print(
                       "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                pontoi = 10
                print("οι πόντοι που κερδίζεις είναι: ", pontoi)
                scorpaikti = scorpaikti + pontoi
                print("οι πόντοι σου συνολικά είναι: ")
                print(scorpaikti)
                print()
                ekt16()
                print()
            elif ((gameDeck1._deck[firstposition][0] == 'Q' and gameDeck1._deck[secondposition][0] == 'K') or (gameDeck1._deck[firstposition][0] == 'K' and gameDeck1._deck[secondposition][0] == 'Q')):
                    print(
                    "άνοιξες μία ντάμα και ένα Ρήγα! Μπορείς να ανοίξεις και μια τρίτη κάρτα")
                    thirdpositiongr = int(
                     input("Δώσε γραμμή τρίτης κάρτας στον πίνακα των καρτών από 1-4 "))
                    thirdpositionst = int(
                      input("Δώσε στήλη τρίτης κάρταςστον πίνακα των καρτών από 1-4 "))
                    thirdposition = (thirdpositiongr-1)*4 + (thirdpositionst-1)
                    while (thirdpositiongr not in range(1, 5) or thirdpositionst not in range(1, 5)) or state16[thirdposition] != 'X ' or (firstposition == thirdposition or secondposition == thirdposition):
                        print(
                            "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                        print()
                        ekt16()
                        thirdpositiongr = int(
                               input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                        thirdpositionst = int(
                                input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                        thirdposition = (thirdpositiongr-1) * \
                                4 + (thirdpositionst-1)
                    state16[thirdposition] = gameDeck1._deck[thirdposition]
                    ekt16()
                    print("άνοιξες την ακόλουθη τρίτη κάρτα:")
                    print(gameDeck1._deck[thirdposition])
                    if (gameDeck1._deck[thirdposition][0] == 'Q' or gameDeck1._deck[thirdposition][0] == 'K'):
                        pontoi = 10
                        scorpaikti = scorpaikti + pontoi
                        print(
                            "κερδίζεις 10 πόντους γιατί με την τρίτη κάρτα πέτυχες δύο όμοιες κάρτες")
                        print(" οι πόντοι σου είναι")
                        print(scorpaikti)
                        found = found+2
                        print("ανοίγουμε τις όμοιες κάρτες")
                        state16[thirdposition] = gameDeck1._deck[thirdposition]
                        if gameDeck1._deck[firstposition][0] == gameDeck1._deck[thirdposition][0]:
                            state16[firstposition] = gameDeck1._deck[firstposition]
                            state16[secondposition] = 'X '
                        else:
                            state16[secondposition] = gameDeck1._deck[secondposition]
                            state16[firstposition] = 'X '
                        ekt16()

                        if gameDeck1._deck[thirdposition][0] == 'K':
                            p = 1
                            print(
                                "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), χάνω την σειρά μου")
                    else:
                        state16[thirdposition] = 'X '
                        state16[firstposition] = 'X '
                        state16[secondposition] = 'X '

            else:
                state16[firstposition] = 'X '
                state16[secondposition] = 'X '

            if (gameDeck1._deck[firstposition][0] == 'J' and gameDeck1._deck[secondposition][0] == 'J'):
                print()
                p = 1
                print("Παίζεις ξανά γιατί άνοιξες ταυτόχρονα δύο βαλέδες")
            elif (gameDeck1._deck[firstposition][0] == 'K' and gameDeck1._deck[secondposition][0] == 'K'):

                print()
                print(
                    "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), χάνω την σειρά μου")
                print()
                p = 1
            if found < 16:
              print("...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
              print()
          if p == 0:
            m = 0
            st1 = 100
            st2 = 100
            ekt16()
            for i in range(5):
                for x in range(5):
                    if mem[i] == mem[x] and mem[i] != '' and i != x:
                        if i < st1:
                           st1 = i
                        else:
                           st2 = i
            if st1 != st2:
                state16[lpos[st1]] = gameDeck1._deck[lpos[st2]]
                state16[lpos[st2]] = gameDeck1._deck[lpos[st2]]
                ekt16()
                print("άνοιξα τις ακόλουθες κάρτες:")
                print(gameDeck1._deck[lpos[st1]],
                      '   ', gameDeck1._deck[lpos[st2]])
                found = found+2
                print(
                    "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                pontoi = 10
                print("οι πόντοι που κερδίζω είναι: ", pontoi)
                minescor = minescor + pontoi
                print("οι πόντοι μου συνολικά είναι: ")
                print(minescor)
                print()
                ekt16()
                print()
                if (gameDeck1._deck[lpos[st1]][0] == 'J' and gameDeck1._deck[lpos[st2]][0] == 'J'):
                    print()
                    m = 1
                    print("Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                elif (gameDeck1._deck[lpos[st1]][0] == 'K' and gameDeck1._deck[lpos[st2]][0] == 'K'):

                    print()
                    print(
                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                    print()
                    m = 1
                if found < 16:
                    print(
                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                    print()
                mem.remove(mem[st2])
                mem.remove(mem[st1])
                lpos.remove(lpos[st2])
                lpos.remove(lpos[st1])
                mem.append('')
                mem.append('')
            else:
                grammi = random.choice(range(1, 5))
                stili = random.choice(range(1, 5))
                position = (grammi-1)*4 + (stili-1)
                while (grammi not in range(1, 5) or stili not in range(1, 5)) or state16[position] != 'X ':
                    grammi = random.choice(range(1, 5))
                    stili = random.choice(range(1, 5))
                    position = (grammi-1)*4 + (stili-1)
                state16[position] = gameDeck1._deck[position]
                ekt16()
                y = gameDeck1._deck[position]
                st2 = 100
                for x in range(5):
                    if y == mem[x]:
                        st2 = x

                if st2 != 100:
                    state16[lpos[st2]] = gameDeck1._deck[lpos[st2]]
                    ekt16()
                    print("άνοιξα τις ακόλουθες κάρτες:")
                    print(gameDeck1._deck[position],
                          '   ', gameDeck1._deck[lpos[st2]])
                    found = found+2
                    print(
                        "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)

                    pontoi = 10
                    print("οι πόντοι που κερδίζω είναι: ", pontoi)
                    minescor = minescor + pontoi
                    print("οι πόντοι μου συνολικά είναι: ")
                    print(minescor)
                    print()
                    ekt16()
                    print()
                    if gameDeck1._deck[position][0] == 'J' and gameDeck1._deck[lpos[st2]][0] == 'J':
                        print()
                        m = 1
                        print("Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                    elif (gameDeck1._deck[position][0] == 'K' and gameDeck1._deck[lpos[st2]][0] == 'K'):

                        print()
                        print(
                            "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                        print()
                        m = 1
                    if found < 16:
                       print(
                           "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                       print()

                    mem.remove(mem[st2])
                    lpos.remove(lpos[st2])
                    mem.append('')
                else:
                    grammi2 = random.choice(range(1, 5))
                    stili2 = random.choice(range(1, 15))
                    position2 = (grammi2-1)*4 + (stili2-1)
                    while (grammi2 not in range(1, 5) or stili2 not in range(1, 5)) or state16[position2] != 'X ' or position == position2:
                        grammi2 = random.choice(range(1, 5))
                        stili2 = random.choice(range(1, 5))
                        position2 = (grammi2-1)*4 + (stili2-1)
                    state16[position2] = gameDeck1._deck[position2]
                    ekt16()
                    print("άνοιξα τις ακόλουθες κάρτες:")
                    print(gameDeck1._deck[position],
                          '   ', gameDeck1._deck[position2])
                    if gameDeck1._deck[position][0] == gameDeck1._deck[position2][0]:
                        state16[position] = gameDeck1._deck[position]
                        state16[position2] = gameDeck1._deck[position2]
                        found = found+2
                        print(
                            "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                        pontoi = 10
                        print("οι πόντοι που κερδίζω είναι: ", pontoi)
                        minescor = minescor + pontoi
                        print("οι πόντοι μου συνολικά είναι: ")
                        print(minescor)
                        print()
                        ekt16()
                        print()
                    elif ((gameDeck1._deck[lpos[st1]][0] == 'Q' and gameDeck1._deck[lpos[st2]][0] == 'K') or (gameDeck1._deck[lpos[st1]][0] == 'K' and gameDeck1._deck[lpos[st2]][0] == 'Q')):
                        print(
                            "άνοιξα μία ντάμα και ένα Ρήγα! Μπορώ να ανοίξω και μια τρίτη κάρτα")
                        st3 = 100
                        ekt16()
                        for i in range(5):
                            if (mem[i] == mem[st1] and i != st1) or (mem[i] == mem[st2] and i != st2):                                
                                st3 = i

                        if st3 != 100:
                            state16[lpos[st3]] = gameDeck1._deck[lpos[st3]]
                            ekt16()
                            print("άνοιξα την ακόλουθη τρίτη κάρτα:")
                            print(gameDeck1._deck[lpos[st3]])
                            if (gameDeck1._deck[lpos[st3]][0] == 'Q' or gameDeck1._deck[lpos[st3]][0] == 'K'):
                                pontoi = 10
                                minescor = minescore + pontoi
                                print(
                                    "κερδίζω 10 πόντους γιατί με την τρίτη κάρτα πέτυχα δύο όμοιες κάρτες")
                                print(" οι πόντοι μου είναι")
                                print(minescor)
                                found = found+2
                                print("ανοίγουμε τις όμοιες κάρτες")
                                state16[lpos[st3]] = gameDeck1._deck[lpos[st3]]
                                if gameDeck1._deck[lpos[st1]][0] == gameDeck1._deck[lpos[st3]][0]:
                                    state16[lpos[st1]
                                            ] = gameDeck1._deck[lpos[st1]]
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck1._deck[lpos[st2]][0])
                                    state16[lpos[st2]] = 'X '
                                else:
                                    state16[lpos[st2]
                                            ] = gameDeck1._deck[lpos[st2]]
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck1._deck[lpos[st1]][0])
                                    state16[lpos[st1]] = 'X '
                                ekt16()

                                if gameDeck1._deck[lpos[st3]] == 'K':
                                    m = 1
                                    print(
                                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις τη σειρά σου")
                            else:
                                mem.pop()
                                mem.pop()
                                mem.pop()
                                mem.insert(0, gameDeck1._deck[lpos[st3]][0])
                                mem.insert(1, gameDeck1._deck[lpos[st2]][0])
                                mem.insert(2, gameDeck1._deck[lpos[st1]][0])
                                lpos.insert(0, position3)
                                lpos.insert(1, position2)
                                lpos.insert(2, position)
                                state16[lpos[st3]] = 'X '
                                state16[lpos[st1]] = 'X '
                                state16[lpos[st2]] = 'X '
                        else:
                            grammi3 = random.choice(range(1, 5))
                            stili3 = random.choice(range(1, 5))
                            position3 = (grammi-1)*4 + (stili-1)
                            while (grammi not in range(1, 5) or stili not in range(1, 5)) or state16[position3] != 'X ':
                                grammi3 = random.choice(range(1, 5))
                                stili3 = random.choice(range(1, 5))
                                position3 = (grammi-1)*4 + (stili-1)
                            state16[position3] = gameDeck1._deck[position3]
                            ekt16()
                            if (gameDeck1._deck[position3][0] == 'Q' or gameDeck1._deck[position3][0] == 'K'):
                                pontoi = 10
                                minescor = minescore + pontoi
                                print(
                                    "κερδίζω 10 πόντους γιατί με την τρίτη κάρτα πέτυχα δύο όμοιες κάρτες")
                                print(" οι πόντοι μου είναι")
                                print(minescor)
                                found = found + 2
                                print("ανοίγουμε τις όμοιες κάρτες")
                                state16[position3] = gameDeck1._deck[position3]
                                if gameDeck1._deck[position][0] == gameDeck1._deck[position3][0]:
                                    state16[position]= gameDeck1._deck[position]
                                    mem.pop()
                                    mem.insert(
                                    0, gameDeck1._deck[position2][0])
                                    state16[position2] = 'X '
                                else:
                                    state16[position2] = gameDeck1._deck[position2]
                                    mem.pop()
                                    mem.insert(0, gameDeck1._deck[position][0])
                                    state16[position] = 'X '

                                    ekt16()

                                if gameDeck1._deck[position3] == 'K':
                                    m = 1
                                    print(
                                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις τη σειρά σου")
                                else:
                                    mem.pop()
                                    mem.pop()
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck1._deck[position3][0])
                                    mem.insert(
                                        1, gameDeck1._deck[position2][0])
                                    mem.insert(2, gameDeck1._deck[position][0])
                                    lpos.insert(0, position3)
                                    lpos.insert(1, position2)
                                    lpos.insert(2, position)
                                    state16[position3]= 'X '
                                    state16[position]= 'X '
                                    state16[position2]= 'X '


                            else:
                                    mem.pop()
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck1._deck[position2][0])
                                    mem.insert(1, gameDeck1._deck[position][0])
                                    state16[position]= 'X '
                                    state16[position2]= 'X '

                            if (gameDeck1._deck[position][0] == 'J' and gameDeck1._deck[position2][0] == 'J'):
                                    print()
                                    m= 1
                                    print(
                                        "Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                            elif (gameDeck1._deck[position][0] == 'K' and gameDeck1._deck[position2][0] == 'K'):

                                    print()
                                    print(
                                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                                    print()
                                    m = 1
                                  if found < 16:
                                    print(
                                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()
                                  elif epipedo == 2:
                                   if n != 1:
                                    found = 0
                                    paiktis = 1
                                    print(
                                        "το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
                                    while found < 40:
                                    print()
                                    print(
                                        "παίζει ο παίκτης κατά σειρά: ", paiktis)
                                    ekt40()
                                    firstpositiongr= int(
                                        input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    firstpositionst= int(
                                        input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-10 "))
                                    firstposition= (firstpositiongr-1)*10 + (firstpositionst-1)
                                    while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 11)) or state40[firstposition] != 'X ':
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt40()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών από 1-10 "))
                firstposition = (firstpositiongr-1)*10 + (firstpositionst-1)
                                    state40[firstposition]= gameDeck2._deck[firstposition]
                                    ekt40()
                                    secondpositiongr= int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    secondpositionst= int(
                                        input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-10 "))
                                    secondposition= (secondpositiongr-1)*10 + (secondpositionst-1)
                                    while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 11)) or state40[secondposition] != 'X ' or firstposition == secondposition:
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt40()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-10 "))
                secondposition = (secondpositiongr-1)*10 + (secondpositionst-1)
                                    state40[secondposition]= gameDeck2._deck[secondposition]
                                    ekt40()

                                    print("άνοιξες τις ακόλουθες κάρτες:")
                                    print(gameDeck2._deck[firstposition], '   ',
                                          gameDeck2._deck[secondposition])
                                    if gameDeck2._deck[firstposition][0] == gameDeck2._deck[secondposition][0]:
                state40[firstposition] = gameDeck2._deck[firstposition]
                state40[secondposition] = gameDeck2._deck[secondposition]
                found = found+2
                                    print(
                    "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχετε βρει συνολικά είναι  ", found)
                                    if gameDeck2._deck[firstposition][1] == '0':
                    pontoi = 10
                                    else:
                    c = Card(gameDeck2._deck[firstposition]
                                        [0], gameDeck2._deck[firstposition][1])
                    pontoi = int(c.axia)

                                    print("οι πόντοι που κερδίζει o ", str(
                    paiktis)+"ος", " παίκτης είναι: ", pontoi)
                scor[paiktis-1] = scor[paiktis-1] + pontoi
                                    print("οι πόντοι συνολικά είναι: ")
                                    print(scor)
                                    print()
                                    ekt40()
                                    print()
                                    else:
                state40[firstposition] = 'X '
                state40[secondposition] = 'X '
                                    if found < 40:
                                    print(
                    "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()
                                    paiktis= paiktis+1
                                    if paiktis > n:
                paiktis = 1
                                    else:
                                    scorpaikti= 0
                                    minescor= 0
                                    mem= ['', '', '', '', '']
                                    lpos= []
                                    import random
                                    found= 0
                                    paiktis= 1
                                    print(
                                        "το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
                                    while found < 40:
                                    print()
                                    print("παίζεις εσύ")
                                    ekt40()
                                    firstpositiongr= int(
                                        input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    firstpositionst= int(
                                        input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-10 "))
                                    firstposition= (firstpositiongr-1)*10 + (firstpositionst-1)
                                    while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 11)) or state40[firstposition] != 'X ':
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt40()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών από 1-10 "))
                firstposition = (firstpositiongr-1)*10 + (firstpositionst-1)
                                    state40[firstposition]= gameDeck2._deck[firstposition]
                                    ekt40()
                                    secondpositiongr= int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    secondpositionst= int(
                                        input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-10 "))
                                    secondposition= (secondpositiongr-1)*10 + (secondpositionst-1)
                                    while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 11)) or state40[secondposition] != 'X ' or firstposition == secondposition:
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt40()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-10 "))
                secondposition = (secondpositiongr-1)*10 + (secondpositionst-1)
                                    state40[secondposition]= gameDeck2._deck[secondposition]
                                    ekt40()

                                    print("άνοιξες τις ακόλουθες κάρτες:")
                                    print(gameDeck2._deck[firstposition], '   ',
                                          gameDeck2._deck[secondposition])
                                    if gameDeck2._deck[firstposition][0] == gameDeck2._deck[secondposition][0]:
                state40[firstposition] = gameDeck2._deck[firstposition]
                state40[secondposition] = gameDeck2._deck[secondposition]
                found = found+2
                                    print(
                    "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχoουμε βρει συνολικά είναι  ", found)
                                    if gameDeck2._deck[firstposition][1] == '0':
                    pontoi = 10
                                    else:
                    c = Card(gameDeck2._deck[firstposition]
                                        [0], gameDeck2._deck[firstposition][1])
                    pontoi = int(c.axia)

                                    print("οι πόντοι που κερδίζεις είναι: ", pontoi)
                scorpaikti = scorpaikti + pontoi
                                    print("οι πόντοι σου συνολικά είναι: ")
                                    print(scorpaikti)
                                    print()
                                    ekt40()
                                    print()
                                    else:
                state40[firstposition] = 'X '
                state40[secondposition] = 'X '
                                    if found < 40:
                                    print(
                    "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()
                                    st1= 100
                                    st2= 100
                                    ekt40()
                                    for i in range(5):
                                    for x in range(5):
                    if mem[i] == mem[x] and mem[i] != '' and i != x:
                        if i < st1:
                                    st1= i
                        else:
                                    st2= i

                                    if st1 != st2:
                state40[lpos[st1]] = gameDeck2._deck[lpos[st2]]
                state40[lpos[st2]] = gameDeck2._deck[lpos[st2]]
                                    ekt40()
                                    print("άνοιξα τις ακόλουθες κάρτες:")
                                    print(gameDeck2._deck[lpos[st1]],
                                        '   ', gameDeck2._deck[lpos[st2]])

                found = found+2
                                    print(
                    "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                                    if gameDeck2._deck[lpos[st1]][1] == '0':
                    pontoi = 10
                                    else:
                    c = Card(gameDeck2._deck[lpos[st1]]
                                        [0], gameDeck2._deck[lpos[st1]][1])
                    pontoi = int(c.axia)

                                    print("οι πόντοι που κερδίζω είναι: ", pontoi)
                minescor = minescor + pontoi
                                    print("οι πόντοι μου συνολικά είναι: ")
                                    print(minescor)
                                    print()
                                    ekt40()
                                    print()
                                    if found < 40:
                    print(
                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                    print()

                                    mem.remove(mem[st2])
                                    mem.remove(mem[st1])
                                    lpos.remove(lpos[st2])
                                    lpos.remove(lpos[st1])
                                    mem.append('')
                                    mem.append('')
                                    else:
                grammi = random.choice(range(1, 5))
                stili = random.choice(range(1, 11))
                position = (grammi-1)*10 + (stili-1)
                                    while (grammi not in range(1, 5) or stili not in range(1, 11)) or state40[position] != 'X ':
                                    grammi= random.choice(range(1, 5))
                                    stili= random.choice(range(1, 11))
                                    position= (grammi-1)*10 + (stili-1)
                state40[position] = gameDeck2._deck[position]
                                    ekt40()
                y = gameDeck2._deck[position]
                st2 = 100
                                    for x in range(5):
                    if y == mem[x]:
                        st2 = x

                                    if st2 != 100:
                    state40[lpos[st2]] = gameDeck2._deck[lpos[st2]]
                    ekt40()
                    print("άνοιξα τις ακόλουθες κάρτες:")
                    print(gameDeck2._deck[position],
                                        '   ', gameDeck2._deck[lpos[st2]])
                    found = found+2
                    print(
                        "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                    if gameDeck2._deck[position][1] == '0':
                        pontoi = 10
                    else:
                        c = Card(gameDeck2._deck[position]
                                        [0], gameDeck2._deck[position][1])
                        pontoi = int(c.axia)

                    print("οι πόντοι που κερδίζω είναι: ", pontoi)
                    minescor = minescor + pontoi
                    print("οι πόντοι μου συνολικά είναι: ")
                    print(minescor)
                    print()
                    ekt40()
                    print()
                    if found < 40:
                                    print(
                                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()

                    mem.remove(mem[st2])
                    lpos.remove(lpos[st2])
                    mem.append('')
                                    else:
                    grammi2 = random.choice(range(1, 5))
                    stili2 = random.choice(range(1, 11))
                    position2 = (grammi2-1)*10 + (stili2-1)
                    while (grammi2 not in range(1, 5) or stili2 not in range(1, 11)) or state40[position2] != 'X ' or position == position2:
                        grammi2 = random.choice(range(1, 5))
                        stili2 = random.choice(range(1, 11))
                        position2 = (grammi2-1)*10 + (stili2-1)
                    state40[position2] = gameDeck2._deck[position2]
                    ekt40()
                    print("άνοιξα τις ακόλουθες κάρτες:")
                    print(gameDeck2._deck[position],
                                        '   ', gameDeck2._deck[position2])
                    if gameDeck2._deck[position][0] == gameDeck2._deck[position2][0]:
                        state40[position] = gameDeck2._deck[position]
                        state40[position2] = gameDeck2._deck[position2]
                        found = found+2
                        print(
                            "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                        if gameDeck2._deck[position][1] == '0':
                            pontoi = 10
                        else:
                            c = Card(
                                gameDeck2._deck[position][0], gameDeck2._deck[position][1])
                            pontoi = int(c.axia)

                        print("οι πόντοι που κερδίζω είναι: ", pontoi)
                        minescor = minescor + pontoi
                        print("οι πόντοι σου συνολικά είναι: ")
                        print(minescor)
                        print()
                        ekt40()
                        print()
                    else:

                        mem.pop()
                        mem.pop()
                        mem.insert(0, gameDeck2._deck[position2][0])
                        mem.insert(1, gameDeck2._deck[position][0])
                        lpos.insert(0, position2)
                        lpos.insert(1, position)
                        state40[position] = 'X '
                        state40[position2] = 'X '

                    if found < 40:
                        print(
                            "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                        print()
                                    else:
                                    if n != 1:
                                    found= 0
                                    paiktis= 1
                                    print(
                                        "το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
                                    while found < 52:
                                    print()
                                    print(
                                        "παίζει ο παίκτης κατά σειρά: ", paiktis)
                                    ekt52()
                                    firstpositiongr= int(
                                        input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    firstpositionst= int(
                                        input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-13 "))
                                    firstposition= (firstpositiongr-1)*13 + (firstpositionst-1)
                                    while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 14)) or state52[firstposition] != 'X ':
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  την κάρτα που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt52()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-13 "))
                firstposition = (firstpositiongr-1)*13 + (firstpositionst-1)
                                    state52[firstposition]= gameDeck3._deck[firstposition]
                                    ekt52()
                                    secondpositiongr= int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    secondpositionst= int(
                                        input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-13 "))
                                    secondposition= (secondpositiongr-1)*13 + (secondpositionst-1)
                                    while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 14)) or state52[secondposition] != 'X ' or firstposition == secondposition:
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  την κάρτα που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt52()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-13 "))
                secondposition = (secondpositiongr-1)*13 + (secondpositionst-1)
                                    state52[secondposition]= gameDeck3._deck[secondposition]
                                    ekt52()

                                    print("άνοιξες τις ακόλουθες κάρτες:")
                                    print(gameDeck3._deck[firstposition], '   ',
                                          gameDeck3._deck[secondposition])
                                    if gameDeck3._deck[firstposition][0] == gameDeck3._deck[secondposition][0]:
                    state52[firstposition] = gameDeck3._deck[firstposition]
                    state52[secondposition] = gameDeck3._deck[secondposition]
                    found = found+2
                    print(
                        "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχετε βρει συνολικά είναι  ", found)
                    ekt52()
                    if gameDeck3._deck[firstposition][1] == '0':
                        pontoi = 10
                    else:
                        c = Card(
                            gameDeck3._deck[firstposition][0], gameDeck3._deck[firstposition][1])
                        pontoi = int(c.axia)
                    print("οι πόντοι που κερδίζει o ", str(
                        paiktis)+"ος", " παίκτης είναι: ", pontoi)
                    scor[paiktis-1] = scor[paiktis-1] + pontoi
                    print("οι πόντοι συνολικά είναι: ")
                    print(scor)
                    print(names)
                    print()
                                    elif ((gameDeck3._deck[firstposition][0] == 'Q' and gameDeck3._deck[secondposition][0] == 'K') or (gameDeck3._deck[firstposition][0] == 'K' and gameDeck3._deck[secondposition][0] == 'Q')):
                    print(
                                        "άνοιξες μία ντάμα και ένα Ρήγα! Μπορείς να ανοίξεις και μια τρίτη κάρτα")
                    thirdpositiongr = int(input("Δώσε γραμμή τρίτης κάρτας στον πίνακα των καρτών από 1-4 "))
                    thirdpositionst = int(
                                        input("Δώσε στήλη τρίτης κάρταςστον πίνακα των καρτών από 1-13 "))
                    thirdposition= (thirdpositiongr-1) *
                                    13 + (thirdpositionst-1)
                    while (thirdpositiongr not in range(1, 5) or thirdpositionst not in range(1, 14)) or state52[thirdposition] != 'X ' or (firstposition == thirdposition or secondposition == thirdposition):
                            print()
                            ekt52()
                            print(
                                        "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                            thirdpositiongr = int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                            thirdpositionst = int(
                                input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                            thirdposition= (thirdpositiongr-1) *
                                    13 + (thirdpositionst-1)
                    state52[thirdposition] = gameDeck3._deck[thirdposition]
                    ekt52()
                    print("άνοιξες την ακόλουθη τρίτη κάρτα:")
                    print(gameDeck3._deck[thirdposition])
                    if (gameDeck3._deck[thirdposition][0] == 'Q' or gameDeck3._deck[thirdposition][0] == 'K'):
                        pontoi = 10
                        scor[paiktis-1] = scor[paiktis-1] + pontoi
                        print(
                            "κερδίζεις 10 πόντους γιατί με την τρίτη κάρτα πέτυχες δύο όμοιες κάρτες")
                        print(" οι πόντοι αντίστοιχα των παικτών είναι")
                        print(scor)
                        found = found+2
                        print("ανοίγουμε τις όμοιες κάρτες")
                        state52[thirdposition] = gameDeck3._deck[thirdposition]
                        if gameDeck3._deck[firstposition][0] == gameDeck3._deck[thirdposition][0]:
                            state52[firstposition] = gameDeck3._deck[firstposition]
                            state52[secondposition] = 'X '
                        else:
                            if gameDeck3._deck[secondposition][0] == gameDeck3._deck[thirdposition][0]:
                                state52[secondposition] = gameDeck3._deck[secondposition]
                                state52[firstposition] = 'X '
                    else:
                        state52[thirdposition] = 'X '
                        state52[firstposition] = 'X '
                        state52[secondposition] = 'X '
                    ekt52()
                    if gameDeck3._deck[thirdposition][0] == 'K':
                        paiktis = paiktis+1
                        print(
                            "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), ο επόμενος παίκτης χάνει την σειρά του")

                                    else:
                state52[firstposition] = 'X '

                state52[secondposition] = 'X '

                                    if found < 52:
                                    print(
                    "...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    ekt52()
                                    print()
                                    if (gameDeck3._deck[firstposition][0] == 'J' and gameDeck3._deck[secondposition][0] == 'J'):
                                    print()
                                    print("Παίζει ξανά ο ίδιος παίκτης γιατί άνοιξε ταυτόχρονα δύο βαλέδες")
                                    elif (gameDeck3._deck[firstposition][0] == 'K' and gameDeck3._deck[secondposition][0] == 'K'):
                paiktis = paiktis+2
                                    print()
                                    print(
                    "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), ο επόμενος παίκτης χάνει την σειρά του")
                                    print()
                                    else:
                paiktis = paiktis+1
                                    if paiktis > n:
                                    if paiktis == n+1:
                    paiktis = 1
                                    else:
                    paiktis = 2
                                    else:
                                    scorpaikti= 0
                                    minescor= 0
                                    mem= ['', '', '', '', '']
                                    lpos= []
                                    import random
                                    found= 0
                                    paiktis= 1
                                    print(
                                        "το παιχνίδι αρχίζει! Μάντεψε τις θέσεις δύο όμοιων καρτών")
                                    m= 0
                                    while found < 52:
                                    if m == 0:
                                    p= 0
                                    print()
                                    print("παίζεις εσύ")
                                    ekt52()
                                    firstpositiongr= int(
                                        input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    firstpositionst= int(
                                        input("Δώσε στήλη πρώτης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    firstposition= (firstpositiongr-1)*13 + (firstpositionst-1)
                                    while (firstpositiongr not in range(1, 5) or firstpositionst not in range(1, 14)) or state52[firstposition] != 'X ':
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt16()
                firstpositiongr = int(
                    input("Δώσε γραμμή πρώτης κάρτας στον πίνακα των καρτών από 1-4 "))
                firstpositionst = int(
                    input("Δώσε στήλη πρώτης κάρταςστον πίνακα των καρτών από 1-4 "))
                firstposition = (firstpositiongr-1)*13 + (firstpositionst-1)
                                    state52[firstposition]= gameDeck3._deck[firstposition]
                                    ekt52()
                                    secondpositiongr= int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    secondpositionst= int(
                                        input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών, από 1-4 "))
                                    secondposition= (secondpositiongr-1)*13 + (secondpositionst-1)
                                    while (secondpositiongr not in range(1, 5) or secondpositionst not in range(1, 14)) or state52[secondposition] != 'X ' or firstposition == secondposition:
                                    print(
                    "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                                    print()
                                    ekt52()
                secondpositiongr = int(
                    input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondpositionst = int(
                    input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                secondposition = (secondpositiongr-1)*4 + (secondpositionst-1)
                                    state52[secondposition]= gameDeck3._deck[secondposition]
                                    ekt52()
                                    print("άνοιξες τις ακόλουθες κάρτες:")
                                    print(gameDeck3._deck[firstposition], '   ',
                                          gameDeck3._deck[secondposition])
                                    if gameDeck3._deck[firstposition][0] == gameDeck3._deck[secondposition][0]:
                    state52[firstposition] = gameDeck3._deck[firstposition]
                    state52[secondposition] = gameDeck3._deck[secondposition]
                    found = found+2
                    print(
                        "μπράβο βρήκες δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                    pontoi = 10
                    print("οι πόντοι που κερδίζεις είναι: ", pontoi)
                    scorpaikti = scorpaikti + pontoi
                    print("οι πόντοι σου συνολικά είναι: ")
                    print(scorpaikti)
                    print()
                    ekt16()
                    print()
                                    elif ((gameDeck3._deck[firstposition][0] == 'Q' and gameDeck3._deck[secondposition][0] == 'K') or (gameDeck3._deck[firstposition][0] == 'K' and gameDeck3._deck[secondposition][0] == 'Q')):
                    print(
                        "άνοιξες μία ντάμα και ένα Ρήγα! Μπορείς να ανοίξεις και μια τρίτη κάρτα")
                    thirdpositiongr = int(
                        input("Δώσε γραμμή τρίτης κάρτας στον πίνακα των καρτών από 1-4 "))
                    thirdpositionst = int(
                        input("Δώσε στήλη τρίτης κάρταςστον πίνακα των καρτών από 1-4 "))
                    thirdposition = (thirdpositiongr-1)*13 + (thirdpositionst-1)
                    while (thirdpositiongr not in range(1, 5) or thirdpositionst not in range(1, 14)) or state52[thirdposition] != 'X ' or (firstposition == thirdposition or secondposition == thirdposition):
                            print(
                                "Error!!!........ ΠΡΟΣΟΧΗ!!! Δώσε ΣΩΣΤΑ  τις κάρτες που θέλεις να ανοίξεις.....")
                            print()
                            ekt52()
                            thirdpositiongr = int(
                                        input("Δώσε γραμμή δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                            thirdpositionst = int(
                                input("Δώσε στήλη δεύτερης κάρτας στον πίνακα των καρτών από 1-4 "))
                            thirdposition = (thirdpositiongr-1) * 13 + (thirdpositionst-1)
                    state52[thirdposition] = gameDeck3._deck[thirdposition]
                    ekt52()
                    print("άνοιξες την ακόλουθη τρίτη κάρτα:")
                    print(gameDeck3._deck[thirdposition])
                    if (gameDeck3._deck[thirdposition][0] == 'Q' or gameDeck3._deck[thirdposition][0] == 'K'):
                        pontoi = 10
                        scorpaikti = scorpaikti + pontoi
                        print(
                            "κερδίζεις 10 πόντους γιατί με την τρίτη κάρτα πέτυχες δύο όμοιες κάρτες")
                        print(" οι πόντοι σου είναι")
                        print(scorpaikti)
                        found = found+2
                        print("ανοίγουμε τις όμοιες κάρτες")
                        state52[thirdposition] = gameDeck3._deck[thirdposition]
                        if gameDeck3._deck[firstposition][0] == gameDeck3._deck[thirdposition][0]:
                            state52[firstposition] = gameDeck3._deck[firstposition]
                            state52[secondposition] = 'X '
                        else:
                            state52[secondposition] = gameDeck3._deck[secondposition]
                            state52[firstposition] = 'X '
                        ekt52()

                        if gameDeck3._deck[thirdposition][0] == 'K':
                            p = 1
                            print(
                                "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), χάνω την σειρά μου")
                    else:
                        state52[thirdposition] = 'X '
                        state52[firstposition] = 'X '
                        state52[secondposition] = 'X '

                                    else:
                state52[firstposition] = 'X '
                state52[secondposition] = 'X '

                                    if (gameDeck3._deck[firstposition][0] == 'J' and gameDeck3._deck[secondposition][0] == 'J'):
                                    print()
                p = 1
                                    print("Παίζεις ξανά γιατί άνοιξες ταυτόχρονα δύο βαλέδες")
                                    elif (gameDeck3._deck[firstposition][0] == 'K' and gameDeck3._deck[secondposition][0] == 'K'):

                                    print()
                                    print(
                    "άνοιξες ταυτόχρονα δύο Ρηγάδες(Κ), χάνω την σειρά μου")
                                    print()
                p = 1
                                    if found < 16:
              print("...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
              print()
                                    if p == 0:
                                    m= 0
                                    st1= 100
                                    st2= 100
                                    ekt52()
                                    for i in range(5):
                                    for x in range(5):
                    if mem[i] == mem[x] and mem[i] != '' and i != x:
                        if i < st1:
                                    st1= i
                        else:
                                    st2= i
                                    if st1 != st2:
                state52[lpos[st1]] = gameDeck3._deck[lpos[st2]]
                state52[lpos[st2]] = gameDeck3._deck[lpos[st2]]
                                    ekt52()
                                    print("άνοιξα τις ακόλουθες κάρτες:")
                                    print(gameDeck3._deck[lpos[st1]],
                                        '   ', gameDeck3._deck[lpos[st2]])
                found = found+2
                                    print(
                    "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                                    ekt52()
                                    if gameDeck3._deck[lpos[st1]][1] == '0':
                        pontoi = 10
                                    else:
                    c = Card(gameDeck3._deck[lpos[st1]][0], gameDeck3._deck[lpos[st1]][1])
                    pontoi = int(c.axia)
                                    print("οι πόντοι που κερδίζω είναι: ", pontoi)
                minescor = minescor + pontoi
                                    print("οι πόντοι μου συνολικά είναι: ")
                                    print(minescor)
                                    print()
                                    ekt52()
                                    print()
                                    if (gameDeck3._deck[lpos[st1]][0] == 'J' and gameDeck3._deck[lpos[st2]][0] == 'J'):
                    print()
                    m = 1
                    print("Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                                    elif (gameDeck3._deck[lpos[st1]][0] == 'K' and gameDeck3._deck[lpos[st2]][0] == 'K'):

                    print()
                    print(
                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                    print()
                    m= 1
                                    if found < 52:
                                    print(
                                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()
                                    mem.remove(mem[st2])
                                    mem.remove(mem[st1])
                                    lpos.remove(lpos[st2])
                                    lpos.remove(lpos[st1])
                                    mem.append('')
                                    mem.append('')
                                    else:
                grammi = random.choice(range(1, 5))
                stili = random.choice(range(1, 14))
                position = (grammi-1)*13 + (stili-1)
                                    while (grammi not in range(1, 5) or stili not in range(1, 14)) or state52[position] != 'X ':
                                    grammi= random.choice(range(1, 5))
                                    stili= random.choice(range(1, 5))
                                    position= (grammi-1)*13 + (stili-1)
                state52[position] = gameDeck3._deck[position]
                                    ekt52()
                y = gameDeck3._deck[position]
                st2 = 100
                                    for x in range(5):
                    if y == mem[x]:
                        st2 = x

                                    if st2 != 100:
                    state52[lpos[st2]] = gameDeck3._deck[lpos[st2]]
                    ekt52()
                    print("άνοιξα τις ακόλουθες κάρτες:")
                    print(gameDeck3._deck[position],
                                        '   ', gameDeck3._deck[lpos[st2]])
                    found = found+2
                    print(
                        "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)

                    ekt52()
                    if gameDeck3._deck[position][1] == '0':
                        pontoi = 10
                    else:
                        c = Card(gameDeck3._deck[position][0], gameDeck3._deck[position][1])
                        pontoi = int(c.axia)
                    print("οι πόντοι που κερδίζω είναι: ", pontoi)
                    minescor = minescor + pontoi
                    print("οι πόντοι μου συνολικά είναι: ")
                    print(minescor)
                    print()
                    ekt16()
                    print()
                    if (gameDeck3._deck[position[0] == 'J' and gameDeck3._deck[lpos[st2]][0] == 'J'):
                                        print()
                                        m = 1
                                        print(
                                            "Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                                        elif (gameDeck3._deck[position][0] == 'K' and gameDeck3._deck[lpos[st2]][0] == 'K'):

                                        print()
                                        print(
                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                                        print()
                                        m = 1
                                        if found < 52:
                                        print(
                        "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                        print()

                                        mem.remove(mem[st2])
                                        lpos.remove(lpos[st2])
                                        mem.append('')
                                        else:
                                        grammi2 = random.choice(range(1, 5))
                                        stili2 = random.choice(range(1, 15))
                                        position2 = (grammi2-1)*4 + (stili2-1)
                                        while (grammi2 not in range(1, 5) or stili2 not in range(1, 14)) or state52[position2] != 'X ' or position == position2:
                                        grammi2 = random.choice(range(1, 5))
                                        stili2 = random.choice(range(1, 13))
                                        position2 = (grammi2-1)*13 + (stili2-1)
                                        state52[position2] = gameDeck3._deck[position2]
                                        ekt52()
                                        print("άνοιξα τις ακόλουθες κάρτες:")
                                        print(gameDeck3._deck[position],
                                              '   ', gameDeck3._deck[position2])
                                        if gameDeck3._deck[position][0] == gameDeck3._deck[position2][0]:
                                        state52[position] = gameDeck3._deck[position]
                                        state52[position2] = gameDeck3._deck[position2]
                                        found = found+2
                                        print(
                        "βρήκα δύο όμοιες κάρτες, οι κάρτες που έχουμε βρει συνολικά είναι  ", found)
                                        ekt52()
                                        if gameDeck3._deck[position][1] == '0':
                            pontoi = 10
                                        else:
                            c = Card(gameDeck3._deck[position][0], gameDeck3._deck[position][1])
                            pontoi = int(c.axia)
                                        print(
                                            "οι πόντοι που κερδίζω είναι: ", pontoi)
                                        minescor = minescor + pontoi
                                        print("οι πόντοι μου συνολικά είναι: ")
                                        print(minescor)
                                        print()
                                        ekt16()
                                        print()
                                        elif ((gameDeck3._deck[position][0] == 'Q' and gameDeck3._deck[position2][0] == 'K') or (gameDeck3._deck[position][0] == 'K' and gameDeck3._deck[position2[0] == 'Q')):
                                              print(
                                            "άνοιξα μία ντάμα και ένα Ρήγα! Μπορώ να ανοίξω και μια τρίτη κάρτα")
                        st3 = 100
                        ekt52()
                        for i in range(5):
                            if (mem[i] == mem[st1] and i != st1) or (mem[i] == mem[st2] and i != st2):                                
                                st3 = i

                        if st3 != 100:
                            state52[lpos[st3]] = gameDeck3._deck[lpos[st3]]
                            ekt52()
                            print("άνοιξα την ακόλουθη τρίτη κάρτα:")
                            print(gameDeck3._deck[lpos[st3]])
                            if (gameDeck3._deck[lpos[st3]][0] == 'Q' or gameDeck3._deck[lpos[st3]][0] == 'K'):
                                pontoi = 10
                                minescor = minescore + pontoi
                                print(
                                    "κερδίζω 10 πόντους γιατί με την τρίτη κάρτα πέτυχα δύο όμοιες κάρτες")
                                print(" οι πόντοι μου είναι")
                                print(minescor)
                                found = found+2
                                print("ανοίγουμε τις όμοιες κάρτες")
                                state52[lpos[st3]] = gameDeck3._deck[lpos[st3]]
                                if gameDeck3._deck[lpos[st1]][0] == gameDeck3._deck[lpos[st3]][0]:
                                    state52[lpos[st1]] = gameDeck3._deck[lpos[st1]]
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck3._deck[lpos[st2]][0])
                                    state52[lpos[st2]] = 'X '
                                else:
                                    state52[lpos[st2]] = gameDeck3._deck[lpos[st2]]
                                    mem.pop()
                                    mem.insert(
                                        0, gameDeck3._deck[lpos[st1]][0])
                                    state52[lpos[st1]] = 'X '
                                ekt52()

                                if gameDeck3._deck[lpos[st3]] == 'K':
                                    m = 1
                                    print(
                                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις τη σειρά σου")
                            else:
                                mem.pop()
                                mem.pop()
                                mem.pop()
                                mem.insert(0, gameDeck3._deck[lpos[st3]][0])
                                mem.insert(1, gameDeck3._deck[lpos[st2]][0])
                                mem.insert(2, gameDeck3._deck[lpos[st1]][0])
                                lpos.insert(0, position3)
                                lpos.insert(1, position2)
                                lpos.insert(2, position)
                                state52[lpos[st3]] = 'X '
                                state52[lpos[st1]] = 'X '
                                state52[lpos[st2]] = 'X '
                        else:
                            grammi3 = random.choice(range(1, 5))
                            stili3 = random.choice(range(1, 5))
                            position3 = (grammi-1)*13 + (stili-1)
                            while (grammi not in range(1, 5) or stili not in range(1, 14)) or state52[position3] != 'X ':
                                grammi3 = random.choice(range(1, 5))
                                stili3 = random.choice(range(1, 14))
                                position3 = (grammi-1)*13 + (stili-1)
                            state52[position3] = gameDeck3._deck[position3]
                            ekt52()
                            if (gameDeck3._deck[position3][0] == 'Q' or gameDeck3._deck[position3][0] == 'K'):
                                pontoi = 10
                                minescor = minescore + pontoi
                                print(
                                    "κερδίζω 10 πόντους γιατί με την τρίτη κάρτα πέτυχα δύο όμοιες κάρτες")
                                print(" οι πόντοι μου είναι")
                                print(minescor)
                                found = found+2
                                print("ανοίγουμε τις όμοιες κάρτες")
                                state52[position3] = gameDeck3._deck[position3]
                                if gameDeck3._deck[position[0] == gameDeck3._deck[position3][0]:
                                                   state52[position]= gameDeck3._deck[position]
                                                   mem.pop()
                                                   mem.insert(
                                    0, gameDeck3._deck[position2][0])
                                    state52[position2] = 'X '
                                else:
                                    state52[position2] = gameDeck3._deck[position2]
                                    mem.pop()
                                    mem.insert(0, gameDeck3._deck[position][0])
                                    state52[position] = 'X '

                                ekt52()

                                if gameDeck3._deck[position3] == 'K':
                                    m = 1
                                    print(
                                        "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις τη σειρά σου")
                                            else:
                                mem.pop()
                                mem.pop()
                                mem.pop()
                                mem.insert(0, gameDeck3._deck[position3][0])
                                mem.insert(1, gameDeck3._deck[position2][0])
                                mem.insert(2, ameDeck3._deck[position][0])
                                lpos.insert(0, position3)
                                lpos.insert(1, position2)
                                lpos.insert(2, position)
                                state52[position3] = 'X '
                                state52[position] = 'X '
                                state52[position2] = 'X '


                                            else:
                                            mem.pop()
                                            mem.pop()
                                            mem.insert(
                                                0, gameDeck3._deck[position2][0])
                                            mem.insert(
                                                1, gameDeck3._deck[position][0])
                                            state52[position]= 'X '
                                            state52[position2]= 'X '

                                            if (gameDeck3._deck[position][0] == 'J' and gameDeck3._deck[position2][0] == 'J'):
                                            print()
                                            m= 1
                                            print(
                                                "Παίζω ξανά γιατί άνοιξα ταυτόχρονα δύο βαλέδες")
                                            elif (gameDeck3._deck[position[0] == 'K' and gameDeck3._deck[position2][0] == 'K'):

                                                   print()
                                    print(
                                                "άνοιξα ταυτόχρονα δύο Ρηγάδες(Κ), χάνεις την σειρά σου")
                                    print()
                                    m = 1
                                    if found < 52:
                                    print(
                                                "υπομονή...συνεχίζουμε μέχρι να ανοίξουμε όλα τα ζευγάρια όμοιων καρτών...")
                                    print()
                                    print()
                                    print("Μήπως τελειώσαμε το παιχνίδι;;;;.....για να μετρήσουμε τις ανοιχτές κάρτες...",
                                                found, " ανοιχτές κάρτες, ΜΠΡΑΒΟ σε όλους!!! ΟΛΟΚΛΗΡΩΣΑΤΕ ΤΟ ΠΑΙΧΝΙΔΙ ")
                                    print(
                                        "Οι παίκτες που έπαιξαν με τις αντιστοιχες βαθμολογίες τους είναι: ")
                                    for i in range(n):
                                    print(names[i], ":", scor[i])

                                    print()

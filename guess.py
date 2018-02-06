#!/usr/bin/python
# -*- coding: iso-8859-7 -*-

'''

παιχνίδι  : "μάντεψε ένα αριθμό" - ο παίκτης προσπαθεί να μαντέψει ένα αριθμό από το 1 έως και το 100 
            που τυχαία έχει επιλέξει ο υπολογιστής.

περιγραφή : 
- το πρόγραμμα περιμένει την είσοδο ενός αριθμού από το χρήστη και ελέγχει αν 
  αυτός είναι ίδιος με αυτόν που έχει επιλέξει ο υπολογιστής.
- εάν ο παίκτης δεν βρει τον αριθμό, το πρόγραμμα εμφανίζει το μήνυμα "Ο κρυμμένος αριθμός είναι μεγαλύτερος" ή 
  το μήνυμα "Ο κρυμμένος αριθμός είναι μικρότερος", ανάλογα με το αν ο αριθμός που έχει επιλέξει ο υπολογιστής 
  είναι μεγαλύτερος ή μικρότερος από αυτόν που έδωσε ο παίκτης.
- ο έλεγχος επαναλαμβάνεται μέχρι ο παίκτης να βρει τον αριθμό ή ο ίδιος να τερματίσει το παιχνίδι.
- ο παίκτης κερδίζει 10-ν πόντους, όπου ν οι αποτυχημένες προσπάθειες, και 0 πόντους αν οι αποτυχημένες προσπάθειες 
  είναι 10 ή περισσότερες. Π.χ. αν ο παίκτης βρει τον αριθμό μετά από 4 αποτυχημένες προσπάθειες τότε κερδίζει 
  10 - 4 = 6 πόντους, ενώ αν ο παίκτης έχει 10 ή περισσότερες αποτυχημένες προσπάθειες, τότε απλά δεν κερδίζει κανένα πόντο.
- όταν ο παίκτης βρει τον ζητούμενο αριθμό, το πρόγραμμα εμφανίζει το μήνυμα "Το βρήκατε μετά από Χ προσπάθειες, και κερδίσατε Υ πόντους" 
 (όπου Χ ο αριθμός των προσπαθειών και Υ οι πόντοι που κερδήθηκαν όπως παραπάνω). 
- αμέσως μετά το πρόγραμμα εμφανίζει το κατάλληλο μήνυμα συνέχειας ή όχι του παιχνιδιού. Αν ο παίκτης απαντήσει ΝΑΙ, 
  τότε το παιχνίδι αρχίζει από την αρχή. Αν απαντήσει ΟΧΙ το παιχνίδι τερματίζει.
  
σημειώσεις :
- το παιχνίδι αρχίζει με σαφείς οδηγίες ως προς τους δύο τρόπους τερματισμού του : 
  α) εύρεση του αριθμού από τον παίκτη και 
  β) εκούσιος τερματισμός από τον παίκτη.
- ο υπολογισμός του τυχαίου αριθμού γίνεται με χρήση της βιβλιοθήκης random.
- το παιχνίδι εμφανίζει τα κατάλληλα μηνύματα στον παίκτη, όπως περιγράφονται παραπάνω.
- αν ο χρήστης δώσει μη αριθμό ή αριθμό μικρότερο από το 1 ή μεγαλύτερο από το 100, το πρόγραμμα ζητά 
  και πάλι από τον παίκτη την εισαγωγή ενός αριθμού, χωρίς να σταματήσει και χωρίς αυτού του είδους το λάθος να προσμετράται 
  στις αποτυχημένες προσπάθειές του. Σε αυτό το σημείο χρησιμοποιείται αμυντικός προγραμματισμός. 
- όταν βρεθεί ο αριθμός, το παιχνίδι εμφανίζει το κατάλληλο μήνυμα στον παίκτη, όπως περιγράφεται παραπάνω.
- υπάρχει η δυνατότητα εκούσιου τερματισμού του παιχνιδιού από τον παίκτη πριν την λήξη του.
- στο τέλος του κάθε παιχνιδιού υπάρχει η επιλογή για να ξαναπαίξει ο παίκτης, με υπολογισμό από το πρόγραμμα νέου τυχαίου αριθμού.  

'''

# implements pseudo-random number generators for various distributions.
import random

# --------------------------------------------------------------------

__author__  = "Αριστοτέλης Μετσίνης"
__email__   = "aristotelis.metsinis@gmail.com"
__version__ = "1.0.0"
__date__    = "2017/12/05"
__license__ = "MIT"
__status__  = "Production"

# --------------------------------------------------------------------
# constant module variables; pre-defined messages per case containing "replacement fields" at the proper
# places if necessary.

HIGHER = "Ο κρυμμένος αριθμός είναι μεγαλύτερος"
LOWER  = "Ο κρυμμένος αριθμός είναι μικρότερος"
POINTS = "Κερδίσατε {} πόντους"
FOUND  = "Το βρήκατε μετά από {} προσπάθειες, και κερδίσατε {} πόντους"
PLAY   = "Θέλετε να ξαναπαίξετε (ΝΑΙ/ΟΧΙ) : "
PROMPT = "Μαντέψτε ένα αριθμό [1-100] ή πληκτρολογήστε 'ΟΧΙ' για έξοδο : "
BYE    = "Καλή σας μέρα ..."

# --------------------------------------------------------------------

def validate(number):
    '''

    validate input number.
    return True if number is an integer in [1,100], else False.

    '''

    # strip +/- character at the beginning of the string (if any), and
    # check whether all characters in the string are
    # digits and there is at least one character.
    # i.e. ensure that number is an integer such as "+/-12",
    # i.e. not alphanumerical e.g. "1a", or float e.g "1.0".    
    if not number.lstrip("+-").isdigit():
        return False
    # check if integer number is in [1,100] range.
    else:
        if 1 <= int(number) <= 100:
            return True
        else:
            return False

# --------------------------------------------------------------------

def guess(input, computer):
    '''

    print a hint.
    if user's input == computer's number return True,
    else return False.
    
    '''

    # compare user's input and computer's number.
    # print proper message in all cases.
    if input < computer:
        print(HIGHER)
        return False
    elif input > computer:
        print(LOWER)
        return False
    else:
        return True

# --------------------------------------------------------------------
# main script.

# computer generates a random number in [1,100] range.
computer = random.randint(1,100)
# print("\nComputer : {}".format(computer)) # DEBUG.

# Initialise variables.
total_points = 0
failures = 0
play = True

# play until user types "oxi" for exit; then "play" flag changes from true to false. 
while play:
    # ask user for a number; any leading and trailing characters are being removed.
	# all cased characters are being converted to upper-case.
    user_input = input("\n" + PROMPT).strip().upper()

    # user types an integer in [1,100].
    if validate(user_input):
        
        # user's number != computer; increment failures counter.
        if not guess(int(user_input), computer):
            failures += 1

        # user's number == computer; print proper messages.
        else:
			# calculate points of this game.
            points = 10-failures if failures <10 else 0
            print(FOUND.format(failures, points))

            # update total points.
            total_points += points

            # ask user to play again or exit the game.
			# any leading and trailing characters are being removed.
			# all cased characters are being converted to upper-case.
            while True:
                choise = input("\n" + PLAY).strip().upper()

                # play again; take care for either Greek or Latin input.
                if choise == "ΝΑΙ" or choise == "NAI":
                    # reset counter.
                    failures = 0
                    # regenerate computer's random number.
                    computer = random.randint(1,100)
                    # print("\nComputer : {}".format(computer)) # DEBUG.
					# exit loop immediately.
                    break

                # exit game; take care for either Greek or Latin input.
                elif choise == "ΟΧΙ" or choise == "OXI":
                    print("\n" + POINTS.format(total_points))
                    print(BYE + "\n")
					# reset flag to terminate game script.
                    play = False
					# exit loop immediately.
                    break

	# exit game; take care for either Greek or Latin input.
    elif user_input == "ΟΧΙ" or user_input == "OXI":
        print("\n" + POINTS.format(total_points))
        print(BYE + "\n")
		# reset flag to terminate game script.
        play = False 

# --------------------------------------------------------------------

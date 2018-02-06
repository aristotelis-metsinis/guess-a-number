#!/usr/bin/python
# -*- coding: iso-8859-7 -*-

'''

��������  : "������� ��� ������" - � ������� ��������� �� �������� ��� ������ ��� �� 1 ��� ��� �� 100 
            ��� ������ ���� �������� � �����������.

��������� : 
- �� ��������� ��������� ��� ������ ���� ������� ��� �� ������ ��� ������� �� 
  ����� ����� ����� �� ����� ��� ���� �������� � �����������.
- ��� � ������� ��� ���� ��� ������, �� ��������� ��������� �� ������ "� ��������� ������� ����� �����������" � 
  �� ������ "� ��������� ������� ����� ����������", ������� �� �� �� � ������� ��� ���� �������� � ����������� 
  ����� ����������� � ���������� ��� ����� ��� ����� � �������.
- � ������� ��������������� ����� � ������� �� ���� ��� ������ � � ����� �� ���������� �� ��������.
- � ������� �������� 10-� �������, ���� � �� ������������ �����������, ��� 0 ������� �� �� ������������ ����������� 
  ����� 10 � ������������. �.�. �� � ������� ���� ��� ������ ���� ��� 4 ������������ ����������� ���� �������� 
  10 - 4 = 6 �������, ��� �� � ������� ���� 10 � ������������ ������������ �����������, ���� ���� ��� �������� ������ �����.
- ���� � ������� ���� ��� ��������� ������, �� ��������� ��������� �� ������ "�� ������� ���� ��� � �����������, ��� ��������� � �������" 
 (���� � � ������� ��� ����������� ��� � �� ������ ��� ���������� ���� ��������). 
- ������ ���� �� ��������� ��������� �� ��������� ������ ��������� � ��� ��� ����������. �� � ������� ��������� ���, 
  ���� �� �������� ������� ��� ��� ����. �� ��������� ��� �� �������� ����������.
  
���������� :
- �� �������� ������� �� ������ ������� �� ���� ���� ��� ������� ����������� ��� : 
  �) ������ ��� ������� ��� ��� ������ ��� 
  �) �������� ����������� ��� ��� ������.
- � ����������� ��� ������� ������� ������� �� ����� ��� ����������� random.
- �� �������� ��������� �� ��������� �������� ���� ������, ���� ������������� ��������.
- �� � ������� ����� �� ������ � ������ ��������� ��� �� 1 � ���������� ��� �� 100, �� ��������� ���� 
  ��� ���� ��� ��� ������ ��� �������� ���� �������, ����� �� ���������� ��� ����� ����� ��� ������ �� ����� �� ������������ 
  ���� ������������ ����������� ���. �� ���� �� ������ ��������������� ��������� ���������������. 
- ���� ������ � �������, �� �������� ��������� �� ��������� ������ ���� ������, ���� ������������ ��������.
- ������� � ���������� �������� ����������� ��� ���������� ��� ��� ������ ���� ��� ���� ���.
- ��� ����� ��� ���� ���������� ������� � ������� ��� �� ���������� � �������, �� ���������� ��� �� ��������� ���� ������� �������.  

'''

# implements pseudo-random number generators for various distributions.
import random

# --------------------------------------------------------------------

__author__  = "����������� ��������"
__email__   = "aristotelis.metsinis@gmail.com"
__version__ = "1.0.0"
__date__    = "2017/12/05"
__license__ = "MIT"
__status__  = "Production"

# --------------------------------------------------------------------
# constant module variables; pre-defined messages per case containing "replacement fields" at the proper
# places if necessary.

HIGHER = "� ��������� ������� ����� �����������"
LOWER  = "� ��������� ������� ����� ����������"
POINTS = "��������� {} �������"
FOUND  = "�� ������� ���� ��� {} �����������, ��� ��������� {} �������"
PLAY   = "������ �� ����������� (���/���) : "
PROMPT = "�������� ��� ������ [1-100] � �������������� '���' ��� ����� : "
BYE    = "���� ��� ���� ..."

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
                if choise == "���" or choise == "NAI":
                    # reset counter.
                    failures = 0
                    # regenerate computer's random number.
                    computer = random.randint(1,100)
                    # print("\nComputer : {}".format(computer)) # DEBUG.
					# exit loop immediately.
                    break

                # exit game; take care for either Greek or Latin input.
                elif choise == "���" or choise == "OXI":
                    print("\n" + POINTS.format(total_points))
                    print(BYE + "\n")
					# reset flag to terminate game script.
                    play = False
					# exit loop immediately.
                    break

	# exit game; take care for either Greek or Latin input.
    elif user_input == "���" or user_input == "OXI":
        print("\n" + POINTS.format(total_points))
        print(BYE + "\n")
		# reset flag to terminate game script.
        play = False 

# --------------------------------------------------------------------

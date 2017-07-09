from random import randint #imports random function


#prints welcome message
print """
welcome to my slot Machine game.

Rules are pretty simple.You will be given
initial 400 credits.For each trial,25 credits 
will be taken from your account.If your all 
numbers are same,you will get jackpot of 100
credits.if your any two numbers are same,then you will 
get credit of 40.If no numbers are same,you will

get a big ZERO.
"""
#start game by calling 'play_game' function and assign initial 400 credits
def start():
	print "Type start to play game."
	initialINP=raw_input()
	if initialINP=="start" or initialINP == "START" or initialINP == "Start" or initialINP=="s":
		play_game(400)
	else:
	    print "I told you to type start.Please give correct input"
	    start()	
#quits the code
def Fuck():
	quit()




#ask wether play agian or not
def choice(k):
	print "\nWant to play again?Yes or No"
	YoN=raw_input()
	if YoN == "yes" or YoN=="YES" or YoN=="y" or YoN=="Y" or YoN=="Yes":
		play_game(k)
	else:
		Fuck()


#runs when all three numbers are same
def jackpot(old_tokens):
    new_tokens=old_tokens+100 #add 100 credits to blance as jackot
    print """
    congratulations,You have won JACKPOT.
    You have been credited by 100.
    so your curret balance is %d.

    """%new_tokens
    
    choice(new_tokens) #sends to function which ask play again or not


#runs when two are numbers same
def midMan(old_tokens):
	new_tokens=old_tokens+40
	print """
	Opps.You are unabale to win jackpot.
	But you are able to win some prize.
	of 40 credits.
	Your current balance is %d.
	"""%new_tokens
	choice(new_tokens) #sends to function which ask play again or not


#runs when no number are same,Bad Luck
def lose(old_tokens):
	print """
	Sorry.You Lose.
	Luck was not with you this time.
	Everything gonna be Okay.
	your current balance is %d.
	"""%old_tokens
	choice(old_tokens) #sends to function which ask play again or not

#brain of game
def play_game(tokens):
#checks wether sufficent tokens or not	
 if tokens-25<0:          #when NOT sufficent
 	print "You dont have sufficent Balance"
 else:                    #when sufficient
	print "##### -25 #####"
	tokens-=25         #deducts 25 for playing
	#x,y,z vars are assigned random number and then displays them
	x=randint(0,9)     
	y=randint(0,9)
	z=randint(0,9)
	print "Press Enter to Slot first number"
	trial1=raw_input() #just added for user to press enter and then display x.Same for trial2 and 3.
	print "%d----------Again press enter."%x
	trial2=raw_input()
	print "%d----------Last one time"%y
	trial3=raw_input()
	print "%d----------" % z
	#checks for jackpot,prize,or loose
	if x==y==z:   #jackpot
		jackpot(tokens)
	elif x!=y and y!=z and x!=z: #loose
		lose(tokens)
	else:
		midMan(tokens)  #prize



start() #starts the game by calling start function

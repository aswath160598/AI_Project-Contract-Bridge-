import random
import time


start_time = time.time()
list_cards = [('spade','1'),('spade','2'),('spade','3'),('spade','4'),('spade','5'),('spade','6'),('spade','7'),('spade','8'),('spade','9'),('spade','10'),('spade','11'),('spade','12'),('spade','13'),('diamond','1'),('diamond','2'),('diamond','3'),('diamond','4'),('diamond','5'),('diamond','6'),('diamond','7'),('diamond','8'),('diamond','9'),('diamond','10'),('diamond','11'),('diamond','12'),('diamond','13'),('heart','1'),('heart','2'),('heart','3'),('heart','4'),('heart','5'),('heart','6'),('heart','7'),('heart','8'),('heart','9'),('heart','10'),('heart','11'),('heart','12'),('heart','13'),('flower','1'),('flower','2'),('flower','3'),('flower','4'),('flower','5'),('flower','6'),('flower','7'),('flower','8'),('flower','9'),('flower','10'),('flower','11'),('flower','12'),('flower','13')]

random.shuffle(list_cards)

#print(list_cards)
spade7 = list_cards.index(('spade','7'))

#print(spade7)
c = [[] for i in range(4)]

c[0] = list_cards[0:13]
c[1] = list_cards[13:26]
c[2] = list_cards[26:39]
c[3] = list_cards[39:52]

#print(c[1],"\n",c[2],"\n",c[3],"\n",user4)
#print(c[3],"\n")
lsp7 = 0
if(spade7>=0 and spade7<=12):
	lsp7 = 0
elif(spade7>=13 and spade7<=25):
	lsp7 = 1
elif(spade7>=26 and spade7<=38):
	lsp7 = 2
else:
	lsp7 = 3


print("Player who put spade 7 : ",lsp7)
num = -1 
spade = []
flower = []
diamond = []
heart = []
if(lsp7 == 3):
	while(num!='7'):
		num = input("Drop a Card : \n")
		if(num!='7'):
			print("Invalid Card")
	print('You droppped Spade-7. \n')
	ind = c[3].index(('spade','7'))
	val = c[3].pop(ind)
	spade.append(val)

else:
	if(lsp7 == 0):
		ind = c[0].index(('spade','7'))
		val = c[0].pop(ind)
		spade.append(val)
	elif(lsp7 == 1):
		ind = c[1].index(('spade','7'))
		val = c[1].pop(ind)
		spade.append(val)
	elif(lsp7 == 2):
		ind = c[2].index(('spade','7'))
		val = c[2].pop(ind)
		spade.append(val)


print("Spade : ",spade,"\n")
print("Flower : ",flower,"\n")
print("Heart : ",heart,"\n")
print("Diamond : ",diamond,"\n")

#print(spade[0][1])

#print("c"+ str(turn))
turn = (lsp7 + 1)%4

avail_list = [('spade','6'),('spade','8'),('flower','7'),('heart','7'),('diamond','7')]
#useable = []
turn = (lsp7)%4

def play(turn,avail_list):
	useable = []
	
	for i in c[turn]:
			if i in avail_list:
				useable.append(i)
	#random.shuffle(useable)
	card = minimax(turn,avail_list,useable)
	if not isinstance(card,type(None)):
		try:
			#print(useable[0],"\n")
			if(card[0] == 'spade'):
				if(int(card[1])>7):
					spade.append(card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
				else:
					spade.insert(0,card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
			elif(card[0] == 'flower'):
				if(int(card[1])>7):
					flower.append(card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
				else:
					flower.insert(0,card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
			elif(card[0] == 'heart'):
				if(int(card[1])>7):
					heart.append(card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
				else:
					heart.insert(0,card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
			elif(card[0] == 'diamond'):
				if(int(card[1])>7):
					diamond.append(card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
				else:
					diamond.insert(0,card)
					indx = c[turn].index(card)
					c[turn].pop(indx)
					avail_list.remove(card)
					addcard(card)
		except IndexError :
			print("You do not have any valid cards. \n")
	else:
		print("You do not have any valid cards. \n")

	#print(useable

	print("--------------------------------------------------------------------------------------- \n")
	print("PLAYERS CURRENT CARDS : \n")

	print(" Player 1 : ",c[0],"\n\n\n","Player 2 : ",c[1],"\n\n\n","Player 3 : ",c[2],"\n\n\n","Player 4(user) : ",c[3])
     
	print("\n************************************************************************************* \n")

	print("CARDS ALREADY PUT: \n")

	print("Spade : ",spade,"\n")
	print("Flower : ",flower,"\n")
	print("Heart : ",heart,"\n")
	print("Diamond : ",diamond,"\n")

	print("--------------------------------------------------------------------------------------- \n")
		
	#print("Current Valid Cards : ",avail_list)

def addcard(card):
	if(card[0] == 'spade'):
		if(int(card[1])<7 and (int(card[1])-1)>0):
			avail_list.insert(0,('spade',str(int(card[1])-1)))
		elif(int(card[1])>7 and (int(card[1])+1)<14):
			avail_list.append(('spade',str(int(card[1])+1)))
	elif(card[0] == 'flower'):
		if(int(card[1])<7 and (int(card[1])-1)>0):
			avail_list.insert(0,('flower',str(int(card[1])-1)))
		elif(int(card[1])>7 and (int(card[1])+1)<14):
			avail_list.append(('flower',str(int(card[1])+1)))
		else:
			avail_list.insert(0,('flower',str(int(card[1])-1)))
			avail_list.append(('flower',str(int(card[1])+1)))


	elif(card[0] == 'heart'):
		if(int(card[1])<7 and (int(card[1])-1)>0):
			avail_list.insert(0,('heart',str(int(card[1])-1)))
		elif(int(card[1])>7 and (int(card[1])+1)<14):
			avail_list.append(('heart',str(int(card[1])+1)))
		else:
			avail_list.insert(0,('heart',str(int(card[1])-1)))
			avail_list.append(('heart',str(int(card[1])+1)))
	elif(card[0] == 'diamond'):
		if(int(card[1])<7 and (int(card[1])-1)>0):
			avail_list.insert(0,('diamond',str(int(card[1])-1)))
		elif(int(card[1])>7 and (int(card[1])+1)<14):
			avail_list.append(('diamond',str(int(card[1])+1)))
		else:
			avail_list.insert(0,('diamond',str(int(card[1])-1)))
			avail_list.append(('diamond',str(int(card[1])+1)))

def minimax(turn,avail_list,useable):

	high = 13
	lower = 1
	p = 0
	t = 0
	chtype = ''
	cltype = ''
	while(high>=7):
		for i in c[turn]:
			if(i[1]==high):
				chtype = i[0]
				numh = i[1]
				p = 1
				break
		if(p==1):
			break
		else:
			high -= 1


	while(lower<=7):
		for i in c[turn]:
			if(i[1]==lower):
				cltype = i[0]
				numl = i[1]
				t = 1
				break
		if(t==1):
			break
		else:
			lower += 1

	low_dif = 0
	high_dif = 0

	if(chtype == 'spade'):
		l = len(spade)
		high_dif = high-spade[l-1]
	elif(chtype == 'flower'):
		l = len(flower)
		high_dif = high-flower[l-1]	
	elif(chtype == 'heart'):
		l = len(heart)
		high_dif = high-heart[l-1]
	elif(chtype == 'diamond'):
		l = len(diamond)
		high_dif = high-diamond[l-1]

	if(cltype == 'spade'):
		l = len(spade)
		low_dif = spade[l-1] - lower
	elif(cltype == 'flower'):
		l = len(flower)
		low_dif = flower[l-1] - lower
	elif(cltype == 'heart'):
		l = len(heart)
		low_dif = heart[l-1] - lower
	elif(cltype == 'diamond'):
		l = len(diamond)
		low_dif = diamond[l-1] - lower

	if(high_dif > low_dif):
		if(chtype == 'spade'):
			for card in useable:
				if(card[0]=='spade' and card[1]>=7):
					return card
		elif(chtype == 'flower'):
			for card in useable:
				if(card[0]=='flower' and card[1]>=7):
					return card
		elif(chtype == 'heart'):
			for card in useable:
				if(card[0]=='heart' and card[1]>=7):
					return card
		elif(chtype == 'diamond'):
			for card in useable:
				if(card[0]=='diamond' and card[1]>=7):
					return card
	else:
		if(cltype == 'spade'):
			for card in useable:
				if(card[0]=='spade' and card[1]<7):
					return card
		elif(cltype == 'flower'):
			for card in useable:
				if(card[0]=='flower' and card[1]<7):
					return card
		elif(cltype == 'heart'):
			for card in useable:
				if(card[0]=='heart' and card[1]<7):
					return card
		elif(cltype == 'diamond'):
			for card in useable:
				if(card[0]=='diamond' and card[1]<7):
					return card

	random.shuffle(useable)
	if(len(useable)> 0):
		return useable[0]



k = 1
while(len(avail_list)!=0):
	turn = (turn + 1)%4
	if(turn==3):
		k+=1
		print("Round : " + str(k))
		
	play(turn,avail_list)
	if(len(c[0]) == 0):
		print("Player 1 is the Winner!!")
		playwin=1
		break
	elif(len(c[1]) == 0):
		print("Player 2 is the Winner!!")
		playwin=2
		break
	elif(len(c[2]) == 0):
		print("Player 3 is the Winner!!")
		playwin=3
		break
	elif(len(c[3]) == 0):
		print("Player 4(user) is the Winner!!")
		playwin=4
		break
	#time.sleep(4)

print(" %s seconds " % (time.time() - start_time))
def printtext():
    global e
    x=list()
    string = e.get() 
    x=string.split()
    t=tuple(x)
    print(t)
    if(playwin==1):
    	label = Label(root, text= "Player 1 IS THE WINNER",fg = "red",bg = "blue",font = "Helvetica 26 bold italic")
    if(playwin==2):
    	label = Label(root, text= "Player 2 IS THE WINNER",fg = "red",bg = "blue",font = "Helvetica 26 bold italic")
    if(playwin==3):
    	label = Label(root, text= "Player 3 IS THE WINNER",fg = "red",bg = "blue",font = "Helvetica 26 bold italic")
    if(playwin==4):
    	label = Label(root, text= "Congradulations, You are the WINNER",fg = "light green",bg = "blue",font = "Helvetica 26 bold italic")
    label.pack() 
from tkinter import *  
from PIL import ImageTk,Image  
root = Tk()  
root.title('Contract Bridge')
e=Entry(root)
e.pack()
e.focus_set()
b = Button(root,text='Next',command=printtext)
b.pack(side='bottom')
canvas = Canvas(root, width = 300, height = 500)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("spade_7.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 
root.mainloop() 


####################################################
CounterMarker =("Counter", "578b38fc-2e96-4375-8763-d33bda7b5d19")
	
def untapAll(group, x = 0, y = 0):
	mute()
	notify("{} untaps all his cards".format(me))
	for card in group: 
		if card.controller == me:
			card.orientation &= ~Rot90			
			
def clearAll(group, x = 0, y = 0):
    notify("{} clears all targets and combat.".format(me))
    for card in group:
		if card.controller == me:
			card.target(False)
			card.highlight = None

def roll20(group, x = 0, y = 0):
    mute()
    n = rnd(1, 20)
    notify("{} rolls {} on a 20-sided die.".format(me, n))

def flipCoin(group, x = 0, y = 0):
    mute()
    n = rnd(1, 2)
    if n == 1:
        notify("{} flips heads.".format(me))
    else:
        notify("{} flips tails.".format(me))

def tap(card, x = 0, y = 0):
    mute()
    card.orientation ^= Rot90
    if card.orientation & Rot90 == Rot90:
		notify('{} taps {}'.format(me, card))
    else:
        notify('{} untaps {}'.format(me, card))
		  
def flip(card, x = 0, y = 0):
    mute()
    if card.isFaceUp:
        notify("{} turns {} face down.".format(me, card))
        card.isFaceUp = False
    else:
        card.isFaceUp = True
        notify("{} turns {} face up.".format(me, card))

def discard(card, x = 0, y = 0):
	card.moveTo(me.piles['Discard Pile'])
	notify("{} discards {}".format(me, card))

def addCounter(card, x = 0, y = 0):
	mute()
	notify("{} adds 1 counter to {}.".format(me, card))
	card.markers[CounterMarker] += 1

def removeCounter(card, x = 0 , y = 0):
	mute()
	notify("{} removes 1 counter to {}.".format(me, card))
	card.markers[CounterMarker] -= 1
	  
def setCounter(card, x = 0, y = 0):
	mute()
	quantity = askInteger("How many counters", 0)
	notify("{} sets {} counters on {}.".format(me, quantity, card))
	card.markers[CounterMarker] = quantity	
		
def play(card, x = 0, y = 0):
	mute()
	src = card.group
	card.moveToTable(0, 0)
	notify("{} plays {} from their {}.".format(me, card, src.name))

def mulligan(group):
    mute()
    newCount = len(group) - 1
    if newCount < 0: return
    if not confirm("Mulligan down to %i ?" % newCount): return
    notify("{} mulligans down to {}".format(me, newCount))
    librarycount = len(me.piles["Life Deck"])
    for card in group:
        n = rnd(0, librarycount)
        card.moveTo(me.piles["Life Deck"], n)
    me.piles["Life Deck"].shuffle()
    for card in me.piles["Life Deck"].top(newCount):
        card.moveTo(me.hand)

def randomDiscard(group):
	mute()
	card = group.random()
	if card == None: return
	notify("{} randomly discards {}.".format(me,card.name))
	card.moveTo(me.piles['Discard Pile'])

def draw(group, x = 0, y = 0):
	if len(group) == 0: return
	mute()
	group[0].moveTo(me.hand)
	notify("{} draws a card.".format(me))

def drawMany(group, count = None):
	if len(group) == 0: return
	mute()
	if count == None: count = askInteger("Draw how many cards?", 0)
	for card in group.top(count): card.moveTo(me.hand)
	notify("{} draws {} cards.".format(me, count))

def drawBottom(group, x = 0, y = 0):
	if len(group) == 0: return
	mute()
	group.bottom().moveTo(me.hand)
	notify("{} draws a card from the bottom.".format(me))

def shuffle(group):
	group.shuffle()
  



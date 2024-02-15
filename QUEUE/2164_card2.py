def Mixing_cards(cards):
    if len(cards) == 1:
        return cards[0]
    else:
        cards.pop()
        cards.insert(0,cards[-1])
        cards.pop()
        return Mixing_cards(cards)

from collections import deque

T = int(input())
cards = deque(i for i in range(T,0,-1))
#print(Mixing_cards(cards))

while len(cards) > 1:
    cards.pop()
    cards.insert(0, cards[-1])
    cards.pop()
print(*cards)
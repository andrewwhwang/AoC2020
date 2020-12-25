from collections import deque
import numpy as np

def play(deck1, deck2):
    while deck1 and deck2:
        c1, c2 = deck1.popleft(), deck2.popleft()
        if c1 > c2:
            deck1.extend([c1,c2])
        else:
            deck2.extend([c2,c1])

    if deck1:
        return deck1
    else:
        return deck2

if __name__ == "__main__":
    with open('inputs/22.txt', 'r') as file:
        players = file.read().split("\n\n")
    
    deck1 = deque([int(card) for card in players[0].split('\n')[1:]])
    deck2 = deque([int(card) for card in players[1].split('\n')[1:]])

    final = play(deck1, deck2)

    print(np.sum(np.array(final)* np.arange(len(final), 0, -1)))
import random

CELLS = [(0,0),(0,1),(0,2),
         (1,0),(1,1),(1,2),
         (2,0),(2,1),(2,2)]

print("Welcome to the dungeon!")

def get_locations():
    # if monster, door, or start are the same, do it again
    # return monster, door, start

    monster = random.choice(CELLS)
    door = random.choice(CELLS)
    start = random.choice(CELLS)

    if monster == door or monster == start or door == start:
        return get_locations()
        
    return monster, door, start

def move_player(player, move):
    #player = (x, y)
    x, y = player
    if move == 'LEFT':
        y -= 1
    elif move == 'RIGHT':
        y += 1
    elif move == 'UP':
        x -= 1
    elif move == 'DOWN':
        x += 1
        
    return x, y

def get_moves(players):
    moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
    # players = (x, y)
    
    if players[1] == 0:
        moves.remove('LEFT')
    if players[1] == 2:
        moves.remove('RIGHT')
    if players[0] == 0:
        moves.remove('UP')
    if players[0] == 2:
        moves.remove('DOWN')
    # if players y is 0, remove LEFT
    # if players x is 0, remove UP
    # if players y is 2, remove RIGHT
    # if players x is 2, remove DOWN
    return moves

def draw_map(player):
    print(' _ _ _ ')
    tile = '|{}'
    
    for idx, cell in enumerate(CELLS):
        if idx in [0, 1, 3, 4, 6, 7]:
            if cell == player:
                print(tile.format('X'), end='')
            else:
                print(tile.format('_'), end='')
        else:
            if cell == player:
                print(tile.format('X|'))
            else:
                print(tile.format('_|'))

monster, door, player = get_locations()

while True:
    moves = get_moves(player)
    
    print("You're currently in room {}".format(player)) # fill in with player position

    draw_map(player)

    print("You can move {}".format(moves)) # fill in with avaible moves
    print("Enter QUIT to quit")

    move = input("> ")
    move = move.upper()

    if move == 'QUIT':
        break
    
    if move in moves:
        player = move_player(player, move)
    else:
        print("** Walls are hard, stop walking into them! **")
        continue

    if player == door:
        print("You escaped!")
        break
    elif player == monster:
        print("You were eaten by the monster!")
        break
        # if it's a good move, change the player's position
        # if it's a bad move, don't change anything
        # if the new player position is the door, they win!
        # if the new player postion is the monster, they lose!
        # otherwise, continue
        

import util
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# helper functions
def unvisited_directions_from_this_room(room_id):
    return [k for (k,v) in tg[room_id].items() if v == '?']

def select_random_unvisited_door(room_id):
    return random.choice(unvisited_directions_from_this_room(room_id))

direction_opposites = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


start_room_exits = player.current_room.get_exits()
start_room = player.current_room.id
tg = {start_room :{dir: '?' for dir in start_room_exits}}

traversal_path = []

def update_tg(new_room, from_room, to_dir):
    tg[from_room][to_dir] = new_room
    if new_room not in tg:
        new_dict = {dir: '?' for dir in player.current_room.get_exits()}
    else:
        new_dict= tg[new_room]
    new_dict[direction_opposites[to_dir]] = from_room
    tg[new_room] = new_dict

while len(unvisited_directions_from_this_room(player.current_room.id)) > 0:
    from_room = player.current_room.id
    to_dir = select_random_unvisited_door(player.current_room.id)
    player.travel(to_dir)
    traversal_path.append(to_dir)
    update_tg(player.current_room.id, from_room, to_dir)

print ('here')

input()

# traversal_path = ['n', 'n']







# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     current_room = player.current_room.id
#     exits = player.current_room.get_exits()
#     # print(f'current_room: {current_room}')
#     # print(f'traversal path: {traversal_path}')
#     # print(f'exits: {exits}')


#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:

#         # my_move(cmds[0])
#         player.travel(cmds[0], True)

#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()







from util import Queue 
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval





############################################################## 



# helpers 
def opposite_dir(direction):
    return {'n': 's', 's': 'n', 'e': 'w','w': 'e'}[direction]






def update_tg(new_room, from_room, to_dir):
    tg[from_room][to_dir] = new_room
    if new_room not in tg:
        new_dict = {dir: '?' for dir in player.current_room.get_exits()}
    else:
        new_dict = tg[new_room]
    new_dict[opposite_dir[to_dir]] = from_room
    tg[new_room] = new_dict
    return tg




def explore():
    while len(unvisited_directions_from_this_room(player.current_room.id)) > 0:
        from_room = player.current_room.id
        to_dir = select_random_unvisited_door(player.current_room.id)
        player.travel(to_dir)
        traversal_path.append(to_dir)
        update_tg(player.current_room.id, from_room, to_dir)
        print(tg)
#         print(player.current_room.id)
    

def move_loop(direction):
#     exits = player.current_room.get_exits()
    start_pos = player.current_room.id
    player.travel(direction)
    end_pos = player.current_room.id
    return (start_pos, direction, end_pos)






############################################################## 

    





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

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []




# TRAVERSAL TEST
# visited_rooms = set()
# player.current_room = world.starting_room
# visited_rooms.add(player.current_room)

# for move in traversal_path:
#     player.travel(move)
#     visited_rooms.add(player.current_room)

# if len(visited_rooms) == len(room_graph):
#     print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
# else:
#     print("TESTS FAILED: INCOMPLETE TRAVERSAL")
#     print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
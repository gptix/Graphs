from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

from util import Queue

def opposite_dir(direction):
    return {'n': 's', 's': 'n', 'e': 'w','w': 'e'}[direction]

def unvisited_doors_here(room_id):
    return [k for (k,v) in tg[room_id].items() if v == '?']

def select_random_unvisited_door(room_id):
    return random.choice(unvisited_doors_here(room_id))

def move_and_update_traverse_list(direction):
    """These are combined into one function to avoid de-synchronization."""
    global traversal_path
    
    player.travel(direction)
    traversal_path.append(direction)
    print(traversal_path)

def explore():
    # Stop trying to explore when there are no unexplored doors in 
    # the current room.
    while len(unvisited_doors_here(player.current_room.id)) > 0:
        # if there are any moves, explore
        explore_one_move()

def explore_one_move():
    # Store this so we can update tg
    from_room = player.current_room.id
    # Select an unexplored door and store so we can update tg
    to_dir = select_random_unvisited_door(player.current_room.id)
    # use the Player object to travel
    move_and_update_traverse_list(to_dir)
    # Update tg.
    update_tg(player.current_room.id, from_room, to_dir)
    # print(tg)
#         print(player.current_room.id)

def update_tg(new_room, from_room, to_dir):
    # Add the id of the new room to the record for the room
    # we came from.
    tg[from_room][to_dir] = new_room
    # If there is no record for the room we arrived in, we need to add one.
    if new_room not in tg:
        # Find out what doors exist.
        dirs_to_add = player.current_room.get_exits()
        # We can temporarily leave all directions (that we can go) as '?'.
        tg[new_room] = {d: '?' for d in dirs_to_add}
    # Now we definitely have a record, and can overwrite a '?'
    # or overwrite existing info.  No point in checking if it exists.
    tg[new_room][opposite_dir(to_dir)] = from_room
    # return tg
    
def setup_bfs():
    global q
    global path_to_nearest
    global visited
    global base_room
    
    q = Queue()
    
    # Build paths. One will be successful. These will be stored on the queue.
    base_room = player.current_room.id
    # A variable used inside the loop to hold the current path being examined 
    # in combination with neighbors.
    path_to_nearest = []
    q.enqueue(path_to_nearest)
    # A variable used to hold ids of rooms that have been examined
    # to avoid duplicate examination.
    visited = set()
    # print(f'q - {q}')
    # print(f'path_to_nearest - {path_to_nearest}')
    # print(f'enqueued path_to_nearest')
    
def dq_and_use_path():
    # pull a path from the queue
    current_path = q.dequeue()
    # go to the end of the dequeued path
    current_room = base_room
    for move in current_path:
        current_room = tg[current_room][move]
        
# def enqueue_neighbors():
#     global current_room
#     visited.add(current_room)
#     # this will be a dict of direction:room_id pairs
#     visit_from_here = (tg[current_room])
#     # this is looking at the VALUE for the tg entry.
#     # That is a dict of DIRECTION, ROOM_BEYOND pairs
#     for direction, room_id in visit_from_here.items():
#         q.enqueue(current_path.append(direction))
#         # after addin neighbors to the queue, loop again

# def test_for_success(curr_room):
#     unvisited_from_here = unvisited_directions_from_this_room(curr_room)
#     return current_room not in visited and len(unvisited_from_here) > 0

def handle_success():
    # print(f'success: path:   {path_to_nearest}')
    ## append the current value of the 'path_to_nearest' to 'traversal_path'
    ## use the Player object to make the moves in the 'path_to_nearest'
    for move in path_to_nearest:
        move_and_update_traverse_list(to_dir)
    return True

def bfs_nearest_Qmark_door():
    global traversal_path
    """Use breadth-first search to find nearest unexplored door.
    The graph is tg:
    {ROOM_ID: 
        {one or more of DIRECTION: KNOWN_ROOM_ID or '?'}
        }
    e.g., 
    {
        0: {'n': '1', 's': '?', 'w': '?', 'e': '?'}
    }"""
    
    setup_bfs()
    
    # Loop indefinitely until a success condition is met.
    while True:
    # Dequeue to check for success
        current_path = q.dequeue()
        
        # go to the end of the dequeued path
        current_room = base_room
        # print(f'current_path = {current_path}')
        for move in current_path:
            current_room = tg[current_room][move]
            # print(f'current room = {current_room}')
        # print('Now at the end of the path')
        
        # print(f'Visited: {visited}')
        # print(f'Current room: {current_room}')
        # input(f'current room info: {tg[current_room]}')
        # if the room we are examining has a door marked '?'
        found_a_Q_door = len(unvisited_doors_here(current_room)) > 0
        
        if(found_a_Q_door):
            # print('Success')
            # print(f'Before: {traversal_path}')
            # input('Inside success loop')
            for direction in current_path:  

                player.travel(direction)
                traversal_path.append(direction)
            
            # print(f'After: {traversal_path}')
            return

        # continue if success condition not yet met
        visited.add(current_room)
        
        # enqueue paths that have not been visited yet
        ## select doors from this room that do not lead to rooms we have 
        ## visited before
        to_append = [dr for (dr, rm) in tg[current_room].items() if rm not in visited]

        ## build paths
        paths_to_enqueue = [current_path + [direction] for direction in to_append]
        
        # enqueue them 
        for path in paths_to_enqueue:
            q.enqueue(path)

        # after addin neighbors to the queue, loop again

#         # handle_success()
#         input('Success')
#         print(f'success: path:   {path_to_nearest}')
#         ## append the current value of the 'path_to_nearest' to 'traversal_path'
#         ## use the Player object to make the moves in the 'path_to_nearest'
#         for move in path_to_nearest:
#             move_and_update_traverse_list(to_dir)
#         print(f'traversal path - {traversal_path}')
#         print(f'present room id - {player.current_room.id}')
#         input('At end of success path')
#         return True

############### Setup game ############################################### 

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

this_room = player.current_room.id

doors = player.current_room.get_exits()

# Start an association list to hold nodes and edges
# We don't know what is behind any of them
tg = {this_room: {d: '?' for d in doors}}



#####################################################################

target_room_count = len(room_graph)
while len(tg) < target_room_count:
    bfs_nearest_Qmark_door()
    explore()

#####################################################################


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

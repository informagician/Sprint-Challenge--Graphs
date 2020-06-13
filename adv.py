from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


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
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# backtrack ref
switch = {'n':'s','s':'n','e':'w','w':'e'}

backtrack = []

visited = {}

unexplored = {}

while len(visited) < len(room_graph):

    room = player.current_room.id

    if len(visited) == 0 or room not in visited:
        visited[room] = player.current_room.get_exits()
        unexplored[room] = player.current_room.get_exits()

    while len(unexplored[player.current_room.id]) < 1:
        back = backtrack.pop()
        traversal_path.append(back)
        player.travel(back)

    move = unexplored[player.current_room.id].pop()
    traversal_path.append(move)
    backtrack.append(switch[move])
    player.travel(move)    






# g = {}
# for room in room_graph:
#     g[room] = {k:v for k,v in room_graph[room][1].items()}

# print(g)

# stack = []
# back = []
# stack.append([player.current_room.id])
# visited = set()

# switch = {'n':'s','s':'n','e':'w','w':'e'}

# while len(stack) > 0:
#     path = stack.pop()
#     room = path[-1]

#     if room not in visited:
#         visited.add(room)

#         for exit in g[room].keys():

#             if g[room][exit] not in visited:
#                 new_path = list(path)
#                 traversal_path.append(exit)
#                 back.append(switch[exit])
#                 new_path.append(g[room][exit])
#                 stack.append(new_path)
# # print(visited)
# # print(path)
# print(back)

# g = {}
# counter = {} # num of possible visits

# for room in room_graph:
#     g[room] = {v:k for k,v in room_graph[room][1].items()}
#     counter[room] = len(g[room])

# print(g)
# # print(counter)

# stack = []
# stack.append(0)
# visited = set()

# prev = []

# while len(stack) > 0:

#     print('stack',stack)
#     node = stack.pop()
#     print('stack popped', stack)
#     print('prev',prev)

#     if node not in visited:
#         if len(prev) == 0: # for starting room
#             prev.append(node)
#             if counter[node] == 1:
#                 counter[node] -= 1
#                 visited.add(node)
#                 for next_node in g[node]:
#                     if next_node not in visited:
#                         stack.append(next_node)
#             elif counter[node] > 1:
#                 counter[node] -= 1
#                 for next_node in g[node]:
#                     if next_node not in visited:
#                         stack.append(next_node)
#         else:
#             if counter[node] == 1: # leaf node
#                 counter[node] -= 1
#                 visited.add(node)
#                 traversal_path.append(g[prev[-1]][node])
#                 if len(g[node]) == 1:
#                     #
#                     # if stack[-1] == prev[-1]:
#                     #     stack.pop()
#                     #     prev.pop()
#                     #
#                     p = prev.pop()
#                     stack.append(p)
#                     prev.append(node)
#                 else:
#                     while prev[-1] == node:
#                         prev.pop()
#                     prev.pop()
#                     # if prev[-1] == node:
#                     #     prev.pop()
#                     stack.append(prev[-1])
#                     prev.append(node)

#             elif counter[node] > 1:
#                 counter[node] -= 1
#                 traversal_path.append(g[prev[-1]][node])
#                 for next_node in g[node]:
#                     if next_node != prev[-1] and next_node not in visited:
#                         stack.append(next_node)
#                 prev.append(node)
#                 if prev.count(prev[-1]) > 1:
#                     p = prev[-1]
#                     i = prev.index(p)
#                     loop_items = prev[i+1:-1]
#                     prev = prev[:i+1]
#                     for item in loop_items:
#                         visited.add(item)
#                         counter[item] = 0
#                         if item in stack:
#                             stack.pop(stack.index(item))
# print(traversal_path)



# stack = []

# visited = set()

# while len(visited) < len(world.rooms):

#     paths = player.current_room.get_exits()

#     path_list = []

#     for path in paths:
#         if player.current_room.get_room_in_direction(path) not in visited and path is not None:
#             path_list.append(path)
#     visited.add(player.current_room)

#     if len(path_list) > 0:
#         news = random.choice(path_list)
#         stack.append(news)
#         player.travel(news)
#         traversal_path.append(news)
#     else:
#         last_room = stack.pop()

#         def switch(x):
#             switcher = {
#                 'n':'s',
#                 's':'n',
#                 'w':'e',
#                 'e':'w'
#             }
#             return switcher[x]

#         player.travel(switch(last_room))
#         traversal_path.append(last_room)


# TRAVERSAL TEST - DO NOT MODIFY
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
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

# print(len(traversal_path))
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
# world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []


g = {}
counter = {} # num of possible visits

for room in room_graph:
    g[room] = {v:k for k,v in room_graph[room][1].items()}
    counter[room] = len(g[room])

print(g)
print(counter)

stack = []
stack.append(0)
visited = set()

prev = []

while len(stack) > 0:
    node = stack.pop()

    if node not in visited:
        if len(prev) == 0: # for starting room
            prev.append(node)
            if counter[node] == 1:
                counter[node] -= 1
                visited.add(node)
                for next_node in g[node]:
                    if next_node not in visited:
                        stack.append(next_node)
            elif counter[node] > 1:
                counter[node] -= 1
                for next_node in g[node]:
                    if next_node not in visited:
                        stack.append(next_node)
        else:
            if counter[node] == 1 and len(g[node]) == 1:
                counter[node] -= 1
                visited.add(node)
                traversal_path.append(g[node][prev[-1]])
                stack.append(prev[-1])
                prev.pop()
                prev.append(node)
            elif counter[node] > 1:
                counter[node] -= 1
                traversal_path.append(g[prev[-1]][node])
                for next_node in g[node]:
                    if next_node != prev[-1] and next_node not in visited:
                        stack.append(next_node)
                prev.append(node)
print(traversal_path)

#     if node not in visited:
#         if len(prev) == 0:
#             prev.append(node)
#             if node not in counter and len(g[node]) == 1:
#                 counter[node] = 1
#                 visited.add(node)
#                 for next_node in g[node]:
#                     stack.append(next_node)
#             elif node not in counter and len(g[node]) > 1:
#                 counter[node] = 1
#                 for next_node in g[node]:
#                     stack.append(next_node)
#             elif node in counter:
#                 counter[node] += 1
#                 for next_node in g[node]:
#                     stack.append(next_node)

#         elif node not in counter and len(g[node]) == 1:
#             counter[node] = 1
#             visited.add(node)
#             traversal_path.append(g[node][prev[-1]])
#             stack.append(prev[-1])
#             prev.pop()
#         elif node not in counter and len(g[node]) > 1:
#             counter[node] = 1
#             traversal_path.append(g[prev[-1]][node])
#             for next_node in g[node]:
#                 if next_node != prev[-1]:
#                     stack.append(next_node)
#             prev.append(node)
#         elif counter[node] == len(g[node]):
            
#             visited.add(node)
#             stack.append(prev[-1])
#             traversal_path.append(g[node][prev[-1]])
#         elif counter[node] < len(g[node]):
#             counter[node] += 1
#             for next_node in g[node]:
#                 if next_node != prev[-1]:
#                     stack.append(next_node)

#         prev.append(node)
# print(traversal_path)

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
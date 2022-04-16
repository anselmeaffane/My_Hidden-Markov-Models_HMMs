
def yen(nodes, distances, start, end, max_k):
# Dictionary "solspace" stores actual k-shortest paths, the first of which comes from Dijkstra's algorithm.
solspace = {}
potentialsolspace = []
selected = []
# Adding the Dijkstra's shortest path into solspace dictionary
solspace[0] = (dijkstra(nodes, distances, start, end))[0]
# max_k is the specified number of shortest paths you want to find
#max_k = max_k
max_k = 4

# Looping from k = 1 to k = max_K and the 0 to (size of previous entry of solspace)-1
# Reference: http://en.wikipedia.org/wiki/Yen's_algorithm

for k in range(1, max_k):
    #distances = copy.deepcopy(actual_distances)
    for i in range(0, (len(solspace[k - 1]) - 1)):
        spur_node = solspace[k - 1][i]
        spur_node_plus_one = solspace[k - 1][i + 1]
        root_path = solspace[k - 1][0:i + 1]

        for shortPath in solspace:

            path_root_path = (solspace[shortPath])[0:i + 1]
            #print(path_root_path)
            if root_path == path_root_path and (len(solspace[shortPath]) - 1 > i):
                # make each overlapping edges of root path and path_root_path infinity, hence impossible to select
                distances[spur_node][spur_node_plus_one] = float('inf')
                distances[spur_node_plus_one][spur_node] = float('inf')

                # Call Dijkstra function to compute spur path (the shortest path between spur node
                # and end ignoring the i,i+1 edge
                spur_path_a = dijkstra(nodes, distances, spur_node, end)
                spur_path = spur_path_a[0]
                # Restore actual dist to distances nested dictionary
                # Total path is just the combination of root path & spur path
                total_path_tempo = root_path + spur_path
                total_path = []
                # This removes duplicates nodes but note that this is O(n^2) computing time, not efficient
                # Ref: Stack Overflow questions:480214
                [total_path.append(item) for item in total_path_tempo if item not in total_path]
                print(total_path)
                # build up potentialsolspace by adding in total path which are yet found in solspace or Potential
                # hence, the use of nested if
                if total_path not in solspace.values():
                    if [total_path, cost_path(total_path, distances)] not in potentialsolspace[:]:
                        potentialsolspace.append([total_path, cost_path(total_path, distances)])

                distances = copy.deepcopy(actual_distances)
    # This handles the case of there being no spur paths, or no spur paths left.
    # This could happen if the spur paths have already been exhausted (added to A),
    # or there are no spur paths at all such as when both the source and sink vertices lie along a "dead end".
    if len(potentialsolspace) is 0:
        break
    wcg = min(potentialsolspace, key=lambda x: x[1])
    # remove selected potential shortest path from the potential solspace
    potentialsolspace.remove(wcg)
    # Attach minimum of potentialSolSpace into solspace dictionary
    solspace[k] = wcg[0]

return solspace

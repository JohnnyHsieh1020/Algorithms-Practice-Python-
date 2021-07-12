# Graph table
graph = {}
graph["start"] = {}
graph["start"]["a"] = 6
graph["start"]["b"] = 2

graph["a"] = {}
graph["a"]["fin"] = 1

graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5

graph["fin"] = {}

# Costs table
infinity = float("inf")
costs = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

# Route table
parents = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed = []


def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None

    for node in costs:  # Search each nodes.
        cost = costs[node]  # Get the corresponding cost.
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node

    return lowest_cost_node


node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]  # Get the corresponding cost.
    next_nodes = graph[node]  # Find the node's neighbors.

    for n in next_nodes.keys():
        new_cost = cost + next_nodes[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node

    processed.append(node)
    # Find the next node.
    node = find_lowest_cost_node(costs)

print(costs)

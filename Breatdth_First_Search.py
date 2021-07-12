from collections import deque

# Create a hash table.
graph = {}
graph['dog'] = ['chair', 'table', 'tv']
graph['chair'] = ['toys']
graph['table'] = ['food', 'toys']
graph['tv'] = ['ball', 'sofa']
graph['food'] = []
graph['toys'] = []
graph['ball'] = []
graph['sofa'] = []


# Search item
def search_item(data, target):
    return data == target


def search(item, target):
    # Create a queue.
    search_queue = deque()
    search_queue += graph[item]
    # Create a list to track the item that has been searched before.
    searched = []
    while search_queue:
        search = search_queue.popleft()  # Get the first item from the left.
        if search not in searched:
            if search_item(search, target):
                print('Found!')
                return True
            else:
                # Add items to the queue.
                search_queue += graph[search]
                # Marks this item as searched.
                searched.append(search)
    print('Not found!')
    return False


# Let 'dog' search 'food'.
search('dog', 'food')

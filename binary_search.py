def test_location(cards,query, mid):
    print(cards, query, mid)
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[mid] < query:
        return 'left'
    else:
        return 'right'
    
def locate_card(cards,query):
    low, high = 0, len(cards)-1

    while low <= high:
        
        mid = (low + high)//2
        result = test_location(cards,query,mid)
        
        if result == 'found':
            return mid
        elif result == 'left':
            high = mid - 1
        elif result == 'right':
            low = mid + 1
    return -1

cards = [1,2,3,4,5,6,7]
query = int(input('Enter Query: '))
print(locate_card(cards,query))

import random, math, sys

def bogoSort(items):
    # Kopier den liste, vi har modtaget som parameter, så vi ikke ændrer den originale
    items = items.copy()
    isSorted = None # Boolean til markering af, om listen er sorteret
    attempts = 0 # Tællevariabel til at holde styr på antal af forsøg
    while not isSorted:
        attempts += 1
        if attempts > len(items) * 5000: # Check for at stoppe tendensen mod uendeligt
            print('Afbryder på grund af for mange forsøg ({}) og bruger TimSort'.format(attempts))
            items.sort()
            return items
        random.shuffle(items) # Bland alle elementer helt tilfældigt
        isSorted = True # Vi går ud fra at listen tilfældigvis er sorteret,
        # ...og prøver i denne løkke at bevise det modsatte
        for index in range(len(items)-1):
            if items[index] > items[index+1]:
                isSorted = False
                break # Bryd løkken hvis et eneste element er forkert sorteret
    print('Sorteret efter {} forsøg'.format(attempts))
    return items


def selectionSort(items):
    items = items.copy()
    for i in range(len(items) - 1):
        minIdx = i
        for j in range(i, len(items) - 1):
            if items[j] < items[minIdx]:
                minIdx = j
        items[i], items[minIdx] = items[minIdx], items[i]
    return items

def insertionSort(items):
    items = items.copy()
    isSorted = None
    while not isSorted:
        for i in range(len(items) - 1):
            if items[i + 1] < items[i]:
                items[i], items[i - 1] = items[i - 1], items[i]
    for p in range(len(items) - 1)
    return items


if __name__ == '__main__':
    for i in range(10):
        listen = list(range(1, 8))
        random.shuffle(listen)
        sorteret = insertionSort(listen)
        print('Shuffled:\t', listen)
        print('Sorted:\t\t', sorteret)
        print('==============================================================')

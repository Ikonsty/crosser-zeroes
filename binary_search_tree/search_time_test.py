from linkedbst import LinkedBST
from datetime import datetime
from random import sample, shuffle

def find_in_list(words, to_find):
    """
    lst, lst -> float
    Find some words "to_find" in list
    of words from en dictionary
    Return time what was needed for searching
    """
    start_time = datetime.now()
    for w in to_find:
        if w in words:
            pass
    end_time = datetime.now()
    return end_time - start_time


def find_in_tree(tree, to_find):
    """
    bst, lst -> float
    Find some words "to_find" in binary search tree
    of words from en dictionary
    Return time what was needed for searching
    """
    start_time = datetime.now()
    for w in to_find:
        if w in tree:
            pass
    end_time = datetime.now()
    return end_time - start_time


def choose_words(filename, num):
    """
    str, num -> lst
    Read file, choose random "num" word from file
    Return list of random words
    """
    f = open(filename, 'r')
    words = f.readlines()
    f.close()
    ran_lst = sample(words, num)
    words = []
    for w in ran_lst:
        k = w.rstrip()
        words.append(k)
    return words

def main():
    """
    Main function that saves all tests` result into file
    """
    new_file = open("time_research.txt", "w+")
    random_words = choose_words('words.txt', 10000)

    f = open('words.txt', 'r')
    words_last = f.readlines()[:1000]
    f.close()
    words = []
    for w in words_last:
        k = w.rstrip()
        words.append(k)
    new_file.write("Searching in a list: " + str(find_in_list(words, random_words)) + "\n")

    word_tree1 = LinkedBST()
    for w in words:
        word_tree1.add(w)
    new_file.write("Searching in a sorted tree: " + str(find_in_tree(word_tree1, random_words)) + "\n")

    word_tree2 = LinkedBST()
    for w in words:
        word_tree2.add(w)
    word_tree2 = word_tree2.rebalance()
    new_file.write("Searching in a balanced tree: " + str(find_in_tree(word_tree2, random_words)) + "\n")

    word_tree3 = LinkedBST()
    shuffle(words)
    for w in words:
        word_tree3.add(w)
    new_file.write("Searching in a shuffled tree: " + str(find_in_tree(word_tree3, random_words)) + "\n")
    new_file.close()

if __name__ == "__main__":
    main()

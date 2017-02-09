import sys
from itertools import product
import pickle
import math
import random
def read_file(fname):
    file1 = open(fname , "r")
    #lines = file1.readlines()
    allwords = file1.read()
    allwords = allwords.replace("\n" , " ")
    allwords = allwords.split(" ")
    return allwords
    #return words_list
def input_length_file(fname , length):
    new_list = []
    file2 = open(fname , "r")
    allwords = read_file("words.txt")
    for each_word in allwords:
        if int(len(each_word)) == length:
            new_list.append(each_word)
    return new_list

def one_letter_diff_list(input, dict):
    output_list = []
    for i in range(int(len(dict.values()))):
        count = 0
        if int(len(dict[i])) == int(len(input)):
            u = zip (input, dict[i])
            #print u
            for j,k in u:
                if j != k:
                    count = count + 1

            if count == 1 and dict[i] != input:
                output_list.append(dict[i])
    return output_list


def bfs(my_dict, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in my_dict.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


def main():
    dict = {}
    my_dict = {}
    input = raw_input()
    output = raw_input()
    output_list = []
    allwords = read_file("words.txt")
    new_list = input_length_file("words.txt" , int(len(input)))
    #print allwords
    print new_list
    for i in range(int(len(new_list))):
        dict[i] = new_list[i]

    for i in new_list:
        my_dict[i] = one_letter_diff_list(i, dict)
    #print my_dict
    if input and output not in my_dict:
        print "Word(s) not avaialble in the Dictionary"
    else:
        print bfs(my_dict, input, output)
if __name__ == "__main__": main()
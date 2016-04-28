from random import random,randint,shuffle
import math

def get_random_importance(length):
    res = []

def text_to_datalist(path):
    f = open(path, "r")
    a = f.readline().split("\t")
    test_data = []
    for line in f.readlines():
        x = line.split("\t")
        x[-1] = x[-1][0]
        for i in range(len(x)):
            x[i] = int(x[i])-1
        test_data.append(x)
    return test_data

class Tree(object):

    def __init__(self, root):
        self.root = root
        self.v = [None,None]

    def add_branch(self, vk, subtree):
        self.v[vk] = subtree

    def feed_tree(self, inputen):
        inp = inputen[:]
        value = inp.pop()
        if type(self.v[value])== Tree:
            return self.v[value].feed_tree(inp)
        return self.v[value]

    def print_tree(self):
        print(self.root, "parent: ")
        for node in self.v:
            if (type(node)!=Tree):
                print(node)
            else:
                print(node.root)
                node.print_tree()

def decision_tree_learning(examples, attributes, parent_examples=None):
    examples = examples[:]

    if examples==[]:
        return plurality_value(parent_examples)

    elif  same_class(examples):
        return same_class(examples)

    elif attributes == []:
        return plurality_value(examples)

    else:
        #shuffle(attributes)
        #A = attributes.pop()
        A = attributes.pop(importance(examples,attributes))

        tree = Tree(A)
        for vk in [1,0]:
            exs = []
            for e in examples:
                if e[A] == vk:
                    exs.append(e)

            subtree = decision_tree_learning(exs, attributes, examples)
            tree.add_branch(vk, subtree)
        return tree

def plurality_value(li):
    zum = 0
    for data in li:
        zum += data[7]
    if zum > len(li)/2:
        return 1
    if zum < len(li)/2:
        return 0
    if zum == len(li)/2:
        return randint(0,1)

def same_class(li):
    unique = li[0][7]
    for data in li:
        if data[7] != unique:
            return False
    return unique

def test_tree(tree,test_data):
    score = 0
    for data in test_data:
        if tree.feed_tree(data[:-1])==data[-1]:
            score +=1

    return score

def entropy(examples, target_attr):

    ones = 0
    zeroes = 0
    data_entropy = 0.0

    for exs in examples:
        if exs[target_attr]:
            ones += 1
        else:
            zeroes += 1

    data_entropy+= (-ones/len(examples))*math.log(ones/len(examples),2)
    data_entropy+= (-zeroes/len(examples))*math.log(zeroes/len(examples),2)
    return data_entropy

def gain(data, target_attr):

        ones = 0
        zeroes = 0
        data_entropy = 0.0

        for exs in data:
            if exs[target_attr]:
                ones += 1
            else:
                zeroes += 1

        ones_prob = ones/len(data)
        zeroes_prob = zeroes/len(data)

        ones_subset = [exs for exs in data if exs[target_attr] == 1]
        zeroes_subset = [exs for exs in data if exs[target_attr]==0]

        ones_entropy = ones_prob*entropy(ones_subset, target_attr)
        zeroes_entropy = zeroes_prob*entropy(zeroes_subset, target_attr)

        subset_entropy = ones_entropy+zeroes_entropy
        print (subset_entropy)
        return (entropy(data, target_attr)-subset_entropy)

def importance(data, attributes):
    imp_list = []
    for i, attr in enumerate(attributes):
        imp_list.append((gain(data,attr),i))
    return max(imp_list)[1]
 #----------------------------------------------------------------------------------------------------------

examples = text_to_datalist("data/training.txt")
test_data = text_to_datalist("data/test.txt")

attributes = [i for i in range(7)]

a = decision_tree_learning(examples,attributes)
score = test_tree(a,test_data)
#a.print_tree()

print(a.feed_tree([1,0,1,0,0,0,0]))
print (score)

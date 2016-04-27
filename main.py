from random import random,randint,shuffle

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

def decision_tree_learning(examples, attributes, parent_examples=None):
    examples = examples[:]

    if examples==[]:
        return plurality_value(parent_examples)

    elif  same_class(examples):
        return same_class(examples)

    elif attributes == []:
        return plurality_value(examples)

    else:
        A = attributes.pop()
        tree = Tree(A)
        for vk in [0,1]:
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
    return True

def test_tree(tree,test_data):
    score = 0
    for data in test_data:
        if tree.feed_tree(data[:-1])==data[-1]:
            score +=1

    return score
 #----------------------------------------------------------------------------------------------------------

examples = text_to_datalist("data/training.txt")
test_data = text_to_datalist("data/test.txt")

random_importance = [i for i in range(7)]
shuffle(random_importance)
print(random_importance)

a = decision_tree_learning(examples,random_importance)
score = test_tree(a,test_data)
print(a.feed_tree([0,1,0,0,1,1,0]))
print (score)


"""
function DECISION-TREE-LEARNING(examples, attributes, parent examples) returns
a tree
    if examples is empty then return PLURALITY-VALUE(parent examples)
    else if all examples have the same classification then return the classification
    else if attributes is empty then return PLURALITY-VALUE(examples)
    else
        A ←argmaxa ∈ attributes IMPORTANCE(a, examples)
        tree ← a new decision tree with root test A
        for each value vk of A do
            exs ← {e : e ∈examples and e.A = vk}
            subtree ← DECISION-TREE-LEARNING(exs, attributes − A, examples)
            add a branch to tree with label (A = vk) and subtree subtree
        return tree
"""

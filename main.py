from ramdom import random

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
            x[i] = int(x[i]-1)
        test_data.append(x)
    return test_data



def decision_tree_learning(examples, attributes, parent_examples):
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
            for


 #----------------------------------------------------------------------------------------------------------


print(text_to_datalist("data/test.txt"))




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

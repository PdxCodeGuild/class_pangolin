# Shawn Stolsig
# PDX Code Guild
# Assignment: Optional Lab - Tree
# Date: 11/7/2019

import random

names = ['virginia', 'christine', 'carl', 'lillian']

# function for generating a tree
def generate_tree(depth):
    # returns a random number between 1 and 10, representing how many branches from starting node at specified depth
    n_children = int(random.random()*10/depth)
    # if no children
    if n_children == 0:
        # create a leaf node since this node has no childredn
        # a leaf is a dictionary with one property, it's name (chosen randomly from list above)
        return {'type': 'leaf', 'name': random.choice(names)}
    # otherwise, there are children and this node is a branch
    # a branch has one other property, a list of it's child nodes
    branch = {'type': 'branch', 'children': []}

    # for the number of children this node has
    for i in range(n_children):
        # recursively generate another subtree with one higher depther
        child = generate_tree(depth+1)
        # add this subtree to the children list in the branch's property
        branch['children'].append(child)

    # return generated node at this depth
    return branch

# tells how to print node on each line
def print_node(node, indentation):
    # if node is a leaf
    if node['type'] == 'leaf':
        # print passed indentation string and the name of the leaf node
        print(indentation + node['name'])
    # else if node is not a leaf
    else:
        # print the indentation amount and a dash
        print(indentation + '-')
        # recursively call print_node function for each child branch of node
        for i in range(len(node['children'])):
            print_node(node['children'][i], indentation + '\t')


# count all trees and branches
def count_nodes(node):
    # return 1 if function has reached a leaf
    if node['type'] == 'leaf':
        return 1
    # initialize r as 1 to count this node
    r = 1
    # iterate through all children of this node
    for i in range(len(node['children'])):
        # recursively return however many leaf nodes there are in the subtree starting at this node
        r += count_nodes(node['children'][i])
    # return r, which is the count of this node plus all subtrees
    return r

### assignment below #####

# counts all leaves of given node
def count_leaves(node):
    # return 1 if you've arrived at a leaf
    if node['type'] == 'leaf':
        return 1
    # don't count this node since it's not a leaf
    sum = 0
    # if you are not at a leaf, iterate through all children
    for i in range(len(node['children'])):
        # recursively return the count of all leafs that are in the subtree of the input branch node
        sum += count_leaves(node['children'][i])
    return sum

# function that finds leaves with provided name and replaces it with another provided name
def rename_leaves(node, to_find, to_replace):
    sum = 0
    # check if leaf first, then check name
    if node['type'] == 'leaf' and node['name'] == to_find:
        # replace name if it's a match
        node['name'] = to_replace
        return 1
    # else if a leaf but not the right name
    elif node['type'] == 'leaf':
        return 0
    # else must be a branch, continue down tree recursively
    else:
        # for each children of the branch
        for i in range(len(node['children'])):
            # call rename_leaves recursively
            sum += rename_leaves(node['children'][i], to_find, to_replace)
    # return sum, which will be total number of names swapped
    return sum

# main
root = generate_tree(1)
print_node(root, '')
print(f"{count_nodes(root)} total nodes")
print(f"{count_leaves(root)} total leaves")
leaves_changed = rename_leaves(root,names[0],names[1])
print_node(root, '')
print(f"Renamed {names[0]} to {names[1]} {leaves_changed} times.")
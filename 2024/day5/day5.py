def part1():
    # parsing
    with open("input.in") as f:
        lines = f.read().split("\n")
    rules = [rule.split("|") for rule in lines if rule.find("|") != -1]
    for r in rules:
        r[0] = int(r[0])
        r[1] = int(r[1])
    updates = [u.split(",") for u in lines if u.find(",") != -1]
    for u in updates:
        for  i in range(len(u)):
            u[i] = int(u[i])

    sum = 0
    for update in updates:
        indices = {key: index for index, key in enumerate(update)}
        correct = True
        for page in update:
            for rule in rules:
                # page comes first in rule
                if page == rule[0]:
                    second = rule[1]
                    if second in update and indices[second] < indices[page]:
                        correct = False
                elif page == rule[1]:
                    first = rule[0]
                    if first in update and indices[first] > indices[page]:
                        correct = False
        if correct is True:
            sum += update[len(update) // 2]
    print(sum)

from functools import cmp_to_key

class Node:
    def __init__(self,val):
        self.val = val
        self.next = []
    
    def find(self,val):
        if val == self.val:
            return True
        for node in self.next:
            if (node.find(val) == True):
                return True
        return False

import random

def part2():
    # parsing
    with open("input.in") as f:
        lines = f.read().split("\n")
    rules = [rule.split("|") for rule in lines if rule.find("|") != -1]
    for r in rules:
        r[0] = int(r[0])
        r[1] = int(r[1])
    updates = [u.split(",") for u in lines if u.find(",") != -1]
    for u in updates:
        for i in range(len(u)):
            u[i] = int(u[i])

    nodes = {}
    for a, b in rules:
        if a not in nodes:
            nodes[a] = Node(a)
        if b not in nodes:
            nodes[b] = Node(b)
        nodes[a].next.append(nodes[b])
    
    # for node in nodes:
    #     print(node,[p.val for p in nodes[node].next])

    comp = {}
    for a,b in rules:
        if a in comp:
            comp[a].append(b)
        else:
            comp[a] = [b]
    
    def cmp(a,b):
        # b comes after a, i.e. a is less than b
        if b in comp[a]:
            return -1
        elif a in comp[b] is True:
            return 1
        else:
            return 0

    sum = 0
    for i, update in enumerate(updates):
        indices = {key: index for index, key in enumerate(update)}
        correct = True
        # determines correctness
        for page in update:
            for rule in rules:
                # page comes first in rule
                if (page == rule[0] and rule[1] in update and indices[rule[1]] < indices[page]) or (page == rule[1] and rule[0] in update and indices[rule[0]] > indices[page]):
                    correct = False
                    # correct it HERE
                    break
        if correct is False:
            new_update = sorted(update,key=cmp_to_key(cmp))
            # while correct is False:
            #     correct = True
            #     random.shuffle(update)
            #     indices = {key: index for index, key in enumerate(update)}
            #     for page in update:
            #         for rule in rules:
            #             # page comes first in rule
            #             if page == rule[0]:
            #                 second = rule[1]
            #                 if second in update and indices[second] < indices[page]:
            #                     correct = False
            #                     break
            #             elif page == rule[1]:
            #                 first = rule[0]
            #                 if first in update and indices[first] > indices[page]:
            #                     correct = False
            #                     break
            #         else:
            #             continue
            #         break
            sum += new_update[len(new_update) // 2]
    print(sum)




        
    

part1()
part2()

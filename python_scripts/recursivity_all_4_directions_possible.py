# -*- coding: utf-8 -*-
"""
recursivity

"""

import time

instr = ['LEFT ', 'RIGHT ', 'UP ', 'DOWN ']

t3 = time.time()
combi = []
w = []


def pickup(combi, instructions):
    instruction_index = 0
    while instruction_index < 3:
        if len(instructions) < 3:
            instructions.append(instr[instruction_index])
            if len(instructions) == 3:
                combi.append(instructions)
                instructions = instructions[:-1]
                instruction_index += 1
                continue
            combi = pickup(combi, instructions)
        instructions = instructions[:-1]
        instruction_index += 1
    return (combi)


combi = pickup(combi, w)

print(len(combi))
print(combi)
t4 = time.time()
print(t4 - t3)

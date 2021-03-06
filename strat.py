#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rules import surrounding_detection
from rules import start_detection
import numpy as np
import copy


def run(matrix, start_point, step, steps, pre_move, clear_dots, move_list, end):
    
    temp_matrix = copy.deepcopy(matrix)
    move_translate = {0: '↑', 1: '↓', 2: '←', 3: '→'}
       
    if step == 0:
        choice_dict = surrounding_detection(temp_matrix, start_point[0], start_point[1], None, last_move=False)
        clear_dots = [None for i in range(steps + 1)]  # initializing the list for coords of removed points
        move_list = [None for i in range(steps + 1)]

    if step == steps:
        choice_dict = surrounding_detection(temp_matrix, start_point[0], start_point[1], pre_move, last_move=True)
    else:
        choice_dict = surrounding_detection(temp_matrix, start_point[0], start_point[1], pre_move, last_move=False)
    
    possible_moves = []
    
    for i in choice_dict:
        if choice_dict[i] is not None:
            possible_moves.append(i)
    
    if len(possible_moves) == 0:
        return 'Break'
    
    clear_dots[step] = start_point  # The first index in the list would be the coord of starting point
    step = steps - int((np.sum(temp_matrix) - 4) / 2) + 1  # step now = 1
    
    for move in possible_moves:
        for i in range(step, steps + 1):
            clear_dots[i] = None
            move_list[i] = None
    
        for dot in clear_dots:
            if dot is not None:
                temp_matrix[dot[0]][dot[1]] = 0
        
        '''
        print('\n\n\nstep:', step)
        print(temp_matrix, '\n')
        print(clear_dots)
        print(choice_dict)
        '''
        
        new_dot = choice_dict[move]
        
        if step > steps:
            return 'end'
        
        clear_dots[step] = new_dot
        move_list[step] = move
    
        pre_move = move
        _ = run(temp_matrix, new_dot, step, steps, pre_move, clear_dots, move_list, end=end)
        if _ == 'end':
            if step == 1:
                return clear_dots, [move_translate[i] for i in move_list[1:]]
            else:
                return 'end'
        
        
def strat(matrix):
    steps = int((np.sum(matrix) - 4) / 2)
    # print(steps)
    # exit()
    start_point = start_detection(matrix)
    # print(start_point)
    step = 0
    return run(matrix, start_point, step, steps, None, [0], [0], end=False)

def surrounding_detection(matrix, x_start, y_start, pre_move, last_move):
    
    matrix_v = matrix.transpose()
    horizontal_slice = list(matrix[x_start])
    vertical_slice = list(matrix_v[y_start])
    
    h_left, h_right = horizontal_slice[:y_start], horizontal_slice[y_start + 1:]
    v_up, v_down = vertical_slice[:x_start], vertical_slice[x_start + 1:]
    h_left.reverse()
    v_up.reverse()
    # print(horizontal_slice, h_left, h_right)
    # print(vertical_slice, v_up, v_down)
    
    list_potential_dict = {}
    
    def dot_selection(sliced, target, tag):
        list_potential_dict[tag] = None
        for i in range(len(sliced)):
            if target == 2:
                if sliced[i] == 3:
                    break
            if sliced[i] == target:
                # print(len(sliced), sliced[i], tag)
                list_potential_dict[tag] = len(sliced) - 1 - i
                # print(list_potential_dict[tag], i)
                break
    
    target_dict = {True: 3, False: 2}
    
    dot_selection(v_up, target=target_dict[last_move], tag=0)
    dot_selection(v_down, target=target_dict[last_move], tag=1)
    dot_selection(h_left, target=target_dict[last_move], tag=2)
    dot_selection(h_right, target=target_dict[last_move], tag=3)
    
    # print(list_potential_dict)
    
    if list_potential_dict[0] is not None:
        list_potential_dict[0] = (list_potential_dict[0], y_start)  # Up Detection
    if list_potential_dict[1] is not None:
        list_potential_dict[1] = (7 - list_potential_dict[1], y_start)  # Down Detection
    if list_potential_dict[2] is not None:
        list_potential_dict[2] = (x_start, list_potential_dict[2])  # Left Detection
    if list_potential_dict[3] is not None:
        list_potential_dict[3] = (x_start, 7 - list_potential_dict[3])  # Right Detection
    
    pre_move_translate = {0: 1, 1: 0, 2: 3, 3: 2}
    if pre_move is not None:
        list_potential_dict[pre_move_translate[pre_move]] = None
    
    # print(list_potential_dict)
    return list_potential_dict
    
    
def start_detection(matrix):
    print(matrix)
    for i in range(matrix.shape[0]):
        if 1 in matrix[i]:
            for j in range(matrix.shape[1]):
                if matrix[i][j] == 1:
                    print(i, j)
                    return i, j

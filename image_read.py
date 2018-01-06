def image_to_matrix(file):
    
    import matplotlib.pyplot as plt
    from skimage import transform
    import matplotlib.image as mpimg
    import numpy as np
    
    original_image = mpimg.imread(file)
    task_image = original_image[110:1110]
    task_image = transform.resize(task_image, (400, 300))
    background_info = original_image[1000:1120, :120].reshape(14400, 4).transpose()
    r_range = [min(background_info[0]) - 0.02, max(background_info[0]) + 0.02]
    g_range = [min(background_info[1]) - 0.02, max(background_info[1]) + 0.02]
    b_range = [min(background_info[2]) - 0.02, max(background_info[2]) + 0.02]
    
    temp_array = task_image
    new_array = np.zeros(temp_array.shape[:2])
    print('\n\nImage processing...')
    
    for x in range(len(temp_array)):
        for y in range(len(temp_array[0])):
            if r_range[0] < temp_array[x][y][0] < r_range[1] and g_range[0] <\
                    temp_array[x][y][1] < g_range[1] and b_range[0] < temp_array[x][y][2] < b_range[1]:
                new_array[x][y] = 0
            else:
                new_array[x][y] = 1
    
    y_slice = [sum(x) for x in new_array]
    x_slice = [sum(x) for x in new_array.transpose()]
    
    def single_speculate(array):
        if len(array) < 3:
            return False
        for i in range(1, len(array) - 2):
            if array[i] < array[i - 1] and array[i] < array[i + 1]:
                return False
        return True
    
    def analyze(array):
        
        temp_index, temp_mark = [], []
        
        for i in range(1, len(array)):
            if array[i - 1] <= 10 < array[i]:
                temp_index.append([])
                temp_mark.append([])
            if array[i] > 10:
                temp_mark[-1].append(i)
                temp_index[-1].append(array[i])
        
        boundary_estimate = (np.mean(temp_mark[0]), np.mean(temp_mark[-1]))
        seq = list(range(len(temp_index)))
        seq.reverse()
        
        for i in seq:
            if not single_speculate(temp_index[i]):
                temp_mark.remove(temp_mark[i])
        valid_mark = [np.mean(i) for i in temp_mark]
        length = int(np.mean([len(i) for i in temp_mark]))
        
        distances, crosses = [], []
        
        for i in range(1, len(valid_mark)):
            distances.append(valid_mark[i] - valid_mark[i - 1])
        if len(distances) == 0:
            distance = length * 1.66
        else:
            distance = min(distances)
    
        if length * 1.4 < distance < 2.2 * length:
            pass
        else:
            distance = length * 1.66
        for i in np.arange(-8.5, 8.5, 1):
            index = valid_mark[int(len(valid_mark) / 2)] + i * distance
            if boundary_estimate[0] - distance <= index <= boundary_estimate[1] + distance:
                crosses.append(int(index))
        
        return crosses
    
    y_slice = analyze(y_slice)
    x_slice = analyze(x_slice)
    
    plt.figure(0)
    plt.subplot(131)
    plt.title('Original')
    plt.axis('off')

    plt.imshow(original_image)
    plt.subplot(132)
    plt.title('Processed')
    plt.axis('off')

    plt.imshow(new_array, cmap='gray')
    
    for x in x_slice:
        plt.axvline(x, color='white')
    for x in y_slice:
        plt.axhline(x, color='white')
    
    plt.xlim(min(x_slice) - 5, max(x_slice) + 5)
    plt.ylim(min(y_slice) - 5, max(y_slice) + 5)

    matrix = np.zeros((8, 8))
    for y in range(len(y_slice) - 1):
        for x in range(len(x_slice) - 1):
            core = new_array[y_slice[y]:y_slice[y + 1], x_slice[x]:x_slice[x + 1]]

            core_sum = np.sum(core)
            if core_sum > 900:
                matrix[y][x] = 1
                plt.scatter(x_slice[x] + 20, y_slice[y] + 20, marker='+', s=220, c='green')
    
            elif 350 < core_sum < 500:
                if core[int(len(core) / 2)][int(len(core[0]) / 2)] == 1:
                    matrix[y][x] = 2
                    plt.scatter(x_slice[x] + 20, y_slice[y] + 20, marker='^', s=220, c='blue')
    
                else:
                    matrix[y][x] = 3
                    plt.scatter(x_slice[x] + 20, y_slice[y] + 20, marker='*', s=220, c='red')
            else:
                matrix[y][x] = 0
        plt.subplot(133)
    plt.imshow(matrix, cmap='hot')
    plt.title('Abstract')
    plt.axis('off')
    
    plt.show()
    return matrix

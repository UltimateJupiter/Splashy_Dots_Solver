from image_read import image_to_matrix
from strat import strat
for x in range(3, 9):
    task_matrix = image_to_matrix('tasks/' + str(x) + '.png')
    print(strat(task_matrix))
    


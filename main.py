from image_read import image_to_matrix
from strat import strat
import datetime

for x in range(3, 9):
    # start_time = datetime.datetime.now()

    task_matrix = image_to_matrix('tasks/' + str(x) + '.png')
    start_time = datetime.datetime.now()

    result = strat(task_matrix)
    print('Solution:', result[1])
    
    end_time = datetime.datetime.now()
    interval = end_time - start_time
    print('Time_Cost: ' + str(float(str(interval)[6:]) * 1000) + 'ms')

def leastInterval(tasks, n):
    count = [0]*26
    max_frequency = 0
    number_max_freq_tasks = 0
 
    for task in tasks:
        index = ord(task) - ord('A')
        count[index] +=1 
        if max_frequency == count[index]:
            number_max_freq_tasks +=1
        elif max_frequency < count[index]:
            max_frequency = count[index]
            number_max_freq_tasks = 1    
 
    parts = max_frequency - 1
    empty_slots_per_part = n - (number_max_freq_tasks - 1)         
    total_empty_slots = parts * empty_slots_per_part
    remaining_tasks= len(tasks) -  max_frequency * number_max_freq_tasks
    idle_slots = max(0, total_empty_slots - remaining_tasks)
 
    return len(tasks) + idle_slots
     

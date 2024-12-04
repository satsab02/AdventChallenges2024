test = [
    [7,6,4,2,1],
    [1,2,7,8,9],
    [9,7,6,2,1],
    [1,3,2,4,5],
    [8,6,4,4,1],
    [1,3,6,7,9]
]

input = []
file_path = 'Input_Day2.txt'
with open(file_path, 'r') as file:  # Open the file for reading
    for line in file:  # Read each line in the file
    # Split the line into elements, convert them to integers, and add to list_of_lists
        input.append([int(num) for num in line.split()])


def safety_check(masterlist):

    
    safe_count = 0

    for lst in masterlist:
        safe = True
        differences = [abs(lst[i + 1] - lst[i]) for i in range(len(lst) - 1)]  
        
        
        if any(abs(diff) < 1 or abs(diff) > 3 for diff in differences):
            safe = False  
            continue  
        
        
        is_increasing = all(lst[i] < lst[i + 1] for i in range(len(lst) - 1))
        is_decreasing = all(lst[i] > lst[i + 1] for i in range(len(lst) - 1))

        if not (is_increasing or is_decreasing):  
            safe = False
        
        if safe:  
            safe_count += 1
        
    return safe_count   

answer = safety_check(input)

print(answer)
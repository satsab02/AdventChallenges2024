data = 'Input_Day1.txt'

list_a = []
list_b = []

test_a = [3,4,2,1,3,3]
test_b = [4,3,5,3,9,3]

with open(data, 'r') as file:
    for line in file:
        values = line.strip().split()

        list_a.append(int(values[0]))
        list_b.append(int(values[1]))


def list_distance(a, b):

    total_dist = 0

    a.sort()
    b.sort()

    for i in range(0, len(a)):
        dist = abs(a[i] - b[i])
        total_dist += dist
    
    return(total_dist)

def similarity_score(a,b):
    count_a = {}
    count_b = {}

    for i in a:
        count_a[i] = count_a.get(i, 0) + 1
    for i in b:
        count_b[i] = count_b.get(i, 0) + 1
    
    score = 0

    for number, count in count_a.items():
        if number in count_b:
            score += int(number)*int(count)*int(count_b[number])
        else:
            score += 0
    
    return score

#answer = list_distance(list_a, list_b)
answer = similarity_score(list_a, list_b)
print(answer)
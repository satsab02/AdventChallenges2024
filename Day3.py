import re

test ="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()mul(3,6)do()mul(6,9)"

file_path = "Input_Day3.txt"

with open(file_path, 'r') as file:
    input = file.read()


'''
We know that after mul, we need have 4 characters.

regex to find mul(number, number)

make an array of valid muls

sum products
'''



def get_products(mem):
    valid_mul = r"mul\((\d+),(\d+)\)"
    valid_muls = re.findall(valid_mul, mem)
    num_pairs = [(int(num1), int(num2)) for num1, num2 in valid_muls]
    return(num_pairs)

def conditional_mul(mem):
    valid_mul = r"mul\((\d+),(\d+)\)"
    invalid_ident = r"don't\(\)"
    valid_ident = r"do\(\)"
    valid_pairs =[]
    #valid_muls = re.findall(valid_mul, mem)
    valid_matches = []
    invalid_matches = []
    for i in re.finditer(invalid_ident, mem):
        invalid_match = i.start()
        invalid_matches.append(invalid_match)
    for i in re.finditer(valid_ident, mem):
        valid_match = i.start()
        valid_matches.append(valid_match)

    invalid_region = []
    is_active = True

    for i in invalid_matches:
        #find the next do()
        valid_pos = next((pos for pos in valid_matches if pos > i), None)
        if valid_pos > i:
            invalid_region.append((i, valid_pos))
            
            
        else:
            invalid_region.append((i, len(mem)))
            
    
    matches = re.finditer(valid_mul, mem)
    for i in matches:
        start, end = i.start(), i.end()
        pair = i.groups()

       
        is_invalid = any(start>= region[0] and end<=region[1] for region in invalid_region)
        if is_active and not is_invalid:
            valid_pairs.append(pair)
    return(valid_pairs)
    
def mul_sum(pairs):
    sum = 0
    for i in pairs:
        product = int(i[0])*int(i[1])
        sum += product
    return(sum)



pairs = conditional_mul(input)
answer = mul_sum(pairs)
print(answer)
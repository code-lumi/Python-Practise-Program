#lex_auth_012693750719488000124

def get_count(num_list):
    count=0

    # Write your logic here
    for i in range(len(num_list) - 1):  # Iterate through the list until the second-to-last element
        if num_list[i] == num_list[i + 1]:  # Check if the current element is the same as the next one
            count += 1
    return count

#provide different values in list and test your program
inputs = [
    [1, 1, 5, 100, -20, -20, 6, 0, 0],
    [10, 20, 30, 40, 30, 20],
    [1, 2, 2, 3, 4, 4, 4, 10]
]

for lst in inputs:
    print(get_count(num_list))


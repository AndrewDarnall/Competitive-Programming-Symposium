import comboer

# Create a list of integers between -1000 and 1000 with a length from 1 to 50
result_list = [x for x in range(-1000, 1001)][:50]

# Print the result
print(result_list)

print(comboer.solution(result_list))
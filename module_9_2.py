first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(s) for s in first_strings if len(s) >= 5]


second_result = [(first, second) for first in first_strings for second in second_strings if len(first) == len(second)]


third_result = {s: len(s) for s in first_strings + second_strings if len(s) % 2 == 0}


print("first_result:", first_result)
print("second_result:", second_result)
print("third_result:", third_result)
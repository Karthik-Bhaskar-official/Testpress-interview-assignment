#1
def reverse_word(word):
    return word[::-1]

word = input()
if 1 <= len(word) <= 100 and word.islower():
    result = reverse_word(word)
    print(result)
else:
    print("Invalid input. Please make sure the string length is between 1 and 100, and it contains only lowercase characters.")

#2

def check_prime(n):
    for i in range(2, n):
        if(n%i) == 0:
            return "No"
    return "Yes"

n = int(input())

result = check_prime(n)
print(result)

#3

def custom_sort(arr):
    arr = [str(num) for num in arr]
    arr.sort(key=lambda x: x * 3, reverse=True)  
    return ''.join(arr)

input_str = input()

input_str = input_str.strip('[]')
input_array = [int(x) for x in input_str.split(',')]

result = custom_sort(input_array)
print(result)

#4

def reverse_n(n):
    return int(n[::-1])

n = int(input())
if 1 <= n <= 10000:
    result = reverse_n(str(n))
    print(result)
else:
    print("Please enter a number between 1 and 10000.")
    
#5

input_str = input()
new_input = input_str.strip("[]")
list_array = [int(i) for i in new_input.split(",")]
print(max(list_array), min(list_array))


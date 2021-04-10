numbers=[12,13,67,45,34]
new_list=[number for number in numbers if number%2 == 0]
print(new_list)

nums=[ 1,2,3,4,5]
power_of_two=[ num**2 for num in nums ]
print(power_of_two)

words=['automobile','car','anger','fox','anchor']
new_words=[word.capitalize() if word.startswith('a') else word for word in words]
print(new_words)

a=12
b=13.12345
a,b=b,a
print(f"{a:.2f} and {b}")

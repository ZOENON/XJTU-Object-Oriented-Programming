input_numbers = input().split()
sum_of_numbers = sum(float(number) for number in input_numbers)
print(f"{sum_of_numbers} {round(sum_of_numbers)}")
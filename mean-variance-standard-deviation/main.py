from mean_var_std import calculate

numbers = [0,1,2,3,4,5,6,7,8]
result = calculate(numbers)

for key, value in result.items():
    print(f"{key}:{value}\n")
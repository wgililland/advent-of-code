import fileinput

input_val = [int(values) for values in fileinput.input('input_day1')]
for i in range(len(input_val)):
    for j in range(i+1, len(input_val)):
        if input_val[i] + input_val[j] == 2020:
            print(str(input_val[i]*input_val[j]))
        for k in range(j+1, len(input_val)):
            if input_val[i] + input_val[j] + input_val[k] == 2020:
                print(str(input_val[i]*input_val[j]*input_val[k]))

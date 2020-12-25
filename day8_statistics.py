#day8
#20-Dec-2020

def statistics(numbers):
    #validating that input argument is list
    if isinstance(numbers, list):

        #validating if all items are of same data type
        same_data_cond = True
        for item in numbers:
            if not isinstance(item, type(numbers[0])):
                same_data_cond = False
                break

        if same_data_cond:
            #validating that all items in list are numbers
            int_float_cond = all(isinstance(i,(int,float)) for i in numbers)
            
            #if not numbers, then checking if all items are strings with digits
            if int_float_cond != True:
                new_list = [i for i in numbers if i.isdigit()]
                if len(numbers) == len(new_list):
                    for i in range(0,len(numbers)):
                        numbers[i] = int(numbers[i])
                else:
                    print("Only Numbers are allowed in the list")
            
            check_data_type = all(isinstance(i,(int,float)) for i in numbers)

            if check_data_type:
            
                #calculating mean
                mean = sum(numbers)/len(numbers)
                mean = round(mean,2)
            

                #calculating median
                sorted_numbers = sorted(numbers)
                index = len(sorted_numbers)//2
                median = (sorted_numbers[index] + sorted_numbers[(-1*index)-1])/2
                median = round(median,2) 
            

                #calculating mode
                count = []
                for i in sorted_numbers:
                 count.append(sorted_numbers.count(i))
                numb_dict = dict(zip(sorted_numbers,count))

                mode = []
                for key,value in numb_dict.items():
                    if value == max(count):
                        mode.append(key) 
            
                #calculating range
                range1 = sorted_numbers[-1] - sorted_numbers[0]
                range1 = round(range1, 2)

                stats_answer = []
                stats_answer.append(mean)
                stats_answer.append(median)
                stats_answer.append(mode)
                stats_answer.append(range1)

                return stats_answer
            else:
                print("data type is not integer or float")
        else:
            print("List contains items with different data type, Please input list with only numbers as items.")

    else:
        print("Invalid input, Input argument list with numbers (floats and integers) allowed")

input_numbers = input("Enter numbers and separated by comma(,)").replace(" ","")
number_list = input_numbers.split(",")
output1 = statistics(number_list)
print(output1)
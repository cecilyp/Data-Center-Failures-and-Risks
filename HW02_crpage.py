# Homework 02
# [Please replace this comment with your name]

# allowed imports only (you may not need all of these):
import sys, os
import glob
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
# no other imports please!


############## Functions ##############

def load_report(filename):
    file_dict = {}
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip('\n')
            split_line = line.split(':')

            try:
                value = int(split_line[1])
                file_dict[split_line[0]] = value
            except:
                pass

    # print(file_dict)

    return file_dict


def get_id_nums():
    id_nums = []
    for file in os.listdir('reports/'):
        filename = 'reports/{}'.format(file)
        with open(filename, 'r') as file:
            for line in file:
                if "DATACENTER" in line:
                    line = line.strip("\n")
                    new_line = line.split(" ")
                    id_nums.append(new_line[1])
                break
    return id_nums


# [Define any of your other functions here, replacing this code comment]


############ End Functions ############



# [Organize code related to problems in the corresponding sections delineated
# below (if code is required). Place code specific to a (sub)problem BELOW that
# problem's header. Please do not delete header comments]

############## Problem 1 ##############

#### P1.1 ####

#### P1.2 ####

#### P1.3 ####

total_errors = {}

error_names = set()

for file in os.listdir('reports/'):
    file_data = load_report('reports/{}'.format(file))
    for error_type, error_value in file_data.items():
        error_names.add(error_type)
        try:
            current = total_errors[error_type]
            total_errors[error_type] = current + error_value
        except KeyError:
            total_errors[error_type] = error_value


#### P1.4 ####

ID_nums = get_id_nums()


if len(ID_nums) == len(set(ID_nums)):
    print('All {} DATACENTER ids are unique'.format(len(ID_nums)))
else:
    print(len(ID_nums))
    print(len(set(ID_nums)))


for x in range(0, 1431):
    filename = "reports/{:06d}.dat".format(x)
    # print(filename)
    if not os.path.exists(filename):
        print('there is a file that is not sequential')



#### P1.5 ####
# for name in total_errors:
#     print(name)
total_errors['AC'] = total_errors['Air Con.'] + total_errors['A/C']
del total_errors['Air Con.']
del total_errors['A/C']
print(total_errors['AC'])

#### P1.6 ####

############## Problem 2 ##############

#### P2.1 ####

total_errors_for_centers = {}

for num in ID_nums:
    single_report = load_report('reports/{}.dat'.format(num))
    total = 0
    for key,value in single_report.items():
        total = total + int(value)
    total_errors_for_centers[num] = total

worst_centers = sorted(list(total_errors_for_centers.items()), key=lambda x: x[1], reverse=True)[:10]
best_centers = sorted(list(total_errors_for_centers.items()), key=lambda x: x[1], reverse=False)[:10]

print('The Centers with the most errors')
for center in worst_centers:
    print(center[0], ': ', center[1])

print('The Centers with the lease errors')
for center in best_centers:
    print(center[0], ': ', center[1])

#### P2.2 ####

total_centers = 0
total_e = 0
for center, errors in total_errors_for_centers.items():
    total_centers = total_centers + 1
    total_e = total_e + errors

print('The Expected Number (Average) of errors per center is {}'.format(int(total_e/total_centers)))

#### P2.3 ####

sorted_total_errors = sorted(list(total_errors.items()), key=lambda x: x[1], reverse=True)[:10]

total_num_errors = 0

print('\nErrors in highest occurrence')
for error in sorted_total_errors:
    total_num_errors = total_num_errors + error[1]
    print(error[0],':', error[1])

#### P2.4 ####


############## Problem 3 ##############
expected_value_of_water_error = total_errors['Physical intrusion (water)'] / total_num_errors
print(expected_value_of_water_error)

print('expected errors from flooding ', total_num_errors/1430)

#### P3.1 ####
water_errors = []
for id in ID_nums:
    errors = load_report('reports/{}.dat'.format(id))
    try:
        water_error = errors['Physical intrusion (water)']
        water_errors.append(water_error)
        result = scipy.stats.ttest_1samp(water_error, expected_value_of_water_error)
        print(result)
    except KeyError:
        pass



# result = scipy.stats.ttest_1samp(water_errors, expected_value_of_water_error)
# print(result)
#### P3.2 ####

#### P3.2 Bonus ####

#### P3.3 Bonus ####

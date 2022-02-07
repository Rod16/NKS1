#γ =0.94,
#ймовірність безвідмовної роботи на час 449 годин,
#інтенсивність відмов на час 1187 годин
gamma = 0.94
probability = 449
intensity = 1187
work_to_failure_list = [332, 609, 70, 315, 74, 1914, 765, 310, 13, 1746, 362, 303, 508, 1283, 950, 786, 23, 561,
                        2018, 20, 70, 351, 380, 720, 2117, 744, 308, 533, 357, 2058, 378, 420, 145, 987, 1280,
                        440, 104, 189, 83, 866, 9, 2206, 1406, 758, 240, 463, 132, 621, 11, 119, 974, 434, 355,
                        597, 1937, 575, 1239, 791, 987, 173, 1013, 304, 1435, 5, 253, 1288, 237, 386, 282, 300,
                        240, 855, 443, 625, 353, 635, 1099, 758, 164, 507, 733, 963, 159, 133, 22, 1002, 2086,
                        804, 244, 126, 344, 2687, 279, 114, 530, 392, 645, 60, 670, 165]

# Кількість значень
print("Кількість значень: ", len(work_to_failure_list))

# Середній наробіток до відмови Tср.
list_av = sum(work_to_failure_list)/len(work_to_failure_list)
#print("Середній наробіток до відмови Tср.", list_av)

sorted_list = sorted(work_to_failure_list) #Відсортована вибірка
#print(sorted_list)

list_max = max(sorted_list) #Максимальне значення наробітку до відмови
print("Максимальне значення наробітку до відмови: ", list_max)

#Довжина інтервалу
intervals = 10
interval_length = list_max/intervals
print("Довжина інтервалу: ", interval_length)

#Границі інтервалів
interval_bounds = []
for i in range(1, intervals+1):
    interval_bounds.append(round(interval_length * i, 1))
print("Границі інтервалів: ", interval_bounds)

elements_amount = []
statistical_density=[]

for i in interval_bounds:
    #print("i", i)
    elements_amount_counter = 0
    for j in sorted_list:
        if j < i:
            elements_amount_counter +=1
    elements_amount.append(elements_amount_counter)
    #print(elements_amount_counter)
#print(elements_amount)
for count, i in enumerate(elements_amount):
    #print(i, count)
    if count != 0:
        #print(i - elements_amount[count-1])
        statistical_density.append(i - elements_amount[count-1])
statistical_density.insert(0, elements_amount[0])
print("Кількість елементів у кожному з інтервалів: ", statistical_density)

statistical_density_res = []
statistical_density_usage = []
for i in statistical_density:
    #print("{:.6f}".format(i/(len(work_to_failure_list)*interval_length)))
    statistical_density_res.append("{:.6f}".format(i / (len(work_to_failure_list) * interval_length)))
    statistical_density_usage.append(i / (len(work_to_failure_list) * interval_length))
print("Значення статистичної щільності розподілу ймовірності відмови:")
print(statistical_density_res)
#print(statistical_density_usage)

trouble_free_operation = 0
trouble_free_operation_list = []
trouble_free_operation_list_res = []
for count, i, in enumerate(statistical_density_usage):
    trouble_free_operation+=round(i * interval_length,2)
    trouble_free_operation_list.append(trouble_free_operation)
    #print(trouble_free_operation)
#print(trouble_free_operation_list)
for i in trouble_free_operation_list:
    trouble_free_operation_list_res.append(round(1-i,2))
print("Ймовірність безвідмовної роботи пристрою на час правої границі інтервалу:")
print(trouble_free_operation_list_res)
d_text = round(1-gamma,3)
d = 0
#print(d)
T_ind = 0
for count, i in enumerate(trouble_free_operation_list_res):
    if i<gamma:
        d = round((trouble_free_operation_list_res[count] - gamma)/(trouble_free_operation_list_res[count]-1),3)
        T_ind = count
        break
print("d(",d_text, "): ", d)
#print(T_ind)

T = round(interval_bounds[T_ind]-interval_length*d,3)
print("T",gamma, "= ", T)

probability_ind = 0
probability_val = 0
probability_res = 0
probability_counter = 0
intensity_res = 0
for count, i in enumerate(interval_bounds):
    if probability<i:
        #print(i)
        probability_val = i
        probability_ind = count
        for count, j in enumerate(statistical_density_usage):
            #print(j*interval_length)
            probability_counter+= j*interval_length
            if count == probability_ind-1:
                probability_counter+=statistical_density_usage[probability_ind]*(probability_val-probability)
                probability_res = round(1 - probability_counter,3)

                break
        break
#print(probability_ind)
#print(probability_val)
print("Ймовірність безвідмовної роботи на час", probability, "годин:", probability_res)

probability_ind = 0
probability_val = 0
probability_res = 0
probability_counter = 0
for count, i in enumerate(interval_bounds):
    if intensity<i:
        #print(i)
        probability_val = i
        probability_ind = count
        for count, j in enumerate(statistical_density_usage):
            #print(j*interval_length)
            probability_counter+= j*interval_length
            if count == probability_ind-1:
                probability_counter+=statistical_density_usage[probability_ind]*(probability_val-intensity)
                probability_res = round(1 - probability_counter,3)
                intensity_res = round(statistical_density_usage[probability_ind] / probability_res,6)
                break
        break
print("Інтенсивність відмов на час", intensity, "годин: ", intensity_res)
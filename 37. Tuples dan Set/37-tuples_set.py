# Tuples dan Set

# List
data_list = [1,2,3,4,5]
print(data_list)

# Tuples
data_tuples = (1,2,3,4,5)
print(data_tuples)
print(data_tuples[0])
## Data tuple tidak bisa dimodifikasi
# data_tuples[0] = 10000 --> TypeError: 'tuple' object does not support item assignment
# data_tuples.append(1000) --> AttributeError: 'tuple' object has no attribute 'append'
# So, what's tuple used for? --> buat nampung data yang udah fix

# Set
data_set = {1,2,3,4,5}
print(data_set)
## Data set tidak punya index
# print(data_set[2]) --> TypeError: 'set' object is not subscriptable
# So, data set digunakan untuk menampung data yang tidak memperhitungkan index
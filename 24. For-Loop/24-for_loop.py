# For-Loop
print("\n== For-Loop ==\n")
# 1. Pengulangan dengan menggunakan list
# Assign list
angka = [0,1,2,3,4]

for i in angka:
    print(f"Ini loop ke-{i}")
print("End of Loop Program using List \n")

# 2. Loop dengan range
## a. Range original
angka2 = range(5) # Isinya: 0,1,2,3,4

for i in angka2:
    print(f"Ini loop ke-{i}")
print("End of Loop Program using Range \n")

## b. Range dengan nilai awalan tertentu
angka2 = range(2,5) # Isinya: 2,3,4 --> mulai dari angka 2

for i in angka2:
    print(f"Ini loop ke-{i}")
print("End of Loop Program using Range \n")

# 3. Loop dengan string
data_str = "Akooeh Ketjee Abiezz.."
for i in data_str:
    print(i)
print("End of Loop Program using String \n")

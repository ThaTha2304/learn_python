# Dictionary

# List
data_list = ["Jakarta Pusat", "Jakarta Barat", "Jakarta Timur", "Jakarta Selatan", "Jakarta Utara"]
print(data_list)
## Akses member
print(data_list[1])

# Dictionary(dict) --> pasangan antara key:values (associative array)
data_dict = {
    # key:value
    ## Value bebas, bisa isi apa ajaaahhh...
    "jakpus": "Jakarta Pusat",
    "jakbar": 'Jakarta Barat',
    'jaktim': 'Jakarta Timur',
    'jaksel': 'Jakarta Selatan',
    'jakut': 'Jakarta Utara',
    "nmbr": 198.5,
    "bool": True,
    "list": data_list
}
print(data_dict)
## Akses member
print(data_dict["jakpus"])
print(data_dict["nmbr"])
print(data_dict["bool"])
print(data_dict["list"])
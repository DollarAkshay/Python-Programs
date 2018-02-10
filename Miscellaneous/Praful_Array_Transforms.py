import random
import numpy as np
import matplotlib as plt

random.seed(900)


res = 0.1
lat = [1, 2]
lon = [8, 9]
lon_range = (lon[1] - lon[0]) / res
lat_range = (lat[1] - lat[0]) / res

sum = 0
sst_dictionary = {}
for i in range(int(lon_range)):
    for j in range(int(lat_range)):
        # Populate only 50% of the values
        if random.random() < 0.5:
            obj = {}
            lat_v = lat[0] + j * res
            lon_v = lon[0] + i * res

            # Key is of the form '1.4,7.8' i.e '<lon>,<lat>'
            key = str(lon_v) + "," + str(lat_v)
            sst_value = random.randint(20, 30)
            sum += sst_value
            sst_dictionary[key] =


average = sum / len(sst_dictionary)

# Print the sst_dictionary
print("SST Dictionary :")
for key, value in sst_dictionary.items():
    print(key, " = ", value)
print("")

result_dictionary = {}
for i in range(int(lon_range)):
    for j in range(int(lat_range)):
        obj = {}
        lat_v = lat[0] + j * res
        lon_v = lon[0] + i * res
        key = str(lon_v) + "," + str(lat_v)

        # Check if you have sst value for the corresponding lkat,long in the dictionary
        # If it exists get that sst value
        if key in sst_dictionary:
            result_dictionary[key] = sst_dictionary[key]
        else:
            result_dictionary[key] = average


# Print the result_dictionary
print("RTesult Dictionary :")
for key, value in result_dictionary.items():
    print(key, " = ", value)
print("")

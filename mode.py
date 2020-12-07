from collections import Counter
import csv
with open("height-weight.csv", newline='')as f:

    reader = csv.reader(f)
    file_data = list(reader)
file_data.pop(0)
new_data = []
for i in range(len(file_data)):
    n_num = file_data[i][1]
    new_data.append(float(n_num))
data = Counter(new_data)
mrange = {"50-60": 0, "60-70": 0, "70-80": 0}
for height, occurence in data.items():
    if 50 < float(height) < 60:
        mrange["50-60"] += occurence
    elif 60 < float(height) < 70:
        mrange["60-70"]+occurence
    elif 70 < float(height) < 80:
        mrange["70-80"]+occurence
modeRange = 0
modeOccurence = 0
for range, occurence in mrange.items():
    if occurence > modeOccurence:
        modeRange, modeOccurence = [
            int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((modeRange[0]+modeRange[1])/2)
print(mode)

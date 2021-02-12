data = []
count = 0
data_length_sum = 0
data_length_average = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        data_length_sum += len(data[count])
        count += 1
        if count % 10000 == 0:
            print('Loading ... ', count)

data_length_average = data_length_sum / len(data)

print('data_length_average = ', data_length_average)
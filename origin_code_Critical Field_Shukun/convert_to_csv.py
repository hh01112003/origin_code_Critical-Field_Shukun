import pandas as pd

# 读取原
file_path = r"C:\Users\19755\Desktop\JY1-90_Ta027-1.ac.dat"

# 读取数据
with open(file_path, 'r') as file:
    lines = file.readlines()


data_start = lines.index('[Data]\n') + 1
data_lines = lines[data_start:]

# 解析
data = [line.strip().split(',') for line in data_lines]

# 创建DataFrame
columns = data[0]
data = data[1:]
df = pd.DataFrame(data, columns=columns)

# 保存为CSV文件
csv_file_path = r"C:\Users\19755\Desktop\converted_data_JY1-90_Ta027-1.csv"
df.to_csv(csv_file_path, index=False)

print(f"CSV file saved to: {csv_file_path}")

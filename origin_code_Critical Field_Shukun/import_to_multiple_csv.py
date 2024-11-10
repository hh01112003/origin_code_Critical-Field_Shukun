import pandas as pd
import os

# 读取CSV数据
csv_file_path = r"C:\Users\19755\Desktop\converted_data_JY1-90_Ta027-1.csv"
df = pd.read_csv(csv_file_path)
print(f"Successfully read CSV file: {csv_file_path}")

# 根据 Field (Oe) 列分组
grouped = df.groupby('Field (Oe)')
print(f"Number of groups: {len(grouped)}")

# 创建输出目录
output_dir = r"C:\\Users\\19755\\Desktop\\origin_csv_JY1-90_Ta027-1_files"
os.makedirs(output_dir, exist_ok=True)

# 保存每个组为单独的CSV文件，只保留Temperature (K)和m' (emu)两列
for name, group in grouped:
    output_file = os.path.join(output_dir, f"Field_{name}.csv")
    group_filtered = group[['Temperature (K)', "m' (emu)"]]
    group_filtered.to_csv(output_file, index=False)
    print(f"Data written to file: {output_file}")

print(f"All CSV files saved to: {output_dir}")

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import os

# 路径
data_folder = r"C:\Users\19755\Desktop\fit"

# CSV 文件
file_paths = [os.path.join(data_folder, f) for f in os.listdir(data_folder) if f.endswith('.csv')]

# 定义高斯
def gaussian(x, amp, cen, wid):
    return amp * np.exp(-(x-cen)**2 / (2*wid**2))

# 存储拟合参数
fit_parameters = []

# 处理每个文件
for file_path in file_paths:
    df = pd.read_csv(file_path)
    
    # 获取数据
    x = df['Temperature (K)']
    y = df['m" (emu)']
    
    # 初始
    initial_guess = [max(y), x[np.argmax(y)], 1]
    
    try:
        # 高斯拟合
        popt, _ = curve_fit(gaussian, x, y, p0=initial_guess)
        
        # 拟合参数
        amp, cen, wid = popt
       
        fit_parameters.append((file_path, amp, cen, wid))
        
        max_x = cen
        max_y = gaussian(cen, amp, cen, wid)
        
        # 可视
        plt.figure()
        plt.plot(x, y, 'o', label='Data')
        plt.plot(x, gaussian(x, *popt), '-', label='Gaussian Fit')
        plt.plot(max_x, max_y, 'ro', label='Maximum Point')
        plt.xlabel('Temperature (K)')
        plt.ylabel('m" (emu)')
        plt.title(f'File: {os.path.basename(file_path)}')
        plt.legend()
        plt.savefig(os.path.join(data_folder, f"{os.path.basename(file_path).split('.')[0]}_fit.png"))
        plt.close()
        
        # 输出
        print(f'File: {os.path.basename(file_path)}, Max at x = {max_x}, y = {max_y}')
        
    except RuntimeError:
        print(f'Failed to fit data for file: {os.path.basename(file_path)}')
        continue

# 保存最高点到CSV文件
max_points = [(os.path.basename(file_path), cen, gaussian(cen, amp, cen, wid)) for file_path, amp, cen, wid in fit_parameters]
max_points_df = pd.DataFrame(max_points, columns=['File', 'Max_x', 'Max_y'])
max_points_df.to_csv(os.path.join(data_folder, 'max_points.csv'), index=False)

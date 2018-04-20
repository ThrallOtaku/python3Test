# coding:utf-8

import numpy as np
import pandas as pd
# 导入图表库以进行图表绘制
import matplotlib.pyplot as plt

#参考连接https://www.cnblogs.com/jianjianyu/p/7102645.html

loandata = pd.DataFrame(pd.read_excel('loan_data.xlsx'))

print(loandata)

# 按月汇总贷款金额及利息
loan_x = loandata['loan_amnt']
loan_y = loandata['total_rec_int']
loan_z = loandata['total_rec_int']
# 图表字体为华文细黑，字号为15
plt.rc('font', family='STXihei', size=15)
# 设置气泡图颜色
colors = ["#99CC01", "#FFFF01", "#0000FE", "#FE0000", "#A6A6A6", "#D9E021", '#FFF16E', '#0D8ECF', '#FA4D3D', '#D2D2D2',
          '#FFDE45', '#9b59b6']
# 创建气泡图贷款金额为x，利息金额为y，同时设置利息金额为气泡大小，并设置颜色透明度等。
plt.scatter(loan_x, loan_y, s=loan_z, color=colors, alpha=0.6)
# 添加x轴标题
plt.xlabel(u'贷款金额')
# 添加y轴标题
plt.ylabel(u'利息收入')
# 添加图表标题
plt.title(u'贷款金额与利息收入')
# 设置背景网格线的颜色，样式，尺寸和透明度
plt.grid(color='#95a5a6', linestyle='--', linewidth=1, axis='both', alpha=0.4)
# 显示图表
plt.show()

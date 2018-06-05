# 程序功能：
# 记录python pandas 读取外部文件 的方法，包括
# 1.sas格式数据
# 2.csv格式数据
# 3.excel格式
# 4.通过mysql读取






import pandas as pd 
import numpy as np 
import os 




# 1.sas 文件读取并且保存到csv文件
# 切换工作路径

path = '/media/sean/项目/4.Project/Current/5.Sharpe_Ratio/analysis/input/InvestmentRelatedData'

os.chdir(path)

# 获取所有的sas文件，并将文件名保存在list Files中

def main():
	Files = []
	for file in os.listdir():
	    if os.path.splitext(file)[1] == '.sas7bdat':
	        Files.append(os.path.splitext(file)[0])

	# 针对每一个sas文件，转换为csv文件
	for file in Files:
	    sasfile = file + ".sas7bdat"
	    csvfile = file + ".csv"
	    print(sasfile)
	    print(csvfile)
	    df = pd.read_sas(sasfile)
	    df.to_csv(csvfile)


if __name__== "__main__":
	main()
from openpyxl import workbook
from openpyxl import load_workbook

# 讀檔
wb = load_workbook('bom.xlsx')

# 指定工作表
sheet = wb.get_sheet_by_name("bom")
new = wb.get_sheet_by_name("Sheet1")

#先定義Sheet1要使用的A, B欄row index初始值
global_A_col = 1	
global_B_col = 1
# 印出bom J列的所有內容
for i in sheet["J"]:
	rawstr = str(i.value)
	#計算該欄位以 , 區分的陣列長度
	str_len = len(rawstr.split(",")) 
	for j in range(0,str_len):
		#寫入Sheet1的A1
		new['A'+str(global_B_col)] = sheet['D'+str(global_A_col)].value
		#寫入Sheet1的B1
		new['B'+str(global_B_col)] = rawstr.split(",")[j]
		global_B_col = global_B_col + 1
	#Bom J列第一行處理完後，再把整個Index +1
	global_A_col = global_A_col + 1
		
#另存新檔，檔名為Final.xlsx
wb.save('Final.xlsx')


# # 獲取A1格的值
# print(sheet['C9'].value)
# print(sheet1['A1'].value)

# # 獲取表的最大工作列數
# print('The max row of this sheet is ' + str(sheet.max_row))
# # 獲取表的最大工作行數
# print(sheet.max_column)

# 印出D列的所有內容
# for i in sheet["D"]:
    # print(i.value)
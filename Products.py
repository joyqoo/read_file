import os # operating system
# 讀取檔案
def read_file(fileName): 
	products = []
	with open(fileName,'r', encoding='utf-8') as f:
		for line in f:
			if '商品名稱,商品價格' in line:
				continue
			name ,price = line.strip().split(',')
			products.append([name, price])
	return products

# 讓使用者輸入
def user_point(products):
	while True:
		name = input('請輸入商品名稱: ')
		if name =='q':
			break;
		price = int(input("請輸入商品價格: ")	)
		products.append([name, price])
	print(products)
	return products

# 印出所有購買紀錄
def print_products(products):
	for product in products:
		print(product[0],'的價格是',product[1])

# 寫入檔案
def write_file(fileName, products):
	with open(fileName, 'w', encoding='utf-8') as f:
		f.write('商品名稱,商品價格\n')
		for product in products:
			f.write(product[0] + " , " + str(product[1]) + '\n')

# 主程式執行
def main(fileName):
	if os.path.isfile(fileName): #檢查檔案是否存在
		print('已搜尋到目標檔案')
		products = read_file(fileName)
	else:
		print('未搜尋到目標檔案')	

	products = user_point(products)
	print_products(products)
	write_file(fileName,products)

main('products.csv')
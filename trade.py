import csv,os,glob
#get file list in Market Data
def get_file_list(dir_path, extension_list):
    os.chdir(dir_path)
    file_list = []
    for extension in extension_list:
        extension = '*.' + extension
        file_list += [os.path.realpath(e) for e in glob.glob(extension)]
        return file_list

dir_path = r'E:\assignment\Market Data'
extension_list = ['csv']
csv_filelist = get_file_list(dir_path, extension_list)


#read in the parameters

Month_char = {'F':'01','G':'02','H':'03','H':'04','J':'05','K':'06','M':'07','Q':'08','U':'09','V':'10','X':'11','Z':'12'}
sma = []
upperband = []
lowerband = []
rsi = []
close_price = []
open_price = []
period = 20
money_left = 10000000.0
stock_price_hold = 22500.0
stock_number = 0


with open(r'E:\assignment\result.csv','r') as resultReader:    
    reader = csv.reader(resultReader)
    result_line = resultReader.readline()
    for result_line in reader:
        if(result_line[0]=='sma'):
            for x in result_line:
                sma.append(x)
        if(result_line[0]=='lowerband'):
            for x in result_line:
                lowerband.append(x)
        if(result_line[0]=='upperband'):
            for x in result_line:
                upperband.append(x)
        if(result_line[0]=='rsi'):
            for x in result_line:
                rsi.append(x)

with open(r'E:\assignment\recordopen.csv','r') as openreader:
    readeropen = csv.reader(openreader)
    open_line = openreader.readline()
    for open_line in readeropen:
        open_price.append(open_line[0])

with open(r'E:\assignment\recordclose.csv','r') as closereader:
    readerclose = csv.reader(closereader)
    close_line = closereader.readline()
    for close_line in readerclose:
        close_price.append(close_line[0])
#min(close or open) > upperband => buy
#max(close or open) < lowerband => sell

#begin to trade
tradetype = ''
for i in range(20,80):
        j=i-20
        if(max(close_price[j],open_price[j])>upperband[j]):
            tradetype = 'B'
            print('buy')
        if(min(close_price[j],open_price[j])<lowerband[j]):
            tradetype = 'S'
        if(tradetype==''):
            print('sell')
            continue
        
        with open(csv_filelist[i], 'r') as readCsvFile:
            csvreader = csv.reader(readCsvFile)
            line = readCsvFile.readline()
            this_month = readCsvFile.name[30]+readCsvFile.name[31]
            this_day = ''
            for x in readCsvFile.name[30:34]:
                this_day = this_day+x

#begin to read each line in csv
#judge buy or sell


      
#filter by date
            for line in csvreader:
                data_flag = False
                if(this_month== Month_char[line[1][3]]):
                    data_flag = True
                if((this_day == '1129')and(line[1][3]=='Z')):
                    data_flag=True
                if((this_day=='1231')and(line[1][3]=='F')):
                    data_flag=True
                if((this_day =='0130')and(line[1][3]=='G')):
                    data_flag=True
                if((this_day=='0228')and(line[1][3]=='H')):
                    data_flag=True
                if(float(line[2])>=99999):
                    data_flag=False
                if(data_flag==False):
                    continue
#               if(tradetype == 'B'):
#                print 'price ',line[2]
#                print 'stock ',stock_price_hold
                if(float(line[2])<stock_price_hold):
                    
                    if(money_left <= 0):
                        continue
                    print 'price ',line[2]
                    print 'stock ',stock_price_hold
                    buymoney = float(line[2])*(float(line[17])+float(line[19]))
                    print 'buy money',buymoney
                    total_stock = stock_number*stock_price_hold
                    print 'money left' , money_left
                    
                    money_left = money_left-buymoney                    
                    stock_number =stock_number+float(line[17])+float(line[19])
                    stock_price_hold = (total_stock + buymoney)/stock_number
                    print 'buy','money left', money_left,'stock price',stock_price_hold,'this day',this_day
                    print ' '
#               if(tradetype == 'S'):

                if(line[2]>stock_price_hold):
                    
                    if(stock_number-float(line[6])-float(line[8])<0):
                        continue
                    print 'price ',line[2]
                    print 'stock ',stock_price_hold
                    sellmoney = float(line[2])*(float(line[6])+float(line[8]))
                    print 'sell money',sellmoney
                    total_stock = stock_number*stock_price_hold                    
                    stock_number = stock_number-float(line[6])-float(line[8])
                    money_left = money_left+sellmoney
                    if(stock_number!=0):
                        
                        stock_price_hold = (total_stock - sellmoney)/stock_number
                    print 'total stock ',total_stock - sellmoney, 'stock number ',stock_number
                    print 'sell','money left', money_left,'stock price',stock_price_hold,'this day',this_day
                    print ' '
'''
                with open(r'E:\assignment\trade.csv','a') as trade_writer:
                    trade_writer.write(tradetype + 'money left'+ money_left)
'''                    
                      
                                            
         
                
            

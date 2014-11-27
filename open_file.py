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


#get the close price of all files

Month_char = {'F':'01','G':'02','H':'03','H':'04','J':'05','K':'06','M':'07','Q':'08','U':'09','V':'10','X':'11','Z':'12'}
close_price = []
open_price = []

with open(r'E:\assignment\recordclose.csv','a')as saveFile1:
    saveFile1.writelines('\n')

for file in csv_filelist:
    with open(file, 'r') as readCsvFile:
        reader = csv.reader(readCsvFile)
        line = readCsvFile.readline()
        this_month = readCsvFile.name[30]+readCsvFile.name[31]
        this_day = ''
        for x in readCsvFile.name[30:34]:
            this_day = this_day+x
#begin to read each line in csv
        data_get_close = False
        data_get_open = False
		
#after filter by date                    
        for line in reader:
            data_flag = False
            if(this_month == Month_char[line[1][3]]):
                data_flag = True
            if(this_day == '1129')and(line[1][3]=='Z'):
                data_flag = True    
            if(this_day == '1231')and(line[1][3]=='F'):
                data_flag = True
            if(this_day == '0130')and(line[1][3]=='G'):
                data_flag = True
            if(this_day == '0228')and(line[1][3]=='H'):
                data_flag = True





            if (line[0] >= '091500' ) and (float(line[2])<99999) and (data_flag==True) and (data_get_open==False):
                data_get_open = True
                print ('open price of '+this_day+' is '+line[2])
                open_price.append(line[2])
                with open(r'E:\assignment\recordopen.csv','a')as saveFile1:
                    saveFile1.writelines(line[2]+'\n')
                
                
            elif(line[0] >= '091500')and (line[0] <= '161500') and (float(line[2])<99999) and (data_flag==True) and (data_get_open==False):
                data_get_open = True
                print ('open price of '+this_day+' is '+line[2])
                open_price.append(line[2])
                with open(r'E:\assignment\recordopen.csv','a')as saveFile1:
                    saveFile1.writelines(line[2]+'\n')
                
#get all the close prices
                
            if (line[0] >= '161548') and (float(line[2])<99999) and (data_flag==True) and (data_get_close==False):
                data_get_close = True
                print ('close price of '+this_day+' is '+line[2])
                open_price.append(line[2])
                with open(r'E:\assignment\recordclose.csv','a')as saveFile:
                    saveFile.writelines(line[2]+'\n')
                
            elif (this_day=='1224' or this_day =='1230' or this_day=='1231' or this_day=='0129' or this_day=='0130' or this_day=='0227') and (line[0]== '120000') and (float(line[2])<99999) and (data_flag==True) and (data_get_close==False):
                data_get_close = True
                print ('close price of '+this_day+' is '+line[2])
                open_price.append(line[2])
                with open(r'E:\assignment\recordclose.csv','a')as saveFile:
                    saveFile.writelines(line[2]+'\n')

#get all the open prices     
            

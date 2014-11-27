import csv,os,math
#calculate all the bollinger band including SMA upperband and lowerband
#calculate the RSI
close_price = []
sma = []
rsi = []
upperband = []
lowerband = []
period = 20
multiplier = 2
#calculate the bollinger band
with open(r'E:\assignment\recordclose.csv','r') as closePriceReader:
    
    reader = csv.reader(closePriceReader)
    priceLine = closePriceReader.readline()
    for priceLine in reader:
        close_price.append(priceLine[0])

#calculate the sma
def toavr(seq=[]):
    avg = 0.0
    sum_1 = 0.0
    for x in seq:
        sum_1 = sum_1 + float(x)
        avg = (sum_1/len(seq))
    return avg

for i in range(period,len(close_price)):
    avg = 0.0
    avg = toavr(close_price[(i-period):i])
    sma.append(avg)

#calculate the upperband and lowerband
def tostand(seq=[]):
    stand = 0.0
    sum1 = 0.0
    avr = toavr(seq)
    for x in seq:
        sum1 = sum1 + (avr-float(x))**2
    stand = math.sqrt(sum1/period)
    return stand

for i in range(period,len(close_price)):
    stand =sma[i-period]+multiplier*tostand(close_price[(i-period):i])
    stand1 = sma[i-period]-multiplier*tostand(close_price[(i-period):i])
    upperband.append(stand)
    lowerband.append(stand1)

    
#calculate the RSI
def tors(seq=[]):
    rs = 0.0
    rsi_temp = 0.0
    sum_gain = 0.0
    sum_loss = 0.0
    
    for i in range(1,len(seq)):
        if(seq[i] >= seq[i-1]):
            sum_gain = sum_gain + (float(seq[i])-float(seq[i-1]))
            
        if(seq[i] < seq[i-1]):
            sum_loss = sum_loss + (float(seq[i-1])-float(seq[i]))
    sum_gain = sum_gain/(len(seq))
    sum_loss = sum_loss/(len(seq))

    rs = sum_gain/sum_loss
    rsi_temp = 100.0-100.0/(1+rs)
    return rsi_temp

for i in range(period,len(close_price)):
    rsi_this = tors(close_price[(i-period):i])
    rsi.append(rsi_this)


#save the calculate result
with open(r'E:\assignment\result'+str(period)+' '+str(multiplier)+'.csv','a') as result_writer:    
    def outResult(seq=[],name=''):
        result_writer.write(name+',')
        for x in seq:
            result_writer.writelines(str(x)+',')
        result_writer.writelines('\n')
        return

    outResult(sma,'sma')
    outResult(upperband,'upperband')
    outResult(lowerband,'lowerband')
    outResult(rsi,'rsi')


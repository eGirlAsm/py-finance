
import locale

def getProfit(amount, percent):
	return amount * (percent / 100)

# 100 만원
initial_money = 1560000 

locale.setlocale( locale.LC_ALL, 'ko_KR' )

temp = initial_money
for x in range(1,100):
	p = getProfit(temp, 30)
	print(f'invest times {x} percent = 30% org { str(locale.currency(temp,grouping=True))} interest = { str(locale.currency(p,grouping=True))}')
	temp = temp + p
#	profit = temp
#	temp = temp +  temp * 30 / 100
##	print('profit is ' + str(temp - profit))
#	print('```in ' + str(x) + ' times the total = ' + str(locale.currency(temp,grouping=True)) + '원  이자 ' + str(30) + '% 순수익 ' + str(locale.currency(temp-profit,grouping=True)) + ' ```\r\n')
##	print(temp)


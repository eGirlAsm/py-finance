
import locale
# 100 만원
initial_money = 1000000 

locale.setlocale( locale.LC_ALL, 'ko_KR' )

temp = initial_money
for x in range(1,100):
	profit = temp
	temp = temp +  temp * 10 / 100
#	print('profit is ' + str(temp - profit))
	print('in ' + str(x) + ' times the total = ' + str(locale.currency(temp,grouping=True)) + '원  이자 10% 순수익 ' + str(locale.currency(temp-profit,grouping=True)) + ' \r\n')
#	print(temp)


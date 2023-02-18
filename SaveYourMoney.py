import os
import sys
from termcolor import colored

options = '''
[a]
		20% ===> Spending
		30% ===> Goal Savings
		25% ===> Crypto Investment
		25% ===> Savings


[b]
		40% ===> Spending
		40% ===> Goal Savings
		20% ===> Savings


[c]
		10% ===> Spending
		40% ===> Goal Savings
		50% ===> Savings


[d]
		40% ===> Savings
		60% ===> Wants

'''
#	phone, rent, laundry, wifi, insurance, gas, nicotine, food, electric
def pd():
	bills = 55 + 400 + 20 + 40 + 110 + 50  + 50 + 150 + 50
	sum = bills / 2
	billsM = ''
	subtotal = 0
	run = ''
	opt1 = input('[a] Set Bills\n[b] Input Bills:\n \n> ')
	if opt1 == 'b':
		while run != 'q':
			billsM = int(input('Put In A Bill You Pay Monthly <press "q" to quit>:\n> '))
			subtotal = billsM + subtotal
			run = input(colored('[q]uit  OR  [c]ontinue:\n> ', 'red'))
			if run  == 'q':
				print(f'\n \n{subtotal} Is What You Pay Every Month\n \n')
				billsB = subtotal * .5
				print(f'{billsB} Is Your Bills Broken Down To Every Pay Period \n \n')
		paycheck = int(input('What Is Your Paycheck:\n> '))
		leftover = paycheck - billsB
		print(f'{leftover}  Is What Is Leftover After Subtracting Your Paycheck To Your Broken Down Monthly Bills \n \n')
		print('\n' + options)
		select = ''
		while select != 'q':
			select = input('> ')
			if select == 'a':
				spending = leftover * .2
				goals = leftover * .3
				crypto = leftover * .25
				savings = leftover * .25
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nCRYPTO: ${crypto}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
				print(colored(f'${billsB} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Put Away In Your Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'b':
				spending = leftover * .4
				goals = leftover * .4
				savings = leftover * .2
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
				print(colored(f'${billsB} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Put Away In Your Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'c':
				spending = leftover * .1
				goals = leftover * .4
				savings = leftover * .5
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#                       vv  <--   <billsB  OR  sum>   -->  vv
				print(colored(f'${billsB} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Be Putting Away In Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'd':
				wants = leftover * .6
				savings = leftover * .4
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'WANTS: ${wants}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#                       vv  <--   <billsB  OR  sum>   -->  vv
				print(colored(f'${billsB} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Be Putting Away In Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))
			else:
				print('Error Occurred')







	elif opt1 == 'a':
		paycheck = int(input('What Is Your Paycheck:\n> '))
#	CHANGE THIS PART OUT IF SWITC
		leftover = paycheck - sum
		print(f'{leftover}  Is What Is Leftover After Subtracting Your Paycheck To Your Broken Down Monthly Bills \n \n')
		print('\n' + options)
		select = ''
		while select != 'q':
			select = input('>  ')
			if select == 'a':
				spending = leftover * .2
				goals = leftover * .3
				crypto = leftover * .25
				savings = leftover * .25
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nCRYPTO: ${crypto}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#			vv	<--   <billsB  OR  sum>   -->  vv
				print(colored(f'${sum} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Put Away In Your Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'b':
				spending = leftover * .4
				goals = leftover * .4
				savings = leftover * .2
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#			 vv  <--   <billsB  OR  sum>   -->  vv
				print(colored(f'${sum} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Put Away In Your Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'c':
				spending = leftover * .1
				goals = leftover * .4
				savings = leftover * .5
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'SPENDING: ${spending}\nGOALS: ${goals}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#			vv  <--   <billsB  OR  sum>   -->  vv
				print(colored(f'${sum} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Be Putting Away In Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))

			elif select == 'd':
				wants = leftover * .6
				savings = leftover * .4
				dWeeks = 52 / 2
				yearlyS = dWeeks * savings
				print(colored(f'WANTS: ${wants}\nSAVINGS: ${savings}', 'green'))
				print('\n \n ^ ^    This Is What How You Should Put Away Your Money   ^ ^\n \n')
#			vv  <--   <billsB  OR  sum>   -->  vv
				print(colored(f'${sum} Is How Much You Need To Pay In Bills This Pay Period :( \n \n', 'red'))
				print(colored(f'${yearlyS} Is How Much You Would Be Putting Away In Savings In A Years Time \n \n', 'green'))
				format = str(savings) + '\n'
				with open('SAVINGS.txt', 'a') as f:
					f.write(format)
				print(colored('Your Savings Account Has Been Stored In "SAVINGS.txt"', 'yellow'))


			elif select == 'q':
				break

			else:
				print(colored('Error Occurred', 'red'))

		else:
			print('ErrorOccurred')

pd()

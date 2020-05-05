import random
start = input('请输入随机数字的开始数： ')
end = input('请输入随机数字的结束数： ')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	guess_num = input('请输入猜测的数字： ')
	guess_num = int(guess_num)
	count += 1  # count = count + 1
	if guess_num == r:
		print('恭喜你猜中了！')
		print('你已经猜了', count, '次')
		break
	elif guess_num > r:
		print('比答案大。')
	elif guess_num < r:
		print('比答案小')
	print('你已经猜了', count, '次')


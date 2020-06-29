import os
import time 
import sys, platform
"""
print(os.getcwd())
path = os.getcwd() + '/Banco_armazenamento/'
os.chdir(path)
print(os.getcwd())
print(os.listdir(path))
with open(path + 'teste','a+') as file:
	file.write('lol')
"""

#num = int(input('Digite o tempo em minutos:\n'))
#um = num * 60
"""
for i in num:
    	sys.stdout.write("\r{i}:{index}".format(i, index))
	for index in num_2:
		sys.stdout.flush()
    	time.sleep(1)
"""
"""
minutos = num // 60 
segundos = 0

for i in range(num,0,-1):
	if segundos == 0:
		segundos = 60	
		minutos -= 1
	if minutos < 10:
		if segundos < 10:
			sys.stdout.write(f'\r0{minutos}:0{segundos}\n')
		else:
			sys.stdout.write(f'\r0{minutos}:{segundos}\n')
	 
	else:
		sys.stdout.write(f'\r{minutos}:{segundos}\n')
	
	sys.stdout.flush()
	time.sleep(1)
	segundos -= 1

"""




print(platform.system())
lis = [1,1,1,]
print(lis, len(lis))
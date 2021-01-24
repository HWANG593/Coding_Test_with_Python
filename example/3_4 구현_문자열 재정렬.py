import copy

data = 'AJKDLSIKJSJ0D'

tmp = []

for i in range(len(data)):
    tmp.append(data[i])


tmp.sort()
tmp1 = copy.deepcopy(tmp)

number = 0

for j in range(len(tmp)):
    if not 65<= ord(tmp[j])<= 90:
        number += int(tmp1.pop(0))
    
    else:
        string = ''.join(tmp1)

if str(number) != '0':        
	print(string + str(number))

else:
    print(string)
    
    
########################################

data = 'AJKDLSI412K4JSJ9D'

result = []
value = 0

for i in data:
    if i.isalpha():
        result.append(i)
    
    else:
        value += int(i)

result.sort()

if value !=0:
    result.append(str(value))
    
print(''.join(result))
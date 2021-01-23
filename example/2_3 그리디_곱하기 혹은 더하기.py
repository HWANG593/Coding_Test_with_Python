S = '0057084'
tmp_list = []
for i in S:
    tmp_list.append(i)

basic = tmp_list.pop(0)
basic = int(basic)

for num in tmp_list:
    if basic <= 1 or int(num) <= 1:
        basic += int(num)

    else:
        basic *= int(num)

print(basic)
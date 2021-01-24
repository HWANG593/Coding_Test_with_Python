N = 4
plan = ['R', 'R', 'R', 'U', 'D', 'D']

x = 1
y = 1

for i in plan:
    if i == 'R':
        if y != N:
            y += 1
        else:
            continue
    
    elif i == 'L':
        if y != 1:
            y -= 1
        else:
            continue
    
    elif i == 'U':
        if x != 1:
            x -= 1
        else:
            continue
        
    else:
        if x != N:
            x += 1
        else:
            continue
        
print(x,y)
    
    
####################################

# 동, 북, 서, 남
n = 5

# 현재 위치
x,y = 1,1
plans = ['R', 'R', 'R', 'U', 'D', 'D']

dx = [0,0,-1,1]		# x는 세로축
dy = [1,-1,0,0]		# y는 가로축
move_types = ['R','L','U','D']


# 이동할 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구해놓기
    for i in range(len(move_types)):
    	if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
	
    if nx<1 or ny<1 or nx>n or ny>n:
        continue
    else:
        x = nx
        y = ny
        
print(x,y)
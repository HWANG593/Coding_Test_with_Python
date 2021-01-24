data = 'b2'

for i in range(1,9):
    if data[0] == chr(i+96):
        x = i

y = int(data[1])
    
behavior = ['RRU','RRD','LLU','LLD','UUR','UUL','DDR','DDL']

dx = [-1,1,-1,1,-2,-2,2,2]
dy = [2,2,-2,-2,1,-1,1,-1]


count = 0
for i in range(len(behavior)):
    nx = x+dx[i]
    ny = y+dy[i]
    
    if nx<1 or ny<1 or nx>8 or ny>8:
        continue
    else:
        count += 1
        
print(count)
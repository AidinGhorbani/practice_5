x = int(input('x:'))
y = int(input('y:'))

m = min(x , y)
ma = max(x , y)

for i in range(m , ma+1):
    print(i)
# ----------------------------------

t = int(input('t:'))
p = int(input('p:'))

for i in range(1 , t+1):
    if t % i == 0 and p % i == 0:
        print(i)

# ------------------------------------

t = int(input('m:'))
p = int(input('i:'))

for i in range(m , 0 , -1):
    if t % i == 0 and p % i == 0:
        print(i)
        break

#-------------------------------------
o = int(input('o: '))
v = int(input('v: '))
max_ = max(o , v)
min_ = min(o , v)

for i in range(1 , min_+1):
    if (max_ * i) % min_ == 0:
        print(i * max_)
        break



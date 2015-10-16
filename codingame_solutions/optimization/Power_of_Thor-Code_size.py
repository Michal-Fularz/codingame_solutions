__author__ = 'Amin'
L,M,T,U=[int(i) for i in input().split()]
while 1:
 a=""
 if M<U:a+="N";U-=1
 if M>U:a+="S";U+=1
 if L<T:a+="W";T-=1
 if L>T:a+="E";T+=1
 print(a)
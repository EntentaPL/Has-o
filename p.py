import random
n = int(input("Enter a lenght of the password:   "))

result = []
value = "!,@,#,$,%,&,_,-,1,2,3,4,5,6,7,8,9,0,q,w,e,r,t,y,u,i,o,p,a,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m,Q,W,E,R,T,Y,U,I,O,P,A,S,D,F,G,H,J,K,L,Z,X,C,V,B,N,M,"
list = value.split(',')


x = 0


while x < n :
   x = x + 1
   result.append(random.choice(list))

print("".join(result))
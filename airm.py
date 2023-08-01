a=[]
def sum(x,*a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]
    return sum

# def name(*inp):
#     for i in range(len(inp)):
#         print(inp[i]);

# name("hello",45,'t')


# def add(i):
#     sm=0
#     for i in range(i,(i+10)):
#         sm+=i
#     return sm    
     
# a=int(input("Enter a number : "))
# if(type(a)==type(34)):
#     i=a
#     print("Here the sum : ",add(i))
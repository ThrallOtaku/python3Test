mylist1=[1,2,3,["a","b","c"]]
mylist2=[4,5,6]
mylist3=[7,8,9]
mylist=[mylist1,mylist2,mylist3]
print(mylist)
for  data  in mylist:
    print(data) #[1, 2, 3]

for data  in  mylist:
    for idata in data:
        print(idata)

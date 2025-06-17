def merge(l):
    if(len(l)>1):
        mid=len(l)//2
        l_list=l[:mid]
        r_list=l[mid:]
        merge(l_list)
        merge(r_list)
        i,j,k=0,0,0
        while(i<len(l_list) and j<len(r_list)):
            if(l_list[i]<r_list[j]):
                l[k]=l_list[i]
                i+=1
                k+=1
            else:
                l[k]=r_list[j]
                j+=1
                k+=1

        while(i<len(l_list)):
            l[k]=l_list[i]
            i+=1
            k+=1
        while(j<len(r_list)):
            l[k]=r_list[j]
            j+=1
            k+=1
            

num=int(input("Enter the number of items in a list : "))
l=[int(input()) for i in range(num)]
merge(l)
print(l)
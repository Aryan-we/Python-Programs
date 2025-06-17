def pivot_element_place(l,first,last):
    pivot=l[first]
    left=first+1
    right=last
    while True:
        while left<=right and l[left]<=pivot:
            left=left+1
        while left<=right and l[right]>=pivot:
            right=right-1
        if(left>right):
            break
        else:
            l[left],l[right]=l[right],l[left]
    l[first],l[right]=l[right],l[first]
    return right

    
def quick_sort(l,first,last):
    if first<last:
        p=pivot_element_place(l,first,last)
        quick_sort(l,first,p-1)
        quick_sort(l,p+1,last)
lis=[1,3,6,0,8,5]
a=len(lis)-1
quick_sort(lis,0,a)
print(lis)


        


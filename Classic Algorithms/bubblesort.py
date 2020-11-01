def bubble(lst):
    l = len(lst)
    for i in range(l):
        ## not adjacent elements according to wikipedia
        for j in range(l-1,i, -1):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

####### My method: 
 def bubble_merge(lst):
    #start with a non-zero number
    swap_count = 1
    #continue while swaps are done
    while swap_count !=0:
        count = 0
        #choose two adjacent elements iterating from 0 until 1 before last element
        for r in range(len(lst)-1):
            elm0,elm1 = lst[r], lst[r+1]        
            #swap them in order if necessary
            if elm1 < elm0:
                lst[r], lst[r+1] = elm1, elm0
                count +=1
        swap_count = count
    return lst



if __name__ == "__main__":
    print "please input integer number array"
    lst = []
    while 1:
        try:
            n = raw_input(">")
        except:
            print ""
            break
        lst.extend([int(i) for i in n.split()])
    print "origin: ", lst
    print "sorted: ", bubble(lst)
 

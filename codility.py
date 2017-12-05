



def sol(a):
    
    b = set(a)
    # print b

    finalset = set([])
    emptyset = set([])
    startday = 0

    for day in range(0, len(a)):
        finalset = set(a[day:])
        if(finalset ^ b == emptyset):
            # print finalset
            # print day
            if startday < day:
                startday = day
            # print finalset

    # print startday
    finalset = set([])

    endday = startday
    while endday!=len(a):

        finalset.add(a[endday])
        # print finalset
        if finalset==b:
            break
        
        endday = endday+1

    # print startday
    # print endday

    # return a[startday:endday+1]
    return endday-startday+1
     
    # for day in range(minday, len(a)):
    #     finalset = set(a[day:])
    #     if(finalset ^ b == emptyset):
    #         print finalset
    #         print day
    #         if minday < day:
    #             minday = day





if __name__ == '__main__':
    a = [6,3,3,3,3,3]
    print sol(a)

#to avoid excesive times in search algorythms, it splits the list until find the target or return false
#this fx will be used in an other functions
def binary_search(target, my_list):
    if isinstance (my_list,tuple):
        new_list=[]
        for i in my_list:
            new_list.append(i)
        
        new_list.sort()
        my_list=new_list
    
    elif isinstance (my_list,list):
        my_list.sort()
    
    start=0 #it's 0 because what matters to this variable is the quantity of elements and not their values
    end=len(my_list)
    middle=0
    #print("fx binary_search")
    #print("buscando ", target)
    #print("en >>>> ", list)
    while (start<=end):
        #print("start: ", start)
        #print("end: ", end)
        middle=(start + end) //2
        #print("valor de middle: ", middle)
        if middle == len(my_list):
    #        print("el valor de middle se fue a la garcha... no hay nada con que contrastar...")
            return False
            break
            
        if target == my_list[middle]:
    #        print(target, " es igual a ", list[middle])
            return True
        
        if target < my_list[middle]:
    #        print(target, " es menor a ", list[middle])
            end = middle-1
        else:
    #        print(target, " es mayor a ", list[middle])
            start = middle+1
    
    #print("el valor de fx binary_search() es FALSE")
    return False


"""-----------------------------is_number_in----------------"""
def is_number_in(number,list):
    #print("fx is_number_in")
    if binary_search(number,list) == True:
    #    print(number, " Hay cohincidencia!")
        return True
    else:
    #    print(number, " NO está")
        return False


"---------------------------number_in_dict_of_ranges-----------------------"
#there are 2 uses 

def number_in_dict_of_ranges(number, dict,total):
    for i in dict:
        for key in i:
            print(f'checkeando grupos de criterio {key}')
            for d in i[key]:
                #print(d) OK!
                
                if number>=d[0] and number<=d[1]: #d[0] is the range minimun and d[1] is the maximun; d[2]are the matches; d[3]percentage
                    print(f'{number} está entre {d[0]} y {d[1]}')
                    d[-2]+=1
                    #print(d[-2])
                    #print(i[key])
                    
                d[-1]=(d[-2]*100)/total
                print(f'Matches --> {d[-2]}')
                print(f'Total --> 100% = {total}') 
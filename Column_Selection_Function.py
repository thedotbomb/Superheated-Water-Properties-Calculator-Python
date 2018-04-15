#5/27/2017
#Column Selection Function


from Open_File_Function import*

def column_selection(temperture,move, file):

    
    #file = "first.txt" remove when any fail can be used 
    data = open_file(file) # open file function

    a = move
    b = a + 4 # data blocks are 4 values long : v , u , h , s 
    x=-1
    count = 0
    col_data = []
    items = []

    for element in data:
        col_data.append(element.split(' ')[0]) # locates temperture from text file
    
    for item in col_data: # converts list items from strings to float
        items.append(float(item))

    for temp in items: # locates temperture and respected values
        x+=1
        if items[x] < temperture and temperture < items[x+1]:
        
            #print(items[x], items[x+1], count)
        
            break
        else:
            count+= 1
        
            continue

    
    first = [data[count]] # selects water data for users temperture and inserts into a list
    second = [data[count+1]] # selects water data for users temperture and inserts into a list
    #print( first , second ) 
    new_list_one = []
    new_list_two = []

    for number in first:
        new_list_one.append(number.split(' '))

    for number in second:
        new_list_two.append(number.split(' '))
    
    new_list1 = new_list_one[0]
    new_list2 = new_list_two[0]
    data_list1 = []
    data_list2 = []

    for item in new_list1: # converts list items from strings to int
        data_list1.append(float(item))

    for item in new_list2:
        data_list2.append(float(item))

    Temp_lower = data_list1[0]
    Temp_higher = data_list2[0]
    
    
    return data_list1[a:b] , data_list2[a:b] , Temp_lower , Temp_higher

    ################# Both Pressure and Temperture are different from Table #########################################################
def column_selection_for_two(temperture,move , file , f):
    
    
        #file = "first.txt" remove when any file can be used 
        data = open_file(file) # open file function

        a = move
        b = a + 4 # data blocks are 4 values long : v , u , h , s 
        x=-1
        count = 0
        col_data = []
        items = []

        for element in data:
            col_data.append(element.split(' ')[0]) # locates temperture from text file
        
        for item in col_data: # converts list items from strings to int
            items.append(float(item))

        for temp in items: # locates temperture and respected values
            x+=1
            if items[x] < temperture and temperture < items[x+1]:
            
                #print(items[x], items[x+1], count)
            
                break
            else:
                count+= 1
            
                continue

        
        first = [data[count]] # selects water data for users temperture and inserts into a list
        second = [data[count+1]] # selects water data for users temperture and inserts into a list

        new_list_one = []
        new_list_two = []

        for number in first:
            new_list_one.append(number.split(' '))

        for number in second:
            new_list_two.append(number.split(' '))
        
        new_list1 = new_list_one[0]
        new_list2 = new_list_two[0]
        data_list1 = []
        data_list2 = []

        for item in new_list1: # converts list items from strings to int
            data_list1.append(float(item))

        for item in new_list2:
            data_list2.append(float(item))
        # Maybe # 
        
        
        
        ####################### second file reader 
        
        
        data = open_file(f) # open file function

        a = move
        b = a + 4 # data blocks are 4 values long : v , u , h , s 
        x=-1
        count = 0
        col_data_two = []
        items2 = []

        for element in data:
            col_data_two.append(element.split(' ')[0]) # locates temperture from text file
        
        for item in col_data_two: # converts list items from strings to int
            items2.append(float(item))
        
        for temp in items2: # locates temperture and respected values
            x+=1
            if items2[x] < temperture and temperture < items2[x+1]:
            
                #print(items2[x], items2[x+1], count)
            
                break
            else:
                count+= 1
            
                continue

        
        first_two = [data[count]] # selects water data for users temperture and inserts into a list
        second_two= [data[count+1]] # selects water data for users temperture and inserts into a list

        new_list_one2 = []
        new_list_two2 = []

        for number in first_two:
            new_list_one2.append(number.split(' '))

        for number in second_two:
            new_list_two2.append(number.split(' '))
        
        new_list1_two = new_list_one2[0]
        new_list2_two = new_list_two2[0]
        data_list1_two = []
        data_list2_two = []

        for item in new_list1_two: # converts list items from strings to int
            data_list1_two.append(float(item))

        for item in new_list2_two:
            data_list2_two.append(float(item))
        
        Temp_lower = data_list1[0]
        Temp_higher = data_list2[0]
        return Temp_lower, Temp_higher, data_list1[a:b] , data_list2[a:b], data_list1_two[1:5] , data_list2_two[1:5]

        




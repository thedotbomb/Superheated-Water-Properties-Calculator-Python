#5/27/2017
#Open File Function
#Column Selection Function 


def open_file(file):
    data = []
    text_file = open(file,"r") #opens file from selected temp and pressure
    data = text_file.readlines() 
    text_file.close()
    return data
    





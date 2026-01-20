''' File Handling '''

#  open a file 
#  Read the text in the file

f = open("myfile.txt" , "r")      # r : r is mode that for read data

t = f.read()     # for read 
print(t)
f.close()

# Write the data in file 
# For writing a data in file use w 

f = open("myfile.txt","w")
f.write("Writing a text in a file by write mode")
f.close()


# For append data in file
try:
    f = open("myfile.txt", "a")
    f.write("\n This is new is write in data by append mode ")
    f.close()
    f = open("myfile.txt","r")
    print(f.read())
    f.close()
except Exception as e:
    print("error :", e)

# Another way to open file that autometic close the file
try:
    with open("myfile.txt","a") as f:
        f.write("\nWith method autometic close the file after use")

    with open("myfile.txt", "r") as f:
        print(f.read())

except Exception as e:
    print("Error : ",e)


# There are many mode that we use so  we read or write file 
# Read and append 
with open("myfile.txt", "a+") as f:
    f.seek(0)
    t = f.read()
    print(t)  # Print old data 

    f.write("\nWe can use a+ for read and append ")
    
    t = f.read()
    print( " After write  the data ",t) 
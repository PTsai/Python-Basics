#
# Read and write files using the built-in Python file methods
# 

# Opening in write mode overrides whatever is written inside already
def write():
    #Open a file for writing(w) and create(+) it if it doesn't exist
    f = open("textfile.txt", "w+");
    #write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1));
    #close the file when done
    f.close();

# Keeps the data intact if there is any that already exists
def append():
    # Open the file for appending(a) text to the end, create(+) file if it doesn't exist
    f = open("textfile.txt", "a+");
    #write some lines of data to the file
    for i in range(10):
        f.write("This is line %d\r\n" % (i+1));
    #close the file when done
    f.close();
    
def read_all():
    #Open the file back up and read(r) the contents
    f = open("textfile.txt", "r");
    if f.mode == 'r': # check to make sure that the file was opened
        # use the read() function to read the entire file
        contents = f.read();
        print contents;
    f.close();
    
def read_lines():
    #Open the file back up and read(r) the contents
    f = open("textfile.txt", "r");
    if f.mode == 'r': # check to make sure that the file was opened
        # or, readlines reads the individual lines into a list
        fl = f.readlines();
        for x in fl:
            print x;
    f.close();
    
def main():  
    write();
    append();
    read_all();
    read_lines();
    
if __name__ == "__main__":
    main()

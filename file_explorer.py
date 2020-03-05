'''
file_explorer.py
Matthew Grunauer
3/4/2020

A program that reads and writes to text files
'''
# Function allows for writing and appending to files
def file_writer(filename, mode):
    userinp = ""
    print("Welcome to the file writer. Type 'close_file' when finished")
    try:
        with open(filename + ".txt", mode) as f:
            # Adds a newline character if file is opened in append mode
            if mode == 'a':
                f.write('\n')
            while (userinp.lower() != "close_file"):
                userinp = input("Write line here: ")
                if (userinp.lower() != "close_file"):
                    f.write(userinp + "\n")
            f.close()
    except:
        # If file opened in append mode and the filename doesn't exist
        print("You entered an invalid file path.")
    print("Thank you for using the file writer.")
    
# Function allows for reading files
def file_reader(filename):
    print("Welcome to the file reader. The file you selected will now be displayed.")
    try:
        with open(filename + ".txt", 'r') as f:
            print("------- File Contents Below -------\n") 
            print(f.read())
            print("\n------- End of File -------")
        f.close()
    except:
        # Error handling for user entering an invalid filename in read mode
        print("You entered an invalid file path.")
    print("Thank you for using the file reader.")
    
# Handles initialize execution of the program
def main():
    print("Thank you for using the file explorer.")
    print("NOTE: This program only works with .txt files!")
    userinp = ""
    # Checks to make sure the user entered a correct mode
    while(userinp not in ['r','w','a']):
        userinp = input("Please choose the mode you'd like to use: r, w, or a: ")
        if userinp == 'a' or userinp == 'w':
            # Calls the file_writer method if the user selects write or append mode
            filename = input("Enter the filename you'd like to create / edit: ")
            file_writer(filename, userinp.lower())
        elif userinp == 'r':
            # Calls the file_reader method if the use selects the read mode
            filename = input("Enter a filename you'd like to read: ")
            file_reader(filename)
    use_again = input("Would you like to use the file explorer again? (Y or N): ")
    
    # Checking for correct user inputs
    while (use_again.lower() not in ['y','n']):
        use_again = input("Please enter a correct input (Y or N): ")
    if use_again.lower() == 'y':
        # Calls the main function again if the user wants to open another file
        main()
    else:
        print("Goodbye!")

# Calls main function when the program is opened
if __name__ == '__main__':
    main()
 
                
    

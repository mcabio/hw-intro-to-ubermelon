# This code opens um-server-01.txt so process.py can read it
log_file = open("um-server-01.txt")

# This is a function that is supposed to generate sales reports
def generate_sales_reports(log_file):
    for line in log_file:    # This is a for loop that loops over each line of text from um-server-01.txt
        line = line.rstrip() # This remove trailing whitespaces (spaces, tabs, or newline 
                             # characters, depending on what's in between the parenthesis) 
                             # from the right end of a string. The term "right" 
                             # refers to the end of the string.
        day = line[0:3] # This code extracts a substring from the variable 'line' and assigns it to the variable
                        #  'day'. This is a slicing operation on the string. It specifies a 
                        # range of indices to extract from the string. The range [0:3] includes the characters at 
                        # indices 0, 1, and 2, but it excludes the character at index 3. In this exercise, 
                        # line[0] is the first word of the string.
        if day == "Mon": # This code is an if statement saying if day is "Tue", print the line. This filters
                         # all lines that start with Tue and prints it.
            print(line)


generate_sales_reports(log_file)

def matchingStrings(strings, queries):
    # We have to check all the values in the queries, so the 1st for loop ranges from 0 to len(queries)
    for i in range(0, len(queries)):

        # Reinitialize count value every time when the query value changes
        count = 0

        # we have to check 0th value of queries is in the strings array or not..
        # If so increment the count value by 1
        # NOTE : Here we are not going to use 'in' keyword to check the presence of element in an array... 
        #        Because here we wrote an algorithm to check the presence of item in an array using for loop...  
        for j in range(0, len(strings)):
            if queries[i] == strings[j]:
                count += 1
        # Use print function at end of the 2nd for loop to gen count value of i'th query in the strings
        print(count)


if __name__ == '__main__':
    # Store the strings and queries input in a list 
    strings = []
    queries = []

    # In Firstline, n1 asks user to provide number of inputs in strings array and store the value
    n1 = int(input())
    
    # For loop goes for n1 number of times and gets element from the user and append it to the string array
    for i in range(0, n1):
        val = input()
        strings.append(val)

    # n2 asks user to provide number of inputs in queries array and store the value
    n2 = int(input())

    # For loop goes for n2 number of times and gets element from the user and append it to the queries array
    for i in range(0, n2):
        val = input()
        queries.append(val)

    # Thats all, pass the argument into the function and call it!!
    matchingStrings(strings, queries)


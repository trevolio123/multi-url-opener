if __name__ == "__main__":

    import webbrowser
    import time

    # Starting URL
    url = 'https://www.google.com/search?q='
    test = "abcd"
    newTabDelay = 1.5
    totalNumberOfLines = 0

    # Open .csv with read permissions as f.
    # Read lines from f = data.
    with open("multi-url-opener - test CSV.csv", "r") as f:
        data = f.readlines()

        print("\n")
        print("Number of Tabs that will be opened ", len(data))
        print("Time delay between Tabs in seconds ", newTabDelay)
        print("\n")

        # assign (totalNumberOfLines) the total number of lines + 1.
        totalNumberOfLines = len(data) + 1

        # Print range (totalNumberOfLines). Values by line (#\n)
        for i in range(totalNumberOfLines):
            print(i)

        # create a list (listOfNumberOfLines) from range 0 to totalNumberOfLines. Example: [0, 1, 2, 3, 4, 5].
        listOfNumberOfLines = list(range(totalNumberOfLines))
        print(listOfNumberOfLines)

        # - - - -Replaced by above- - - - - - - - - - -
        # listOfNumberOfLines = []
        # for n in range (0, totalNumberOfLines):
        #     listOfNumberOfLines.append(n)
        # - - - - - - - - - - - - - - - - - - - - - - -

        # Test print list (listOfNumberOfLines) example: [0, 1, 2, 3, 4, 5].
        # print(listOfNumberOfLines)

    # Simplify determining answers.
    userYes = ['yes', 'y']
    userNo = ['no', 'n']

    # Prompt user for input.
    # Convert to lowercase.
    userInput = input("Start opening Tabs? (y/N) ").lower()

    # Check answers against sets.
    if userInput in userYes:
        for x in data:
            y = x.replace(',', '')
            z = y.replace('.', '')
            time.sleep(newTabDelay)
            webbrowser.open_new_tab(url + z)
            print(x.strip("\n"))

    elif userInput in userNo:
        print("\n")
        print("Tabs not opened by line")
        print("\n")
        for x in data:
            y = x.replace(' , ', ' ')
            z = y.replace(', ', ' ')
            aa = z.replace(',', ' ')
            ab = aa.replace(' . ', ' ')
            ac = ab.replace('. ', ' ')
            ad = ac.replace('.', ' ')
            ae = ad.replace('"', '')
            print(ae.strip("\n"))

    # Exit.
    else:
        print("\nInvalid input.\nExiting")
        exit = 1

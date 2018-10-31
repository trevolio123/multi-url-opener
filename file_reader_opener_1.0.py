if __name__ == "__main__":

    import webbrowser
    import time

    # Starting URL
    url = 'https://www.google.com/search?q='
    newTabDelay = 1.2

    # Open .csv with read permissions as f.
    # Read lines from f = data.
    with open("multi-url-opener - test CSV.csv", "r") as f:
        data = f.readlines()

        print("\n")
        print("Number of Tabs that will be opened ", len(data))
        print("Time delay between Tabs in seconds ", newTabDelay)
        print("\n")

    # Simplify determining answers.
    userYes = ['yes', 'y']
    userNo = ['no', 'n']

    # Prompt user for input.
    # Convert to lowercase.
    userInput = input("Start opening Tabs? (y/N) ").lower()

    # Check answers against sets.
    if userInput in userYes:
        webbrowser.open_new()
        for x in data:
            time.sleep(newTabDelay)
            webbrowser.open_new_tab(url + x)
            print(x.strip("\n"))

    # Exit.
    else:
        print("\nInvalid input.\nExiting")
        exit = 1

if __name__ == "__main__":

    import webbrowser

    url = 'https://www.google.com/search?q='

    def print_items(alist):
        """
        Iterate over alist and print all item.
        """
        for item in alist:
            webbrowser.open_new_tab(url + item)

    numbers = list(range(5, 82, 3))
    strings = ["python", "is", "fun", "!"]

    print("Iterate over lists and print items")
    print("")

    print_items(numbers)
    print_items(strings)

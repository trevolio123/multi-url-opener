if __name__ == "__main__":

    def print_items(alist):
        """
        Iterate over alist and print all item.
        """
        for item in alist:
            print(item)

    numbers = list(range(0, 100, 5))
    strings = ["1 to 100 by the count of 5"]

    print("Iterate over lists and print items")
    print("")

    print_items(numbers)
    print_items(strings)
    # print_items_bad(numbers)

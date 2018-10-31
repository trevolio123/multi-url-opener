if __name__ == "__main__":
    import webbrowser
    import time

    with open("URLS-Test-copy.txt") as f:
        for url in f:
            time.sleep(2)
            webbrowser.open_new_tab(url.strip())

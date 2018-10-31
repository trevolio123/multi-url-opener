import webbrowser

url = 'https://www.google.com/search?q='

# Open URL in new window, raising the window if possible.
webbrowser.open_new(url)

# Open URL in a new tab, if a browser window is already open.
webbrowser.open_new_tab(url + 'Samuel+Breeding%2C+MD+TN+vitals')
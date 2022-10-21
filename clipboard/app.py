# store multiple things on a clipboard
# then be able to paste all items
import sys
import clipboard
import json

# essentially is a filepath
SAVED_DATA = "clipboard.json"


def save_data(filepath, data):     # takes in filepath and data
    with open(filepath, "w") as f:  # writes data as new file variable named f
        json.dump(data, f)          # in a json format, creates the new file


def load_data(filepath):
    try:
        with open(filepath, "r") as f:  # opens the filepath and reads
            data = json.load(f)
            return data
    except:
        return {}


if len(sys.argv) == 2:  # ['app.py', 'test']
    command = sys.argv[1]  # ['test']
    data = load_data(SAVED_DATA)  # will read filepath and dictionary values

    if command == 'save':
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        # will then read filepath and write the new data
        save_data(SAVED_DATA, data)
        print('Data saved')
    elif command == 'load':
        key = input("enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print('Data copied to clipboard')
        else:
            print('Key does not exist')
    elif command == 'list':
        print(data)
    else:
        print('unknown command')
else:
    print('Please pass exactly one command')

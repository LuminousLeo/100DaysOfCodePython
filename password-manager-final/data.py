import json
from json import JSONDecodeError
from tkinter import messagebox


def save_data(website_input, email_username_input, password_input):
    """save_data(), is a function that saves the inputs in the website entry,
    email entry and password entry, in that order, into a json file. The content of that file will look
    something like this:
    {
        "something": {
            "email": "something@gmail.com",
            "password": "something"
        }
    }
    It also checks if one of the entries is left blank (warns the user that they left one
    of them blank) and also ask the user if they are sure they want to save the
    data inputted. Also create a data.json file if it does not exist already"""

    website_data = website_input.get()
    email_data = email_username_input.get()
    password_data = password_input.get()

    # a nested dict that saves the current user inputted website, email
    # and password combination
    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data,
        }
    }

    # check to see if user filled all entries
    if len(website_data) == 0 or len(email_data) == 0 or len(password_data) == 0:
        empty_warning = messagebox.showwarning(title='Empty Fields', message='Some field were left empty.')
    else:
        # message box that checks if user wants to save the information that they inputted
        save_checker = messagebox.askokcancel(title=website_data,
                                              message=f'These are the details entered: \nEmail: {email_data} \nPassword: {password_data} \nDo you want to save?')

        if save_checker:
            # try to read the data.json file
            try:
                with open('data.json', 'r') as data_file:
                    # read the data in the json file as a dict
                    json_data = json.load(data_file)
                    # update the json_data dict
                    json_data.update(new_data)
            except (FileNotFoundError, JSONDecodeError):
                # if the data.json file does not exist or empty
                # create the file and then write to it
                with open('data.json', 'w') as data_file:
                    json_data = new_data
            finally:
                # regardless of what happens, write data to the data.json file
                with open('data.json', 'w') as data_file:
                    # write the updated / new json_data dict into the data.json file
                    json.dump(json_data, data_file, indent=4)

            # reset user input
            website_input.delete(first=0, last=len(website_data))
            password_input.delete(first=0, last=len(password_data))


def find_password(website):
    """find_password(website) function takes in a string argument and checks if it
    is in a file called data.json. If the file does not exist then this function returns a 2,
    if the files does exist but the string provided by the user does not exist in the data.json file
    then it returns a 1, and finally, if the string provided by the user is in the data.json file then,
    this function, returns the entire data.json file as a dictionary (it's a nested one!!!)"""

    try:
        with open('data.json', 'r') as data_file:
            json_data = json.load(data_file)
            if website in json_data.keys():
                return json_data
            else:
                return 1
    except FileNotFoundError:
        return 2



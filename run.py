import gspread
from google.oauth2.service_account import Credentials
import textwrap
import os
from time import sleep

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("bedtime_adventures")

def get_welcome_message():
    """
    Get the welcome message and print it.
    """  
    story = SHEET.worksheet("welcome").get_all_values()
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("'\\n'", "\n")
    story_text = wrap_text(story_text)
    
    print(story_text)

def get_user_name1():
    """
    Get name input from user and will loop if not passed through 
    validator.
    """
    print("Who will be the heroes of tonight's adventure? We need two brave")
    print("and adventurous names for our characters. \n")
    
    while True:
        print("Please type in a name and press enter! \n")

        name1 = input("Enter the name of the first hero here:\n")
        name1 = name1.capitalize()

        if validate_names(name1):
            print(f"Hello {name1}! \n")
            break
        else:
            continue
    return name1

def get_user_name2():
    """
    Get second name input from user and will loop if not passed 
    through validator.
    """
    sleep(1)
    while True:
        name2 = input("Enter the name of the second hero here:\n")
        name2 = name2.capitalize()

        if validate_names(name2):
            print(f"Hello to you too, {name2}. Let's start our adventure! \n")
            break
    return name2

def validate_names(name):
    """
    Check for a name with 3 or more letters.
    Check for only letters.
    """
    try:
        if len(name) < 3:
            raise ValueError(
                f"We need a name with at least 3 letters from you and you gave us {len(name)}!"
            )
        for letter in name:
            if not letter.isalpha():
                raise ValueError(
                    "Looks like we can only accept letters from A to Z. Please make sure to only enter characters from the alphabet"
                )
    except ValueError as e:
        print(f"Oopsie daisy! {e}. Try again!\n")
        return False
    
    return True

def wrap_text(text):
    """
    Wrap text so lines will not be longer than 70 characters. 
    """
    wrapper = textwrap.TextWrapper(width=70, replace_whitespace=False)
    story_text = wrapper.fill(text=text)
    
    return story_text

def get_start_story(name1, name2):
    """
    Get the beginning of the story from google sheets and replace [Name1] and [Name2]
    with names from input. Add adventure choice for user to pick how the story continues.
    """  
    sleep(2)
    os.system('clear')

    story = SHEET.worksheet("story").get_all_values()
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    story_text = story_text.replace("'\\n'", "\n")
    story_text = wrap_text(story_text)
     
    print(story_text)

    while True: 
        choice1 = input("Insert X or Y here:\n")
        choice1 = choice1.capitalize()
        
        if validate_story_choice(choice1):
            print("Let's go! \n")
            break

    return choice1

def get_adventure_story(name1, name2, choice1):
    """
    Get adventure story X or Y depending on choice in start story.
    Add end choice for user to pick how the story ends. 
    """
    sleep(2)
    os.system('clear')

    if choice1 == "X":
        story = SHEET.worksheet("x").get_all_values()                
    elif choice1 == "Y":
        story = SHEET.worksheet("y").get_all_values()
     
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    story_text = story_text.replace("'\\n'", "\n")
    story_text = wrap_text(story_text)
    print(story_text)
    
    while True:        
        choice2 = input("Insert X or Y here:\n")
        choice2 = choice2.capitalize()

    
        if validate_story_choice(choice2):
            print("Let's go! \n")
            break

    return choice1 + choice2

def get_end_story(name1, name2, choice2):
    """
    Get adventure story XX, XY, YX or Y depending on choice in adventure story.
    Add ending. 
    """
    sleep(2)
    os.system('clear')

    if choice2 == "XX":
        story = SHEET.worksheet("xx").get_all_values()                
    elif choice2 == "XY":
        story = SHEET.worksheet("xy").get_all_values()
    elif choice2 == "YX":
        story = SHEET.worksheet("yx").get_all_values()                
    elif choice2 == "YY":
        story = SHEET.worksheet("yy").get_all_values()
     
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    story_text = story_text.replace("'\\n'", "\n")
    story_text = wrap_text(story_text)
    print(story_text)

def get_ending(name1, name2):
    """
    Get the end of the story from google sheets and replace [Name1] and [Name2]
    with names from input. 
    """  
    story = SHEET.worksheet("end").get_all_values()
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    story_text = story_text.replace("'\\n'", "\n")
    story_text = wrap_text(story_text)
       
    print(story_text)
    
def validate_story_choice(choice):
    """
    Validate that user enters either X or Y 
    """
    try:
        if choice != "X" and choice != "Y":
            raise ValueError(
                f"You need to pick either X or Y, you wrote {choice} !"
            )
    except ValueError as e:
        print(f"Oopsie daisy! {e}. Try again!\n")
        return False
    
    return True

def main():
    """
    Will run all everything 
    """
    get_welcome_message()
    name1 = get_user_name1()
    name2 = get_user_name2()
    choice1 = get_start_story(name1, name2)
    choice2 = get_adventure_story(name1, name2, choice1)
    get_end_story(name1, name2, choice2)
    get_ending(name1, name2)

print("Welcome to Bedtime Adventures! \n")

main()

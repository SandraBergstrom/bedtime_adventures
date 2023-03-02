import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("bedtime_adventures")


def get_user_name1():
    """
    Get name input from user.
    """
    print("Who will be the heroes of tonight's adventure? We need two brave and adventurous names for our characters. \n")
    
    while True:
        print("Please type in a name and press enter! \n")

        name1 = input("Enter the name of the first hero here: ")
        name1 = name1.capitalize()

        if validate_names(name1):
            print(f"Hello {name1}! \n")
            break
        else:
            continue
    return name1

def get_user_name2():
    """
    Get name input from user.
    """
    while True:
        name2 = input("Enter the name of the second hero here: ")
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

def get_start_story(name1, name2):
    """
    Get the beginning of the story from google sheets and replace [Name1] and [Name2]
    with names from input. Add adventure choice for user to pick how the story continues.
    """
       
    story = SHEET.worksheet("story").get_all_values()
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    story_text = story_text.replace("'\\n'", "\n")
       
    print(story_text)
    while True: 
        print("bug")
        choice1 = input("Insert X or Y here: ")
        choice1 = choice1.capitalize()
        
        if validate_story_choice(choice1):
            print("Let's go!")
            break

    return choice1


def get_adventure_story(name1, name2, choice1):
    """
    Get adventure story X or Y depending on choice in start story.
    Add end choice for user to pick how the story ends. 
    """
    
    if choice1 == "X":
        story = SHEET.worksheet("x").get_all_values()
        story_text = "\n".join([row[0] for row in story])
        story_text = story_text.replace("[Name1]", name1)
        story_text = story_text.replace("[Name2]", name2)
        story_text = story_text.replace("'\\n'", "\n")
        print(story_text)
                
    elif choice1 == "Y":
        story = SHEET.worksheet("y").get_all_values()
        story_text = "\n".join([row[0] for row in story])
        story_text = story_text.replace("[Name1]", name1)
        story_text = story_text.replace("[Name2]", name2)
        story_text = story_text.replace("'\\n'", "\n")
        print(story_text)
    
    while True: 
        print("bug2")        
        choice2 = input("Insert X or Y here: ")
        choice2 = choice2.capitalize()

    
        if validate_story_choice(choice2):
            print("Let's go!")
            break

    return choice1 + choice2
    
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
    name1 = get_user_name1()
    name2 = get_user_name2()
    choice1 = get_start_story(name1, name2)
    #print(choice1)
    choice2 = get_adventure_story(name1, name2, choice1)
    #print(choice2)


print("Welcome to Bedtime Adventures! \n")
print("Get ready to embark on exciting and imaginative journeys with your child. Our interactive stories are designed to encourage your child's creativity and critical thinking skills, while also providing an enjoyable and engaging experience.\n")
print("Let's dive in and explore new worlds together! \n")

main()

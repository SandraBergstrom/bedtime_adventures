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
        #validate_names(name1)

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
        #validate_names(name2_input)

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
    with names from input. 
    """
    story = SHEET.worksheet("story").get_all_values()
    story_text = "\n".join([row[0] for row in story])
    story_text = story_text.replace("[Name1]", name1)
    story_text = story_text.replace("[Name2]", name2)
    
    print(story_text)


# start story with names from input

# make a choice to continue story

# make another choice to continue story. 
 
# print end of story. 


def main():
    name1 = get_user_name1()
    name2 = get_user_name2()
    get_start_story(name1, name2)

    
print("Welcome to Bedtime Adventures! \n")
print("Get ready to embark on exciting and imaginative journeys with your child. Our interactive stories are designed to encourage your child's creativity and critical thinking skills, while also providing an enjoyable and engaging experience.\n")
print("Let's dive in and explore new worlds together! \n")

main()

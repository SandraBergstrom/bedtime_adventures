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


def get_user_names():
    """
    Get name input from user.
    """
    print("Who will be the heroes of tonight's adventure? We need two brave and adventurous names for our characters. \n")
    print("If you are reading to more than one child, we suggest using their names, but if you're reading to a single child, you can add your own name as the second hero.")
    print("Please type the two names, separated by a comma, and then press enter to get started with the story!")
    print("Example: Bubbles, Giggles")

    names = input("Enter names here: ")
    print(f"The names proivded is {names}")

    



# start story with names from input

# make a choice to continue story

# make another choice to continue story. 
 
# print end of story. 

#def main():
    

print("Welcome to Bedtime Adventures! \n")
print("Get ready to embark on exciting and imaginative journeys with your child. Our interactive stories are designed to encourage your child's creativity and critical thinking skills, while also providing an enjoyable and engaging experience.")
print("Let's dive in and explore new worlds together! \n")

get_user_names()


#main()
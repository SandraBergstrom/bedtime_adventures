# Bedtime Adventures
Story Adventure is an interactive story app for parents and caregivers to read to children between the ages of 3-6, our app offers a fun and engaging way to encourage children's creativity, critical thinking, and decision-making skills.

Bedtime Adventures is perfect for snuggling up with your little ones at bedtime and exploring exciting new worlds together. Give it a try on the link below and add a bit of variety to your bedtime stories. <br>

[Try it on this link](https://bedtime-adventures.herokuapp.com/)

![responsive image](/assets/images/responsive.png)

## Table of content

- [User Story](#user-story)
- [How to Use Bedtime Adventures](#how-to-use-bedtime-adventures)
- [Program Flow](#program-flow)
- [Data Model](#data-model)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Testing](#testing)
- [Bugs](#bugs)
- [Deployment](#deployment)
- [Credits](#credits)

## User story
As a busy parent who wants to encourage their child's creativity and imagination, I want an interactive story app that is easy to use and allows my child to make choices that guide the direction of the story. I also want the app to be flexible enough to allow me to read to one or multiple children and to personalize the story by using their names.

## How to use Bedtime Adventures
To get started, simply input the names of the children you'll be reading to. If you're reading to only one child, you can add your own name or the name of a pet as the second name.

Once you've inputted the names, the adventure begins! Follow along as the story unfolds, and let your children make choices that guide the direction of the story. You insert either Y or X depending on your choice and then press enter to continue. 

With multiple possible outcomes, every reading of Bedtime Adventures is a unique and exciting experience.

## Program flow
The flowchart represents the logic of the Bedtime Adventures program. The program starts by prompting the user to input two names and validates the input to ensure that each name is at least three letters long and contains only letters. <br>
![flowchart](/assets/images/flowchart.jpg)

If the input is valid, the program moves on to retrieve the first part of the adventure story from a Google Sheet using the Google Sheets API. The program replaces placeholders in the story text with the two names inputted by the user and presents the story to the user.

Next, the program prompts the user to make a choice between two options (X or Y) and validates the input to ensure that it is either X or Y. If the input is valid, the program retrieves the corresponding adventure story from the Google Sheet and presents it to the user.

This process repeats for the third part of the adventure story, where the user is prompted to make another choice between X or Y and the input is validated before retrieving and presenting the final part of the story.

Finally, the program displays the ending of the adventure story based on the user's choices throughout the three parts of the story. 

## Data model
The program uses the Google Sheets API to access a Google Sheet that contains the adventure story text. The program then replaces the placeholders for the user names and presents the story to the users. The program uses input() function to get the user's choices and a series of validation functions to ensure that the user inputs are valid.

## Technologies used
### Language
- Python 3: primary programming language for the project

### Programs used
- Lucidchart: an online diagramming tool, was used to create flowcharts for the project
- Gitpod: cloud-based IDE used for version control and writing code
- Git: version control system used for managing and tracking changes to the project's codebase
- GitHub: web-based hosting service used for version control and storing the project's code after being pushed from Gitpod
- Heroku: cloud platform used for deploying and hosting the project's web application

## Features
### Existing features
This adventure game program prompts users to enter two names and presents them with an adventure story that is divided into three parts. The program checks for errors, such as if the user enters less than three letters or anything other than letters. The error messages are displayed as shown below: <br>
![name_prompt](/assets/images/3letters.png)
![only_letters](/assets/images/onlyletters.png)

At the end of the first part of the story, users are presented with two choices, X or Y. <br>
![choices](/assets/images/xy.png)

Throughout the story, the names that the user entered at the beginning are used.  <br>
![user](/assets/images/user_name_in_story.png)

After the user has made a choice, a confirmation message to reassure that the child made a good choice, is displayed as shown below: <br>
![alt text](/assets/images/choice-confirmation.png)

The second part of the story corresponds to the user's choice. 
The third part is the ending of the story, which is also determined by the user's choices in the previous parts.

### Future ideas
- More options in story
- More story lines to follow so you begin with picking a story
- Possibility to name the teddy bear after the childs favorite teddy bear. 

## Testing:
### Name validation:
- 3 or more letters inserted - OK for both names
- Only letters - OK for both names
- Correct name input - OK for both names
- Numbers instead of letters - OK, gives correct error message
- 2 lettters inserted - OK, gives correct error message
- Name validation for second name input - OK

### First choice validation:
- X - OK
- Y - OK
- anything else inserted - OK, gives the correct error message

### Second choice validation:
- X - OK
- Y - OK
- anything else inserted - OK, gives the correct error message

### Third choice validation:
- X - OK
- Y - OK
- anything else inserted - OK, gives the correct error message

## Bugs:
### Known bugs:
- The textwrap is causing an unintenional line breakssince I added the possibility for line breaks with the parameter replace_whitespace=False. Thouhgt of creating line breaks in the source text instead but since we don´t know the lenght of the names that we get from input we can't control that the line breaks will end up where best suited this way. Not having line breaks at all is not an option since then we go back to long lines and breaking words instead of doing line breaks after/before words.

### Fixed bugs:
- Name validation for only letters will cause an error everytime because of the csv.
    - Created 2 input fields so one for each name instaed. Changed so it validates that there is 3 or more letters in each name. 
- At first choice when Y is pressed, error message: UnboundLocalError: local variable 'story' referenced before assignment.
    - I had mistakenly added an extra = when calling the SHEET. 

- When I have made my first choice it directly tells me again to make a choice even if I put in a valid value (X or Y)
    - by putting a print(bug) before the first input in get_start_story and a print(bug2) before the second input in get_adventure_story I realized that it jumped straight to the input field in get_adventure_story after I have put in a valid value, but went back to the input field in the get_start_story if I put in a not valid value. Turnes out that I mistakenly have removed the print(story_text) in get_adventure_story so everything else was working as it should. 

## Deployment
To deploy this project, follow these steps:

1. Fork and clone this repository to your local machine.
2. Create a new Heroku app.
3. In the Heroku dashboard, navigate to the app's settings and set the buildpacks to Python and NodeJS in that order.
4. Connect your Heroku app to the repository by linking it to your forked copy of the repository.
5. Click on the "Deploy" button in the Heroku dashboard.

After following these steps, your app should be successfully deployed to Heroku. 

## Credits

The development of this project was inspired by various online resources including tutorials from Simplilearn and Digital Ocean, as well as references from websites like W3Schools and GeeksforGeeks. Special credit goes to my mentor for their unwavering support, guidance and valuable feedback throughout the project.

- [Simplilearn](https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python) for their tutorial on list to string conversion in Python.
- [DigitalOcean](https://www.digitalocean.com/community/tutorials/python-remove-spaces-from-string) for their tutorial on removing spaces from a string in Python.
- [W3Schools](https://www.w3schools.com/python/ref_string_join.asp) for their tutorial on the `join()` method in Python.
- [Scaler](https://www.scaler.com/topics/capitalize-in-python/) for their tutorial on capitalizing strings in Python.
- [GeeksforGeeks](https://www.geeksforgeeks.org/textwrap-text-wrapping-filling-python/) for their tutorial on text wrapping and filling in Python.
- [Stack Overflow](https://stackoverflow.com/questions/1166317/python-textwrap-library-how-to-preserve-line-breaks), 
- [nkmk](https://note.nkmk.me/en/python-textwrap-wrap-fill-shorten/),  
- [Scaler](https://www.scaler.com/topics/how-to-clear-screen-in-python/) for their discussions on using the `textwrap` module and clearing the screen in Python.

### Story
The story is written with help from my daughter and ChatGPT.
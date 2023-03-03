# Bedtime Adventures
Story Adventure is an interactive story app for parents and caregivers to read to children between the ages of 3-6, our app offers a fun and engaging way to encourage children's creativity, critical thinking, and decision-making skills.

Bedtime Adventures is perfect for snuggling up with your little ones at bedtime and exploring exciting new worlds together. Give it a try on the link below and add a bit of variety to your bedtime stories.



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
- anything else inserted - 

## Bugs:
### Known bugs:
- Textwrap is causing unintentional line breaks since I added the possibility for line breaks with the parameter replace_whitespace=False. Thouhgt of creating line breaks in the source text instead but since we don´t know the lenght of the names that we get from input we can´t control that the line breaks will end up where best suited this way. Not having line breaks at all is not an option since then we go back to long lines and breaking words instead of doing line breaks after/before words. 
    - 

### Fixed bugs:
- Name validation for only letters will cause an error everytime because of the csv.
    - Created 2 input fields so one for each name instaed. Changed so it validates that there is 3 or more letters in each name. 
- At first choice when Y is pressed, error message: UnboundLocalError: local variable 'story' referenced before assignment.
    - I had mistakenly added an extra = when calling the SHEET. 

- When I have made my first choice it directly tells me again to make a choice even if I put in a valid value (X or Y)
    - by putting a print(bug) before the first input in get_start_story and a print(bug2) before the second input in get_adventure_story I realized that it jumped straight to the input field in get_adventure_story after I have put in a valid value, but went back to the input field in the get_start_story if I put in a not valid value. Turnes out that I mistakenly have removed the print(story_text) in get_adventure_story so everything else was working as it should. 

## Deployment


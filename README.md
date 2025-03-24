# Mixed-Apes
A place to share mix tapes of favourite playlists.

## Wireframe
![wireframe image of project](static/images/mixedapes-wireframe.png)

## Entity Relationship Diagram
![Entity Relationshio Diagram](staticfiles/images/mixedapes-ERD.webp)

## Project Board
[Kanban board][1]

## Learning Outcomes

**LO1 apply Agile Methodology in Planning and Designing a Django Web Framework** 

1. Front-End Design - to meet accessibilty guidelines and follow UX design principles. Semantic use of HTML. No Web Content Accessibility Guideline errors.
A user-friendly interface with consistent styles and adherence to wireframes/mockups.

2. Database

3. Agile Methodology

4. Cold Quality

5. Documentation

[🔼 Back to top](#mixed-apes)

---

**LO2 Develop and Implement a data model, application features and business logic to manage data in a real-world domain**

1. Database Development

2. CRUD functionality

3. User notifications

4. Form validation

[🔼 Back to top](#mixed-apes)

---

**LO3 Authorisation and Authentication Permissions**

1. Role-based Login and Registration

2. Reflect login state

3. Access control

[🔼 Back to top](#mixed-apes)

---

**LO4 Design, Create and Execute Manual or Automated tests**

1. Python tests procedures

2. Javascript test procedures

3. Testing documentation

[🔼 Back to top](#mixed-apes)

---

**LO5 Version control and Repository Hosting**

1. Version control with Git and GitHub

2. Secure code management

[🔼 Back to top](#mixed-apes)

---

**LO6 Deploy to cloud based platform**

1. Deploy to a Cloud-based platform

2. Document the deployment process

3. Ensure the security in deployment: No sensitive data, no Passwords and Debug set to False

[🔼 Back to top](#mixed-apes)

---

**LO7 Design and Implement custom data models**

1. Design and Implement a custom data model

[🔼 Back to top](#mixed-apes)

---

**LO8 Leverage AI tools to orchestrate the software Development Phase**

1. Use AI tools to assist in code creation

2. Use AI tools to assist in debugging code

3. Use AI tools to optimise code for performance and user experience.

4. Use AI tools to create automated tests

5. Reflect on AI's role in the development process and impact on workflow.

[🔼 Back to top](#mixed-apes)

---

## Manual Testing

### Feature Testing

|Page|Feature|Action|Effect|
|---|---|---|---|
|Homepage|Site Logo|Click|Redirects to home page from all pages|
|Homepage|Logged In User Display|Log in as existing user|Username appears in navbar|
|Homepage|Home link|Click|Redirects to home page from all pages|
|Homepage|Logout link|Click|Redirects to confirm signout page|
|Homepage|Confirm logout|Click 'ok'|Redirects to home page|
|Homepage|Login link|Click|Redirects to Sign In Page|
|Homepage|Register link|Click|Redirects to Sign Up Page|
|Homepage|All Loops Button|Click|All loops displayed on homepage|
|Homepage|My Loops Button|Not logged in|Button is disabled|
|Homepage|My Loops Button|Logged in : click|Only user's loops are displayed|
|Homepage|Edit Button|Logged out|Not visible|
|Homepage|Edit Button|Logged in : click|Visible - redirects to Loop Editor Page|
|Homepage|Loop row|Hover on row|Row is highlighted in green|
|Homepage|Loop row|Click|Redirects to Loop Detail Page for this selected loop|
|Homepage|Call-to-Action New Loop Button|Logged in : click|Redirects to Create New Loop Form|
|Homepage|Call-to-Action login button|Logged out : click|Redirects to Login Page|
|Homepage|Message on login|Login as user|Successful Signin message appears, clears after 3 seconds|
|Homepage|Message on logout|Logout|Successful signout message appears, clears after 3 seconds|
|Login Page|Social sign-in button|Click|Redirects to confirm social signin page|
|Login Page|Social sign-in continue button|Click|Redirects to Sign in with Google page|
|Login Page|Username validation|Enter incorrect username|Error message response - does not specify if username or password failed|
|Login Page|Password validation|Enter incorrect password|Error message response - does not specify if username or password failed|
|Login Page|Remember me button|Checkbox on|Close browser window and reopen - user still logged in|
|Login Page|Sign in button|Click|Redirects to home page, shows successful login message|
|Logout Confirm Page|Sign Out button|Click|Redirects to home page, user logged out|
|Register Page|Reroute to login page|Click link|Redirects to login page|
|Register Page|Username validation|Try using existing username|Error message appears - 'A user with that username already exists'|
|Register Page|email validation|Entered invalid email (without '@'|Error message - 'Please enter valid email address' and registration fails|
|Register Page|password1|Enter a short password|Error message - 'That password is too short'|
|Register Page|password2|Enter different password to password1 field|Error message - 'You must type the same password each time'|
|Register Page|Sign Up button|Entered valid form data|Redirects to home page - success message displayed|
|Loop Detail Page|Loop name display|No action|Loop name displays correctly|
|Loop Detail Page|Creator display|No action|Creator name displays correctly|
|Loop Detail Page|Track beat display|No action|All tracks present, all beats present|
|Loop Detail Page|Track beat animation|Click play button|Each beat highlighted in time on each track|
|Loop Detail Page|Site logo animation|Click play button|Logo grows on every 16th beat, and then slowly shrinks|
|Loop Detail Page|Play button|Click|Audio playback and animations begin|
|Loop Detail Page|Play button|Hover|Button appearance changes|
|Loop Detail Page|Pause button|Click|Audio playback and animations cease|
|Loop Detail Page|Play/pause button animation|Click to play|Button icon rotates quickly at beginning of every 16th beat|
|Loop Detail Page|Volume Input|Click on up and down buttons on input|Volume immediately goes up and down|
|Loop Detail Page|Share link display|No action|current url displayed|
|Loop Detail Page|Share link copy button|Click|link successfully copied to clipboard|
|Loop Detail Page|Rating button|Click|Redirects to rating page|
|Loop Detail Page|Rating button when logged out|No action|Not shown|
|Loop Editor Page|Loop name display|No action|Loop name displayed correctly|
|Loop Editor Page|Creator display|No action|Creator name displayed correctly|
|Loop Editor Page|Tempo control|Click arrow buttons to increase and decrease value|Tempo increases and decreases immediately as audio plays|
|Loop Editor Page|Instrument button|Click|Instrument modal shown, current instrument highlighted|
|Loop Editor Page|Instrument modal|Click on option|Sample plays once|
|Loop Editor Page|Instrument modal dismiss|Click outside modal or close button|Modal is hidden|
|Loop Editor Page|Instrument modal save button|Save clicked|Modal hidden, instrument updated|
|Loop Editor Page|Instrument change message|No action|Instrument changed message shown, fades after 3 sec|
|Loop Editor Page|Track volume control|Adjust slider|Volume of track changes in real time|
|Loop Editor Page|Beat toggle|Toggle on|Beat is now heard in playback, beat div highlighted|
|Loop Editor Page|Delete track button|Click|Confirm delete track modal shown|
|Loop Editor Page|Confirm delete track|Click|Track deleted and confirmation message shown|
|Loop Editor Page|Refuse delete track|Click|No change to loop|
|Loop Editor Page|Play button|Click|Audio playback and animations begin, icon changes to pause|
|Loop Editor Page|Pause button|Click|Audio playback and animations end, icon changes to play|
|Loop Editor Page|Loop volume control|Click on up and down arrow buttons|Overall playback volume increases and decreases|
|Loop Editor Page|Add new track button|Click|Instrument modal shown, after save clicked, new track appears with chosen instrument|
|Loop Editor Page|Delete Loop Button|Click|Confirm delete loop modal appears|
|Loop Editor Page|Delete Loop confirm|Click|Redirects to homepage, success message displayed, loop gone|
|Loop Editor Page|Delete loop reject|Click|No change to loop|
|New Loop Form|Name field|No action|Default name shown|
|New Loop Form|Tempo field|Click on arrow buttons|Tempo increases and decreases|
|New Loop Form|Let's get looping button|Click|Redirects to Loop Editor page, success message displayed|
|New Loop Creation Flow|Default set-up|Create new loop|New loop created with one track, default instrument selected, no beats yet selected|
|New Loop Creation Flow|Error|Enter name that already exists|Form displayed again with error shown|
|Loop Rating page|Previous comment|No action|Previous comments shown correctly|
|Loop Rating page|Previous rating|No action|Previous ratings shown correctly|
|Loop Rating page|Previous reviewer|No action|Previous reviewer shown correctly|
|Loop Rating page|User rating selector|Click on up and down arrows|Rating ranges from 0 to 5|
|Loop Rating page|User rating validation|Click to increase from 5 to 6|No change and red error highlight appears|
|Loop Rating page|User comment field|Fill with text|Text appears, comment max length observed|
|Loop Rating page|Submit button|Click|Redirects to home page, success message appears|

---

[1]: https://github.com/users/Olbotron/projects/7
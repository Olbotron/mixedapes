# Mixed-Apes
A place to share mix tapes of favourite playlists.

## Learning Outcomes

**LO1 apply Agile Methodology in Planning and Designing a Django Web Framework** 

1. Front-End Design

*I created the app based on an existing template for a site that I have a mock up site for online. I didn't spend a lot of time on wireframes as I wanted my site to look as closely as possible to the online mockup site on www.mixedapes.com.* 

## Wireframe
![wireframe image of project](static/images/mixedapes-wireframe.png)

*In the end, this would have been too much of an undertaking for this project. I believe the site meets the MVP for the main point of the site which is to create playlists and discover other's tastes. I believe the app could be continued after the assessment to improve the social app idea.*

*I used the [Lighthouse Accessibility checker][2] and acheived 100% for accessibility standards and in the 90s for the other criteria.*

2. Database

## Entity Relationship Diagram
![Entity Relationshio Diagram](staticfiles/images/mixedapes-ERD.webp)

3. Agile Methodology

*Here is a copy of the [Kanban board][1] project I created, though I did in fact use notes in my notebook and pen and paper more than this. This is an area I need to work on.*

4. Code Quality

*I used the online W3C code validator to check the code quality and received [no errors or warnings][3].*

5. Documentation

*I created daily lists of what I needed to do in my notebook, I knew that later I would need to update these into my repository's README.md which is this document.*

[🔼 Back to top](#mixed-apes)

---

**LO2 Develop and Implement a data model, application features and business logic to manage data in a real-world domain**

1. Database Development

*With the help of Co-Pilot I created the models based on the ERD I had designed.*

2. CRUD functionality

*The CRUD functionality of my app is that registered users can Create tapes, Read tapes of theirs and other users, Update their own tapes and Delete their own tapes.*

*When they have created a tape, or tapes, users can Create, Read, Update and Delete songs on that tape.*

3. User notifications

*The user gets notification by the tape being added to the list of tapes, songs get added to the list of songs. If a song is added that is recognised by the Spotify API I wrote then the song's album cover also appears next to the song title and artist.*

*If a user tries to delete an entire tape then a confirmation page appears to check that this is the desired action.*

4. Form validation

*I relied on Django "Crispy Forms" for form controls, as I wanted more control over the look of the controls. However my stylesheet somehow crashed at the 11th hour and I lost a lot of the presentation side of the form but I thought it was more important to keep the functionality.*

[🔼 Back to top](#mixed-apes)

---

**LO3 Authorisation and Authentication Permissions**

1. Role-based Login and Registration

*A user has to login in order to obtain CRUD permissions and still then the user can only manage their own tapes and songs.*

2. Reflect login state

*A registration and login link is shown in the top right of the page until logged in whereupon it changes to a greeting and the users name.*

3. Access control

*The database also has a super user account and under the sites admin area this super user can add or delete any songs or tapes, and can even manage users should the need arise.*

[🔼 Back to top](#mixed-apes)

---

**LO4 Design, Create and Execute Manual or Automated tests**

1. Python tests procedures

[Manual testing table below](#Manual-Testing)

2. Javascript test procedures

[Manual testing table below](#Manual-Testing)

3. Testing documentation

[Manual testing table below](#Manual-Testing)

[🔼 Back to top](#mixed-apes)

---

**LO5 Version control and Repository Hosting**

1. Version control with Git and GitHub

*Regular commits were made to this GitHub repository and to Heroku.*

2. Secure code management

*Any environment variables, passwords or other sensitive information was kept in file(s) which were labelled under gitignore*


[🔼 Back to top](#mixed-apes)

---

**LO6 Deploy to cloud based platform**

1. Deploy to a Cloud-based platform

*Deployed to Heroku using a PostGres SQL database and with sensitive information stored as environment variables.
This includes the database connection string and the SECRET KEY and TOKEN for the Spotify API.*

2. Document the deployment process

*Created a new application on Heroku, linked it to the relevant GitHub repository and added the Database connection string into
an an environment variable. Then deployed from the "main" branch. Took some time to build but once it had needed to do some testing
to check that everything was configured correctly. There were some errors at first which I needed to consult the logs for, but these turned out to be differences in the settings file for remote and local deployment. Once I had solved these errors the app was
deployed and I could carry out testing on it.*

3. Ensure the security in deployment: No sensitive data, no Passwords and Debug set to False

*No sensitive data was sent to the remote server and Debug was set to False on the live site.*

[🔼 Back to top](#mixed-apes)

---

**LO7 Design and Implement custom data models**

1. Design and Implement a custom data model

*I created a custom model of the mixtape and its related songs, This was based on the real-world model of a person create a mixtape for friends, family or potential partner. The idea is that the playlist would be themed and songs added to each specific tape for other people to give feedback on.*

*I created the Spotify API app that works with the name of the song and the name of the artist to return a copy of album cover that the song comes from. The album cover art URL is stored in the database*  

[🔼 Back to top](#mixed-apes)

---

**LO8 Leverage AI tools to orchestrate the software Development Phase**

1. Use AI tools to assist in code creation

*I used Co-Pilot to help with the initial creation of the apps, I then had to re-configure or amend code that was not relevant.*

2. Use AI tools to assist in debugging code

*Co-Pilot was very useful at times for pointing out errors in code, and even how to fix the code. However, sometimes it did repeat
the same information if the code it supplied the first time didn't solve an error. This made for asking more direct questions or pointing out that certain code snippets didn't work and to ask for a different solution.*

3. Use AI tools to optimise code for performance and user experience.

*I used the online W3C online checker to make sure the code was fully optimised.*

4. Use AI tools to create automated tests

*I used the lighthouse Developer tools on Chrome to check the site's compliance to accessibility and speed.*

5. Reflect on AI's role in the development process and impact on workflow.

*On the whole I found AI (Co-Pilot) to be helpful for debugging as most of the time it would find the broken code and give an example of how to fix it. However, at times I found myself to become to reliant on using Co-Pilot as it was supplying code that could have broken other areas of the site. I believe if you check the AI code through then you can save a lot of time debugging or searching online for an answer.*

[🔼 Back to top](#mixed-apes)

---

## Manual-Testing

### Feature Testing

|Page|Feature|Action|Effect|
|---|---|---|---|
|Header|Site Logo|Click|Redirects to home page from all pages|
|Header|Logged In User Display|Log in as existing user|Username appears in navbar|
|Header|Login link|Click|Redirects to Sign In Page|
|Header|Register link|Click|Redirects to Sign Up Page|
|Header|Logout link|Click|Redirects to home page with user signed out|
|Homepage|View Tapes Button|Click|Directs to tapes page|
|View Tapes Page|Lists all tapes|Click|Opens tape to show songs|
|Add Tape Page|"Add Tape" button|Click|Opens "Add Tape" Form|
|Edit Tape Page|"Edit Tape" button|Click|Opens "Edit Tape" Form|
|Delete Tape Page|"Delete Tape" button|Click|Opens "Delete Tape" Form|
|View Tape Page that you own|"Add song" button|Click|Opens "Add Song" Form|
|View Tape Page that you own|"Edit song" button|Click|Opens "Edit Song" Form|
|View Tape Page that you own|"Delete song" button|Click|Opens "Delete Songs" Form|
---

[1]: https://github.com/users/Olbotron/projects/7
[2]: https://github.com/Olbotron/mixedapes/blob/main/static/images/lighthouse-check.png
[3]: https://github.com/Olbotron/mixedapes/blob/main/static/images/HTML-checker.png
# academix

https://devpost.com/software/academix?ref_content=user-portfolio&ref_feature=in_progress

##Inspiration##
We were inspired to make our web app, Academix, due to the amounting stress that grades and GPA's have on us, and our future. We wanted to make a way for us to study and be better prepared for important tests, and make that big difference between a good and a great education. As students, we often find that there are very few concise and focused work assignments that benefit us, which is why we created Academix, the web app that uses AI to generate homework based on questions you are less familiar with than others. This app also allows for teacher to have less work strain, and make their lives that much better.

##What Academix does##
Academix is an AI based tutoring site that provides personalized homework from results of a test. Teachers can input what specific tags they want their students working on, and we generate a join code to an assessment that the students will later take. After the assessment, students will get personalized homework focused solely on their performance in the test, and what they were struggling with on the assessment. We have 2 dashboards: a teachers one and a students one, and the teachers dashboard is where tests can get created. On the students dashboard, students can join the teacher created test, or try out the sample test.

##How we built Academix##
We built Academix using the flask framework, HTML/CSS/JS, using JQuery, Ajax, and using databases from Heroku. We found a mathgenerator library and used specific methods to populate a list of tags, and based on the checkboxes of the tags that the teacher selects, we create a join code. After this, we made it so that students can enter the join code, and take the specific assessment that the teacher created. No two tests will be the same, as we generate questions randomly, using our AI. After the assessment, students get reviewed on what they got wrong vs. what they got right, and we generate homework problems based on their performance. For example, if a student gets a question wrong on multiplication, but gets another question right on basic algebra, the homework will be specifically targeted towards multiplication, rather than basic algebra (which they already know).

##Challenges we ran into##
Many parts of the code were a challenge, but the most time consuming would be finding the best library for our goals, troubleshooting failures in sending requests, and having to deal with long javascript sessions without a break and little to no experience. We were often very frustrated, and feeling like we wanted to quit, however we perservered due to the moral support we provided each other, and the passion we had for the idea.

##Accomplishments that we're proud of##
We are very proud of the UI/UX we managed to make, and of delivering a fully functional app that can be used at it's present state. We are also very proud of our ability to create a functional project with no experience in the libraries used, nor the framework we used.

##What we learned##
We learned how to navigate the flask framework, how to set up a database on Heroku, and we learned how to use certain AI libraries. We also greatly improved our skills in JQuery, Ajax, and HTML/CSS/JS.

##What's next for Academix##
We hope to expand Academix to cover more topics not only in math, but in subjects such as English and science. If enough people enjoy their experience on our app, we are commited to improving our app in whatever ways we can.

Built With
ajax
css
flask
html
javascript
jquery
mathgenerator
numpy
python

Try it out
 academix2-ai.herokuapp.com
 GitHub Repo

# AGS_Worksheet_Generator

A website for generating mathematics(AGS) related worksheets
See a live demo at http://ericyu.dev

## Installation

Use the package manager **pip** to install the following modules.

```bash
pip install flask
pip install SQLAlchemy
pip install WTForms==2.3.3
pip install Flask
pip install Flask-Bootstrap
pip install Flask-Login
pip install Flask-MySQL
pip install Flask-MySQLdb
pip install Flask-SQLAlchemy
pip install Flask-WTF
pip install latextable
pip install names
pip install num2words
pip install numpy
pip install sympy
pip install pandas
pip install scipy
pip install texttables
pip install texttable
```

## Usage

```python
import flask
import sqlalchemy
```

## Explanation


## Pages
    -Register (Register User and gathers info such as username, password, email. Has additional features like hyperlinks to register, login)
    -Login (Logs user into their account. Has additional features like hyperlinks to register, login, recover account)
    -Rate (Users of the website can rate the website using a combination of comments and stars)
    -Layout (Basic landscape of the website. Every page will use its template)
    -Links (Filled with helpful links and advice)
    -Settings (Need to get the update password working. Also try to get unhashed password)
    -Index ("Main" page of the website that the user will first encounter when they login)
    -Quote/Quoted (Needs to receive user input correctly, save it into database, then give proper feedback, in both graphical and visual)
    -Compare (Needs to portray data in the form of a graph in order for the user to compare their sleep data to others if they wish to)


## Databases
    -age (Structure: {id}, {age})
	-data (Structure: {id}, {day1}, {day2}, {day3}, {day4}, {day5}, {day6}, {day7})
	-datadump (Structure: {id}, {day1}, {day2}, {day3}, {day4}, {day5}, {day6}, {day7})
	-rate (Structure: {id}, {username}, {rating}, {comment})
	-users (Structure: {id}, {username}, {hash}, {email})
CREATE TABLE Users (
    uid integer AUTO_INCREMENT PRIMARY KEY,
    username text,
    hash text,
    email text,
    classrooms text,
    parent text,
    worksheets text,
    ADHD BIT
);

CREATE TABLE learningtarget_ags1 (
    Seed text,
    ccss text,
    section text,
    difficulty text,
    options text,
    description text,
    latex text
);

## Future Plans:
* improve navbar, sidebar
* add user login, register, settings
* add teacher, parent, classroom database set up
* TOGGLE HTML VERSION FOR LIVE ANSWERING (image of exmaple + mathjax/SVG plot) https://github.com/kisonecat/tikzjax
* ADHD font availability in PDF
* AUTO GRADE FEATURE
* Quizlet similar single online activities availiablity
    - lazy loading using async JS and creating
* Local compilation of latex PDF
* 
* 
* 
* 
* 
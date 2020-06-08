<p align="center">
  <a href="" rel="noopener">
    <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Get Tutored Online">
 </a>
</p>

<h3 align="center">Get Tutored Online</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Few lines describing your project.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

The Get Tutored Online project is an innovation that eveolved from several online tutoring platforms combning several purposes and helping to further improve the relationship between Parents and Tutors

## 🏁 Getting Started <a name = "getting_started"></a>

Clone or download this Repository and proceed to getting the requirements.

### Prerequisites

First up, install all the neccesary tools:

Steps:

1. First, make sure you have python3 installed on your computer use (python3 --version) to check
2. Next, we have to create a virtual environment, check if python package manager, 'pip' is installed.(pip --version) although you should have it by default if python3 is installed
3. Then, create a virtual environment with 'virtualenv'. If it is not installed use(pip install virtualenv)
4. Create a virtual environment in the base directory simply by: (virtualenv <\env_name>)
5. Next up, activate the virtual environment . use (source <\env_name>/bin/activate)
6. When the virtual environment has been activated upgrade pip with(pip install -U pip)
7. Next, up install the packages in the requirements.txt file using (pip install -r requirements.txt)

Now you have what we need to run the project:
Remember that you have to remain in the Virtual enviroment to run the server or use the Django services. To leave the virtual enviroment, simply type the (deactivate) command.

### Installing

Once you have setup the prerequisites, type (python manage.py runserver) in the base directory.
The server should be up and running. Then, in your browser, go to http://localhost:8000/tutors_api/tutor_list/ you should see the api view of the json objects of all tutors

## 🔧 Running the tests <a name = "tests"></a>

All Available API Endpoints:

1. http://localhost:8000/tutors_api/tutor_list/ (To display list of all tutors)
2. http://localhost:8000/tutors_api/become_tutor/ (To create a tutor account)
3. http://localhost:8000/tutors_api/tutor/${tutor.id}/ (To view the profile of a particular tutor)
4. http://localhost:8000/parents_api/become_parent/ (To create a parent account)
5. http://localhost:8000/parents_api/parent/${parent.id}/ (To view the profile of a particular parent)
6. http://localhost:8000/accounts/api/auth/register/ (To register a user)
7. http://localhost:8000/accounts/api/auth/login/ (To log a user in)
8. http://localhost:8000/accounts/api/auth/logout/ (To log a user out)
9. http://localhost:8000/accounts/api/auth/user/ (To know what user is logged in according to the token in the local storage).
   NOTE: trailing forward slash '/' must be added at the end of every url. E.g: '/auth/user/' and not '/auth/user'

### Break down into end to end tests

Details on each end point:

<p align="center">
User Actions API urls(Register, Login, Getting Logged in User, Logout):
</p>
<p>
We are going to be using TokenAuthentication with knox.
</p>
<p>

### A token will be generated at every successful registration, login, and getting logged in user.

### To Register a User: Send a POST request to 'accounts/api/auth/register/' containing the following:

1. Body; returning: first_name, last_name, username, email, and password in that order.
2. Headers: Content_Type: application/json.
Using Axios or Fetch, Axios is preferrable though.
A token will be generated, set the token as an item in local storage.
Create a function to get the token from localstorage and set it as an header with key 'Authorization': 'Token <\the sent token\>' whenever a token is needed to view protected views.
</p>
<p>

### To Get an authenticated user: Send GET request to 'accounts/api/auth/user/' with config:

1. Headers: Content_Type: application/json.

2. The function to get the token and set it as an header with key 'Authorization': 'Token <\the sent token\>' whenever a token is needed to view protected views.
   (We are doing this to check if there's an authenticated user when the website is visited)

The idea of this authentication is that when the user comes back to the website without logging out previously,
The user gets automatically logged in with the token stored in the localstorage.

</p>
<p>

### To Login a user: Send POST request to 'accounts/api/auth/login/' with config:

1. Body; returning: username, password

2. Headers: Content_Type: application/json.

Another token will be sent, set the token as an item to local storage.(if you are using redux, you can use the same state reducer for both login success and register success).

</p>
<p>

### To Get an authenticated user: Send GET request to 'accounts/api/auth/user/' with config:

Headers:

1. Content_Type: application/json.
2. The function to get the token set ia as an header with key'Authorization': 'Token <\the sent token>' whenever a token is needed for protected views.

(We are doing this when the user is not authenticated, the website should redirect to login page.)

The idea of this authentication is that when the user comes back to the website without logging out previously,
The user gets automatically logged in with the token stored in the localstorage.

</p>
<p>

### To Logout a user: Send POST request to 'accounts/api/auth/logout/' with headers:

1. body: null(this must be specified, else it won't work)

2. Headers: Content_Type: application/json, TokenAuthentication

</p>
<p align="center">
Tutor Account API urls(Become A Tutor, Get Tutors List):
</p>

<p>

### To get Tutor Lists:

Send GET Request to 'tutors_api/tutor_list/' (To display list of all tutors) with empty body and Content_Type

It doesn't need Token because, it is not a protected view.

### To Become A Tutor: Send POST request to 'tutors_api/become_tutor/' with config:

1. Body to return serializer fields, as seen in the output of tutor_list, excluding: id, info, and date_joined (they will be added automatically)Note: info will be the logged in user, so we need to pass token authentication.
2. Headers: Content_Type: applicaion/json, Token Authentication

### To view profile of tutor: Send GET request to 'tutors_api/tutor/\${tutor.id}/' with config:

1. Body: null
2. Headers: Content_Type: application/json, TokenAuthentication
   This view is also protected.

### To view update an tutor: Send POST request to 'tutors_api/tutor/\${tutor.id}/' with config:

1. Body: null
2. Headers: Content_Type: application/json, TokenAuthentication(only the user asociated the tutor account can update)
   This view is protected.

### To delete profile of an tutor: Send DELETE request to 'tutors_api/tutor/\${tutor.id}/' with config:

1. Body: null
2. Headers: Content_Type: application/json, TokenAuthentication
This view is very protected, and only by the user associated with tutor account can delete it.
</p>
<p>

### To view profile of parent: Send GET request to 'tutors_api/parent/\${parent.id}/' with config:

1. Body: null
2. Headers: Content_Type: application/json, TokenAuthentication
   This view is also protected. Only the owner can see it

### To update an parent: Send POST request to 'parents_api/parent/\${parent.id}/' with config:

1. Body: As used seen in the first view, sorry. exceptt id, tutor, address, state, photo doesn't show
2. Headers: Content_Type: application/json, TokenAuthentication(only the user asociated the parent account can update)
   This view is protected.

### To delete profile of a parent: Send DELETE request to 'parents_api/parent/\${parent.id}/' with config:

1. Body: null
2. Headers: Content_Type: application/json, TokenAuthentication
This view is very protected, and only by the user associated with parent account protected.
<p>

## 🎈 Reactification(Integrating React with Django) <a name="usage"></a>

The Current URL to load the react frontend is at the root '/'
So, after running the server like so:

```
python manage.py runserver

```

link to http://localhost:8000/

## ⛏️ Built Using <a name = "built_using"></a>

- [sqlite3] - Database
- [Django](https://djangoproject.com/) - Server Framework
- [ReactJs](https://vuejs.org/) - Web Framework
- [Python](https://nodejs.org/en/) - Server Environment

## ✍️ Authors <a name = "authors"></a>

[EthicalRalph](add your github link) -- FrontEnd Engineer
[Double_DOS](my github link) -- BackEnd Engineer & Initial Work
[Ediare_Stephen] -- Idea
[Dayo_Abdullahi] -- UIUX Designer

See also the list of [contributors](I'll the link) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References

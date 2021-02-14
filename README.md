# Movie Search App using OMDB API

## A Movie / TV Show Search Web Application using OMDB API powered by Django.

<b>Language Choice:</b> Python, JavaScript <br>
<b>Frameworks:</b> Django, Bootstrap <br>
<b>API:</b> OMDB


### Features

  - It has Django's User Authentication System where user can Sign up and login.
  - After successfully Signing in, user can able to see logout option.
  - Any user caThen, replace the API key in Service.pyn search any movie / tv show by using three criteria (type, title, release year)
  - It'll show details(title,genre,plot,poster, etc.) of the movie / tv show in a separate page.
  - Dashboard displays a list of movies.


### Instructions to run this app on local machine

First, Clone the repository and go to the project folder
```console
git clone https://github.com/rish4bhn/movieclue.git && cd movieclue
```

Install required dependencies of the project
 ```console
 pip install -r requirements.txt
```

After that, go to the "API Key" section of OMDB and generate a free API.
```console
http://www.omdbapi.com/apikey.aspx
```
Then, replace the generated API key in line 10 & 55 of services.py and line 85 of views.py with existing one.

Finally, start the application with this command and open it on local server (e.g. http://127.0.0.1:8000/)
```console
python manage.py runserver
```

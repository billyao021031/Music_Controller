# Party-room-music-controller
A shared music playing system built with **django** and **React**

## Setup Instructions

### Install Required Python Modules

```bash
pip install -r requirements.txt
```
### Start Web Server

To start the web server you need to run the following sequence of commands.

First cd into your desired tutorial folder (replace x with tutorial number).
```bash 
cd music_controller
```
Next run the django web server.
```bash
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
```

### [Install Node.js](https://nodejs.org/en/)

### Install Node Modules

First cd into the ```frontend``` folder.
```bash
cd frontend
```
Next install all dependicies.
```bash
npm i
```

### Compile the Front-End

Run the production compile script
```bash
npm run build
```
or for development:
```bash
npm run dev
```
### Requirement of Spotify
Please have your Spotify music open while you run in the local server. 
However, only Spotify Premium user can control the pause/play button due to the developer functionality limitation.

Ideally you should have the display as:

![sample](https://github.com/billyao021031/Music_Controller/blob/main/demo/screenshot.png)

## Design

Tools | Function | Details
------|--------|---------
**Python Django** | Backend system | Implement basic web framework, handle URL routing and database
**Django Rest Framework** | Rest-API | Fetch calls from frontend and perform standard CRUD operations, also connects to Spotify API
**React JS** | Frontend system | Builds browsable user interface (UI) 

Each piece of functionality is implemented as a seperate *django* app.

App Name | Purpose
---------|---------
**api** | Handle standard CRUD operation on database models, such as the keeping track of the room and people in the room
**spotify** | Allows our app to connect to Spotify API and access the music
**frontend** | Implements the multiple webpage design with React

### Spotify API

To access the Spotify API, we use the following steps.
1. Application requests for authorization; the user logs in and authorizes access
2. Application requests refresh and access tokens; Spotify returns access and refresh tokens
3. Use the access token to access the Spotify Web API; Spotify returns requested data such as music library. This also gives control to user to pause/skip songs
4. Access token expires every 1 hour. So we need to requests a refreshed access token; Spotify returns a new access token to your app

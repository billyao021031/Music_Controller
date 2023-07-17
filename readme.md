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
**frontend** | Implements the webpage design with React
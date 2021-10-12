# hobbyapp
> This is a hobby project tracking app that allows users to plan and manage their miniature wargamming projects. 
> The live app can be found [_here_](https://hobby-project-tracker.herokuapp.com). 

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)


## General Information
I undertook this project to fullfill three objectives: 
- A) Use all the knowledge I gained during my Back End Engineering course on Codecademy. 
- B) Pick up a new technology for the front end. 
- C) Build something I would use. 

I am an avid miniature collector and painter with many projects on the go. I therefore decided to build a hobby project tracking app that would let me keep track of these projects. My Codecademy course mainly focused on backend and my previous projects had not been very visually appealing. I therefore decided to learn and use React for the front end to expand my horizons and improve the visuals of the app. Finally, I wanted to be able to share this app with other hobbiests and therefore planned to implement user authentications and sessions. 

This repository contains the full functional app. However, the React based front end is hashed and therefore not very readable. To see the development version of the front end, go to [_this_](https://github.com/thomas-dunlop/hobby-project-manager-front-end) repository. 


## Technologies Used
Front End
- React - version 17.0.2
- Font Awesome - version 1.2.36
- Bootstrap - version 3.0
- react-select - version 5.0.0 

Back End
- Django - version 3.2.7
- Postgres - version 13.0
- Gunicorn - version 20.1.0
- Whitenoise - version 5.3.0


## Features
The app allows users to:
- Keep track of projects, including their name, description, related notes, and their associated hobby recipes.
- Keep track of hobby recipes, including their name, description, and required materials (paint, glue, etc), and steps. The user can link hobby recipes to multiple projects (for instance if you use the same true metal armor recipe across multipe armies).
- Keep track of material including their name, part number, re-order link, etc. The user can link materials to multiple hobby recipes. The user can also keep track of various lots of materials.

The app also includes the following features: 
- Account creation and user authentication so users can only access their own projects. 
- Sessions and cookies to keep users logged in. 


## Usage
The live app can be found [_here_](https://hobby-project-tracker.herokuapp.com). 


## Project Status
Project is: _in progress_ 

The app is fully functional, but there are several features still on the to-do list (see the [Room for Improvement](#room-for-improvement) section). 


## Room for Improvement
Go to the Issues tab and look for enhancement labels to see planned improvements.  

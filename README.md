# Item Catalog Project
This is project #2 required for Udacity Full-Stack Web Developer Nanodegree program.
It is a web application uses Flask framework to retrieve the data from the database
in order to show different categories in a catalog along with their items.

## Technologies used
1. Python
2. Flask
3. sqlalchemy
4. HTML
5. CSS 

## Prerequisites 
1. Download and install [Vagrant](https://www.vagrantup.com/downloads.html)
2. Download and install [Virtual Machine](https://www.virtualbox.org/wiki/Downloads) 
3. Download or clone this project and put it inot the **vagrant** directory.

###### Run the following commands from the terminal in the folder where your vagrant is installed in:
1. `vagrant up`
2. `vagrant ssh`
3. `cd /vagrant` to navigate to vagrant directory
4. `python database_setup.py`
5. `python seeder.py`
6. `python logAnalysis_p1.py`

## Using Google Login
To get the Google login:
1. Go to [Google Dev Console] (https://console.developers.google.com/)
2. Login with your Google account
3. Click on APIs & Services
4. Select Credentials 
5. Click on Create credentials > OAuth client ID
6. Select Wep application
7. On Authorized JavaScipt origins add [http://localhost:5000] (http://localhost:5000)
8. On Authorized redirect URIs add [http://localhost:5000/login] (http://localhost:5000/login) & [http://localhost:5000/gconnect] (http://localhost:5000/gconnect)
9. Click on Create
10. Click on DOWNLOAD JSON
11. Rename the downlaoded file to client_secrets.json
12. Put this file inside the item catalog folder
13. Copy the Client ID and paste it into the `data-clientid` in login.html 



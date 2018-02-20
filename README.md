# Hiring-Project-britecore
this repo is a frontend and a backend API for britecore company 

# backend 
 - used django to build the api
 - REST API with two end point 
 - 1 ``` api/risk/company_id/risk_id/```
 - so when you hit the api like this link  http://127.0.0.1:8000/api/risk/1/1/ you got 
```
{"result": [{"date": {"data": "2018-02-13", "type": "date", "id": 4, "options": []}, "season": {"data": "spring", "type": "enum", "id": 4, "options": ["spring", "summer", "winter"]}, "age": {"data": 20.0, "type": "number", "id": 1, "options": []}, "place": {"data": "egypt", "type": "text", "id": 1, "options": []}}, {"date": {"data": "2018-02-13", "type": "date", "id": 8, "options": []}, "season": {"data": "winter", "type": "enum", "id": 7, "options": ["spring", "summer", "winter"]}, "age": {"data": 60.0, "type": "number", "id": 2, "options": []}, "place": {"data": "mansoura", "type": "text", "id": 3, "options": []}}, {"date": {"data": "2018-02-23", "type": "date", "id": 5, "options": []}, "season": {"data": "winter", "type": "enum", "id": 5, "options": ["spring", "summer", "winter"]}, "age": {"data": 1.0, "type": "number", "id": 4, "options": []}, "place": {"data": "23", "type": "text", "id": 6, "options": []}}, {"date": {"data": "2018-02-13", "type": "date", "id": 7, "options": []}, "season": {"data": "winter", "type": "enum", "id": 6, "options": ["spring", "summer", "winter"]}, "age": {"data": 7.0, "type": "number", "id": 5, "options": []}, "place": {"data": "cairo", "type": "text", "id": 7, "options": []}}]}
````
 
 - 2  ``` api/risk/company_id/risk_id/``` so when you hit the api like this link  http://127.0.0.1:8000/api/risk/1/1/ you got
 - 
 ```
 {"result": [{"riskName": "Earthquake", "data": [{"date": {"data": "2018-02-13", "type": "date", "id": 4, "options": []}, "season": {"data": "spring", "type": "enum", "id": 4, "options": ["spring", "summer", "winter"]}, "age": {"data": 20.0, "type": "number", "id": 1, "options": []}, "place": {"data": "egypt", "type": "text", "id": 1, "options": []}}, {"date": {"data": "2018-02-13", "type": "date", "id": 8, "options": []}, "season": {"data": "winter", "type": "enum", "id": 7, "options": ["spring", "summer", "winter"]}, "age": {"data": 60.0, "type": "number", "id": 2, "options": []}, "place": {"data": "mansoura", "type": "text", "id": 3, "options": []}}, {"date": {"data": "2018-02-23", "type": "date", "id": 5, "options": []}, "season": {"data": "winter", "type": "enum", "id": 5, "options": ["spring", "summer", "winter"]}, "age": {"data": 1.0, "type": "number", "id": 4, "options": []}, "place": {"data": "23", "type": "text", "id": 6, "options": []}}, {"date": {"data": "2018-02-13", "type": "date", "id": 7, "options": []}, "season": {"data": "winter", "type": "enum", "id": 6, "options": ["spring", "summer", "winter"]}, "age": {"data": 7.0, "type": "number", "id": 5, "options": []}, "place": {"data": "cairo", "type": "text", "id": 7, "options": []}}], "id": 1}, {"riskName": "Material damage", "data": [{"date": {"data": "2018-02-12", "type": "date", "id": 1, "options": []}, "material age": {"data": "old", "type": "enum", "id": 1, "options": ["old", "new", "medium"]}}, {"date": {"data": "2018-01-01", "type": "date", "id": 2, "options": []}, "material age": {"data": "new", "type": "enum", "id": 2, "options": ["old", "new", "medium"]}}, {"date": {"data": "2018-01-01", "type": "date", "id": 3, "options": []}, "material age": {"data": "medium", "type": "enum", "id": 3, "options": ["old", "new", "medium"]}}], "id": 2}]}
 ```
## How to run
- just clone this repo then 
- install python 2.7
- insatll pip 
- change terminal to be at Backend/
below the comand you should use
```
cd Backend
pip install -r requirment.txt
python manage.py runserver
```
- now supposed to see http server running on local host @ port 8000

# frontend 
- using angular 5.2.4 to build a single page application 
- single page application build with angular 5 to submit the data 
- and view the saved data by hitting the API
## How to run
 - Verify that you are running at least node 6.9.x and npm 3.x.x by running node -v and npm -v in a terminal/console window. Older versions produce errors, but newer versions are fine.
 -
 ```
 npm install -g @angular/cli
 ```
 - cd to the frontend directory then 
 
 ```$ npm install        ## to install npm models 
 
    $ ng serve           ## now you running on port 4200
 ```
 
## the image is entity relationship diagram

# DEPLOYMENT FrontEnd 
- while you are done with any edit and you want to go production 
- make sure you are in the project directory then run build production 
```
ng build --prod --build-optimizer
```
- now you have the production file at dist directory 
- install nginx or apache i prefere using linux so this is instruction https://www.digitalocean.com/community/tutorials/how-to-install-nginx-on-ubuntu-16-04
- configure your server  like at this linke 
- make sure that root dir is pointing to the ```dist/``` directory or you just Copy thes files at root dir


## this is the link of the instace where i hosted the app 
http://23.236.49.20


# courier-service-api

## Project Installation

* First of all created a virtual environment and then install all the necessary packages:

```
pip install django djangorestframework djangorestframework-simplejwt
```

* Now created the project file: 
```
django-admin startproject courier-service-rest
```
Inside of the project folder create an app called package_tracker:

```
py manage.py startapp package_tracker 
```

now move on to the settings.py file and add app and rest apis: [settings.py](https://prnt.sc/XdvsFz_AhrUU).

* I have also added a .gitignore file to ignore our venv or virtual environment file for further necessity.


# How To Run Courier-Service-Rest Project SUCCESSFULLY

* First clone the project from our github repo 
```
git clone https://github.com/Mohammad-Rakibuzzaman/courier-service-api.git
```

* Now create a virtual environment:
```
python3 -m venv venv
```

* Lets activate our virtual environment which is "venv" in this case by following command:

```
# On Linux we use : `source env/bin/activate`

# On Windows use:  `venv\Scripts\activate`
```
* After activating our venv environment lets install all the requirements.txt file. so that we won't need to install manually our essential packages and libraries:
```
pip install -r requirements.txt
```

now lets move on to our "courier_service_rest" folder:
```
cd courier_service_rest
```

now run => ``` py manage.py runserver ```



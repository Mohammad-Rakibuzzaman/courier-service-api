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

now create a new superuser by using command"
```
py manage.py createsuperuser
```
* after creating a new super user now its time to create our table in the database to store our all the created courier packages list according to its status:
```
py manage.py makemigrations
py manage.py migrate

```

now run => ``` py manage.py runserver ```




## Now our service is running locally to our machine.

Now Lets check all the API's we have created all are working nicely or not.

* To check those api's we need to install [POSTMAN](https://www.postman.com/downloads/)

* Now open the postman software and create a new tab to test all the apis. 

### Checking all the essential API's

* Let's ensure that we can read our all stored file we have added from admin panel.

now paste this using "GET" method in postman search bar and send this api request using:

```
http://127.0.0.1:8000/api/packages/
```

we can now see our data without authentication. Here is an screenshot of my POSTMAN api test for READ data. 

[READ DATA USING POSTMAN WITHOUT AUTHENTICATION](https://prnt.sc/ViwCXQRhIKO4)

You will notice a 200 Ok sign and all the data below to the body section. This indicates that our apis is working and we can check our data without having authentication.

* Now its time to check our authentication system with create, update and soft-delete apis working or not.

1. First hit the url using "POST" method because for authenctication system we have used simple jwt authenticate system.:

```
http://127.0.0.1:8000/api/token/

```
2. Body(JSON):
```
{
    "username": "your-username",
    "password": "your-password"
}

```
Now you will have our "refresh" and "access" keys. Just copy the "ACCESS" key.

3. Then Create one of our new package. so that we would understand our "CREATE" is working perfectly or not.

* now create a post request to : 

```
http://127.0.0.1:8000/api/packages/

```

Now add in Headers: 

```
Authorization: Bearer YOUR_ACCESS_TOKEN

```

Now write in Body section below json to store our package:


```
{
    "product_description": "BODY SPRAY",
    "tracking_number": "TRACK-1001",
    "sender": "KAKAROT",
    "receiver": "Boby",
    "address": "123 Main Street, USA",
    "status": "pending"
}

```

Now if you see 201 created message then Create method API is working successfully. here is my [created package](https://prnt.sc/Yv0fj_avppwy)


* Update Package (Requires Authentication)

Create a PUT request to:

```
http://127.0.0.1:8000/api/packages/6/

```

keep your authorization stay inside of Authorization or Headers you have created so far. 

Now just change the Body(JSON) file so that we can update our package.

After requesting with the "PUT" request we can see our data has been changed to new one. Here is my screenshot of [PUT REQUEST SUCCESSFUL](https://prnt.sc/pDCypPqROqIo)


* Finally Soft Delete Package (Requires Authentication)

1. Create a DELETE request to:
```
http://127.0.0.1:8000/api/packages/7/
```

Also keep authorization open for this process also. Becuase we have set authorization system for our UPDATE, CREATE and SOFT-DELETE api request in our views.py file.

2. If we send delete request then our pacakges should soft-delete from our database which means the record is not actually deleted from the database its just marked as deleted using the deleted_at field. With soft delete, we can recover the data by simply setting deleted_at = None.

Finally we should see 204 No Content and we have deleted our database id number 6 product successfully. HERE is the screenshot attached: [DELETE API TEST](https://prnt.sc/gET_Q15JZZJF)
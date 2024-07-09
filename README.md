# ConnectLinkAPI
## Follow below steps to setup the project 

Open your favorite Terminal and run these commands.

First open the directry where you want to clone the project
```sh
cd "path/to/your/dierectry"
```
1. Clone the Repository and go to the Repository

```sh
git clone <repository_url>
cd <repository_name>
```
2. Create and Activate a Virtual Environment

```sh
# Create a virtual environment
python -m venv env

# Activate the virtual environment
# On Windows
env\Scripts\activate

# On macOS and Linux
source env/bin/activate
```

3. Install Project Dependencies
```sh
pip install -r requirements.txt
```

4. Create Migrations
```sh
python manage.py makemigrations
```

5. Apply Migrations
```sh
python manage.py migrate
```

6. Create a superuser
```sh
python manage.py createsuperuser
```

7. Start the Development Server
```sh
python manage.py runserver
```
> Note: keep the server on to test in local.

8. Check on the browser.

```sh
127.0.0.1:8000
```

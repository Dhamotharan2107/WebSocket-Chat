Open your project folder in VS Code.
Open the terminal by clicking on Terminal

In the terminal, run the following command:

python3 -m venv venv

This will create a virtual environment named venv in your project directory.

Activate the Virtual Environment
To activate the virtual environment, run the appropriate command depending on your operating system:

macOS/Linux:

source venv/bin/activate

Windows:

venv\Scripts\activate

Set up Django and Django Channels
First, install Django and Django Channels:

pip install django channels

Configure Channels Layers (Redis)
For WebSocket communication between clients, you need to configure a channel layer. Install Redis and set up the channels-redis package:

pip install channels_redis

Database Migrations
After defining the models, you need to create and apply migrations:

python manage.py makemigrations

python manage.py migrate

Set up Daphne 

pip install daphne

without this its show Error or Connection failed


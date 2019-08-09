# Star Social

Social media forum with multiple groups of members that can communicate with each other.

## Running the Project Locally

First, clone the repository to your local machine:

```bash
git clone https://github.com/tigekid/star-social.git
```

Setup the virtual environment:

```bash
python3 -m venv venv
```

Start virtual environment:
```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Create the database:

```bash
python manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The project will be available at **127.0.0.1:8000**.

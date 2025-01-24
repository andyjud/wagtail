#### Commands
##### Set up:
git clone https://github.com/andyjud/django-starter.git . && rm -rf .git <br/>
python3 -m venv venv <br/>
source venv/bin/activate <br/>
pip install --upgrade pip <br/>
pip install -r requirements.txt <br/>
python manage.py migrate <br/>
python manage.py createsuperuser <br/>
python manage.py runserver <br/>
ctrl + c <br/>

##### Create blog app:
pip install wagtail <br/>
python manage.py startapp a_blog <br/>
python manage.py makemigrations<br/>
python manage.py migrate <br/>
python manage.py runserver <br/>
<br/>

##### Indexing:
python manage.py update_index<br/>
<br/>

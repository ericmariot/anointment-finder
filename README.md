# anointment-finder
This is a web project used to easily find anointments for the game [Path of Exile (PoE)](https://www.pathofexile.com/);

In the game we have a mechanic called Blight, where we can drop oils, they are used to anoint amulets or Blight unique items, making so that the item grant the Passive skill.

It's running live at https://anointment-finder.fly.dev/


# how to run this app locally
Firstly clone this repository; <br>
Then at the folder, run '`pip install -r requirements.txt`'; <br>
And start the project '`python manage.py runserver`';<br>
It should be up at `localhost:8000`


# how to run the web crawler
Run '`python scripts/list_oils_and_anoints.py`';

# how to update the database
Use the custom management command to update the database with the json. <br>
Run '`python manage.py createanointments path/to/all_anointments.json`'
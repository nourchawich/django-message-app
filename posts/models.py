from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, unique=True)
    text = models.TextField()
    author = models.CharField(max_length=20, db_index=True)

# Todo (Mentee): After creating the campaigns app
#  1. Create models.py where you define your `Campaign` model. You need to think which field it requires.
#  2. Make migrations by running `python manage.py makemigrations campaigns`
#  3. Apply migrations by running `python manage.py migrate`

# You can always delete everything and start fresh by deleting `db.sqlite3` file and applying the migration again
# In case you created wrong migrations, delete the newly created migration file under `app_name/migrations` directory

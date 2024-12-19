import datetime
from flask_login import UserMixin
from mongoengine import DateTimeField
from . import db, login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.objects(id=user_id).first()

class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True, min_length=8, max_length=20)
    email = db.EmailField(unique=True, required=True)
    password = db.StringField(required=True)

class Budget(db.Document):
    user = db.ReferenceField(User, required=True)
    category = db.StringField(required=True)
    amount = db.FloatField(required=True)
    start_date = db.DateField(required=True)
    end_date = db.DateField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now)

    def remaining_budget(self):
        expenses = Expense.objects(category=self.category, user=self.user)
        total_expenses = sum(expense.amount for expense in expenses)
        return self.amount - total_expenses

class Expense(db.Document):
    user = db.ReferenceField(User, required=True)
    category = db.StringField(required=True)
    amount = db.FloatField(required=True)
    description = db.StringField(max_length=200)
    date = db.DateField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now)
import unittest
from flask_testing import TestCase
from flask import abort, url_for
import os
from application import app, db
from application.models import User, Workout

class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='mysql+pymysql://' +os.getenv('MYSQL_USER')+ ':' +os.getenv('MYSQL_PASS')+ '@' +os.getenv('MYSQL_IP')+ '/llewthenics')
        return app

    def setUp(self):

        db.session.commit()
        db.drop_all()
        db.create_all()

        admin = User(first_name="admin", last_name="admin", email="admin@admin.com", password="admin2019")

        employee = User(first_name="test", last_name="test", email="test@user.com", password="test2019")

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):

        db.session.remove()
        db.drop_all()

class multipletests(TestBase):

    def test_about_page(self):
        response = self.client.get(url_for('about'))
        self.assertEqual(response.status_code, 200)

    def test_log_page(self):
        response = self.client.get(url_for('log'))
        self.assertEqual(response.status_code, 302)
    
    def test_account_page(self):
        response = self.client.get(url_for('account'))
        self.assertEqual(response.status_code, 302)
    
    def test_login_page(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)
    
    def test_register_page(self):
        response = self.client.get(url_for('register'))
        self.assertEqual(response.status_code, 200)
    
    def test_create_page(self):
        response = self.client.get(url_for('create'))
        self.assertEqual(response.status_code, 302)
    
    def test_logout_page(self):
        response = self.client.get(url_for('logout'))
        self.assertEqual(response.status_code, 302)

    """
    ------------------------------
    """

    def test_log_model(self):
        log = Workout(workout="test", sets=3, reps=10, body_part="test", user_id=1)

        db.session.add(log)
        db.session.commit()

        self.assertEqual(Workout.query.count(), 1)
        
    def test_log_model(self):
        log = Workout(workout="test", sets=3, reps=10, body_part="test", user_id=1)

        db.session.add(log)
        db.session.commit()

        self.assertEqual(Workout.query.count(), 1)

    def test_user_model(self):
        user = User(first_name="test", last_name="test", email="test@test.com", password="test")

        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.count(), 3)

    def test_user_model(self):
        user = User(first_name="test", last_name="test", email="test@test.com", password="test")

        db.session.add(user)
        db.session.commit()

        self.assertEqual(User.query.count(), 3)

    """
    ----------------------------
    """

    def test_log_view(self):

        target_url = url_for('log')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_account_view(self):

        target_url = url_for('account')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_create_view(self):

        target_url = url_for('create')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_logout_view(self):

        target_url = url_for('logout')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_update_account_view(self):

        target_url = url_for('update_account')
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    
    

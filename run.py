#!/usr/bin/env python3.6
from user import User
from credentials import Credential
import string, random
from rich import print 
from rich.console import Console
from rich.table import Table
from rich.progress import track
from time import sleep


def create_user(username,password,email):
  '''
  Function to create a new user
  '''
  new_user = User(username,password,email)
  return new_user

def save_user(user):
    '''
    save the user
    '''
    return user.save_user()

def del_user(user):
  '''
  Function to delete a user
  '''
  user.delete_user()

def find_user(username):
  '''
  Function that finds a user by username and returns the user
  '''
  return User.find_by_username(username)

def check_existing_user(username):
  '''
  Function that check if user exists with username and returns a Boolean
  '''
  return User.user_exists(username)

def display_users():
  '''
  Function that returns all the saved users
  '''
  return User.display_user()
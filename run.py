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

  def create_credential(account_name,username,password):
  '''
  Function to create a new credential
  '''
  new_credential = Credential(account_name,username,password)
  return new_credential

def save_credential(credential):
  '''
  Function to save credential
  '''
  credential.save_credential()

def del_credential(credential):
  '''
  Function to delete a credential
  '''
  credential.delete_credential()

def find_credential(account_name):
  '''
  Function that finds a credential by account_name and returns the credential
  '''
  return Credential.find_credential_by_account_name(account_name)

def check_existing_credential(account_name):
  '''
  Function that check if credential exists with account_name and returns a Boolean
  '''
  return Credential.credential_exist(account_name)

def display_credentials():
  '''
  Function that returns all the saved credentials
  '''
  return Credential.display_credentials()
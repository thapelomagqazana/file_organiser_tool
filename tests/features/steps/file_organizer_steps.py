from behave import given, when, then
import sys
import os

# Adjust the Python path to include the 'src' directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from src.file_organizer import FileOrganizer

import shutil
import pytest

@given('the source directory is "{source}"')
def set_source(context, source):
    context.source = source


@given('the destination directory in "{destination}"')
def set_destination(context, destination):
    context.destination = destination


@given('the rules are defined in {rules}')
def set_rules(context, rules):
    context.rules = rules


@when('the usr runs the File Organizer')
def run_file_organizer(context):
    file_organizer = FileOrganizer()
    context.output = file_organizer.organize_files()


@then('files shoul be organized successfully')
def check_output(context):
    assert "File organization completed successfully." in context.output

@then('an error should be displayed')
def check_error_output(context):
    assert "Error organizing files" in context.output
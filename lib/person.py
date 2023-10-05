#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    # Initialize the Person class with a name and job
    def __init__(self, name, job):
        self._name = self._validate_name(name)
        self._job = self._validate_job(job)

    # Define a property for the "name" attribute
    @property
    def name(self):
        return self._name

    # Setter method for "name" attribute with validation
    @name.setter
    def name(self, value):
        self._name = self._validate_name(value)

    # Define a property for the "job" attribute
    @property
    def job(self):
        return self._job

    # Setter method for "job" attribute with validation using APPROVED_JOBS
    @job.setter
    def job(self, value):
        self._job = self._validate_job(value)

    # Helper method to validate and format the name
    def _validate_name(self, value):
        if isinstance(value, str) and len(value) < 25:
            return value.title()
        else:
            print("Name must be a string under 25 characters.")
            return ""

    # Helper method to validate the job using APPROVED_JOBS
    def _validate_job(self, value):
        if value in APPROVED_JOBS:
            return value
        else:
            print("Job must be in the list of approved jobs.")

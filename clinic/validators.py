
# class InvalidRecordError(Exception):
# def clean_name(raw_name: str) -> str:
#     # TODO 1: strip spaces, apply .title(), handle the empty case
#     name = raw_name.strip().title()
#     if not name:
#         raise InvalidRecordError("name is missing")

#     return name


# def parse_age(raw_age: str) -> int:
#     # TODO 2
#     ## raise NotImplementedError
#     try:
#         age = int(raw_age)
#     except ValueError:
#         raise InvalidRecordError("age is not a number")

#     if age < 1 or age > 120:
#         raise InvalidRecordError("age must be between 1 and 120")

#     return age

# def parse_fee(raw_fee: str) -> float:
    
#     fee_text = raw_fee.replace(",", "").strip()

#     if not fee_text:
#         raise InvalidRecordError("consultation fee is missing")

#     try:
#         fee = float(fee_text)
#     except ValueError:
#         raise InvalidRecordError("consultation fee is not a number")

#     if fee < 0:
#         raise InvalidRecordError("consultation fee cannot be negative")

#     return fee

# def clean_department(raw_dept: str, default: str = "General") -> str:

#     department = raw_dept.strip()

#     if not department:
#         return default

#     return department.title()

# """Pure validation and cleaning functions for raw patient data.

# YOUR JOB: complete every function marked TODO.
# Each takes messy text in and returns a clean value out — or raises
# InvalidRecordError explaining what is wrong.
# (Module 4 functions + Module 9 exceptions, working together.)
# """


# class InvalidRecordError(Exception):
#     """Raised when a patient row cannot be repaired safely."""
#     # Nothing to add — inheriting from Exception is enough (Module 9).


# def clean_name(raw_name: str) -> str:
#     """Return the name stripped of extra spaces, in Title Case.

#     >>> clean_name("  priya sharma ")
#     'Priya Sharma'

#     Raise InvalidRecordError("name is missing") if the result is empty.
#     """
#     name = raw_name.strip().title()

#     if not name:
#         raise InvalidRecordError("name is missing")

#     return name
#     # TODO 1: strip spaces, apply .title(), handle the empty case
#     raise NotImplementedError


# try:
#     age = int(raw_age.strip())
# except ValueError:
#     raise InvalidRecordError("age must be a number")

# if age < 1 or age > 120:
#     raise InvalidRecordError("age must be between 1 and 120")

# return age
#     # TODO 2
# raise NotImplementedError


# value = raw_fee.strip().replace(",", "")

# if not value:
#     raise InvalidRecordError("consultation fee is missing")

# try:
#     fee = float(value)
# except ValueError:
#     raise InvalidRecordError("consultation fee must be a number")

# if fee < 0:
#     raise InvalidRecordError("consultation fee cannot be negative")

# return fee
#     # TODO 3
# raise NotImplementedError


# department = raw_dept.strip()

# if not department:
#     return default

# return department.title()
#     # TODO 4 (two lines are enough)
# raise NotImplementedError



"""Pure validation and cleaning functions for raw patient data.

YOUR JOB: complete every function marked TODO.
Each takes messy text in and returns a clean value out — or raises
InvalidRecordError explaining what is wrong.
(Module 4 functions + Module 9 exceptions, working together.)
"""


class InvalidRecordError(Exception):
    """Raised when a patient row cannot be repaired safely."""
    pass


def clean_name(raw_name: str) -> str:
    """Return the name stripped of extra spaces, in Title Case."""
    name = raw_name.strip().title()

    if not name:
        raise InvalidRecordError("name is missing")

    return name


def clean_age(raw_age: str) -> int:
    """Return a valid patient age between 1 and 120."""
    try:
        age = int(raw_age.strip())
    except ValueError:
        raise InvalidRecordError("age must be a number")

    if age < 1 or age > 120:
        raise InvalidRecordError("age must be between 1 and 120")

    return age


def clean_fee(raw_fee: str) -> float:
    """Return a valid non-negative consultation fee."""
    value = raw_fee.strip().replace(",", "")

    if not value:
        raise InvalidRecordError("consultation fee is missing")

    try:
        fee = float(value)
    except ValueError:
        raise InvalidRecordError("consultation fee must be a number")

    if fee < 0:
        raise InvalidRecordError("consultation fee cannot be negative")

    return fee


def clean_department(raw_dept: str, default: str = "General") -> str:
    """Return a cleaned department name, or the default if missing."""
    department = raw_dept.strip()

    if not department:
        return default

    return department.title()
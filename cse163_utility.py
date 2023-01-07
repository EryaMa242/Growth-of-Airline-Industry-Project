"""
Hunter Schafer, Lyra Ma, Wendy Huang, Gloria Hu
CSE 163

A file that contains some CSE 163 specific helper functions.
We include parse, check_approx_equals, and assert_equals which
is created by professor.
We also create convert_money, load_data_and_clean to facilitate
our code
"""

import math

import numpy as np
import pandas as pd

TOLERANCE = 0.001


def convert_money(data):
    '''
    since all the numbers in the column is str, we need to convert it to int
    '''
    data = data.replace('.00', '')
    data = data.replace(',', '')
    data = data.replace('$', '')
    return float(data)


def parse(file_name):
    """
    Reads the CSV with the given file_name and returns it as a list of
    dictionaries. The list will have a dictionary for each row, and each
    dictionary will have a key for each column.
    """
    df = pd.read_csv(file_name)
    df['Sum of RPM (Revenue Passenger Mile)'] = df[
        'Sum of RPM (Revenue Passenger Mile)'].apply(convert_money)
    return df.to_dict('records')


def load_data_and_clean(file_name):
    '''
    This function is used to facilitate salary_of_aircrafts. to filter
    dataframe and convert str to int
    '''
    df = pd.read_csv(file_name)
    df['Salary'] = df['Salaries and Wages (000)'].apply(convert_money)
    data = df[['Aircraft Type', 'Salary', 'Year']]
    return data


def check_approx_equals(expected, received):
    """
    Checks received against expected, and returns whether or
    not they match (True if they do, False otherwise).
    If the argument is a float, will do an approximate check.
    If the arugment is a data structure will do an approximate check
    on all of its contents.
    """
    try:
        if type(expected) == dict:
            # first check that keys match, then check that the
            # values approximately match
            return expected.keys() == received.keys() and \
                all([check_approx_equals(expected[k], received[k])
                    for k in expected.keys()])
        elif type(expected) == list or type(expected) == set:
            # Checks both lists/sets contain the same values
            return len(expected) == len(received) and \
                all([check_approx_equals(v1, v2)
                    for v1, v2 in zip(expected, received)])
        elif type(expected) == float:
            return math.isclose(expected, received, abs_tol=TOLERANCE)
        elif type(expected) == np.ndarray:
            return np.allclose(expected, received, abs_tol=TOLERANCE,
                               equal_nan=True)
        elif type(expected) == pd.DataFrame:
            try:
                pd.testing.assert_frame_equal(expected, received,
                                              atol=TOLERANCE)
                return True
            except AssertionError:
                return False
        elif type(expected) == pd.Series:
            try:
                pd.testing.assert_series_equal(expected, received,
                                               atol=TOLERANCE)
                return True
            except AssertionError:
                return False
        else:
            return expected == received
    except Exception as e:
        print(f"EXCEPTION: Raised when checking check_approx_equals {e}")
        return False


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If the argument is a float, will do an approximate
    check. If the arugment is a data structure will do an approximate check
    on all of its contents.
    """

    if type(expected) == str:
        # Make sure strings have explicit quotes around them
        err_msg = f'Failed: Expected "{expected}", but received "{received}"'
    elif type(expected) in [np.ndarray, pd.Series, pd.DataFrame]:
        # Want to make multi-line output for data structures
        err_msg = f'Failed: Expected\n{expected}\n\nbut received\n{received}'
    else:
        err_msg = f'Failed: Expected {expected}, but received {received}'

    assert check_approx_equals(expected, received), err_msg

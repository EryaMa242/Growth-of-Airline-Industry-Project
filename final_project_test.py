'''
Lyra Ma, Wendy Huang, Gloria Hu
CSE 163

This file tests the function in project_code to make sure these functions
are correct.
'''
import project_code
import pandas as pd
from cse163_utility import assert_equals, parse, load_data_and_clean
from cse163_utility import convert_money


def test_rpm_year_sum(data, dataframe):
    '''
    Use parsed dataset to get the same result as rpm_year_sum,
    then use assert_equals to test whether
    we got the same answer
    '''
    dic = {}
    for i in range(len(data)):
        if data[i]["Year"] in dic:
            dic[data[i]['Year']] += data[i][
                'Sum of RPM (Revenue Passenger Mile)']
        else:
            rpm_values = 0
            rpm_values += data[i]['Sum of RPM (Revenue Passenger Mile)']
            dic[data[i]['Year']] = rpm_values
    assert_equals(dic, project_code.rpm_year_sum(dataframe))


def test_rpm_year_highest(dataframe):
    '''
    By looking at the rpm_year_sum, I found out the year
    with highest rpm is 2015
    '''
    assert_equals(2015, project_code.rpm_year_highest(dataframe))


def test_rpm_year_lowest(dataframe):
    '''
    By looking at the rpm_year_sum, I found out the year with
    lowest rpm is 2003
    '''
    assert_equals(2003, project_code.rpm_year_lowest(dataframe))


def main():
    dataframe1 = pd.read_csv('datasets/operation_summary.csv')
    dataframe1['Sum of RPM (Revenue Passenger Mile)'] = dataframe1[
        'Sum of RPM (Revenue Passenger Mile)'].apply(convert_money)
    data = parse('datasets/operation_summary.csv')
    dataframe2 = load_data_and_clean('datasets/UA_aircraft_spending.csv')
    dataframe3 = pd.read_csv("datasets/UA_salary_benefits.csv")
    project_code.plt_rpm_trend_each_operation(dataframe1)
    project_code.plt_rpm_year_sum(dataframe1)
    project_code.salary_of_aircrafts(dataframe2)
    project_code. salary_employee_position(dataframe3)
    test_rpm_year_highest(dataframe1)
    test_rpm_year_lowest(dataframe1)
    test_rpm_year_sum(data, dataframe1)


if __name__ == '__main__':
    main()

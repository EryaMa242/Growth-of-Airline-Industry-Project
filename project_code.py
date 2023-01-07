'''
Lyra Ma, Wendy Huang, Gloria Hu
CSE 163

This file answer the following questions. What is the trend of revenue
passengermiles of each type of operation?  Which year has the highest RPM?
Which yearhas the lowest RPM? What is the trend of overall RPM? Which type
of aircraft(small narrowbodies, large narrowbodies, widebodies, fleet)
has the highestsalary for a pilot over the years? Is there any correlation
between salaries and each type of employee position
'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings


def plt_rpm_trend_each_operation(dataframe):
    '''
    find the trend of rpm of each operation using seaborn, then put the result
    in a graph
    '''
    sns.relplot(
        x='Year',
        y='Sum of RPM (Revenue Passenger Mile)',
        data=dataframe, kind='line', hue='Type of Operations')
    plt.xlabel('Year')
    plt.xticks(rotation=45)
    plt.ylabel('RPM')
    plt.title("Trend of RPM of each operation")
    plt.savefig('plot_RPM_trend_operations.png', bbox_inches='tight')


def rpm_year_sum(dataframe):
    '''
    find the sum of RPM (Revenue Passenger Mile) of all operations in each
    year, then put it in a dictionary
    '''
    return dataframe.groupby('Year')[
        'Sum of RPM (Revenue Passenger Mile)'].sum().to_dict()


def plt_rpm_year_sum(dataframe):
    '''
    plot rpm_year_sum with seaborn to visualize the relationship of year and
    sum of RPM
    '''
    df = pd.DataFrame(
        rpm_year_sum(dataframe).items(), columns=[
            'Year', 'Sum of RPM (Revenue Passenger Mile)'])
    sns.relplot(x='Year',
                y='Sum of RPM (Revenue Passenger Mile)', data=df, kind='line')
    plt.xlabel('Year')
    plt.xticks(rotation=45)
    plt.ylabel('RPM')
    plt.title("Trend of RPM")
    plt.savefig('plot_RPM_trend.png', bbox_inches='tight')


def rpm_year_highest(dataframe):
    '''
    Find the year with highest rpm
    '''
    return max(rpm_year_sum(dataframe), key=rpm_year_sum(dataframe).get)


def rpm_year_lowest(dataframe):
    '''
    Find the year with lowest rpm
    '''
    return min(rpm_year_sum(dataframe), key=rpm_year_sum(dataframe).get)


def salary_of_aircrafts(dataframe):
    '''
    this function will shows the Salary Of different Aircrafts Change Over Year
    we want to know whether there is a relationship between type of aircrafts
    and the salary of their pilots
    '''
    plt.figure(figsize=(15, 6))
    sns.lineplot(data=dataframe, x="Year", y="Salary", hue='Aircraft Type')
    plt.title("Salary Of Aircrafts Change Over Year")
    plt.savefig('Salary change over year.jpg')


def salary_employee_position(df):
    '''
    This function will answer the question Is there any correlation between
    salaries and each type of employee position? we plot multiple graph to
    find the relationship between salaries and each type of employee position
    '''
    warnings.filterwarnings('ignore')
    # We need to convert String salary to float so that
    # we can operate to it as a float, not as a string
    for columnName in df.iloc[:, 1:7]:
        df[columnName] = df[
            columnName].str.replace(',', '').str.replace('$', '').astype(float)
    # Show converted values just received
    df.iloc[:, 1:7]
    # Generate and sort relevant columns
    cols = []
    for columnName in df.iloc[:, 1:8]:
        cols.append(columnName)
    # Since we only need data til the end of the 'Average Salary'
    df = df.iloc[:21]
    # Use Droppna to get rid of 'All Others' because there is no value inside
    df.drop("All Others", axis=1, inplace=True)
    df.drop("Salary & Benefits Category", axis=1, inplace=True)
    df
    # Plot per employee(per type) per year
    for columnName in df:
        # Use 'reg' to draw regression lines to illustrate the
        # corelation better
        sns.jointplot("Year", columnName, data=df, kind='reg')
    # For a better comparison in paired plots
    sns.pairplot(df, size=2.5)
    plt.savefig('Salary of different jobs.jpg')

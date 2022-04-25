import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # assume initial values for variables
    city='city'
    month='month'
    day='day'
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while city not in CITY_DATA.keys():
        city=input('Please select the cityfrom this list [chicago, new york city, washington]: ').lower()
    # TO DO: get user input for month (all, january, february, ... , june)
    months=['all', 'january', 'feburary', 'march', 'april', 'may', 'june' ]
    while month not in months:
        month=input('Please select the month between{}: '.format(months)).lower()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days=['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        day=input('Please select the day of the week: ').lower()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df=pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

        # filter by day of week if applicable
        
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    
    Returns:
         dispaly the most common month, the most common day of week, and the most common start hour
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    common_month = months[common_month-1]
    print('The most common month is {}'.format(common_month).title())

    # TO DO: display the most common day of week
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    common_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is {}'.format(common_day_of_week))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common start hour is {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_start_station = df['Start Station'].mode()[0]
    print('Most commonly used start station is {}'.format(commonly_start_station))
    

    # TO DO: display most commonly used end station
    commonly_end_station = df['End Station'].mode()[0]
    print('Most commonly used end station is {}'.format(commonly_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    df['Combination Stations'] = df['Start Station'] + ' and ' + df['End Station']
    most_frequent_combination = df['Combination Stations'].mode()[0]
    print('Most frequent combination of start station and end station trip is {}'.format(most_frequent_combination))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trip_duration = df['Trip Duration'].dropna(axis = 0).sum()
    print('The total travel time is {}'.format(total_trip_duration))


    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].dropna(axis = 0).mean()
    print('The average travel time is {}'.format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    try:
        counts_types = df['User Type'].value_counts()
        print('counts of Subscriber users is {} and counts of Customer users is {}'.format( counts_types['Subscriber'],counts_types['Customer']))
    except:
        print("There is no User Type data.")
    # TO DO: Display counts of gender
    try:
        counts_gender = df['Gender'].dropna(axis = 0).value_counts()
        print('counts of Male gender is {} and counts of Female gender is {}'.format(counts_gender['Male'],counts_gender['Female']))
    except:
        print("There is no Gender data.")
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_birthyear = df['Birth Year'].dropna(axis = 0).min()
        print('earliest year of birth is {} '.format(earliest_birthyear))
        most_recent_birthyear = df['Birth Year'].dropna(axis = 0).max()
        print('most recent of birth is {}'.format(most_recent_birthyear))
        common_birthyear = df['Birth Year'].dropna(axis = 0).mode()[0]
        print('most common year of birth {}'.format(common_birthyear))
    except:
        print("There is no Birth Year data.")
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        # ask user if want to display data
        view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n ').lower()
        start_loc = 0
        # loop for display 5 rows data then ask for display new 5 row data 
        while view_data=='yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
            view_data = input(" Do you wish to continue?Enter yes or no \n ").lower()    
    
        restart = input(' \nWould you like to restart? Enter yes or no.\n ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('Which of these cities would you like to explore? chicago, new york city or        washington? \n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('please choose from chicago, new york city, washington')            

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month would you like to explore? all, January, February, March, April, May,June? \n').lower()
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('please choose from January, February, March, April, May,June, all') 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('which day of the week are you interested in? all, monday, tuesday, wednesday, thursday, friday, saturday, sunday?').lower()
        if day in ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('please choose all or any day of the week')

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
    df = pd.read_csv(CITY_DATA[city])
    
    #converting start time to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    #getting columns for month and weekday
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
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    commonest_month = df['month'].mode()[0]
    print('The most common month is: ', commonest_month)

    # TO DO: display the most common day of week
    commonest_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: ', commonest_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Hour:', popular_start_station)


    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular end Hour:', popular_end_station.value_counts())

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df['Start Station'] + 'and' + df['End Station']
    print('Most Popular end Hour:', frequent_combination.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    print('the total travel time in seconds is: ', total_travel)
    print('the total travel time in minutes is: ', total_travel/60)

    # TO DO: display mean travel time
    print('the mean travel time is: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if city in ['chicago', 'new york city']:
        gender_counts = df['Gender'].value_counts()
        #print(gender_counts)
    else:
        print("This information is not available in this particular acid. Try either chicago or new york city")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    
    earliest_yr = int(df['Birth Year'].min())
    most_recent_yr = int(df['Birth Year'].max())
    commonest_yr = int(df['Birth Year'].mode())
    print('The earliest year of birth is {}.\nThe most recent year of birth is {}.'
          '\nThe commonest year of birth is {}.'.format(earliest_yr, most_recent_yr, commonest_yr))
    


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

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

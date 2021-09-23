import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
CITY_NAME = ""
# comment line 1
# comment line 2

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            "1. Enter the city name (chicago, new york city, washington): ")
        CITY_NAME = city
        print("Great! the city is {}".format(city.title()))

        if city.lower() not in ('chicago', 'new york city', 'washington'):
            print("Not an appropriate choice.")
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "2. Enter the month name (all, january, february, ... , june): ")
    print("Good jop! the month is {}".format(month.title()))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("1. Enter the day name (all, monday, tuesday, ... sunday): ")
    print("Well Done! the day is {}".format(day.title()))

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

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month from the Start Time column to create an month column
    df['month'] = df['Start Time'].dt.month
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Start month:', popular_month)

    # TO DO: display the most common day of week
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['day'] = df['Start Time'].dt.day
    # find the most popular hour
    popular_day = df['day'].mode()[0]
    print('Most Popular Start day:', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly Used Start Station:', start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print('Most Commonly Used End Station:', end_station)

    # TO DO: display most frequent combination of start station and end station trip
    start_end = ("FROM" + df['Start Station'] + "TO" +
                 df['End Station']).value_counts().idxmax()
    print('Most Commonly Trip is:', start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('Total Travel Time is:', total)
    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('Mean Travel Time is:', mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if CITY_NAME.lower() in ('new york city', 'washington'):
        # print value counts for each gender type
        genders = df['Gender'].value_counts()
        print(genders)

    # TO DO: Display earliest, most recent, and most common year of birth
    if CITY_NAME.lower() in ('new york city', 'washington'):
        df['Brith Year'] = pd.to_datetime(df['Brith Year'])
        # extract hour from the Start Time column to create an year column
        df['year'] = df['Brith Year'].dt.year
        # find the years
        popular_year = df['year'].mode()[0]
        recent_year = df['year'].max()[0]
        earliest_year = df['year'].min()[0]

        print('Most Popular Brith Year:', popular_year)
        print('Most Recent Brith Year:', recent_year)
        print('The Earliest Brith Year:', earliest_year)

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

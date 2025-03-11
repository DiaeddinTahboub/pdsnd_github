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
        city_choice = input("Would you like to see data for: Chicago, New York city, or Washington?\n")
        city = city_choice.lower()
        if city in CITY_DATA:
            print('-' * 40)
            acceptance_choice = input(f"You chose to see the data of {city}, proceed? (yes/no)\n").lower()
            if acceptance_choice == 'yes':
                break

        else:
            print("Enter a valid city")

    filter = input("Would you like to filter by month, day, or all, insert \"none\" for no filter?\n").lower()
    filter_day = filter == "all" or filter == "day"
    filter_month = filter == "all" or filter == "month"

    months = ['january', 'february', 'march', 'april', 'may', 'june', "all"]
    month = ""
    day = ""
    # TO DO: get user input for month (all, january, february, ... , june)
    while filter_month:
        month = input("Which month? January, February, March, April, May, June, or all?\n").lower()
        if month in months:
            print('-' * 40)
            break
        else:
            print("Enter a valid month")
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "all"]
    while filter_day:

        try:
            day_choice = int(input("Which day? please enter your response as an integer (1=Sunday, 7=Saturday, 8=all):\n"))
            if 8 >= day_choice >= 1:
                day = days[day_choice-1]
                print('-' * 40)
                break
        except:
            print("Enter a valid day")
        if day == "":
            print("Enter a valid day")
    if day == "":
        day = "all"
    if month == "":
        month = "all"
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
    df = pd.read_csv(CITY_DATA[city])

    # create a start and destination column
    df["Start - End"] = "(" + df["Start Station"] + ", " + df["End Station"] + ")"
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime("%A")

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
    most_frequent_month = df['month'].mode()[0]
    print('Most Frequent Month:', most_frequent_month)
    print('-' * 40 + "\n")
    # TO DO: display the most common day of week
    most_frequent_day = df['day_of_week'].mode()[0]
    print('Most Frequent Day:', most_frequent_day)
    print('-' * 40 + "\n")
    # TO DO: display the most common start hour

    most_frequent_hour = df['Start Time'].dt.hour.mode()[0]
    print('Most Frequent Start Hour:', most_frequent_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40 + "\n")


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_frequent_start_station = df['Start Station'].mode()[0]
    print("Most Frequent Start Station:", most_frequent_start_station)
    print('-' * 40 + "\n")
    # TO DO: display most commonly used end station
    most_frequent_end_station = df['End Station'].mode()[0]
    print("Most Frequent End Station:", most_frequent_end_station)
    print('-' * 40 + "\n")
    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_start_end = df['Start - End'].mode()[0]
    print("Most Frequent Start and End stations:", most_frequent_start_end)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40 + "\n")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_duration = df["Trip Duration"].sum()
    print("Total Trip Duration:", total_travel_duration)
    print('-' * 40 + "\n")
    # TO DO: display mean travel time
    average_trip_duration = df["Trip Duration"].mean()
    print("Average Trip Duration:", average_trip_duration)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40 + "\n")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("What is the breakdown of users?")
    print(df["User Type"].value_counts())
    print('-' * 40 + "\n")
    # TO DO: Display counts of gender
    try:
        column = df["Gender"].value_counts()
        print("What is the breakdown of users gender?")
        print(column)
        print('-' * 40 + "\n")
    except:
        pass
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        column = df["Birth Year"]
        print(f"The earliest year of birth: {column.min()}")
        print(f"The latest year of birth: {column.max()}")
        print(f"The most comon year of birth: {column.mode()[0]}")
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-' * 40 + "\n")
    except:
        pass
def display_data(df):
    """
    Args:
        df: The dataframe containing bikeshare data.

    Returns: None
    """
    choice = input("Would you like to see a portion of the data? (yes/no)\n").lower()
    i = None
    if choice == 'yes':
        i = 0



    while choice != "no" and i is not None and i < len(df):
        print(df.iloc[i: i + 5])
        print('-' * 40 + "\n")
        choice = input("Would you like to see another portion of the data? (yes/no)\n").lower()
        if choice != 'yes':
            break
        i += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Goodbye! Have a nice day!")
            break


if __name__ == "__main__":
    main()

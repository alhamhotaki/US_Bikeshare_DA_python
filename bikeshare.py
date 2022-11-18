import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
#This project is submitted by Alham Hotaki. For this project I used different study materials, mainly solutions provided by udacity course, associated examples and also I studied different material from w3schools.com on pandas methods, github.com on how to extract day and month from start time column and watched some educational videos shared by other fellows on our slack channel to understand how to display more data if required by the user. I also included the plotting function from matplot. 

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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:  
        city = input('Please choose one of the cities from our experimenting list: chicago, new york city, or washington: ').lower()
        if city not in CITY_DATA:
            print('Please enter a valid city name only from the list provided:')
        else:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Please choose a month from january to june or you can select "all" to filter all months:  ''\n').lower()
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        if month not in months and month != 'all':
            print('Please enter a valid Month filter')
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please choose a day of the week or you can select "all" to filter all days:  ''\n').lower()
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in days and day != 'all':
            print('Please enter a valid Day of the weekcd ')
        else:
            break

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
    #first we should load the city data:
    df = pd.read_csv(CITY_DATA[city])
    #as it is stated in the project files, we should change the start time column to date time, for this purpose we can use:
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #now we need month and day of the week from the column: Start Time
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.day_name()
    #now filtering:
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['week_day'] == day.title()]
        
    return df

def raw_data(df):
    while True:
        choices=['yes', 'no']
        answer = input('Do you want to display first five rows of data? please type yes or no in lowercases\n').lower()
        if answer in choices: 
            if answer == 'yes':
                start=0
                end=5
                data = df.iloc[start:end]
                pd.set_option('display.max_columns',200)
                print(data)
            break
        else:
            print('Please choose a proper response')
    if answer == 'yes':
        while True:
            answer2 = input('Do you want to display more data? please type yes or no in lowercase\n').lower()
            if answer2 in choices:
                if answer2 == 'yes':
                    start+=5
                    end+=5
                    data = df.iloc[start:end]
                    pd.set_option('display.max_columns',200)
                    print(data)
                else:    
                    break  
            else:
                print("Please choose a proper response")

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    months= ['January','February','March','April','May','June']
    common_month= months[common_month-1]
    print("The most Common popular month is:  ",common_month)


    # display the most common day of week
    common_day= df['week_day'].mode()[0]
    print("The most Common popular day is:  ",common_day)


    # display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour=df['Start Hour'].mode()[0]
    print("The Common popular Start Hour is {}:00 hrs".format(common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print("The most commonly used/busy Start Station is {}".format(common_start_station))


    # display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print("The most commonly used/busy End Station is {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['combined']=df['Start Station']+" "+"to"+" "+ df['End Station']
    combined_stations= df['combined'].mode()[0]
    print("The most frequent combined (start and end) Station is {} ".format(combined_stations))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    ttrip_time=df['Trip Duration'].sum()
    print('Total travel time is:  ', ttrip_time,  'seconds or   ', ttrip_time/60,  'minutes or   ', ttrip_time/3600,  'hours or  ', ttrip_time/3600/24, 'days' )

    # display mean travel time
    ttrip_average=df['Trip Duration'].mean()
    print('Average trip time is:  ', ttrip_average,  'seconds or   ', ttrip_average/60,  'minutes or   ', ttrip_average/3600,  'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_num= df['User Type'].value_counts()
    
    plt.figure(figsize=(7,6))
    plt.pie(user_num.values, labels =user_num.index,autopct='%1.1f%%')
    plt.title("Percentage of user type category")
    plt.legend(user_num.index)
    plt.show()
    #plt.title("User Type")
    #plt.bar(user_num.index, user_num.values)
    #plt.ticklabel_format(style='plain', axis='y')
    #plt.show()

    print("The user types are:\n",user_num)

    # Display counts of gender
    # washington city data does not have gender column, so we will put if function as follows:
    if 'Gender' in df:
        print('Number of users by gender:  ', df['Gender'].value_counts())

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest= int(df['Birth Year'].min())
        print('The most senior user was born in:  ' ,earliest)
        most_recent= int(df['Birth Year'].max())
        print('A {} birth year makes up the youngest user.'.format(most_recent))
        common= int(df['Birth Year'].mode())
        print("Most users are born in {} year".format(common))

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
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

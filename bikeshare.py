import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'NY': 'new_york_city.csv',
              'Washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June', 'all']
days = ['Sunday' ,'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']


# This funtion asks for user input and explains how needs to be entered.
def get_filters():
    """Function to get city, month and day inputs ."""
     
    # get city input    
    city = ""
    while city not in CITY_DATA:
        city = input("Please type which City: ")
        if city not in CITY_DATA:
            print("Cities available are NY, Chicago and Washington")

    # get the month input
    month = ""
    while month not in months:
        month = input("Please type month i.e. January, February or all: ")
        if month not in months:
            print("Data available from January thru June. Please type month name or 'all': ")

    # get the day input
    day = ""
    while day not in days:
        day = input("Please type day name or 'all': ")
        if day not in days:
            print("Please type day name in this format: Sunday, Friday, etc or type 'all': ")

    print('-'*40, "\n"*2, "These are the options you selected: ", city, month, day,"\n"*2,'-'*40)
    return city, month, day


def load_data(city, month, day):

    # loads data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # converts the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extracts month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month_name()
    df['day'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
  
    print('\nCalculating The Most Frequent Times of Travel...\n')

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Displays the most common month
    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month_name()  
  
    # find the most popular month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # Displays the most common day of week
    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.day_name()
  
    # find the most popular month
    popular_day = df['day'].mode()[0]
    print('Most Popular Day:', popular_day)    

    # Display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    
    # find the most popular hour
    popular_hour = df['hour'].mode()[0]    
    print('Most Popular Start Hour:', popular_hour)
    print('-'*40)

    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trips...\n')


    # Displays the most commonly used start station
    
    # find the most popular starting station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular Starting Station is: ', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular End Station is: ', popular_end_station)
    
    
    # Display the most frequent combination of start station and end station trip
    df['Trip Combination'] = df['Start Station'] + ' to ' + df['End Station']
    popular_trip = df['Trip Combination'].mode()[0]
    print('The most popular trip combination is: ',popular_trip)

    print('-'*40)
    

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration stats...\n')


    # Display total travel time
    total_travel = pd.Series(df['Trip Duration']).sum().astype(int)
    print('The total time travelled is {} minutes!: '.format(total_travel))

    # Display mean travel time
    average_travel = df["Trip Duration"].mean().astype(int)
    print('The average time per travel is {} minutes!: '.format(average_travel))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""
 

    print('\nCalculating User Stats...\n')
    
    if 'Gender' in df:
        # Display counts of user types
        print('Count per User Type:\n', df.groupby('User Type').size())
        # Display counts of gender
        print('\nCount by Gender:\n',df.groupby('Gender').size())    
        # Display earliest, most recent, and most common year of birth  
        print('The earliest birthday of users is: ', df['Birth Year'].min().astype(int))
        print('The most recent birthday of users is: ', df['Birth Year'].max().astype(int))
        print('The most common birthday of users is: ', df['Birth Year'].mode()[0].astype(int))
        print('-'*40)
    else:
        # TO DO: Display counts of user types        
        print('Count per User Type:\n', df.groupby('User Type').size())
        print('\nWashington does not have Gender information')
        print('-'*40)

        

def raw_data(df):
    """Displays raw data based on customer input."""
  
    view_raw = input('Would you like to see some raw data? Please type "y" for yes or "n" for no.\n ')
    i = 0
    while view_raw != 'n':
        print(df[i:i+5])
        i += 5
        view_more_raw = input('Do you want to see more rows? Please type "y" for yes or "n" for no.\n ')    
        if view_more_raw != 'y':
            break
    

def main():
    while True:
        start_time = time.time()
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        print("\nThis analysis took %s seconds." % int((time.time() - start_time)))
        restart = input('\nWould you like to restart? Enter "y" for yes or "n" for no.\n')
        if restart.lower() != 'y':
            print('Thanks for using the stat analysis program!')
            break


if __name__ == "__main__":
	main()
# Khoa Duong
# Assignment 13
# Create a database function to store population for 10 cities, their expected growth, then let user choose a city to display.

import sqlite3
import matplotlib.pyplot as plt

# Create and insert data for 2023.
def population_KD():
    
    #Create database file.
    conn = sqlite3.connect('population_KD.db')
    cur = conn.cursor()
    
    #Create a table.
    cur.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    cities_data = [
        ('Miami', 2023, 449514),
        ('Orlando', 2023, 316081),
        ('Tampa', 2023, 407599),
        ('Jacksonville', 2023, 971319),
        ('St. Pete', 2023, 261256),
        ('Hialeah', 2023, 220490),
        ('Tallahassee', 2023, 201731),
        ('Fort Lauderdale', 2023, 183445),
        ('Cape Coral', 2023, 216992),
        ('Gainesville', 2023, 145214)
    ]
    
    #Insert data into database table.
    cur.executemany("INSERT INTO population (city, year, population) VALUES (?, ?, ?)", cities_data)
    conn.commit()
    conn.close()

# Simulate 2% growth for the next 20 years.
def population_growth():
    
    #connect to database.
    conn = sqlite3.connect('population_KD.db')
    cur = conn.cursor()

    #Gett 2023 data from table.
    cur.execute("SELECT city, population FROM population WHERE year = 2023")
    data_2023 = cur.fetchall()

    #Calculate and insert data for next 20 years.
    for city, pop in data_2023:
        current_pop = pop
        for year in range(2024, 2024 + 20):
            current_pop = int(current_pop * 1.02)
            cur.execute("INSERT INTO population (city, year, population) VALUES (?, ?, ?)",
                        (city, year, current_pop))
    conn.commit()
    conn.close()

# Let user choose a city and display population growth.
def main():
    population_KD()
    population_growth()

    # Connect to database again.
    conn = sqlite3.connect('population_KD.db')
    cur = conn.cursor()

    # Get city list.
    cur.execute("SELECT DISTINCT city FROM population")
    cities = [row[0] for row in cur.fetchall()]

    # Show city options.
    print('\nAvailable cities:')
    for i, city in enumerate(cities, 1):
        print(f'{i}. {city}')

    # Let user choose by number with a loop.
    while True:
        try:
            choice = int(input('\nChoose a city by number (1-10): '))
            if 1 <= choice <= 10:
                selected_city = cities[choice - 1]
                # Retrieve info for selected city.
                cur.execute('SELECT year, population FROM population WHERE city = ? ORDER BY year', (selected_city,))
                results = cur.fetchall()
                break  
            else:
                print('Please enter a number from the list.')
        except ValueError:
            print('Invalid input. Please enter a number.')

    # Separate into lists for plotting.
    years = [row[0] for row in results]
    populations = [row[1] for row in results]

    # Use matplotlib to plot population data.
    plt.plot(years, populations, marker='o')
    plt.title(f"Population Growth for {selected_city}")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Close connection.
    conn.close()


if __name__ == '__main__':
    main()

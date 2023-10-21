"""
Name:Yizhi Chen
Date started:21/10/2023
GitHub URL: https://github.com/yizhichengit/starter_a1_songs.git
"""


import csv  # Import the csv module for reading and writing CSV files.

# Function to display the menu
def display_menu():
    # Print menu options
    print("\nMenu:")
    print("D - Display songs")
    print("A - Add new song")
    print("C - Complete a song")
    print("Q - Quit")

# Function to display songs
def display_songs(songs):
    # Loop through each song in the songs list
    for i, song in enumerate(songs):
        # Set status to "*" if the song is not learned, otherwise empty string
        status = "*" if song[3] == 'n' else ""
        # Print song details with status
        print(f"{i+1}. {song[0]:<20} - {song[1]:<15} ({song[2]}) {status}")

    # Calculate the number of songs not learned
    not_learned = sum(1 for song in songs if song[3] == 'n')
    # Print the number of songs learned and not learned
    print(f"\n{len(songs)-not_learned} songs learned, {not_learned} songs still to learn.")

# Function to add a new song
def add_song(songs):
    # Take input for song title, artist, and year
    title = input("Title: ")
    artist = input("Artist: ")
    year = input("Year: ")
    # Check if song already exists in the list
    for song in songs:
        if song[0].lower() == title.lower() and song[1].lower() == artist.lower():
            # Notify user if song exists and return to menu
            print(f"{title} by {artist} already exists in the song list.")
            return
    # Add the new song to the songs list
    songs.append([title, artist, year, 'n'])
    # Notify user that song has been added
    print(f"{title} by {artist} ({year}) added to song list")

# Function to mark a song as learned
def complete_song(songs):
    try:
        # Ask user for song number
        num = int(input("Enter the number of a song to mark as learned: "))
        # Check if entered song number is valid
        if 1 <= num <= len(songs):
            # If song is not learned
            if songs[num-1][3] == 'n':
                # Mark the song as learned
                songs[num-1][3] = 'y'
                # Notify user
                print(f"{songs[num-1][0]} by {songs[num-1][1]} learned")
            else:
                # Notify user if song is already learned
                print(f"You have already learned {songs[num-1][0]} by {songs[num-1][1]}.")
        else:
            # Notify user if entered song number is invalid
            print("Invalid song number")
    except:
        # Handle any exception (like if user doesn't enter a number) and notify user
        print("Invalid song number")

def main():
    songs = []  # Initialize an empty list to store songs
    # Open the CSV file for reading
    with open('songs.csv', 'r') as file:
        reader = csv.reader(file)
        # Convert CSV content to a list of songs
        songs = list(reader)

    # Print the welcome message with total songs count
    print(f"Song List 1.0 - by [Your Name]\n{len(songs)} songs loaded.")
    display_menu()  # Display the main menu

    # Take user's choice for menu option
    choice = input(">>> ").upper()
    # Loop until user chooses to quit
    while choice != 'Q':
        if choice == 'D':
            display_songs(songs)  # Display the list of songs
        elif choice == 'A':
            add_song(songs)  # Add a new song to the list
        elif choice == 'C':
            complete_song(songs)  # Mark a song as learned
        else:
            # Notify user if an invalid choice is made
            print("Invalid menu choice")

        display_menu()  # Display the menu again after each action
        choice = input(">>> ").upper()  # Take the next choice from user

    # Open the CSV file for writing and save updated songs list
    with open('songs.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(songs)

    # Print the goodbye message with total songs count
    print(f"{len(songs)} songs saved to songs.csv\nHave a nice day :)")

# Entry point of the script
if __name__ == '__main__':
    main()



# your code goes here
import sys

print("Welcome to Anirudh's Online Auction System")

logged_in = False
username = 'admin'
while True:
    print("Please select the appropriate option:")
    if not logged_in:
        print("\tEnter 1 to log in")
        print("\tEnter 2 to view the items up for bidding")
        print("\tEnter 3 to register")
        print("\tEnter q to exit")
        response = input("Answer: ")
        if response == 'q':
            sys.exit("Thanks for visitng. Goodbye.")
        elif response == '1':
            username = LogIn()
            if username:
                logged_in = True
                print("Welcome "+username+"!")
            else:
                print("Invalid credentials. Please try again.")    
        elif response == '2':
            ViewAllItems()
        elif response == '3':
            RegisterUser()
        else:
            print("Please enter a valid response")    
    else:
        print("\tEnter 1 to view all items up for bidding")
        print("\tEnter 2 to place a bid")
        print("\tEnter 3 to put an item up for auction")
        print("\tEnter 4 to view all my items")
        print("\tEnter 5 to view all my bids")
        print("\tEnter 6 to log out")
        print("\tEnter q to exit")
        response = input("Answer: ")
        if response == 'q':
            sys.exit("Thanks for visitng. Goodbye.")
        elif response == '1':
            ViewAllItems()
        elif response == '2':
            PlaceBid(username)
        elif response == '3':
            AuctionItem(username)
        elif response == '4':
            ViewMyItems(username)
        elif response == '5':
            ViewMyBids(username)
        elif response == '6':
            username = 'admin'
            logged_in = False
        else:
            print("Please enter a valid response")    

def db_login(username, password):
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE username="+username+" AND password="+password)
    return cursor.fetchall()

def LogIn():
    username = input("Please enter the username")
    password = input("Please enter the password")
    if db_login(username, password):
        return username
    else
        return False

# def ViewAllItems():


#Khoa Duong
#Programing exercise 1
#Write a program that sell ticket to user, mac is 4 per user until the total reavh 20 tickets.


    
# Main function to run.
def main():
    total_tickets = 20 
    total_buyers = 0

    while total_tickets > 0:
        print(f'Tickets remaining: {total_tickets}')
        tickets_requested = get_ticket_request()

        if tickets_requested <= total_tickets:
            total_tickets -= tickets_requested
            total_buyers += 1
            print(f'Successfully purchased! {total_tickets} tickets remaining.')
        else:
            print(f'Not enough tickets left. Only {total_tickets} tickets are available.')

    print(f'All tickets are sold out! Total number of buyers: {total_buyers}')

# Ask user to purchase tickets.
def get_ticket_request():
    while True:
        try:
            tickets = int(input('How many tickets would you like to buy? (1 to 4 only): '))
            if 1 <= tickets <= 4:
                return tickets
            else:
                print('Please enter a number between 1 and 4 only.')
        except ValueError:
            print('Please enter a valid number.')

main()

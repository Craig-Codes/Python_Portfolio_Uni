total_in_party = int(input("How many are in your party? "))
adults = int(input("How many adults are in your party? "))
concessions = int(input("How many concessions (adults over 65) are in your party? "))

children = total_in_party - adults - concessions

# Check to ensure children are always accompanied by an adult
if adults <= 0 and concessions <= 0:
    print("Sorry, children must be accompanied by at least 1 adult")
    exit()

# check to ensure entered quantities add up
if children < 0:
    print("Sorry please check your party total")
    exit()

postage = str(input("Are the tickets being posted - additional charge of £2.34? (y/n) ")).lower()

# Work out how many adults get in free depending on how many children there are
free_adults = 0

if children >= 10 and children <= 19:
    free_adults = 1
elif children >= 20 and children <= 29:
    free_adults = 2
elif children >= 30 and children <= 39:
    free_adults = 3
elif children >= 40 and children <= 49:
    free_adults = 4
elif children >= 50 and children <= 59:
    free_adults = 5
elif children >= 60 and children <= 69:
    free_adults = 6
elif children >= 70 and children <= 79:
    free_adults = 7
elif children >= 80 and children <= 89:
    free_adults = 8
elif children >= 90 and children <= 99:
    free_adults = 9
elif children >= 100 and children <= 109:
    free_adults = 10

# Work out the number of free tickets - prioritising adults over concessions (who are adults with cheaper tickets)
adult_tickets_total = adults - free_adults
concessions_ticket_total = concessions
if adult_tickets_total < 1:
    # if less than 1 adult ticket after the free tickets, we want to give the free tickets to concessions
    concessions_ticket_total = concessions + adult_tickets_total
    adult_tickets_total = 0
    if concessions_ticket_total < 1:
        # if less than 1 concession ticket, and less than 1 adult ticket, no free tickets!
        concessions_ticket_total = 0

print("Your tickets are for {} adults, {} children and {} concessions".format(adults, children, concessions))
if adults is not adult_tickets_total or concessions is not concessions_ticket_total:
    # ticket numbers dont match, so an offer has been used
    print("after the free ticket offer is applied, you are paying for {} adults and {} concessions".format(
        adult_tickets_total, concessions_ticket_total))
print("{} adults x £10.50 = £{:.2f}".format(adult_tickets_total, adult_tickets_total * 10.50))
print("{} children x £7.30 = £{:.2f}".format(children, children * 7.30))
print("{} concessions x £8.40 = £{:.2f}".format(concessions_ticket_total, concessions_ticket_total * 8.40))

# Work out the bill
bill = (adult_tickets_total * 10.50) + (children * 7.30) + (concessions_ticket_total * 8.40)

if bill > 100:
    # 10% discount
    print("Subtotal is £{:.2f}".format(bill))
    print("Your bill is over £100 so you qualify for a 10% discount!")
    print("Your bill was £{:.2f}".format(bill))
    bill = bill * 0.90
    print("Your bill is now £{:.2f}".format(bill))
else:
    print("Your bill is £{:.2f}".format(bill))

# Check for postage charge
if postage == "y":
    bill += 2.34
    print("We have added a £2.34 postage charge")
    print("Total bill = £{:.2f}".format(bill))
else:
    print("Total bill = £{:.2f}".format(bill))



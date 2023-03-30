#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input('What was your total bill $'))
tip = int(input("How much tip would you like to give? 10, 12, or 15?"))
people = int(input("How many people are going to split the bill?"))
bill_tip = tip / 100 * bill + bill
split_bill = bill_tip / people
final_amt = round(split_bill, 2)
final_amt = "{:.2f}".format(split_bill)
print(f"Each person should pay {final_amt}")
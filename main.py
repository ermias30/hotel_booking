import pandas as pd

df = pd.read_csv("hotels.csv", dtype={"id": str})
df_cards = pd.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_secure=pd.read_csv("card-security.csv",dtype=str)


# class User:
#     def view_hotel(self):
#         pass
#


class Hotel:
    def __init__(self, id1):

        self.id1 = id1
        self.name = df.loc[df["id"] == self.id1, "name"].squeeze()

    def book(self):
        df.loc[df["id"] == self.id1, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):

        availability = df.loc[df["id"] == self.id1, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False


class ReservationTicket:
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        # content=f"name of the customer name "
        # return content

        content = f"""
        thank you for booking in our hotel:
        name:{self.customer_name}
        hotel name:{self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validatate(self, expiration, holder, cvc):
        card_date = {"number": self.number, "expiration": expiration,
                     "holder": holder, "cvc": cvc}
        if card_date in df_cards:
            return True
        else:
            return False
class SecureCard(CreditCard):
    def authentication(self,given_password):
        password=df_cards_secure.loc[df_cards_secure["number"] == self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


print(df)
print(df_cards)

id1 = input("enter the hotel id")

hotel = Hotel(id1)
if hotel.available():
    # card_number=input("enter the credit number")
    # credit_card = CreditCard(number="1234" )
    credit_card = SecureCard(number="1234")
    if credit_card.validatate(expiration="12/26", cvc="123", holder="JOHN SMITH"):
        if credit_card.authentication(given_password="mypass"):
            hotel.book()
            name = input("enter your name")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())
        else:
            print("credit card failed")
    else:
        print("wrong credit card")
else:
    print("hotel is not free")

# df = pd.DataFrame({'Sports': ['Football', 'Cricket', 'Baseball', 'Basketball',
#                               'Tennis', 'Table-tennis', 'Archery', 'Swimming', 'Boxing'],
#                    'Player': ["Messi", "Afridi", "Chad", "Johnny", "Federer",
#                               "Yong", "Mark", "Phelps", "Khan"],
#                    'Rank': [1, 9, 7, 12, 1, 2, 11, 1, 1]})
#
# print(df.loc[df["Rank"] == 1])
# print('\n')
# print(df.loc[df["Sports"] == "Football"])

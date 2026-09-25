while True :
    name = input("Enter your name : ")

    if name.lower() == "done":
        break


    city        = input("Enter your city : ")
    weight      = float(input("Weight (Kg) :"))

    if weight <= 0:
        print("Invalid Weight.Please enter.....")
        continue

    tracking_id = input("Enter your tracking id : ")
    service = input("Service (standard/express: ")


    tracking_id = tracking_id.strip().upper()
    service    = service.strip().lower()

    if service == "express":
        rate_per_kg = 90  #rupees per kg
    elif service == "standard":
        rate_per_kg = 60  #rupees per kg
    else:
        print("Unknown services")       
        rate_per_kg = 60 # rupees per kg
        
    total_price = weight * rate_per_kg

    if weight > 20:
        surcharge = 100
        total_price += surcharge
        print(f"Heavy package surcharge applied: Rs.{surcharge}")

    print("=" * 50)
    print("SHIPPING LABEL".center(50))
    print("=" * 50)
    print(f"Your name : {name.capitalize()}")
    print(f"You from : {city.strip().title()}")
    print(f"Package  deliver after Weigh : {weight} Kg")
    print(f"Your tracking basic id : {tracking_id}")
    print(f"Total price : Rs. {total_price:.2f}")
    print("=" * 50)

print("Program closed. Thanks for using the shipping tool!")    
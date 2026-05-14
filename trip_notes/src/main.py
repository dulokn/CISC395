import sys
import os

# Fix import path for running from root
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.models import Destination
from src.storage import load_trips, save_trips

def main():
    collection = load_trips()
    
    while True:
        print("\n=== Trip Notes ===")
        print("[1] Add destination")
        print("[2] View all destinations")
        print("[3] Search by country")
        print("[4] Add note to a destination")
        print("[5] Quit")
        
        choice = input("Select an option: ").strip()
        
        if choice == "1":
            name = input("Enter destination name: ")
            country = input("Enter country: ")
            try:
                budget = float(input("Enter estimated budget in USD: "))
                trip = Destination(name=name, country=country, budget=budget)
                collection.add(trip)
                save_trips(collection)
                print(f"Added {name} to your trips!")
            except ValueError:
                print("Invalid budget. Please enter a number.")
                
        elif choice == "2":
            trips = collection.get_all()
            if len(trips) == 0:
                print("No trips saved yet.")
            else:
                for i, trip in enumerate(trips, 1):
                    notes_str = ", ".join(trip.notes) if trip.notes else "None"
                    print(f"{i}. {trip.name}, {trip.country} (${trip.budget:.2f}) - Notes: {notes_str}")
                    
        elif choice == "3":
            country = input("Enter country to search for: ")
            results = collection.search_by_country(country)
            if not results:
                print(f"No trips found in {country}.")
            else:
                for trip in results:
                    notes_str = ", ".join(trip.notes) if trip.notes else "None"
                    print(f"- {trip.name}, {trip.country} (${trip.budget:.2f}) - Notes: {notes_str}")
                    
        elif choice == "4":
            trips = collection.get_all()
            if len(trips) == 0:
                print("No trips saved yet.")
            else:
                for i, trip in enumerate(trips, 1):
                    print(f"[{i}] {trip.name}, {trip.country}")
                
                try:
                    idx_input = int(input("Select a destination number: "))
                    if 1 <= idx_input <= len(trips):
                        note = input("Enter note: ")
                        trip = collection.get_by_index(idx_input - 1)
                        trip.add_note(note)
                        save_trips(collection)
                        print("Note added!")
                    else:
                        print("Invalid number.")
                except ValueError:
                    print("Please enter a valid number.")
                    
        elif choice == "5":
            print("Goodbye!")
            break
            
        else:
            print("Invalid option, try again.")

if __name__ == "__main__":
    main()

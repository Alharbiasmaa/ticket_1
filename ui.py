from app import App
import json

class UI:
    def __init__(self):
        self.app = App()

    def _print_menu(self):
        print("\t\tPeople List Application")
        print("\n")
        print("\t1. Add New Person")
        print("\t2. List People")
        print("\t3. Delete Person")
        print("\t4. Exit")
        print("\n")

    def _process_menu_choice(self):
        try:
            user_input = input("Enter Menu Choice: ")

            match(user_input[0]):
                case "1": self.add_person()
                case "2": self.list_people()
                case "3": self.delete_person()
                case "4": quit()
                case _: print("Invalid menu choice!")
        except IndexError:
            print("Invalid input. Please enter a valid menu choice.")

    def start_ui(self):
        while True:
            self._print_menu()
            self._process_menu_choice()

    def add_person(self):
        try:
            first_name = input("First Name: ")
            middle_name = input("Middle Name: ")
            last_name = input("Last Name: ")
            self.app.add_person(first_name=first_name, middle_name=middle_name, last_name=last_name)
            print("person added successfully")
        except Exception as e:
            print(f"Error adding person: {e}")

    def list_people(self):
        try:
            people = self.app.get_people()
            if len(people) > 0:
                print("\nList of People:")
                for person_name, person_info in people.items():
                    first_name =  person_info.get('firstName', '')
                    middle_name = person_info.get('middleName', '')
                    last_name = person_info.get('lastName',  '')
                    
                    full_name = f"{first_name} {middle_name} {last_name}".strip()
                    print(f"{person_name}: {full_name}")
            else:
                print("NO people found. ")
        except Exception as e:
            print(f"Error listing people: {e}") 

    def save_people(self,data):
        with open("people_list.json", mode="w") as f:
            json.dump(data,f)

    def delete_person(self):
        try:
            temp_dic= {}
            person_name = input("Enter the last name of the person to delete: ")  

            with open("people_list.json", mode="r") as f:
                temp_dic = json.loads(f.read())

            if person_name in temp_dic:

                del temp_dic[person_name]

                self.save_people(temp_dic)

                print(f"Person '{person_name}' delete successfully.")

            else:
                print(f"Person '{person_name}' not found.")


        except Exception as e:
            print(f"Error deleting person: {e}") 

                 
                                       

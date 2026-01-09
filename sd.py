import os
class Patient:
    def __init__(self, p_id, name, age, ailment, doctor):
        self.p_id = p_id
        self.name = name
        self.age = age
        self.ailment = ailment
        self.doctor = doctor

    def __str__(self):
        return f"{self.p_id} | {self.name} | {self.age} | {self.ailment} | {self.doctor}"

patients_list = []
FILE_NAME = "patients_data.txt"

def load_data():
    """Reads data from file and populates the patients_list"""
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) == 5:
                p = Patient(data[0], data[1], data[2], data[3], data[4])
                patients_list.append(p)

def save_data():
    """Writes all patient objects to the file"""
    with open(FILE_NAME, "w") as file:
        for p in patients_list:
            file.write(f"{p.p_id},{p.name},{p.age},{p.ailment},{p.doctor}\n")

def add_patient():
    print("\n--- Add New Patient ---")
    p_id = input("Enter Patient ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    ailment = input("Enter Ailment: ")
    doctor = input("Enter Assigned Doctor: ")

    new_patient = Patient(p_id, name, age, ailment, doctor)
    patients_list.append(new_patient)
    save_data()
    print("Patient added successfully!")

def view_patients():
    print("\n--- List of Patients ---")
    print("ID | Name | Age | Ailment | Doctor")
    print("-" * 40)
    for p in patients_list:
        print(p)

def delete_patient():
    p_id = input("Enter Patient ID to delete: ")
    global patients_list
    patients_list = [p for p in patients_list if p.p_id != p_id]
    save_data()
    print("Record deleted (if it existed).")

def main():
    load_data()
    while True:
        print("\n=== HOSPITAL PATIENT RECORDS ===")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Delete Patient")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            delete_patient()
        elif choice == '4':
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

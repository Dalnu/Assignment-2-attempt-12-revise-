
class Doctor:
    def __init__(self, name, specialization):
        self._name = name
        self.__specialization = specialization

    def get_specialization(self):
        return self.__specialization

class PatientRec:
    def __init__(self, name, dob, contactInfo, medicalHistory=None, currCondition=None, docAssigned=None,
                 appointmentDetails=None, medications=None):
        self._name = name
        self._dob = dob
        self._contactInfo = contactInfo
        self._medicalHistory = medicalHistory if medicalHistory else []
        self._currCondition = currCondition
        self._docAssigned = docAssigned
        self._appointmentDetails = appointmentDetails
        self._medications = medications if medications else []

    def update_medical_history(self, new_entry):
        self._medicalHistory.append(new_entry)

    def add_medication(self, medication):
        self._medications.append(medication)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self._front = None
        self._rear = None

    def enqueue(self, data):
        new_node = Node(data)
        if self._rear is None:
            self._front = self._rear = new_node
            return
        self._rear.next = new_node
        self._rear = new_node

    def dequeue(self):
        if self._front is None:
            return None
        temp = self._front
        self._front = temp.next
        if self._front is None:
            self._rear = None
        return temp.data

    def peek(self):
        return self._front.data if self._front else None

    def isEmpty(self):
        return self._front is None

    def __iter__(self):
        current = self._front
        while current:
            yield current.data
            current = current.next

class PrescriptionStack:
    def __init__(self):
        self._stack = []

    def push(self, prescription):
        self._stack.append(prescription)

    def pop(self):
        if self.is_empty():
            return None
        return self._stack.pop()

    def peek(self):
        return self._stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._stack) == 0

class ConsultationQueue:
    def __init__(self):
        self._front = None
        self._rear = None

    def enqueue(self, patient):
        new_node = Node(patient)
        if self._rear is None:
            self._front = self._rear = new_node
            return
        self._rear.next = new_node
        self._rear = new_node

    def dequeue(self):
        if self._front is None:
            return None
        temp = self._front
        self._front = temp.next
        if self._front is None:
            self._rear = None
        return temp.data

    def peek(self):
        return self._front.data if self._front else None

    def isEmpty(self):
        return self._front is None


#.............................................................................

def addPatientRec(patient, patientQueue):
    patientQueue.enqueue(patient)
    print("Patient record added successfully.")

def updatePatient(patient, patientQueue):
    updatedPatient = None
    tempQueue = Queue()
    found_patient = False
    while not patientQueue.is_empty():
        currPatient = patientQueue.dequeue()
        if currPatient._name == patient._name:
            found_patient = True
            print("Patient found. Here is the information:")
            print("Name:", currPatient._name)
            print("Date of Birth:", currPatient._dob)
            print("Contact Info:", currPatient._contactInfo)
            print("Medical History:", currPatient._medicalHistory)
            print("Current Condition:", currPatient._currCondition)
            print("Doctor Assigned:", currPatient._docAssigned)
            print("Appointment Details:", currPatient._appointmentDetails)
            print("Medications:", currPatient._medications)

            print("\nWhich section would you like to update?")
            print("1. Medical History")
            print("2. Current Condition")
            print("3. Doctor Assigned")
            print("4. Appointment Details")
            print("5. Medications")
            section_choice = input("Enter your choice (1-5): ")

            if section_choice == "1":
                medical_history = input("Enter patient's new medical history (if any): ")
                currPatient.update_medical_history(medical_history)
            elif section_choice == "2":
                curr_condition = input("Enter patient's new current condition (if any): ")
                currPatient.currCondition = curr_condition
            elif section_choice == "3":
                doc_assigned = input("Enter doctor's name: ")
                currPatient.docAssigned = doc_assigned
            elif section_choice == "4":
                appointment_details = input("Enter appointment details: ")
                currPatient.appointmentDetails = appointment_details
            elif section_choice == "5":
                medication = input("Enter new medication: ")
                currPatient.add_medication(medication)
            else:
                print("Invalid choice.")
            updatedPatient = currPatient
            choice = input("Do you want to update anything else? (yes/no): ").lower()
            if choice == "no":
                break
        tempQueue.enqueue(currPatient)
    while not tempQueue.isEmpty():
        patientQueue.enqueue(tempQueue.dequeue())
    if updatedPatient:
        print("Patient record updated successfully.")
    else:
        if not found_patient:
            print("Patient not found.")

def scheAppoint(patient, doctor, appointment_time):
    patient.appointmentDetails = (doctor.name, appointment_time)
    print("Appointment scheduled successfully.")

def issuPrescription(patient, prescStack, prescription):
    patient.medications.append(prescription)
    prescStack.push(prescription)
    print("Prescription issued successfully.")

def searPatient(patientName, patientQueue):
    found = False
    while not patientQueue.isEmpty():
        currPatient = patientQueue.dequeue()
        if currPatient.name == patientName:
            found = True
            print("Patient Name:", currPatient.name)
            print("Date of Birth:", currPatient.dob)
            print("Contact Info:", currPatient.contactInfo)
            print("Medical History:", currPatient.medicalHistory)
            print("Current Condition:", currPatient.currCondition)
            print("Doctor Assigned:", currPatient.docAssigned)
            print("Appointment Details:", currPatient.appointmentDetails)
            print("Medications:", currPatient.medications)
            break
    if not found:
        print("Patient not found.")

def removePatientRec(patientName, patientQueue):
    tempQueue = Queue()
    found = False
    while not patientQueue.isEmpty():
        currPatient = patientQueue.dequeue()
        if currPatient.name == patientName:
            found = True
            print("Patient record removed successfully.")
        else:
            tempQueue.enqueue(currPatient)
    if not found:
        print("Patient not found.")
    while not tempQueue.isEmpty():
        patientQueue.enqueue(tempQueue.dequeue())

def add_to_consultation_queue(patient_name, patient_queue, consultation_queue):
    found_patient = False
    for patient in patient_queue:
        if patient.name == patient_name:
            found_patient = True
            consultation_queue.enqueue(patient)
            print("Patient added to consultation queue successfully.")
            break
    if not found_patient:
        print("Patient not found. Please check the name and try again.")

def consult_all_patients(consultation_queue):
    consulted_patients = []
    while not consultation_queue.isEmpty():
        next_patient = consultation_queue.dequeue()
        consulted_patients.append(next_patient)
    return consulted_patients


#.............................................................................


patientQueue = Queue()
consultationQueue = ConsultationQueue()

services = {
    "1": "Add a new patient record",
    "2": "Update an existing patient record",
    "3": "Remove an existing patient record",
    "4": "Schedule an appointment for a patient",
    "5": "Issue a prescription to a patient",
    "6": "Search for a patient and display patient summary",
    "7": "Add patient to consultation queue",
    "8": "Consult next patient",
    "9": "Exit the program"
}


def main():
    prescStack = PrescriptionStack()
    while True:
        choice = Services()
        if not process_choice(choice, prescStack):
            break

def Services():
    print("Available Services:")
    for key, value in services.items():
        print(f"{key}. {value}")

    while True:
        choice = input("Please select a service (1-9): ")
        if choice.isdigit() and 1 <= int(choice) <= 9:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 9.")


def process_choice(choice, prescStack):
    if choice == "1":
        print("Service 1: Add a new patient record")
        name = input("Enter patient's name: ")
        dob = input("Enter patient's date of birth (YYYY-MM-DD): ")
        contact_info = input("Enter patient's contact information: ")
        new_patient = PatientRec(name, dob, contact_info)
        addPatientRec(new_patient, patientQueue)
    elif choice == "2":
        print("Service 2: Update an existing patient record")
        name = input("Enter patient's name to update record: ")
        found_patient = False
        for patient in patientQueue:
            if patient.name == name:
                found_patient = True
                print("Patient found. Here is the information:")
                print("Name:", patient.name)
                print("Date of Birth:", patient.dob)
                print("Contact Info:", patient.contactInfo)
                print("Medical History:", patient.medicalHistory)
                print("Current Condition:", patient.currCondition)
                print("Doctor Assigned:", patient.docAssigned)
                print("Appointment Details:", patient.appointmentDetails)
                print("Medications:", patient.medications)

                print("\nWhich section would you like to update?")
                print("1. Medical History")
                print("2. Current Condition")
                print("3. Doctor Assigned")
                print("4. Appointment Details")
                print("5. Medications")
                section_choice = input("Enter your choice (1-5): ")

                if section_choice == "1":
                    medical_history = input("Enter patient's new medical history (if any): ")
                    patient.update_medical_history(medical_history)
                elif section_choice == "2":
                    curr_condition = input("Enter patient's new current condition (if any): ")
                    patient.currCondition = curr_condition
                elif section_choice == "3":
                    doc_assigned = input("Enter doctor's name: ")
                    patient.docAssigned = doc_assigned
                elif section_choice == "4":
                    appointment_details = input("Enter appointment details: ")
                    patient.appointmentDetails = appointment_details
                elif section_choice == "5":
                    medication = input("Enter new medication: ")
                    patient.add_medication(medication)
                else:
                    print("Invalid choice.")
                print("Patient record updated successfully.")
                break

        if not found_patient:
            print("Patient not found. Please add a new patient.")

    elif choice == "3":
        print("Service 3: Remove an existing patient record")
        name = input("Enter patient's name to remove record: ")
        removePatientRec(name, patientQueue)
    elif choice == "4":
        print("Service 4: Schedule an appointment for a patient")
        name = input("Enter patient's name to schedule appointment: ")
        doctor_name = input("Enter doctor's name: ")
        doctor_specialization = input("Enter doctor's specialization: ")
        print("Select appointment time:")
        print("1. 9:00 AM")
        print("2. 11:00 AM")
        print("3. 2:00 PM")
        print("4. 4:00 PM")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            appointment_time = "9:00 AM"
        elif choice == '2':
            appointment_time = "11:00 AM"
        elif choice == '3':
            appointment_time = "2:00 PM"
        elif choice == '4':
            appointment_time = "4:00 PM"
        else:
            print("Invalid choice. Defaulting to 9:00 AM.")
            appointment_time = "9:00 AM"

        patient = PatientRec(name, "", "")
        doctor = Doctor(doctor_name, doctor_specialization)
        scheAppoint(patient, doctor, appointment_time)
    elif choice == "5":
        print("Service 5: Issue a prescription to a patient")
        name = input("Enter patient's name to issue prescription: ")
        prescription = input("Enter prescription: ")
        patient = PatientRec(name, "", "")
        issuPrescription(patient, prescStack, prescription)
    elif choice == "6":
        print("Service 6: Search for a patient and display patient summary")
        name = input("Enter patient's name to search: ")
        searPatient(name, patientQueue)
    elif choice == "7":
        print("Service 7: Add patient to consultation queue")
        name = input("Enter patient's name to add to consultation queue: ")
        add_to_consultation_queue(name, patientQueue, consultationQueue)
    elif choice == "8":
        print("Service 8: Consult all patients")
        consulted_patients = consult_all_patients(consultationQueue)
        if consulted_patients:
            print("Consulting all patients:")
            for i, patient in enumerate(consulted_patients, start=1):
                print(f"Patient {i}:")
                print("Name:", patient.name)
                print("Date of Birth:", patient.dob)
                print("Contact Info:", patient.contactInfo)
                print("Medical History:", patient.medicalHistory)
                print("Current Condition:", patient.currCondition)
                print("Doctor Assigned:", patient.docAssigned)
                print("Appointment Details:", patient.appointmentDetails)
                print("Medications:", patient.medications)
                print()
        else:
            print("No patients in the consultation queue.")

    elif choice == "9":
        print("Exiting the program.")
        return False
    else:
        print("Invalid choice. Please select a valid option.")
    return True

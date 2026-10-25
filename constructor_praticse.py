class Faculty:
    def put_data(self):
        self.id = int(input("Enter the id: "))
        self.name = str(input("Enter the name: "))
        self.salary = float(input("Enter the salary: "))

    def Display(self):
        print("Faculty ID: ", self.id)    
        print("Name of Employee: ", self.name)
        print("Salary of employee: ", self.salary)
a = Faculty()
a.put_data()
a.Display()
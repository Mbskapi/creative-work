class Human(object):
    def __int__(self, first_name, last_name, age, bouse):
        self.bouse = bouse
        super
        self.last_name = last_name
        self.age = age
        self.sex = self.sex

        Human.count += 1



        def full_name(self):
            return f"{self.last_name} {self.first_name}"

        def _str__(self):
            return f"name={self.last_name}{self.first_name} age={self.age}, sex={self.sex}"

        class manager(Human):
            def full_name(self):
                return f"{self.last_name[0].upper()}.{self.first_name}"
            pass

        class Employee(Human):
         def pay_salary(self, salary):
            return salary +self.bouse


        employee1: Employee = Employee("Hadiza", "umar", 21, "female")
        manager1: manager = manager("Egusi", "cappy", 65, "Unknow")

        print(employee1.full_name())
        print(employee1.full_name())


        human_list = [employee1, manager1]
        for human in human_list:
            print(human.pay_salary(50_000))



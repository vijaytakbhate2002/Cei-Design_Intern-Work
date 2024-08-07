class profile:
    """ This is a constructor which takes email and password parameters and make its 
    own email and password variables """
    def __init__(self, email:str, password:int) -> None:
        """Constructor function"""
        self.email = email
        self.password = password

    # takes user input and create class variables
    def get_info(self) -> None:
        self.name = input("Enter name\n")
        self.phone_no = input("Enter mobile number\n")
        self.address = input("Enter Address\n")

    # fucntion prints all class variables
    def print_info(self) -> None:   
        print(self.name)
        print(self.phone_no)
        print(self.address)

if __name__ == "__main__":
    obj = profile(email="xyz@gmail.com", password=87654321)
    obj.get_info()
    obj.print_info()


    
        
    

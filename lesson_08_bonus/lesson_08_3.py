
class Printer():

    def __init__(self, name:str):
        self.name = name
    
    def to_print(self, data:str):
        print(data)
    
    def check_paper(self, counter:int):
        return counter > 0

class Scanner():
    def scan(self, some_string:str):
        self.copy = some_string

class MFU(Printer, Scanner):

    def __init__(self, name):
        super().__init__(name)

if __name__ == "__main__":
    my_hp_printer = Printer("HP Laser Jet")
    # my_hp_printer.set_model()
    print(my_hp_printer.name)

    my_canon_printer = Printer("canon")
    # my_canon_printer.set_model()
    print(my_canon_printer.name)
    print(isinstance(my_hp_printer, Printer) == isinstance(my_canon_printer, Printer))

    my_mfu = MFU("HP Laser Scan Jet")
    # my_mfu.set_model()
    print(my_mfu.name)
    my_mfu.scan("ssss")
    print(my_mfu.copy)

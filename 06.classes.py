#
# Example file for working with classes
#

class myClass():
    def method1(self):
        print "myClass method1";
    
    def method2(self, someString):
        print "myClass method2: " + someString;
    
    def method3(self):
        print "myClass method3";
      
#anotherClass inheriting from myClass and overriding method1 and method2
class anotherClass(myClass):
    def method1(self):
        myClass.method1(self);
        print "anotherClass method 1";
        
    def method2(self):
        print "anotherClass method2";
        
def main():
    #exercise the class methods
    c = myClass();
    c.method1();
    c.method2("This is a string");
    c2 = anotherClass();
    c2.method1();
    c2.method2();
    c2.method3();             #method3 is printed from myClass as it is because it was not overriden
  
if __name__ == "__main__":
    main();
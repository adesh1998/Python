#Task 1

squares = {x: x*x for x in range(1,4)}

print(squares)
print([x for x in squares.values()])

#Task 2

list1=[1, 2, 5, 2, 3, 1, 4, 5]
squares = {x: x*x for x in set(list1)}
print(squares)

#Task 3
tuplelist=[("Guido", 2000, 500), ("Raymond", -52, 1000), ("Jack", 900, 1000), ("Brandon", 2000, 0)]
Dic={}
list1=[]
list2=[]
for index,tuples in enumerate(tuplelist):
    if tuples[1]>=tuples[2]:
        Dic[tuples[0]]=tuples[1]
    list1.append(tuples[1])
    list2.append(tuples[0])

print(Dic)
print(set(list1))
print(list2)

#Task 4

class Developer:

    def __init__(self):
        self.languages=["C","C++","Java","Python","JS","JSON"]

   

    def code(self,lang):
        if lang not in self.languages:
            print("code not found")
        else:
            print(f"code in {lang}")
    
    
    def resume(self):
        print(self.languages)

input_language = (input("Enter a coding language: ")).strip()

print(input_language.__str__())

print(input_language.__repr__())
obj= Developer()
obj.code(input_language)
obj.resume()

class SrDeveloper(Developer):

    def __init_(self):
        self.reviews=[]
        super().__init__(self)

    def review(self,review):
        if(review in self.languages):
            self.reviews.append(review)
            print(self.reviews)

        

obj1 = SrDeveloper()

obj1.code("java")

obj1.review("dotnet")

class TechLead(SrDeveloper):



    def __init__(self):

        SrDeveloper.__init__(self)

    

    def design(self):                      

        print("Design called by TechLead")

obj3 = TechLead()

obj3.code("java")

obj3.code("C")

obj3.resume()

obj3.review("Java") 

obj3.review("Python") 

obj3.review("ruby") #Doesn't get appended as the Code is not in main listc

obj3.design()          #Object of Subclass calling all it's  functions

    
    

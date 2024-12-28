class MyFirstClass():
    print("Who wrote this?")

    index = "Author-Book"

    def hand_list(self,philosopher,book ):
        print(MyFirstClass.index)
        print("{0} wrote the book: {1}".format(philosopher,book))
obj1 = MyFirstClass()
obj1.hand_list("amr","knight of the seven kingdoms")
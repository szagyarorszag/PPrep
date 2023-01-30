class MyFirstClass():

    print("Who wrote this?")

    def __init__(self,philosopher,book ):
        self.philosopher = philosopher
        self.book = book
    def Who_wrote_this_book( self ):
        print( f"{self.philosopher}  wrote this book :  {self.book} " )

class characteristic_of_author(MyFirstClass):
    def __init__( self , philosopher , birthday , nation ):
        super().__init__(self,philosopher)
        self.birthday = birthday 
        self.nation = nation
        
class characteristic_of_book(MyFirstClass): 
    def __init__(self, genre , book ):
        super().__init__(self, book)
        self.genre = genre 
    def genre_of_this_book(self ) :
        print(f"Genre of {self.book} is {self.genre}")

class main_info ( characteristic_of_book,characteristic_of_author ):
    def __init__(self , philosopher , nation , book , ) -> None :
        super().__init__( philosopher , nation , book ) 
    def main_info_(self):
        print(f"{self.philosopher} was { self.nation } author also philosopher which wrote {self.book}  ")
philosopher = input("Please put the name : ") 
genre = input("Please put the genre : ") 
nation = input("Please put the nation : ") 
birthday = input("Please put the birthday :") 
book = input("Please put the book : ")

author_and_book = MyFirstClass( philosopher , book )
genre_of_book = characteristic_of_book( genre , book )
author_info = characteristic_of_author( philosopher , birthday , nation )
main = main_info(philosopher ,  nation , book ) 
main.main_info_() 

''' 
whodunnit = MyFirstClass("Sun Tzu", "The Art of War")
whodunnit.Who_wrote_this_book()
'''
'''
try : 
    whodunnit.Who_wrote_this_book()
except TypeError as e: 
    print( "Something gone wrong" )
'''
'''
book_and_genre = characteristic_of_book("Historical" , "The Art of War" )
book_and_genre.genre_of_this_book() 
'''




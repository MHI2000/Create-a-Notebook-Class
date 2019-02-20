import sys
from Notebook import Notebook, Note

class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }
    def displayMenu(self):
        print("""
        Notebook Menu

        1.Show all notes
        2.Search notes
        3.Ass note
        4.Modify note
        5.quit
        """)

    def run(self):
        while True:
            self.displayMenu()
            choice = input("Enter an option:")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def quit(self):
         print("Thank you for using the notebook.")
         sys.exit(0)

         
    def add_note(self):
         memo = input("Enter a memo:")
         self.notebook.new_note(memo)
         print("Your note has been added.")

    def show_notes(self, notes=None):
         if not notes:self.notebook.notes.getNotes()
         for note in self.notebook.notes.getNotes():
             print("{0}: {1}\n{2}".format(note.getId(), note.memo, note.tags)







                   
    def search_notes(self):
                   filter = input("Search for:")
                   notes = self.notebook.search(filter)
                   self.show_notes(notes)

    def modify_note(self):
        id = int(input("Enter a bote id: "))
        memo = input ("Enter a memo: ")
        tags = input ("Enter tags: ")
                   if memo:
                   self.notebook.modifay_memo(id, memo)
                   if tags:
                   self.notebook.modifay_tags(id, memo)






menu= Menu()
menu.run()


                






     
                    

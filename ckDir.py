import os 

# check working directory
def display_cwd():
   cwd = os.getcwd()
   print("Current Working Directory: ", cwd)

# moves up one directory in cmd
def up_one_directory_level():
   os.chdir("../")

# Returns an iterator of all files in inputed directory
def display_entries_in_directory(directory):
   with os.scandir(directory) as entries: 
      for entry in entries:
         print(entry.name)

if __name__ == "__main__":
    display_cwd()
    up_one_directory_level()
    display_cwd()
    display_entries_in_directory("LinkedLearn/")
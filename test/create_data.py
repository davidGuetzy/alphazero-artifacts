# create_data.py
# A script to test the artifactory is working correctly

import os
from datetime import datetime 

def test_commit_file():
    # Grab original information and determine the working directory
    original_dir = os.getcwd()
    working_dir = os.getcwd().split('alphazero')[0] + 'alphazero/play_data/test'
    os.chdir(working_dir)

    # Get the current time for the commit message
    current_time = datetime.now().strftime("%D %H:%M:%S")

    os.system("git pull")
    # alter the file
    with open("test_file.txt", "a") as file:
        file.write('Running the test \n')

    # add, commit, & push the file
    print("Committing a file at " + str(current_time))
    os.system('git add test_file.txt')
    os.system('git commit -m "'+ str(current_time) + ': Running Test"')
    os.system("git push")
    print("File Successfully Pushed")
    os.chdir(original_dir)


if __name__ == "__main__":
    test_commit_file()
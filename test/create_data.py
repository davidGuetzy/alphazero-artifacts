# create_data.py
# A script to test the artifactory is working correctly

import os
from datetime import datetime 

def test_commit_file():
    original_dir = os.getcwd()
    working_dir = os.getcwd().split('alphazero')[0] + 'alphazero/play_data/test'
    os.chdir(working_dir)

    current_time = datetime.now().strftime("%D %H:%M:%S")

    os.system("echo Committing a file at " + str(current_time))
    # os.system('git add test_file.txt')
    os.system('git status')
    with open("test_file.txt", "a") as file:
        file.write('Running the test \n')

    os.system("echo Created a new file?")
    os.chdir(original_dir)


if __name__ == "__main__":
    test_commit_file()
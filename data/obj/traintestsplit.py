import glob, os
# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
cwd = os.getcwd()
os.chdir('../')
cwd = os.getcwd()

print(cwd)
#current_dir = '/Users/mattokc35ibm.com/spacetech-PLASTICNET/7classdarknetyolo/darknet/data/obj'
# Percentage of images to be used for the test set
percentage_test = 20;
# Create and/or truncate train.txt and test.txt

file_train = open(str(cwd) + '/train.txt', 'w')
file_test = open(str(cwd) + '/test.txt', 'w')
"""
# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))
    if counter == index_test:
        counter = 1
        file_test.write("data/obj" + "/" + title + '.jpg' + "\n")
    else:
        file_train.write("data/obj" + "/" + title + '.jpg' + "\n")
        counter = counter + 1
"""      
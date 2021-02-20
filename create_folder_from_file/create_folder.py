import os


def tab_level(astr):
    """Count number of leading tabs in a string
    """
    return len(astr) - len(astr.lstrip('\t'))


def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except OSError:
        print("Creation of the directory %s failed" % dirname)
    else:
        print("Successfully created the directory %s " % dirname)


# base dir name
base_url = "./tutorial"
current_dir = base_url
previous_dir = base_url
previous_level = 0
current_level = 0
levels_dir = [base_url]

create_dir(base_url)

# Using readlines()
file1 = open('documentation_python.txt', 'r')
Lines = file1.readlines()

count = 0
# Strips the newline character
for line in Lines:
    previous_level = current_level
    current_level = tab_level(line)
    if current_level == previous_level:
        previous_dir = current_dir + "/" + line.strip()
        create_dir(previous_dir)
    elif current_level > previous_level:
        try:
            levels_dir[current_level] = previous_dir
        except IndexError:
            levels_dir.insert(current_level, previous_dir)
        print("#########################", levels_dir, "######################")
        current_dir = previous_dir
        previous_dir = current_dir + "/" + line.strip()
        create_dir(previous_dir)
    else:
        print("#########################", current_level, previous_level, "######################")
        current_dir = levels_dir[current_level]
        previous_dir = current_dir + "/" + line.strip()
        create_dir(previous_dir)

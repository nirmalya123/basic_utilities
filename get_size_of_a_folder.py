import os

input_path = '.'

#----------------------------------------------------------------------------
# Using inorder traversal technique
#----------------------------------------------------------------------------
def get_absolute_path(path):
    return os.path.abspath(os.path.realpath(path))
    # realpath() removes the links then abspath() returns the absolute path

def get_size(path):
    size = 0
    for t in os.listdir(path):
        name = get_absolute_path(os.path.join(get_absolute_path(path), t))
        if os.path.isfile(name):
            size = size + os.path.getsize(name)
        elif os.path.isdir(name):
            size = size + get_size(name)
        elif os.path.islink(name):
            pass
    return size

print('Size of {} using in order way {}'.format(input_path,get_size(input_path)))

#----------------------------------------------------------------------------
# Using os.walk()
#----------------------------------------------------------------------------
f_set = set()
for dirpath, dirnames, filenames in os.walk(input_path):
    for t in filenames:
        f_set.add(os.path.join(dirpath, t))
size = 0
for i in f_set:
    size = size + os.path.getsize(i)
print('Size of {} using os.walk {}'.format(input_path,size))


#----------------------------------------------------------------------------
# Some other utilities
#----------------------------------------------------------------------------

# Filter files with .py extenstions
print(filter(lambda x: x.endswith('.py'),os.listdir(input_path)))
print([x for x in os.listdir(input_path) if x.endswith('.py')])
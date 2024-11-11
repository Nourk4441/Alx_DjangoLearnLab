import os

# Replace '/path/to/LibraryProject' with your actual project path
project_path = '/path/to/LibraryProject'
manage_path = os.path.join(project_path, 'manage.py')

if os.path.isfile(manage_path):
    print("manage.py exists in the correct location.")
else:
    print("manage.py is missing or in the wrong location.")

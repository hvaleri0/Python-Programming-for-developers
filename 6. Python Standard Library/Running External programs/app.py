import subprocess

# old ways of working:
# subprocess.call
# subprocess.check_call
# subprocess.check_output

# new ways of working
# set capture_output to tru if you want to store in stdout:
# set text=True to convert output to string (default to binary)
completed = subprocess.run(["ls", "-l"], capture_output=True, text=True)
print("args", completed.args)  # arguments
print("returncode", completed.returncode)  # return code if 0 its successful
print("stderr", completed.stderr)  # std Error
print("stdout", completed.stdout)  # std Output

# How to run Child Process:
completed = subprocess.run(["python3", "other.py"],
                           capture_output=True, text=True)
print("args", completed.args)  # arguments
print("returncode", completed.returncode)  # Any non zero return is an error
print("stderr", completed.stderr)  # std Error
print("stdout", completed.stdout)  # std Output

# Testing the errors:
# set check=True so that method automatically raises an exception
try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)
    print("args", completed.args)  # arguments
    # Any non zero return is an error
    print("returncode", completed.returncode)
    print("stderr", completed.stderr)  # std Error
    print("stdout", completed.stdout)  # std Output
    # if completed.returncode != 0:
    #     print(completed.stderr)
except subprocess.CalledProcessError as ex:
    print(ex)

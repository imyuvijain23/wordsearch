from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your Python file
setup(
    name="YourAppName",
    version="0.1",
    description="Description of your app",
    executables=[Executable("gui.py")],
)

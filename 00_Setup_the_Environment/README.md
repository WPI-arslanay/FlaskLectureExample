---
## Setup Flask on your `localhost`
---
1. If you haven't yet, go ahead and install [Python](https://www.python.org/downloads/). (Your Python version should be 3.4.x or higher.)

      **Important** (Windows users):
      Please make sure to add the Python path to Windows Path. Read more [here](https://superuser.com/questions/143119/how-to-add-python-to-the-windows-path).
      Also, Windows installer now includes an option to add python.exe to the system search path. When you install Python, [select the "Add Python 3.x to PATH" option](https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=0ahUKEwit9NyWmafWAhXH44MKHaV9CfkQjRwIBw&url=https%3A%2F%2Floadbalancerblog.com%2Fblog%2F2015%2F11%2Fpython-35-install&psig=AFQjCNG10siDMl9gL49FY-3IQHICIPD2pw&ust=1505565091140981). If selected, the install directory will be added to your PATH.

      **Important** (Mac/Linux users): 
      Mac and Linux systems have Python 2.x installed already. When you type and run `python` on the terminal, it will run the Python2 interpreter. To launch Python 3, run `python3` and to run the `python3` installer run `pip3`.

2. Open a terminal or command line window. 
   Run the following commands to install `flask` and `flask-sqlalchemy`. 

    on `Windows`:
    ```
    pip install flask
    pip install flask-wtf
    pip install flask-sqlalchemy
    pip install python-dotenv
    ```
    on `Mac/Linux`:
    ```
    pip3 install flask
    pip3 install flask-wtf
    pip3 install flask-sqlalchemy
    pip3 install python-dotenv
    ```
  
    Note for Windows users: If `pip` is not installed in your system, you need to also add the Python\Scripts path to the Windows Path. On Windows, Python will typically be installed under the directory `C:\Users\<username>\AppData\Local\Programs\Python\Python3.x`. Locate your Python installation directory, make sure `pip` or `pip3` is under the `Scripts` directory, and add the "path of Scripts directory" to the Path environment variable. 

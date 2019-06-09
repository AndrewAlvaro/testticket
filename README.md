# testticket
-----Installation-----

Install Homebrew...
- Open terminal
- Install homebrew with the following command "curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
- Add this line "export PATH="/usr/local/opt/python/libexec/bin:$PATH" into the ~/profile file

Install Python3...
- Install Python3 with the following command "brew install python3"
- Make sure that Python3 is installed not Python2, as Python2 will soon be obselete. You can check the version by running command "python --version" or just running a command with "python3 [some command]" to ensure you are using Python3 all the time

-----Installing modules-----
- Run the command "pip3 install flask"
- Run the command "pip3 install zenpy"
- Run the command "pip3 install flack_paginate"

*Note that modules needs to be installed before running application, other error(s) might appear for other missing modules that needs to be installed before running application*

-----README-----

Once the following requirements have been installed, go to the directory 'Test ticket' on terminal and run the following command "python3 flask_main.py"(a popup message may come up for the application to connect incoming network traffic and just select 'allow'). Open a web browser and the input the following 'localhost:5000' address and it will direct you to the Ticket Viewer.
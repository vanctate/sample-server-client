How to run Server.py and Client.py 
    - ensure you have Python 3 installed, you can check by typing 'python --version' into your terminal 
    - navigate into 'sample-server-client' folder
    - in the terminal type 'python3 Server.py' to start the server 
    - open a new terminal and navigate into the 'sample-server-client' folder
    - type 'python3 Client.py' and you will be greeted with a menu of options
    - you can open a few other terminals and run clients that connect with the server 
    - when ready to quit first disconnect on the client and then press 'ctrl+c' to exit server 

known bugs:
    - if you cannot run server because the port is still active run this command in terminal
        - 'sudo lsof -i :5000'
        - (only need 'sudo' command if on macOS)

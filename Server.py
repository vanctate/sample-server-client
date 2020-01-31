from socket import socket, AF_INET, SOCK_STREAM  # sockets to connect to clients
import threading  # multi-thread the clients
import random # choosing a random greeting

# simple Server class that accepts multiple clients via localhost 5000
class Server:

    # socket to bind and listen for clients
    __serversocket = socket(AF_INET, SOCK_STREAM)
    # list of client connections, when client chooses to disconnect, connection is removed from list and connection is closed
    __connections = []
    __clients = []

    # default initializer, listen for clients on port 5000
    def __init__(self):
        self.__serversocket.bind(('localhost', 5000))
        self.__serversocket.listen(5)
        self.__connections = []
        self.__clients = []

    def getClients(self):
        return self.__clients

    def addClient(self, user):
        self.__clients.append(user)

    # only function we need to call to start the server while it listens for clients
    def run(self):
        # listen for client connections
        while True:
            # accept connection from client and add to list of connections
            connection, address = self.__serversocket.accept()
            self.__connections.append(connection)
            # thread for this connection, call self.handler() function
            cthread = threading.Thread(
                target=self.handler, args=(connection, address))
            cthread.daemon = True
            cthread.start()
            # print the address for reference
            print(str(address[0]) + ':' + str(address[1]) + " connected\n")

    # calls initialMenu(connection, address) function to display the first menu to the user
    def handler(self, connection, address):
        self.initialMenu(connection, address)

    # first menu client/user sees when connecting to server
    # takes connection and address variables from serversocket.accept() function in run(self)
    def initialMenu(self, connection, address):
        while True:
            initialMsg = " ** Welcome to the Sample Server, choose an option below ***\n" \
                         "1: receive random a greeting from different languages\n" \
                         "2: sign in\n" \
                         "3: disconnect\n"
 
            connection.send(bytes(initialMsg, 'utf-8')) # send menu message to user       
            data = connection.recv(1024) # receive input from the user on which option
            clientOption1 = str(data, 'utf-8') # convert client input to string
            print('address : ' + str(address))

            # switch on user input option
            if clientOption1 == "1":     
                print("client chose receive greeting\n") # print message on server for reference

                greetings = ['Konbonwa', 'Howdy', 'Bonjour', 'Hey there', 'Konnichiwa', 'Salut', 'Ciao',
                'Hola', 'Sawasdee', 'Namaste', 'Guten tag']
                random.shuffle(greetings)
                randomGreeting = greetings[0] + ' to you client, thank you for connecting\n'

                # send random greeting back to client back to client
                connection.send(bytes(randomGreeting, 'utf-8'))

            elif clientOption1 == "2":
                print("client chose sign in")
                # break
                #self.signIn(connection, address)

            # remove client from list of connections and close connection
            elif clientOption1 == "3":
                connection.send(bytes('you will now be disconnected\n', 'utf-8'))
                #connection.shutdown(address[0])
                connection.close()
                #self.__serversocket.close(address[1])
                print(str(address[1]))
                self.__connections.remove(connection)
                print(str(address[0]) + ':' +
                      str(address[1]) + " disconnected")
                
                break

            # default catch
            else:
                invalidInput = "*** invalid input, try again\n"
                print(invalidInput)
                connection.send(bytes(invalidInput, 'utf-8'))

            # this is a catch if there is no more connections of data incoming
            if not data:
                # self.connections.remove(connection)
                print(str(address[0]) + ':' +
                      str(address[1]) + " disconnected")
                connection.close()
                break


# instantiate Server object
server = Server()
# run the whole party
server.run()

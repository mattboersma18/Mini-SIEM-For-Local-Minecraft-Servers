# Mini-SIEM-For-Local-Minecraft-Servers
This project is a project designed to monitor and track activity in a Minecraft server. This program tracks different types of data and alerts the user of any issues potentially going on with the server.

To start, we have to get the program to actually read what is going on inside of the server, were going to use two different pythong imports in order to do this, paramiko and dotnv

Paramiko is a open source library that I will be using to connect directly to the server, it allows the code to connect directly via SSHv2 which is exactly what I want. This makes sure that we have direct contact with the server, and that we dont have to go through multiple mediums in order to check on our server.

Dotenv is a library that allows us to load configuration settings safely, without anyone seeing them. We can create a .env file with sensitive information and the program will automatically withdraw information from that file. API keys, passwords, usernames, IP addresses are just some of the things that we can keep secure inside of a .env file.

(ADD ANY MORE LIBRARIES HERE)

The actual code starts in main with setting up all of our connection variables, such as the Host, port, username, etc. Then the code initiates a connection to the ssh server with out .env file information. If something goes wrong, and the server cannot connect, then the connection will time out.

We then run a command to read the system from our connection. If successful, the program will give a success message, then it will begin reading the logs coming from the actual server system.


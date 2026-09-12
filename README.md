# Mini-SIEM-For-Local-Minecraft-Servers
This project is a project designed to monitor and track activity in a Minecraft server. This program tracks different types of data and alerts the user of any issues potentially going on with the server.

To start, we have to get the program to actually read what is going on inside of the server, were going to use two different pythong imports in order to do this, paramiko and dotnv

Paramiko is a open source library that I will be using to connect directly to the server, it allows the code to connect directly via SSHv2 which is exactly what I want. This makes sure that we have direct contact with the server, and that we dont have to go through multiple mediums in order to check on our server.

Dotenv is a library that allows us to load configuration settings safely, without anyone seeing them. We can create a .env file with sensitive information and the program will automatically withdraw information from that file. API keys, passwords, usernames, IP addresses are just some of the things that we can keep secure inside of a .env file.

(ADD ANY MORE LIBRARIES HERE)

The actual code starts in main with setting up all of our connection variables, such as the Host, port, username, etc. Then the code initiates a connection to the ssh server with out .env file information. If something goes wrong, and the server cannot connect, then the connection will time out.

We then run a command to read the system from our connection. If successful, the program will give a success message, then it will begin reading the logs coming from the actual server system. The actual logs coming from the server are a little difficult to read, so the parser.py file takes the logs and makes them more readible. This file takes in the logs, recompiles them to a more readible format, then displays it as a parser.

All of the tracking and rules for the file goes into the rules.py file, where each server rule is coded. The first rule is a rapid reconnect alert. The code keeps a history every 30 seconds of connections and disconnects. If a user at a IP address is rapidly connecting and reconnecting, then the server will show an alert to the terminal, displaying that there may be an active rapid reconnect attack.

(ADD MORE RULES HERE)

Lessons Learned:
This project has taught me many lessons and showed me valueable insight on what specific security software uses to track attackers and maintain system security. (ADD MORE LESSONS HERE)

Although there are many things Id like to add to this project, Id love to make the display more clean and not run out of a terminal. (ADD MORE IMPROVEMENTS HERE)



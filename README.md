# Assignment 4 - Infiltrating the Government in an Alternative Universe


## Strucutre
Different script for the different levels will be found in the levels folder, and the files should be named accordingly <br> 

# Intranet: Level 1
- Jonas Dahl frequently logs in to check his Wireguard credentials.
- Discord WEBHOOKS can be very useful here.<br> </br> 
- Consider using the webhook to send data to yourself when Jonas Dahl logs in.<br> </br>  
- Keep an eye out for information about Jonas' supervisor. She might have more access than Jonas.<br> </br>  
# Intranet: Level 2
You need to access the network on Wireguard. You'll retrieve this on Intranet: Level 1.
nmap is a great tool for service discovery. Perhaps you can check which ports are open?
## SSH
The SSH Server only accepts public-key authentication. You need to do something before accessing this server. 
What if we could overwrite the authorized_keys file somehow?<br> </br> 
Use ssh-rsa keys.<br> </br> 
## Dropbox
Consider how Dropbox could be used to gain access to SSH.<br> </br> 
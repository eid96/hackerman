# Pre requestis for 4 attack: 
- Need to find open ports, per hint ports conencted to 10.13.13.254
    - Done by installing wireguard and configure per "options"
    - Install wsl 
    - run following commands: 
      - apk update
      - apk add nmap
      - nmap 10.13.13.0/24
    - If done right: port 80/tcp open http 
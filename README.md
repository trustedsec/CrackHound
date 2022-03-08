## CrackHound - introduce plain text passwords to da hound.

This tool has a corresponding blogpost which can be found here:
https://www.trustedsec.com/blog/expanding-the-hound-introducing-plaintext-field-to-compromised-accounts/

CrackHound is a way to introduce plain-text passwords into BloodHound. 
This allows you to upload all your cracked hashes to the Neo4j database and use it for reporting purposes (csv exports) or path finding in BloodHound using custom queries.
In this repository you will find two items:
* `customqueries.json` - These are example cypherqueries that you can use in your BloodHound GUI, feel free to expand upon these.
* `crackhound.py` - The core of this repository. This script allows you to make the necessary edits to the Neo4j database


### Usage
```
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0xl:,'.........',,:oOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dl:;,,,,;;;::::::;;;,''',:okKWMMMMMWWWNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNXWMMMMMMMMMMWXkl;,,;::ccccccccccccccccccc;.   .,collcccc:ccldOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNOl:dXMMMMMMMMW0o;',:cc;..':cccccccccccccccccc:.    ..',;::::::;,,;o0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl' .lNMMMMMMMMXo'';:ccc:.   ':cccccccccccccccccc:'.',:cccc::ccccccc:,,oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMKc.  .oNMMMMMMWXx;';:ccccc:,.   ..';:cccccccc:ccccccccccc:;'...;cccccccc;':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:   .oNMMMMWKxc'.':ccccccccc;.      ..',,'..';:ccccccccc:,     .;cccccccc:';OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. .cONMNKkl;.   .:ccccccccccc;.            .,::cccccccccc;.     .;cccccccc:',kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMx. 'dkdc,.       .:ccccccc:;,,,.           .,cccccccccccccc'      .,::cccccc:''dNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMXo.     .''.  .';:cccccc:,.               .;ccccccccccccc:,.        ...':cccc:,'cxkk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxdodk0Oc'';:cccccccc:,.       .ox;    .;ccccc:::c:;'...              .....';;'....:ONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0;.;cccccccccc:,.       'kWMXo. .:ccccc:,....                       .','......';xWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK:.;cccccccccc:'        ;0WMMM0, ..''',,,;;;,'...     'lc.        .,;:;''',,'... .oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKkl' .;:ccc:;;,,'.       .oXMMMMWo   .......,::::::;,'...dWWO,      ':ccc;,,;;...''...;OWMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd.     .,:c;',:.       .:kXWMMMMMW0l;,,;;;.............,;.'kWW0;    ':cc:'. .;:;,'......oNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.  .....'''.;0WKx:.     .:xKWMMMMMMMWWNNXd.       .;o; .::.;KMMK: .,:ccc,. ';,..    .. ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo.     ':loodkXMMMMWXOo;.    .:OWMMMMMMMMWk.     .;d00kc. .,.:KMMXc.,:ccc:. .;:,,'.  ';,..;0WMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMKc     ,xXWMMMMMMMMMMMMMMNOl.    '0MMMMMMMWk.     ;ONMK:      ,OMMNl.,:cccc,   ..,;cc,..:c:,.,dKWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMWO,    .oXMMMMMMMMMMMMMMMMNo'.     cXMMMMMMNx.    .lXMMX:      :0MMXl.,ccccc;.      .;c:;;:cc::,''oNMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMKc.    .xWMMMMMMMMMMMMMMMMKc.     .lXMMMMMWKc.   .,dNMMMNx;.',ckNMWK:.;ccccc:'        .';:ccc:,... ;XMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWo.     .coxKMMMMMMMMMMMMMMk.     'xNMMMMMMX:     ckONMMMMMWNNWWMWXd'.;cccccc;..;.      ..';:,','. .dWMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMX:       ...;0MMMMMMMMMMMMMW0doloxKWMMMMMMNo.       .:KMMMMMMMWXkl'..;cccccc:'.oN0,    ..';;,,',. .dWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKc.   .'.',.;0MMMMMMMMMMMMMMMMMMMMMMMMMMMXc          ;0MMMMMXo,.',,;::::::;,.;KNk,  ....,:;,;'....kMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMXl....'..'.,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMXl.........'dWMMMM0:.',,,,,,,,,,'':OWXc..,,;;,;,,;,':O00NMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWXKKXKKKKKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXXXXXXXXXXWMMMMMMNXXXXXXXXXXXXXXWMMMNXXXXXXXXXXXXXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM

                                                            CRACKHOUND - jfmaes
    
usage: crackhound.py [-h] [-f FILE] [-url URL] [-u USERNAME] [-p PASSWORD] [-plaintext] [-addpw] [-v] [-d DOMAIN]

update bloodhound database with pwned users

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  file with list of all users you have compromised
  -url URL, --url URL   the neo4j url to auth to (defaults to bolt://localhost:7687)
  -u USERNAME, --username USERNAME
                        username to login to neo4j (defaults to neo4j)
  -p PASSWORD, --password PASSWORD
                        password to login to neo4j (defaults to bloodhound)
  -plaintext, --plain-text
                        adds plaintext property to compromised user to help with custom queries
  -addpw, --add-password
                        adds the actual plain text password to the bloodhound data as well
  -v, --verbose         verbose
  -d DOMAIN, --domain DOMAIN, -fqdn DOMAIN
                        the domain name of client in case its different than netbiosname
                                                                                                                                                                 
```

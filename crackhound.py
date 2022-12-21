#!/usr/bin/env python

import argparse
import os
import string
import neo4j


def banner():
    print(r"""
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
    """)


def parse_compromised_users(file, type):
    compromised_users = []

    # Trying to open file specified on command line
    try:
        os.path.exists(file)
        f = open(file, "r")

    # If file doesn't exist, exit with exception
    except Exception as a:
        print(f"{file} is not valid or doesn't exist!")
        exit()

    else:
        lines = f.readlines()
        for line in lines:
            user_dict = {}
            line = line.strip()
            if type == "plaintext":
                if ":" in line:
                    split = line.split(":")
                    compromised_user = split[0]
                    user_dict["password"] = split[2]
                else:
                    compromised_user = line
                user_dict["username"] = compromised_user
                compromised_users.append(user_dict)

            elif type.upper() == "NTDS":
                if ":" in line:
                    split = line.split(":")
                    compromised_user = split[0]
                    user_dict["NT"] = split[3]
                else:
                    compromised_user = line
                user_dict["username"] = compromised_user
                compromised_users.append(user_dict)
        return compromised_users


def format_compromised_users(compromised_users, domain, type):
    for user in compromised_users:
        user["username"] = user["username"].upper()
        if "\\" in user["username"]:
            split = user["username"].split("\\")
            if domain:
                user["username"] = split[1] + "@" + domain
            else:
                user["username"] = split[1] + "@" + split[0]
        else:
            pass
    return compromised_users


def update_database(compromised_users, url, username, password, plaintext, verbose, add_password, type):
    try:
        print(
            "Connecting to neo4j on {} with username {} and password {} ".format(
                url, username, password
            )
        )

        try:
            db_conn = neo4j.GraphDatabase.driver(
                url, auth=(username, password), encrypted=False
            )
        except Exception:
            print("Couldn't connect to database.")
        else:
            print("Connection success!")

        for user in compromised_users:
            try:
                with db_conn.session() as session:

                    # If plaintext not specified, simply mark user as owned in BH
                    if type.upper() == "NTDS":
                        tx = session.run("match (u:User) where u.name=\"{0}\" set u.nthash=\"{1}\" set u.plaintext=False set u.owned=True".format(
                                user["username"], user["NT"]
                            )
                        )
                        if verbose:
                            print("added NT hash of {0} and marked as owned.".format(
                               user["username"]
                            )
                        )
                    #this could be optional?
                    elif type == "plaintext":
                        if not plaintext:
                            tx = session.run(
                                "match (u:User) where u.name=\"{0}\" set u.owned=True set u.plaintext=False".format(
                                   user["username"]
                                )
                            )
                            if verbose:
                                print("{0} successfully marked as owned!".format(
                                   tx.single()[0]
                                )
                            )
                    #till here?
                        elif add_password:
                            if user["password"]:
                                tx = session.run(
                                    "match (u:User) where u.name=\"{0}\" set u.plaintextpassword=\"{1}\" set u.owned=True set u.plaintext=True".format(
                                       user["username"], user["password"]
                                    )
                                )
                                if verbose:
                                    print("added plaintext password of {0} and marked as owned.".format(
                                       user["username"]
                                    )
                                )
                            else:
                                continue
                        else:
                            tx = session.run(
                                "match (u:User) where u.name=\"{0}\" set u.owned=True set u.plaintext=True".format(
                                    user["username"]
                                )
                            )
                            if verbose:
                                print("{0} successfully marked as owned and marked as plaintext!".format(
                                tx.single()[0]
                                )
                            )
            except Exception as e:
                print(e)
                continue
                session.close()

    except Exception as e:
        print(f"An error occured {e}")

def main():
    parser = argparse.ArgumentParser(
        description="Update bloodhound database with pwned users"
    )
    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="File with list of all users you have compromised. Supports DOMAIN.COM\\USER:NTHASH:PASS or DOMAIN.COM\\USER",
    )
    parser.add_argument(
        '-t',
        '--type',
        required=False,
        help="File with [plaintext] or [NTDS]",
        default="plaintext"
    )
    parser.add_argument(
        "-url",
        "--url",
        required=False,
        help="The neo4j url to auth to (defaults to bolt://localhost:7687)",
        default="bolt://localhost:7687",
    )
    parser.add_argument(
        "-u",
        "--username",
        required=False,
        help="Username to login to neo4j (defaults to neo4j)",
        default="neo4j",
    )
    parser.add_argument(
        "-p",
        "--password",
        required=False,
        help="Password to login to neo4j (defaults to bloodhound)",
        default="bloodhound",
    )
    parser.add_argument(
        "-plaintext",
        "--plain-text",
        required=False,
        help="Adds plaintext property to compromised user to help with custom queries",
        default=False,
        action="store_true",
    )
    parser.add_argument(
        "-addpw",
        "--add-password",
        action="store_true",
        required=False,
        default=False,
        help="Adds the actual plain text password to the bloodhound data as well",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        required=False,
        default=False,
        help="verbose",
        action="store_true",
    )
    parser.add_argument(
        "-d",
        "--domain",
        "-fqdn",
        required=False,
        default="",
        help="The domain name of client in case its different than netbiosname. It very likely will be different. Check your secretsdump for more info.",
    )
    parser.add_argument(
        "-s",
        "--silent",
        required=False,
        action="store_true",
        help="Don't show ascii art ;)",
    )
    args = parser.parse_args()

    if args.silent:
        pass
    else:
        banner()

    compromised_users = parse_compromised_users(args.file, args.type)
    compromised_users = format_compromised_users(compromised_users, args.domain, args.type)

    print("Updating database, could take a while...")

    update_database(
        compromised_users,
        args.url,
        args.username,
        args.password,
        args.plain_text,
        args.verbose,
        args.add_password,
        args.type,
    )

    print("All Done!")


if __name__ == "__main__":
    main()

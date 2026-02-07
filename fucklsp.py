
# FuckLSP Utilities
# By suaminyafreya<3

import interface

# system functions

class system:

    def change_hostname(filepath, hostname):

        interface.print_process(context="Changing hostname", stat=6)
        import os

        if(os.name == 'nt'):
            interface.print_process(context="'nt' detected, not changing hostname", stat=1)

        elif(os.name == 'posix'):
            system.write_single(filepath=filepath, content=(hostname))
            interface.print_process(context="Hostname changed", stat=1)

        else:
            interface.print_process(context="Unknown OS", stat=10)

    def check_system_environment():

        interface.print_process(context="Checking OS environment", stat=7)

        import os

        if(os.name == 'nt'):
            interface.print_process(context="Windows (nt) detected", stat=1)
            return "demo"
        
        elif(os.name == 'posix'):
            interface.print_process(context="Debian (posix) detected", stat=1)
            return "compatible"
        
        else:
            interface.print_process(context="Unknown OS detected", stat=0)
            return "incompatible"

    def find_system_address():

        interface.print_process(context="Finding system address", stat=6)

        import socket
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        interface.print_process(context="Connecting to '8.8.8.8' to get hostname", stat=6)
        client.connect(("8.8.8.8", 80))

        interface.print_process(context="Getting hostname", stat=6)
        address = client.getsockname()[0]

        interface.print_process(context="Hostname has been found", stat=1)
        interface.print_process(context="Returning address", stat=6)

        return str(address)

    def split_address(address):

        interface.print_process(context="Splitting address into array", stat=6)

        address_listed = []
        address_list = ""
        for octet in address:

            if(octet == '.'):
                address_listed.append(address_list)
                address_list = ""

            if(octet != '.'):
                address_list += octet

        address_listed.append(address_list)

        return address_listed

    def check_address_validation(address):

        interface.print_process(context="Checking address syntax validation", stat=7)

        import string

        limit = 0
        seq = True
        vald = 0
        vald1 = False
        vald2 = False
        vald3 = 0
        vald4 = False

        strnum = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')


        if(address == ''):
            interface.print_process(context="The address cannot have an empty string", stat=0)
            return False

        for char in address:

            if(char in strnum or char == '.'):
                vald1 = True


            else:
                interface.print_process(context="The address has incorrect spelling", stat=0)
                interface.print_process(context=f"The address contains prohibited '{char}' character in address string", stat=0)
                vald1 = False
                break

        if(vald1):
            interface.print_process(context="The address has correct spelling", stat=1)

        for char in address:

            if(char == '.' and vald <= 3 and limit != 4):
                vald +=1
                limit +=1


        if(vald == 3):
            interface.print_process(context="The address has the enough required dots", stat=1)
            vald2 = True

        elif(vald > 3):
            interface.print_process(context="The address has required too many dots", stat=0)
            interface.print_process(context=f"Extra {vald - 3} dot", stat=0)
            vald2 = False

        elif(vald < 3):
            interface.print_process(context="The address has not required enough dots", stat=0)
            interface.print_process(context=f"Missing {3 - vald} dot", stat=0)
            vald2 = False
            
            limit += 1

        for char in address:

            if(char != '.' and seq):
                vald3 += 1
                seq = False

            if(char == '.'):
                seq = True


        if(vald3 < 4):
            interface.print_process(context="The address structure is incorrect", stat=0)
            interface.print_process(context="Missing octet after '.'", stat=0)
            vald4 = False

        else:
            interface.print_process(context="The address has correct structure", stat=1)
            vald4 = True

        return(True if vald1 and vald2 and vald4 else False)
            
    def check_domain_validation(domain):

        interface.print_process(context="Checking domain syntax validation", stat=7)

        import string

        vald = 0
        vald1 = False
        vald2 = False
        vald3 = False
        seq = True

        if(domain == ''):
            interface.print_process(context="Domain cannot have an empty string", stat=0)
            return False
        
        for char in domain:

            if(char in string.ascii_lowercase or char == '.'):
                vald1= True

            elif(char in string.punctuation):
                vald1 = False
                break

        if(vald1):
            interface.print_process(context="Domain has correct spelling", stat=1)
        
        else:
            interface.print_process(context="Domain has incorrect spelling", stat=0)
            interface.print_process(context=f"Domain contains prohibited '{char}' in domain string", stat=0)

        if('.' in domain):
            interface.print_process(context="Domain has correct syntax", stat=1)
            vald2= True

        else:
            interface.print_process(context="Domain has incorrect syntax", stat=0)
            interface.print_process(context="Missing '.' in domain string", stat=0)
            vald2 = False

        for letter in domain:

            if(letter != '.' and seq):
                vald += 1
                seq = False

            if(letter == '.'):
                seq = True


        if(vald <= 1):
            interface.print_process(context="Domain has incorrect structure", stat=0)
            interface.print_process(context="Missing name after '.'", stat=0)
            vald3 = False

        else:
            interface.print_process(context="Domain has correct structure", stat=1)
            vald3 = True
        
        return (True if vald1 and vald2 and vald3 else False)

    def check_netmask_classC(netmask):
        
        import string

        int_netmask = []

        vald0 = False
        vald1 = False
        vald2 = False
        vald3 = False

        oct = ''
        for x in netmask:
            if(x == '.'):
                int_netmask.append(int(oct))
                oct = ''
            else:
                oct += x

        int_netmask.append(int(oct))

        try:

            if(int_netmask[0] <= 255):
                vald0 = True

            if(int_netmask[1] <= 255):
                vald1 = True

            if(int_netmask[2] <= 255):
                vald2 = True

            if(int_netmask[3] <= 255):
                vald3 =True

        except Exception:
            return False

        return(True if vald0 and vald1 and vald2 and vald3 else False)

    def write(filepath, content):

        with open(filepath, 'w') as file:
            
            i = 0
            for line in content:
                file.write(f"{content[i]}\n")
                i += 1

    def write_single(filepath, content):

        with open(filepath, 'w') as file:
            
            file.write(f"{content}")

    def change_resolv(filepath, nameservers):

        interface.print_process(context="Changing resolv.conf with embedded one", stat=2)
        system.write(filepath=filepath, content=nameservers)
        interface.print_process(context="resolv.conf changed successfuly", stat=1)

    def check_network_conf():

        import subprocess
        import os

        if (os.name == 'nt'):
            interface.print_process(context="Windows (nt) detected", stat=1)
            interface.print_process(context="Skipping net port checking", stat=1)

            return ("vdeth0")

        elif(os.name == 'posix'):
            interface.print_process(context="Debian (posix) detected", stat=1)
            interface.print_process(context="Checking available net port", stat= 6)

            import subprocess

            netslot = subprocess.run('ip a', text=True, shell=True, capture_output=True)
            netslot = netslot.stdout

            newline = ''
            resultarr = []
            netslotarr = []
            strippeds = []
            final = []

            for line in netslot:


                    if(line != '\n'):
                            newline += line

                    elif(line == '\n'):
                            resultarr.append(newline)
                            newline = ''

            i = 0
            for result in resultarr:

                    if(len(resultarr) > i):
                            netslotarr.append(resultarr[i])
                            i += 6
                    else:
                            break

            r = ''
            for line in netslotarr:

                    for char in line:

                            if(char != '<'):
                                    r += char

                            else:
                                    strippeds.append(r.strip(":1234567890"))
                                    r = ''
                                    break

            for line in strippeds:
                    xs = ''

                    for x in line:

                            if(x != ':'):
                                    xs += x

                            else:
                                    final.append(xs.strip())
                                    break

                    else:
                        None

            interface.print_process(context=f"slot name available {final}", stat= 1)
            return final

        else:
            interface.print_process(context="Unknown OS name", stat=0)

    def set_dhcp_address(netslot, filepath, capture):

        to_write = []

        interface.print_process(context="Setting DHCP address", stat=6)

        for x in netslot:
            
            if(x == 'lo'):
                 
                 to_write.append("auto lo\niface lo inet loopback\n")

            else:
                 
                 to_write.append(f"allow-hotplug {x}\niface {x} inet dhcp")

        system.write(filepath=filepath, content=to_write)

        if(capture):
            return "dhcp", "dhcp", "dhcp", "dhcp"
        else:
            None

    def set_static_address(netslot, filepath, capture):

        to_write = []

        interface.print_process(context="Setting static address", stat=6)

        for x in netslot:
            
            if(x == 'lo'):
                 
                 to_write.append("auto lo\niface lo inet loopback\n")

            else:
                print(f"Enter following properties for {x} :")
                while(True):
                    address = interface.fancy_input(context="Enter IP address :")
                    if(system.check_address_validation(address=address)):
                        break
                    else:
                        interface.print_process(context="Invalid address", stat=0)
                while(True):
                    netmask = interface.fancy_input(context="Enter address netmask :")
                    if(system.check_netmask_classC(netmask=netmask)):
                        break
                    else:
                        interface.print_process(context="Invalid netmask", stat=0)
                while(True):
                    gateway = interface.fancy_input(context="Enter address gateway :")
                    if(system.check_address_validation(address=gateway)):
                        break
                    else:
                        interface.print_process(context="Invalid gateway", stat=0)
                while(True):
                    dns = interface.fancy_input(context="Enter address nameserver :")
                    if(system.check_address_validation(address=dns)):
                        break
                    else:
                        interface.print_process(context="Invalid nameserver", stat=0)
                 
                to_write.append(f"allow-hotplug {x}\niface {x} inet static\n\taddress {address}\n\tnetmask {netmask}\n\tgateway {gateway}\n\tdns-nameservers {dns}")
        
        system.write(filepath=filepath, content=to_write)

        if(capture):
            return address, netmask, gateway, dns
        else:
            None

    def check_hostname_validation(hostname):

        import string
        exc = []

        for x in string.punctuation:
            if(x == '-'):
                None
            else:
                exc.append(x)

        if(hostname == ''):
            interface.print_process(context=f"Hostname cannot be empty", stat=0)
            vald0 = False

        else:
            interface.print_process(context=f"Hostname has name", stat=1)
            vald0 = True

        for x in hostname:
            if(x in exc):
                interface.print_process(context=f"Hostname cannot contain the following characters :", stat=0)
                interface.print_process(context=f"{exc}", stat=0)
                vald1 = False
                break

            else:
                vald1 = True
        if(vald1):
            interface.print_process(context="Karakter hostname valid", stat=1)

        if(len(hostname) < 2):
            interface.print_process(context=f"Hostname tidak boleh memiliki kurang dari 2 karakter", stat=0)
            vald2 = False

        else:
            interface.print_process(context=f"Hostname memiliki jumlah karakter valid", stat=1)
            vald2 = True

        return(True if vald0 and vald1 and vald2 else False)
    
    def os_reboot():
        
        import os
        import subprocess

        if(os.name == 'nt'):
            interface.print_process(context="'nt' detected, not rebooting", stat=1)

        elif(os.name == 'posix'):
            interface.timer(context="OS will reboot in :", stat=3, time=3)
            interface.print_process(context="Rebooting now", stat=1)
            subprocess.run('reboot now', shell=True)

        else:
            interface.print_process(context="Unknown OS", stat=0)

    def restart_networking():

        import os
        import subprocess

        if(os.name == 'nt'):
            interface.print_process(context="'nt' detected, skipping networking restart", stat=1)

        elif(os.name == 'posix'):
            interface.print_process(context="This proccess might shut your ssh or any other network connections", stat=8)
            interface.print_process(context="Restarting network.service", stat=6)
            subprocess.run('systemctl restart networking', shell=True)

        else:
            interface.print_process(context="Unknown OS", stat=0)

# Bind9

class bind9:

    def make_db_domain(address, domain, db_path):

        interface.print_process(context=f"Making {db_path} with {domain} as domain and {address[0]}.{address[1]}.{address[2]}.{address[3]} as address", stat=2)

        content = (
        f';',
        f'; bind9 data file for local loopback interface',
        f';',
        f'$TTL    604800',
        f'@       IN      SOA     {domain}. root.{domain}. (',
        f'                            2         ; Serial',
        f'                        604800         ; Refresh',
        f'                        86400         ; Retry',
        f'                        2419200         ; Expire',
        f'                        604800 )       ; Negative Cache TTL',
        f';',
        f'@       IN      NS      {domain}.',
        f'@       IN      A       {address[0]}.{address[1]}.{address[2]}.{address[3]}')
        
        system.write(filepath=db_path, content=content)
        interface.print_process(context=f"{db_path} has been successfuly made with no errors", stat=1)

    def make_db_resolve(address, domain, db_path):

        interface.print_process(context=f"Making {db_path} with {domain} as domain and {address[0]}.{address[1]}.{address[2]}.{address[3]} as address", stat=2)

        content = (
        f';',
        f'; bind9 reverse data file for local loopback interface',
        f';',
        f'$TTL    604800',
        f'@       IN      SOA     {domain}. root.{domain}. (',
        f'                              1         ; Serial',
        f'                         604800         ; Refresh',
        f'                          86400         ; Retry',
        f'                        2419200         ; Expire',
        f'                         604800 )       ; Negative Cache TTL',
        f';',
        f'@       IN      NS      {domain}.',
        f'{address[3]}   IN      PTR     {domain}.')
        
        system.write(filepath=db_path, content=content)

        interface.print_process(context=f"{db_path} has been successfuly made with no errors", stat=1)

    def make_named_conf(address, domain, dbdomain_path, dbresolve_path, named_path):

        interface.print_process(context=f"Making {named_path}", stat=2)

        content = (
        f'// This is the primary configuration file for the bind9 DNS server named.',
        f'//',
        f'// Please read /usr/share/doc/bind/README.Debian.gz for information on the',
        f'// structure of bind9 configuration files in Debian, *BEFORE* you customize',
        f'// this configuration file.',
        f'//',
        f'// If you are just adding zones, please do that in /etc/bind9/named.conf.local',
        f'',
        f'include \"/etc/bind/named.conf.options\";',
        f'include \"/etc/bind/named.conf.local\";',
        f'include \"/etc/bind/named.conf.default-zones\";',
        f'',
        f'zone \"{domain}\" {{',
        f'type master;',
        f'file \"{dbdomain_path}\";',
        f'}};',
        f'',
        f'zone \"{address[2]}.{address[1]}.{address[0]}.in-addr.arpa\" {{',
        f'type master;',
        f'file \"{dbresolve_path}\";',
        f'}};')
        
        system.write(filepath=named_path, content=content)
        interface.print_process(context=f"{named_path} has been successfuly made with no errors", stat=1)

    def restart():
        
        interface.print_process(context="Restarting named.service", stat=6)

        import subprocess
        import os
        
        if(os.name == 'nt'):
            None
        else:
            subprocess.run("systemctl restart bind9", shell=True)
        
        interface.print_process(context="named.service restarted", stat=1)

    def check_installation():

        interface.print_process(context="Checking if bind9 is installed on the system", stat=7)

        import os
        import subprocess

        if(os.name == 'nt'):
            interface.print_process(context="Windows detected", stat=1)
            interface.print_process(context="Skipping installation checking", stat=1)
            return True

        else:
            
            interface.print_process(context="Linux detected", stat=1)

            while(True):
                interface.print_process(context="Checking bind9 installation", stat=7)
                check = subprocess.run(["dpkg-query", "-W", "-f=${Status}", "bind9"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)
                if("install ok installed" in check.stdout):
                    interface.print_process(context="bind9 is installed", stat=1)
                    return True
                
                else:
                    interface.print_process(context="bind9 is not installed", stat=8)
                    interface.print_process(context="Triggering 'apt update'", stat=6)

                    subprocess.run("apt update", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                    
                    interface.print_process(context="Triggering 'apt install bind9'", stat=6)
                    interface.print_process(context="Installing bind9", stat=6)
                    
                    subprocess.run("apt install bind9 -y", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                    
                    interface.print_process(context="Operation completed successsfuly", stat=1)
                    interface.print_process(context="Re-running installation check", stat=6)
    
# Apache2

class apache2:

    def make_siteconf(domain, documentroot, siteconf, port):

        interface.print_process(context=f"Making {siteconf} for {documentroot} with {domain} as ServerName with {port} as port", stat=2)

        content = (
                f'<VirtualHost *:{port}>',
                '   # The ServerName directive sets the request scheme, hostname and port that',
                '   # the server uses to identify itself. This is used when creating',
                '   # redirection URLs. In the context of virtual hosts, the ServerName',
                "   # specifies what hostname must appear in the request's Host: header to",
                '   # match this virtual host. For the default virtual host (this file) this',
                '   # value is not decisive as it is used as a last resort host regardless.',
                '   # However, you must set it for any further virtual host explicitly.',
                    f'ServerName {domain}',
                '',
                '   ServerAdmin webmaster@localhost',
                f'   DocumentRoot {documentroot}',
                '',
                '   # Available loglevels: trace8, ..., trace1, debug, info, notice, warn,',
                '   # error, crit, alert, emerg.',
                '   # It is also possible to configure the loglevel for particular',
                '   # modules, e.g.',
                '   #LogLevel info ssl:warn',
                '',
                f'   ErrorLog ${{APACHE_LOG_DIR}}/error.log',
                f'   CustomLog ${{APACHE_LOG_DIR}}/access.log combined',
                '',
                '   # For most configuration files from conf-available/, which are',
                '   # enabled or disabled at a global level, it is possible to',
                '   # include a line for only one particular virtual host. For example the',
                '   # following line enables the CGI configuration for this host only',
                '   # after it has been globally disabled with "a2disconf".',
                '   #Include conf-available/serve-cgi-bin.conf',
                '</VirtualHost>')
        
        system.write(filepath=siteconf, content=content)

        interface.print_process(context=f"{siteconf} has been successfuly made with no errors", stat=1)

    def make_siteconf_name(site):

        interface.print_process(context=f"Making siteconf name from {site}", stat=5)

        siteconfname = ''

        for letter in site:

            if(letter !='.'):
                siteconfname += letter

            if(letter == '.'):
                siteconfname += letter
                break

        interface.print_process(context=f"siteconf has been saved as {siteconfname + 'conf'}", stat=1)

        return siteconfname + 'conf'

    def import_site(site, documentroot):

        interface.print_process(context=f"Extracting {site} and exporting it to {documentroot}", stat=4)

        import zipfile as zip

        with zip.ZipFile(site, 'r') as sitezip:
            sitezip.extractall(documentroot)

        interface.print_process(context=f"Exporting succeeded", stat=1)

    def reload():

        interface.print_process(context="Reloading apache2", stat=6)

        import os
        import subprocess

        if(os.name == 'nt'):
            None

        else:
            subprocess.run("systemctl reload apache2", shell=True)

        interface.print_process(context="apache2 has been reloaded", stat=1)

    def enable_site(siteconf_name, linking_path):

        interface.print_process(context=f"Making filelink for {siteconf_name} to enable it", stat=6)

        import os
        import subprocess

        if(os.name == 'nt'):
            None
        
        else:
            subprocess.run(f"ln -s {siteconf_name} {linking_path}", shell=True)

        interface.print_process(context=f"{siteconf_name} has been linked as {linking_path}", stat=1)

    def check_webzip(site, siteszips):

        interface.print_process(context=f"Checking if {site} exist in {siteszips}", stat=7)

        import os

        if(os.path.exists(f"{siteszips}{site}")):
            interface.print_process(context=f"{site} does exist in {siteszips}", stat=1)
            return True
        
        else:
            interface.print_process(context=f"{site} does not exist in {siteszips}", stat=0)

    def check_installation():

        interface.print_process(context="Checking if apache2 is installed on the system", stat=7)

        import os
        import subprocess

        if(os.name == 'nt'):
            interface.print_process(context="Windows detected", stat=1)
            interface.print_process(context="Skipping installation checking", stat=1)
            return True

        else:
            
            interface.print_process(context="Linux detected", stat=1)

            while(True):
                interface.print_process(context="Checking apache2 installation", stat=7)
                check = subprocess.run(["dpkg-query", "-W", "-f=${Status}", "apache2"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True)

                if("install ok installed" in check.stdout):
                    interface.print_process(context="apache2 is installed", stat=1)
                    return True
                
                else:
                    interface.print_process(context="apache2 is not installed", stat=8)
                    interface.print_process(context="Triggering 'apt update'", stat=6)

                    subprocess.run("apt update", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                    
                    interface.print_process(context="Triggering 'apt install apache2'", stat=6)
                    interface.print_process(context="Installing apache2", stat=6)
                    
                    subprocess.run("apt install apache2 -y", stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, shell=True)
                    
                    interface.print_process(context="Operation completed successsfuly", stat=1)
                    interface.print_process(context="Re-running installation check", stat=6)

# Apt

class apt:

    def change_repository(filepath, repositories):

        interface.print_process(context="Changing sources.list with embedded one", stat=3)
        system.write(filepath=filepath, content=repositories)
        interface.print_process(context="sources.list changed successfuly", stat=1)

    def update_apt():

        import os
        import subprocess

        if(os.name == 'nt'):
            interface.print_process(context="Updating apt", stat=6)
            interface.print_process(context="apt updated successfuly", stat=1)

        elif(os.name == 'posix'):
            interface.print_process(context="Updating apt", stat=6)
            subprocess.run("apt update", stderr=subprocess.DEVNULL, stdout=subprocess.DEVNULL, shell=True)
            interface.print_process(context="apt updated successfuly", stat=1)

        else:
            interface.print_process(context="Unknown OS name", stat=6)
            interface.print_process(context="apt update failed", stat=6)

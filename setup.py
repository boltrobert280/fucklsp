
#   FuckLSP quicksetup
#   By suaminyafreya<3

import fucklsp
import interface

interface.clear_cli()
interface.print_asciiart()

# Check environment and set corresponding variables

print("Password root adalah : 123")
print("Ctrl + C untuk keluar secara paksa\n")

mode = fucklsp.system.check_system_environment()

if(mode == 'demo'):

    repositories = ("deb http://deb.debian.org/debian bullseye main contrib",
                    "deb http://security.debian.org/debian-security bullseye-security main contrib",
                    "deb-src http://security.debian.org/debian-security bullseye-security main contrib")
    apt_path = "./etc/apt/sources.list"
    resolv_path = "./etc/resolv.conf"
    resolv_names = ("nameserver 8.8.8.8\n", "nameserver 1.1.1.1\n")
    networkinterfaces = "./etc/network/interfaces"
    domain = ''
    address = ''
    db_domain = "./etc/bind/db.domain"
    db_resolve = "./etc/bind/db.resolve"
    named_conf = "./etc/bind/named.conf"
    siteconf_dir = "./etc/apache2/sites-available/"
    siteconf_en = "./etc/apache2/sites-enabled/"
    siteszips = './webzips/'
    sitezip = ''
    documentroot = "./var/www/fucklsp"
    port = 80
    hostname_path = './etc/hostname'
    hostname = ''

    runable = True

if(mode == 'compatible'):

    repositories = ("deb http://deb.debian.org/debian bullseye main contrib",
                    "deb http://security.debian.org/debian-security bullseye-security main contrib",
                    "deb-src http://security.debian.org/debian-security bullseye-security main contrib")
    apt_path = "/etc/apt/sources.list"
    resolv_path = "/etc/resolv.conf"
    resolv_names = ("nameserver 8.8.8.8\n", "nameserver 1.1.1.1\n")
    networkinterfaces = "/etc/network/interfaces"
    domain = ''
    address = ''
    db_domain = "/etc/bind/db.domain"
    db_resolve = "/etc/bind/db.resolve"
    named_conf = "/etc/bind/named.conf"
    siteconf_dir = "/etc/apache2/sites-available/"
    siteconf_en = "/etc/apache2/sites-enabled/"
    siteszips = './webzips/'
    sitezip = ''
    documentroot = "/var/www/fucklsp"
    port = 80
    hostname_path = '/etc/hostname'
    hostname = ''

    runable =True

if(mode == 'incompatible'):

    runable = False

# Main setup

if(runable):
    has_sitezip = True
    stage = 0

    while (runable):

        restarted = False

        # Setting up hostname

        if(stage == 0):
            while(True):
                hostname = interface.fancy_input(context="Masukkan nama hostname contoh 'Debian-Milik-Saya' :")

                if(fucklsp.system.check_hostname_validation(hostname=hostname)):
                    stage += 1
                    break

                else:
                    interface.print_process(context=f"Hostname tidak valid", stat=1)

        # Setting up system address

        if(stage == 1):
            while(True):
                usin = interface.fancy_input(context="Apa jenis IP Debian kamu? [Y/y] untuk DHCP [N/n] untuk Static :")

                if(usin in 'Yy'):
                    sys_addr, sys_netmask, sys_gateway, sys_dns = fucklsp.system.set_dhcp_address(netslot=fucklsp.system.check_network_conf(), filepath=networkinterfaces, capture=True)
                    stage += 1
                    break

                if(usin in 'Nn'):
                    sys_addr, sys_netmask, sys_gateway, sys_dns = fucklsp.system.set_static_address(netslot=fucklsp.system.check_network_conf(), filepath=networkinterfaces, capture=True)
                    stage += 1
                    break

                else:
                    interface.print_process(context="Input salah", stat=0)
                    interface.print_process(context="Masukkan jawaban antara [Y, y, N, n] ", stat=0)

        # Getting domain name

        if(stage == 2):
            while(True):
                domain = interface.fancy_input(context="Masukkan nama domain contoh 'suaminyafreyajkt48.lsp.tkj' :")

                if(fucklsp.system.check_domain_validation(domain=domain)):
                    stage += 1
                    break

                else:
                    interface.print_process(context="Nama domain tidak valid", stat=0)
                    interface.print_process(context="Masukkan nama domain lain", stat=0)

        # Getting system address

        if(stage == 3):
            while(True):
                usin = interface.fancy_input(context="Masukkan IP address secara otomatis atau manual? [Y/y] untuk otomatis [N/n] untuk manual :")

                if(usin in 'Yy'):
                    address = fucklsp.system.find_system_address()
                    
                    if(fucklsp.system.check_address_validation(address=address)):
                        stage += 1
                        break

                    else:
                        interface.print_process(context="IP address tidak valid", stat=0)
                
                if(usin in 'Nn'):
                    address = str(interface.fancy_input(context="Masukkan IP Debianmu secara manual :"))

                    if(fucklsp.system.check_address_validation(address=address)):
                        stage += 1
                        break

                    else:
                        interface.print_process(context="IP address tidak valid", stat=0)


                else:
                    interface.print_process(context="Input salah", stat=0)
                    interface.print_process(context="Masukkan jawaban antara [Y, y, N, n]", stat=0)

        # Getting the sitezip

        if(stage == 4):
            import os

            while(True):
                print('')
                print("Cari file web kamu di bawah ini :\n")
                zips = os.listdir(siteszips)

                for zip in zips:
                    print(f"\033[32m->\033[0m {zip}")

                print("Masukkan angka 0 untuk menggunakan web default apache2")
                sitezip = interface.fancy_input(context="Masukkan nama web kalian contoh [web.zip] :")

                if(os.path.exists(f"{siteszips}{sitezip}")):
                    interface.print_process(context=f"File {sitezip} ditemukan", stat=1)
                    interface.print_process(context="", stat=9)
                    stage += 1
                    break

                elif(str(sitezip) == '0'):
                    interface.print_process(context=f"Menggunakan laman default Apache2", stat=1)
                    nama = interface.fancy_input(context="Masukkan nama kamu :")
                    has_sitezip = False
                    documentroot = "/var/www/html"
                    stage += 1
                    break
                
                else:
                    interface.print_process(context=f"File {siteszips}{sitezip} tidak ditemukan", stat=0)

        # Reassuring settings variabels

        if(stage == 5):

            while(not restarted):

                print("Apakah informasi ini benar? [Yy/Nn] :\n")
                print("[\033[33mSistem\033[0m]")
                print('')
                print(f"\033[32mNama hostname\033[0m    : {hostname} ")
                print(f"\033[32mAlamat IP\033[0m        : {sys_addr}")
                print(f"\033[32mNetmask\033[0m          : {sys_netmask}")
                print(f"\033[32mAlamat Gateway\033[0m   : {sys_gateway}")
                print(f"\033[32mAlamat DNS\033[0m       : {sys_dns}")
                print('')
                print("[\033[33mBind9\033[0m]")
                print('')
                print(f"\033[32mNama domain\033[0m      : {domain} ")
                print(f"\033[32mAlamat IP\033[0m        : {address}")
                print('')
                print("[\033[33mApache2\033[0m]")
                print('')
                print(f"\033[32mNama domain\033[0m      : {domain} ")
                print(f"\033[32mDocument root\033[0m    : {documentroot}")
                print(f"\033[32mWeb file\033[0m         : {sitezip}")
                print('')


                usin = interface.fancy_input(context="Masukkan pilihan [Y/y] bila benar [N/n] apabila salah : ")

                if(usin in 'Yy'):
                    stage += 1
                    break

                if(usin in 'Nn'):
                    while(True):
                        usin = interface.fancy_input(context="Kamu yakin untuk mengulangi ini semua dari awal? [Y/y] untuk ya [N/n] untuk tidak :")

                        if(usin in 'Yy'):
                            interface.timer(context="Mengulangi proses :", stat=1 ,time=5)
                            stage = 0
                            restarted = True
                            break

                        if(usin in 'Nn'):
                            break

                        else:
                            interface.print_process(context="Input salah", stat=0)
                            interface.print_process(context="Masukkan jawaban antara [Y, y, N, n] ", stat=0)

                else:
                    interface.print_process(context="Input salah", stat=0)
                    interface.print_process(context="Masukkan jawaban antara [Y, y, N, n] ", stat=0)

        # Applying changes

        if(stage == 6):
            while(True):

                # Changing hostname

                fucklsp.system.change_hostname(filepath=hostname_path, hostname=(hostname))

                # Changing resolv.conf

                fucklsp.system.change_resolv(filepath=resolv_path, nameservers=(resolv_names))

                # Changing apt sources to embedded one

                fucklsp.apt.change_repository(filepath=apt_path, repositories=repositories)
                fucklsp.apt.update_apt()

                # Bind9 configuring

                address = fucklsp.system.split_address(address=address)

                fucklsp.bind9.check_installation()
                fucklsp.bind9.make_db_domain(address=address, domain=domain, db_path=db_domain)
                fucklsp.bind9.make_db_resolve(address=address, domain=domain, db_path=db_resolve)
                fucklsp.bind9.make_named_conf(address=address, domain=domain, dbdomain_path=db_domain, dbresolve_path=db_resolve, named_path=named_conf)

                fucklsp.bind9.restart()

                # Apache2 configuring

                fucklsp.apache2.check_installation()
                fucklsp.apache2.make_siteconf(domain=domain, documentroot=documentroot, siteconf=f"{siteconf_dir}{fucklsp.apache2.make_siteconf_name(site=sitezip)}", port=80)
                if(has_sitezip):
                    fucklsp.apache2.import_site(site=f"{siteszips}{sitezip}", documentroot=documentroot)
                else:
                    None

                if(has_sitezip):
                    fucklsp.apache2.enable_site(siteconf_name=f"{siteconf_dir}{fucklsp.apache2.make_siteconf_name(site=sitezip)}", linking_path=f"{siteconf_en}{fucklsp.apache2.make_siteconf_name(site=sitezip)}")
                
                else:
                    fucklsp.apache2.enable_site(siteconf_name=f"{siteconf_dir}{nama}.conf", linking_path=f"{siteconf_en}{nama}.conf")
                    
                fucklsp.apache2.reload()

                # Finishing setup

                interface.clear_cli()
                interface.print_process(context="Installasi selesai", stat=1)
                interface.timer(context="Menutup setup :",time= 3, stat=1)
                interface.clear_cli()

                # Goodbye display

                interface.print_asciiart()
                print("Terima Kasih telah menggunakan program \033[31mFuckLSP\033[0m")
                print("Semoga LSP mu berjalan lancar \033[31m<3\033[0m GoodBye")
                print('')

                interface.timer(context="Mohon Bersabar", stat=3,time=5)
                interface.magic()
                interface.timer_no_out(time=8)
                

                # Reapplying changes by rebooting os

                interface.print_process(context="Peringatan", stat=8)
                interface.print_process(context="Beberapa perubahan memerlukan reboot", stat=8)
                interface.print_process(context="Harap bersabar", stat=8)
                interface.timer(context="OS akan reboot dalam", stat=3, time=5)
                fucklsp.system.restart_networking()
                fucklsp.system.os_reboot()

else:   
    print('')
    interface.print_process(context="Error asing", stat=0)
    interface.print_process(context="OS asing", stat=0)
    interface.timer(context="Kembali ke terminal :", stat=0)

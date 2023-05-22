import subprocess

print("""
   _   _   _   _   _   _   _   _   _     _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( G | r | e | e | n | b | o | n | e ) ( I | n | s | t | a | l | l | e | r )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

Created by Z@rn!
    """)

def package_update():
    print("\nPackage Updating\n")
    pgk_update = "apt update"
    returned_value = subprocess.call(pgk_update, shell=True)
    print('returned value:', returned_value)

def greenbone():
    print("\nInstall Greenbone Package\n")
    greenbone = "apt install gvm"
    returned_value = subprocess.call(greenbone, shell=True)
    print('returned value:', returned_value)

def feed_update():
    print("\nFeed Updating\n")
    feed_update = "gvm-feed-update"
    returned_value = subprocess.call(feed_update, shell=True)
    print('returned value:', returned_value)

def user():
    user_pass = input("Do you want to set password for admin (Y/N) : ")
    if user_pass == "Y" or user_pass == "y":
        pass_set = input("Enter your new password: ")
        pass_cmd = "sudo -E -u _gvm gvmd --user=admin --new-password=" + pass_set
        eturned_value = subprocess.call(pass_cmd, shell=True)      
        print("Your Username is admin & Password is", pass_set)
    else:
        print("Bye Bye")

def gvm_run():
    gvm_start=input("Do you want to start Greenbone(Y/N) : ")
    if gvm_start == "Y" or gvm_start == "y":
        gvm_run = "gvm-start"
        returned_value = subprocess.call(gvm_run, shell=True)
        print('returned value:', returned_value)
    else:
        print("Your GVM is not running!")


package_update()
greenbone()
feed_update()
user()
gvm_run()

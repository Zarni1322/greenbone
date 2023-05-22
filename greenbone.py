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
    pkg_update = "apt update"
    returned_value = subprocess.run(pkg_update, shell=True)
    print('returned value:', returned_value.returncode)

def greenbone():
    print("\nInstall Greenbone Package\n")
    greenbone_cmd = "apt install gvm"
    returned_value = subprocess.run(greenbone_cmd, shell=True)
    print('returned value:', returned_value.returncode)

def feed_update():
    print("\nFeed Updating\n")
    feed_update_cmd = "gvm-feed-update"
    returned_value = subprocess.run(feed_update_cmd, shell=True)
    print('returned value:', returned_value.returncode)

def user():
    user_pass = input("Do you want to set a password for admin (Y/N): ")
    if user_pass.lower() == "y":
        pass_set = input("Enter your new password: ")
        pass_cmd = f"sudo -E -u _gvm gvmd --user=admin --new-password={pass_set}"
        returned_value = subprocess.run(pass_cmd, shell=True)
        print("Your Username is admin & Password is", pass_set)
    else:
        print("Bye Bye")

def gvm_run():
    gvm_start = input("Do you want to start Greenbone (Y/N): ")
    if gvm_start.lower() == "y":
        gvm_run_cmd = "gvm-start"
        returned_value = subprocess.run(gvm_run_cmd, shell=True)
        print('returned value:', returned_value.returncode)
    else:
        print("Your GVM is not running!")

package_update()
greenbone()
feed_update()
user()
gvm_run()

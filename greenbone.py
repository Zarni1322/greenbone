import subprocess

print("""
   _   _   _   _   _   _   _   _   _     _   _   _   _   _   _   _   _   _  
  / \ / \ / \ / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \ / \ / \ 
 ( G | r | e | e | n | b | o | n | e ) ( I | n | s | t | a | l | l | e | r )
  \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ \_/ 

Created by Z@rn!
    """)

class GreenboneManager:
    def __init__(self):
        self.package_update()
        self.greenbone()
        self.feed_update()
        self.gvm_setup()
        self.user()
        self.gvm_run()

    def run_command(self, command):
        returned_value = subprocess.run(command, shell=True)
        print('Returned value:', returned_value.returncode)

    def package_update(self):
        print("\nPackage Updating\n")
        pkg_update = "apt update"
        self.run_command(pkg_update)

    def greenbone(self):
        print("\nInstall Greenbone Package\n")
        greenbone_cmd = "apt install gvm -y"
        self.run_command(greenbone_cmd)

    def feed_update(self):
        print("\nFeed Updating\n")
        feed_update_cmd = "gvm-feed-update"
        self.run_command(feed_update_cmd)

    def gvm_setup(self):
        gvm_setup_check = "gvm-setup -h"
        self.run_command(gvm_setup_check)

    def user(self):
        user_pass = input("Do you want to set a password for admin (Y/N): ")
        if user_pass.lower() == "y":
            pass_set = input("Enter your new password: ")
            pass_cmd = f"sudo -E -u _gvm gvmd --user=admin --new-password={pass_set}"
            self.run_command(pass_cmd)
            print("Your Username is admin & Password is", pass_set)
        else:
            print("Bye Bye")

    def gvm_run(self):
        gvm_start = input("Do you want to start Greenbone (Y/N): ")
        if gvm_start.lower() == "y":
            gvm_run_cmd = "gvm-start"
            self.run_command(gvm_run_cmd)
        else:
            print("Your GVM is not running!")

GreenboneManager()

version = "0.0.1_Alpha - 0002"
import os
from time import time
boot_log = r"Python\SpyrOS\System\boot.log"
def logout():
    pass

def help(q):
    if q.lower() in ["neofetch","screenfetch","info","information"]:
        return "Returns system info, along with used memory."
    elif q.lower() == "help" or q.lower() == "?":
        return "Runs this command, which displays help."
    elif q.lower() == "logout" or q.lower() == "exit":
        return "Exits spyrOS."
    else:
        return "Parameter was null or invalid, please enter parameter."

def neofetch():
    print(f'''                                                                                                    
                                                             .@@@@@@@@@      #@@@@@@@     OS: SpyrOS (Prototype)
                                                           @@@@     *@@@,  (@@@     .     Version: {version}
            @@@@@@@%   @@&@@@@@@@  ,@@@    &@@#  @@@@@@@ .@@@,       @@@&  %@@@*          Shell: Custom; spyrOS
           #@@@       #@@@    @@@.  @@@   %@@#  /@@@.    @@@#        @@@,    @@@@@@       Shell-type: Python-based
             @@@@@(   @@@     @@@   #@@% @@@*   @@@      @@@,       @@@&        %@@@      
               ,@@@  %@@@   *@@@     @@@@@@    /@@@      @@@@     %@@@,  %/     @@@&      Used RAM: At this current moment,
          @@@@@@@    @@@(@@@@@.      &@@@*     @@@         @@@@@@@@(     %@@@@@@@/        not avaliable.
                    %@@#            @@@%                                                  
                    &@%           (@@(                                                    
                                                                                                    ''')

with open(boot_log,"a") as file:
    file.write(f"Boot at {time()} since epoch.\n")

path_default = "Python\SpyrOS\System"
path = path_default
path_displayed = "~/" + path + ">"

print('''                                                                                                    
                                                             .@@@@@@@@@      #@@@@@@@               
                                                           @@@@     *@@@,  (@@@     .               
            @@@@@@@%   @@&@@@@@@@  ,@@@    &@@#  @@@@@@@ .@@@,       @@@&  %@@@*                    
           #@@@       #@@@    @@@.  @@@   %@@#  /@@@.    @@@#        @@@,    @@@@@@                 
             @@@@@(   @@@     @@@   #@@% @@@*   @@@      @@@,       @@@&        %@@@                
               ,@@@  %@@@   *@@@     @@@@@@    /@@@      @@@@     %@@@,  %/     @@@&                
          @@@@@@@    @@@(@@@@@.      &@@@*     @@@         @@@@@@@@(     %@@@@@@@/                  
                    %@@#            @@@%                                                            
                    &@%           (@@(                                                              
                                                                                                    ''')
print(f"SpyrOS [v{version}]\nNon-copyrighted (c)",end="\n\n")


while True:
    command = input(f"{path_displayed}")
    if command.lower() == "exit" or command.lower() == "logout":
        logout()
        break
    elif command.split(" ")[0].lower() in ["help","?"]:
        tOH = command.split(" ")[0].lower()
        try:
            print(help(command.split(" ")[1]))
        except:
            print(f"Error. Please enter {tOH} [Command Name].")
    elif command.lower() in ["neofetch","screenfetch","info","information"]:
        neofetch()
    else:
        print(f"Invalid command.\nspyrOS is currently in {version} and is a prototype, so commands are limited.")
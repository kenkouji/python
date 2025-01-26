import os
if __name__ == '__main__':
    print("Welcome to robo speaker101","\n-------created by ash")
    while True:
        x=input("enter what do you want me to speak: ")
        if x== "q":
            os.system("say 'bye bye'")
            break
        command=f"say {x}"
        os.system(command)
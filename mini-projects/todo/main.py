#TODO list

def main():
    
    tasks = []
    
    while True:
        
        print("\nChoose what you want: ")
        print("1. Add TODO")
        print("2. Show list")
       # print("3. Mark as done")
        print("4. Exit")
        
        choice = input("Write a number:  ")
        
        #add
        if(choice == "1"):
            print()
            n_tasks = int(input("How many task you want to add? "))
            
            for i in range(n_tasks):
                task = input("Name a Task: ")
                tasks.append({"task": task})
                print("You added a new task!")
                    
                    
        elif(choice == "2"):
            print(f"\nTasks: ")
            
            for index, task in enumerate(tasks):
                print(f"{index + 1}. {task['task']}")
        
        elif(choice == "4"):
            print("exiting program")
            break        
        
        else:
            print("Wrong number.. \nTry again.")
        
                    
if __name__ == "__main__":
    main()
tasks = []

def show_tasks():
    if not tasks:
        print("\n[!] Abhi koi task nahi hai!")
    else:
        print("\n--- AAPKI TO-DO LIST ---")
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")

while True:
    print("\n-------------------------")
    print("1. Tasks Dekho")
    print("2. Naya Task Add Karo")
    print("3. Task Delete Karo")
    print("4. Exit")
    
    choice = input("Option chuno (1-4): ").strip()

    if choice == '1':
        show_tasks()
        
    elif choice == '2':
        new_task = input("Naya task likho: ").strip()
        if new_task:
            tasks.append(new_task)
            print("✓ Task add ho gaya!")
        else:
            print("⚠️ Khaali task add nahi ho sakta!")
            
    elif choice == '3':
        show_tasks()
        if tasks:
            try:
                task_num = int(input("Konta task delete karna hai (Number): "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"✓ '{removed}' delete ho gaya!")
                else:
                    print("⚠️ Galat number daala!")
            except ValueError:
                print("⚠️ Kripya sirf number enter karein!")
                
    elif choice == '4':
        print("Goodbye!")
        break
        
    else:
        print("⚠️ Galat option! 1 se 4 ke beech chuno.")

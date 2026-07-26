contacts = {}

def show_contacts():
    if not contacts:
        print("\n[!] Abhi koi contact save nahi hai!")
    else:
        print("\n--- AAPKI CONTACT LIST ---")
        for name, phone in contacts.items():
            print(f"👤 {name} : 📞 {phone}")

while True:
    print("\n-------------------------")
    print("1. Sare Contacts Dekho")
    print("2. Naya Contact Add Karo")
    print("3. Contact Search Karo")
    print("4. Contact Delete Karo")
    print("5. Exit")
    
    choice = input("Option chuno (1-5): ").strip()

    if choice == '1':
        show_contacts()
        
    elif choice == '2':
        name = input("Naam likho: ").strip()
        phone = input("Phone Number: ").strip()
        if name and phone:
            contacts[name] = phone
            print(f"✓ '{name}' ka contact save ho gaya!")
        else:
            print("⚠️ Naam aur Number dono likhna zaroori hai!")
            
    elif choice == '3':
        search_name = input("Kiska number search karna hai (Naam): ").strip()
        if search_name in contacts:
            print(f"✓ Found: {search_name} -> 📞 {contacts[search_name]}")
        else:
            print("⚠️ Ye naam contacts mein nahi mila!")

    elif choice == '4':
        del_name = input("Kiska contact delete karna hai (Naam): ").strip()
        if del_name in contacts:
            del contacts[del_name]
            print(f"✓ '{del_name}' delete ho gaya!")
        else:
            print("⚠️ Ye naam contacts mein nahi hai!")
            
    elif choice == '5':
        print("Goodbye!")
        break
        
    else:
        print("⚠️ Galat option! 1 se 5 ke beech chuno.")

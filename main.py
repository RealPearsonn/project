import random
import requests


words = [
    "Eagle", "Lion", "Tiger", "Wolf", "Dragon", "Phoenix", "Shark", "Falcon", 
    "Bear", "Hawk", "Panda", "Cheetah", "Otter", "Jaguar", "Dolphin", "Rhino", 
    "Whale", "Giraffe", "Elephant", "Buffalo", "Fox", "Viper", "Grizzly", "Bison",
    "Cobra", "Seal", "Sparrow", "Raven", "Parrot", "Lynx", "Hedgehog", "Tortoise",
    "Antelope", "Kangaroo", "Koala", "Sloth", "Crab", "Octopus", "Lizard", "Chameleon",
    "Wolverine", "Puma", "Iguana", "Ocelot", "Buffalo", "Mongoose", "Swan", "Pelican",
    "Gazelle", "Armadillo", "Walrus", "Narwhal", "Capybara", "Cheetah", "Toad", "Gecko",
    "Tapir", "Porcupine", "Manatee", "Aardvark", "Pangolin", "Emu", "Llama", "Yak",
    "Sloth", "Flamingo", "Macaw", "Ostrich", "Quokka", "Tarantula", "Frog", "Newt",
    "Wombat", "Zebra", "Koi", "Seahorse", "Goldfish", "Pufferfish", "Angelfish", 
    "Crane", "Heron", "Vulture", "Condor", "Buffalo", "Tapir", "Chinchilla", "Ape",
    "Hummingbird", "Mynah", "Platypus", "Raccoon", "Kookaburra", "Armadillo", "Dingo"
]
adjectives = [
    "Swift", "Brave", "Mighty", "Clever", "Bold", "Fierce", "Wise", "Gentle", 
    "Loyal", "Noble", "Fearless", "Daring", "Radiant", "Savage", "Graceful", 
    "Tenacious", "Vigorous", "Charming", "Astute", "Valiant", "Dynamic", 
    "Inventive", "Impressive", "Dazzling", "Heroic", "Luminous", "Bold", 
    "Courageous", "Witty", "Sly", "Eloquent", "Artistic", "Creative", 
    "Fearsome", "Majestic", "Zany", "Epic", "Proud", "Nimble", "Gallant", 
    "Humble", "Sincere", "Eager", "Sassy", "Unique", "Whimsical", 
    "Spirited", "Zealous", "Funky", "Groovy", "Radiant", "Dapper", 
    "Astounding", "Enchanting", "Fearless", "Lively", "Persuasive", 
    "Curious", "Affectionate", "Hilarious", "Dashing", "Charming", 
    "Magnificent", "Bubbly", "Exuberant", "Inspiring", "Passionate", 
    "Adventurous", "Diligent", "Playful", "Innovative", "Respectful", 
    "Optimistic", "Sincere", "Joyful", "Benevolent", "Thoughtful", 
    "Polished", "Fearless", "Brilliant", "Fulfilling", "Magnificent", 
    "Sublime", "Valorous", "Intrepid", "Enthusiastic", "Exciting", 
    "Incredible", "Outstanding", "Radiant", "Vibrant", "Playful", 
    "Challenging", "Spectacular", "Dynamic", "Energetic", "Intelligent"
]

def generate_username(custom_word=None):
    if custom_word:
        word = custom_word
    else:
        word = random.choice(words)
    
    adjective = random.choice(adjectives)
    
    
    username = f"{adjective}{word}"

    
    if random.choice([True, False]):
        number = random.randint(0, 999)
        username += f"_{number:03d}"  
    
    
    if len(username) > 20:
        username = username[:20]  

    return username

def check_username_availability(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    return response.status_code == 404  

def main():
    print("Random Username Generator")
    
    custom_choice = input("Would you like to enter your own word? (yes/no): ").strip().lower()
    custom_word = None
    
    if custom_choice == 'yes':
        custom_word = input("Enter your custom word: ").strip()
    
    
    usernames = [generate_username(custom_word) for _ in range(10)]
    print("\nGenerated Usernames:")
    for i, username in enumerate(usernames, start=1):
        print(f"{i}. {username}")

   
    selected_index = int(input("\nSelect a username by number (1-10): ")) - 1
    selected_username = usernames[selected_index]
    
    
    if check_username_availability(selected_username):
        print(f"Username '{selected_username}' is available!")
    else:
        print(f"Username '{selected_username}' is taken.")

if __name__ == "__main__":
    main()

import random
import string
from datetime import datetime, timedelta

male_names = [
    "Aiden", "Alexander", "Andrew", "Anthony", "Austin", "Adam", "Aaron", "Adrian", "Blake", "Benjamin",
    "Brandon", "Brian", "Brody", "Bryce", "Bradley", "Carter", "Caleb", "Cameron", "Casey", "Charles",
    "Christian", "Christopher", "Cody", "Cole", "Colin", "Connor", "Cooper", "Daniel", "David", "Dawson",
    "Dean", "Derek", "Devin", "Dominic", "Dylan", "Easton", "Edward", "Elijah", "Elliot", "Ethan", "Evan",
    "Felix", "Finn", "Gabriel", "Gavin", "George", "Grant", "Grayson", "Henry", "Hudson", "Hunter", "Ian",
    "Isaac", "Isaiah", "Ivan", "Jack", "Jackson", "Jacob", "Jake", "James", "Jason", "Jasper", "Jax",
    "Jayden", "Jeremy", "Joel", "John", "Jonah", "Jonathan", "Jordan", "Joseph", "Joshua", "Julian", "Justin",
    "Kevin", "Kyle", "Landon", "Leo", "Liam", "Lincoln", "Logan", "Lucas", "Luis", "Luke", "Marcus", "Mark",
    "Mason", "Matthew", "Max", "Micah", "Michael", "Miles", "Nathan", "Nathaniel", "Nicholas", "Nolan",
    "Noah", "Oliver", "Owen", "Patrick", "Paul", "Parker", "Philip", "Preston", "Quentin", "Ralph", "Raymond",
    "Reese", "Reid", "Richard", "Riley", "Robert", "Ryan", "Samuel", "Sawyer", "Scott", "Sean", "Seth",
    "Silas", "Spencer", "Stephen", "Steven", "Theodore", "Thomas", "Timothy", "Travis", "Trevor", "Tristan",
    "Tucker", "Tyler", "Victor", "Vincent", "Walter", "Wesley", "William", "Xavier", "Zachary", "Zander",
    "Abel", "Alvin", "Arthur", "Ashton", "Barrett", "Bennett", "Boston", "Bryan", "Colt", "Cyrus", "Damien",
    "Davis", "Desmond", "Donovan", "Drew", "Edgar", "Ellis", "Emerson", "Emmett", "Everett", "Ford",
    "Frederic", "Gerald", "Gordon", "Grey", "Hank", "Harley", "Harold", "Harvey", "Hendrix", "Holden",
    "Jamal", "Jay", "Jeffrey", "Jensen", "Jerome", "Jessie", "Joaquin", "Julius", "Kareem", "Karter",
    "Kendrick", "Kingston", "Lance", "Larry", "Lawson", "Lennox", "Lionel", "Malakai", "Malcolm", "Marvin",
    "Mateo", "Matthias", "Maurice", "Maverick", "Milan", "Mitchell", "Moses", "Murphy", "Neil", "Nelson",
    "Nixon", "Omar", "Orlando", "Peyton", "Pierce", "Porter", "Quincy", "Raphael", "Reagan", "Ronan",
    "Russell", "Ryker", "Sage", "Samson", "Santos", "Shaquille", "Sheldon", "Shepard", "Stanley", "Tate",
    "Thatcher", "Thiago", "Tomas", "Troy", "Tyson", "Uriel", "Vernon", "Wade", "Warren", "Wayne", "Wells",
    "Westin", "Wilder", "Willis", "Winston", "Yosef", "Zayne", "Zechariah", "Briggs", "Callum", "Conrad",
    "Corbin", "Crew", "Dalton", "Dane", "Deacon", "Denver", "Dwight", "Edison", "Elias", "Fisher", "Gage",
    "Garrett", "Gideon", "Harlan", "Hayes", "Heath", "Hugo", "Iker", "Idris", "Jamison", "Kamden", "Kellen",
    "Kian", "Kody", "Korbin", "Leroy", "Madden", "Magnus", "Nash", "Oakley", "Palmer", "Ridge", "Rowan",
    "Royce", "Royal", "Santino", "Saul", "Soren", "Sterling", "Stone", "Sutton", "Truett", "Vance", "Westley",
    "Zion"
]

female_names = [
    "Abigail", "Addison", "Aaliyah", "Alice", "Alyssa", "Amara", "Amber", "Amelia", "Amy", "Anastasia",
    "Andrea", "Angela", "Anna", "Annabelle", "Aria", "Ariana", "Aubrey", "Autumn", "Avery", "Bella",
    "Bethany", "Bianca", "Blair", "Bria", "Brianna", "Brooklyn", "Camila", "Cara", "Carmen", "Caroline",
    "Casey", "Cassandra", "Catherine", "Cecilia", "Charlotte", "Chelsea", "Chloe", "Christina", "Claire",
    "Clara", "Cora", "Daisy", "Dakota", "Daniela", "Danielle", "Daphne", "Deborah", "Delilah", "Destiny",
    "Diana", "Eden", "Eleanor", "Elena", "Eliza", "Elizabeth", "Ella", "Ellie", "Eloise", "Emilia",
    "Emily", "Emma", "Erin", "Esme", "Esther", "Eva", "Evelyn", "Faith", "Fiona", "Flora", "Francesca",
    "Freya", "Gabriella", "Georgia", "Gia", "Giselle", "Grace", "Gracie", "Hailey", "Hannah", "Harper",
    "Haven", "Hazel", "Heidi", "Holly", "Hope", "Irene", "Iris", "Isabella", "Isla", "Ivy", "Jade", "Jamie",
    "Jane", "Jasmine", "Jenna", "Jennifer", "Jessica", "Jill", "Joanna", "Jocelyn", "Jordan", "Josephine",
    "Joy", "Julia", "Juliet", "June", "Kailey", "Kaitlyn", "Kara", "Karen", "Karina", "Kate", "Katherine",
    "Kayla", "Keira", "Kennedy", "Kiara", "Kimberly", "Kinsley", "Kyla", "Kylie", "Lacey", "Lana", "Laura",
    "Lauren", "Layla", "Leah", "Leila", "Lexi", "Lila", "Liliana", "Lily", "Lindsay", "Lisa", "Lola",
    "London", "Lucia", "Lucy", "Luna", "Lydia", "Mackenzie", "Maddie", "Madison", "Maggie", "Maisie",
    "Makayla", "Margaret", "Maria", "Mariana", "Marie", "Mariah", "Marlee", "Martha", "Mary", "Maya",
    "Mckenna", "Megan", "Melanie", "Melissa", "Mia", "Michelle", "Mila", "Miley", "Millie", "Miranda",
    "Molly", "Nadia", "Naomi", "Natalie", "Natasha", "Nicole", "Nina", "Noelle", "Nora", "Nova", "Olive",
    "Olivia", "Paige", "Paisley", "Palmer", "Patricia", "Pearl", "Penelope", "Peyton", "Phoebe", "Piper",
    "Poppy", "Quinn", "Rachel", "Raelynn", "Rebecca", "Reese", "Renee", "Riley", "Rose", "Rosie", "Rowan",
    "Ruby", "Ruth", "Sabrina", "Sadie", "Samantha", "Sara", "Sarah", "Sasha", "Savannah", "Scarlett",
    "Selena", "Serenity", "Sienna", "Sierra", "Simone", "Skye", "Sophia", "Sophie", "Stella", "Stephanie",
    "Summer", "Sydney", "Talia", "Tara", "Taylor", "Teresa", "Tessa", "Tiffany", "Vanessa", "Vera",
    "Veronica", "Victoria", "Violet", "Virginia", "Vivian", "Willa", "Willow", "Winter", "Whitney", "Yara",
    "Yasmin", "Zara", "Zoe", "Adriana", "Alma", "Angelica", "Arielle", "Ashlyn", "Aspen", "Astrid",
    "Beatrice", "Bonnie", "Bridget", "Brynn", "Cadence", "Cali", "Callie", "Carly", "Celeste", "Charlee",
    "Cynthia", "Danna", "Denise", "Demi", "Dorothy", "Elaine", "Elsa", "Emersyn", "Fallon", "Felicity",
    "Hallie", "Harmony", "Helena", "Holland", "Indie", "Ivanna", "Jayla", "Jolene", "Journey", "Julie",
    "Julissa", "Kamila", "Kara", "Katelyn", "Kendra", "Kira", "Landry", "Laurel", "Leighton", "Lia",
    "Lillie", "Lorelei", "Louisa", "Luciana", "Lyra", "Madilyn", "Mallory", "Marley", "Mina", "Monroe",
    "Myra", "Nola", "Oakley", "Opal", "Paislee", "Perla", "Priscilla", "Raegan", "Raina", "Rebekah",
    "Rhea", "Saige", "Salem", "Sari", "Selah", "Sloane", "Tiana", "Tinley", "Viviana", "Wren", "Zuri"
]

genz_suffix = [
    "tzy", "zyyy", "xyz", "qt", "luv", "core", "chan", "kun", "senpai",
    "vibes", "vibez", "zz", "xoxo", "ly", "ify", "lol", "lmao", "xd",
    "ouh", "onigiri", "rawr", "uwu", "owo", "notfound", "404", "void",
    "blink", "coffee", "matcha", "latte", "mochii", "nugget", "boba",
    "milk", "cloud", "storm", "rain", "sunset", "sunny", "night",
    "dream", "dreamer", "sleepy", "ghost", "spirit", "shade", "shadow",
    "wolf", "tiger", "lion", "dragon", "phoenix", "reaper", "samurai",
    "ninja", "ronin", "hype", "hyped", "epic", "legend", "god", "goat",
    "beast", "alpha", "beta", "sigma", "delta", "omega",
    "killa", "killer", "sniper", "blaze", "burn", "spark", "frost",
    "ice", "cold", "snow", "winter", "heat", "flame", "fire", "ignite",
    "nova", "lunar", "stellar", "galaxy", "orbit", "space", "cosmo",
    "astro", "matrix", "cyber", "glitch", "error", "bug", "lag",
    "speed", "fast", "boost", "turbo", "hyper"
]

email_domains = ["@gmail.com", "@yahoo.com", "@company.com", "@test.local"]

# =======================
# RANDOM GENERATORS
# =======================

def random_password():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(10))

def random_date(start_year=2020, end_year=2025):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d")

def generate_fullname(names):
    length = random.choice([2, 3])
    return " ".join(random.sample(names, length))

def random_username(base_name):
    if random.random() < 0.5:
        return base_name.lower()
    suffix = random.choice(genz_suffix)
    num = str(random.randint(1, 999)) if random.random() < 0.4 else ""
    return f"{base_name.lower()}{suffix}{num}"

# =====================================================
# FIX: UNIQUE USERNAME & UNIQUE EMAIL CHECK
# =====================================================

used_fullnames = set()
used_usernames = set()
used_emails = set()

def unique_username(base_name):
    username = random_username(base_name)

    # kalo masih unik, langsung gas
    if username not in used_usernames:
        used_usernames.add(username)
        return username

    # kalo duplikat, kasih angka
    count = 1
    while True:
        candidate = f"{username}{count}"
        if candidate not in used_usernames:
            used_usernames.add(candidate)
            return candidate
        count += 1

def unique_email(username):
    while True:
        email = username + random.choice(email_domains)
        if email not in used_emails:
            used_emails.add(email)
            return email

# =======================
# PROGRAM
# =======================

print("Pilih gender nama:")
print("1. Laki-laki")
print("2. Perempuan")
gender = int(input("Pilih (1/2): "))

nama_list = male_names if gender == 1 else female_names

total = int(input("Mau generate berapa data: "))
start_id = int(input("Mulai dari ID berapa: "))

print("\nGenerating...\n")

rows = []

for i in range(total):
    # fullname unik
    while True:
        fullname = generate_fullname(nama_list)
        if fullname not in used_fullnames:
            used_fullnames.add(fullname)
            break

    first_name = fullname.split()[0].lower()

    # username unik
    username = unique_username(first_name)

    # email unik
    email = unique_email(username)

    password = random_password()
    created_at = random_date()
    updated_at = random_date() if random.random() < 0.5 else None
    deleted_at = random_date() if random.random() < 0.2 else None

    row = (
        f"({start_id + i}, '{username}', '{email}', '{password}', "
        f"'{fullname}', '{created_at}', "
        f"{'NULL' if updated_at is None else f'\"{updated_at}\"'}, "
        f"{'NULL' if deleted_at is None else f'\"{deleted_at}\"'}),"
    )

    rows.append(row)

# print hasil
print("\n".join(rows))
print(f"\nDone bro 😎🔥 Total rows printed: {total}")

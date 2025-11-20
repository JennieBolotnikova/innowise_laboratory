
def generate_profile(age: int):
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"
    else:
        return "Invalid age"

def get_user_name():
    name = input("Enter your full name: ")
    return name

def get_user_age():
    while True:
        try:
            birth_year_str = input("Enter your birth year: ")
            birth_year = int(birth_year_str)
            if birth_year < 1905:
                print("Error: Birth year cannot be earlier than 1905. Please try again.")
                continue

            if birth_year > 2025:
                print("Error: Birth year cannot be in the future. Please try again.")
                continue
            current_age = 2025 - birth_year

            return birth_year, current_age
        except ValueError:
            print("Error: Please enter a valid integer for the birth year. Please try again.")


def get_hobbies():
    hobbies = list()
    while True:
        answer = input("Enter a favorite hobby or type 'stop' to finish: ")
        if answer == "stop":
            break
        else:
            hobbies.append(answer)
    return hobbies

def create_user_profile(name, current_age, hobbies):
    life_stage = generate_profile(current_age)
    user_profile = {"name": name,
                    "age": current_age,
                    "stage": life_stage,
                    "hobbies": hobbies}
    return user_profile


def display_profile(user_profile):
    print("---")
    print("Profile Summary")
    print(f"Name: {user_profile["name"]}")
    print(f"Age: {user_profile["age"]}")
    print(f"Life stage: {user_profile["stage"]}")

    if len(user_profile["hobbies"]) == 0:
        print("You didn't mention any hobbies")
    else:
        print(f"Favorite hobbies ({len(user_profile["hobbies"])})")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")

    print("---")

def main():
    user_name = get_user_name()
    birth_year, current_age = get_user_age()
    hobbies = get_hobbies()
    user_profile = create_user_profile(user_name, current_age, hobbies)
    display_profile(user_profile)


if __name__ == '__main__':
    main()





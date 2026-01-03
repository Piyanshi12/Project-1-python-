import random
subjects = ["Rehman Dakait","Katrina Kaif","AP Dhillon","Virat Kohli"]
actions = ["scrolling reels","dances with","plays ludo","runs at","riding buffalo"]
places_or_things = ["in a club","at Gwalior fort","in a village","in front of Taj Mahal"]
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)
    headline = f"BREAKING NEWS:{subject} {action} {place_or_thing}"
    print("\n" + headline )
    user_input = input("\n Do you want another headline?(yes/no)").strip()
    if user_input == "no":
        break
    print("\n Thank you for using False News Headline Generator.Have a fantastic day.")

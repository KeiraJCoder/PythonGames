import random

when = ['A long long time ago', 'Two weeks after the end of the world', 'Before Jesus was born', 'Sometime in the future', 'Before the arrival of Thanos']
who = ['Demi, ', 'Jordan, ', 'Keira, ', 'Katy, ', 'Neil, ']
withh = ['Tony Stark, ', 'Pikachu, ', 'Darth Vader, ', "The Terminator, ", "Stan Lee, ", "Zelda, ", "Princess Peach, ", "Boba fet, ", "Chewbacca, ", "Peter Parker, ", "Superman, ", "The Doctor, "]
where = ['a Galaxy far far away', 'into the Underworld', 'Netherland', 'Arkham Asylum', 'Indigo City', 'The Tardis', 'The Bat Cave', 'The Avengers HQ']
what = ['to eat all the chocolate', 'to steal the Tesseract', 'to support Fathers for Justice', 'to lick all the doorknobs', 'to do Gangnam Style', 'to find out whether the cake is a lie', 'to get attention from Senpai', 'to punch a Dalek', 'to make an embarrasing TikTok']
outcome = ['It did not go well', 'It was truly chilling', 'Thats when things got Truly bizarre', 'It inspired awe and fear for generations to come.', 'That is what Death now thinks of as a bad day', 'Tinkerbell died that day.', 'And thats all I can say about that', 'I still have nightmares about that day']\

print(random.choice(when) + ', ' + random.choice(who) + 'accompanied by ' + random.choice(withh) + 'went to ' + random.choice(where) + ' ' + random.choice(what) + '. ' + random.choice(outcome))
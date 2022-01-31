def sent_maker(phrase):
    interogatives = ("how", "why", "do")
    capitalized = phrase.capitalize()

    if phrase.startswith(interogatives):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)


list_of_results = []
while True:
    user_input = input("Say something, I am giving up on you:")
    if(user_input == 'no'):
        break
    else:
        list_of_results.append(sent_maker(user_input))
print(" ".join(list_of_results))

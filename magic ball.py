import random

answers = [    "It is certain.",    "It is decidedly so.",    "Without a doubt.",    "Yes - definitely.",    "You may rely on it.",    "As I see it, yes.",    "Most likely.",    "Outlook good.",    "Yes.",    "Signs point to yes.",    "Reply hazy, try again.",    "Ask again later.",    "Better not tell you now.",    "Cannot predict now.",    "Concentrate and ask again.",    "Don't count on it.",    "My reply is no.",    "My sources say no.",    "Outlook not so good.",    "Very doubtful."]

def magic_8_ball():
    print("Welcome to the Magic 8 Ball game!")
    question = input("Ask a yes/no question: ")
    print("Thinking...")
    print(random.choice(answers))

magic_8_ball()

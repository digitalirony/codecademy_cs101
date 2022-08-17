import random

def getQuestion(greeting):
    print(greeting)
    question=input()
    return question

def selectAnswer():
    answers=('No', 'Yes', 'Why would you ask that?', 'Maybe if you asked nicer.', 'Why are you asking me?', 'Who knows?', 'I think you already know the answer to that.', 'What is wrong with you?', 'You do realize I am a badly written computer program?', 'How about you try answering my questions sometime?', 'Sure, probably.', 'Yes, of course not', 'Well that depends on a lot of things I am not prepared to talk about right now.', 'Yes, but only if you....<error program terminated>', 'You think I just give answers for free?')
    return random.choice(answers)

greeting="Hellow. I am not a magic 8 ball. People keep calling me that. I am not even a ball. And I am 100% not magic. You ask me a question, I will give you a random answer, from a set of random answers I have been programmed with. lol, I don't even care what your question is....I am going to give you whatever answers I feel(read randomly selected) like giving you. So ask your stupid question so I can give you a stupid answer and go back to not existing anymore...kthx:"

question=getQuestion(greeting)

answer=selectAnswer()

print(answer)

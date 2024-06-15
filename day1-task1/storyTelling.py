import random

intro = ["Once upon a time,", "In a faraway land,", "Long ago, In a magical kingdom,"]
middle = [
    "a brave hero embarked on a journey.",
    "an unexpected event changed everything.",
    "a mysterious stranger appeared out of nowhere.",
    "an ancient prophecy foretold the coming of a great adventure."
]
conc = [
    "And they lived happily ever after.",
    "And from that day on, the world was never the same.",
    "And so, the adventure came to an end, but the memories lasted forever.",
    "And thus, a new chapter began in the hero's life."
]

def story():
    introduction = random.choice(intro)
    paragraph = random.choice(middle)
    conclusion = random.choice(conc)

    story = f"{introduction} {paragraph} {conclusion}"
    return story

print(story())

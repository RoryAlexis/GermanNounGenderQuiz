from rulesAndWords import Rule, Word
import random
import json

word_to_varsDict = {}
with open("wordCreaterHeartbeat.json", "r", encoding="utf-8") as f:
    word_to_varsDict = json.load(f)

word_to_wordObject = {}
for word, varsDict in word_to_varsDict.items():
    word_to_wordObject[word] = Word.fromDict(varsDict)

rule_to_varsDict = {}
with open("genderRules.json", "r", encoding="utf-8") as f:
    rule_to_varsDict = json.load(f)

rule_to_ruleObject = {}
for rule, varsDict in rule_to_varsDict.items():
    rule_to_ruleObject[rule] = Rule.fromDict(varsDict)

totalWords = len(list(word_to_wordObject.keys()))
word_to_correctRule = {}

wordsWithNoRules = []
for word, wordObject in word_to_wordObject.items():
    for rule, ruleObject in rule_to_ruleObject.items():
        if ruleObject.doesRuleApply(wordObject) and ruleObject.isRuleCorrect(wordObject):
            word_to_correctRule[word] = rule
            break
    else:
        wordsWithNoRules.append(word)
print(f"The total number of words tested was {totalWords}")
print(f"The number of words that can be deduced by following the rules are {len(word_to_correctRule)}")
print(f"The number of words that have to just be memorized is {len(wordsWithNoRules)}")

"""
while True:
    word = random.choice(list(word_to_wordObject.keys()))
    myWord = word_to_wordObject[word]
    print(myWord.word)
    print("guess the gender! (der/die/das)")
    myGuess = input()
    if myGuess.strip().lower() == myWord.gender:
        print("yay")
    else:
        print(f"I'm sorry.  The correct article for {myWord.word} is {myWord.gender}")
    for rule, ruleObject in rule_to_ruleObject.items():
        if ruleObject.doesRuleApply(myWord) and ruleObject.isRuleCorrect(myWord):
            print(rule)
            break
    else:
        print("No rule applies here! You just gotta memorize it!")
    """
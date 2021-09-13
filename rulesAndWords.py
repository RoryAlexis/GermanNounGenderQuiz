class Rule():
    def __init__(self, suffix, gender, etymology="", 
                exceptions={}, canBeMonosyllabic=False, 
                canBePolySyllabic=True):
        self.suffix = suffix
        self.gender = gender
        self.etymology = etymology
        self.excludedWord_to_gender = exceptions
        self.canBeMonosyllabic = canBeMonosyllabic
        self.canBePolySyllabic = canBePolySyllabic

    def doesRuleApply(self, word):
        if word.syllables > 1 and not self.canBePolySyllabic:
            #print(f"words has too many syllabes {word.syllables}")
            return False
        if word.syllables == 1 and not self.canBeMonosyllabic:
            #print(f"words has too few syllabes {word.syllables}")
            return False
        if not word.word.endswith(self.suffix):
            #print(f"word does not end with right suffix: {self.suffix} vs. {word.word[-3:]}")
            return False
        if word.etymology != self.etymology:
            #print(f"word is  of the wrong etymology: {self.etymology} vs. {word.etymology}")
            return False
        if word.word in self.excludedWord_to_gender.keys():
            #print(f"This is an exception to the rule that words ending with {self.suffix} use the {self.gender} article")
            return True 
        return True

    def guessGender(self, word):
        if not self.doesRuleApply(word):
            return None
        if word.word in self.excludedWord_to_gender.keys():
            return self.excludedWord_to_gender[word.word]
        return self.gender

    def isRuleCorrect(self,word):
        if not self.doesRuleApply(word):
            return True
        if self.doesRuleApply(word) and word.word not in self.excludedWord_to_gender.keys() and word.gender != self.gender:
            return False
        else:
            return True

    @classmethod
    def fromDict(cls, varsDict):
        return cls(varsDict["suffix"], varsDict["gender"], varsDict["etymology"], 
                    varsDict["excludedWord_to_gender"], varsDict["canBeMonosyllabic"], varsDict["canBePolySyllabic"])

class Word():

    def __init__(self, word, gender, syllables=1, etymology=""):
        self.word = word
        self.gender = gender
        self.syllables = syllables
        self.etymology = etymology

    @classmethod
    def fromDict(cls, varsDict):
        return cls(varsDict["word"], varsDict["gender"], varsDict["syllables"], varsDict["etymology"])



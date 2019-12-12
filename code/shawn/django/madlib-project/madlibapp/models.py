from django.db import models

# MadLib will hold title and be one-to-many with MadLibWord
class MadLib(models.Model):
    title = models.CharField(max_length=200)

    # a helper function to parse the text 
    def parse_text(self, input_string):

        # delete exiting madlibwords for this madlib
        for word in MadLibWord.objects.filter(madlib=self):
            word.delete()

        # iterate through input string and create MadLibWords
        for list_word in input_string:
            MadLibWord.objects.create(madlib=self, word=list_word)
        
    # a helper function to figure out how many MadLibwords there are
    def count_madlibwords(self): 
        count = 0
        for word in MadLibWord.objects.filter(madlib=self):
            try:
                if word.word[0] == '*':
                    count += 1
            except IndexError:
                continue
        return count

# MadLibWord will be many-to-one with MadLib.  Each MadLibWord has the word, type of word, and ForeignKey to the MadLib puzzle to which it belongs
class MadLibWord(models.Model):
    word = models.CharField(max_length=50, blank=True, null=True)                              # limit to max of 50 characters
    madlib = models.ForeignKey(MadLib, on_delete=models.CASCADE)

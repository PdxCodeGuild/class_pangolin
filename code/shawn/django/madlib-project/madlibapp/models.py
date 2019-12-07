from django.db import models

# MadLib will hold title and be one-to-many with MadLibWord
class MadLib(models.Model):
    title = models.CharField(max_length=200)

    # a helper function to parse the text 
    def parse_text(self, input_string):

        # iterate through input string and create MadLibWords
        for list_word in input_string:
            MadLibWord.objects.create(madlib=self, word=list_word)

# MadLibWord will be many-to-one with MadLib.  Each MadLibWord has the word, type of word, and ForeignKey to the MadLib puzzle to which it belongs
class MadLibWord(models.Model):
    word = models.CharField(max_length=50, blank=True, null=True)                              # limit to max of 50 characters
    madlib = models.ForeignKey(MadLib, on_delete=models.CASCADE)

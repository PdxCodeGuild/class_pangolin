from django.db import models

# MadLib will hold title and be one-to-many with MadLibWord
class MadLib(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()                                           # the text field containing madlib text plus MadLibWords

    # a helper function to parse the text 
    def parse_text(self):

        # split input on ***
        self.text = self.text.split('***')

        # iterate through input string
        for item in self.text:
            # if a 'noun' is found
            if item in ['noun','adjective','verb','plural noun','pronoun','adverb']:
                # create new MadLiBWord 
                item = MadLibWord.objects.create(word_type=item, madlib=self, word='')

        # save changes
        self.save()



# MadLibWord will be many-to-one with MadLib.  Each MadLibWord has the word, type of word, and ForeignKey to the MadLib puzzle to which it belongs
class MadLibWord(models.Model):
    word = models.CharField(max_length=50, blank=True, null=True)                              # limit to max of 50 characters
    word_type = models.CharField(max_length=20)                         # valid word types: 'noun', 'verb', 'adjective', 'plural noun', 'adverb', 'pronoun'
    madlib = models.ForeignKey(MadLib, on_delete=models.CASCADE)
    
    def is_madlibword(self):
        return True

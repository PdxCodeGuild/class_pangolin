from django.db import models

# MadLib will hold title and be one-to-many with MadLibWord
class MadLib(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()                                           # the text field containing madlib text plus MadLibWords

# MadLibWord will be many-to-one with MadLib.  Each MadLibWord has the word, type of word, and ForeignKey to the MadLib puzzle to which it belongs
class MadLibWord(models.Model):
    word = models.CharField(max_length=50)                              # limit to max of 50 characters
    word_type = models.CharField(max_length=20)                         # valid word types: 'noun', 'verb', 'adjective', 'plural noun', 'adverb'
    madlib = models.ForeignKey(MadLib, on_delete=models.CASCADE)
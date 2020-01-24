# The first three lines bring in the packages needed for performing the language analysis and the HTTP framework.
import flask
import spacy
import vaderSentiment.vaderSentiment as vader

# The next three lines create a few global variables. 
# The first variable, app, is the main entry point that Flask uses for creating HTTP routes. The second variable, analyzer, is the same type used in the previous example, and it will be used to generate the sentiment scores. 
# The last variable, english, is also the same type used in the previous example, and it will be used to annotate and tokenize the initial text input.
app = flask.Flask(__name__)
analyzer = vader.SentimentIntensityAnalyzer()
english = spacy.load("en_core_web_sm")

# The next piece is the heart of the service—a function for generating sentiment values from a string of text. 
# You can see that the operations in this function correspond to the commands you ran in the Python interpreter earlier. 
# Here they're wrapped in a function definition with the source text being passed in as the variable text and finally the sentiments variable returned to the caller.
def get_sentiments(text):
    result = english(text)
    sentences = [str(sent) for sent in result.sents]
    sentiments = [analyzer.polarity_scores(str(s)) for s in sentences]
    return sentiments


# The last function in the source file contains the logic that will instruct Flask how to configure the HTTP server for the service. 
# It starts with a line that will associate an HTTP route / with the request methods POST and GET.
@app.route("/", methods=["POST", "GET"])
def index():
    if flask.request.method == "GET":
        return "To access this service send a POST request to this URL with" \
               " the text you want analyzed in the body."
    body = flask.request.data.decode("utf-8")
    sentiments = get_sentiments(body)
    return flask.json.dumps(sentiments)
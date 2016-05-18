import sys
from wordcloud import WordCloud

stops = ["POTUS","https","http","a","about","above","after","again","against","all","am","an","and","any","are","aren't","as","at","be","because","been","before","being","below","between","both","but","by","can't","cannot","could","couldn't","did","didn't","do","does","doesn't","doing","don't","down","during","each","few","for","from","further","had","hadn't","has","hasn't","have","haven't","having","he","he'd","he'll","he's","her","here","here's","hers","herself","him","himself","his","how","how's","i","i'd","i'll","i'm","i've","if","in","into","is","isn't","it","it's","its","itself","let's","me","more","most","mustn't","my","myself","no","nor","not","of","off","on","once","only","or","other","ought","our","ours","ourselves","out","over","own","same","shan't","she","she'd","she'll","she's","should","shouldn't","so","some","such","than","that","that's","the","their","theirs","them","themselves","then","there","there's","these","they","they'd","they'll","they're","they've","this","those","through","to","too","under","until","up","very","was","wasn't","we","we'd","we'll","we're","we've","were","weren't","what","what's","when","when's","where","where's","which","while","who","who's","whom","why","why's","with","won't","would","wouldn't","you","you'd","you'll","you're","you've","your","yours","yourself","yourselves"]


def genWordCloud(filename):
    text = open(filename).read()
    words = WordCloud(width=500, height=500, font_path='/Library/Fonts/Trebuchet MS.ttf', stopwords=stops)
    words.generate(text)
    words.to_file(filename.split('.')[0] + '.png')

if __name__ == '__main__':
    filename = sys.argv[1]
    genWordCloud(filename)

# filename = {0}
#
# text = open(filename).read()
# words = WordCloud(width=500, height=500, font_path='/System/Fonts/LastResort.ttf')
# words.generate(text)
# words.to_file(filename.split('.')[0] + '.png')

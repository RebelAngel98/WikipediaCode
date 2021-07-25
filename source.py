# import pyttsx3
import wikipedia
import sumy
from sumy.nlp.tokenizers import Tokenizer
from sumy.parsers.plaintext import PlaintextParser
from sumy.summarizers.lex_rank import LexRankSummarizer

# pyttsx3 is the voices (david & Zira for Windows)
# wikipedia is of course the online sources
# sumy, I didn't use, however we did import a lot of stuff from Sumy

# converter = pyttsx3.init()

# def speaks_lines(lines_to_speak):
#     # init my convertor
#     converter = pyttsx3.init()
#
#     # setting the voice as zira, not David
#     # using the code for Zira down below that will be used in the set.Property
#     zira = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
#     converter.setProperty('voice', zira)
#
#     # set properties for speaking
#     # Speed Property - how fast AI talks
#     # normal values being 1-100
#     converter.setProperty('rate', 165)
#
#     # Volume Property
#     # between 0-1 ; use decimals for percentages
#     converter.setProperty('volume', 1)
#
#     # AI speaking for first time
#     # Each say command is like a person talking/pausing
#     # Loading information for AI to say
#     converter.say(lines_to_speak)
#
#     # AI speaking outloud command
#     converter.runAndWait()


def read_file_by_line():
    # a txt file that is holding all the information
    my_file = open("memory.txt", "r")
    print(my_file.read)
    my_file.close()

def write_file_by_line(line_to_write):
    # Writing all the information that is given to the txt file
    my_file =open("memory.txt", "a")
    my_file.write(str(line_to_write))
    my_file.close()

def summarize_research():
    # testing_data = ""
    # summarizes all the information in the summary of research.
    # down to about two lines of sentences
    parser = PlaintextParser.from_string(summarize_research , Tokenizer("english"))
    # The Summarizer that Sumy is using
    # LexRank - one algorithm to summarize data
    summarizer = LexRankSummarizer()
    # how many sentences to summarize
    number_of_sentences = 1
    summary = summarizer(parser.document, number_of_sentences)
    print("\n\n\t\t***SUMMARY OF INFORMATION ABOVE***")
    for sentence in summary:
        print(sentence)
        write_file_by_line(sentence)
    # Show file contents
    read_file_by_line()


def main():
    print("_" * 100, "\n")
    # inserting a greeting because it brings in a bit more UX to the program
    print("\n\n\t\t===Welcome to Retarded Wikipedia!===\n\n")
    print("\n\n\t\t==Directions: Once the question pops up, please type in something you wish to research.==")
    # having the user choose their topic
    user_topic_choice = input("\n\n\t\t****What Do You Want to Research?***")
    print("_" * 100, "\n")
    # the beginning of researching on Wiki
    my_research = wikipedia.page(user_topic_choice)
    # down below this is the research, summary, content, and references, all sorted into topics
    print("\n\n\t\t***Research on " + user_topic_choice + "***")
    print("_" * 100, "\n")

    print("\n\n\t\t***SUMMARY***\n\n")

    summary = my_research.summary
    # print("summary=", type(summary))
    # ^ didn't work correctly
    print(summary)
    # speaks_lines(summary)
    print("_" * 100, "\n")

    # Summary, Content, and References are all about the same
    # using a print statement to grasp the information from the WIKI page
    # the first print statement is the title
    # last print statement is literally just to make the project look pretty.
    print("\n\n\t\t***CONTENT***\n\n")
    print(my_research.content)
    print("_" * 100, "\n")

    # see above comments
    print("\n\n\t\t***REFERENCES***\n\n")
    research_references_raw = my_research.references;
    # printing each references that show up
    print(my_research.references)
    for each_ref in research_references_raw:
        print(each_ref)
    print("_" * 100, "\n")
    summarize_research()


if __name__ == "__main__":
    main()

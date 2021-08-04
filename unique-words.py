# This program scans an entire text file
# and returns only the unique words

def main():

    # Open file
    poem = open('Hamlet_2B_or_not_2B.txt', 'r')

    # Read the entire text file
    content = poem.read()

    # Loop through text file to return each line
    while content != '':
        # Remove all punctuation to isolate only unique words
        content = content.replace(':','').replace('!','').replace(',','')\
        .replace('?','').replace('.','')
        content = content.lower()

        # Create a set which will only return unique words
        line = set(content.split())
        print(line)
        content = poem.read()
        
    # Close the text file
    poem.close()
    
main()
    


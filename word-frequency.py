# This program counts the frequency of each word.

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
        

        # Split the text into unique words
        line = content.split()

        # Initialize variable to count repeating words        
        count = {}

        # Loop through each word and find multiples
        for words in line:
            if words not in count.keys():
                count[words] = 0
            count[words] =+ count[words]+1

        # Display word frequency
        print(count)
             
        content = poem.read()

    # Close the text file
    poem.close()
    
main()
    


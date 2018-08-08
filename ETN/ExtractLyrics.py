import os

if __name__ == '__main__':

    #song_id,song_length,genre_ids,artist_name,composer,lyricist,lyrics,language

    for line in open("./metadata.csv" , 'r'):

        line = line.split(',')
        print("Open File " + line[0] + "...")

        #remove newline
        line[len(line)-1] = line[len(line)-1].rstrip('\n')

        #processing lyrics with common
        if len(line) > 8:
            line[6:len(line)-1] = [''.join(line[6:len(line)-1])]

        #only handle English song
        if line[7] == '52':

            f = open("./lyrics/" + line[0] , 'w')
            print("Write Lyrics " + line[0] + "...")
            f.write(line[6])
            f.close()

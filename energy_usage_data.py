fname = "/home/pi/josh/CTA_EWH/build/debug/log.csv"

# Function to read
# last N lines of the file
N = 1

def LastNlines(fname, N):
    with open(fname, 'rt') as file:
        # loop to read iterate
        # last n lines and print it
        for line in (file.readlines()[-N:]):
            print(line, end='')
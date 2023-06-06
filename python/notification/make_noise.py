import os 

def make_noise():
    '''Make noise after finishing executing a code'''
    duration = 1  # seconds
    freq = 440  # Hz
    os.system(f'play -nq -t alsa synth {duration} sine {freq}')

def main():
    even_arr = [i for i in range(10000) if i%2==0]
    make_noise()

if __name__=='__main__':
    main()
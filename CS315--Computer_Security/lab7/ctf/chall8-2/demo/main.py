from scipy.io import wavfile

if __name__ == "__main__":
    samplerate, data = wavfile.read('./output.wav')

    i = 0
    countsilent = 0
    samplefound = 0

    avg = []
    start = 0
    end = 0
    avg.append([0])

    for sample in data:
        i+=1
        if sample[1]<100:
            countsilent += 1
        if countsilent > 10000 and sample[1]>100:
            countsilent = 0
            #print(str(i)+": sample found")
            start = i
            samplefound = 1
        if countsilent > 8000 and samplefound==1:
            samplefound = 0
            #print(str(i)+": sample ended")
            end = i
            avg[len(avg)-1]=avg[len(avg)-1]/(end-start)
            print("avg: "+str(avg[len(avg)-1]))
            avg.append([0])
        if samplefound == 1:
            avg[len(avg)-1] += sample[1]

    alphabet = "abcdefghijklmnopqr stuvwxyz"
    avg_1 = {}
    i = 0
    res = ""

    for value in avg:
        if str(value) not in avg_1:
            avg_1[str(value)] = alphabet[i]
            i += 1
        res += avg_1[str(value)]
    print(res)

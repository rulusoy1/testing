def mode(lis):
    frequencies = [1] * len(lis) #each number occurs at east 1
    for i in range(len(lis)): #i from 0 to len-1
        for j in range(i+1, len(lis)): #j from i+1 to len-1
            if (lis[j] == lis[i]):  #if current value equal to current i
                frequencies[i] += 1  #increment the frequency of i
    maxFrequency = max(frequencies)  #maximum frequency
    posMaxFrequency = frequencies.index(maxFrequency)  #position of maximum frequency
    modeValue = lis[posMaxFrequency]  #value in that position in original list
    return modeValue  #return this value which is the mode

            
        

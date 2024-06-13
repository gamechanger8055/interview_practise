# ["This", "is", "a", "classic", "implementation", "of", "the", "sample", "lil", "project"], 16
# This     is    a
# classic
# implementation
# of the project

def textJustification(words,maxLength):
    curr_length,curr_line,result=0,[],[]
    for word in words:
        if curr_length+len(curr_line)+len(word)>maxLength:
            for i in range(maxLength-curr_length):
                #adding 1 to remove exception for 0 in case len(curr_line) is 0 or 1
                curr_line[i%(len(curr_line)-1 or 1)]+=' '
            result.append("".join(curr_line))
            curr_line,curr_length=[],0
        curr_line+=[word]
        curr_length+=len(word)
        print(curr_line,curr_length)
    result.append(" ".join(curr_line).ljust(maxLength))
    return result

words=["This", "is", "a", "classic", "implementation", "of", "the", "sample", "lil", "project"]
maxLength=16
print(textJustification(words,maxLength))
# thisisa

# [t,h,i,s]->this





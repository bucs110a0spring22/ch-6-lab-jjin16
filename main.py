
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: None
    """
    count=0
    while(n != 1):
        #print(n)
        if(n % 2) == 0:        # n is even
            n = n // 2
        else:                 # n is odd
            n = n * 3 + 1
        count+=1
    return count
    #print(n)                  # the last print is 1

def main():
    upper_bound= int(input("Upper bound:"))
    start=1
    if upper_bound<=0:
      quit()
    for start in range(upper_bound):
      print(start)
  	  count_result= seq3np1(start)
      print(count_result)
      start+=1
main()

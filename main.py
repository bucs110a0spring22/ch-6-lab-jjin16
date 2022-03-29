import turtle
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
def line_graph(upper_bound=0, count_result=0):
  max_so_far=0
  extra_space=10
  right_angle=90
  window= turtle.Screen()
  if max_so_far< count_result:
    max_so_far= count_result
  window.setworldcoordinates(0,0,upper_bound+extra_space, max_so_far+extra_space)
  myturtle= turtle.Turtle()
  myturtle.pu()
  myturtle.goto(0,0)
  myturtle.pd()
  myturtle.fd(upper_bound)
  myturtle.pu()
  myturtle.gotp(0,0)
  myturtle.lt(right_angle)
  myturtle.pd()
  myturtle.fd(max_so_far)
  myturtle.pu()
  myturtle.goto(upper_bound, count_result)
  myturtle.dot()
  
def main():
  upper_bound= int(input("Upper bound:"))
  #start=1
  if upper_bound<=0:
    quit()
  for start in range(1,upper_bound+1):
    print(start)
    count_result=seq3np1(start)
    print(count_result)
    line_graph(upper_bound, count_result)
    start+=1
    
main()

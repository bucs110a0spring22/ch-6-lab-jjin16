import turtle
import time
def seq3np1(n):
    """
        Print the 3n+1 sequence from n, terminating when it reaches 1.
        args: n (int) starting value for 3n+1 sequence
        return: count (int) loop count
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
def line_graph(upper_bound=0):
  """
        draws the function graph
        args: upper_bound (int) upper limit of the range in for loop
        return: None
  """
  max_so_far=0
  extra_space=10
  right_angle=90
  window= turtle.Screen()
  graphing_turtle=turtle.Turtle()
  writing_turtle=turtle.Turtle()
  window.setworldcoordinates(0,0,upper_bound+extra_space, max_so_far+extra_space)
  graphing_turtle.pu()
  graphing_turtle.home()
  graphing_turtle.pd()
  graphing_turtle.fd(upper_bound)
  graphing_turtle.pu()
  graphing_turtle.home()
  graphing_turtle.lt(right_angle)
  graphing_turtle.pd()
  graphing_turtle.fd(max_so_far)
  graphing_turtle.pu()
  writing_turtle.pu()
  writing_turtle.goto(0,max_so_far)
  writing_turtle.write(f"Maximum so far: {1}, {max_so_far}")
  for start in range(1, upper_bound+1):
    result=seq3np1(start)
    if max_so_far<result:
      max_so_far=result
      window.setworldcoordinates(0,0,upper_bound+extra_space, max_so_far+extra_space)
      updating_axis(upper_bound,max_so_far)
      writing_turtle.clear()
      writing_turtle.pu()
      writing_turtle.goto(0,max_so_far)
      writing_turtle.write(f"Maximum so far: {start}, {result}")
    graphing_turtle.pd()
    graphing_turtle.goto(start,result)
    graphing_turtle.dot()
  window.exitonclick()
def updating_axis(x_axis_length=0, y_axis_length=0):
  """
        redraws the length of the axis to fit the graph
        args: 
        x_axis_length (int) x-axis length
        y_axis_length (int) y-axis length
        return: None
  """
  axis=turtle.Turtle()
  hidden_turtle_size=0.01
  axis.shapesize(hidden_turtle_size)
  right_angle=90
  axis.pu()
  axis.home()
  axis.pd()
  axis.fd(x_axis_length)
  axis.home()
  axis.lt(right_angle)
  axis.fd(y_axis_length)
def main():
  """
        uses the defined functions to run the program
        args:   None
        return: None
  """
  upper_bound= int(input("Upper bound:"))
  if upper_bound<=0:
    quit()
  for start in range(1,upper_bound+1):
    print(start)
    count_result=seq3np1(start)
    print(count_result)
    start+=1
  line_graph(upper_bound)
  
main()
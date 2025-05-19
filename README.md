

[wikipedia article](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction)
[reed solomon explained](https://youtu.be/1pQJkt7-R4Q?si=NskXnJ7DCiLB1_z7)
[reed solomon encoding simplified](https://youtu.be/3HRIeWYbIuI?si=PC215nO0uAjgr2l1)
[lagrange interpolation](https://youtu.be/nvkX1Bd90Gk?si=JS0mckhXKG3XpEQl)
[desmos example](https://www.desmos.com/calculator/sdvedp28bp)
[python code](https://github.com/llaammbbddaa/linearAlgebraProject1)

**LAGRANGE INTERPOLATION**
**REED-SOLOMON CODES**

research and explain an application of linear algebra that you find interesting
- write two to three paragraphs describing what you found out about this application
- give two references you consulted for your research
**DUE FEB 3RD**

**essay here**
	For my application of Linear Algebra, I chose Lagrange Interpolation and Reed-Solomon Codes. As a form of implementation I created a program in Python that took in a string of letters turning it into a list of relevant ASCII values. The ASCII values along with the corresponding indexes provided a set of points on a graph, which then through Lagrange Interpolation would convert them into a polynomial of degree *n - 1*. *(Where n is the length of the string / list)* Depending on user input, a few points, from the function, would be added to the overall list. *(The ASCII Values of the string, along with some function values from the derived function.)*
	The way Reed-Solomon encoding works is we can lose as many extra function values we have appended from the derived function and still get the original message back. This works because if we lose a couple of the values, we can still use the other values to get the original derived function, and then get the original message. *(As long as the number of remaining bits is greater than or equal to the original message length)* This is used in a variety of places, for example, CD Data Recovery. Whenever a CD is mildly scratched, it can still play the full song(s) as a result of the Reed-Solomon Encoding. I feel that it is a great example of how there can be unintended applications for new findings in math.

#school #math

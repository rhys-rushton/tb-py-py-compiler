- First specification for Tiny Basic was made by Dennis Alison. Made in response to Bill gates ragging about people pirating software. So they decided to make a lightweight portable version that was free.

- How is the problem to be solved? Divide and Conquer. 

# Breakdown of problem": 
* Supervisor - determines what is to be done next. Receives controls when BASIC is loaded. 
* Program line editor: Input storage. 
* Line executor routine that executes a single BASIC statement. 
* A line sequence which dtermines which line is to be executed next. 
* Floating point package to handle floating point on a machine without the hardware. 
* Terminal I/O handler to input and output information from the teletype and provide simple editing (backspace and line deletion)
* function package for all the BASIC functions
* error handling routine (part of the supervisor)
* memory management program whcih provides dynamic allocation fo data objects. 

# The tiny basic specification
* Integer Arithmetic 8-bits, 16 bits - you decide!
* 26 Variables: A, B, C, D
* RND Function
* Seven BASIC statement types: 
** INPUT, PRINT, LET, GO TO, IF, GOSUB, RETURN
* Strings? Only in print() statements
* Only 256 Line programs - totally arbitrary now but that was the actual constraint at the time - I think implement this but then also have an override option in the CLI when you compile.


# Extension Ideas
- Overide the number of lines limit. 
- Floating Point Arithmetic. 
- Logarithmic and trigonmetirc calculation capability. 

# Some Random Resources I came across (Old Skool)
- Compiler Construction For Digital COmputers - David Gires
- Theory and Application of a Bottom-Up Syntact Directed Transaltor - Harvey Abramson
- Compiling Techniques - Hopgood. 



# Welcome to GNM (Gauss Nunca Mais) 2.0.0
<p>The system has been optmized and became a "micro-language" that parses commands and applies them to as many matrices as you want!</p>

## CREATING YOUR FIRST MATRIX:
<p>To create a Matrix, you must assign a new Matrix object into a variable. To assign a new variable, type in the name of the variable followed by an equals sign (=).</p>
<p>
Ex:
    <pre>"Run Command | variable1 = ..."</pre>
</p>
<p>Then we need to define a scope. Since we're working with Matrices, the scope is "m". Once we have
defined the scope, we can use one of the functions available in that scope. We're gonna use "create" here.</p>
<p>Ex:
<pre>"Run Command | matrix1 = m create ..."</pre>
</p>
<p>Now time to give our Matrix an identity. The <b>create</b> function accepts a single argument which is the
Matrix itself. You can build the Matrix just like in <i>MATLAB</i>, by separating columns with <b>SPACES</b> and rows
with <b>SEMICOLONS</b> (;).</p>
<p>For example, we want to build:
<pre>
| 1 2 |
| 3 4 |
</pre>
So we type in:
<pre>Run Command | matrix1 = m create 1 2; 3 4"</pre>
The system still accepts fractions and decimals to build and operate with matrices:
<pre>Run Command | matrix1 = m create 1/2 2; 3/4 4"</pre> would build:
<pre>
| 1/2 2 |
| 3/4 4 |
</pre>
</p>
<h2>OPERATING WITH MATRICES</h2>
<p>
To operate with matrices, we can use the "swap", "scale" and "add" functions present in the same "m" scope.
The difference is that since we're operating with matrices that are already stored in variables, we use
the variables' name as a scope! That allows us to operate with multiple matrices at the same time.
</p>
<
    Example:
        "Run Command | matrix1 scale 1 1/2" would multiply matrix1's first line by 0.5;
        "Run Command | matrix1 swap 1 3" would swap matrix1's line 1 with line 3; and
        "Run Command | matrix2 add 3 -2 1" would add matrix2's line 3 by line 1 * (-2).

## USING THE VAR SCOPE
    The "var" (variable) scope comes to make it easier to work with multiple matrices at the same time. Allowing to,
in the future, perform operations like add, subtract and multiple matrices. The available functions for the
"var" scope are:
    1. "all" [no arguments] prints all current variables stored in the system's memory alongside their value. If we had created
two matrices "matrix1" and "matrix2" before and we used "Run Command | var all", all the matrices in their current
form would be printed;
    
    2. "del" [variable1, ...] deletes all the provided variables. Again, if we had matrix1 and matrix2 currently
loaded in the system, we could either:
    "Run Command | var del matrix1" -> destroys matrix1 from the system, remaining only matrix2;
    "Run Command | var del matrix2" -> destroys matrix2 from the system, remaining only matrix1;
    "Run Command | var del matrix1 matrix2"-> destroys both matrix1 and matrix2 simultaneously.

    3. "show" [variable1, ...] displays all the provided variables. Same thing as "var all" but you can limit
what variables you want to display. For example:
    "Run Command | var show matrix1" -> displays only matrix1;
    "Run Command | var show matrix2" -> displays only matrix2;
    "Run Command | var show matrix1 matrix2" -> displays both matrix1 and matrix2 simultaneously.

    4. "focus" [variable] focuses all operations on that specific variable. Since it's annoying and not efficient
to keep typing the variable's name everytime we want to operate with it, specifically when we're working with a
single variable, we can use the "focus" function so we don't have to mention which variable we're working with.
    Example:
        "Run Command | var focus matrix1" -> focuses on matrix1. Now all operations will be applied to matrix1;
        "Run Command | scale 1 1/2" -> performs the same as "Run Command | matrix1 scale 1 1/2".

    5. "reset" [no arguments] resets the focused variable. Not necessary if you have previously deleted the
variable with "var del". Use this if you want to operate with another variable after having focused on a variable already.


    To leave the program, you can either use the built-in "Ctrl+C" hotkey (doesn't break the program anymore) or
use the "exit" command with no scopes ("Run Command | exit").


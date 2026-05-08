# Welcome to GNM (Gauss Nunca Mais) 2.0.0
    The system has been optmized and became a "micro-language" that parses commands and applies them
to as many matrices as you want!

## CREATING YOUR FIRST MATRIX:
    To create a Matrix, you must assign a new Matrix object into a variable. To assign a new variable,
type in the name of the variable followed by an equals sign (=).
    Ex:
        "Run Command | variable1 = ..."
    Then we need to define a scope. Since we're working with Matrices, the scope is "m". Once we have
defined the scope, we can use one of the functions available in that scope. We're gonna use "create" here.
    Ex:
        "Run Command | matrix1 = m create ..."
    Now time to give our Matrix an identity. The "create" function accepts a single argument which is the
Matrix itself. You can build the Matrix just like in MATLAB, by separating columns with SPACES and rows
with semicolons (;).
    For example, we want to build:
| 1 2 |
| 3 4 |
    So we type in:
        "Run Command | matrix1 = m create 1 2; 3 4"
    The system still accepts fractions and decimals to build and operate with matrices:
        "Run Command | matrix1 = m create 1/2 2; 3/4 4" would build:
| 1/2 2 |
| 3/4 4 |

## OPERATING WITH MATRICES
    To operate with matrices, we can use the "swap", "scale" and "add" functions present in the same "m" scope.
    The difference is that since we're operating with matrices that are already stored in variables, we use
the variables' name as a scope! That allows us to operate with multiple matrices at the same time.
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


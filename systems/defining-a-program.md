# What is a Program?

a program is a sequence of isntructions that specifies how to perform a computation. The computation might be something mathematical or a symbolic computation; ie. searching and replacing text within a document; or, processing graphical images or videos into different encodings; streams; formats etc...

### Common instructions which appear within mostly all programs
regardless of the languages which it is being written in; the basic recipe for the creation of program consists of:
**input**: Retrieve data from something(keyboard, text-file, url, network-address or device information)
**output**: Display the data on the screen; save it within a file; parse its contents into less pre-processor, send it over the network etc ..
**math**: Perform basic mathematical operations with the data such as : addition, multiplication, division...
**conditional execution**: Check for certain pre-defined conditions and depending on the underlying results either run the program or display an error msg.
**repetition**: Perform some action repeatedly, usually with some variation.

> __ So you can think of programming as the process of breaking a large, complex task into smaller and smaller subtasks until the subtasks are simple enough to be performed with one of the basic instructions.__

#### Formal and Natural Languages
> Programming languages are **formal languages** that have been designed to express computations.

__Formal Languages__: tend to have strict syntax rules that govern the structure of statements.
__Syntax Rules__ come in two flavors, pertaining to **tokens** and structures. Tokens are the basic elements of the language, such as: words, numbers and chemical elements. 
The second type of syntax rule pertains to the way tokens are combined. 
> When you read a sentence in English or a statement in a formal language, you have to figure out the structure (although in a natural language you do this subconsciously). This process is called parsing.
** Differences btw natural and formal languages**: 
**ambiguity: **Natural languages are full of ambiguity, which people deal with by using con- textual clues and other information. Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly one meaning, regardless of context. 
**redundancy: **In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a result, they are often verbose. Formal languages are less redundant and more concise. 
**literalness: **Natural languages are full of idiom and metaphor. If I say, “The penny dropped”, there is probably no penny and nothing dropping (this idiom means that someone understood something after a period of confusion). Formal languages mean exactly what they say. 

#### Debugging
Programmers make mistakes. For whimsical reasons, programming errors are called **bugs **
and the process of tracking them down is called **debugging**.
Programming, and especially debugging, sometimes brings out strong emotions. If you 
are struggling with a difficult bug, you might feel angry, despondent, or embarrassed. 
There is evidence that people naturally respond to computers as if they were people. When they work well, we think of them as teammates, and when they are obstinate or rude, we respond to them the same way we respond to rude, obstinate people (Reeves and Nass, _The Media Equation: How People Treat Computers, Television, and New Media Like Real People and Places_). 
Preparing for these reactions might help you deal with them. One approach is to think of the computer as an employee with certain strengths, like speed and precision, and partic- ular weaknesses, like lack of empathy and inability to grasp the big picture. 
Your job is to be a good manager: find ways to take advantage of the strengths and mitigate the weaknesses. And find ways to use your emotions to engage with the problem, without letting your reactions interfere with your ability to work effectively. 
Learning to debug can be frustrating, but it is a valuable skill that is useful for many activ- ities beyond programming. At the end of each chapter there is a section, like this one, with my suggestions for debugging. I hope they help! 

##### Section I: Glossary
**problem solving: **The process of formulating a problem, finding a solution, and express- 
ing it. 
**high-levellanguage: **AprogramminglanguagelikePythonthatisdesignedtobeeasyfor humans to read and write. 
**low-level language: **A programming language that is designed to be easy for a computer to run; also called “machine language” or “assembly language”. 
**portability: **A property of a program that can run on more than one kind of computer. 
**interpreter: **A program that reads another program and executes it 
**prompt: **Characters displayed by the interpreter to indicate that it is ready to take input from the user. 
**program: **A set of instructions that specifies a computation. 
**print statement: **An instruction that causes the Python interpreter to display a value on 
the screen. 
**operator: **A special symbol that represents a simple computation like addition, multipli- cation, or string concatenation. 
**value: **One of the basic units of data, like a number or string, that a program manipulates. **type: **A category of values. The types we have seen so far are integers (type int), floating- 
point numbers (type float), and strings (type str).
**integer: **A type that represents whole numbers.
**floating-point: **A type that represents numbers with fractional parts.
**string: **A type that represents sequences of characters.
**natural language: **Any one of the languages that people speak that evolved naturally. 
**formal language: **Any one of the languages that people have designed for specific pur- poses, such as representing mathematical ideas or computer programs; all program- ming languages are formal languages. 
**token: **One of the basic elements of the syntactic structure of a program, analogous to a word in a natural language. 
**syntax: **The rules that govern the structure of a program.
**parse: **To examine a program and analyze the syntactic structure. **bug: **An error in a program.
**debugging: **The process of finding and correcting bugs. 
----
## Section II: Variables, expressions and Statements
one of the most powerful features of a programing language is the ability to manipulate variables. A variable is a name that refers to a particular, pre-defined, specific value.

#### 2.1 Assignment Statements:
an assignment statement creates a new variable and gives it a value: 
>>> mesage = 'And now for something completely different.'
>>> n = 17
>>> pi = 3.1415926535897932
the above example states three assignments: The first assigns a string to a new variable named message;
the second gives the integer 17 to n;
the third defines the approximate  value of pi.
> A common way to represent variables on paper is to write the name with an arrow pointing to its value. This kind of figure is called a **state diagram **because it shows what state each of the variables is in (think of it as the variable’s state of mind). Figure 2.1 shows the result of the previous example. 

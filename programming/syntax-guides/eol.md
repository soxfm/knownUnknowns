---
title: end-of-line-notes
slugs: eol
tag_list: ['programming, 'coding', 'best-practices', 'notation', 'syntax']
date: 2020-12-9
---

# End of Line Notes

Notes on dealing with end-of-line characteristics.

- Different operating systems handle eol in different manners.
- Within windows operating systems : CRLF \ (Carriage Rerturn Line Feed)\
- Within UNIX/MacOS Systems: LF denotes end of line.
- Git's solution is specify that **LF** is the best way to sotre line endings for _text files_ in a Git repository's object database.

### core.eol

- core.eol = native the default: whenever git normalizes line endings in files within a repository it will default to the natize Operating Systems' default ling ending structure.
- core.eol = crlf : crlf will denote line endings
- core.eol = lf : LF will denote line endings

### in and out of the object database
(minding the end of line)[https://adaptivepatchwork.com/2012/03/01/mind-the-end-of-your-line/]
> All you need to know is that when you do something like git commit you are writing objects into the database. This involves taking the files that you are committing, calculating their shas and writing them into the object database as blobs. This is what I mean when I say writing to the object database and this is when Git has a chance to run filters and do things like converting line endings.
> The other place that Git has a chance to run filters is when it reads out of the object database and writes files into your working directory. This is what I mean when I say writing out into the working directory. Many commands in Git do this, but git checkout is the most obvious and easy to understand. This also happens when you do a git clone or run a command like git reset that changes your working directory.

## .GitAttributes File

The new system moves to defining all of this in the .gitattributes file that you keep with your repository. This means that line endings can be encapsulated entirely within a repository and don’t depend on everyone having the proper global settings.

In the new system you are in charge of telling git which files you would like CRLF to LF replacement to be done on. This is done with a text attribute in your repository’s .gitattributes file. In this case the man page is actually quite helpful. Here are some examples of using the text attribute:

- \*\.txt : text set all files matching the filter .txt to be text. This means that Git will run CRLF to LF replacement on these files every time they are written to the object database and the rever replacement will be run when writing out to the working directory
- \*\.txt -text : Unset all files matching the filter. These files will never run through the CRLF to LF replacement
- \*\.txt text=auto Set all files matching the filter to be converted, CRLF to LF, if those files are determined by Git to be text and not binary. This relies on Git's built in binary detection ehuristics.

Example .gitattributes files for a C# project
```
# These files are text and should be normalized (convert crlf =&gt; lf)
*.cs      text diff=csharp
*.xaml    text
*.csproj  text
*.sln     text
*.tt      text
*.ps1     text
*.cmd     text
*.msbuild text
*.md      text

# Images should be treated as binary
# (binary is a macro for -text -diff)
*.png     binary
*.jepg    binary

*.sdf     binary
```

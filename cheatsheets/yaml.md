---
title: yaml
slugs: yaml
tag_list: [ 'programming', 'code', 'languages', 'syntax', 'cheatsheets' ]
date: 2020-12-22
---

## YAML: Yet Another Markup Language

Yaml is a data-serialization laguange often used for configuration files, such as Open API specifications or CI/CD pipelines.

### Basic Syntax

YAML documents are basically a colleciton of key-value pairs where the value can be as simple as a string or as complex as a tree.
**Basic Properties**
  - Indentation is used to denote structure: **TABS** are note allowed and the amount of whitespace doesn't matter as long as the child node is more indented than the parent.
  - UTF-8, UTF-16, and UTF-32 encodings are allowed.

### STRINGS
```yaml
# Strings don't require quotes:
title: Introduction to YAML

# But you can still use them:
title-w-quotes: 'Introduction to YAML'

# Multiline Strings start with pipe symbol | 
execute: |
    npm ci
    npm build
    npm test
```

the above code translated into JSON:

```json
{
    "title": "Introduciton to YAML",
    "title-w-quotes": "Introdution to YAML",
    "execute": "npm ci\nnpm build\nnpm test\n"
}
```

```yaml
# Boolean values can be written in various ways
published: false
published: FALSE
published: False

# Null values can be represented by simply ommiting a value:
null-value: 

# or more explicitly:
null-value: null 
null-value: NULL
null-value: Null

# Dates and TimeStamps
# ISO-Formated dates can be used, like so:
date: 2020-12-14
canonical: 2020-12-14T03:09:55.1Z
iso8601: 2020-12-14t15:09:55.10-05:00
spaced: 2020-12-14 15L03L44.10 -5

# Sequences allow us to define YAML lists
# A list of numnbers using hyphens:
numbers:
  - one
  - two
  - three

# Inline Version
numbers: [ one, two, three ]
```

### Nested Values
```yaml
# Moral Tribes NonFiction Book Data
moral-tribes:
  author: Joshua Greene
  published-at: 2013
  page-count: 421
  description: | 
      "Moral Tribes is a masterpiece - a landamark work brimming with originality and insight that also happens to be wickedly fun to read. The only dissapointing thing about this book is that it ends" - Daniel Gilbert, professor of Psychology, Harvard University. 
```

### Reusability with Node Anchors

Node Anchors mark a node for future reference, which allow us to reuse the node. To mark a node we use the & character, and to trefrence it we use *

In the following list we'll define a list of books and reuse the author data, so we only have to define it once.
```yaml
# The author data:
author: &gOrwell 
    name: George
    last-name: Orwell

# Some books:
books: 
    - 1984:
        author: *gOrwell 
    - animal-farm:
        author: *gOrwell
```

### Explicit data types with tags
YAML autodetects the type of our values, but it's possible to specify which type we want. We specify the type by including it before the value preceeded by !!.
Example:
```yaml
# The following value should be an int, no matter what:
should-be-int: !!int 3.2

# Parse any value to string:
should-be-string: !!str 30.25

# I need the next value to be boolean:
should-be-boolean: !!bool yes
```

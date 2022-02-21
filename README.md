# String-Calculator-TDD-Kata

- Create a simple String calculator with a method signature:

```python
int Add(string numbers)
```

&emsp;&emsp;The method can take up to two numbers, separated by commas, and will return their sum.

&emsp;&emsp;For example "" or "1" or "1,2" as inputs. (for an empty string it will return 0)

&emsp;&emsp;Hints:

&emsp;&emsp;Start with the simplest test case of an empty string and move to one and two numbers
<br> &emsp;&emsp;Remember to solve things as simply as possible so that you force yourself to write tests you did not think about
<br> &emsp;&emsp;Remember to refactor after each passing test

- Allow the Add method to handle an unknown amount of numbers

- Allow the Add method to handle new lines between numbers (instead of commas).

&emsp;&emsp;The following input is ok: "1\n2,3" (will equal 6)
<br> &emsp;&emsp;The following input is NOT ok: "1,\n" (not need to prove it - just clarifying)

- Support different delimiters

&emsp;&emsp;To change a delimiter, the beginning of the string will contain a separate line that looks like this: "//[delimiter]\n
<br> &emsp;&emsp;[numbers…]" for example "//;\n1;2" should return three where the default delimiter is ";"
<br> &emsp;&emsp;The first line is optional. all existing scenarios should still be supported

- Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that was passed.

&emsp;&emsp;If there are multiple negatives, show all of them in the exception message.

Link to Kata: https://blog.incubyte.co/blog/tdd-assessment/
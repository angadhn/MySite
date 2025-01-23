---
title: Bon appétit!
---

{% newthought 'In his later books' %}, Tufte starts each section with small caps...

Page titles with accents are supported. But is $$1$$ in $$\LaTeX$$?

## Equations

The Markdown parser being used by this Jekyll theme is Kramdown, which contains some built-in [Mathjax](//www.mathjax.org) support. Both inline and block-level mathematical figures can be added to the content.

For instance, the following inline sequence:

*When $$ a \ne 0 $$, there are two solutions to $$ ax^2 + bx + c = 0 $$*

is written by enclosing a Mathjax expression within *a matching pair of double dollar signs: ```$$```*:

```When $$ a \ne 0 $$, there are two solutions to $$ ax^2 + bx + c = 0 $$```

Similarly, this block-level Mathjax expression:

$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$

is written by enclosing the expression within a pair of ```$$``` with an empty line above and below:

```$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$```


You can get pretty fancy, for instance, the wave equation's nabla is no big thing:

$$ \frac{\partial^2 y}{\partial t^2}= c^2\nabla^2u $$


All of the standard <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> equation markup is available to use inside these block tags.

Please note that the block-level Mathjax expressions *must* be on their own line, separated from content above and below the block by a blank line for the Kramdown parser and the Mathjax javascript to play nicely with one another.

The Mathjax integration is tricky, and some things such as the inline matrix notation simply do not work well unless allowances are made for using the notation for a small matrix. Bottom line: If you are using this to document mathematics, be super careful to isolate your <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> blocks by blank lines!  


Here's some text with a sidenote{% sidenote 'sn-id-1' 'This is a sidenote with a superscript' %}

And here's text with a margin note{% marginnote 'mn-id-1' 'This is a margin note without a superscript' %}

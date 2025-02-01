---
title: This Site
published: 2025-01-22
tags:
  - site
  - aesthetics
permalink: ObsidianToTufteWorkflow
top_of_mind: "true"
---
I am a big-time and longtime fan of [Obsidian](https://obsidian.md)- it is my note-taking tool of choice both for its usability and, just as importantly, its [ethos](https://stephango.com/file-over-app) of avoiding the travails of lock-in. However, my use of it recently plateaued- perhaps, even dropped off a cliff- when I started working on creating a personal static website using Jekyll. This seemed absurd to me as the reason to build the website was that it generated pages from Markdown.

Part of the reason was that I was a novice website builder who had the tools but not the wisdom to integrate them. To move fast at getting a website running that wasn't merely Obsidian Publish (which is excellent[^1]!), I used the [Academic Pages](https://academicpages.github.io/) template- again, a great open source template to get oneself out there. I then started working with ChatGPT and Claude to start tweaking that template to get it to have more of a Tufte-style using the excellent example of [clayh53's Jekyll site](https://clayh53.github.io/tufte-jekyll/articles/20/tufte-style-jekyll-blog). Merging this work into my template continued to drive my Obsidian use and, more generally, my writing as my focused turned to battling CSS and HTML in Vim with LLMs. I had never been further from my vision of  a seamless writing and publication workflow that integrated Obsidian to Jekyll- all of that code wrangling had also not got me closer to a site whose appearance matched my taste [^3]. I was lamenting the loss of Obsidian and knew deep down that I had to embark on a second disparate journey that let go of this template. The current site is the result of this effort.

In January 2025, I happened to stumble into a tweet that linked to [this post by Steph Ango](https://stephango.com/vault) on how he had was building his website from Obsidian leveraging Obsidian's Git plugin, Jekyll, Github, and Netlify- this sounds like a lot but believe me, reader, the initial setup is worth it and can be done under one hour[^4]. I also like thinkg that one day, what I write could be circulated- I saw Steph Ango uses ButtonDown to send out newsletters of some posts so thought why not put in the overhead now to get the potential for circulation out even if I never use it. This [blogpost](https://michaelsoolee.com/buttondown-newsletter-5-reasons/) made ButtonDown sound like a nice alternative to other options and [used the guidance for integration into Jekyll is here](https://buttondown.com/blog/netlify).

With the site built and ready for publication, I can officially say that my writing to publication workflow matches the friction-free vision I had. I am currently writing this post in markdown in Obsidian- no more use of Vim or Cursor for editing Markdown[^5]. Anyone who has written notes in Obsidian for a while knows why it's a desirable tool to work with. I can't place my finger on it but I think it is fantastic as a place to think, even without all the bells and whistles- an IDE-style writing vibes that's also minimal is criminally undervalued.

[^1]: I am a paying user for Obsidian Publish to host my notes at this time but it is likely that I will cancel that subscription eventually and reallocate the moeny to paying for Sync.
# Tufte customizations

The Jekyll customisations of the Tufte theme of this site is an attempt to create a design with the look and feel of Edward Tufte's books and handouts but with my own twist. My core philosophy is to get the good parts of Tufte by maximising the use of Markdown while minimising the use of Liquid tags which are really irritating to work with for fast writing. However, I am not directly lifting the Tufte style as I think there are things it could do better; instead, I am working with Cursor to adapt [clayh53's SCSS](https://github.com/clayh53/tufte-jekyll/blob/master/css/tufte.scss)[^6] to meet my needs.
## Fundamentals
### Headings
Like Tufte, I am trying to work with three levels of headings, tops- though more specific headings are not encouraged, I do have the option to go 6 levels deep. The following passage from Tufte is pretty interesting to consider:

> [It is] notable that the Feynman lectures (3 volumes) write about all of physics in 1800 pages, using only 2 levels of hierarchical headings: chapters and A-level heads in the text. It also uses the methodology of *sentences* which then cumulate sequentially into *paragraphs*, rather than the grunts of bullet points. Undergraduate Caltech physics is very complicated material, but it didn’t require an elaborate hierarchy to organize.
> 
> [Tufte site](http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0000hB)

The headings all make us of the Aniron font, which is free for non-commercial use, which this site is.
### Text
Inspired by [Gwern](https://gwern.net), I have instead made use of the Aniron font and make all the content of the first line of any post in all caps; the first character of any post makes use of dropcaps () That's because I wish to minimise my use of Liquid tags. Much of this was setup for me by Claude in Cursor- some css tweaking and a little bit of javascript and html magic. Instead Tufte starts each section with a bit of vertical space, a non-indented paragraph, and sets the first few words of the sentence in small caps.  {% sidenote 'two' '[http://www.edwardtufte.com/tufte/books_be](http://www.edwardtufte.com/tufte/books_be)'%}. Outside of  that body of the text currently makes use of [GIll Sans](https://www.edwardtufte.com/notebook/whats-your-font/).
### Epigraphs
The following are examples of epigraphs, generated on this website without Liquid tags.
> The English language . . . becomes ugly and inaccurate because our thoughts are foolish, but the slovenliness of our language makes it easier for us to have foolish thoughts.'
 > 
> George Orwell
> 
> Politics and the English Language

> For a successful technology, reality must take precedence over public relations, for Nature cannot be fooled.
> 
> Richard P. Feynman
> 
> What Do You Care What Other People Think?

This first of these examples is generated using Markdown formatting with the following snippet:
``` markdown
> The English language . . . becomes ugly and inaccurate because our thoughts are foolish, but the slovenliness of our language makes it easier for us to have foolish thoughts.'
> 
> George Orwell
> 
> Politics and the English Language
```

Note that this is created using Markdown; the first example of my getting rid of using Liquid tags thanks to Claude and Cursor. This allows a nice readable version of the epigraph in Obsidian as and a reasonably informative version on the site.
### Lists
Lists can be generated in standard markdown syntax but Tufte CSS points discourages using lists

> while lists have valid uses, they tend to promote ineffective writing habits due to their “lack of syntactic and intellectual discipline”. He is particularly critical of hierarchical and bullet-pointed lists.
> 
> [Tufte CSS](https://edwardtufte.github.io/tufte-css/)

It says that a writer must, instead, ask themselves:
- Would my idea be better expressed as sentences in paragraphs?
- Is my message causally complex enough to warrant a flow diagram instead?

More excerpts from Tufte CSS:
> A better way to understand Tufte’s thoughts on lists would be to read “The Cognitive Style of PowerPoint: Pitching Out Corrupts Within,” a chapter in Tufte’s book *Beautiful Evidence*, excerpted at some length by Tufte himself [on his website](http://www.edwardtufte.com/bboard/q-and-a-fetch-msg?msg_id=0002QF). The whole piece is information-dense and therefore difficult to summarize. He speaks to web design specifically, but in terms of examples and principles rather than as a set of simple do-this, don’t-do-that prescriptions. It is well worth reading in full for that reason alone.\
> For these reasons, Tufte CSS encourages caution before reaching for a list element, and by default removes the bullet points from unordered lists.
> 
> [Tufte CSS](https://edwardtufte.github.io/tufte-css/)

## Sidenotes
In text, I like the idea of Tufte's sidenotes{% sidenote 'sn-id-whatever' 'This is a sidenote and *displays a superscript*'%} which display a superscript- very similar to footnotes but without the disorienting scrolling behaviours. However, I have to be very judicious here as it requires using Liquid tags, which looks like this in markdown
``` markdown
{% sidenote 'sn-id-xx' 'This is a sidenote and *displays a superscript*'%}
```
Might get this sorted in the future; but as I said, this is a quite low priority as it is not just a matter of handling the Liquid tags with Claude[^7] but requires my own insight into how I write and how long these footnotes can get to convey sufficient information.
## Margin notes
Tufte’s style is well known for its extensive use of notes in margins- this was one of the driving forces for me modifying my previous site's template. My sense is that footnotes are disorienting for readers (this is how I feel but YMMV). The following Liquid tag snippet in my markdown file renders the margin note to the right {% marginnote 'mn-id-whatever' 'This is a margin note.' %}

``` markdown
 {% marginnote 'mn-id-whatever' 'This is a margin note.' %}
```

As you can see, this uses Liquid tags which makes for poor reading my markdown file and I am trying to eliminate their use as much as possible, even though the reading experience can be superior. So, at this moment, I am optimising for my writing process over reading[^7]. Thus, I use such notes sparingly.
### Main Column Figures
One place that you will see margin notes appear is when I insert an image, like of this rhino:

![F.J. Cole, “The History of Albrecht Dürer’s Rhinoceros in Zoological Literature,” *Science, Medicine, and History: Essays on the Evolution of Scientific Thought and Medical Practice* (London, 1953), ed. E. Ashworth Underwood, 337-356. From page 71 of Edward Tufte’s *Visual Explanations*.](assets/OldSite/rhino.png) 
which is generated using Markdown as so:
``` markdown
![F.J. Cole, “The History of Albrecht Dürer’s Rhinoceros in Zoological Literature,” *Science, Medicine, and History: Essays on the Evolution of Scientific Thought and Medical Practice* (London, 1953), ed. E. Ashworth Underwood, 337-356. From page 71 of Edward Tufte’s *Visual Explanations*.](assets/OldSite/rhino.png)
```
Within Obsidian, this gives me an image (without captions, which I can live with for my writing).
On the website, I have been able to build in some nifty behaviour: in most cases, captions appear on the right margin of an image but, on mobile screens, defaults to being under the image. I think this optimises for both my writing and reading experience. I think the power of this is best experienced in [[The winds have been howling for a hundred years at NASA's Virginia Research Center]], an article translated from Hungarian to English [^8].
### Full Width Figures and Margin Figures
I don't have a good solution in case a full-width image or figure must be included, like so:

{% fullwidth 'assets/OldSite/napoleons-march.png' "Napoleon's March *(Edward Tufte’s English translation)*" %}

which needs to use custom liquid tag is available to use. Oddly enough, it is named 'fullwidth', and this markup:

``` markdown
{{ "{% fullwidth 'assets/OldSite/napoleons-march.png' 'Napoleon's March *(Edward Tufte’s English translation)*' "}} %}
```
  
{% marginfigure 'mf-id-1' "assets/OldSite/exports-imports.png" "From Edward Tufte, *Visual Display of Quantitative Information*, page 92" %}

This is also true of margin figures
which again reads poorly in Obsidian:
``` markdown
{{ "{% marginfigure 'mf-id-whatever' 'assets/OldSite/rhino.png' 'F.J. Cole, “The History of Albrecht Dürer’s Rhinoceros in Zoological Literature,” *Science, Medicine, and History: Essays on the Evolution of Scientific Thought and Medical Practice* (London, 1953), ed. E. Ashworth Underwood, 337-356. From page 71 of Edward Tufte’s *Visual Explanations*.' "}} %}
```

## Equations
The Markdown parser being used by this Jekyll theme is Kramdown, which contains some built-in [Mathjax](//www.mathjax.org) support. The only thing I am unhappy about is the way inline math currently works.
For instance, the following inline sequence:

*When $$a \ne 0$$, there are two solutions to $$ ax^2 + bx + c = 0 $$*

is written by enclosing a Mathjax expression within *a matching pair of double dollar signs: ```$$```* like so:

``` markdown
When $$ a \ne 0 $$, there are two solutions to $$ ax^2 + bx + c = 0 $$
```

This renders poorly in Obsidian; where the equation is shown in a new line. Not a huge deal breaker but Obsidian is well capable of handling the more standard `$ a \ne 0 $` with single dollar signs either side of he equation. Outside of that, equations work about as expected.

Similarly, this block-level Mathjax expression is written by enclosing the expression within a pair of ```$$``` with an empty line above. You can get pretty fancy, for instance, the wave equation's nabla is no big thing:

$$ \frac{\partial^2 y}{\partial t^2}= c^2\nabla^2u $$

All of the standard <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> equation markup is available to use inside these block tags so I won't go into that here. Do note that the block-level Mathjax expressions *must* be on their own line, separated from content above and below the block by a blank line for the Kramdown parser and the Mathjax javascript to play nicely with one another. As [clayh53](https://clayh53.github.io/tufte-jekyll/articles/20/tufte-style-jekyll-blog) notes:
> The Mathjax integration is tricky, and some things such as the inline matrix notation simply do not work well unless allowances are made for using the notation for a small matrix. Bottom line: If you are using this to document mathematics, be super careful to isolate your <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> blocks by blank lines! 

Clearly much room for improvement here- my main gripe being the handling of inline math.
## Tables
Tables can be done in many ways so I have lifted the below directly from [clayh53](https://clayh53.github.io/tufte-jekyll/articles/20/tufte-style-jekyll-blog)
Tables are, frankly,  a pain in the ass to create. That said, they often are one of the best methods for presenting data. Tabular data are normally presented with right-aligned numbers, left-aligned text, and minimal grid lines.

Note that when writing Jekyll Markdown content, there will often be a need to get some dirt under your fingernails and stoop to writing a little honest-to-god html. Yes, all that hideous ```<table>..<thead>..<th>``` nonsense. *And* you must wrap the unholy mess in a ```<div class="table-wrapper">``` tag to ensure that the table stays centered in the main content column.

Tables are designed with an ```overflow:scroll``` property to create slider bars when the viewport is narrow. This is so that you do not collapse all your beautiful data into a jumble of letters and numbers when you view it on your smartphone.

{% marginnote 'table-1-id' '*Table 1*: A table with default style formatting' %}
<div class="table-wrapper">
  <table class="table-alpha" id="newspaper-tone">
    <thead>
      <tr>
        <th class="left">Content and tone of front-page articles in 94 U.S. newspapers, October and November, 1974</th>
        <th class="left">Number of articles</th>
        <th>Percent of articles with negative criticism of specific person or policy</th></tr>
    </thead>
    <tbody>
      <tr>
        <td class="text">Watergate: defendants and prosecutors, Ford’s pardon of Nixon</td>
        <td><div class="number">537</div></td>
        <td class="c"><div class="number">49%</div></td>
      </tr>
      <tr>
        <td class="text">Inflation, high cost of living</td>
        <td><div class="number">415</div></td>
        <td class="c"><div class="number">28%</div></td>
      </tr>
      <tr>
        <td class="text">Government competence: costs, quality, salaries of public employees</td>
        <td><div class="number">322</div></td>
        <td class="c"><div class="number">30%</div></td>
      </tr>
      <tr>
        <td class="text">Confidence in government: power of special interests, trust in political leaders, dishonesty in politics</td>
        <td><div class="number">266</div></td>
        <td class="c"><div class="number">52%</div></td>
      </tr>
      <tr>
        <td class="text">Government power: regulation of business, secrecy, control of CIA and FBI</td>
        <td><div class="number">154</div></td>
        <td class="c"><div class="number">42%</div></td>
      </tr>
      <tr>
        <td class="text">Crime</td>
        <td><div class="number">123</div></td>
        <td class="c"><div class="number r">30%</div></td>
      </tr>
      <tr>
        <td class="text">Race</td>
        <td><div class="number">103</div></td>
        <td class="c"><div class="number">25%</div></td>
      </tr>
      <tr>
        <td class="text">Unemployment</td>
        <td><div class="number">100</div></td>
        <td class="c"><div class="number">13%</div></td>
      </tr>
      <tr>
        <td class="text">Shortages: energy, food</td>
        <td><div class="number">68</div></td>
        <td class="c"><div class="number">16%</div></td>
      </tr>
    </tbody>
  </table>
</div>


This is not the One True Table. Such a style does not exist. One must craft each data table with custom care to the narrative one is telling with that specific data. So take this not as “the table style to use”, but rather as “a table style to start from”. From here, use principles to guide you: avoid chartjunk, optimize the data-ink ratio (“within reason”, as Tufte says), and “mobilize every graphical element, perhaps several times over, to show the data.{% sidenote 'table-id' 'Page 139, *The Visual Display of Quantitative Information*, Edward Tufte 2001.'%} Furthermore, one must know when to reach for more complex data presentation tools, like a custom graphic or a JavaScript charting library.

As an example of alternative table styles, academic publications written in <span class="latex">L<sup>a</sup>T<sub>e</sub>X</span> often rely on the ```booktabs``` package to produce clean, clear tables. Similar results can be achieved in Tufte CSS with the ```booktabs``` class, as demonstrated in this table:

{% marginnote 'table-2-id' '*Table 2*: A table with booktabs style formatting' %}
<div class="table-wrapper">
<table class="booktabs">
          <thead>
            <tr><th colspan="2" class="cmid">Items</th><th class="nocmid"></th></tr>
            <tr><th class="l">Animal</th><th>Description</th><th class="r">Price ($)</th></tr>
          </thead>
          <tbody>
            <tr><td>Gnat</td>     <td>per gram</td><td class="r">13.65</td></tr>
            <tr><td></td>         <td>each</td>    <td class="r">0.01</td></tr>
            <tr><td>Gnu</td>      <td>stuffed</td> <td class="r">92.50</td></tr>
            <tr><td>Emu</td>      <td>stuffed</td> <td class="r">33.33</td></tr>
            <tr><td>Armadillo</td><td>frozen</td>  <td class="r">8.99</td></tr>
          </tbody>
</table>
</div>

The table above was written in HTML as follows:

```
<div class="table-wrapper">
<table class="booktabs">
          <thead>
            <tr><th colspan="2" class="cmid">Items</th><th class="nocmid"></th></tr>
            <tr><th class="l">Animal</th><th>Description</th class="r"><th>Price ($)</th></tr>
          </thead>
          <tbody>
            <tr><td>Gnat</td>     <td>per gram</td><td class="r">13.65</td></tr>
            <tr><td></td>         <td>each</td>    <td class="r">0.01</td></tr>
            <tr><td>Gnu</td>      <td>stuffed</td> <td class="r">92.50</td></tr>
            <tr><td>Emu</td>      <td>stuffed</td> <td class="r">33.33</td></tr>
            <tr><td>Armadillo</td><td>frozen</td>  <td class="r">8.99</td></tr>
          </tbody>
</table>
</div>
```


I like this style of table, so I have made it the default for unstyled tables. This allows use of the [*Markdown Extra*](https://michelf.ca/projects/php-markdown/extra/) features built into the [*Kramdown*](http://kramdown.gettalong.org/parser/kramdown.html) parser. Here is a table created using the Markdown Extra table syntax to make a nice table which has the side benefit of being human readable in the raw Markdown file:

{% marginnote 'tableID-3' 'Table 3: a table created with *Markdown Extra* markup using only the default table styling' %}

|                 |mpg  | cyl  |  disp  |   hp   |  drat  | wt  |
|:----------------|----:|-----:|-------:|-------:|-------:|----:|
|Mazda RX4        |21   |6     |160     |110     |3.90    |2.62 |
|Mazda RX4 Wag    |21   |6     |160     |110     |3.90    |2.88 |
|Datsun 710       |22.8 |4     |108     |93      |3.85    |2.32 |
|Hornet 4 Drive   |21.4 |6     |258     |110     |3.08    |3.21 |
|Hornet Sportabout|18.7 |8     |360     |175     |3.15    |3.44 |
|Valiant          |18.1 |6     |160     |105     |2.76    |3.46 |


Using the following Markdown formatting:

```
|                 |mpg  | cyl  |  disp  |   hp   |  drat  | wt  |
|:----------------|----:|-----:|-------:|-------:|-------:|----:|
|Mazda RX4        |21   |6     |160     |110     |3.90    |2.62 |
|Mazda RX4 Wag    |21   |6     |160     |110     |3.90    |2.88 |
|Datsun 710       |22.8 |4     |108     |93      |3.85    |2.32 |
etc...
```

The following is a more simple table, showing the Markdown-style table markup. Remember to label the table with a *marginnote* Liquid tag, and you *must* separate the label from the table with a single blank line. This markup:

```
{{ "{% marginnote 'Table-ID4' 'Table 4: a simple table showing left, center, and right alignment of table headings and data' "}} %}

|**Left** |**Center**|**Right**|
|:--------|:--------:|--------:|
 Aardvarks|         1|$3.50
       Cat|   5      |$4.23
  Dogs    |3         |$5.29
```

Yields this table:

{% marginnote 'Table-ID4' 'Table 4: a simple table showing left, center, and right alignment of table headings and data' %}

|**Left** |**Center**|**Right**|
|:--------|:--------:|--------:|
 Aardvarks|         1|$3.50
       Cat|   5      |$4.23
  Dogs    |3         |$5.29


## Code
Again, I am lifting this from [clayh53](https://clayh53.github.io/tufte-jekyll/articles/20/tufte-style-jekyll-blog)'s section as I haven't touched this much. But likely need to in the future. Code samples use a monospace font using the 'code' class. The Kramdown parser has the 'GFM' option enabled, which stands for 'Github Flavored Markdown', and this means that both inline code such as ```#include <stdio.h>``` and blocks of code can be delimited by surrounding them with 3 backticks:

```
(map tufte-style all-the-things)
```
is created by the following markup:
<pre><code>```(map tufte-style all-the-things)```</code></pre>

To get the code highlighted in the language of your choice like so:


``` ruby
module Jekyll
  class RenderFullWidthTag < Liquid::Tag
  require "shellwords"

    def initialize(tag_name, text, tokens)
      super
      @text = text.shellsplit
    end

    def render(context)
      "<div><img class='fullwidth' src='#{@text[0]}'/></div> " +
      "<p><span class='marginnote'>#{@text[1]}</span></p>"
    end
  end
end

Liquid::Template.register_tag('fullwidth', Jekyll::RenderFullWidthTag)
```

Enclose the code block in three backticks, followed by a space and then the language name, like this:

<pre> <code>``` ruby
    module Jekyll
    blah, blah...
   ```</code> </pre> %%

[^2]: [[My Jekyll Site had ButtonDown Integration Issues|This note]] tells you of some issues I had with integrating ButtonDown in my Jekyll+Netlify site. Hope it helps someone.

[^3]: Unsure if this site is there yet but I think it will eventually get there as the template I started with was far more minimal.

[^4]: All the bells and whistles of this site is just a consequence of excessive use of [Cursor](https://cursor.ai) to build something that aligns with my aesthetics of what a website against my name ought to be/feel/look like.

[^5]: Though these tools will forever be a part of my life. Cursor is super useful because it is still helping me tweak the site's appearance with LLMs faster than I ever could.

[^6]: I am no expert on why people work with SCSS and [SASS](http://sass-lang.com) file (the .scss type) but this is articulated by clayh53 on their website. The short version is that you can easily handle font changes etc. quite easily.

[^7]: While it might be feasible to convert Markdown footnotes into margin notes during the build, I sense that there must be some limit on how long a sidenote must be before it is formatted as a footnote. So this is a quite low priority todo for me.

[^8]: Getting this page made was so cool- I got the page into Obsidian using the Obsidian Web Clipper. I then popped into Cursor and asked Claude to translate the article.

Tags
```html
<p>This is a paragaph.</p>
```
- tags consists of opening `<>` and closing `</>`

Comments
```html
<!-- This is a comment -->
```
HTML comments start with `<!--` and end with `-->`

DOM (Document Object Model)
- elements are nested in HTML which creates a tree 
- hierarchy and structure of HTML (like a tree)

**Inline vs Block-Level**
==Inline== tags that wrap around other words, eg. italic, bold, quote
==Block Level== tags that is entire block, eg. blockquote, headings

**Paragraph**
```html
<p> </p>
```
Without marking these, the browser by default renders everything in a single paragraph.

**Headings**
```html
<h1> </h1>
```
The headlines consists of 6 sizes from h1 to h6. Similar to markdown `#`
- h1 is the largest title hence the most important

**Styling**
```html
<i> </i>  <!-- Italic -->
<b> </b> <!-- Bold -->
```
- it the closing tag is not used, everything after the starting tag will have the styles applied
- you can also use `<em>` and `<strong>` but sometimes these render the same as `<b>`

**Lists**
```html
<li></li> <!-- List item -->
```
![](assets/Pasted%20image%2020240917220254.png)
Unordered List `<ul>`
- group of list items that is not sorted
Ordered List `<ol>`
- group of list item that can be counted like 123
Definition List `<dl>`
```html
<dl>
<dt>Term</dt> <dd> Description </dd>
<dl>
```
![](assets/Pasted%20image%2020240917220519.png)
- definition lists start as `<dl>` and it can contain list of dictionaries with a term and its definition

**Quotes**
```html
<blockquote>Entire Block of quote.</blockquote>
<q>inline quote</q>
```
Add quotation to entire some text in a paragraph or entire block of text.

**Time**
```html
<time>on some dates</time>
```
Time tag is a human readable text that can have a [datetime attribute](html-attributes.md#^270b7d) applied to it (which must be machine-readable)

**Code**
```html
<code>some code</code>
```
![](assets/Pasted%20image%2020240917222010.png)
Code can be inline and will change the font to monospace.
Code can also be used to represent HTML entities so it doesn't get rendered as HTML
- `<` = `%lt;`
- `>` = `%gt;`
- `&` = `&amp;`

**Line Break**
![](assets/Pasted%20image%2020240917222403.png)
```html
<br>
```
Line break add a new line to the end of the text, it doesn't need a closing tag.

**Pre**
![](assets/Pasted%20image%2020240917222631.png)
```html
<pre> Already formatted text </pre>
```
Pre stands for already formatted text, everything in the pre will have the spacing exactly as is; whereas in normal paragraph it will render as long line of text.

**Sub/Superscript**
```html
<sub></sub>
<sup></sup>
```
Subscripts and superscripts, eg. math and chemistry formulas and foornotes.

**Smalltext**
![](assets/Pasted%20image%2020240917223019.png)
```html
<small></small>
```
Text that are smaller, good for copyright information or fine print.

**None Breaking Space**
![](assets/Pasted%20image%2020240918214339.png)
```html
This is some&nbsp;text.
```
Add `&nbsp;` between some texts and these will not break even where other characters will be on a new line.

**Navbar**
```html
<nav>
<ul>
<li><a href="/home">Home</a></li>
</ul>
</nav>
```
Element that is used for website navigation. Consists of an unordered list of links.
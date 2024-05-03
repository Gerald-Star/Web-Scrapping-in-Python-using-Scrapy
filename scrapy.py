

<html>
  <body>
    <div>
      <p>Good Luck!</p>
      <p>Not here...</p>
    </div>
    <div>
      <p>Where am I?</p>
    </div>
  </body>
</html>

In this exercise, you will navigate
to a specific element using your new knowledge
of XPath notation.

Your job will be to create an XPath string using single forward-slashes
and brackets which navigates to the paragraph p element which contains 
the text "Where am I?".

# Fill in the blank
xpath = '/html/body/div[2]/p[1]'

Using double forward-slash notation, assign to 
the variable xpath a simple XPath string navigating 
to all paragraph p elements within any HTML code.

xpath = '//p'

# EXERCISE

A classy span
Although we haven't yet gone deep into XPath, one thing we can do is select 
elements by their attributes using an XPath. For example, 
if we want to direct to the div element within the HTML document
whose id attribute is "uid", then we could write the XPath string '//div[@id="uid"]'. The first part of this string, //div, first looks at all div elements in the HTML document. Then, using the brackets, we specify that we want only the div element with a specific id attribute (in this case uid). To note, the phrase @id="uid" in the brackets would be read as "attribute id equals uid".

In this exercise, you will select all span elements whose 
class attribute equals "span-class". (Note: span is just another possible tag-name).

Instructions

Assign to the variable xpath an XPath string which will select all span elements whose class attribute equals "span-class". You do not need to see the actual HTML code to do this!




# XPATH EXPRESSIONS TO SCRAP A WEBSITE
 XPath syntax, learning to navigate to elements based on their attributes as well as direct to the attribute information within elements.
 
# Fill in the blank
xpath = '//span[@class="span-class"]'


# CHAPTER 2

# XPath Notation 
 XPath notation to navigate HTML 
 
 # 2. Slashes and Brackets

As we briefly saw before, XPath directs us down one generation 
with a single forward slash, and down all future generations with a 
double forward slash. We also saw that using square brackets in the 
XPath expression helps narrow in on which element or elements we want,
but it turns out these brackets aren't always necessary nor desired.


3. To Bracket or not to Bracket
00:37 - 00:56
For example, the first XPath expression without brackets and the second with brackets lead us to the same element the body element since there is only one html element at the root level, and one body element which is a child of that html element.

4. A Body of P
00:56 - 01:18
As another example, the XPath string here leads us to the single paragraph element which is one generation below the body element. Do you understand why there is only this one element selected? It's because there is only one paragraph element which is a child of the body element!

5. The Birds and the Ps
01:18 - 01:43
On the other hand, if we consider the XPath string here, this directs us to both paragraph children of the div element. We haven't clarified a specific one. We could, of course, add in brackets to help narrow in on which element we want; in this case, we will be selecting the second paragraph child of the div element.

6. Double Slashing the Brackets
01:43 - 03:10
Using a double forward-slash, we could have selected all paragraph elements which are within the HTML document. Adding the bracketed number 1, it turns out we select two elements! Let's take this opportunity to be very careful in describing exactly what adding the brackets filled with a number does. When we add the brackets filled with the number N, say, to the end of an XPath expression, each of the elements that are selected before adding the brackets asks: "Am I the Nth of my selected siblings?"; if the answer is "Yes!", then that element is selected. Here, with the brackets filled with the number 1, the top paragraph element is selected because it asks "Am I the first element of my selected siblings?" and answers "Yes!". The bottom paragraph element is also selected since its sibling is the div element, which was not not originally selected, and so when the bottom paragraph element asks "Am I the first element of my selected siblings?" the answer is again "Yes!". Honestly, I don't often mix double forward-slashes and brackets filled with numbers. We'll see in later slides there are other, more interesting ways to use brackets to select elements.

7. The Wildcard
03:10 - 03:34
One final piece of notation we will cover in this lesson is the "wildcard" character, the asterisks. The asterisks indicates we want to ignore tag type. For example, in this expression, we are directed to both children of the body element, regardless that one is a div element and one is a paragraph element.

8. Xposé
03:34 - 03:56
To summarize, we have learned the basics of XPath notation, including the meaning of single and double forward slashes, as well as some uses for the square brackets; and finally you saw the asterisks as the "wildcard" character. You will become more familiar with these ideas in the exercises! 

# XPath Notion EXpressions 

Xpath string Xpath = "//*" starts at the root level and selects all elements of all future generations without regards to tag type, it selects all elements within the HTML document

 "/*" selects all elements in the HTML document of the first generation (without concern of tag type), it will select any root element, which is typically the 1 html root element.
 

 "/html/body/*" selects all elements one generation below the body element without concern of the tag type, it selects all children of the body element. On the other hand, "/html/body//*" selects all elements from all future generations of the body element (that is, all descendants of the bo
 
 
  "/html/body/*" selects all elements one generation below the body element without concern of the tag type, it selects all children of the body element. On the other hand, "/html/body//*" selects all elements from all future generations of the body element (that is, all descendants of the body) regardless of tag type.
  

"//div" starts at the root level and selects all div elements of all future generations, it selects all div elements within the HTML document

"//div[@id='uid']" starts at the root level and selects all div elements of all future generations with an id attribute equal to "uid", it selects all div elements with an id attribute equal to "uid" within the HTML document

"//div/p" starts at the root level and selects all p elements which are children of a div element, it selects all p elements which are children of a div element within the HTML document

"//div/p[2]" starts at the root level and selects the second p element which is a child of a div element, it selects the second p element which is a child of a div element within the HTML document

"//div/*" starts at the root level and selects all elements which are children of a div element, it selects all elements which are children of a div element within the HTML document

# EXERCISE

# Where it's @

In this exercise, you will write an XPath expression to select the paragraph element within the div element, which has a class attribute equal to "class-1".

Instructions

Assign to the variable xpath an XPath string which will select the paragraph element within the div element, which has a class attribute equal to "class-1". You do not need to see the actual HTML code to do this!

# Fill in the blank

xpath = '//div[@class="class-1"]/p'

# EXERCISE

# Hyper(link) Active

In this exercise, you will write an XPath expression to select the hyperlink (a) element which contains the text "Next".

Instructions

Assign to the variable xpath an XPath string which will select the hyperlink (a) element which contains the text "Next". You do not need to see the actual HTML code to do this!



# INSTRUCTIONS

Assign to the variable xpath an XPath string which directs to all child elements of the body element. There is only one body element in this HTML document and it is a child of the root html element.

Hint
Remember that a single forward slash moves down one generation, and a wildcard ignores tag type.

# solution

# Create an XPath string to direct to children of body element
xpath = '/html/body/*'

# Print out the number of elements selected
how_many_elements( xpath )



# EXERCISE

<html>
  <body>
    <div>
      <p>Hello World!</p>
      <div>
        <p>Choose DataCamp!</p>
      </div>
    </div>
    <div>
      <p>Thanks for Watching!</p>
    </div>
  </body>
</html>

# INSTRUCTIONS

Assign to the variable xpath an XPath string to direct to the paragraph element containing the phrase: "Choose DataCamp!".

# Create an XPath string to the desired paragraph element
xpath = '/html/body/div[1]/div/p'

# Print out the element text
print_element_text( xpath )


# CHAPTER 3 OFF THE BEATEN XPATH

3. Brackets and Attributes
00:49 - 01:08
We saw before that square brackets can be used in xpath syntax to hone in on a specific element 
or elements based on their order within a given generation. 
We can also include other information within square brackets to 
select specific elements.



# EXERCISE

Exercise
Where it's @
In this exercise, you'll begin to write an XPath string using attributes to achieve a certain task; that task is to select the paragraph element containing the text "Thanks for Watching!". We've already created most of the XPath string for you.

Consider the following HTML:

<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose DataCamp!</p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>


# Create an Xpath string to select desired p element
xpath = '//*[@id="div3"]/p'

# Print out selection text
print_element_text( xpath )


# EXERCISE

Exercise
Check your Class
This exercise is to emphasize that when you use an XPath to select an element by its class attribute without using the contains() function, you match the class exactly. Your job is to fill in the blank below and finish the variable xpath directing to the specified element.

Consider the following HTML:

<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose DataCamp!</p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
Instructions
100 XP
Fill in the blanks in the xpath below to select the paragraph element containing the phrase: "Hello World!".


# Create an XPath string to select p element by class
xpath = '//p[@class="class-1 class-2"]'

# Print out select text
print_element_text( xpath )


# EXERCISE


Hyper(link) Active
One of the most important attributes to extract for "web-crawling" is the hyperlink url (href attribute) within an a tag. Here, you will extract such a hyperlink! We have created the function print_attribute to print out the data extracted from your XPath, so you can test your XPath strings in the console, if you like.

The exercise refers to the following HTML source code:

<html>
  <body>
    <div id="div1" class="class-1">
      <p class="class-1 class-2">Hello World!</p>
      <div id="div2">
        <p id="p2" class="class-2">Choose 
            <a href="http://datacamp.com">DataCamp!</a>!
        </p>
      </div>
    </div>
    <div id="div3" class="class-2">
      <p class="class-2">Thanks for Watching!</p>
    </div>
  </body>
</html>
Instructions
100 XP
Fill in the blanks to complete the variable xpath below to select the href attribute value from the DataCamp hyperlink.



# Create an xpath to the href attribute
xpath = '//p[@id="p2"]/a/@href'

# Print out the selection(s); there should be only one
print_attribute( xpath )


# EXERCISE

Exercise
Secret Links
We have loaded the HTML from a secret website and have used it to create the functions how_many_elements() and preview(). The function how_many_elements() allows you to pass in an XPath string and it will print out the number of elements the XPath you wrote has selected. The function preview() allows you to pass in an XPath string and it will print out the first few elements you've selected.

Your job in this exercise is to create an XPath which directs to all href attribute values of the hyperlink a elements whose class attributes contain the string "package-snippet". If you do it correctly, you should find that you have selected 10 elements with your XPath string and that it previews links.

Instructions
100 XP
Instructions
100 XP
Fill in the blanks below to assign an XPath string to the variable xpath which directs to all href attribute values of the hyperlink a elements whose class attributes contain the string "package-snippet". Remember that we use the contains call within the XPath string to check if an attribute value contains a particular string.


Hint
Remember that the format for contains(____,____) is contains(@attr, "string") to check that the attr attribute value contains the string "string". You need to decide what to write for @attr and "string".
The final blank is left to reference the href attribute value you want to point to; don't forget to include the @ symbol (i.e., you will write @href).

# Create an xpath to the href attributes
xpath = '//a[contains(@class,"package-snippet")]/@href'

# Print out how many elements are selected
how_many_elements( xpath )
# Preview the selected elements
preview( xpath )


# EXERCISE 
# XPATH CHAINING

XPath Chaining
Selector and SelectorList objects allow for chaining when using the xpath method. What this means is that you can apply the xpath method over once you've already applied it. For example, if sel is the name of our Selector, then

sel.xpath('/html/body/div[2]')
is the same as

sel.xpath('/html').xpath('./body/div[2]')
or is the same as

sel.xpath('/html').xpath('./body').xpath('./div[2]')
The only catch is that you need to "glue together" the XPath pieces by using a period at the start of each subsequent XPath string (notice the periods we added to the XPath strings in our examples).

Instructions
0 XP
Fill in the blank below to chain together two xpath calls which result in the same selection as
sel.xpath('//div/span/p[3]')

# Chain together xpath methods to select desired p element
# Chain together xpath methods to select desired p element

sel.xpath('//div').xpath('./span/p[3]')
[<Selector query='./span/p[3]' data='<p>YOU GOT IT!</p>'>]


# EXERCISE

Divvy Up This Exercise
We have pre-loaded an HTML into the string variable html. In this two part problem you will use this html variable as the HTML document to set up a Selector object with, and create a SelectorList which selects all div elements; then, you will check your understanding of what happens within the SelectorList.

Instructions 1/2
50 XP
1
2
Set up the Selector object sel with the html variable passed as the text argument.
Assign to the variable divs a SelectorList of all div elements within the HTML document.



Hint
Remember that you pass in a string of HTML into a Selector using the text argument.
You should already know an easy XPath string which selects all div elements.


# solution

from scrapy import Selector

# Create a Selector selecting html as the HTML document
sel = Selector( text = html )

# Create a SelectorList of all div elements in the HTML document
divs = sel.xpath( '//div' )


# EXERCISE


Requesting a Selector
We have pre-loaded the URL for a particular website in the string variable url and use the requests library to put the content from the website into the string variable html. Your task is to create a Selector object sel using the HTML source code stored in html.

Instructions
100 XP
Fill in the two blanks below to assign to create the Selector object sel which uses the string html as the text it inputs.

#! Solution

# Import a scrapy Selector
from scrapy import Selector

# Import requests
import requests

# Create the string html containing the HTML source
html = requests.get( url ).content

# Create the Selector object sel from html
sel = Selector( text = html)

# Print out the number of elements in the HTML document
print( "There are 1020 elements in the HTML document.")
print( "You have found: ", len( sel.xpath('//*') ) )
There are 1020 elements in the HTML document.
You have found:  1020

<script.py> output:
    There are 1020 elements in the HTML document.
    You have found:  1020



The (X)Path to CSS Locators
Many people prefer using CSS Locator notation to XPath notation. As we will see later, it often makes attribute selection very easy. To help get you more comfortable going back and forth between XPath and CSS Locator strings, we give you a chance in this exercise to do some direct "translation" between the two.

Assign to the variable css_locator a CSS Locator string which is equivalent to the XPath string given.


Show Answer (-35 XP)
Hint
Pay attention to the single vs double forward-slashes.
You will likely need to use the :nth-of-type argument somewhere in your string.

#SOLUTION

# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'html > body > span:nth-of-type(1) a'



# EXERCISE


Assign to the variable xpath a XPath string which is equivalent to the CSS Locator string given.


Show Answer (-35 XP)
Hint
The trickiest part of this is to decide whether to start your XPath string with a single forward-slash or a double forward-slash. So, think about whether you are selecting just root level div elements, or all div elements in the document.
Don't forget that # indicates a selection by the id attribute.


# solution

# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'



# exercise


Get an "a" in this Course
We have loaded the HTML from a secret website which you will use to set up a Selector object and the function how_many_elements(). When passing this function a CSS Locator string, it will print out the number of elements that the CSS Locator you wrote has selected.

In the second part of this problem, we want you to create a CSS Locator string which will select a certain collection of elements as described here: Select the hyperlink (a element) children of all div elements belonging to the class "course-block" (that is, any div element with a class attribute such that "course-block" is one of the classes assigned). The number of such elements is 11, so you can check your solution with how_many_elements if you choose.

Instructions 2/2
35 XP
2
Assign the variable css_locator a CSS Locator string which directs to the hyperlink (a element) children of all div elements belonging to the class "course-block".


Show Answer (-35 XP)
Hint
Remember to use a period . when trying to select by class.
Remember to use the greater than > symbol when moving down a generation.


#solution


from scrapy import Selector

# Create a selector from the html (of a secret website)
sel = Selector( text = html )

# Fill in the blank
css_locator = 'div.course-block > a'

# Print the number of selected elements.
how_many_elements( css_locator )
11



# exercise


The CSS Wildcard
You can use the wildcard * in CSS Locators too! In fact, we can use it in a similar way, when we want to ignore the tag type. For example:

The CSS Locator string '*' selects all elements in the HTML document.
The CSS Locator string '*.class-1' selects all elements which belong to class-1, but this is unnecessary since the string '.class-1' will also do the same job.
The CSS Locator string '*#uid' selects the element with id attribute equal to uid, but this is unnecessary since the string '#uid' will also do the same job.
In this exercise, we want you to work by analogy with the wildcard character you know from XPath notation to discover how to select all the children of a certain element in CSS Locator notation.

Instructions
100 XP
Instructions
100 XP
Assign to the variable css_locator a CSS Locator string which will select all children (regardless of tag-type) of the unique element in the HTML document that has its id attribute equal to uid.


# Create the CSS Locator to all children of the element whose id is uid
css_locator = "#uid > *"



# exercise


You've been `href`ed
In a previous exercise, you created a CSS Locator string to select the hyperlink (a element) children of all div elements belonging to the class "course-block". Here we have created a SelectorList called course_as having selected those hyperlink children.

Now, we want you to fill in the blank below to extract the href attribute values from these elements. This is another example of chaining, as we've seen in a previous exercise.

The point here is that we can chain together calls to the methods css and xpath, and combine them! We help nudge you in the correct direction by giving you the solution if we chain with another call to the css method.

Instructions
70 XP
Instructions
70 XP
Set up the Selector object sel using the string html as the text input.
Assign to the variable hrefs_from_xpath the href attribute values from the elements in course_as. Your solution should match hrefs_from_css!


Show Answer (-70 XP)
Hint
Don't forget when chaining with xpath, to use a period as "glue" as you did in a previous exercise.


# solution


from scrapy import Selector

# Create a selector object from a secret website
sel = Selector( text = html )

# Select all hyperlinks of div elements belonging to class "course-block"
course_as = sel.css( 'div.course-block > a' )

# Selecting all href attributes chaining with css
hrefs_from_css = course_as.css( '::attr(href)' )

# Selecting all href attributes chaining with xpath
hrefs_from_xpath = course_as.xpath( './@href' )



Top Level Text
This exercise will have you write an XPath and CSS Locator string to direct to the text of a specific paragraph p element. The p element in the HTML is uniquely defined by its id attribute, which is "p3". With this small piece of information, you should be able to create the desired strings; however, we have preloaded the variable html with a string containing the HTML in which this link belongs, if you want to peruse it.

In this exercise, you will only be selecting the text within the element, which does not include the text in future generations of the element. We have created a function print_results for you to compare which elements your strings direct to.

Instructions
70 XP
Instructions
70 XP
Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which does not include the text of future generations of this p element.
Assign to the variable css_locator a CSS Locator string directing to this same text.


Show Answer (-70 XP)
Hint
Remember that in CSS Locator notation, the pound sign # is used in helping identify an element by its id.
Don't forget that for an XPath string, you need to have parentheses following the word text (i.e., text() should be part of the string).
Don't forget that for a CSS Locator string, you need to connect the word text with a double colon ::.



# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

# Print the text from our selections
print_results( xpath, css_locator )
Your XPath extracts to following:
['\nHere is the ', ' link you want!\n']
_________________

Your CSS Locator extracts the following:
['\nHere is the ', ' link you want!\n']



# exercise

This exercise is similar to the previous, but differs in that you will be selecting text from multiple generations of a given element.

You will write an XPath and CSS Locator strings to direct to the text of a specific paragraph p element. The p element in the HTML is uniquely defined by its id attribute, which is "p3". With this small piece of information, you should be able to create the desired strings; however, we have preloaded the variable html with a string containing the HTML in which this link belongs, if you want to peruse it.

In this exercise, you will only be selecting the text within the element which includes all text within the future generations. We have created a function print_results for you to compare which elements your strings direct to.

Instructions
70 XP
Instructions
70 XP
Assign to the variable xpath an XPath string directing to the text within the paragraph p element with id equal to p3, which includes the text of future generations of this p element.
Assign to the variable css_locator a CSS Locator string directing to this same text.


Show Answer (-70 XP)
Hint
Remember that in CSS Locator notation, the pound sign # is used in helping identify an element by its id.
Don't forget that for an XPath string, you need to have parentheses following the word text (i.e., text() should be part of the string).
Don't forget that for a CSS Locator string, you need to connect the word text with a double colon ::.

# solution

# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )


<script.py> output:
    Your XPath extracts to following:
    ['\nHere is the ', 'DataCamp', ' link you want!\n']
    _________________
    
    Your CSS Locator extracts the following:
    ['\nHere is the ', 'DataCamp', ' link you want!\n']
    
    
    
 # exercise SPIDER
 
 creating spiders, programs that crawl the web and scrape data in a way we specify, and although we will need to wait to the next chapter to build a spider, moving from Selector objects to Response objects gives us these extra pieces we need to crawl between sites instead of simply parsing one site.
 
 
# selector vy response object


But for now, we will focus on Response objects which already have HTML pre-loaded. You ask: "Tom, why are you making us learn a new Response object when you just taught us about Selectors?!". My "Response" to you is that you can use everything we've learned for Selectors with Responses. The Selector object was our introduction to a Response object! What makes us want to use a Response object rather than a Selector is that, on top of all the Selector functionality, the Response object keeps track of which URL the HTML code is from, and hence gives us a tool to not only scrape one single site, but crawl between links on sites and scrape multiple sites automatically!


#exercise

Exercise
Reveal By Response
We have pre-loaded a Response object, named response, with the content from a secret website. Your job is to figure out the URL and the title of the website using the response variable. You learned how to find the URL in the last lesson. To find the website title, what you need to know is:

The title is the text from the title element
The title element is a child of the head element, which is a child of the html root element.
To note: the html root element only has one child head element, and the head element only has one child title element.

#Instructions

Assign to the variable this_url the URL used to load the response variable.
Assign to the variable this_title the title of the website used to load the response variable. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text.
Regardless of whether you use xpath or css, make sure that you are selecting the text within the title element, and not just the title itself.



You can access the URL of the response via its .url attribute.
You can use your choice of either the xpath or css method within response to get to the title.
If you are using xpath, don't forget that you will need to include /text() within your XPath string to point to the text of the title.
If you are using css, don't forget that you will need to include ::text within your CSS Locator string.


# solution 

# Get the URL to the website loaded in response
this_url = response.url

# Get the title of the website loaded in response
this_title = response.xpath( '/html/head/title/text()' ).extract_first()

# Print out our findings
print_url_title( this_url, this_title )
Here is what you found:
	-URL: https://www.datacamp.com/courses/all
	-Title: Data Science Courses: R & Python Analysis Tutorials | DataCamp



#EXERCISE    

Responding with Selectors
Something that we should emphasize at this point about the relationship between a Selector and Response objects is that both objects return a SelectorList when using the xpath or css methods to direct to elements. In this exercise, we'll prove it to you, by having you find all hyperlink elements belonging to the class course-block__link (notice the double underscore!) and looking at the object that is produced when doing so.

Recall that to find an element by class, you can use a period (.). For example, div.class-2 selects all div elements belonging to class-2.

We have pre-loaded both a Response object named response and a Selector object named sel with the content from the same "secret" website. Once you complete the task of creating a CSS Locator, you will compare both the output from response.css and selector.css to see that they are effectively the same!

Instructions

Assign to the variable css_locator a CSS Locator string which directs to all hyperlink a elements belonging to the class course-block__link.
Assign to the variable response_as the output of passing the css_locator variable to the css method in response.
Assign to the variable sel_as the output of passing the css_locator variable to the css method in sel.



Your CSS Locator string should take the form a.____, where the blank represents the class that you want to find.
Don't forget the double underscore!


# solution


# Create a CSS Locator string to the desired hyperlink elements
css_locator = 'a.course-block__link'

# Select the hyperlink elements from response and sel
response_as = response.css( css_locator )
sel_as = sel.css( css_locator )

# Examine similarity
nr = len( response_as )
ns = len( sel_as )
for i in range( min(nr, ns, 2) ):
  print( "Element %d from response: %s" % (i+1, response_as[i]) )
  print( "Element %d from sel: %s" % (i+1, sel_as[i]) )
  print( "" )
Element 1 from response: <Selector query="descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' course-block__link ')]" data='<a class="course-block__link ds-snowp...'>
Element 1 from sel: <Selector query="descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' course-block__link ')]" data='<a class="course-block__link ds-snowp...'>

Element 2 from response: <Selector query="descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' course-block__link ')]" data='<a class="course-block__link ds-snowp...'>
Element 2 from sel: <Selector query="descendant-or-self::a[@class and contains(concat(' ', normalize-space(@class), ' '), ' course-block__link ')]" data='<a class="course-block__link ds-snowp...'>
In [1]:


# exercise

Selecting from a Selection
In this exercise, you will find the text from an h4 element within a particular div element. It will occur in steps where the first step is selecting a family of div elements, and the second step is narrowing in on the first one, from which we will grab the h4 element text. This process of progressively narrowing in on elements (e.g., first to the div elements, then to the h4 element) is another example of "chaining", even if it doesn't look exactly the same as we've seen it before.

Along the way in this exercise, there is a variable first_div set up for you to use. Think carefully about what type of object first_div is!

Instructions 1/2
35 XP
1
2
Instructions 1/2
35 XP
1
2
Assign to the variable divs a SelectorList which selects all div elements belonging to the class course-block.
Assign to the variable h4_text the text from the only h4 element within the content selected in first_div. Since we only want the text from the single element we will select, we use the extract_first() method to extract the text.


Show Answer (-35 XP)
Hint
Remember that to point to the text within the h4 element, you need to include ::text within your CSS Locator string for h4_text.
Remember that the h4 element is the only h4 element in the content selected within first_div.


# solution


# Select all desired div elements
divs = response.css( 'div.course-block' )

# Take the first div element
first_div = divs[0]

# Extract the text from the h4 element in first_div
h4_text = first_div.css('h4::text').extract_first()

# Print out the text
print( "The text from the h4 element is:", h4_text )
The text from the h4 element is: Introduction to R


# questions

What type of element is first_div?

A Selector object.


# exercise datacamp

Titular
Similar to the work given in the previous lesson, we will have you use a pre-loaded Response object, named response to scrape the course titles from the (shortened version of the) DataCamp course directory https://www.datacamp.com/courses/all. To successfully do so, you only need to know the following

The course titles are the text from all the h4 elements within the HTML document.
We ask you to extract these course titles here.

Instructions
70 XP
Using response, assign to the variable crs_title_els a SelectorList of the selected course titles.
Assign to the variable crs_titles a list created by extracting the course titles from crs_title_els.


Show Answer (-70 XP)
Hint
You can use either the xpath or css method within response to get to the the course titles.
Remember that every h4 element is used for the course titles (and you need to get the text from these elements).


# solution

# Create a SelectorList of the course titles
crs_title_els = response.css( 'h4::text' )

# Extract the course titles 
crs_titles = crs_title_els.extract()

# Print out the course titles 
for el in crs_titles:
  print( ">>", el )
>> Introduction to R
>> Data Analysis in R, the data.table Way
>> Data Manipulation in R with dplyr
>> Data Visualization in R with ggvis
>> Reporting with R Markdown
>> Intermediate R
>> Introduction to Machine Learning
>> Cleaning Data in R
>> Intro to Python for Data Science
>> Intermediate R - Practice
>> Predicting Customer Churn in Python


# exercise


Scraping with Children
We did a cute trick in the lesson to calculate how many children there were of one of the div elements belonging to the class course-block. Here we ask you to find the number of children of a mystery element (already stored within a Selector object, so you can use the xpath or css method).

To be explicit, we have created the Selector object mystery in the following way:

We first loaded a Response variable using a secret website as the input.
Then we used a call to the xpath method to create a SelectorList of elements (but we won't say which ones)
Finally, we let mystery be the first Selector object of this SelectorList.
Instructions
70 XP
Instructions
70 XP
Fill in the blank below to chain on a call to xpath so that we can calculate the number of children of the mystery element; we assign this number to the variable how_many_kids.

Remember, if you use xpath, this really is an instance of chaining, so don't forget to use a period (.) as glue.


Show Answer (-70 XP)
Hint
Remember that children are only down one generation, and thus you only need to use a single forward slash (/).
You will need to use an asterisks (*) wildcard in your solution.


# solution
# Calculate the number of children of the mystery element
how_many_kids = len( mystery.xpath( './*' ) )

# Print out the number
print( "The number of elements you selected was:", how_many_kids )
The number of elements you selected was: 23



# exercise

# Import scrapy library
import scrapy

# Create the spider class
class YourSpider(scrapy.Spider):
  name = "your_spider"
  # start_requests method
  def start_requests(self):
    pass
  # parse method
  def parse(self, response):
    pass
  
# Inspect Your Class
inspect_class(YourSpider)
Your spider class name is: your_spider
It seems you have inherited methods from scrapy.Spider -- NICE!
In [1]:


# exercise


Instructions
0 XP
Fill in the blank within the start_requests method to assign the variable urls a list with the two strings: "https://www.datacamp.com" and"https://scrapy.org".

# solution


# Import scrapy library
import scrapy


# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    urls = ["https://www.datacamp.com", "https://scrapy.org"]
    for url in urls:
      yield url
  # parse method
  def parse( self, response ):
    pass
    
    
# exercise

Instructions
100 XP
Fill in the required scrapy object into the class YourSpider needed to create the scrapy spider.
Pass the string argument "Hello World!" to fill in the blank in the start_requests method to use the print_msg method.
    
# solution


# Import scrapy library
import scrapy

# Create the spider class
class YourSpider( scrapy.Spider ):
  name = "your_spider"
  # start_requests method
  def start_requests( self ):
    self.print_msg( "Hello World!")
  # parse method
  def parse( self, response ):
    pass
  # print_msg method
  def print_msg( self, msg ):
    print( "Calling start_requests in YourSpider prints out:", msg )
  
# Inspect Your Class
inspect_class( YourSpider )
Calling start_requests in YourSpider prints out: Hello World!

<script.py> output:
    Calling start_requests in YourSpider prints out: Hello World!
    
        
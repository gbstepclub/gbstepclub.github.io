## gbstepclub.github.io Code Maintenance Guide

### Updating the navigation
Modify the script `navigation-generator.py` and execute the following command: `python3 navigation-generator.py`

#### Explanation
There are three navigation elements - the nav bar, the dropdown on the nav bar, and the side nav. Modifying all of these for every page every time a page is created is not ideal. Instead, use this script: `navigation-generator.py`.
At the top of this script you will find two variables: `main_bar` and `drop_down`. They list the html pages and the corresponding text to be displayed, in the order they will appear. `main_bar` lists items from left to right and `drop_down` lists items from top to bottom. Note that the side nav includes all items from `main_bar` and `drop_down`. Example:

~~~~
 main_bar = { \
	'index.html': 'Meetings', \
	'about.html': 'About', \
	}
~~~~
	
this will create put two pages on the navbar: "Meetings" and "About". If you wanted "About" to go first, you would do this: 

~~~~
 main_bar = { \
 	'about.html': 'About', \
	'index.html': 'Meetings', \
	}
~~~~

note that the .html files must exist before  the script is run. 

#### Drawbacks
The script includes an auto-formatter which cannot be avoided. The code generation uses a library called BeautifulSoup, which deletes all whitespace before the html tags. This makes it hard to read the code. To fix this, `navigation-generator.py` includes an auto-formatter. 

### Creating a new page
Make a copy of `template.html` and rename the new file. Don't worry about filling in anything related to the navigation; let `navigation-generator.py` handle that for you. Simply update the script to include the new web page (process described above). The template file includes everything needed to make the sidenav and dropdowns work. You should be adding html inside of the `<main>` tag.  

### Formatting pages
Wrap any text in `<div>` tags. Then add one, maybe two classes and you should be done. The helper classes are defined in `css/custom.css`.

There are three types of helper classes:
1. centering titles/headers - use the class `center-text`
2. centering and formatting blocks of text - use `my-text-section`
3. Flexbox

#### Flexbox background information
Page layouts are accomplished using css flexbox. for more information see the following: https://css-tricks.com/snippets/css/a-guide-to-flexbox/. Flexbox is used to make all the child elements inside of a `<div>` (or any other tag) align in a row or a column. Flexbox lets you place the items on the left, right, or center of the alignment axis, and control  the spacing between items. This is preferable to using a grid or floats, as it is simpler. 

### Changing the meeting list
The meeting list is in `index.html`. It is defined in Javascript. Hopefully you can figure out how to change it after reading this paragraph and the first few lines of the `<script>` tag at the bottom of `index.html`. A few pointers:
1. each day of the week is a list of meetings. 
2. the meetings are ordered chronologically. 
3. each meeting is a javascript object, initialized using the es6 object initializer syntax. 
4. Note that javascript evaluates 'null' as false. 
5. Meetings which aren't virtual don't need the meetingId, password, or link. 
6. to list an inactive meeting, set isVirtual and isInPerson to false. 

### Adding a new fellowship to the meeting list
This is a little more invloved. 
1. look for `id="dd_fellowship"` and add the corresponding acronym to the list. 
2. Add the Acronym to the legend `(id="legend-modal")`
3. Define a javascript variable for the acronym. ex: `let FELLOWSHIP_ABC = "ABC";`. This is done with the rest of them, right under `class Day`
4. When you create the new meeting, use that variable (eg. FELLOWSHIP_ABC). Please use a variable for this. It will reduce the chance of a typo.




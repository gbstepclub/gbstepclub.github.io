# gbstepclub.github.io

*Updating the navigation:
There are three navigation elements - the nav bar, the dropdown on the nav bar, and the side nav. Modifying all of these for every page every time a page is created is not ideal. So there's a script to do this automatically. It's called 'navigation-generator.py'.
At the top of this script you will find two variables: main_bar and drop_down. list the html pages and the corresponding text to be displayed, in the order they will appear (from left to right, top to bottom). For example:

 main_bar = { \
	'index.html': 'Meetings', \
	'about.html': 'About', \
	}
	
this will create put two pages on the navbar: "Meetings" and "About". If you wanted "About" to go first, you would do this: 

 main_bar = { \
 	'about.html': 'About', \
	'index.html': 'Meetings', \
	}

note that the '.html' files must exist. 
If you want to add something to the dropdown list, do the same thing. The side nav has everything from the navbar and dropdown list. Anything you add to the navbar or dropdown list will be added to the side nav automatically. 

Drawbacks: The automatic updating is performed using a Python library called BeautifulSoup. The library deletes all the tabs that come before the html tags. This makes it hard to read the code. Luckily VisualStudio Code can fix this for you with one click - autoformat. Just run 'python3 navigation-generator.py' before comitting. This will keep the diff small, so we can easily identify what was changed. 

*Creating a new page:
Use template.html. Don't worry about filling in anything related to the navigation, because my script will do this for you, assuming you update it as described. Special Javascript is needed to make the sidenav and dropdowns work. It is included in the template file. You should be adding html inside of the <main> tag.  

*Formatting pages:
The file, css/custom.css has css classes to help you properly format the page. It also contains css that is only used by one page (anything that starts with a #). 

Page layouts are accomplished using css flexbox. for more information see the following: https://css-tricks.com/snippets/css/a-guide-to-flexbox/. Flexbox is used to make all the child elements inside of a <div> display in a row or a column. Item alignemnt and item spacing is also configurable. This is preferable to using a grid or floats, as it is simpler. custom.css has helper classes for using flexbox. see other pages for example usage. 

The other big thing is how to center text on the screen without flexbox. For headers, use the class "center-text". For blocks of text, use "my-text-section". These classes are defined in custom.css. 

*Changing the meeting list
The meeting list is in index.html. It is defined in Javascript. If you can't figure out how to change it after reading this paragraph and the first few lines of the <script> tag at the bottom of index.html, then I will be very displeased. It should be self explanatory that for each day of the week there is a list of meetings. the meetings are ordered chronologically. each meeting is a javascript object, initialized using the es6 object initializer syntax. Note that javascript evaluates 'null' as false. Meetings which aren't virtual don't need the meetingId, password, or link. to list an inactive meeting,  set isVirtual and isInPerson to false. 

*Adding a new fellowship to the meeting list
This is a little more invloved. 
1) look for 'id="dd_fellowship"' and add the corresponding acronym to the list. 
2) Add the Acronym to the legend (id="legend-modal")
3) Define a javascript variable for the acronym. ex: 'let FELLOWSHIP_ABC = "ABC"'. This is done with the rest of them, right under "class Day"
4) When you create the new meeting, use that variable (FELLOWSHIP_ABC). Please use a variable for this. It will reduce the chance of a typo.


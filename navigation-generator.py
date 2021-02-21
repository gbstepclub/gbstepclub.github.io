# run with python3

import re

# the main bar has 3 items as of now, the third one being "More", defined in drop_down
main_bar = { \
	'index.html': 'Meetings', \
	'about.html': 'About', \
	}

# contents of "More"
drop_down = { \
	'contact.html': 'Contact Us', \
	'donate.html' : 'Donate', \
	'links.html' : 'Links', \
	}

# everything is listed in the sidenav, used for mobile browsers 
side_nav = {}
side_nav.update(main_bar)
side_nav.update(drop_down)

# side_nav has everything
html_files = side_nav.keys()

'''
<ul id="nav-mobile" class="right hide-on-med-and-down">
	<li class=""><a href="index.html">Meetings</a></li>
	<li class="active"><a href="about.html">About</a></li>
	<li class=""><a class="dropdown-trigger" href="#" data-target="dropdown-more">More<i class="material-icons right">arrow_drop_down</i></a></li>
</ul>

'''

for f in html_files:
	# generate main_bar
	to_insert=""
	for item in main_bar.keys():
		_class = 'class=""'
		if item == f:
			_class = 'class="active"'
		to_insert += f'\t<li {_class}><a href="{item}">{main_bar[item]}</a></li>\n'
	main_bar_html = (
	'<ul id="nav-mobile" class="right hide-on-med-and-down">\n'
	f'{to_insert}'
	'\t<li class=""><a class="dropdown-trigger" href="#" data-target="dropdown-more">More<i class="material-icons right">arrow_drop_down</i></a></li>\n'
	'</ul>'
	)
	
	# generate drop down
	to_insert = ""
	for item in drop_down.keys():
		_class = 'class=""'
		if item == f:
			_class = 'class="active"'
		to_insert += f'\t<li {_class}><a href="{item}">{drop_down[item]}</a></li>\n'
	drop_down_html = (
	'<ul id="dropdown-more" class="dropdown-content">\n'
	f'{to_insert}\n'
	'</ul>'
	)
	
	# generate side nav
	to_insert = ""
	for item in side_nav.keys():
		_class = 'class=""'
		if item == f:
			_class = 'class="active"'
		to_insert += f'\t<li {_class}><a href="{item}">{side_nav[item]}</a></li>\n'
	side_nav_html = (
	'<ul id="slide-out" class="sidenav">\n'
	f'{to_insert}'
	'</ul>'
	)
	
	# perform updates
	f_content = ''
	with open(f, 'r') as current_file:
		f_content = current_file.read()
	
	# update main_bar
	f_content = re.sub(r'<ul id="nav\-mobile"(.|\n)+<\/ul>', main_bar_html, f_content)
	
	# update drop_down
	f_content = re.sub(r'<ul id="dropdown\-more"(.|\n)+<\/ul>', drop_down_html, f_content)
	
	# update side_nav
	f_content = re.sub(r'<ul id="slide\-out"(.|\n)+<\/ul>', side_nav_html, f_content)
	
	# write changes back to file
	with open(f, 'w') as current_file:
		f.write(f_content)
	


import re
from enum import Enum

class ParseState(Enum):
	ERROR = 0
	PARSING = 1
	OPENING = 2
	OPEN = 3
	CLOSING = 4
	CLOSED = 5

# usage: parse_state = parse(parse_state, char)
def parse(parse_state, char):

	#clean up
	if parse_state == ParseState.OPEN or parse_state == ParseState.CLOSED:
		parse_state = ParseState.PARSING

	terminals = ['<', '/']
	if char not in terminals:
		if parse_state == ParseState.OPENING and char != '!':
			return ParseState.OPEN
		elif parse_state == ParseState.CLOSING and char == '>':
			return ParseState.CLOSED
		else:
			return ParseState.PARSING	
	elif char == '<':
		return ParseState.OPENING
	elif char == '/':
		if parse_state == ParseState.OPENING:
			return ParseState.CLOSED
		else:
			return ParseState.CLOSING
	else:
		return  ParseState.ERROR
		

def calculate_tabs(open_tags, closed_tags):
	return open_tags - closed_tags

def html(_html):
	open_tags = 0
	closed_tags = 0
	num_tabs = 0
	parse_state = ParseState.PARSING
	
	formatted_lines = []
	lines = [line.strip() for line in _html.splitlines()]
	
	for line in lines:
		for char in line:
			parse_state = parse(parse_state, char)
			if parse_state == ParseState.OPEN:
				open_tags += 1
			elif parse_state == ParseState.CLOSED:
				closed_tags += 1
			elif parse_state == ParseState.ERROR:
				print("ERROR PARSING HTML on line: ", line)
		
		prev_tabs = num_tabs
		num_tabs = calculate_tabs(open_tags, closed_tags)
		
		tabs_to_use = num_tabs # decrease indent on the line of the closing tab
		if num_tabs > prev_tabs: # don't indent extra on the line of the opening tab
				tabs_to_use = prev_tabs
		formatted_lines.append(('\t' * tabs_to_use) + line)
		
		
	return '\n'.join(formatted_lines)


# yes, this is for  javascript inside of <script> tags
def javascript(_html):
	is_formatting = False
	is_before = True
	before = []
	to_format = []
	after = []
	lines = [line for line in _html.splitlines()]
	for line in lines:
		stripped = line.strip()
		if re.match('<script type="text/javascript">', stripped) != None:
			is_formatting = True
			before[-1] += '\n'
			is_before = False
		if is_formatting and stripped == r'</script>':
			is_formatting = False
		
		if is_before:
			before.append(line)
		elif is_formatting:
			to_format.append(stripped)
		else:
			after.append(line)
	
	formatted_lines = []
	open_tags = 0
	closed_tags = 0
	num_tabs = 0
	
	for line in to_format:
		prev_closed = closed_tags
		for char in line:
			if char == '{':
				open_tags += 1
			elif char == '}':
				closed_tags += 1
		
		prev_tabs = num_tabs
		num_tabs = calculate_tabs(open_tags, closed_tags)
		
		tabs_to_use = num_tabs # decrease indent on the line of the closing tab
		if num_tabs > prev_tabs: # don't indent extra on the line of the opening tab
				tabs_to_use = prev_tabs
		elif num_tabs == prev_tabs and closed_tags > prev_closed:
			tabs_to_use -= 1
			
		formatted_lines.append(('\t' * tabs_to_use) + line)
	
	list_of_strings = map(lambda x: '\n'.join(x), [before, formatted_lines, after])
	return '\n'.join(list_of_strings)

	

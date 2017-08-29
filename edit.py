import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
brown = (100, 0, 0)
lines = [1]
height_gap = 17
width_gap = 10

cur_cursor_w = 1
cur_cursor_l = 1
words_in_line = [0]
calc_i = 0

s = ''
editor = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Editor')

def preprocess():
	global words_in_line, calc_i
	words_in_line = []
	put_string = '\n'
	for ch in s:
		if ch == '\n':
			words_in_line.append(len(put_string))
			put_string = '\n'
		else:
			put_string += ch
	words_in_line.append(len(put_string))

def cur_index():
	global calc_i, cur_cursor_w, cur_cursor_l
	calc_i = 0
	for i in range(0, cur_cursor_l-1):
		calc_i += words_in_line[i]
	calc_i += cur_cursor_w-1

def displayText(s):
	global lines
	arial = pygame.font.Font('fonts\monaco.ttf', 15)
	arialLines = pygame.font.SysFont('Arial', 15)
	start_i = 0
	s_height = 0
	s_width = 40
	line_surface = arialLines.render(str(lines[start_i]), False, brown)

	line_seperate = pygame.draw.line(editor, blue,  (s_width - 10, 0), (s_width - 10, s_height + height_gap), 1)

	editor.blit(line_surface, (10, s_height))
	for ch in s:
		if ch == '\n':
			s_height += height_gap
			s_width = 40
			
			start_i += 1
			line_surface = arialLines.render(str(lines[start_i]), False, brown)
			editor.blit(line_surface, (10, s_height))
			line_seperate = pygame.draw.line(editor, blue,  (s_width - 10, 0), (s_width - 10, s_height + height_gap), 1)
			continue

		textSurface = arial.render(ch, False, black)
		editor.blit(textSurface, (s_width , s_height))
		s_width += width_gap

def make_menu():
	return True

def displayCursor(x, y):
	x -= 1
	y -= 1
	put_x = 40 + x * width_gap - 1
	if (put_x < 39):
		put_x = 39
	
	pygame.draw.line(editor, black,  (put_x, y * height_gap), (put_x, y * height_gap + height_gap), 1)


while True:
	changed = False
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()

		keys_pre = pygame.key.get_pressed()
		if keys_pre[pygame.K_LSHIFT] or keys_pre[pygame.K_RSHIFT]:
			if event.key == pygame.K_0:
				s = s[0:calc_i] + ')' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_1:
				s = s[0:calc_i] + '!' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_2:
				s = s[0:calc_i] + '@' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_3:
				s = s[0:calc_i] + '#' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_4:
				s = s[0:calc_i] + '$' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_5:
				s = s[0:calc_i] + '%' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_6:
				s = s[0:calc_i] + '^' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_7:
				s = s[0:calc_i] + '&' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_8:
				s = s[0:calc_i] + '*' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_9:
				s = s[0:calc_i] + '(' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_COMMA:
				s = s[0:calc_i] + '<' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_PERIOD:
				s = s[0:calc_i] + '>' + s[calc_i:len(s)]
				cur_cursor_w += 1
				cur_cursor_w += 1
			if event.key == pygame.K_SEMICOLON:
				s = s[0:calc_i] + ':' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_LEFTBRACKET:
				s = s[0:calc_i] + '{' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_RIGHTBRACKET:
				s = s[0:calc_i] + '}' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_QUOTEDBL:
				s = s[0:calc_i] + '"' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_SLASH:
				s = s[0:calc_i] + '?' + s[calc_i:len(s)]
				cur_cursor_w += 1
			if event.key == pygame.K_BACKSLASH:
				s = s[0:calc_i] + '|' + s[calc_i:len(s)]
				cur_cursor_w += 1

			cur_index()
			break

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				s = s[0:calc_i] + ' ' + s[calc_i:len(s)]

			if event.key == pygame.K_BACKSPACE:
				if cur_cursor_w == 1:
					if cur_cursor_l != 1:
						s = s[0:calc_i-1] + s[calc_i:len(s)]
						cur_cursor_l -= 1
						cur_cursor_w = words_in_line[cur_cursor_l-1]-1
					else:
						cur_cursor_w -= 1
				else:
					s = s[0:calc_i-1] + s[calc_i:len(s)]
					cur_cursor_w -= 2

			if event.key == pygame.K_RETURN:
				lines.append( lines[len(lines) - 1] + 1)
				s = s[0:calc_i] + '\n' + s[calc_i:len(s)]
				cur_cursor_w = 0
				cur_cursor_l += 1
				preprocess()

			if event.key == pygame.K_LEFT:
				if cur_cursor_w == 1 and cur_cursor_l != 1:
					cur_cursor_l -= 1
					cur_cursor_w = words_in_line[cur_cursor_l-1]-1
				else:
					cur_cursor_w -= 2

			if event.key == pygame.K_UP:
				cur_cursor_l -= 1
				if cur_cursor_w >= words_in_line[cur_cursor_l-1]:
					cur_cursor_w = words_in_line[cur_cursor_l-1]-1
				else:
					cur_cursor_w -= 1

			
			if event.key == pygame.K_DOWN:
				if cur_cursor_l < len(words_in_line):
					cur_cursor_l += 1
					if cur_cursor_w > words_in_line[cur_cursor_l-1]:
						cur_cursor_w = words_in_line[cur_cursor_l-1]-1
					else:
						cur_cursor_w -= 1
				elif cur_cursor_l == len(words_in_line):
					cur_cursor_w -= 1
			
			if event.key == pygame.K_RIGHT:
				if cur_cursor_w >= words_in_line[cur_cursor_l-1]:
					cur_cursor_w = 0
					cur_cursor_l += 1
				if cur_cursor_l > len(words_in_line):
					cur_cursor_l = len(words_in_line)
				pass
			
			if event.key == pygame.K_0 or event.key == pygame.K_KP0:
				s = s[0:calc_i] + '0' + s[calc_i:len(s)]
			if event.key == pygame.K_1 or event.key == pygame.K_KP1:
				s = s[0:calc_i] + '1' + s[calc_i:len(s)]
			if event.key == pygame.K_2 or event.key == pygame.K_KP2:
				s = s[0:calc_i] + '2' + s[calc_i:len(s)]
			if event.key == pygame.K_3 or event.key == pygame.K_KP3:
				s = s[0:calc_i] + '3' + s[calc_i:len(s)]
			if event.key == pygame.K_4 or event.key == pygame.K_KP4:
				s = s[0:calc_i] + '4' + s[calc_i:len(s)]
			if event.key == pygame.K_5 or event.key == pygame.K_KP5:
				s = s[0:calc_i] + '5' + s[calc_i:len(s)]
			if event.key == pygame.K_6 or event.key == pygame.K_KP6:
				s = s[0:calc_i] + '6' + s[calc_i:len(s)]
			if event.key == pygame.K_7 or event.key == pygame.K_KP7:
				s = s[0:calc_i] + '7' + s[calc_i:len(s)]
			if event.key == pygame.K_8 or event.key == pygame.K_KP8:
				s = s[0:calc_i] + '8' + s[calc_i:len(s)]
			if event.key == pygame.K_9 or event.key == pygame.K_KP9:
				s = s[0:calc_i] + '9' + s[calc_i:len(s)]

			if event.key == pygame.K_QUOTEDBL:
				s = s[0:calc_i] + "'" + s[calc_i:len(s)]
			if event.key == pygame.K_SEMICOLON:
				s = s[0:calc_i] + ';' + s[calc_i:len(s)]
			if event.key == pygame.K_EQUALS:
				s = s[0:calc_i] + '=' + s[calc_i:len(s)]
			if event.key == pygame.K_AT:
				s = s[0:calc_i] + '@' + s[calc_i:len(s)]
			if event.key == pygame.K_LEFTBRACKET:
				s = s[0:calc_i] + '[' + s[calc_i:len(s)]
			if event.key == pygame.K_BACKSLASH:
				s = s[0:calc_i] + '\\' + s[calc_i:len(s)]
			if event.key == pygame.K_RIGHTBRACKET:
				s = s[0:calc_i] + ']' + s[calc_i:len(s)]
			if event.key == pygame.K_CARET:
				s = s[0:calc_i] + '^' + s[calc_i:len(s)]
			if event.key == pygame.K_UNDERSCORE:
				s = s[0:calc_i] + '_' + s[calc_i:len(s)]
			if event.key == pygame.K_BACKQUOTE:
				s = s[0:calc_i] + '`' + s[calc_i:len(s)]
			if event.key == pygame.K_SLASH:
				s = s[0:calc_i] + '/' + s[calc_i:len(s)]
			if event.key == pygame.K_COMMA:
				s = s[0:calc_i] + ',' + s[calc_i:len(s)]
			if event.key == pygame.K_PERIOD:
				s = s[0:calc_i] + '.' + s[calc_i:len(s)]
			if event.key == pygame.K_TAB:
				s = s[0:calc_i] + '    ' + s[calc_i:len(s)]
				cur_cursor_w += 3
			if event.key == pygame.K_a:
				
				s = s[0:calc_i] + 'a' + s[calc_i:len(s)]
			if event.key == pygame.K_b:
				
				s = s[0:calc_i] + 'b' + s[calc_i:len(s)]
			if event.key == pygame.K_c:
				
				s = s[0:calc_i] + 'c' + s[calc_i:len(s)]
			if event.key == pygame.K_d:
				
				s = s[0:calc_i] + 'd' + s[calc_i:len(s)]
			if event.key == pygame.K_e:
				
				s = s[0:calc_i] + 'e' + s[calc_i:len(s)]
			if event.key == pygame.K_f:
				
				s = s[0:calc_i] + 'f' + s[calc_i:len(s)]
			if event.key == pygame.K_g:
				
				s = s[0:calc_i] + 'g' + s[calc_i:len(s)]
			if event.key == pygame.K_h:
				
				s = s[0:calc_i] + 'h' + s[calc_i:len(s)]
			if event.key == pygame.K_i:
				
				s = s[0:calc_i] + 'i' + s[calc_i:len(s)]
			if event.key == pygame.K_j:
				
				s = s[0:calc_i] + 'j' + s[calc_i:len(s)]
			if event.key == pygame.K_k:
				
				s = s[0:calc_i] + 'k' + s[calc_i:len(s)]
			if event.key == pygame.K_l:
				
				s = s[0:calc_i] + 'l' + s[calc_i:len(s)]
			if event.key == pygame.K_m:
				
				s = s[0:calc_i] + 'm' + s[calc_i:len(s)]
			if event.key == pygame.K_n:
				
				s = s[0:calc_i] + 'n' + s[calc_i:len(s)]
			if event.key == pygame.K_o:
				
				s = s[0:calc_i] + 'o' + s[calc_i:len(s)]
			if event.key == pygame.K_p:
				
				s = s[0:calc_i] + 'p' + s[calc_i:len(s)]
			if event.key == pygame.K_q:
				
				s = s[0:calc_i] + 'q' + s[calc_i:len(s)]
			if event.key == pygame.K_r:
				
				s = s[0:calc_i] + 'r' + s[calc_i:len(s)]
			if event.key == pygame.K_s:
				
				s = s[0:calc_i] + 's' + s[calc_i:len(s)]
			if event.key == pygame.K_t:
				
				s = s[0:calc_i] + 't' + s[calc_i:len(s)]
			if event.key == pygame.K_u:
				
				s = s[0:calc_i] + 'u' + s[calc_i:len(s)]
			if event.key == pygame.K_v:
				
				s = s[0:calc_i] + 'v' + s[calc_i:len(s)]
			if event.key == pygame.K_w:
				
				s = s[0:calc_i] + 'w' + s[calc_i:len(s)]
			if event.key == pygame.K_x:
				
				s = s[0:calc_i] + 'x' + s[calc_i:len(s)]
			if event.key == pygame.K_y:
				
				s = s[0:calc_i] + 'y' + s[calc_i:len(s)]
			if event.key == pygame.K_z:
				
				s = s[0:calc_i] + 'z' + s[calc_i:len(s)]

			cur_cursor_w += 1
			
			if cur_cursor_w < 1:
				cur_cursor_w = 1
			if cur_cursor_l < 1:
				cur_cursor_l = 1
			if cur_cursor_l > len(words_in_line):
				cur_cursor_l = len(words_in_line)

			changed = True

	if changed:
		preprocess()
		cur_index()
		changed = False

	editor.fill(white)
	displayText(s)

	displayCursor(cur_cursor_w, cur_cursor_l)

	pygame.display.update()
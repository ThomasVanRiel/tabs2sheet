lookup_strings = {
	'E':['E','F','Gb','G','Ab','A','Bb','B','C','Db','D','Eb'],
	'A':['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab'],
	'D':['D','Eb','E','F','Gb','G','Ab','A','Bb','B','C','Db'],
	'G':['G','Ab','A','Bb','B','C','Db','D','Eb','E','F','Gb']
}


# tabs = "G --------------------------------\nD --------------------------------\nA --------------------------------\nE ------3-5-----3-5-------5-3-5-3"
# tabs = "G --------4-7-4---------------------------6-------4----------------\nD ----4-7-------7-4-------4-7-4-------6-9-----4-7---7-4-----7-4----\nA --5-----------------4-7-------7-4-7-------5-----------7-4-----7-4\nE ------------------5----------------------------------------------"
# tabs = "G -----------------\nD -----------------\nA -----------------\nE --5-----3-5-----3"
# tabs = "G --------------------------------\nD 7-4-----7-4-----7-4-----7-5-4---\nA ----7-4-----7-4-----7-4-------7-\nE --------------------------------"
# tabs = "G ----------------\nD ------4-7-4-----\nA --4-7-------7-4-\nE 5---------------"
tabs = "G --------------------------------\nD --------------------------------\nA --------------------------------\nE ------3-5-----3-5-------5-5-5-5-"

def beats_to_notes(beats):
	notes = []
	for beat in beats:
		if beat == '':
			notes.append('')
		else:
			notes.append(lookup_strings[beat[:1]][int(beat[1:])])
	return notes

def main():
	raw_strings = tabs.split('\n')
	strings = {}	
	length = 0
	for string in raw_strings:
		strings[string[:1]]=string[2:]
		length = len(string[2:])
	
	if length%2:
		length += 1
	
	beats = []
	
	for x in xrange(0,length, 2):
		is_beat_added = False
		for snare, notes in strings.iteritems():
			tab = notes[x:x+1]
			if tab is not '-':
				beats.append(snare+tab)
				is_beat_added = True
		if not is_beat_added:
			beats.append('')
	notes = beats_to_notes(beats)
	print notes

if __name__ == '__main__':
	main()
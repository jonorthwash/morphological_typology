import sys, re 

n_syll = 0
n_feats = 0
n_tokens = 0
n_types = 0
dico = {}
n_analyses = 0
token_length = 0

for block in open(sys.argv[1]).read().split('\n'):
	for line in block.split('\n'):
		if line.strip() == '':
			continue
		if line[0] == '#':
			continue
		if '.' in line[0] or '-' in line[0]:
			continue
		row = line.split('\t')
		if len(row) != 10:
			continue

		#4	жылы	жыл	NOUN	n	Case=Nom|Number[psor]=Plur,Sing|Person[psor]=3	24	obl	_	_
		token = row[1]
		lem = row[2]
		tag = row[3]
		token_length += len(row[1])

		if tag not in ['VERB', 'NOUN']:
			continue
	
		feats = row[5].split('|')
		n_feats += len(feats)
		n_tokens += 1
		
		if token not in dico:
			dico[token] = []
		dico[token].append(lem + '#' + '|'.join(feats))

n_types = len(dico.keys())
t_length = 0
for tipus in dico:
	n_analyses += len(list(set(dico[tipus])))
	t_length += len(tipus)

print(n_feats, file=sys.stderr)
print(n_types, file=sys.stderr)
print(n_tokens, file=sys.stderr)
print(n_analyses, file=sys.stderr)
print(t_length, file=sys.stderr)

code = sys.argv[1].split('/')[1].split('_')[0]

#print('%s\t%s\t%.4f\t%.4f\t%.4f' % (sys.argv[1], code, n_feats/n_tokens, n_analyses/t_length, n_analyses/n_types))
print('%s\t%s\t%.4f\t%.4f\t%.4f' % (sys.argv[1], code, n_feats/n_tokens, n_feats/token_length, n_analyses/n_types))

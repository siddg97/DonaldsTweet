import random

startings = list()
token_list = list()
models = list()

# build markov model from list of tokens with n-grams
def build_markov_model(n, tokens):
	markov = dict()
	if(len(tokens) < n):	# if less tokens that the length of each n-gram ]=> do nothing
		return markov
	for i in range(len(tokens) - n):
		gram = tuple(tokens[i:i+n])	# grab the next n tokens and save in a tuple
		_next = tokens[i+n]			# go the next initial token
		if gram in markov:
			markov[gram].append(_next)
		else:
			markov[gram] = [_next]
	last_gram = tuple(tokens[len(tokens)-n:])
	if last_gram in markov:
		markov[last_gram].append(None)
	else:
		markov[last_gram] = [None]
	return markov


# generate a sample text from existing makrov model data
def generate(markov_model, n, start=None, niter=100):
	if start is None:	# choose a random start 
		start = random.choice(markov_model.keys())
	output = list(start)
	curr = tuple(start)
	for i in range(niter):
		if curr in markov_model:	# if already in markov model get the next possible token
			next_possible = markov_model[curr]
			new_token = random.choice(next_possible)	# choose randomly from the token array
			if new_token is None:	# end of text generation
				break
			output.append(new_token)
			curr = tuple(output[-n:])
		else:
			break
	return output

# merge a list of markov models into one model
def merge_markov_models(list_of_models):
	model_merge = dict()
	for each in list_of_models:
		for key, val in each.items():
			if key in model_merge:
				model_merge[key].extend(val)
			else:
				model_merge[key] = val
	return model_merge

# get text for line-by-line input of tokens
def getText(txt, n, count=14, niter=100):
	for token_line in txt:
		Astarting = token_line[:n]
		startings.append(Astarting)
		Amodel = build_markov_model(n, token_line)
		models.append(Amodel)
	concatModels = merge_markov_models(models)
	result_list = list()
	for i in range(count):
		result = generate(concatModels,n,random.choice(startings), niter)
		result_list.append(result)
	return result_list

def generate_word_level(n, count=14, niter=100):
	txt = open("inputs.txt","r")
	for each in txt:
		each = each.replace('\n','')
		each = each.replace('.','')
		each = each.lower()
		each = each.split()
		token_list.append(each)

	generated = getText(token_list, n, count, niter)
	#print(generated)
	output = ''
	for each in generated:
		for word in each:
			output += word + ' '
	return output
	


w = generate_word_level(3,14,100)
print(len(w))
print(w)
print(merge_markov_models(models))

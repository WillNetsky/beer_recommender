# beer_recommender
beer recommendation engine project for Metis

# todo
	~take all beer styles~
	~scrape every beer with more than 25 hads~
		~20.8k~
	~take first 100 reviews from top reviewers for those beers~

	text processing
		~remove names of breweries~
		+remove words common to beer names (IPA etc)
		~remove words with numbers~
		+lemmatize all words
		~remove all words less than 3 chars (sn, rr, etc)~

	model
		~similar words between beers~
		kmeans on the lsi, hopefully this gives something similar to the beer styles

	visualization
		force directed graph of beer types
		teaswarm

	Flask App
		~beer emoji favicon~
		~javascript autocomplete~
		* result formatting
			~links to ba pages~
			~two columns~
				+ make this into a table
				~one is the beers with ba pages~
				~one is the keywords between beers~
					-the other is the part of the visualization where these beers occur
		~make text input wider~
		- search for both beer and brewery

		-hop word descriptions
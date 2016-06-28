# beer_recommender
beer recommendation engine project for Metis

# todo  
**scraping**
- [x] take all beer styles  
- [x] scrape every beer with more than 25 hads (~20.8k)
- [x] take first 100 reviews from top reviewers for those beers  
  
**text processing**
- [x] remove names of breweries  
- [x] remove words common to beer names (IPA etc)  
- [x] remove words with numbers  
- [ ] lemmatize all words  
- [x] remove all words less than 3 chars (sn, rr, etc)  
  
**model**
- [x] similar words between beers  
- [ ] kmeans on the lsi, hopefully this gives something similar to the beer styles  
  
**visualization**
- [ ] force directed graph of beer types  
- [ ] teaswarm  
  
**Flask App**
- [x] beer emoji favicon  
- [x] javascript autocomplete  
**result formatting**
	- [x] links to ba pages  
	- [x] two columns  
		+ make this into a table  
		- [x] one is the beers with ba pages  
		- [x] one is the keywords between beers  
			- [ ] the other is the part of the visualization where these beers occur 
- [x] make text input wider  
- [ ] search for both beer and brewery  

-hop word descriptions  
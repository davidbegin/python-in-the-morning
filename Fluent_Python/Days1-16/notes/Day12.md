Day 12
======

Questions
---------
	* What is this syntax called: d[key]` notation?
	* Understand: Most use cases don't need or want the reverse lookup feature
  (what is wanted is a set of one-way canonicalization functions).
	* 

Learnings
---------
	* The default_factory of a defaultdict is only invoked to provide default values for __getitem__ calls, and not for the other methods. For example, if dd is a defaultdict, and k is a missing key, dd[k] will call the default_factory to create a default value, but dd.get(k) still returns None.
	* A better way to create a user-defined mapping type is to subclass collections.UserDict instead of dict
	* A search like k in my_dict.keys() is efficient in Python 3 even for very large mappings because dict.keys() returns a view, which is similar to a set, and containment checks in sets are as fast as in dictionaries. 

Ponderings
----------
	* Is there a faster way for this string or int lookup?
			`return key in self.keys() or str(key) in self.keys()`
			create a list of string and int keys ahead of time.

	* Can we use ChainMap for our Method Aliases for Morguebot?
	* Can we use Counter for our Most Popular Runes and Weapons commands?


Open Source
----------
	* A single script can easily control more than board at the same time.
		* http://www.pingo.io/docs/

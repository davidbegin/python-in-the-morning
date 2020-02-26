Day 15
======

Questions
---------
	* Should I always casefold() instead of lower()?
			When one versus the other?
			I feel like casefold always?
	* Should I not be using re, and use regex?

Learnings
---------
	* locale.getpreferredencoding(do_setlocale=True)
		Return the encoding used for text data, according to user preferences.
 		User preferences are expressed differently on different systems,
 		and might not be available programmatically on some systems,
 		so this function only returns a guess. […]

		Therefore, the best advice about encoding defaults is: do not rely on them.

	* We can add an accent to anything! \u0301
	* Might want to use NFKC or NFKD when we are stretching the searching,
 		through normalization: 1⁄2 inch' also finds documents containing '½ inch'.
		NFKC and NFKD normalization should be applied with care and only in
 		special cases—e.g., search and indexing—and not for permanent storage,
 		because these transformations cause data loss.
	* ` print('U+%04x' % ord(char))`
	* Don't use Bytes when defining Regular Expressions
		- you can use regular expressions on str and bytes,
 			but in the second case bytes outside of the ASCII range
 			are treated as nondigits and nonword characters.
	* My take after many hours studying Unicode:
 		it is hugely complex and full of special cases,
 		reflecting the wonderful variety of human languages
 		and the politics of industry standards.
	* DONT USE: sys.setdefaultencoding

Ponderings
----------
  * Is this something I should actually do?
      - Always pass an explicit encoding=


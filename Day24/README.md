2019 - 12 - 19
==============

Questions
=========

Learnings
=========
	* cls is the python way
		ruby - klass

Make money teaching programming:
	* Step 1:
			- Create book that teaches you old way
			- Create another boook that teachers newer way
			- Wait for newer ways
			- Repeat

Ponderings
==========
	* Should we always be trying to mimic the Standard Library APIs
		Pro:
			- Someone whose a Pythonista, might find your API obvious
		Con:
			- Bad Branding
				- Is this from the standard library or Joe Schmo


	* What are valid use cases for @staticmethod?
		Pro:
			- Its in a namespace
		Con:
			- Making refactoring slightly harder


Which do you like better:

```
# This
class_name = type(self).__name__
return '{}({!r}, {!r})'.format(class_name, *self)

# Or This
return f"{self.__class__.__name__}({self.x}, {self.y})"
```


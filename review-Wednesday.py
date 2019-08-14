Python 3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
APPLE Apple banana APPLE Orange orange APPLE Orange orange ORANGE Banana orange APPLE Orange banana ORANGE Apple banana APPLE Banana orange ORANGE Apple orange BANANA Orange apple APPLE Apple orange BANANA Banana banana BANANA Apple apple APPLE Apple orange APPLE Apple orange BANANA Apple banana ORANGE Apple orange ORANGE Orange apple APPLE Banana apple APPLE Orange apple BANANA Apple apple APPLE Apple orange APPLE Banana banana BANANA Banana apple ORANGE Apple banana APPLE Orange apple APPLE Banana banana BANANA Orange banana ORANGE Orange banana ORANGE Orange orange APPLE Orange banana ORANGE Apple apple BANANA Apple orange ORANGE Apple orange ORANGE Orange orange BANANA Orange apple BANANA Orange banana BANANA Apple apple APPLE Apple apple APPLE Apple orange APPLE Orange apple APPLE Banana banana BANANA Banana orange BANANA Apple apple BANANA Orange banana APPLE Orange banana ORANGE Orange apple BANANA Apple apple BANANA Banana orange ORANGE Banana orange BANANA Orange apple APPLE Orange banana ORANGE Banana banana ORANGE Apple orange ORANGE Banana apple ORANGE Orange banana APPLE Banana banana BANANA Banana orange ORANGE Apple banana APPLE Apple banana BANANA Orange banana APPLE Banana banana BANANA Apple apple APPLE Orange orange APPLE Orange apple BANANA Orange apple APPLE Orange apple BANANA Apple apple ORANGE Apple apple ORANGE Apple banana APPLE Apple apple ORANGE Apple banana BANANA Apple orange APPLE Orange apple APPLE Apple banana APPLE Apple orange ORANGE Apple apple ORANGE Orange orange ORANGE Apple orange BANANA Orange banana BANANA Apple apple BANANA Banana orange APPLE Apple orange BANANA Apple orange BANANA Orange banana ORANGE Apple banana APPLE Banana banana BANANA Banana apple APPLE Orange banana APPLE Orange orange ORANGE Orange banana BANANA Banana orange BANANA Orange banana BANANA Banana banana BANANA Apple apple BANANA Orange orange APPLE Apple orange APPLE Orange apple BANANA Banana apple ORANGE Banana orange APPLE Apple orange
>>> fruit
'APPLE Apple banana APPLE Orange orange APPLE Orange orange ORANGE Banana orange APPLE Orange banana ORANGE Apple banana APPLE Banana orange ORANGE Apple orange BANANA Orange apple APPLE Apple orange BANANA Banana banana BANANA Apple apple APPLE Apple orange APPLE Apple orange BANANA Apple banana ORANGE Apple orange ORANGE Orange apple APPLE Banana apple APPLE Orange apple BANANA Apple apple APPLE Apple orange APPLE Banana banana BANANA Banana apple ORANGE Apple banana APPLE Orange apple APPLE Banana banana BANANA Orange banana ORANGE Orange banana ORANGE Orange orange APPLE Orange banana ORANGE Apple apple BANANA Apple orange ORANGE Apple orange ORANGE Orange orange BANANA Orange apple BANANA Orange banana BANANA Apple apple APPLE Apple apple APPLE Apple orange APPLE Orange apple APPLE Banana banana BANANA Banana orange BANANA Apple apple BANANA Orange banana APPLE Orange banana ORANGE Orange apple BANANA Apple apple BANANA Banana orange ORANGE Banana orange BANANA Orange apple APPLE Orange banana ORANGE Banana banana ORANGE Apple orange ORANGE Banana apple ORANGE Orange banana APPLE Banana banana BANANA Banana orange ORANGE Apple banana APPLE Apple banana BANANA Orange banana APPLE Banana banana BANANA Apple apple APPLE Orange orange APPLE Orange apple BANANA Orange apple APPLE Orange apple BANANA Apple apple ORANGE Apple apple ORANGE Apple banana APPLE Apple apple ORANGE Apple banana BANANA Apple orange APPLE Orange apple APPLE Apple banana APPLE Apple orange ORANGE Apple apple ORANGE Orange orange ORANGE Apple orange BANANA Orange banana BANANA Apple apple BANANA Banana orange APPLE Apple orange BANANA Apple orange BANANA Orange banana ORANGE Apple banana APPLE Banana banana BANANA Banana apple APPLE Orange banana APPLE Orange orange ORANGE Orange banana BANANA Banana orange BANANA Orange banana BANANA Banana banana BANANA Apple apple BANANA Orange orange APPLE Apple orange APPLE Orange apple BANANA Banana apple ORANGE Banana orange APPLE Apple orange'
>>> 
>>> lst = fruit.split()
>>> lst
['APPLE', 'Apple', 'banana', 'APPLE', 'Orange', 'orange', 'APPLE', 'Orange', 'orange', 'ORANGE', 'Banana', 'orange', 'APPLE', 'Orange', 'banana', 'ORANGE', 'Apple', 'banana', 'APPLE', 'Banana', 'orange', 'ORANGE', 'Apple', 'orange', 'BANANA', 'Orange', 'apple', 'APPLE', 'Apple', 'orange', 'BANANA', 'Banana', 'banana', 'BANANA', 'Apple', 'apple', 'APPLE', 'Apple', 'orange', 'APPLE', 'Apple', 'orange', 'BANANA', 'Apple', 'banana', 'ORANGE', 'Apple', 'orange', 'ORANGE', 'Orange', 'apple', 'APPLE', 'Banana', 'apple', 'APPLE', 'Orange', 'apple', 'BANANA', 'Apple', 'apple', 'APPLE', 'Apple', 'orange', 'APPLE', 'Banana', 'banana', 'BANANA', 'Banana', 'apple', 'ORANGE', 'Apple', 'banana', 'APPLE', 'Orange', 'apple', 'APPLE', 'Banana', 'banana', 'BANANA', 'Orange', 'banana', 'ORANGE', 'Orange', 'banana', 'ORANGE', 'Orange', 'orange', 'APPLE', 'Orange', 'banana', 'ORANGE', 'Apple', 'apple', 'BANANA', 'Apple', 'orange', 'ORANGE', 'Apple', 'orange', 'ORANGE', 'Orange', 'orange', 'BANANA', 'Orange', 'apple', 'BANANA', 'Orange', 'banana', 'BANANA', 'Apple', 'apple', 'APPLE', 'Apple', 'apple', 'APPLE', 'Apple', 'orange', 'APPLE', 'Orange', 'apple', 'APPLE', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'Apple', 'apple', 'BANANA', 'Orange', 'banana', 'APPLE', 'Orange', 'banana', 'ORANGE', 'Orange', 'apple', 'BANANA', 'Apple', 'apple', 'BANANA', 'Banana', 'orange', 'ORANGE', 'Banana', 'orange', 'BANANA', 'Orange', 'apple', 'APPLE', 'Orange', 'banana', 'ORANGE', 'Banana', 'banana', 'ORANGE', 'Apple', 'orange', 'ORANGE', 'Banana', 'apple', 'ORANGE', 'Orange', 'banana', 'APPLE', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'ORANGE', 'Apple', 'banana', 'APPLE', 'Apple', 'banana', 'BANANA', 'Orange', 'banana', 'APPLE', 'Banana', 'banana', 'BANANA', 'Apple', 'apple', 'APPLE', 'Orange', 'orange', 'APPLE', 'Orange', 'apple', 'BANANA', 'Orange', 'apple', 'APPLE', 'Orange', 'apple', 'BANANA', 'Apple', 'apple', 'ORANGE', 'Apple', 'apple', 'ORANGE', 'Apple', 'banana', 'APPLE', 'Apple', 'apple', 'ORANGE', 'Apple', 'banana', 'BANANA', 'Apple', 'orange', 'APPLE', 'Orange', 'apple', 'APPLE', 'Apple', 'banana', 'APPLE', 'Apple', 'orange', 'ORANGE', 'Apple', 'apple', 'ORANGE', 'Orange', 'orange', 'ORANGE', 'Apple', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'Apple', 'apple', 'BANANA', 'Banana', 'orange', 'APPLE', 'Apple', 'orange', 'BANANA', 'Apple', 'orange', 'BANANA', 'Orange', 'banana', 'ORANGE', 'Apple', 'banana', 'APPLE', 'Banana', 'banana', 'BANANA', 'Banana', 'apple', 'APPLE', 'Orange', 'banana', 'APPLE', 'Orange', 'orange', 'ORANGE', 'Orange', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'Banana', 'banana', 'BANANA', 'Apple', 'apple', 'BANANA', 'Orange', 'orange', 'APPLE', 'Apple', 'orange', 'APPLE', 'Orange', 'apple', 'BANANA', 'Banana', 'apple', 'ORANGE', 'Banana', 'orange', 'APPLE', 'Apple', 'orange']
>>> list(filter(lambda x: x.upper() != 'APPLE', lst))
['banana', 'Orange', 'orange', 'Orange', 'orange', 'ORANGE', 'Banana', 'orange', 'Orange', 'banana', 'ORANGE', 'banana', 'Banana', 'orange', 'ORANGE', 'orange', 'BANANA', 'Orange', 'orange', 'BANANA', 'Banana', 'banana', 'BANANA', 'orange', 'orange', 'BANANA', 'banana', 'ORANGE', 'orange', 'ORANGE', 'Orange', 'Banana', 'Orange', 'BANANA', 'orange', 'Banana', 'banana', 'BANANA', 'Banana', 'ORANGE', 'banana', 'Orange', 'Banana', 'banana', 'BANANA', 'Orange', 'banana', 'ORANGE', 'Orange', 'banana', 'ORANGE', 'Orange', 'orange', 'Orange', 'banana', 'ORANGE', 'BANANA', 'orange', 'ORANGE', 'orange', 'ORANGE', 'Orange', 'orange', 'BANANA', 'Orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'orange', 'Orange', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'BANANA', 'Orange', 'banana', 'Orange', 'banana', 'ORANGE', 'Orange', 'BANANA', 'BANANA', 'Banana', 'orange', 'ORANGE', 'Banana', 'orange', 'BANANA', 'Orange', 'Orange', 'banana', 'ORANGE', 'Banana', 'banana', 'ORANGE', 'orange', 'ORANGE', 'Banana', 'ORANGE', 'Orange', 'banana', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'ORANGE', 'banana', 'banana', 'BANANA', 'Orange', 'banana', 'Banana', 'banana', 'BANANA', 'Orange', 'orange', 'Orange', 'BANANA', 'Orange', 'Orange', 'BANANA', 'ORANGE', 'ORANGE', 'banana', 'ORANGE', 'banana', 'BANANA', 'orange', 'Orange', 'banana', 'orange', 'ORANGE', 'ORANGE', 'Orange', 'orange', 'ORANGE', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'BANANA', 'Banana', 'orange', 'orange', 'BANANA', 'orange', 'BANANA', 'Orange', 'banana', 'ORANGE', 'banana', 'Banana', 'banana', 'BANANA', 'Banana', 'Orange', 'banana', 'Orange', 'orange', 'ORANGE', 'Orange', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'Banana', 'banana', 'BANANA', 'BANANA', 'Orange', 'orange', 'orange', 'Orange', 'BANANA', 'Banana', 'ORANGE', 'Banana', 'orange', 'orange']
>>> def keep(x):
	return x.upper() != 'APPLE'

>>> list(filter(keep, lst))
['banana', 'Orange', 'orange', 'Orange', 'orange', 'ORANGE', 'Banana', 'orange', 'Orange', 'banana', 'ORANGE', 'banana', 'Banana', 'orange', 'ORANGE', 'orange', 'BANANA', 'Orange', 'orange', 'BANANA', 'Banana', 'banana', 'BANANA', 'orange', 'orange', 'BANANA', 'banana', 'ORANGE', 'orange', 'ORANGE', 'Orange', 'Banana', 'Orange', 'BANANA', 'orange', 'Banana', 'banana', 'BANANA', 'Banana', 'ORANGE', 'banana', 'Orange', 'Banana', 'banana', 'BANANA', 'Orange', 'banana', 'ORANGE', 'Orange', 'banana', 'ORANGE', 'Orange', 'orange', 'Orange', 'banana', 'ORANGE', 'BANANA', 'orange', 'ORANGE', 'orange', 'ORANGE', 'Orange', 'orange', 'BANANA', 'Orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'orange', 'Orange', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'BANANA', 'Orange', 'banana', 'Orange', 'banana', 'ORANGE', 'Orange', 'BANANA', 'BANANA', 'Banana', 'orange', 'ORANGE', 'Banana', 'orange', 'BANANA', 'Orange', 'Orange', 'banana', 'ORANGE', 'Banana', 'banana', 'ORANGE', 'orange', 'ORANGE', 'Banana', 'ORANGE', 'Orange', 'banana', 'Banana', 'banana', 'BANANA', 'Banana', 'orange', 'ORANGE', 'banana', 'banana', 'BANANA', 'Orange', 'banana', 'Banana', 'banana', 'BANANA', 'Orange', 'orange', 'Orange', 'BANANA', 'Orange', 'Orange', 'BANANA', 'ORANGE', 'ORANGE', 'banana', 'ORANGE', 'banana', 'BANANA', 'orange', 'Orange', 'banana', 'orange', 'ORANGE', 'ORANGE', 'Orange', 'orange', 'ORANGE', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'BANANA', 'Banana', 'orange', 'orange', 'BANANA', 'orange', 'BANANA', 'Orange', 'banana', 'ORANGE', 'banana', 'Banana', 'banana', 'BANANA', 'Banana', 'Orange', 'banana', 'Orange', 'orange', 'ORANGE', 'Orange', 'banana', 'BANANA', 'Banana', 'orange', 'BANANA', 'Orange', 'banana', 'BANANA', 'Banana', 'banana', 'BANANA', 'BANANA', 'Orange', 'orange', 'orange', 'Orange', 'BANANA', 'Banana', 'ORANGE', 'Banana', 'orange', 'orange']
>>> class Student:
	def __init__(self, name, yw, sx, yy, ls):
		self.name = name
		self.yw = yw
		self.sx = sx
		self.yy = yy
		self.ls = ls

		
>>> zy = Student('Zhou Yi', 120, 130, 140, 150)
>>> zy
<__main__.Student object at 0x03DEBAD0>
>>> s = 'Zhouyi'
>>> s
'Zhouyi'
>>> type(s)
<class 'str'>
>>> type(zy)
<class '__main__.Student'>
>>> help(s)
no Python documentation found for 'Zhouyi'

>>> help(str)
Help on class str in module builtins:

class str(object)
 |  str(object='') -> str
 |  str(bytes_or_buffer[, encoding[, errors]]) -> str
 |  
 |  Create a new string object from the given object. If encoding or
 |  errors is specified, then the object must expose a data buffer
 |  that will be decoded using the given encoding and error handler.
 |  Otherwise, returns the result of object.__str__() (if defined)
 |  or repr(object).
 |  encoding defaults to sys.getdefaultencoding().
 |  errors defaults to 'strict'.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __format__(...)
 |      S.__format__(format_spec) -> str
 |      
 |      Return a formatted version of S as described by format_spec.
 |  
 |  __ge__(...)
 |      __ge__=($self, value, /)
 |      --
 |      
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(self, key, /)
 |      Return self[key].
 |  
 |  __getnewargs__(...)
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __hash__(self, /)
 |      Return hash(self).
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mod__(self, value, /)
 |      Return self%value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.n
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __rmod__(self, value, /)
 |      Return value%self.
 |  
 |  __rmul__(self, value, /)
 |      Return self*value.
 |  
 |  __sizeof__(...)
 |      S.__sizeof__() -> size of S in memory, in bytes
 |  
 |  __str__(self, /)
 |      Return str(self).
 |  
 |  capitalize(...)
 |      S.capitalize() -> str
 |      
 |      Return a capitalized version of S, i.e. make the first character
 |      have upper case and the rest lower case.
 |  
 |  casefold(...)
 |      S.casefold() -> str
 |      
 |      Return a version of S suitable for caseless comparisons.
 |  
 |  center(...)
 |      S.center(width[, fillchar]) -> str
 |      
 |      Return S centered in a string of length width. Padding is
 |      done using the specified fill character (default is a space)
 |  
 |  count(...)
 |      S.count(sub[, start[, end]]) -> int
 |      
 |      Return the number of non-overlapping occurrences of substring sub in
 |      string S[start:end].  Optional arguments start and end are
 |      interpreted as in slice notation.
 |  
 |  encode(...)
 |      S.encode(encoding='utf-8', errors='strict') -> bytes
 |      
 |      Encode S using the codec registered for encoding. Default encoding
 |      is 'utf-8'. errors may be given to set a different error
 |      handling scheme. Default is 'strict' meaning that encoding errors raise
 |      a UnicodeEncodeError. Other possible values are 'ignore', 'replace' and
 |      'xmlcharrefreplace' as well as any other name registered with
 |      codecs.register_error that can handle UnicodeEncodeErrors.
 |  
 |  endswith(...)
 |      S.endswith(suffix[, start[, end]]) -> bool
 |      
 |      Return True if S ends with the specified suffix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      suffix can also be a tuple of strings to try.
 |  
 |  expandtabs(...)
 |      S.expandtabs(tabsize=8) -> str
 |      
 |      Return a copy of S where all tab characters are expanded using spaces.
 |      If tabsize is not given, a tab size of 8 characters is assumed.
 |  
 |  find(...)
 |      S.find(sub[, start[, end]]) -> int
 |      
 |      Return the lowest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  format(...)
 |      S.format(*args, **kwargs) -> str
 |      
 |      Return a formatted version of S, using substitutions from args and kwargs.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  format_map(...)
 |      S.format_map(mapping) -> str
 |      
 |      Return a formatted version of S, using substitutions from mapping.
 |      The substitutions are identified by braces ('{' and '}').
 |  
 |  index(...)
 |      S.index(sub[, start[, end]]) -> int
 |      
 |      Like S.find() but raise ValueError when the substring is not found.
 |  
 |  isalnum(...)
 |      S.isalnum() -> bool
 |      
 |      Return True if all characters in S are alphanumeric
 |      and there is at least one character in S, False otherwise.
 |  
 |  isalpha(...)
 |      S.isalpha() -> bool
 |      
 |      Return True if all characters in S are alphabetic
 |      and there is at least one character in S, False otherwise.
 |  
 |  isdecimal(...)
 |      S.isdecimal() -> bool
 |      
 |      Return True if there are only decimal characters in S,
 |      False otherwise.
 |  
 |  isdigit(...)
 |      S.isdigit() -> bool
 |      
 |      Return True if all characters in S are digits
 |      and there is at least one character in S, False otherwise.
 |  
 |  isidentifier(...)
 |      S.isidentifier() -> bool
 |      
 |      Return True if S is a valid identifier according
 |      to the language definition.
 |      
 |      Use keyword.iskeyword() to test for reserved identifiers
 |      such as "def" and "class".
 |  
 |  islower(...)
 |      S.islower() -> bool
 |      
 |      Return True if all cased characters in S are lowercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  isnumeric(...)
 |      S.isnumeric() -> bool
 |      
 |      Return True if there are only numeric characters in S,
 |      False otherwise.
 |  
 |  isprintable(...)
 |      S.isprintable() -> bool
 |      
 |      Return True if all characters in S are considered
 |      printable in repr() or S is empty, False otherwise.
 |  
 |  isspace(...)
 |      S.isspace() -> bool
 |      
 |      Return True if all characters in S are whitespace
 |      and there is at least one character in S, False otherwise.
 |  
 |  istitle(...)
 |      S.istitle() -> bool
 |      
 |      Return True if S is a titlecased string and there is at least one
 |      character in S, i.e. upper- and titlecase characters may only
 |      follow uncased characters and lowercase characters only cased ones.
 |      Return False otherwise.
 |  
 |  isupper(...)
 |      S.isupper() -> bool
 |      
 |      Return True if all cased characters in S are uppercase and there is
 |      at least one cased character in S, False otherwise.
 |  
 |  join(...)
 |      S.join(iterable) -> str
 |      
 |      Return a string which is the concatenation of the strings in the
 |      iterable.  The separator between elements is S.
 |  
 |  ljust(...)
 |      S.ljust(width[, fillchar]) -> str
 |      
 |      Return S left-justified in a Unicode string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  lower(...)
 |      S.lower() -> str
 |      
 |      Return a copy of the string S converted to lowercase.
 |  
 |  lstrip(...)
 |      S.lstrip([chars]) -> str
 |      
 |      Return a copy of the string S with leading whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  partition(...)
 |      S.partition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, and return the part before it,
 |      the separator itself, and the part after it.  If the separator is not
 |      found, return S and two empty strings.
 |  
 |  replace(...)
 |      S.replace(old, new[, count]) -> str
 |      
 |      Return a copy of S with all occurrences of substring
 |      old replaced by new.  If the optional argument count is
 |      given, only the first count occurrences are replaced.
 |  
 |  rfind(...)
 |      S.rfind(sub[, start[, end]]) -> int
 |      
 |      Return the highest index in S where substring sub is found,
 |      such that sub is contained within S[start:end].  Optional
 |      arguments start and end are interpreted as in slice notation.
 |      
 |      Return -1 on failure.
 |  
 |  rindex(...)
 |      S.rindex(sub[, start[, end]]) -> int
 |      
 |      Like S.rfind() but raise ValueError when the substring is not found.
 |  
 |  rjust(...)
 |      S.rjust(width[, fillchar]) -> str
 |      
 |      Return S right-justified in a string of length width. Padding is
 |      done using the specified fill character (default is a space).
 |  
 |  rpartition(...)
 |      S.rpartition(sep) -> (head, sep, tail)
 |      
 |      Search for the separator sep in S, starting at the end of S, and return
 |      the part before it, the separator itself, and the part after it.  If the
 |      separator is not found, return two empty strings and S.
 |  
 |  rsplit(...)
 |      S.rsplit(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string, starting at the end of the string and
 |      working to the front.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified, any whitespace string
 |      is a separator.
 |  
 |  rstrip(...)
 |      S.rstrip([chars]) -> str
 |      
 |      Return a copy of the string S with trailing whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  split(...)
 |      S.split(sep=None, maxsplit=-1) -> list of strings
 |      
 |      Return a list of the words in S, using sep as the
 |      delimiter string.  If maxsplit is given, at most maxsplit
 |      splits are done. If sep is not specified or is None, any
 |      whitespace string is a separator and empty strings are
 |      removed from the result.
 |  
 |  splitlines(...)
 |      S.splitlines([keepends]) -> list of strings
 |      
 |      Return a list of the lines in S, breaking at line boundaries.
 |      Line breaks are not included in the resulting list unless keepends
 |      is given and true.
 |  
 |  startswith(...)
 |      S.startswith(prefix[, start[, end]]) -> bool
 |      
 |      Return True if S starts with the specified prefix, False otherwise.
 |      With optional start, test S beginning at that position.
 |      With optional end, stop comparing S at that position.
 |      prefix can also be a tuple of strings to try.
 |  
 |  strip(...)
 |      S.strip([chars]) -> str
 |      
 |      Return a copy of the string S with leading and trailing
 |      whitespace removed.
 |      If chars is given and not None, remove characters in chars instead.
 |  
 |  swapcase(...)
 |      S.swapcase() -> str
 |      
 |      Return a copy of S with uppercase characters converted to lowercase
 |      and vice versa.
 |  
 |  title(...)
 |      S.title() -> str
 |      
 |      Return a titlecased version of S, i.e. words start with title case
 |      characters, all remaining cased characters have lower case.
 |  
 |  translate(...)
 |      S.translate(table) -> str
 |      
 |      Return a copy of the string S, where all characters have been mapped
 |      through the given translation table, which must be a mapping of
 |      Unicode ordinals to Unicode ordinals, strings, or None.
 |      Unmapped characters are left untouched. Characters mapped to None
 |      are deleted.
 |  
 |  upper(...)
 |      S.upper() -> str
 |      
 |      Return a copy of S converted to uppercase.
 |  
 |  zfill(...)
 |      S.zfill(width) -> str
 |      
 |      Pad a numeric string S with zeros on the left, to fill a field
 |      of the specified width. The string S is never truncated.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  maketrans(x, y=None, z=None, /)
 |      Return a translation table usable for str.translate().
 |      
 |      If there is only one argument, it must be a dictionary mapping Unicode
 |      ordinals (integers) or characters to Unicode ordinals, strings or None.
 |      Character keys will be then converted to ordinals.
 |      If there are two arguments, they must be strings of equal length, and
 |      in the resulting dictionary, each character in x will be mapped to the
 |      character at the same position in y. If there is a third argument, it
 |      must be a string, whose characters will be mapped to None in the result.

>>> wyh = Student('Wang Yuheng', 120, 130, 140, 150)
>>> student_lst = [zy, wyh]
>>> wyh.yw
120
>>> wyh.name
'Wang Yuheng'
>>> 'Wang Yuheng'
'Wang Yuheng'
>>> wyh.ls
150
>>> wyh.name.islower()
False
>>> ''.islower()
False
>>> 'wyh'.islower()
True
>>> 'wyh&zy'.islower()
True
>>> 'wyh & zy'.islower()
True
>>> import sys
>>> help(sys)
Help on built-in module sys:

NAME
    sys

MODULE REFERENCE
    http://docs.python.org/3.4/library/sys
    
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

DESCRIPTION
    This module provides access to some objects used or maintained by the
    interpreter and to functions that interact strongly with the interpreter.
    
    Dynamic objects:
    
    argv -- command line arguments; argv[0] is the script pathname if known
    path -- module search path; path[0] is the script directory, else ''
    modules -- dictionary of loaded modules
    
    displayhook -- called to show results in an interactive session
    excepthook -- called to handle any uncaught exception other than SystemExit
      To customize printing in an interactive session or to install a custom
      top-level exception handler, assign other functions to replace these.
    
    stdin -- standard input file object; used by input()
    stdout -- standard output file object; used by print()
    stderr -- standard error object; used for error messages
      By assigning other file objects (or objects that behave like files)
      to these, it is possible to redirect all of the interpreter's I/O.
    
    last_type -- type of last uncaught exception
    last_value -- value of last uncaught exception
    last_traceback -- traceback of last uncaught exception
      These three are only available in an interactive session after a
      traceback has been printed.
    
    Static objects:
    
    builtin_module_names -- tuple of module names built into this interpreter
    copyright -- copyright notice pertaining to this interpreter
    exec_prefix -- prefix used to find the machine-specific Python library
    executable -- absolute path of the executable binary of the Python interpreter
    float_info -- a struct sequence with information about the float implementation.
    float_repr_style -- string indicating the style of repr() output for floats
    hash_info -- a struct sequence with information about the hash algorithm.
    hexversion -- version information encoded as a single integer
    implementation -- Python implementation information.
    int_info -- a struct sequence with information about the int implementation.
    maxsize -- the largest supported length of containers.
    maxunicode -- the value of the largest Unicode codepoint
    platform -- platform identifier
    prefix -- prefix used to find the Python library
    thread_info -- a struct sequence with information about the thread implementation.
    version -- the version of this interpreter as a string
    version_info -- version information as a named tuple
    dllhandle -- [Windows only] integer handle of the Python DLL
    winver -- [Windows only] version number of the Python DLL
    __stdin__ -- the original stdin; don't touch!
    __stdout__ -- the original stdout; don't touch!
    __stderr__ -- the original stderr; don't touch!
    __displayhook__ -- the original displayhook; don't touch!
    __excepthook__ -- the original excepthook; don't touch!
    
    Functions:
    
    displayhook() -- print an object to the screen, and save it in builtins._
    excepthook() -- print an exception and its traceback to sys.stderr
    exc_info() -- return thread-safe information about the current exception
    exit() -- exit the interpreter by raising SystemExit
    getdlopenflags() -- returns flags to be used for dlopen() calls
    getprofile() -- get the global profiling function
    getrefcount() -- return the reference count for an object (plus one :-)
    getrecursionlimit() -- return the max recursion depth for the interpreter
    getsizeof() -- return the size of an object in bytes
    gettrace() -- get the global debug tracing function
    setcheckinterval() -- control how often the interpreter checks for events
    setdlopenflags() -- set the flags to be used for dlopen() calls
    setprofile() -- set the global profiling function
    setrecursionlimit() -- set the max recursion depth for the interpreter
    settrace() -- set the global debug tracing function

FUNCTIONS
    __displayhook__ = displayhook(...)
        displayhook(object) -> None
        
        Print an object to sys.stdout and also save it in builtins._
    
    __excepthook__ = excepthook(...)
        excepthook(exctype, value, traceback) -> None
        
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    call_tracing(...)
        call_tracing(func, args) -> object
        
        Call func(*args), while tracing is enabled.  The tracing state is
        saved, and restored afterwards.  This is intended to be called from
        a debugger from a checkpoint, to recursively debug some other code.
    
    callstats(...)
        callstats() -> tuple of integers
        
        Return a tuple of function call statistics, if CALL_PROFILE was defined
        when Python was built.  Otherwise, return None.
        
        When enabled, this function returns detailed, implementation-specific
        details about the number of function calls executed. The return value is
        a 11-tuple where the entries in the tuple are counts of:
        0. all function calls
        1. calls to PyFunction_Type objects
        2. PyFunction calls that do not create an argument tuple
        3. PyFunction calls that do not create an argument tuple
           and bypass PyEval_EvalCodeEx()
        4. PyMethod calls
        5. PyMethod calls on bound methods
        6. PyType calls
        7. PyCFunction calls
        8. generator calls
        9. All other calls
        10. Number of stack pops performed by call_function()
    
    exc_info(...)
        exc_info() -> (type, value, traceback)
        
        Return information about the most recent exception caught by an except
        clause in the current stack frame or in an older stack frame.
    
    excepthook(...)
        excepthook(exctype, value, traceback) -> None
        
        Handle an exception by displaying it with a traceback on sys.stderr.
    
    exit(...)
        exit([status])
        
        Exit the interpreter by raising SystemExit(status).
        If the status is omitted or None, it defaults to zero (i.e., success).
        If the status is an integer, it will be used as the system exit status.
        If it is another kind of object, it will be printed and the system
        exit status will be one (i.e., failure).
    
    getallocatedblocks(...)
        getallocatedblocks() -> integer
        
        Return the number of memory blocks currently allocated, regardless of their
        size.
    
    getcheckinterval(...)
        getcheckinterval() -> current check interval; see setcheckinterval().
    
    getdefaultencoding(...)
        getdefaultencoding() -> string
        
        Return the current default string encoding used by the Unicode 
        implementation.
    
    getfilesystemencoding(...)
        getfilesystemencoding() -> string
        
        Return the encoding used to convert Unicode filenames in
        operating system filenames.
    
    getprofile(...)
        getprofile()
        
        Return the profiling function set with sys.setprofile.
        See the profiler chapter in the library manual.
    
    getrecursionlimit(...)
        getrecursionlimit()
        
        Return the current value of the recursion limit, the maximum depth
        of the Python interpreter stack.  This limit prevents infinite
        recursion from causing an overflow of the C stack and crashing Python.
    
    getrefcount(...)
        getrefcount(object) -> integer
        
        Return the reference count of object.  The count returned is generally
        one higher than you might expect, because it includes the (temporary)
        reference as an argument to getrefcount().
    
    getsizeof(...)
        getsizeof(object, default) -> int
        
        Return the size of object in bytes.
    
    getswitchinterval(...)
        getswitchinterval() -> current thread switch interval; see setswitchinterval().
    
    gettrace(...)
        gettrace()
        
        Return the global debug tracing function set with sys.settrace.
        See the debugger chapter in the library manual.
    
    getwindowsversion(...)
        getwindowsversion()
        
        Return information about the running version of Windows as a named tuple.
        The members are named: major, minor, build, platform, service_pack,
        service_pack_major, service_pack_minor, suite_mask, and product_type. For
        backward compatibility, only the first 5 items are available by indexing.
        All elements are numbers, except service_pack which is a string. Platform
        may be 0 for win32s, 1 for Windows 9x/ME, 2 for Windows NT/2000/XP/Vista/7,
        3 for Windows CE. Product_type may be 1 for a workstation, 2 for a domain
        controller, 3 for a server.
    
    intern(...)
        intern(string) -> string
        
        ``Intern'' the given string.  This enters the string in the (global)
        table of interned strings whose purpose is to speed up dictionary lookups.
        Return the string itself or the previously interned string object with the
        same value.
    
    setcheckinterval(...)
        setcheckinterval(n)
        
        Tell the Python interpreter to check for asynchronous events every
        n instructions.  This also affects how often thread switches occur.
    
    setprofile(...)
        setprofile(function)
        
        Set the profiling function.  It will be called on each function call
        and return.  See the profiler chapter in the library manual.
    
    setrecursionlimit(...)
        setrecursionlimit(n)
        
        Set the maximum depth of the Python interpreter stack to n.  This
        limit prevents infinite recursion from causing an overflow of the C
        stack and crashing Python.  The highest possible limit is platform-
        dependent.
    
    setswitchinterval(...)
        setswitchinterval(n)
        
        Set the ideal thread switching delay inside the Python interpreter
        The actual frequency of switching threads can be lower if the
        interpreter executes long sequences of uninterruptible code
        (this is implementation-specific and workload-dependent).
        
        The parameter must represent the desired switching delay in seconds
        A typical value is 0.005 (5 milliseconds).
    
    settrace(...)
        settrace(function)
        
        Set the global debug tracing function.  It will be called on each
        function call.  See the debugger chapter in the library manual.

DATA
    __stderr__ = None
    __stdin__ = None
    __stdout__ = None
    api_version = 1013
    argv = [r'C:\Users\Dell\Downloads\xiaolaodi\generate_fruit.py']
    base_exec_prefix = r'C:\Python34'
    base_prefix = r'C:\Python34'
    builtin_module_names = ('_ast', '_bisect', '_codecs', '_codecs_cn', '_...
    byteorder = 'little'
    copyright = 'Copyright (c) 2001-2014 Python Software Foundati...ematis...
    dllhandle = 1723596800
    dont_write_bytecode = False
    exec_prefix = r'C:\Python34'
    executable = r'C:\Python34\pythonw.exe'
    flags = sys.flags(debug=0, inspect=0, interactive=0, opt...ing=0, quie...
    float_info = sys.float_info(max=1.7976931348623157e+308, max_...epsilo...
    float_repr_style = 'short'
    hash_info = sys.hash_info(width=32, modulus=2147483647, inf=...iphash2...
    hexversion = 50594032
    implementation = namespace(cache_tag='cpython-34', hexversion=505...in...
    int_info = sys.int_info(bits_per_digit=15, sizeof_digit=2)
    maxsize = 2147483647
    maxunicode = 1114111
    meta_path = [<class '_frozen_importlib.BuiltinImporter'>, <class '_fro...
    modules = {'__future__': <module '__future__' from 'C:\\Python34\\lib\...
    path = [r'C:\Users\Dell\Downloads\xiaolaodi', r'C:\Python34\Lib\idleli...
    path_hooks = [<class 'zipimport.zipimporter'>, <function FileFinder.pa...
    path_importer_cache = {r'C:\Python34': FileFinder('C:\\Python34'), r'C...
    platform = 'win32'
    prefix = r'C:\Python34'
    stderr = <idlelib.PyShell.PseudoOutputFile object>
    stdin = <idlelib.PyShell.PseudoInputFile object>
    stdout = <idlelib.PyShell.PseudoOutputFile object>
    thread_info = sys.thread_info(name='nt', lock=None, version=None)
    version = '3.4.0 (v3.4.0:04f714765c13, Mar 16 2014, 19:24:06) [MSC v.1...
    version_info = sys.version_info(major=3, minor=4, micro=0, releaseleve...
    warnoptions = []
    winver = '3.4'

FILE
    (built-in)


>>> 形参与实参的区别
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    形参与实参的区别
NameError: name '形参与实参的区别' is not defined
>>> parameter
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    parameter
NameError: name 'parameter' is not defined
>>> argument
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    argument
NameError: name 'argument' is not defined
>>> import string
>>> string.ascii_letters
'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
>>> 'z' in string.ascii_letters
True
>>> '?' in string.ascii_letters
False
>>> 

# TODO: need to supplement for a full guide in python regexp
import re


# regular strings in python
# "\\\\section" same as r"\\section" for matching '\section'


# matching characters
pattern1 = r'[a-z$]'  # '$' as symbol not metacharacter
pattern2 = r'[^?]'  # any symbol except '?'
pattern3 = r'[6^]'  # only '6' or '^' symbols
pattern4 = r'[\\]'  # '\' character
pattern5 = r'\d'  # matches any decimal digit '[0-9]'
pattern6 = r'\D'  # matches any non-digit character '[^0-9]'
pattern7 = r'\w'  # matches any alphanumeric character '[a-zA-Z0-9_]'
pattern8 = r'\W'  # matches any non-alpanumeric character '[^a-zA-Z0-9_]'
pattern = r'\s'
pattern = r'\S'
pattern = r'.'  # matches any character except newline, with re.DOTALL match all characters


# repeating things
# * is greedy in means that when repeating a RE, the matching engine
# will try to repeat it as many times as possible.
# If later portions of the pattern don’t match, the matching engine will
# then back up and try again with fewer repetitions.
pattern = r'.*'  # matches any character zero or more times '{0,}'
pattern = r'ca*t'  # 'ct', 'cat', 'caaaaaat' - all correct matches
pattern = r'a[bcd]*b'  # greedy in action for 'abcbd'
pattern = r'.+'  # matches any character 1 or more times '{1,}'
pattern = r'ca+t'  # matches 'cat', 'caaat' not 'ct'
pattern = r'.?'  # mathces any character 1 or zero times '{0,1}'
pattern = r'.{m,n}'  # matches any character must be at least m repetitions and at most n
pattern = r'ca{1,3}t'  # matches 'cat', 'caat', 'caaat'
pattern = r'[ab]{2}'  # mathces 'aa', 'ab', 'ba', 'bb'
pattern = r'f{,4}'  # matches '', 'f', 'ff', 'ffff'


# using regurlar expressions
pattern = r'start'
pattern_object = re.compile(pattern, flags=re.IGNORECASE | re.DOTALL)
pattern_object.match('startstart')  # Determine if the RE matches at the beginning of the string
pattern_object.search('endstart')  # Scan through a string, looking for any location where this RE matches
pattern_object.findall('sstartstartstarttart')  # Find all substrings where the RE matches, and returns them as a list

pattern = r'^(?=\S*[a-z])(?=\S*[A-Z])(?=\S*\d)\S{8,}$'
print(re.search(pattern, '1dsjflfksdwersdfA'))

import re
import inspect

BASE_FOLDER = 'expressions/'

# Load regex file based on name
def get(reg):
    with open(f'{BASE_FOLDER}{reg}.re', encoding='utf-8') as f:
        return re.compile(f.read())

# Run match and no match simulations
def simulate(reg, match, no_match):
    exp = get(reg)
    for m in match:
        assert exp.match(m)
    for n in no_match:
        assert not exp.match(n)
    
# Get the name of the function that called this function without the first 5 characters
def regname():
    return inspect.stack()[1][3][5:]

###
### End of test framework definition
###

def test_float():
    simulate(
        regname(),
        ['1.0', '7', '0.0012952137'],
        ['a', '', '1.1.1']
    )

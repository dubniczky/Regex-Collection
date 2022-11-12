import re
import inspect

BASE_FOLDER = 'expressions/'

# Load regex file based on name
def get(reg):
    with open(f'{BASE_FOLDER}{reg}.re', encoding='utf-8') as f:
        return re.compile(f.read())

# Run match and no match simulations
def simulate(match, no_match):
    exp = get(regname())
    for m in match:
        assert exp.match(m)
    for n in no_match:
        assert not exp.match(n)
    
# Get the name of the function that called this function without the first 5 characters
def regname():
    return inspect.stack()[2][3][5:]

###
### End of test framework definition
###

def test_float():
    simulate(
        ['1.0', '7', '-0.0012952137'],
        ['a', '', '1.1.1']
    )

def test_integer():
    simulate(
        ['0', '7', '-18449'],
        ['a', '', '1.1']
    )
    
def test_base64():
    simulate(
        ['0', 'abc/99=', 'Zm9vYmFyfg=='],
        ['a===', '', '#']
    )
    
def test_hex():
    simulate(
        ['0', '7', 'a', 'f', 'A', 'fF', '1234567890abcdefABCDEF'],
        ['g', '', '#']
    )
    
def test_uuid4():
    simulate(
        ['29506BA9-4854-4AF9-A311-498EBE583F1E', '6077BFD5-4A5E-4B8D-A6F3-3EAA5A7BA6CF', ],
        ['-', '', 'X9506BA9-4854-4AF9-A311-498EBE583F1E']
    )
    
def test_email():
    simulate(
        ['a@b.c', 'richard+spam@google.com', 'rick@asd.example.com' ],
        ['a @b.c', '', 'a@@b.c', '#a@b.c']
    )
    
def test_sha256():
    simulate(
        ['91c9c3ff310a53f8d179461d9af55371c78b67c38ab030bf9c026693ca495399' ],
        ['gggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg', 'a7']
    )
    
def test_md5():
    simulate(
        ['72b302bf297a228a75730123efef7c41' ],
        ['gggggggggggggggggggggggggggggggg', 'aa']
    )

def test_ipv4():
    simulate(
        ['1.1.1.1', '192.168.1.1', '255.255.255.255'],
        ['0.0.0', '10.10.10.10.10', '3000.1.1.1', '300.0.0.0']
    )
    
def test_ipv6():
    simulate(
        ['2001:0db8:0000:0000:0000:ff00:0042:8329', '::1', 'aa5::1' ],
        ['xa5::1', '', 'aa5::1::1', 'aa5::1::1::1', '1.1.1.1']
    )

def test_date():
    simulate(
        ['2000-01-01', '2020-12-31', '1991-12-21' ],
        ['2000-01-01T00:00:00', '1992-20-11', '1992-10-233']
    )
    
def test_time():
    simulate(
        ['12:33:20', '00:00:00', '23:59:59' ],
        ['12:33:20.000', '12:33:20Z', '12:33:20+00:00']
    )
    
def test_url():
    simulate(
        ['https://example.com', 'file://images.com/whale.jpg', 'http://asd.com/a/b.c' ],
        ['http', '', 'http://.com', ]
    )
    
def test_color():
    simulate(
        ['#000000', '#ffffff', '#123456', '#a1f', '#ABCDEF' ],
        ['!123456', '', '#1234567', '#12345', '#1a']
    )
    
def test_dollars():
    simulate(
        ['$9.99', '$12.5', '$12,122.2', '$0.01', '$0.00', '$2' ],
        ['$ 1.1', '$11.12.3', '', 'a', '$' ]
    )
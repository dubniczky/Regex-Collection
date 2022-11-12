# Regex Collection

Collection of regular expressions for matching strings

## Introduction

This repository is to store commonly used regular expressions for matching specific strings. They are made to be as strict as possible, so they might require some adjustments before use.



## Testing

Testing is done with Python built-in regular expression library `re`. The testing engine is `pytest`. The testing engine uses custom scripts that work in the following format:

```python
def test_NAME():
    simulate(
        [ 'MATCH_1', 'MATCH_2', '...' ],
        [ 'NOMATCH_1', 'NOMATCH_2', '...' ],
    )
```

## Contributing

1. Add your regular expression to the `expressions` folder
2. Add a test with a couple of matching, and non-matching cases

## Sources

- Custom expressions
- Contributions from internal projects
- https://projects.lukehaas.me/regexhub/

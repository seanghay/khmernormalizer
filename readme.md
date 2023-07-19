## Khmer Normalizer 

A missing toolkit for **Khmer Natural Language Processing**.

- Character Reordering
- Duplicate Whitespaces
- Remove zero width space
- Remove emojis
- Fix Common misspellings
- Fix Unicode issues
- Fix Khmer trailing vowels
- URL Replacements
- Unicode Normalization (NFKC)
- Quotes symbols normalization
- Remove repeated punctuations

### Installation

```shell
pip install khmernormalizer
```

### Usage

```python
from khmernormalizer import normalize

text = "hello, world សួស្តី​ពិភពលោក !!!! 🇰🇭"
result = normalize(text)
# -> "hello, world សួស្តី​ពិភពលោក!"
```
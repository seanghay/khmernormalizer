# -*- coding: utf-8 -*-
# adapted from https://github.com/csebuetnlp/normalizer/blob/main/normalizer/const.py
from ftfy import fix_text, TextFixerConfig
from emoji import replace_emoji
from khmernormalizer import mappings

import re
import unicodedata

def fix_quotes(text):
    text = mappings.SINGLE_QUOTE_REGEX.sub("'", text)
    text = mappings.DOUBLE_QUOTE_REGEX.sub('"', text)
    return text

def clean_khmer_trailing_vowels(text):
  text = re.sub(r"([\u17b6-\u17dd])\1+", r"\1", text)
  return text

def reordering_khmer_chars():
  pass

def normalize(
  text, 
  unicode_norm="NFKC",
  emoji_replacement=None,
  url_replacement=None,
  fix_text_config=TextFixerConfig(normalization="NFC", explain=False),
  remove_zwsp=True,
):
  
  if remove_zwsp:
    text = re.sub(r"[\u200b\u200a\u2028]", "", text)
  
  text = fix_text(text, config=fix_text_config)
  text = fix_quotes(text)
  text = mappings.MULTIPLE_PUNCT_REGEX.sub(r"\1", text)
  text = clean_khmer_trailing_vowels(text)
  text = unicodedata.normalize(unicode_norm, text)
  
  if emoji_replacement is not None:
    text = replace_emoji(text, emoji_replacement)
  
  if url_replacement is not None:
    text = mappings.URL_HANDLER_REGEX.sub(url_replacement, text)
  
  text = text.translate(mappings.CHAR_REPLACEMENTS)
  
  text = mappings.UNICODE_REPLACEMENTS_REGEX.sub(
      lambda match: mappings.UNICODE_REPLACEMENTS.get(
        match.group(0), f"{match.group(1)}\u09cc"
      ), 
      text
  )
  
  # remove duplicate whitespace but not newlines
  text = mappings.WHITESPACES_HANDLER_REGEX.sub(" ", text)
  
  # ellipsis
  text = re.sub(r"\.{3,}", "\u2026", text)
    
  # remove space between punctuation
  text = re.sub(r"[ ]+([៙៚៖!?។៕\u17d8])", r"\1", text)
  
  # remove space between the repeat char
  text = re.sub(r"[^\S\r\n]+ៗ", "ៗ", text)
  
  return text.strip()
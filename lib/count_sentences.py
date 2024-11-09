#!/usr/bin/env python3
import re

class MyString:
  def __init__(self, value = ''):
    self.value = value 

  @property
  def value(self):
    '''value property'''
    return self._value

  @value.setter
  def value(self, value):
    '''The value must be a string.'''
    if isinstance(value, str):
      self._value = value 
    else:
      print('The value must be a string.')

  def is_sentence(self):
    if self._value.endswith('.'):
      return True
    else:
      return False

  def is_question(self):
    if self._value.endswith('?'):
      return True 
    else:
      return False 

  def is_exclamation(self):
    if self._value.endswith('!'):
      return True 
    else:
      return False

  def count_sentences(self):
    sentences = re.split(r'[.!?]', self.value.strip())
    return len([s for s in sentences if s])

kelvin = MyString('This is a string! It has three sentences. Right?')
print(kelvin.is_sentence())
print(kelvin.count_sentences())

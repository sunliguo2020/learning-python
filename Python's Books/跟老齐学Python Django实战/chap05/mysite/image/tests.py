from django.test import TestCase

# Create your tests here.
from slugify import slugify

text = "This is a sample text, which will be converted to slug 我是谁"
slug = slugify(text)

print(slug)
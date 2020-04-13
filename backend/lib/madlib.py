#!/usr/bin/env python3
from jinja2 import Template

class Madlib:
    def __init__(self, title, author, nouns, verbs, adjectives, template):
        self.title = title
        self.author = author
        self.nouns = nouns
        self.verbs  = verbs
        self.adjectives = adjectives
        self.template = template

    def get_noun_count(self):
        return len(self.nouns)

    def get_verb_count(self):
        return len(self.verbs)

    def get_adj_count(self):
        return len(self.adjectives)

    def render(self):
        template = self.template
        madlib = template.render(nouns=self.nouns, verbs=self.verbs, adjectives=self.adjectives)
        return madlib

    def print_madlib(self):
        template = self.render()
        print("Title:", self.title)
        print("By:", self.author)
        print(template)


nouns = {
        'n1': 'dog',
        'n2': 'man'
}
verbs = {
        'v1': 'hopped',
        'v2': 'skipping'
}

adjectives = {
        'a1': 'nice',
        'a2': 'tall'
}

template = Template("The {{ adjectives['a1'] }} {{ nouns['n1'] }} {{ verbs['v1'] }} over to the {{ adjectives['a2'] }} {{ nouns['n2'] }} who was {{ verbs['v2'] }}")

title = 'test'
author = 'jamie'

ml1 = Madlib(title, author, nouns, verbs, adjectives, template)

ml1.print_madlib()

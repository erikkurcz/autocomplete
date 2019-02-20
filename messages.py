"""Messages for autocomplete."""

# TODO: this is ugly


class Messages(object):

    def __init__(self):
        self.messages = {
            'usage': self.usage,
            'quit': self.quit_instructions,
            'welcome_boiler': self.welcome_boiler,
            'welcome': self.welcome,
            'suggestions': self.suggestions,
            'display_trie': self.display_trie,
            'current_candidate': self.current_candidate,
            'adding_to_trie': self.adding_to_trie,
            'appending_to_candidate': self.appending_to_candidate,
            'close': self.close,
            'candidate_reset': self.candidate_reset,
            'suggestions_by_alphabet': self.suggestions_by_alphabet
        }

    def __getitem__(self, message_name):
        return self.messages[message_name]

    def usage(self):
        msg = 'Enter words at your pleasing, press enter to make a word ' \
              'the candidate suggestions.'
        msg += '\n\nCandidates are not entered until you submit the comment' \
               ' `:s` or `:sub`.'
        msg += '\n\nCandidates can be viewed using `:cur`, or cleared using' \
               ' `:clr`.'
        msg += '\n\nOnce submitted, you can view the trie using `:trie` for' \
               ' all elements, or `:a` for top 3 by case-sensitive letter.'
        msg += '\n\nTo enter words from a txt file, use `:f`, then enter a ' \
               'fully-qualified filepath. Regex is used to find words, so as' \
               ' long as file can be read as string, it should work.'
        msg += '\n\nTo retain a candidate, but enter another word ' \
               'immediately, type the word followed by a period.'
        msg += '\n\nTo enter multiple words simultaneously, type a ' \
               'space-separated list of words. They will be independently' \
               ' added. Punctuation is ignored.'
        msg += '\n\n*** Finally, to receive suggestions, enter an optional' \
               ' prefix followed by `*`, e.g. `a*` or `tes*` to see the top ' \
               '3 autocomplete suggestions given the prefix.'
        msg += '\n\n\tIf a prefix is not given, the suggestions will be ' \
               'the top 3 for the overall trie structure.'
        print(msg)

    def quit_instructions(self):
        print('If you would like to quit, enter `:q`')

    def welcome_boiler(self):
        print('************** Welcome to autocomplete! **************')

    def welcome(self):
        self.welcome_boiler()
        self.usage()
        self.quit_instructions()

    def suggestions(self, suggestions):
        base = 'Top 3 suggestions are: {}'
        print(base.format(suggestions))

    def display_trie(self, trie):
        base = 'Current trie is:\n{}'
        print(base.format(str(trie)))

    def current_candidate(self, trie):
        base = 'Current candidate is:\n{}'
        print(base.format(str(trie)))

    def adding_to_trie(self, new):
        base = 'Adding "{}" to the trie.'
        print(base.format(new))

    def appending_to_candidate(self, current, new):
        base = 'Appending "{}" to existing candidate "{}" to form: "{}"'
        print(base.format(new, current, current+new))

    def close(self):
        print('Thanks for using autocomplete!')

    def candidate_reset(self):
        print('Candidate reset to ""')

    def suggestions_by_alphabet(self):
        print('The above are suggestions for each letter of the alphabet,'
              ' capital then lowercase.')

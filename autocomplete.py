from trie import Trie, Node
import sys
from utils import alphabet, get_words_only, get_words_from_file
from messages import Messages

# TODO: use parseargs within parseargs for this?

if __name__ == '__main__':

    msgs = Messages()
    msgs['welcome']()

    t = Trie(Node(None))
    candidate = ''
    while True:
        cmd = str(input('>>> ').strip())

        if cmd.startswith(':'):
            cmd = cmd[1:]

            if cmd == 'q':
                msgs['close']()
                sys.exit(0)
            elif cmd == 'f':
                filename = str(
                    input('Enter a qualified filepath:\n>>> ').strip()
                )
                words = get_words_from_file(filename)
                for word in words:
                    msgs['adding_to_trie'](word)
                    t.insert(word)
            elif cmd == 'a':
                for letter in alphabet():
                    print('{}: {}'.format(letter, t.get_suggestions(letter)))
                msgs['suggestions_by_alphabet']()

            elif cmd == 'clr':
                candidate = ''
                msgs['candidate_reset']()
            elif cmd == 'cur':
                msgs['current_candidate'](candidate)
            elif cmd == 'trie':
                msgs['display_trie'](t)
            elif cmd == 'sub' or cmd == 's':
                msgs['adding_to_trie'](candidate)
                t.insert(candidate)
                candidate = ''

        elif cmd.endswith('*'):
            suggestions = t.get_suggestions(cmd[:-1])
            msgs['suggestions'](suggestions)
        else:
            if cmd.count(' ') > 0:
                for word in get_words_only(cmd):
                    msgs['adding_to_trie'](word)
                    t.insert(word)
            elif cmd.endswith('.'):
                direct = cmd[:-1]
                msgs['adding_to_trie'](direct)
                t.insert(direct)
            else:
                msgs['appending_to_candidate'](candidate, cmd)
                candidate += cmd

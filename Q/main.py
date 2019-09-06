import json
import random

QSHOW = """
{}

{}
"""


class Question:
    """
    Represents a multiple choice question with a single answer.
    """
    choice_delim = ') '
    choice_indent = 4

    def __init__(self, id, text, choices, answer):
        """
        :param text: The text of the question.
        :param choices: A list of pairs, where each pair is a (char, text).
        :param answer: Char appearing in choices that is considered the right answer.
        """
        self.id = id
        self.text = text
        self.choices = choices
        self.answer = answer.strip()

    @property
    def display(self):
        parts = []
        for c, text in self.choices:
            parts.append('{}{}{}{}'.format(' ' * self.choice_indent, c, self.choice_delim, text))
        choice_text = '\n'.join(parts)
        t = '\n{}\n{}'.format(self.text, choice_text)
        return t

    def check(self, answer):
        return self.answer.lower() == answer.strip().lower()


class QuestionPool:
    """
    A pool of questions
    """

    def __init__(self, path, encoding='utf-8'):
        pool = {}
        with open(path, encoding=encoding) as file:
            data = json.load(file)
            for id, qdata in data.items():
                pool[id] = Question(**qdata)
        self._pool = pool

    def draw(self, n):
        """
        return a list of randomly chosen n questions:
        """
        if n >= len(self._pool):
            ql = list(self._pool.values())
        else:
            ql = random.sample(list(self._pool.values()), n)
        return ql


class Player:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def run(self, qlist):
        pass


PROMPT_NPLAYERS = 'Unesi broj igrača: '

PROMPT_NQUESTIONS = 'Unesi broj pitanja: '


class Quiz:

    def __init__(self, qpath):
        self.qpool = QuestionPool(qpath)
        self.players = None
        self.questions = None

    def start(self):
        # make players for current game
        n_players = int(input(PROMPT_NPLAYERS).strip())
        players = []
        for i in range(n_players):
            id = i + 1
            p = Player(id, input('player {} name: '.format(id).strip()))
            players.append(p)
        self.players = players

        # make questions for current game
        n_questions = int(input(PROMPT_NQUESTIONS).strip())
        self.questions = self.qpool.draw(n_questions)

    def run(self):
        for p in self.players:
            p.run(self.questions)

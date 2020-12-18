from django.core.management.base import BaseCommand
import os
from api.models import GuessText
from tqdm import tqdm

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error(f"The file {arg} does not exist!")
    else:
        return open(arg, 'r', encoding="ISO-8859-1")

def readDict(file, min_word_length):
    for word in tqdm(file.readlines()):
        word_len = len(word)
        if word_len >= min_word_length:
            yield { 'text': word, 'length': word_len }

class Command(BaseCommand):
    help = 'Imports german dictionary in the database'

    def add_arguments(self, parser):
        parser.add_argument('--min-word-length', nargs="?", type=int, default=10)
        parser.add_argument(
            '--dict-file',
            nargs="?",
            type=lambda x: is_valid_file(parser, x),
            default="german.dic",
            metavar="FILE"
        )

    def handle(self, *args, **options):
        file = options['dict_file']
        min_word_length = options['min_word_length']
        for word in readDict(file, min_word_length):
            GuessText.objects.create(**word)

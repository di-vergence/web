from django.core.management.base import BaseCommand
import csv
from newapl.models import Profile, Question, Answer,Tag
from django.contrib.auth.models import User
from optparse import make_option

from faker.frandom import random
from faker.lorem import sentence, sentences, words
from mixer.fakers import get_username, get_email
from pprint import pformat
from mixer import fakers as f
from mixer import generators as g

from django.db.models  import Min,Max
class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--users',
            action='store',
            dest='users',
            default=0,
        ),
        make_option('--questions',
            action='store',
            dest='questions',
            default=0,
        ),
        make_option('--answers',
            action='store',
            dest='answers',
            default=0,
        ),
        make_option('--t_q',
            action='store',
            dest='t_q',
            default=0,
        ),

    ) 

    def handle(self, *args, **options):
        names = {}
        p = csv.writer(open("CSV/p.csv", "wb"))
        u = csv.writer(open("CSV/u.csv", "wb"))
        q = csv.writer(open("CSV/q.csv", "wb"))
        t = csv.writer(open("CSV/t.csv", "wb"))
        a = csv.writer(open("CSV/a.csv", "wb"))
        tag_questions = csv.writer(open("CSV/t_q.csv", "wb"))
        text_tag = words(100)
        p_min = 1
        p_max = 10001
        q_max = 100000

        while (len(names.keys())<int(options['users'])):
            names[get_username(length=30)]=1

        for i,name in enumerate(names.keys()):
            datetime = next(g.gen_datetime())
            password = next(g.gen_string())
            u.writerow([name, datetime, password, get_email(), datetime])
            p.writerow([i + 1,i + 1, random.randint(0,20), "https://ssl.webpack.de/lorempixel.com/120/120/"])
        
        for i in range(1, int(options['t_q'])):
            numb_of_tags = random.randint(0,3)
            for j in range(0, numb_of_tags):
                tag_questions.writerow([i , random.randint(1,100)])

        for i in range(0, int(options['questions'])):
            title = words(1)
            text = sentences(3)
            date_added = next(g.gen_datetime())
            q.writerow([i+1,random.randint(p_min,p_max), title.pop(0),sentences(3), date_added, ])

        for i in text_tag:
            t.writerow([i])

        for i in range(0, int(options['answers'])):
            date_added = next(g.gen_datetime())
            a.writerow([i+1,sentences(3), date_added, random.randint(0,1), random.randint(p_min,p_max), random.randint(1, q_max)])
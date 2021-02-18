from django.contrib.auth.models import User
from django.core.management.base import BaseCommand, CommandError
from test_app.models import Member

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help="Username of the user")
        parser.add_argument('password', type=str, help="Password of the user")
        parser.add_argument('gender', type=str, help="Gender of the user")
        parser.add_argument('country', type=str, help="Country of the user")

    def handle(self, *args, **kwargs):

        username = kwargs['username']
        password = kwargs['password']
        gender = kwargs['gender']
        country = kwargs['country']
        user = User.objects.create_user(username, password)
        member = Member()
        member.user = user
        member.gender = gender
        member.country = country
        member.save()
        self.stdout.write("Member created")




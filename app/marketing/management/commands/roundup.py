from django.core.management.base import BaseCommand
from marketing.mail import *
from django.conf import settings
from dashboard.models import Bounty


class Command(BaseCommand):

    help = 'sends a test email'

    def handle(self, *args, **options):
        days_back = 90

        email_list = []
        for b in Bounty.objects.filter(web3_created__gt=timezone.now()-timezone.timedelta(days=days_back)).all():
            if b.bounty_owner_email:
                email_list.append(b.bounty_owner_email)
            if b.claimee_email:
                email_list.append(b.claimee_email)
        email_list = set(email_list)

        #TODO: formalize the list management into its own database table, completely with ability to manage subscriptions
        
        for to_email in email_list:
            weekly_roundup([to_email])
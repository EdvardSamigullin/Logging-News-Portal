import  datetime
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from .models import *

@shared_task
def send_mails():
  today = datetime.datetime.now()
  last_week = today - datetime.timedelta(days=7)
  posts = Post.objects.filter(time_of_posting__gte=last_week)
  categories = set(posts.values_list('category__category_name', flat=True))
  subscribers = set(Category.objects.filter(category_name__in=categories).values_list('subscribers__email', flat=True))

  html_content = render_to_string(
    'daily_post.html',
    {
      'link': settings.SITE_URL,
      'posts': posts,
    }
  )

  msg = EmailMultiAlternatives(
    subject='Статьи за неделю',
    body='',
    from_email=settings.DEFAULT_FROM_EMAIL,
    to=subscribers,
  )

  msg.attach_alternative(html_content, 'text/html')
  msg.send()

@shared_task
def new_post_message(pk):
  post = Post.objects.get(id=pk)
  subscribers_emails = []
  categories = post.category.all()
  for cat in categories:
    subscribers = cat.subscribers.all()
    subscribers_emails += [s.email for s in subscribers]
    html_content = render_to_string(
      'post_created_email.html',
      {
        'text': post.preview(),
        'link': f'{settings.SITE_URL}/news/{pk}'
      }
    )

    msg = EmailMultiAlternatives(
      subject=post.title,
      body='',
      from_email=settings.DEFAULT_FROM_EMAIL,
      to=subscribers_emails,
    )

    msg.attach_alternative(html_content, 'text/html')
    msg.send()



#celery -A NewsPaper worker -l INFO --pool=solo
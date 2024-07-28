from django.contrib.auth.models import User
from blog.models import Post
from datetime import date
from django.db.models import Q

# getting the admin user
user = User.objects.get(username='admin')

# creating a new post with the admin user
post = Post(title='Another post',
            slug='another-post',
            body='Post body.',
            author=user)
post.save()

# using the get_or_create method to create a new user
user, created = User.objects.get_or_create(username='user2')

# updating the post object title
post.title = 'New title'
post.save()

# retrieving objects
all_posts = Post.objects.all()
all_posts

# filtering objects
admin=Post.objects.filter(username='admin')
print(admin)

# filtering using field lookups
post = Post.objects.filter(id__exact=1)
print(post)

# it is also equivalent to this below
post = Post.objects.filter(id=1)
post.save()

# case sensitive filtering can be done like this
post = Post.objects.filter(title__iexact='first post')
print(post)
# we also have other ways of filtering lik
post = Post.objects.filter(title__contains='Django')
print(post)
post = Post.objects.filter(title__icontains='django')
print(post)

# You can check for a given iterable (often a list, tuple, or another
# QuerySet object) with the in lookup. The following example
# retrieves posts with an id that is 1 or 3 :
post = Post.objects.filter(id__in=[1, 3])
print(post)

# greater than, greater than equal to, less than nad less than equal to
post = Post.objects.filter(id__gt=3)
print(post)
post = Post.objects.filter(id__gte=3)
print(post)
post = Post.objects.filter(id__lt=3)
print(post)
post = Post.objects.filter(id__lte=3)
print(post)

# A case-sensitive/insensitive starts-with lookup can be performed
# with the startswith and istartswith lookup types, respectively:
post = Post.objects.filter(title__istartswith='who')
print(post)

# A case-sensitive/insensitive ends-with lookup can be performed
# with the endswith and iendswith lookup types, respectively:
post = Post.objects.filter(title__iendswith='reinhardt?')
print(post)

# filtering dates
post = Post.objects.filter(publish__date=date(2024, 1, 31))
post = Post.objects.filter(publish__year=2024)
post = Post.objects.filter(publish__month=1)
post = Post.objects.filter(publish__day=1)

# chaining lookups
post = Post.objects.filter(publish__date__gt=date(2024, 1, 1))
post = Post.objects.filter(author__username='admin')
post = Post.objects.filter(author__username__starstwith='ad')

# chaining filters
post = Post.objects.filter(author__username__starstwith='ad').filter(authot__username='admin')

# excluding objects
post = Post.objects.filter(author__username__starstwith='ad').exclude(title__startswith='why')

# ordering objects
post = Post.objects.order_by('title') # ascending order
post = Post.objects.order_by('-title') # descending order

# ordering by multiple fields
post = Post.objects.order_by('author', 'title')

# limiting querysets
post = Post.objects.all()[:5] # limiting the query to return just 5 objects
post = Post.objects.all()[3:6] # this returns the 4th to 6th objects from the post table

# counting objects
post = Post.objects.filter(id_lt=3).count() # returns the total number of posts with id less than 3

# checking if an object exists
post = Post.objects.filter(id=1).exists()

# deleting objects
post.delete()

# complex lookups with Q objects
starts_who = Q(title_istartswith='who')
starts_why = Q(title_istartswith='why')

post = Post.objects.filter(starts_who | starts_why) # the following code retrieves posts with a title that starts with the string who or why (case-insensitive):






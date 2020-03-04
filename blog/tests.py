from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Posts

class BlogTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a Posts """
        #Author is a required field in our model
        #Creating a user for this test and saving it to the test database
        user = User()
        user.save()

        #Creating and saving a new post to the test database
        post = Posts(title='My test Post', content='test', author=user)
        post.save()

        #Making sure the slug that was generated in Posts.save()
        #matches what we think it should be
        self.assertEqual(post.slug, 'my-test-post')

class PostsListViewTest(TestCase):
    def test_multiple_pages(self):
        #Making some test data to be displayed on the post
        user = User.objects.create()

        Posts.objects.create(title='My test Post', content='test', author=user)
        Posts.objects.create(title='Another test Post', content='test', author=user)

        #Issues a GET request to the HappyMe homepage
        #When we make a request, we get a response back
        response = self.client.get('/')

        #Checking that the response is 200 OK
        self.assertEqual(response.status_code, 200)

        #Checking that the number of posts passed to the template
        #matches the number of pages we have in the database
        responses = response.context['pages']
        self.assertEqual(len(responses), 2)

        self.assertQuerysetEqual(
            responses,
            ['<Posts: My test Post>', '<Posts: Another test Post>'],
            ordered=False
        )
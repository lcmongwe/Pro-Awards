from django.test import TestCase
from .models import Post,Review,Profile


# Create your tests here.
class PostTest(TestCase):
    '''
    test class for Post model
    '''
    def setUp(self):
       
        self.new_post = Post(img_name='blog')
        self.new_post.save_post()
        self.new_review =   Review(design='7')
        self.new_review.save_review()
        self.new_post = Post(  image='images/blog.jpg',img_name='blog',img_description='this is a blog' )
        self.new_post.save_post()
        self.post2 =Post(  image='images/gallery.jpg',img_name='gallery',img_description='this is a gallery' )
        self.post2.save_post()
    def tearDown(self):
     
        Post.objects.all().delete()
        Review.objects.all().delete()
        Post.objects.all().delete()
    def test_save_post(self):
        '''
        test method to ensure an post instance has been correctly saved
        '''
        self.assertTrue(len(Post.objects.all()) == 2)
    def test_instances(self):
        '''
         method to test instances created successfully during setUp
        '''
        self.assertTrue(isinstance(self.new_post,Post))
        self.assertTrue(isinstance(self.new_review, Review))
        

    def test_delete_post(self):
        '''
        test method to ensure an post is deleted correctly deleted
        '''
        self.new_post.delete_post()
        self.assertTrue(len(Post.objects.all()) == 1)




class ProfileTest(TestCase):
    '''
    test class for profile model
    '''
    def setUp(self):
  
        self.new_profile =  Profile(name='lucy',phone='123',email='lucy@gmail.com',bio='my name is lucy')
        self.new_profile.save_profile()

    def tearDown(self):
        '''
        test method to delete Category instance
        '''
        Profile.objects.all().delete()

    def test_save_profile(self):
        '''
        test for profile instance has been correctly saved
        '''
        self.assertTrue(len(Profile.objects.all()) == 1)

    def test_delete_profile(self):
        '''
        test a Category instance has been correctly deleted
        '''
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        self.assertTrue(len(Profile.objects.all()) == 0)



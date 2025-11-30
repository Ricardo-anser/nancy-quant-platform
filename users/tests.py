from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UsersTestCase(TestCase):
    def setUp(self):
        # 创建测试用户
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com'
        )
        
        # 创建用户资料
        self.user_profile = UserProfile.objects.create(
            user=self.user,
            phone='12345678901',
            bio='This is a test user profile'
        )

    def test_user_creation(self):
        """测试用户创建"""
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))
        
    def test_user_profile_creation(self):
        """测试用户资料创建"""
        self.assertEqual(self.user_profile.user, self.user)
        self.assertEqual(self.user_profile.phone, '12345678901')
        self.assertEqual(self.user_profile.bio, 'This is a test user profile')
        
    def test_user_profile_str(self):
        """测试用户资料字符串表示"""
        self.assertEqual(str(self.user_profile), "testuser's Profile")
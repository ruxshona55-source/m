# from django.test import TestCase
# from  .serializers import UserCreateSerializers
# # data={'username':"Ali",'email':"mmm@gmail.com",'first_name':"mmmm",'last_name':"nnnn",'password':32322,'re_password':32322}
#
# # 2 xollatda testlash togri va xato xolat bo'yicha
# class UserCreateSerializersTest(TestCase):
#     def test_user_create(self):
#         data={"username":"Ali",
#               "email":"mmm@gmail.com",
#               "first_name":"mmmm",
#               "last_name":"mmm",
#               "password":"32322",
#               "re_password":"32322"
#         }
#         serializer=UserCreateSerializers(data=data)
#         self.assertTrue(serializer.is_valid())
#         user = serializer.save()
#         self.assertEqual(user.email, data["email"])
#         self.assertTrue(user.check_password(data["password"]))
#
#         self.assertTrue(serializer.is_valid())
#         self.assertIn(data["email"], serializer.errors)
#
#
#
#
#
#
#
#

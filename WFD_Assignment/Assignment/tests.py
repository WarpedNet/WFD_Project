from django.test import TestCase, Client
from .models import *

# Create your tests here.
class FormTests(TestCase):
    def setUp(self):
        self.client = Client()
        user = UserModel(
                username = "test",
                first_name = "test",
                last_name = "test",
                email = "test@test.com",
                address = "test",
                billingAddress = "test",
                accType = "customer"
        )
        user.set_password("test")
        user.save()
        self.user = user

    def test_login_form(self):
        response = self.client.post('/login', {"username":self.user.username, "password":self.user.password})
        self.assertEqual(response.status_code, 200)
    
    def test_register_form(self):
        response = self.client.post('/register', {"userType":"customer"})
        self.assertRedirects(response, "/register_customer")
    
    def test_register_customer_form(self):
        response = self.client.post('/register_customer', {
            "username":"test2",
            "password":"test",
            "firstName":"test",
            "surname":"test",
            "email":"test@test.com",
            "address":"test",
            "billingAddress":"test",
            "dob":"12/04/23",
            "phoneNum":"test"
        })
        self.assertRedirects(response, "/login")
        newUser = UserModel.objects.get(username = "test2")
        self.assertIsNotNone(newUser)
    
    def test_account_update_form(self):
        user = UserModel(
                username = "test3",
                first_name = "test3",
                last_name = "test3",
                email = "test3@test.com",
                address = "test3",
                billingAddress = "test3",
                accType = "customer"
        )
        user.set_password("test")
        user.save()
        customer = Customer(user = user, dob = "11/02/23", phoneNum = "test")
        customer.save()

        self.client.force_login(user)
        response = self.client.post('/account', {
            "username":"test4",
            "firstName":"test4",
            "surname":"test4",
            "email":"test4@test.com",
            "address":"test",
            "billingAddress":"test",
            "password":"test",
            "dob":"12/02/23",
            "phoneNum":"test4",
        })
        updatedUser = UserModel.objects.get(pk = user.pk)
        self.assertEqual(updatedUser.username, "test4")
    
    def test_sell_insurance(self):
        user = UserModel(
                username = "test5",
                first_name = "test5",
                last_name = "test5",
                email = "test5@test.com",
                address = "test5",
                billingAddress = "test5",
                accType = "insurance_provider"
        )
        user.set_password("test")
        user.save()
        insuranceProvider = Insurance_Provider(
            user = user,
            phoneNum = "test5"
        )
        insuranceProvider.save()
        self.client.force_login(user)
        self.client.post('/sell_insurance', {
            "title":"test5",
            "coverage":"test5",
            "details":"test5",
            "cost":500
        })
        
        newInsurance = Insurance.objects.get(title="test5")
        self.assertIsNotNone(newInsurance)
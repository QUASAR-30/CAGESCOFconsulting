from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer, Invoice, Article, Document


class ModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_customer_creation(self):
        customer = Customer.objects.create(
            name='John Doe',
            email='john@example.com',
            phone='123456789',
            address='123 Main Street',
            sex='M',
            age='35',
            city='New York',
            zip_code='10001',
            save_by=self.user
        )
        self.assertEqual(customer.name, 'John Doe')
        self.assertEqual(customer.email, 'john@example.com')

    def test_invoice_creation(self):
        customer = Customer.objects.create(
            name='Jane Smith',
            email='jane@example.com',
            phone='987654321',
            address='456 Oak Avenue',
            sex='F',
            age='28',
            city='Los Angeles',
            zip_code='90001',
            save_by=self.user
        )
        invoice = Invoice.objects.create(
            customer=customer,
            save_by=self.user,
            total=1000.00,
            paid=False,
            invoice_type='R'
        )
        self.assertEqual(invoice.customer, customer)
        self.assertEqual(invoice.total, 1000.00)

    def test_article_creation(self):
        customer = Customer.objects.create(
            name='Alice Johnson',
            email='alice@example.com',
            phone='555555555',
            address='789 Pine Street',
            sex='F',
            age='40',
            city='Chicago',
            zip_code='60601',
            save_by=self.user
        )
        invoice = Invoice.objects.create(
            customer=customer,
            save_by=self.user,
            total=500.00,
            paid=True,
            invoice_type='I'
        )
        article = Article.objects.create(
            invoice=invoice,
            name='Consulting Service',
            quantity=5,
            unit_price=100.00,
            total=500.00
        )
        self.assertEqual(article.invoice, invoice)
        self.assertEqual(article.total, 500.00)

    def test_document_creation(self):
        customer = Customer.objects.create(
            name='Bob Brown',
            email='bob@example.com',
            phone='444444444',
            address='321 Elm Street',
            sex='M',
            age='45',
            city='Houston',
            zip_code='77001',
            save_by=self.user
        )
        document = Document.objects.create(
            customer=customer,
            save_by=self.user,
            document_type='C',
            file='path/to/document.pdf'
        )
        self.assertEqual(document.customer, customer)
        self.assertEqual(document.document_type, 'C')

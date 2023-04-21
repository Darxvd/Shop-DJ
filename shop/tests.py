from django.test import TestCase
from shop.models import Category, Product

# Create your tests here.
class CategoryModelTest(TestCase):
    def setUp(self):
        Category.objects.create(name='Test Category')
        Product.objects.create(name='Test Product', description='Test Description', price=100, category = Category.objects.get(name='Test Category'))
        Product.objects.create(name='Test Product 2', description='Test Description 2', price=200, category = Category.objects.get(name='Test Category'))

    def test_product_category_id(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.category.id, 1)

    def test_object_name_is_name(self):
        category = Category.objects.get(id=1)
        excepted_object_name = f'Categoria {category.name}'
        self.assertEquals(excepted_object_name, str(category))

    def test_total_products(self):
        category = Category.objects.get(id=1)
        self.assertEqual(category.products.count(), 2)

class ProductModelItems(TestCase):
    def setUp(self):
        category = Category.objects.create(name='Pantalones')
        Product.objects.create(name='Pantalon 1', description='Panatalon 1', price=100, category=category)
        Product.objects.create(name='Pantalon 2', description='Panatalon 2', price=200, category=category)
        Product.objects.create(name='Pantalon 3', description='Panatalon 3', price=300, category=category)

    def test_products_list_view_200(self):
        response = self.client.get('/')
        self.assertDictEqual(response.status_code, 200)

    def test_product_list_view_queryset(self):
        response = self.client.get('/')
        self.assertEqual(len(response.context['object_list']), 3)

    def test_product_list_view_title(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Prodductos</h1>')


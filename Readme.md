1. Initialize the project
2. Initialize Store App
3. Add store app reference in the setting.py of main project
4. Create template files for store app
5. Create views - Store, Cart, Checkout
6. Create the urls in urls.py file of Store app
7. Include store urls in the main project urls.py 
8. Create a static folder outside main project and Store app
9. Create two folder for css and images in static directory
10. Add static folder reference in settings.py within STATICFILES_DIRS list
11. Then add main.css in the main.html file of store app
12. Design html files for frontend of store app
13. Create database models:
- Customer
- Product
- Order
- OrderItem
- ShippingModel
14. Database migration
15. Register models
16. Create a super user
17. Add 6 dummy products from admin panel
18. Fetch products dynamically from database using store function in views.py
19. Creating for loop in store.html render products
20. For showing images of products
- Install pillow
- Create imagefield in Prodcut model
- Migrate database
- Make MEDIA_DIR as static/images/products
- Make MEDIA_URL
- Modify urlpatterns in urls.py of main project
- Creating a function in product model to return image url
21. For creating user cart
- Create dummy user from admin panel
- Create dummy order and orderitems from admin panel
- Fetch orders dynamically from database using cart function in views.py
- Creating for loop in cart.html render orders
1. Initialized the project
2. Initialized Store App
3. Added store app reference in the setting.py of main project
4. Created template files for store app
5. Created views - Store, Cart, Checkout
6. Created the urls in urls.py file of Store app
7. Include store urls in the main project urls.py 
8. Created a static folder outside main project and Store app
9. Created two folder for css and images in static directory
10. Added static folder reference in settings.py within STATICFILES_DIRS list
11. Then added main.css in the main.html file of store app
12. Designed html files for frontend of store app
13. Created database models:
- Customer
- Product
- Order
- OrderItem
- ShippingModel
14. Database migrated
15. Registered models
16. Created a super user
17. Added 6 dummy products from admin panel
18. Dynamically products fetched from database
19. For showing images of products
- Install pillow
- Create imagefield in Prodcut model
- Migrate database
- Make MEDIA_DIR as static/images/products
- Make MEDIA_URL
- Modify urlpatterns in urls.py of main project
- Creating a function in product model to return image url
import os
import django

# Set up Django's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

from django.db import transaction
from shop.models import Category, Product

@transaction.atomic
def seed_data():
    products = [
            {
                'name': 'Samsung Galaxy S21',
                'description': 'High-end Samsung smartphone with a stunning display.',
                'price': 799.99,
                'stock': 50,
                'category': 'Smartphones'
            },
            {
                'name': 'iPhone 13 Pro',
                'description': 'Latest iPhone with a powerful A15 Bionic chip.',
                'price': 999.99,
                'stock': 40,
                'category': 'Smartphones'
            },
            {
                'name': 'Dell XPS 15',
                'description': 'Premium Dell laptop with a sleek design and powerful performance.',
                'price': 1299.99,
                'stock': 20,
                'category': 'Laptops'
            },
            {
                'name': 'MacBook Air M1',
                'description': 'Apple MacBook with the M1 chip for blazing-fast performance.',
                'price': 1099.99,
                'stock': 30,
                'category': 'Laptops'
            },
            {
                'name': 'Men\'s Casual T-Shirt',
                'description': 'Comfortable and stylish t-shirt for daily wear.',
                'price': 29.99,
                'stock': 50,
                'category': 'Tops'
            },
            {
                'name': 'Women\'s Blouse',
                'description': 'Elegant blouse suitable for formal occasions.',
                'price': 49.99,
                'stock': 30,
                'category': 'Tops'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Bose QuietComfort 35 II',
                'description': 'Comfortable headphones with world-class noise cancellation.',
                'price': 299.99,
                'stock': 25,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 4K UHD TV',
                'description': 'High-quality 4K Ultra HD TV with a large screen for immersive viewing.',
                'price': 799.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Instant Pot Duo 6-Quart',
                'description': 'Multi-functional electric pressure cooker for quick and easy cooking.',
                'price': 89.99,
                'stock': 40,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Nikon D750 DSLR Camera',
                'description': 'High-performance DSLR camera for photography enthusiasts.',
                'price': 1499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundLink Revolve+',
                'description': 'Portable Bluetooth speaker with 360-degree sound.',
                'price': 199.99,
                'stock': 20,
                'category': 'Speakers'
            },
            {
                'name': 'Fitbit Charge 4',
                'description': 'Fitness tracker with built-in GPS and heart rate monitoring.',
                'price': 149.99,
                'stock': 35,
                'category': 'Wearables'
            },
            {
                'name': 'LG 27-inch 4K Monitor',
                'description': 'Ultra HD monitor with vivid colors for productivity and entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Nike Air Zoom Pegasus 38',
                'description': 'Running shoes with responsive cushioning for comfort and support.',
                'price': 109.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Stainless Steel Cookware Set',
                'description': 'Premium cookware set for versatile cooking at home.',
                'price': 299.99,
                'stock': 10,
                'category': 'Cookware & Bakeware'
            },
            {
                'name': 'Amazon Echo Dot (4th Gen)',
                'description': 'Smart speaker with Alexa for voice control and music playback.',
                'price': 49.99,
                'stock': 40,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Sony PlayStation 5',
                'description': 'Next-gen gaming console with high-quality graphics and gameplay.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 32-inch LED TV',
                'description': 'HD LED TV for compact spaces and sharp visuals.',
                'price': 249.99,
                'stock': 20,
                'category': 'Televisions'
            },
            {
                'name': 'Keurig K-Elite Coffee Maker',
                'description': 'Single-serve coffee maker with strong brew capability.',
                'price': 129.99,
                'stock': 30,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon EOS Rebel T7i DSLR Camera',
                'description': 'Entry-level DSLR camera with a versatile lens for beginners.',
                'price': 799.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Versa 3',
                'description': 'Advanced fitness tracker with built-in GPS and sleep tracking.',
                'price': 199.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'LG 55-inch OLED TV',
                'description': 'Ultra-thin OLED TV with perfect black levels for cinematic viewing.',
                'price': 1499.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'Nike Air Max 270',
                'description': 'Casual sneakers with visible Air Max cushioning for all-day comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Sneakers'
            },
            {
                'name': 'Crock-Pot 6-Quart Slow Cooker',
                'description': 'Programmable slow cooker for easy and delicious meals.',
                'price': 49.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple iPad Pro (12.9-inch)',
                'description': 'Powerful iPad with a large display, ideal for productivity and creativity.',
                'price': 999.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub',
                'description': 'Smart display with Google Assistant for hands-free control and information.',
                'price': 129.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Sony PlayStation 5',
                'description': 'Next-gen gaming console with high-quality graphics and gameplay.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 43-inch 4K TV',
                'description': '4K UHD TV with HDR for stunning picture quality.',
                'price': 399.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'Ninja Foodi Pressure Cooker',
                'description': 'Multi-purpose pressure cooker with air frying capabilities.',
                'price': 249.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Canon EOS 5D Mark IV DSLR Camera',
                'description': 'High-quality DSLR camera with excellent low-light performance.',
                'price': 2499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Studio3 Wireless Headphones',
                'description': 'Wireless headphones with premium sound quality and noise cancellation.',
                'price': 299.99,
                'stock': 20,
                'category': 'Headphones'
            },
            {
                'name': 'LG 65-inch OLED TV',
                'description': 'OLED TV with stunning color accuracy and deep blacks.',
                'price': 1999.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Nike Air Force 1',
                'description': 'Classic sneakers known for their style and comfort.',
                'price': 89.99,
                'stock': 30,
                'category': 'Sneakers'
            },
            {
                'name': 'Instant Pot Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small meals and snacks.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Mini (5th Gen)',
                'description': 'Compact iPad with a retina display for on-the-go productivity.',
                'price': 399.99,
                'stock': 15,
                'category': 'Tablets'
            },
            {
                'name': 'Bose QuietComfort Earbuds',
                'description': 'True wireless earbuds with noise cancellation and clear sound.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Inspire 2',
                'description': 'Affordable fitness tracker with 24/7 heart rate tracking.',
                'price': 99.99,
                'stock': 30,
                'category': 'Wearables'
            },
            {
                'name': 'HP 27-inch 4K Monitor',
                'description': '4K Ultra HD monitor for vibrant colors and productivity.',
                'price': 349.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Asics Gel-Nimbus 23 Running Shoes',
                'description': 'Premium running shoes with gel cushioning for long-distance comfort.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Blender',
                'description': 'High-performance blender for smoothies and more.',
                'price': 129.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
            {
                'name': 'Instant Pot Duo Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small households.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Pro 11-inch (3rd Gen)',
                'description': 'Compact and powerful iPad for creative professionals.',
                'price': 799.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sennheiser HD 660 S Headphones',
                'description': 'High-quality open-back headphones for audiophiles.',
                'price': 499.99,
                'stock': 10,
                'category': 'Headphones'
            },
            {
                'name': 'LG 43-inch 4K TV',
                'description': 'Affordable 4K UHD TV with a large screen for entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Nespresso Vertuo Coffee and Espresso Maker',
                'description': 'Coffee and espresso maker with convenient pod system.',
                'price': 179.99,
                'stock': 15,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Sony Alpha a6400 Mirrorless Camera',
                'description': 'Mirrorless camera with fast autofocus and 4K video recording.',
                'price': 899.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Apple AirPods Pro',
                'description': 'Premium noise-canceling wireless earbuds with spatial audio.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Luxe',
                'description': 'Elegant fitness tracker with a slim design and vibrant AMOLED display.',
                'price': 149.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Samsung 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and productivity.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Hoka One One Clifton 8 Running Shoes',
                'description': 'Cushioned running shoes for a plush and smooth ride.',
                'price': 139.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Vitamix E310 Explorian Blender',
                'description': 'High-performance blender for blending, pureeing, and more.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Audio',
                'description': 'Smart speaker with powerful sound for music and podcasts.',
                'price': 99.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Pro Controller',
                'description': 'High-quality controller for Nintendo Switch gaming.',
                'price': 69.99,
                'stock': 15,
                'category': 'Gaming Accessories'
            },
            {
                'name': 'Sony 85-inch 4K TV',
                'description': 'Massive 4K UHD TV for home theater enthusiasts.',
                'price': 2499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Smart Oven Air Fryer',
                'description': 'Multi-functional countertop oven with air frying capabilities.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'DJI Mavic Air 2 Drone',
                'description': 'Compact drone with 4K camera and intelligent flight modes.',
                'price': 799.99,
                'stock': 10,
                'category': 'Electronics'
            },
            {
                'name': 'Bose QuietComfort 45 Headphones',
                'description': 'Premium noise-canceling headphones with plush ear cushions.',
                'price': 349.99,
                'stock': 15,
                'category': 'Headphones'
            },
            {
                'name': 'LG 75-inch NanoCell 4K TV',
                'description': 'NanoCell TV with vibrant colors and wide viewing angles.',
                'price': 1799.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub',
                'description': 'Smart display with Google Assistant for hands-free control and information.',
                'price': 129.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Sony PlayStation 5',
                'description': 'Next-gen gaming console with high-quality graphics and gameplay.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 43-inch 4K TV',
                'description': '4K UHD TV with HDR for stunning picture quality.',
                'price': 399.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'Ninja Foodi Pressure Cooker',
                'description': 'Multi-purpose pressure cooker with air frying capabilities.',
                'price': 249.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Canon EOS 5D Mark IV DSLR Camera',
                'description': 'High-quality DSLR camera with excellent low-light performance.',
                'price': 2499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Studio3 Wireless Headphones',
                'description': 'Wireless headphones with premium sound quality and noise cancellation.',
                'price': 299.99,
                'stock': 20,
                'category': 'Headphones'
            },
            {
                'name': 'LG 65-inch OLED TV',
                'description': 'OLED TV with stunning color accuracy and deep blacks.',
                'price': 1999.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Nike Air Force 1',
                'description': 'Classic sneakers known for their style and comfort.',
                'price': 89.99,
                'stock': 30,
                'category': 'Sneakers'
            },
            {
                'name': 'Instant Pot Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small meals and snacks.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Mini (5th Gen)',
                'description': 'Compact iPad with a retina display for on-the-go productivity.',
                'price': 399.99,
                'stock': 15,
                'category': 'Tablets'
            },
            {
                'name': 'Bose QuietComfort Earbuds',
                'description': 'True wireless earbuds with noise cancellation and clear sound.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Inspire 2',
                'description': 'Affordable fitness tracker with 24/7 heart rate tracking.',
                'price': 99.99,
                'stock': 30,
                'category': 'Wearables'
            },
            {
                'name': 'HP 27-inch 4K Monitor',
                'description': '4K Ultra HD monitor for vibrant colors and productivity.',
                'price': 349.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Asics Gel-Nimbus 23 Running Shoes',
                'description': 'Premium running shoes with gel cushioning for long-distance comfort.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Blender',
                'description': 'High-performance blender for smoothies and more.',
                'price': 129.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
            {
                'name': 'Instant Pot Duo Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small households.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Pro 11-inch (3rd Gen)',
                'description': 'Compact and powerful iPad for creative professionals.',
                'price': 799.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sennheiser HD 660 S Headphones',
                'description': 'High-quality open-back headphones for audiophiles.',
                'price': 499.99,
                'stock': 10,
                'category': 'Headphones'
            },
            {
                'name': 'LG 43-inch 4K TV',
                'description': 'Affordable 4K UHD TV with a large screen for entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Nespresso Vertuo Coffee and Espresso Maker',
                'description': 'Coffee and espresso maker with convenient pod system.',
                'price': 179.99,
                'stock': 15,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Sony Alpha a6400 Mirrorless Camera',
                'description': 'Mirrorless camera with fast autofocus and 4K video recording.',
                'price': 899.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Apple AirPods Pro',
                'description': 'Premium noise-canceling wireless earbuds with spatial audio.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Luxe',
                'description': 'Elegant fitness tracker with a slim design and vibrant AMOLED display.',
                'price': 149.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Samsung 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and productivity.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Hoka One One Clifton 8 Running Shoes',
                'description': 'Cushioned running shoes for a plush and smooth ride.',
                'price': 139.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Vitamix E310 Explorian Blender',
                'description': 'High-performance blender for blending, pureeing, and more.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Audio',
                'description': 'Smart speaker with powerful sound for music and podcasts.',
                'price': 99.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Pro Controller',
                'description': 'High-quality controller for Nintendo Switch gaming.',
                'price': 69.99,
                'stock': 15,
                'category': 'Gaming Accessories'
            },
            {
                'name': 'Sony 85-inch 4K TV',
                'description': 'Massive 4K UHD TV for home theater enthusiasts.',
                'price': 2499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Smart Oven Air Fryer',
                'description': 'Multi-functional countertop oven with air frying capabilities.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'DJI Mavic Air 2 Drone',
                'description': 'Compact drone with 4K camera and intelligent flight modes.',
                'price': 799.99,
                'stock': 10,
                'category': 'Electronics'
            },
            {
                'name': 'Bose QuietComfort 45 Headphones',
                'description': 'Premium noise-canceling headphones with plush ear cushions.',
                'price': 349.99,
                'stock': 15,
                'category': 'Headphones'
            },
            {
                'name': 'LG 75-inch NanoCell 4K TV',
                'description': 'NanoCell TV with vibrant colors and wide viewing angles.',
                'price': 1799.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
            {
                'name': 'Instant Pot Duo Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small households.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Pro 11-inch (3rd Gen)',
                'description': 'Compact and powerful iPad for creative professionals.',
                'price': 799.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sennheiser HD 660 S Headphones',
                'description': 'High-quality open-back headphones for audiophiles.',
                'price': 499.99,
                'stock': 10,
                'category': 'Headphones'
            },
            {
                'name': 'LG 43-inch 4K TV',
                'description': 'Affordable 4K UHD TV with a large screen for entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Nespresso Vertuo Coffee and Espresso Maker',
                'description': 'Coffee and espresso maker with convenient pod system.',
                'price': 179.99,
                'stock': 15,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Sony Alpha a6400 Mirrorless Camera',
                'description': 'Mirrorless camera with fast autofocus and 4K video recording.',
                'price': 899.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Apple AirPods Pro',
                'description': 'Premium noise-canceling wireless earbuds with spatial audio.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Luxe',
                'description': 'Elegant fitness tracker with a slim design and vibrant AMOLED display.',
                'price': 149.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Samsung 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and productivity.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Hoka One One Clifton 8 Running Shoes',
                'description': 'Cushioned running shoes for a plush and smooth ride.',
                'price': 139.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Vitamix E310 Explorian Blender',
                'description': 'High-performance blender for blending, pureeing, and more.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Audio',
                'description': 'Smart speaker with powerful sound for music and podcasts.',
                'price': 99.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Pro Controller',
                'description': 'High-quality controller for Nintendo Switch gaming.',
                'price': 69.99,
                'stock': 15,
                'category': 'Gaming Accessories'
            },
            {
                'name': 'Sony 85-inch 4K TV',
                'description': 'Massive 4K UHD TV for home theater enthusiasts.',
                'price': 2499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Smart Oven Air Fryer',
                'description': 'Multi-functional countertop oven with air frying capabilities.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'DJI Mavic Air 2 Drone',
                'description': 'Compact drone with 4K camera and intelligent flight modes.',
                'price': 799.99,
                'stock': 10,
                'category': 'Electronics'
            },
            {
                'name': 'Bose QuietComfort 45 Headphones',
                'description': 'Premium noise-canceling headphones with plush ear cushions.',
                'price': 349.99,
                'stock': 15,
                'category': 'Headphones'
            },
            {
                'name': 'LG 75-inch NanoCell 4K TV',
                'description': 'NanoCell TV with vibrant colors and wide viewing angles.',
                'price': 1799.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
            {
                'name': 'Instant Pot Duo Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small households.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Pro 11-inch (3rd Gen)',
                'description': 'Compact and powerful iPad for creative professionals.',
                'price': 799.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sennheiser HD 660 S Headphones',
                'description': 'High-quality open-back headphones for audiophiles.',
                'price': 499.99,
                'stock': 10,
                'category': 'Headphones'
            },
            {
                'name': 'LG 43-inch 4K TV',
                'description': 'Affordable 4K UHD TV with a large screen for entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Nespresso Vertuo Coffee and Espresso Maker',
                'description': 'Coffee and espresso maker with convenient pod system.',
                'price': 179.99,
                'stock': 15,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Sony Alpha a6400 Mirrorless Camera',
                'description': 'Mirrorless camera with fast autofocus and 4K video recording.',
                'price': 899.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Apple AirPods Pro',
                'description': 'Premium noise-canceling wireless earbuds with spatial audio.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Luxe',
                'description': 'Elegant fitness tracker with a slim design and vibrant AMOLED display.',
                'price': 149.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Samsung 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and productivity.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Hoka One One Clifton 8 Running Shoes',
                'description': 'Cushioned running shoes for a plush and smooth ride.',
                'price': 139.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Vitamix E310 Explorian Blender',
                'description': 'High-performance blender for blending, pureeing, and more.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Audio',
                'description': 'Smart speaker with powerful sound for music and podcasts.',
                'price': 99.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Pro Controller',
                'description': 'High-quality controller for Nintendo Switch gaming.',
                'price': 69.99,
                'stock': 15,
                'category': 'Gaming Accessories'
            },
            {
                'name': 'Sony 85-inch 4K TV',
                'description': 'Massive 4K UHD TV for home theater enthusiasts.',
                'price': 2499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Smart Oven Air Fryer',
                'description': 'Multi-functional countertop oven with air frying capabilities.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'DJI Mavic Air 2 Drone',
                'description': 'Compact drone with 4K camera and intelligent flight modes.',
                'price': 799.99,
                'stock': 10,
                'category': 'Electronics'
            },
            {
                'name': 'Bose QuietComfort 45 Headphones',
                'description': 'Premium noise-canceling headphones with plush ear cushions.',
                'price': 349.99,
                'stock': 15,
                'category': 'Headphones'
            },
            {
                'name': 'LG 75-inch NanoCell 4K TV',
                'description': 'NanoCell TV with vibrant colors and wide viewing angles.',
                'price': 1799.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
            {
                'name': 'Instant Pot Duo Mini 3-Quart',
                'description': 'Compact electric pressure cooker for small households.',
                'price': 79.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Pro 11-inch (3rd Gen)',
                'description': 'Compact and powerful iPad for creative professionals.',
                'price': 799.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sennheiser HD 660 S Headphones',
                'description': 'High-quality open-back headphones for audiophiles.',
                'price': 499.99,
                'stock': 10,
                'category': 'Headphones'
            },
            {
                'name': 'LG 43-inch 4K TV',
                'description': 'Affordable 4K UHD TV with a large screen for entertainment.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Nespresso Vertuo Coffee and Espresso Maker',
                'description': 'Coffee and espresso maker with convenient pod system.',
                'price': 179.99,
                'stock': 15,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Sony Alpha a6400 Mirrorless Camera',
                'description': 'Mirrorless camera with fast autofocus and 4K video recording.',
                'price': 899.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Apple AirPods Pro',
                'description': 'Premium noise-canceling wireless earbuds with spatial audio.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Luxe',
                'description': 'Elegant fitness tracker with a slim design and vibrant AMOLED display.',
                'price': 149.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Samsung 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and productivity.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Hoka One One Clifton 8 Running Shoes',
                'description': 'Cushioned running shoes for a plush and smooth ride.',
                'price': 139.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Vitamix E310 Explorian Blender',
                'description': 'High-performance blender for blending, pureeing, and more.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Audio',
                'description': 'Smart speaker with powerful sound for music and podcasts.',
                'price': 99.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Pro Controller',
                'description': 'High-quality controller for Nintendo Switch gaming.',
                'price': 69.99,
                'stock': 15,
                'category': 'Gaming Accessories'
            },
            {
                'name': 'Sony 85-inch 4K TV',
                'description': 'Massive 4K UHD TV for home theater enthusiasts.',
                'price': 2499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Smart Oven Air Fryer',
                'description': 'Multi-functional countertop oven with air frying capabilities.',
                'price': 349.99,
                'stock': 10,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'DJI Mavic Air 2 Drone',
                'description': 'Compact drone with 4K camera and intelligent flight modes.',
                'price': 799.99,
                'stock': 10,
                'category': 'Electronics'
            },
            {
                'name': 'Bose QuietComfort 45 Headphones',
                'description': 'Premium noise-canceling headphones with plush ear cushions.',
                'price': 349.99,
                'stock': 15,
                'category': 'Headphones'
            },
            {
                'name': 'LG 75-inch NanoCell 4K TV',
                'description': 'NanoCell TV with vibrant colors and wide viewing angles.',
                'price': 1799.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Sony WH-1000XM4',
                'description': 'Wireless noise-canceling headphones with exceptional sound quality.',
                'price': 349.99,
                'stock': 30,
                'category': 'Headphones'
            },
            {
                'name': 'Samsung 55-inch QLED TV',
                'description': 'QLED TV with Quantum Dot technology for vivid colors and contrast.',
                'price': 1299.99,
                'stock': 10,
                'category': 'Televisions'
            },
            {
                'name': 'KitchenAid Stand Mixer',
                'description': 'Powerful stand mixer for baking and cooking enthusiasts.',
                'price': 349.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Apple Watch Series 6',
                'description': 'Advanced smartwatch with health and fitness tracking features.',
                'price': 399.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for immersive gaming and multitasking.',
                'price': 599.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Adidas Ultraboost Running Shoes',
                'description': 'High-performance running shoes with responsive cushioning.',
                'price': 159.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'Cuisinart Food Processor',
                'description': 'Versatile food processor for chopping, slicing, and shredding.',
                'price': 89.99,
                'stock': 20,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Mini',
                'description': 'Compact smart speaker with Google Assistant for voice control.',
                'price': 49.99,
                'stock': 35,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series X',
                'description': 'Next-gen gaming console with fast load times and 4K gaming.',
                'price': 499.99,
                'stock': 5,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 50-inch 4K TV',
                'description': 'Affordable 4K UHD TV with built-in streaming apps.',
                'price': 349.99,
                'stock': 15,
                'category': 'Televisions'
            },
            {
                'name': 'Cuisinart Coffee Grinder',
                'description': 'Electric coffee grinder for freshly ground beans.',
                'price': 49.99,
                'stock': 25,
                'category': 'Coffee Accessories'
            },
            {
                'name': 'Canon EOS Rebel T7 DSLR Camera',
                'description': 'Entry-level DSLR camera with basic kit lens for beginners.',
                'price': 499.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Bose SoundSport Wireless Earbuds',
                'description': 'Wireless earbuds for active lifestyles with crisp sound quality.',
                'price': 129.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Fitbit Charge 3',
                'description': 'Fitness tracker with heart rate monitoring and swim tracking.',
                'price': 129.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'LG 32-inch Monitor',
                'description': 'Full HD monitor for work and entertainment.',
                'price': 199.99,
                'stock': 15,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Ghost 14 Running Shoes',
                'description': 'Cushioned running shoes for a comfortable ride.',
                'price': 129.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'Crock-Pot Express Crock Multi-Cooker',
                'description': 'Versatile multi-cooker for pressure cooking, slow cooking, and more.',
                'price': 69.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'iPad Air (4th Gen)',
                'description': 'Powerful iPad with a sleek design for creativity and productivity.',
                'price': 599.99,
                'stock': 10,
                'category': 'Tablets'
            },
            {
                'name': 'Sony WF-1000XM4 Earbuds',
                'description': 'True wireless earbuds with industry-leading noise cancellation.',
                'price': 249.99,
                'stock': 15,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 245 Music',
                'description': 'GPS smartwatch for runners with music streaming support.',
                'price': 299.99,
                'stock': 20,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 27-inch Gaming Monitor',
                'description': 'High-refresh-rate gaming monitor for competitive gaming.',
                'price': 249.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance Fresh Foam 1080v11',
                'description': 'Cushioned running shoes with a comfortable fit.',
                'price': 149.99,
                'stock': 25,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Pro 900 Series Blender',
                'description': 'Compact blender for making smoothies and shakes.',
                'price': 79.99,
                'stock': 30,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 5',
                'description': 'Smart display with Alexa for video calls and entertainment.',
                'price': 79.99,
                'stock': 20,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Xbox Series S',
                'description': 'Next-gen gaming console for digital gaming experiences.',
                'price': 299.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Sony 65-inch 4K TV',
                'description': 'Large 4K UHD TV with excellent picture quality.',
                'price': 899.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville Barista Express Espresso Machine',
                'description': 'Semi-automatic espresso machine for coffee enthusiasts.',
                'price': 699.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Fujifilm Instax Mini 11 Instant Camera',
                'description': 'Fun instant camera for capturing memories on the go.',
                'price': 69.99,
                'stock': 15,
                'category': 'Cameras'
            },
            {
                'name': 'JBL Free X True Wireless Earbuds',
                'description': 'Wireless earbuds with rich JBL sound and convenient controls.',
                'price': 79.99,
                'stock': 25,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Venu 2 Smartwatch',
                'description': 'Smartwatch with AMOLED display and advanced fitness tracking.',
                'price': 349.99,
                'stock': 15,
                'category': 'Wearables'
            },
            {
                'name': 'AOC 24-inch Gaming Monitor',
                'description': 'Budget-friendly gaming monitor with fast response times.',
                'price': 149.99,
                'stock': 20,
                'category': 'Monitors'
            },
            {
                'name': 'Saucony Kinvara 12 Running Shoes',
                'description': 'Lightweight running shoes for speed and comfort.',
                'price': 119.99,
                'stock': 30,
                'category': 'Running Shoes'
            },
            {
                'name': 'KitchenAid Hand Mixer',
                'description': 'Compact hand mixer for baking and cooking tasks.',
                'price': 49.99,
                'stock': 25,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Google Nest Hub Max',
                'description': 'Smart display with a large screen and Google Assistant.',
                'price': 229.99,
                'stock': 10,
                'category': 'Smart Speakers'
            },
            {
                'name': 'Nintendo Switch Lite',
                'description': 'Portable gaming console for Nintendo fans.',
                'price': 199.99,
                'stock': 15,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 27-inch Curved Monitor',
                'description': 'Curved monitor for immersive gaming and entertainment.',
                'price': 299.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Brooks Adrenaline GTS 21 Running Shoes',
                'description': 'Stability running shoes for support and comfort.',
                'price': 129.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'Hamilton Beach Coffee Maker',
                'description': 'Drip coffee maker with programmable features for convenience.',
                'price': 39.99,
                'stock': 25,
                'category': 'Coffee Makers'
            },
            {
                'name': 'Canon PowerShot G7 X Mark III Camera',
                'description': 'Compact camera with 4K video recording and fast autofocus.',
                'price': 699.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Beats Powerbeats Pro Wireless Earbuds',
                'description': 'Wireless earbuds with secure fit for workouts and sports.',
                'price': 199.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Forerunner 945 Smartwatch',
                'description': 'Advanced smartwatch with GPS and performance analytics.',
                'price': 599.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Acer 34-inch Ultrawide Monitor',
                'description': 'Ultrawide monitor for productivity and immersive gaming.',
                'price': 499.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'New Balance 990v5 Running Shoes',
                'description': 'Classic running shoes known for comfort and durability.',
                'price': 169.99,
                'stock': 20,
                'category': 'Running Shoes'
            },
            {
                'name': 'NutriBullet Blender Combo',
                'description': 'Versatile blender for making smoothies, soups, and more.',
                'price': 129.99,
                'stock': 15,
                'category': 'Kitchen Appliances'
            },
            {
                'name': 'Amazon Echo Show 8',
                'description': 'Smart display with an 8-inch screen and Alexa voice assistant.',
                'price': 99.99,
                'stock': 15,
                'category': 'Smart Speakers'
            },
            {
                'name': 'PlayStation 4 Pro',
                'description': 'High-performance gaming console with 4K gaming support.',
                'price': 399.99,
                'stock': 10,
                'category': 'Gaming Consoles'
            },
            {
                'name': 'Samsung 75-inch 4K TV',
                'description': 'Large 4K UHD TV for a cinematic viewing experience.',
                'price': 1499.99,
                'stock': 5,
                'category': 'Televisions'
            },
            {
                'name': 'Breville BES870XL Espresso Machine',
                'description': 'Semi-automatic espresso machine with built-in grinder.',
                'price': 599.99,
                'stock': 10,
                'category': 'Coffee Makers'
            },
            {
                'name': 'GoPro HERO9 Black Action Camera',
                'description': 'Action camera with 5K video recording and waterproof design.',
                'price': 449.99,
                'stock': 10,
                'category': 'Cameras'
            },
            {
                'name': 'Jabra Elite 75t Wireless Earbuds',
                'description': 'True wireless earbuds with customizable sound profiles.',
                'price': 179.99,
                'stock': 20,
                'category': 'Earphones'
            },
            {
                'name': 'Garmin Fenix 6 Pro Smartwatch',
                'description': 'Premium multisport GPS smartwatch with heart rate monitoring.',
                'price': 699.99,
                'stock': 10,
                'category': 'Wearables'
            },
            {
                'name': 'Dell 27-inch 4K Monitor',
                'description': '4K UHD monitor with USB-C connectivity for professionals.',
                'price': 399.99,
                'stock': 10,
                'category': 'Monitors'
            },
            {
                'name': 'Salomon Speedcross 5 Trail Running Shoes',
                'description': 'Trail running shoes for off-road adventures and rugged terrain.',
                'price': 129.99,
                'stock': 15,
                'category': 'Running Shoes'
            },
    ]
    n=1
    for i in products:
        (category, created) = Category.objects.get_or_create(name=i['name'])
        Product.objects.create(
            name=i['name'],
            description=i['description'],
            price=i['price'],
            stock=i['stock'],
            category=category
        )
        print(f"Creatin {i['name']} Product")
        print(n)
        n+=1
if __name__ == "__main__":
    seed_data()

from flask import Flask
from data import db_session
from data.category import Category
from data.products import Products

db_session.global_init("db/shop.db")
session = db_session.create_session()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def fill_categories():
    categories = ['Shooter', 'Horror', 'Simulator', 'RPG', 'Battle Royale', 'Strategy']
    for cat_name in categories:
        cat = Category()
        cat.name = cat_name
        session.add(cat)
    session.commit()


def fill_products():
    products_data = [
        {"name": "Call of Duty: Modern Warfare", "price": 59.99,
         "description": "Experience the ultimate online playground with classic multiplayer.",
         "image": "cod_mw.jpg", "stock": 100, "category_id": 1},
        {"name": "Resident Evil Village", "price": 49.99,
         "description": "Experience survival horror like never before in the eighth major installment in the Resident Evil series.",
         "image": "re_village.jpg", "stock": 50, "category_id": 2},
        {"name": "The Sims 4", "price": 39.99,
         "description": "Enjoy the power to create and control people in a virtual world with The Sims™ 4.",
         "image": "sims_4.jpg", "stock": 75, "category_id": 3},
        {"name": "The Witcher 3: Wild Hunt", "price": 29.99,
         "description": "Become a monster slayer for hire and embark on an epic journey to track down the child of prophecy.",
         "image": "witcher_3.jpg", "stock": 80, "category_id": 4},
        {"name": "Fortnite", "price": 0.00,
         "description": "Jump into Fortnite Battle Royale and start your adventure on the island.",
         "image": "fortnite.jpg", "stock": 150, "category_id": 5},
        {"name": "FIFA 22", "price": 69.99,
         "description": "Experience the world's game like never before with FIFA 22.",
         "image": "fifa_22.jpg", "stock": 60, "category_id": 6},
        {"name": "Minecraft", "price": 26.95,
         "description": "Explore infinite worlds and build everything from the simplest of homes to the grandest of castles in Minecraft.",
         "image": "minecraft.jpg", "stock": 200, "category_id": 3},
        {"name": "Among Us", "price": 5.00,
         "description": "Join your crewmates in a multiplayer game of teamwork and betrayal!",
         "image": "among_us.jpg", "stock": 90, "category_id": 5},
        {"name": "Grand Theft Auto V", "price": 29.99,
         "description": "Enter the lives of three very different criminals, Michael, Franklin, and Trevor, as they risk everything in a series of daring and dangerous heists that could set them up for life.",
         "image": "gta_v.jpg", "stock": 70, "category_id": 4},
        {"name": "Red Dead Redemption 2", "price": 39.99,
         "description": "America, 1899. The end of the Wild West era has begun. After a robbery goes badly wrong in the western town of Blackwater, Arthur Morgan and the Van der Linde gang are forced to flee.",
         "image": "rdr2.jpg", "stock": 55, "category_id": 4},
        {"name": "Assassin's Creed Valhalla", "price": 49.99,
         "description": "Become Eivor, a legendary Viking raider, and lead your clan from the harsh shores of Norway to a new home amid the lush farmlands of ninth-century England.",
         "image": "ac_valhalla.jpg", "stock": 60, "category_id": 4},
        {"name": "Overwatch", "price": 39.99,
         "description": "Join the fight for the future in the ultimate team-based shooter!",
         "image": "overwatch.jpg", "stock": 80, "category_id": 1},
        {"name": "Cyberpunk 2077", "price": 59.99,
         "description": "Enter the world of Cyberpunk 2077 - a story-driven, open world RPG of the dark future from CD PROJEKT RED.",
         "image": "cyberpunk_2077.jpg", "stock": 45, "category_id": 4},
        {"name": "League of Legends", "price": 0.00,
         "description": "Dive into a colorful and thrilling world where teams of champions battle for supremacy.",
         "image": "lol.jpg", "stock": 100, "category_id": 6},
        {"name": "Death Stranding", "price": 39.99,
         "description": "From legendary game creator Hideo Kojima comes an all-new, genre-defying experience for the PlayStation®4.",
         "image": "death_stranding.jpg", "stock": 30, "category_id": 2},
        {"name": "Valorant", "price": 0.00,
         "description": "A 5v5 character-based tactical shooter where creativity is your greatest weapon.",
         "image": "valorant.jpg", "stock": 70, "category_id": 1},
        {"name": "The Elder Scrolls V: Skyrim", "price": 39.99,
         "description": "Winner of more than 200 Game of the Year Awards, Skyrim Special Edition brings the epic fantasy to life in stunning detail.",
         "image": "skyrim.jpg", "stock": 85, "category_id": 4},
        {"name": "Tom Clancy's Rainbow Six Siege", "price": 19.99,
         "description": "Command an arsenal of gadgets to secure the win in Tom Clancy's Rainbow Six Siege.",
         "image": "rainbow_six.jpg", "stock": 110, "category_id": 1},
        {"name": "Apex Legends", "price": 0.00,
         "description": "Conquer with character in Apex Legends, a free-to-play* Battle Royale shooter where legendary characters with powerful abilities team up to battle for fame and fortune on the fringes of the Frontier.",
         "image": "apex_legends.jpg", "stock": 120, "category_id": 5},
        {"name": "Counter-Strike: Global Offensive", "price": 14.99,
         "description": "Counter-Strike: Global Offensive (CS: GO) expands upon the team-based action gameplay that it pioneered when it was launched 19 years ago.",
         "image": "csgo.jpg", "stock": 65, "category_id": 1}
    ]
    for product_info in products_data:
        product = Products()
        product.name = product_info["name"]
        product.price = product_info["price"]
        product.description = product_info["description"]
        product.image = product_info["image"]
        product.stock = product_info["stock"]
        product.category_id = product_info["category_id"]
        session.add(product)
    session.commit()


def main():
    fill_categories()
    fill_products()
    app.run()


if __name__ == '__main__':
    main()

# 
import shop_project
import bot_app
import threading
# 
# if __name__ == "__main__":
#     # 
#     shop_project.project_shop.run(debug = True)



if __name__ == "__main__":

    shop_project.project_shop.run( debug = True )

    # thread_1 = threading.Thread(target = shop_project.project_shop.run)
    # thread_2 = threading.Thread(target = bot_app.bot.infinity_polling)
    # thread_1.start()
    # thread_2.start()
    # thread_1.join()
    # thread_2.join()
try:
    import requests
    import bs4 as bs
    import pandas as pd

    from codes import category, publisher, writers




    class Banner:
        def banner(self):
            print("""
                ---------------------------------------------
                | \t\tChoose Any Of Them \t\t|
                ---------------------------------------------
                1. A Specific Writer's All Books
                2. All Books From A Publisher
                3. Category Wise Book
                4. Help
                5. Exit
                """)
            

    if __name__ == "__main__":

        banner = Banner()
        banner.banner()
            
        while True:
            choice = int(input("Your Choice: "))
                
            # Option 1
            if choice == 1:
                base_url = input("Enter Your URL: ")
                if "publisher" in base_url:
                    print("You are trying to enter 'Publisher' url. Try Again!")
                else:
                    writers = writers.FromWriter(base_url)
                    writers.writersBook()
                
            # Option 2
            elif choice == 2:
                base_url = input("Enter Your URL: ")
                if "author" in base_url:
                    print("You are trying to enter 'Author' url. Try Again!")
                else:
                    publishers = publisher.FromPublisher(base_url)
                    publishers.writersBook() 

            # Option 3
            elif choice == 3:
                base_url = input("Enter Your URL: ")
                if "author" in base_url or "publisher" in base_url:
                    print("You are trying to enter 'Author' or 'Publisher' url. Try Again!")
                else:
                    publishers = publisher.FromPublisher(base_url)
                    publishers.writersBook() 


            elif choice == 4:
                    #Banner
                print("""
                        -----------------------------------------------------
                        | You Have to Enter Proper Link Structue Like This. |
                        -----------------------------------------------------\n
                        Example:
                        For 1: https://www.rokomari.com/book/author/1/humayun-ahmed
                        For 2: https://www.rokomari.com/book/publisher/38/prothoma-prokashan
                            """)
                banner.banner()

            elif choice == 5:
                print("\n\n\tHappy Coding! Bye... Bye ;)\n\n")
                exit()

except KeyboardInterrupt:
    print("\n\n\tHappy Coding! Bye... Bye ;)\n\n")
    exit()

except ValueError:
    print("\n\tTry Again With Valid Choice Input as Number!\n\n")
    
except ModuleNotFoundError:
    import os
    os.system("pip install -r requirements.txt")
    print("\n\tNow you are good to go. Just run:\n\t[-] python booklist.py\n")

except Exception as e:
    print(e)
    print("""
        -----------------------------------------------------
        | You Have to Enter Proper Link Structue Like This. |
        -----------------------------------------------------\n
        Example:
        For 1: https://www.rokomari.com/book/author/1/humayun-ahmed
        For 2: https://www.rokomari.com/book/publisherprothoma-prokashan
        """)

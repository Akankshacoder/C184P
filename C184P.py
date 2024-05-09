import tkinter as tk
import requests
import json

root = tk.Tk()
root.title("BBC News Widget")

def fetch_news():
    api_url = "https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=YOUR_API_KEY"
    api_request = requests.get(api_url)
    open_bbc_page = json.loads(api_request.content)
    titles = []
    descriptions = []
    for article in open_bbc_page["articles"]:
        titles.append(article["title"])
        descriptions.append(article["description"])
    news1.config(text="Title 1: " + titles[0])
    news_desc1.config(text="Description: " + descriptions[0])
    news2.config(text="Title 2: " + titles[1])
    news_desc2.config(text="Description: " + descriptions[1])
    news3.config(text="Title 3: " + titles[2])
    news_desc3.config(text="Description: " + descriptions[2])
    news4.config(text="Title 4: " + titles[3])
    news_desc4.config(text="Description: " + descriptions[3])
    news5.config(text="Title 5: " + titles[4])
    news_desc5.config(text="Description: " + descriptions[4])


newsupdate = tk.Label(root, text="BBC News Update", font=("Arial", 16, "bold"))
newsupdate.place(relx=0.5, rely=0.05, anchor="center")

news1 = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
news1.place(relx=0.05, rely=0.15, anchor="w")
news2 = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
news2.place(relx=0.05, rely=0.30, anchor="w")
news3 = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
news3.place(relx=0.05, rely=0.45, anchor="w")
news4 = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
news4.place(relx=0.05, rely=0.60, anchor="w")
news5 = tk.Label(root, font=("Arial", 12, "bold"), wraplength=500, justify="left")
news5.place(relx=0.05, rely=0.75, anchor="w")

news_desc1 = tk.Label(root, wraplength=500, justify="left")
news_desc1.place(relx=0.05, rely=0.20, anchor="w")
news_desc2 = tk.Label(root, wraplength=500, justify="left")
news_desc2.place(relx=0.05, rely=0.35, anchor="w")
news_desc3 = tk.Label(root, wraplength=500, justify="left")
news_desc3.place(relx=0.05, rely=0.50, anchor="w")
news_desc4 = tk.Label(root, wraplength=500, justify="left")
news_desc4.place(relx=0.05, rely=0.65, anchor="w")
news_desc5 = tk.Label(root, wraplength=500, justify="left")
news_desc5.place(relx=0.05, rely=0.80, anchor="w")

fetch_news()

root.attributes('-toolwindow', True)
root.mainloop()

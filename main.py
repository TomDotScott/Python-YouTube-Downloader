import tkinter as tk

from pytube import YouTube

global entry


def downloadVid():
    string = entry.get()
    yt = YouTube(str(string))
    print(yt.title)

    stream = yt.streams.first()
    stream.download('C:/Users/tomsc/Downloads')


root = tk.Tk()

w = tk.Label(root,text="Youtube Downloader")
w.pack()


entry = tk.Entry(root,bd=5)
entry.pack(side=tk.TOP)


button = tk.Button(root, text="Download", fg="red", command=downloadVid)
button.pack(side=tk.BOTTOM)

root.mainloop()

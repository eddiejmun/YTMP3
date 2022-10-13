from tkinter import filedialog
from pytube import YouTube
import tkinter
import customtkinter
import os

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("YouTube MP3 Downloader")
        self.minsize(700, 500)

        self.grid_columnconfigure(1, weight=2)

        # Input for video URL
        self.url_input = customtkinter.CTkEntry(master=self, placeholder_text='YouTube URL')
        self.url_input.grid(row=0, column=1, padx=20, pady=20, sticky='ew')

        # Label for video URL input
        self.url_label = customtkinter.CTkLabel(master=self, text='YouTube URL:')
        self.url_label.grid(row=0, column=0, padx=20, pady=20, sticky='e')

        # Label for folder path input
        self.path_label = customtkinter.CTkLabel(master=self, text='Download location:')
        self.path_label.grid(row=1, column=0,  padx=20, pady=20, sticky='e')

        # Input for download location folder path
        self.path_input = customtkinter.CTkEntry(master=self, placeholder_text='Path to download location')
        self.path_input.grid(row=1, column=1, padx=20, pady=20, sticky='ew')

        # Button to open file explorer
        self.browse_button = customtkinter.CTkButton(master=self, text='Find Folder', command=self.browse_folder)
        self.browse_button.grid(row=1, column=2, padx=20, pady=20)

        # Download button
        self.download_button = customtkinter.CTkButton(master=self, text='Download', command=self.download)
        self.download_button.grid(row=2, column=1, padx=20, pady=20, sticky='ew')

        # Textbox for logging information
        self.logs = customtkinter.CTkTextbox(master=self)
        self.logs.grid(row=3, column=0, columnspan=3, padx=20, pady=(20, 0), sticky="nsew")

        self.credits = customtkinter.CTkLabel(master=self, text='Created by Eddie Mun. Made with Python, Tkinter, and love.')
        self.credits.grid(row=4, column=0, columnspan=4, sticky="nsew", pady=20)

    def browse_folder(self):
        global folder_path
        filename = filedialog.askdirectory()
        self.path_input.insert(0, filename)

    def download(self):
        self.logs.insert("insert", "Starting download..." + "\n")
        url = self.url_input.get()
        path = self.path_input.get()
        if not path:
            self.logs.insert("insert",  "Please specify a download location!" + "\n")
        if not url:
            self.logs.insert("insert", "Please provide a YouTube url!" + "\n")
        if url and path:
            try:
                yt = YouTube(url)
                video = yt.streams.filter(only_audio=True).first()
                out_file = video.download(output_path=path)

                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)
                self.logs.insert("insert", "Downloaded: " + yt.title + "\n")
                self.logs.insert("insert", "Successfully downloaded!" + "\n")
            except:
                self.logs.insert("insert", "ERROR: Could not download mp3" + "\n")
                self.logs.insert("insert", "Check YouTube url or folder path" + "\n")
            

     
if __name__ == "__main__":
    app = App()
    app.mainloop()
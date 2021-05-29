from pytube import YouTube

print("Enter Link")
link = input()
print("Enter file name")
s=input()

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "C:/YouTube Videos/", 
filename = s)
except:
    print("Some Error!")
print('Task Completed!')
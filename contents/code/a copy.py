import os
import shutil



from modules.MyFile import MyFile



root_dir = r"C:\Users\vvn20206205\Downloads\video\DoThiJava"
new_dir = r"C:\Users\vvn20206205\Downloads\video\DoThiJava\new"



# print(root_dir)
# print(new)
mp4_files = MyFile.TimKiem(root_dir, ".mp4")

# print(mp4_files)
for i,mp4_file in enumerate(mp4_files):
    # print(i)
    # print(mp4_file)


    old = mp4_file
    print("🐍 File: code/a.py | Line: 21 | undefined ~ old",old)
    new = os.path.join(new_dir,f"{i}.mp4")
    print("🐍 File: code/a.py | Line: 23 | undefined ~ new",new)
    # print(mp4_file)
    shutil.copy2(old, new)

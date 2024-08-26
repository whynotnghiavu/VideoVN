
# def HamXuLi(mp4_file):
#     audio = NewNghia(mp4_file) + ".wav"
#     mp4_vn1_nghia = NewNghia(mp4_file) + CONST.MP4_V1_NGHIA
#     mp4_vn2_nghia = NewNghia(mp4_file) + CONST.MP4_V2_NGHIA

#     MyExecute(f'ffmpeg -i {mp4_file} -c:v copy -an {mp4_vn1_nghia}')
#     MyExecute(f'ffmpeg -i {mp4_vn1_nghia} -i {audio} -c:v copy -c:a aac -strict experimental {mp4_vn2_nghia}')


# def middleware(i):
#     HamXuLi(i)


# def GhepAmThanh(root_dir):
#     mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)
#     # mp4_files = MyFile.TimKiem(root_dir, CONST.MP4)

#     if (len(mp4_files) % 2 == 1):
#         end = mp4_files.pop()
#         middleware(end)

#     for i in range(0, len(mp4_files) - 1, 2):
#         thread1 = threading.Thread(target=middleware, args=(mp4_files[i],))
#         thread2 = threading.Thread(target=middleware, args=(mp4_files[i + 1],))
#         thread1.start()
#         thread2.start()
#         thread1.join()
#         thread2.join()
#         sleep(10)

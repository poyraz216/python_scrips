import os

disk = os.statvfs("/home/")


totalBytes = float(disk.f_bsize*disk.f_blocks)

print("Total space : {} GBytes".format(totalBytes/1024/1024/1024))

totalUsedSpace = float(disk.f_bsize*(disk.f_blocks-disk.f_bfree))


print("Used space : {} GBytes".format(totalUsedSpace/1024/1024/1024))

totalAvailSpace = float(disk.f_bsize*disk.f_bfree)


print("Available space : {} GBytes".format(totalAvailSpace/1024/1024/1024))
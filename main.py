# This script handles the user input and output fot creating large amounts of custom contours
def main():
    import os
    import Contour_Creator as CC



    # filepathorg = input("file location")
    filepathorg = r"C:\Users\dstacey\Desktop\Test"
    LiDARList = ["usgs16-70cm_15RUQ3134095.laz"]
    CC.Contour_Creator(filepathorg, "A1", LiDARList, keepgms = 1)





if __name__ == '__main__':
    main()
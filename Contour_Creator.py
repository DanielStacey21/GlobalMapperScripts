# This program is designed to create contours in Global Mapper from large amounts of LiDAR files
def Contour_Creator(filepathorg, Gridnum, LiDARList, keepgms = 1):
    from os import path
    import os
    import time
    import Gridnum_Creator
    from os.path import exists

    # This function takes a grid number and a list of the LiDAR used and creates a .gms file
    def creategmsfile(filepathorg, Gridnum, LiDARList, filter = "ground", outputfile = 0):
        
        #Names the .gms (global mapper script) that will be used
        Gridnumgms = Gridnum + '.gms'
        fileGridPath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnumgms)
        f = open(fileGridPath, 'w')

        f.write('GLOBAL_MAPPER_SCRIPT VERSION="1.00"\n')
        f.write('\n')

        # Writes a line for every LiDAR file coming in
        for i in LiDARList:
            filepath = os.path.join(r'F:\POC-2\POC-2\LiDAR\Neches\*\*', i)
            f.write('IMPORT FILENAME=\"' + filepath + '\" TYPE=LAZ\n')
            f.write('\n')

        # Sets the parameters on which classied LiDAR to use
        if filter == "ground":
            f.write('LIDAR_FILTER="NONE,2"\n')
            f.write('\n')

        # Creates Elevation grid
        f.write('GENERATE_ELEV_GRID NO_DATA_DIST_MULT=25 ELEV_UNITS=FEET\n')
        f.write('\n')

        # Unloads the LiDAR to save processing time. After this point Global Mapper creates the contours from the elevation grid
        for i in LiDARList:
            filepath = os.path.join(r'F:\POC-2\POC-2\LiDAR\Neches\*\*', i)
            f.write('UNLOAD_LAYER FILENAME=\"' + filepath + '\" TYPE=LAZ\n')
            f.write('\n')

        # Generates the Contours
        f.write('GENERATE_CONTOURS INTERVAL=5 ELEV_UNITS=FEET MIN_CONTOUR_LEN=25\n')
        f.write('\n')

        if outputfile == 0:
            Gridnumshp = Gridnum + '.shp'
            fileexportpath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnum, "Shapefile", Gridnumshp)
            f.write('EXPORT_VECTOR FILENAME=\"' + fileexportpath + '\" TYPE=SHAPEFILE SHAPE_TYPE=LINES GEN_PRJ_FILE=YES')
            f.write('\n')
            Gridnumdwg = Gridnum + '.dwg'
            fileexportpath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnum, "DWG", Gridnumdwg)
            f.write('EXPORT_VECTOR FILENAME=\"' + fileexportpath + '\" TYPE=DWG SHAPE_TYPE=LINES GEN_PRJ_FILE=NO')

        # closes the .gms file. The .gms file cannot be written in after this step.
        f.close()

        # Passes command to commandline
        commandline = "\"\"C:\Program Files\GlobalMapper23.0_64bit\global_mapper.exe\"  \"" + filepathorg  + "\\EXPORT\\"  + Gridnum[0] + "\\" +Gridnumgms + "\" -var1 01 -var2 33\""
        print(commandline)
        os.system('cmd /c ' + commandline)

        

    # LiDARList = Gridnum_Creator.main(Gridnum)

    start_time = time.time()

    
    newfolderpath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnum)
    if not os.path.exists(newfolderpath):
        os.makedirs(newfolderpath)

    newfolderpath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnum, "Shapefile")
    if not os.path.exists(newfolderpath):
        os.makedirs(newfolderpath)

    newfolderpath = os.path.join(filepathorg, "EXPORT", Gridnum[0], Gridnum, "DWG")
    if not os.path.exists(newfolderpath):
        os.makedirs(newfolderpath)


    creategmsfile(filepathorg, Gridnum, LiDARList)
    
    print("--- %s seconds  overall---" % (time.time() - start_time))

    #Code to reomve gms file. Default is to keep.
    if keepgms == 0:
        Gridnumgms = Gridnum + '.gms'
        filepath = os.path.join(filepathorg, "EXPORT", Gridnumgms)
        os.remove(filepath)



if __name__ == '__main__':
    Contour_Creator(filepathorg, Gridnum, LiDARList, keepgms = 1)


# "C:\Program Files\GlobalMapper23.0_64bit\global_mapper.exe" "F:\POC-2\POC-2\Global Mapper Scripting\Test\P12.gms" -var1 01 -var2 33
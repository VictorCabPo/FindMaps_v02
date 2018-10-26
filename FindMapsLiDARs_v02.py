#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 10:48:35 2017

@author: victor

EDENVALE YOUNG ASSOCIATES
"""

# we export the modules needed

import os, glob, shutil, geopandas 

# we get the variables of the script

print("You can take the basemaps for England, Wales and Scotland.\nYou can take the LiDAR for England and Wales, but not for Scotland.")

Maps = input('Do you want basemaps? (y/n): ')

if Maps == 'y':
	FolMaps = input('Where do you want to keep the basemaps?: ')

LiD = input('Do you want LiDAR? (y/n): ')

if LiD == 'y':
	FolLiD = input('Where do you want to keep the LiDARs?: ')

shp = input('Zone Shapefile: ')

Country = input('What country are you working in? (England:e, Scotland:s, Wales:w): ')

#**************************************************************************************************************
# GRIDs with the maps for each region.
#**************************************************************************************************************

EnglandMap = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/EnglandMaps5km.shp"
#EnglandLiD = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/EnglandLiDAR1km.shp"
ScotlandMap = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ScotlandMaps5km.shp"
#ScotlandLiD = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ScotlandLiDAR1km.shp"
WalesMap = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/WalesMaps5km.shp"
WalesLiD = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/WalesLiDAR1km.shp"

EnglandArLiD = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/EnglandAreasLiDAR.shp"

# folder with the data maps and LiDARs

EDYMaps = "/net/O/0000_ElectronicLibrary/Data/Mapping/OS_Open_Map-Local_04-2017/Raster/data"
EDYLiDAR = "/net/O/0000_ElectronicLibrary/Data/Mapping/LiDAR/DTM"

#**************************************************************************************************************
# Areas LiDAR of England
#**************************************************************************************************************

nt = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/nt.shp"
nu = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/nu.shp"
nx = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/nx,shp"
ny = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/ny.shp"
nz = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/nz.shp"
ov = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/ov.shp"
sd = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sd.shp"
se = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/se.shp"
sj = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sj.shp"
sk = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sk.shp"
so = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/so.shp"
sp = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sp.shp"
ss = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/ss.shp"
st = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/st.shp"
su = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/su.shp"
sv = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sv.shp"
sw = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sw.shp"
sx = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sx.shp"
sz = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/sz.shp"
ta = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/ta.shp"
tf = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tf.shp"
tg = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tg.shp"
tl = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tl.shp"
tm = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tm.shp"
tq = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tq.shp"
tr = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tr.shp"
tv = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland/AreasLiDAREng/tv.shp"

#**************************************************************************************************************
# Areas LiDAR of Wales.  They are in the same shp, in the 2018 version they will be merge with the England ones in order to avoid too much information
#**************************************************************************************************************

wLiD = "/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/WalesLiDAR1km.shp"

#**************************************************************************************************************

# some parameters 

gpSHP = geopandas.GeoDataFrame.from_file(str(shp))
#gpEM = geopandas.GeoDataFrame.from_file(EnglandMap)
#gpEL = geopandas.GeoDataFrame.from_file(EnglandLiD)
#gpSM = geopandas.GeoDataFrame.from_file(ScotlandMap)
#gpSL = geopandas.GeoDataFrame.from_file(ScotlandLiD)
#gpWM = geopandas.GeoDataFrame.from_file(WalesMap)
gpWL = geopandas.GeoDataFrame.from_file(WalesLiD)

#gpEALi = geopandas.GeoDataFrame.from_file(EnglandArLiD)

Slash = "/"
				

# we get the maps 

if Maps == "y":
    
    print("**************************************")
    print("Working on the Maps")
    
    if Country == "e":
        gpEM = geopandas.GeoDataFrame.from_file(EnglandMap) 
        InterMAPe = geopandas.overlay(gpEM,gpSHP, how='intersection') # intersection of the shp and the map grid
        InterMAPeL = InterMAPe['TILE_NAME'].tolist()
        InterMAPeL2 = [] # new list to remove the repeated elements from the intersection 
        for i in InterMAPeL:
           if i not in InterMAPeL2:
               InterMAPeL2.append(i)
        for k in InterMAPeL2: # we set the proper folder where to look for the files needed, choose them, and copy them in our workspace 
            preMap = k[:2]
            FolderMap = EDYMaps + Slash + preMap
            os.chdir(FolderMap)
            mapF = k + ".tif"
            FinalMap = glob.glob(mapF)
            shutil.copy(FinalMap[0],FolMaps)
            
    elif Country == "s":
        gpSM = geopandas.GeoDataFrame.from_file(ScotlandMap)
        InterMAPe = geopandas.overlay(gpSM,gpSHP, how='intersection')
        InterMAPeL = InterMAPe['TILE_NAME'].tolist()
        InterMAPeL2 = []
        for i in InterMAPeL:
           if i not in InterMAPeL2:
               InterMAPeL2.append(i)
        for k in InterMAPeL2:
            preMap = k[:2]
            FolderMap = EDYMaps + Slash + preMap
            os.chdir(FolderMap)
            mapF = k + ".tif"
            FinalMap = glob.glob(mapF)
            shutil.copy(FinalMap[0],FolMaps)
            
    elif Country == "w":
        gpWM = geopandas.GeoDataFrame.from_file(WalesMap)
        InterMAPe = geopandas.overlay(gpWM,gpSHP, how='intersection')
        InterMAPeL = InterMAPe['TILE_NAME'].tolist()
        InterMAPeL2 = []
        for i in InterMAPeL:
           if i not in InterMAPeL2:
               InterMAPeL2.append(i)
        for k in InterMAPeL2:
            preMap = k[:2]
            FolderMap = EDYMaps + Slash + preMap
            os.chdir(FolderMap)
            mapF = k + ".tif"
            FinalMap = glob.glob(mapF)
            shutil.copy(FinalMap[0],FolMaps)
            
    else:
        print("You have not chosen a proper country.")
        
    print("**************************************")
    print("You have the basemaps in their folder")     
    print("**************************************") 
    
# we get the LiDARs

if LiD == "y":
    
    print("**************************************")
    print("Working on the LiDARs")
    
    if Country == "e":
        gpEALi = geopandas.GeoDataFrame.from_file(EnglandArLiD)
        InterLiDArEng = geopandas.overlay(gpEALi,gpSHP, how='intersection')
        InterLiDArEngL = InterLiDArEng['Area'].tolist()
        InterLiDArEngL2 =[]
        for i in InterLiDArEngL:
            if i not in InterLiDArEngL2:
                ilw = i.lower()
                InterLiDArEngL2.append(ilw)
        for kf in InterLiDArEngL2:
            os.chdir("/net/O/0000_ElectronicLibrary/Data/Mapping/SHPScriptMapsLiDARs/ZonesEngland")
            AreZone = kf + ".shp"
            gpEng = geopandas.GeoDataFrame.from_file(AreZone)
            InterLiDST = geopandas.overlay(gpEng,gpSHP, how='intersection')
            InterLiDSTL = InterLiDST['PLAN_NO'].tolist()
            InterLiDSTL2 = []
            for l in InterLiDSTL:
                if l not in InterLiDSTL2:
                    InterLiDSTL2.append(l)
                    for h in InterLiDSTL2:
                        folH = h[:2]
                        folHl = folH.lower()
                        FolderLiD = EDYLiDAR + Slash + folHl
                        os.chdir(FolderLiD)
                        hLow = h.lower()
                        for f in os.listdir(FolderLiD):
                            LiDAR = glob.glob(f + Slash + hLow + "*")
                            for r in LiDAR:
                                FilLiD = FolderLiD + Slash + r
                                shutil.copy(FilLiD, FolLiD)		
                            
        #os.chdir(FolLiD)
        
        #m1LD = glob.glob("*" + "_DTM_1m" + "*")
        #m2LD = glob.glob("*" + "_DTM_2m" + "*")
                        
        #m1LDl = []
        #for u in m1LD:
        #    h = u[:6]
        #    m1LDl.append(h)
                            
        #m2LDl = []
        #for u in m2LD:
        #    h = u[:6]
        #    m2LDl.append(h)
                            
        #Dif = list(set(m1LDl) & set(m2LDl))
                        
        #Remov = []
        #for u in Dif:
        #    z = u + "_DTM_2m"
        #    Remov.append(z)
            
        #for zx in Remov:
        #    zxs = glob.glob(zx + "*")
        #    for zxc in zxs:
        #        os.remove(zxc)
                            
    elif Country == "w":
        InterLiDArWc = geopandas.overlay(gpWL,gpSHP, how='intersection')
        InterLiDArWcL = InterLiDArWc['PLAN_NO'].tolist()
        InterLiDArWcL2 =[]
        for i in InterLiDArWcL:
            if i not in InterLiDArWcL2:
                InterLiDArWcL2.append(i)
        for h in InterLiDArWcL2:
            folH = h[:2]
            folHl = folH.lower()
            FolderLiD = EDYLiDAR + Slash + folHl
            os.chdir(FolderLiD)
            hLow = h.lower()
            for f in os.listdir(FolderLiD):
                LiDAR = glob.glob(f + Slash + hLow + "*")
                for r in LiDAR:
                    FilLiD = FolderLiD + Slash + r
                    shutil.copy(FilLiD, FolLiD)       
                                                 
                            
        #os.chdir(FolLiD)
        
        #m1LD = glob.glob("*" + "_DTM_1m" + "*")
        #m2LD = glob.glob("*" + "_DTM_2m" + "*")
                        
        #m1LDl = []
        #for u in m1LD:
        #    h = u[:6]
        #    m1LDl.append(h)
                            
        #m2LDl = []
        #for u in m2LD:
        #    h = u[:6]
        #    m2LDl.append(h)
                            
        #Dif = list(set(m1LDl) & set(m2LDl))
                        
        #Remov = []
        #for u in Dif:
        #    z = u + "_DTM_2m"
        #    Remov.append(z)
            
        #for zx in Remov:
        #    zxs = glob.glob(zx + "*")
        #    for zxc in zxs:
        #        os.remove(zxc)
                
    elif Country == "s":
        print("There are no LiDARs for Scotland")
        
    else:
        print("You did not select a proper country")
                
    print("**************************************")
    print("You have the LiDARs in their folder")     
    print("**************************************") 
                
         
if Maps != "y" and LiD != "y":
    print("You have not selected either maps and/or LiDAR.")          
    
print("Done................")       


#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import cartopy
import cartopy.crs as ccrs
import cartopy.geodesic
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


# In[2]:


# You may need this function for computing spherical distance between two point
def great_circle_distance(lon1_deg, lat1_deg, lon2_deg, lat2_deg):
    """
    Return the great-circle spherical distance (in degree) between
    two points (lon1_deg, lat1_deg) and (lon2_deg, lat2_deg) in degree.
    """
    lon1, lat1, lon2, lat2 = np.deg2rad( [lon1_deg, lat1_deg, lon2_deg, lat2_deg] )
    dist = np.arccos( np.sin(lat1) * np.sin(lat2) + np.cos(lat1) * np.cos(lat2) * np.cos(lon1 - lon2) )
    return np.rad2deg(dist)


# Lab 1: Locating earthquakes Part 1
# =====
# 

# Use Seismic Analysis Tool (`SAC`) to read in 3 components of seismograms for each of the stations in the `EQ1` directory.  **Examine all 3 components** of recorded ground motion (velocity, but please note that the vertical axes of seismograms are expressed in counts).
# 
# For each station, **estimate the time at which the P and S waves arrive**. You will use `ppk` to pick and `wh` to store the time. The P wave will be the first prominent arrival on the vertical component; the S wave should be the first prominent arrival showing on both horizontals that typically has smaller (or negligible) amplitude on the vertical component.  Pick the P wave on the vertical (BHZ) component and the S wave on one of the horizontal components (BHN or BHE).  Calculate the difference in arrival times (“S-P time”).  **Complete columns 2-4 of the accompanying table for the stations that are given to you**.  Be aware that other phases may arrive before the S (such as PP), which may lead to identification issues.
# 
# 
# | Station | P arrival time | S arrival time | S-P (seconds) | Distance (degrees) | Origin time |
# |---------|:--------------:|:--------------:|:-------------:|:------------------:|:-----------:|
# |   ENH   | 444.16         |  749.16        | 305           |  32               |  2019-01-06 17:27:23.699000 |
# |   XAN   |                |                |               |                    |             |
# |   NWAO  |                |                |               |                    |             |
# |   ...   |                |                |               |                    |             |

# ![](./sac_time.png)

# In[35]:


# Step 1.1
# Please run SAC in terminal and pick P, S wave for recordings at each station
# Then compute the time difference between P and S waves

# For example we measure the tdiff = 305.0s for ENH station


# In[36]:


# The function for inverting distance and P traveltime by providing a measured time difference
tmp = np.loadtxt('EQ1/timetable.txt')
ref_distance = tmp[:,0]
ref_tp = tmp[:,1]
ref_ts = tmp[:,2]
ref_tdiff = tmp[:,3]
def get_distance(tdiff, flag_plot=False):
    """
    Return the distance and P traveltime by providing a measured time difference
    """
    v = np.abs(ref_tdiff - tdiff)
    idx = np.argmin(v)
    dist = ref_distance[idx]
    tp = ref_tp[idx]
    if flag_plot:
        plt.plot(ref_distance, ref_tdiff, color='k', label='Theoretical time differences')
        plt.plot([0, 90], [tdiff, tdiff], color='b', label='Measured time difference')
        plt.plot([dist], [tdiff], 'o', color='r')
        plt.xlim([0, 90])
        plt.ylim([0, 700])
        plt.xlabel('Distance ($\degree$)')
        plt.ylabel('Time (s)')
        plt.legend()
    return dist, tp


# In[37]:


# Step 1.2
# We can invert the distance for the measurement at the station ENH, and plot for how to invert it
get_distance(305.0, True)


# In[38]:


# We can also invert the origin time
# For ENH recordings, the inverted P traveltime is 380.48 s.
# The reference picked P arrival time in 444.16 s, and the reference time for ENH recordings is 2019-01-06T17:26:20.019000
# So we can invert the origin time
ot = datetime(2019, 1, 6, 17, 26, 20, 19000)+timedelta(seconds=444.16) - timedelta(seconds=380.48)
print(ot)


# In[42]:


# Step 1.3
# We can invert for all measurements without plotting

# For example we measure the tdiff = 305.0s for ENH station, 482.1s for NIL station, 486.2s for YAK station
# We can form our dataset:
measurements = { 'ENH': {'stlo': 109.494, 'stla': 30.2762, 'tp': 444.16, 'ts':  749.16, 'reference_time': datetime(2019, 1, 6, 17, 26, 20, 19000) },
                 'NIL': {'stlo': 73.2686, 'stla': 33.6506, 'tp': 654.65, 'ts': 1130.29, 'reference_time': datetime(2019, 1, 6, 17, 26, 20, 19000) },
                 'YAK': {'stlo': 129.680, 'stla': 62.0310, 'tp': 658.36, 'ts': 1145.47, 'reference_time': datetime(2019, 1, 6, 17, 26, 20, 19000) },
               }

for stnm, v in measurements.items():
    dist, p_travel_time = get_distance(v['ts']-v['tp'], False)
    v['dist'] = dist
    v['origin_time'] = v['reference_time'] + timedelta(seconds=v['tp']) - timedelta(seconds=p_travel_time)
    print(stnm, v['dist'], v['origin_time'])


# 
# **Construct a map** (directions follow) with a circle of constant radius (equal to the source-receiver distance) drawn around each station. All the circles should intersect at approximately one point. If any of the circles are inconsistent with the solution, go back and check your first steps for the appropriate station. 

# In[43]:


fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=160.0))

# make the map global rather than have it zoom in to
# the extents of any plotted data
ax.set_global()
ax.coastlines()
app = cartopy.geodesic.Geodesic()
for stnm, v in measurements.items():
    stlo, stla, dist = v['stlo'], v['stla'], v['dist']
    line, = ax.plot(stlo, stla, '^', markersize=12, label=stnm, transform=ccrs.PlateCarree() )
    radius_in_meter = dist*111195 # convert degree to meter
    circle_points = app.circle(lon=stlo, lat=stla, radius=radius_in_meter, n_samples=3000, endpoint=True)
    ax.plot(circle_points[:,0], circle_points[:,1], '.', color=line.get_color(), markersize=1, transform=ccrs.PlateCarree())

ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle=':')
ax.legend(loc='lower left')

# well, in the generate figure, the circles intersect. The intersection point is the inverted location for the earthquake.
# 


# If the solution looks good, plot a closer view of the region around the epicentre and estimate as accurately as possible the coordinates of the earthquake. One way to do this is to find the point on the map that minimizes the sum of the distances (L1 norm) or distances squared (L2 norm) between the selected point and each of the circles. Write the estimated longitude and latitude on the lines of the attached table.

# In[44]:


fig = plt.figure(figsize=(12, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=160.0))

ax.coastlines()
app = cartopy.geodesic.Geodesic()
for stnm, v in measurements.items():
    stlo, stla, dist = v['stlo'], v['stla'], v['dist']
    line, = ax.plot(stlo, stla, '^', markersize=12, label=stnm, transform=ccrs.PlateCarree() )
    radius_in_meter = dist*110000 # convert degree to meter
    circle_points = app.circle(lon=stlo, lat=stla, radius=radius_in_meter, n_samples=1000, endpoint=True)
    ax.plot(circle_points[:,0], circle_points[:,1], '-', color=line.get_color(), markersize=3, transform=ccrs.PlateCarree())

ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.5, color='gray', alpha=0.5, linestyle=':')
ax.legend(loc='lower left')
ax.set_extent([120, 135, -5, 10], crs=ccrs.PlateCarree())

# The generated Figure presents a closer view. It shows the imperfection of the result. 
# The circles do not intersect at a single point!
#
# Think about a way find the point on the map that minimizes the sum of the distances (L1 norm) or 
# distances squared (L2 norm) between the selected point and each of the circles.
# Write the estimated longitude and latitude on the lines of the attached table.


# Please submit the following:
# 
# - [ ] the table you completed during the exercise,
# - [ ] the maps.
# - [ ] a short summary detailing your thought process regarding picking any difficult phases and how the epicentral location could be improved by this method.

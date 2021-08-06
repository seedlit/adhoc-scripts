from whitebox.whitebox_tools import WhiteboxTools



wbt = WhiteboxTools()
in_path = "/home/naman/Desktop/side_projects/data/dsm-all/2/dsm-000077_000048-20cm.tif"
dsm_path = "/home/naman/Desktop/side_projects/dsm_shadow/data/dem_clipped.tif"
out_path = "/home/naman/Desktop/side_projects/dsm_shadow/data/hillshade_test.tif"
shadow_out_path = "/home/naman/Desktop/side_projects/dsm_shadow/data/time_in_daylight.tif"

# wbt.hillshade(
#     in_path, 
#     out_path, 
#     azimuth=315.0, 
#     altitude=30.0, 
#     zfactor=None,     
# )

# shadow test
# wbt.horizon_angle(
#     in_path, 
#     shadow_out_path, 
#     azimuth=180.0,   
#     # max_dist=0.2           
# )


# # time in day light
wbt.time_in_daylight(
    in_path, 
    shadow_out_path, 
    80, 
    20, 
    az_fraction=10.0, 
    max_dist=100.0, 
    utc_offset="00:00", 
    start_day=1, 
    end_day=100, 
    start_time="00:00:00", 
    end_time="23:59:59",     
)


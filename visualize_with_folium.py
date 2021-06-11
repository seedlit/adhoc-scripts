import os
import webbrowser
import folium


if __name__ == "__main__":

    # Define the center of our map.
    lat, lon = 45.77, 4.855
    my_map = folium.Map(location=[lat, lon], zoom_start=10)

    # to visualize
    filepath = "test_folium.html"
    my_map.save(filepath)
    webbrowser.open("file://" + filepath)

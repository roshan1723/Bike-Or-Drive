
from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap

#converts an adress into lat/lon coordinates
def geocode(adress):
  from pprint import pprint
  import googlemaps
  from datetime import datetime

  gmaps = googlemaps.Client(key='AIzaSyDyN3dz5nCdN_yU0jgFVgvPOvT5WYMzKPI')

  # Geocoding an address
  geocode_result = gmaps.geocode(adress)
  try:
    for key in geocode_result:
        latitude = key['geometry']['bounds']['northeast']['lat']
        longitude = key['geometry']['bounds']['northeast']['lng']
  except:
    for key in geocode_result:
        latitude = key['geometry']['location']['lat']
        longitude = key['geometry']['location']['lng']
  return (latitude, longitude)

#starting point adress
centerCoord = geocode('275 Joe Routt Blvd, College Station')

output_file("gmap.html")
# lat=30.6139183, lng=-96.3460636
map_options = GMapOptions(lat = centerCoord[0], lng = centerCoord[1], map_type="roadmap", zoom=15)

#personal API key:
p = gmap("AIzaSyDyN3dz5nCdN_yU0jgFVgvPOvT5WYMzKPI", map_options, title="Memorial Student Center")

#Polygon coordinates
cscoords = [[30.6139183,-96.3460636],[30.613575,-96.3458061],[30.6128883,-96.3451195],[30.6128883,-96.3447762],[30.6132317,-96.3444328],[30.6134033,-96.3439178],[30.6132317,-96.3434029],[30.6128883,-96.3430595],[30.612545,-96.3420296],[30.6122017,-96.3416862],[30.6122017,-96.3413429],[30.6128883,-96.3406563],[30.6134033,-96.3404846],[30.61409,-96.3404846],[30.6146049,-96.340313],[30.6152916,-96.3396263],[30.6152916,-96.339283],[30.6149483,-96.3389397],[30.6149483,-96.3385963],[30.6152916,-96.338253],[30.6152916,-96.3379097],[30.6147766,-96.337738],[30.61409,-96.337738],[30.613575,-96.3375664],[30.612545,-96.3365364],[30.61203,-96.3363647],[30.611515,-96.3365364],[30.611515,-96.3368797],[30.6118584,-96.3372231],[30.6122017,-96.338253],[30.612545,-96.3385963],[30.612545,-96.3389397],[30.61203,-96.3391113],[30.611515,-96.3389397],[30.6111717,-96.3385963],[30.6101418,-96.338253],[30.6097984,-96.3372231],[30.6091118,-96.3365364],[30.6080818,-96.3361931],[30.6077385,-96.3358498],[30.6073952,-96.3358498],[30.6072235,-96.3363647],[30.6073952,-96.3368797],[30.6077385,-96.3372231],[30.6080818,-96.338253],[30.6087685,-96.3389397],[30.6097984,-96.339283],[30.6101418,-96.3396263],[30.6111717,-96.3399696],[30.6113434,-96.3404846],[30.6111717,-96.3409996],[30.6104851,-96.3416862],[30.6099701,-96.3418579],[30.6094551,-96.3416862],[30.6084251,-96.3406563],[30.6073952,-96.340313],[30.6063652,-96.339283],[30.6053352,-96.3389397],[30.6049919,-96.3385963],[30.6046486,-96.3385963],[30.6044769,-96.3391113],[30.6046486,-96.3396263],[30.6053352,-96.340313],[30.6063652,-96.3406563],[30.6091118,-96.3434029],[30.6091118,-96.3437462],[30.6087685,-96.3440895],[30.6085968,-96.3446045],[30.6087685,-96.3451195],[30.6092834,-96.3452911],[30.6097984,-96.3451195],[30.6101418,-96.3447762],[30.6104851,-96.3447762],[30.6122017,-96.3464928],[30.6127167,-96.3466644],[30.6134033,-96.3466644],[30.6139183,-96.3465786],[30.61409,-96.3463211],[30.6139183,-96.3460636]]
lat = []
lon = []
for i in range(len(cscoords)):
    lat.append(cscoords[i][0])
    lon.append(cscoords[i][1])
    
source = ColumnDataSource(
    # data=dict(lat=[30.6139183, 30.613575, 30.6128883],
    #           lon=[-96.3460636, -96.3458061, -96.3451195])
    data = dict(lat = lat, lon = lon)
)

#overlay polygon onto map
p.patch(x="lon", y="lat", fill_color="blue", fill_alpha=0.8, source=source)

show(p)

# print(lat, "\n\n", lon)
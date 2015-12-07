'''
To follow the tilejson spec "tiles":["url","url"]
however, only the first url is used.
'''
import json
def layerTemplate():
	template = """    <!--Layer-->
    <Layer>
      <ows:Title>%(thisDescription)s</ows:Title>
      <ows:Identifier>%(thisName)s</ows:Identifier>
      <ows:WGS84BoundingBox crs="urn:ogc:def:crs:OGC:2:84">
        <ows:LowerCorner>-180 -90</ows:LowerCorner>
        <ows:UpperCorner>180 90</ows:UpperCorner>
      </ows:WGS84BoundingBox>
      <ows:BoundingBox crs="urn:ogc:def:crs:EPSG::3857">
        <ows:LowerCorner>-20037508.34 -20037508.34</ows:LowerCorner>
        <ows:UpperCorner>20037508.34 20037508.34</ows:UpperCorner>
      </ows:BoundingBox>
      <Style isDefault="true">
        <ows:Identifier>default</ows:Identifier>
      </Style>
      <Format>image/%(thisFormat)s</Format>
      <TileMatrixSetLink>
        <TileMatrixSet>GoogleMapsCompatible</TileMatrixSet>
      </TileMatrixSetLink>
      <!-- Check for switched Row/Col if arcgis rest is the source -->
      <ResourceURL format="image/%(thisFormat)s" resourceType="tile" template="%(thisTiles)s"/>
    </Layer>""" 
    	return template

jin = open('tiles.json','r')
tjson = json.load(jin)
jin.close()


theTitle = tjson['title']
theLink = tjson['link']
print theTitle,theLink
for js in tjson['tilejson']:
	theTiles = js['tiles'][0]
  #print theTiles
	if theTiles == None:
		print '"tiles" is a required field'
	zSub = theTiles.replace('{z}','{TileMatrix}')
	xSub = zSub.replace('{x}','{TileCol}')
	ySub = xSub.replace('{y}','{TileRow}')
	args = {}
	args['thisTiles'] = ySub
	args['thisFormat'] = js['format']
	args['thisName'] = js['name']
	args['thisDescription'] = js['description']
	print layerTemplate()%args
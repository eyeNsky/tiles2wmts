import json
def layerTemplate():
	template = '''    <!--Layer-->
    <Layer>
      <ows:Title>%s</ows:Title>
      <ows:Identifier>%s</ows:Identifier>
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
      <Format>image/png</Format>
      <TileMatrixSetLink>
        <TileMatrixSet>GoogleMapsCompatible</TileMatrixSet>
      </TileMatrixSetLink>
      <!-- Note the switched Row/Col -->
      <ResourceURL format="image/%s" resourceType="tile" template="%s"/>
    </Layer>'''

jin = open('tiles.json','r')
tjson = json.load(jin)
jin.close()


for js in tjson:
	# To follow the the tilejson spec "tiles":["url","url"]
	# however, only the first url is used.
	thisTiles = js['tiles'][0]
	print thisTiles
	if thisTiles == None:
		print '"tiles" is a required field'

#Set File Path with Delimited Text Parameters
#path1 = "file:///C:/Users/jas36/Documents/Clark/Year 5/Comp_Prog/Class_Materials/Final/USA_2020_Nov21.csv?type=csv&xField=LONGITUDE&yField=LATITUDE&crs=EPSG:3857"
#path2 = "file:///C:/Users/jas36/Documents/Clark/Year 5/Comp_Prog/Class_Materials/Final/USA_2020_Nov21.csv?delimiter=,&xField=LONGITUDE&yField=LATITUDE&crs=EPSG:3857"
path3 = "file:///{}/Clark/Year 5/Comp_Prog/Class_Materials/Final/USA_2020_Nov21.csv?delimiter={}&xField={}&yField={}&crs={}".format(os.getcwd(), ",", "LONGITUDE", "LATITUDE", "EPSG:3857")

# Use QgsVectorLayer to create a Vector Layer with the csv file
layer1 = QgsVectorLayer(path3, "ACLED_Nov2020", "delimitedtext")

# To Add the Vector Layer as a Map Layer
QgsProject.instance().addMapLayer(layer1)

# To Remove the Map Layer
#QgsProject.instance().removeMapLayer(layer1)

# Output Field Names and Types
for field in layer1.fields():
    print(field.name(), field.typeName())

# To Show the Attribute Table (in another window)
#iface.showAttributeTable(layer1)

# Make our layer the Active Layer and Select by Attributes
layer = iface.activeLayer()
layer.selectByExpression('"ADMIN1"!=\'Alaska\' and "ADMIN1"!=\'Hawaii\' and "EVENT_TYPE"=\'Violence against civilians\'', QgsVectorLayer.SetSelection)

# Create a new layer from Selected Features
layer = iface.activeLayer()
layer2 = layer.materialize(QgsFeatureRequest().setFilterFids(layer.selectedFeatureIds()))
QgsProject.instance().addMapLayer(layer2)

#Export Layer
output_path = "Clark/Year 5/Comp_Prog/Class_Materials/Final/export"
QgsVectorFileWriter.writeAsVectorFormat(layer2, output_path, "utf-8", layer.crs(), 'GeoJSON')

# Change Symbology using iface
layer2.renderer().symbol().setSize(1)
layer2.triggerRepaint()
layer2.renderer().symbol().setColor(QColor("red"))
layer2.triggerRepaint()

# Updates the Table of Contents
iface.layerTreeView().refreshLayerSymbology(layer2.id())

# Use Heatmap Symbology to visualize
heatmap = QgsHeatmapRenderer()
ramp = QgsStyle().defaultStyle().colorRamp('Magma')
heatmap.setColorRamp(ramp)
layer2.setRenderer(heatmap)
layer2.triggerRepaint()

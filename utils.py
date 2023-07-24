from qgis.core import (QgsGeometry, QgsPointXY, QgsCoordinateReferenceSystem,
                        QgsCoordinateTransform, QgsProject)


def geoJson2geom(ft):
    # only for Multipolygon and polygon (for the moment)
    parts = ft['coordinates']
    if ft['type'] == 'Polygon':
        parts = [parts]
    polygons = []
    for polygon in parts:
        rings = []
        for ring in polygon:
            coords = []
            for coord in ring:
                coords.append(QgsPointXY(coord[0], coord[1]))
            rings.append(coords)
        polygons.append(rings)
    geom = QgsGeometry.fromMultiPolygonXY(polygons)
    crs = QgsProject.instance().crs()
    transform = QgsCoordinateTransform(QgsCoordinateReferenceSystem('EPSG:4326'), crs, 
                                        QgsProject.instance().transformContext())
    geom.transform(transform)
    return geom

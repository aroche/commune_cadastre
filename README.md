# Commune cadastre France plugin

This is a QGIS plugin to search for a commune and a parcelle in the French cadastre. 
It uses the French Cadastre and Geo API from IGN and the French government. https://api.gouv.fr/documentation/api_carto_cadastre

## Usage

The plugin appears as a dock widget on QGIS.

First search for a commune by typing a few letters and select it in the suggestions.

Then select the section

Then type the parcelle number and click "Rechercher". The download can take a while. 
If the parcelle is found, the map zooms to it and the contour of the parcelle is shown as a blue line.

If the section or the number are not entered, you can click on "Rechercher" to zoom to the commune outline and display it.


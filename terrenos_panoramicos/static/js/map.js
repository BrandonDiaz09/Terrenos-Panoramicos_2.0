const osm = "https://www.osm.org/copyright";
const copy = `&copy; <a href="${osm}">OpenStreetMap</a>`;
const url = "https://{s}.tile.osm.org/{z}/{x}/{y}.png";
const layer = L.tileLayer(url, { attribution: copy });
const map = L.map("map", { layers: [layer] });
map.fitWorld();

const data = document.getElementById("markers-data");
let feature = L.geoJSON(JSON.parse(data.textContent))
    .bindPopup(function (layer) {
        return layer.feature.properties.name;
    })
    .addTo(map);
map.fitBounds(feature.getBounds());

document.addEventListener('DOMContentLoaded', function () {
    //console.log(miDato); // aquí tienes acceso a la variable pasada desde Django
});
const osm = "https://www.osm.org/copyright";
const copy = `&copy; <a href="${osm}">OpenStreetMap</a>`;
const url = "https://{s}.tile.osm.org/{z}/{x}/{y}.png";
var mapa = L.map("contenedor-del-mapa").setView([19.269335641455235, -99.45479492275484], 11)
L.tileLayer(url, {}).addTo(mapa)
const map = L.map("map", { layers: [layer] });
map.fitWorld();

const data = miDato;
let feature = L.geoJSON(JSON.parse(data.textContent))
    .bindPopup(function (layer) {
        return layer.feature.properties.name;
    })
    .addTo(map);
map.fitBounds(feature.getBounds());




// var marcador = L.marker([4.6281045, -74.0654527]).addTo(mapa)
// marcador.bindPopup("Hola GeoCositas")

// const circulo = L.circle([4.613573, -74.063889], {
//     radius: 1000,
//     color: "green"
// }).addTo(mapa)
// circulo.bindPopup("Programación en SIG")

function clicSobreMapa(evento) {
    alert("Diste clic en el punto con coordenadas latitud: " + evento.latlng.lat + " y longitud: " + evento.latlng.lng)
}

mapa.on("click", clicSobreMapa);

console.log(mapa)
console.log(marcador)
console.log(circulo)
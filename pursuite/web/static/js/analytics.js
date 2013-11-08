function render_map(year, map_type, static_url) {
  function initialize() {
    proj.scale(7000);
    proj.translate([-1310, 750]);
  }

  var width = 600;
  var height = 600;
  var proj = d3.geo.mercator();
  var path = d3.geo.path().projection(proj);
  var trans = proj.translate();
  var scale = proj.scale();

  var map = d3.select("#india-map").append("svg:svg")
      .attr("width", width)
      .attr("height", height)
      .call(initialize);
  var stats = d3.select("#stats");
  var india = map.append("svg:g")
      .attr("id", "india");

  d3.json(static_url + "/states.json", function (json) {
    india.selectAll("path")
        .data(json.features)
        .enter().append("path")
        .attr("d", path)
        .attr("class", "state")
        .on("click", function(d, i){
          d3.selectAll("path").classed("selected", false);
          d3.select(this).classed("selected", true);
          render_chart(year, states_map[d.id], 'chart-container');
        })
        .on("mouseover", function(d, i){
          d3.select(this).classed("hover", true);
        })
        .on("mouseout", function(d, i){
          d3.select(this).classed("hover", false);
        });
  });
  setTimeout(function() {
    d3.json("../data/" + map_type + "/" + year, function(json) {
      data = json[map_type + '_data'];
      states_map = json['states'];
      india.selectAll("path").style("opacity", quantize);
    });
  }, 100);
}

function quantize(d, i) {
  d['wealth'] = data[d.id];
  return Math.floor(d.wealth/10)/10;
}

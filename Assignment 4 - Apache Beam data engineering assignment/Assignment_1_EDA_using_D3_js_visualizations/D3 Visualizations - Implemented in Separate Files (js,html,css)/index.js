// Bar Chart: SaleCondition vs. Average SalePrice
d3.csv("./avg_sale_price.csv").then((data) => {
  const margin = { top: 20, right: 20, bottom: 60, left: 60 },
    width = 600 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  const svg = d3
    .select("#chart1")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const x = d3.scaleBand().range([0, width]).padding(0.4);
  const y = d3.scaleLinear().range([height, 0]);

  x.domain(data.map((d) => d.SaleCondition));
  y.domain([0, d3.max(data, (d) => d.SalePrice)]);

  svg
    .append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  svg.append("g").call(d3.axisLeft(y));

  svg
    .selectAll(".bar")
    .data(data)
    .enter()
    .append("rect")
    .attr("class", "bar")
    .attr("x", (d) => x(d.SaleCondition))
    .attr("y", (d) => y(d.SalePrice))
    .attr("width", x.bandwidth())
    .attr("height", (d) => height - y(d.SalePrice));
});

// Scatter Plot: GrLivArea vs. SalePrice
d3.csv("./scatter_data.csv").then((data) => {
  const margin = { top: 20, right: 20, bottom: 60, left: 60 },
    width = 600 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;

  const svg = d3
    .select("#chart2")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  const x = d3.scaleLinear().range([0, width]);
  const y = d3.scaleLinear().range([height, 0]);

  x.domain([0, d3.max(data, (d) => +d.GrLivArea)]);
  y.domain([0, d3.max(data, (d) => +d.SalePrice)]);

  svg
    .append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  svg.append("g").call(d3.axisLeft(y));

  svg
    .selectAll(".dot")
    .data(data)
    .enter()
    .append("circle")
    .attr("class", "dot")
    .attr("cx", (d) => x(+d.GrLivArea))
    .attr("cy", (d) => y(+d.SalePrice))
    .attr("r", 3);
});

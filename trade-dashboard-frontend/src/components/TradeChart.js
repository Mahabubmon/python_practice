import React from "react";
import {
  LineChart,
  Line,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
} from "recharts";

function TradeChart({ trades }) {
  return (
    <div>
      <LineChart width={600} height={300} data={trades}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis yAxisId="left" />
        <YAxis yAxisId="right" orientation="right" />
        <Tooltip />
        <Legend />
        <Line yAxisId="left" type="monotone" dataKey="close" stroke="#8884d8" />
        <Bar yAxisId="right" dataKey="volume" fill="#82ca9d" />
      </LineChart>
    </div>
  );
}

export default TradeChart;

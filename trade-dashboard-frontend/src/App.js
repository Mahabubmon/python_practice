import React, { useEffect, useState } from "react";
import axios from "axios";
import TradeTable from "./components/TradeTable";
import TradeChart from "./components/TradeChart";

function App() {
  const [trades, setTrades] = useState([]);
  const [selectedTradeCode, setSelectedTradeCode] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:5000/trades")
      .then((response) => setTrades(response.data))
      .catch((error) => console.error(error));
  }, []);

  const updateTrade = (id, updatedTrade) => {
    axios
      .put(`http://localhost:5000/trades/${id}`, updatedTrade)
      .then((response) => {
        setTrades(
          trades.map((trade) => (trade.id === id ? response.data : trade))
        );
      })
      .catch((error) => console.error(error));
  };

  const handleTradeCodeChange = (e) => {
    setSelectedTradeCode(e.target.value);
  };

  return (
    <div>
      <TradeChart
        trades={trades.filter(
          (trade) => trade.trade_code === selectedTradeCode
        )}
      />
      <select onChange={handleTradeCodeChange} value={selectedTradeCode}>
        <option value="">Select Trade Code</option>
        {Array.from(new Set(trades.map((trade) => trade.trade_code))).map(
          (code) => (
            <option key={code} value={code}>
              {code}
            </option>
          )
        )}
      </select>
      <TradeTable trades={trades} updateTrade={updateTrade} />
    </div>
  );
}

export default App;

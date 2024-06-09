import React from "react";

function TradeTable({ trades, updateTrade }) {
  const handleInputChange = (id, field, value) => {
    const updatedTrade = trades.find((trade) => trade.id === id);
    updatedTrade[field] = value;
    updateTrade(id, updatedTrade);
  };

  return (
    <table>
      <thead>
        <tr>
          <th>Date</th>
          <th>Trade Code</th>
          <th>Open</th>
          <th>High</th>
          <th>Low</th>
          <th>Close</th>
          <th>Volume</th>
        </tr>
      </thead>
      <tbody>
        {trades.map((trade) => (
          <tr key={trade.id}>
            <td>{trade.date}</td>
            <td>{trade.trade_code}</td>
            <td>
              <input
                type="number"
                value={trade.open}
                onChange={(e) =>
                  handleInputChange(
                    trade.id,
                    "open",
                    parseFloat(e.target.value)
                  )
                }
              />
            </td>
            <td>
              <input
                type="number"
                value={trade.high}
                onChange={(e) =>
                  handleInputChange(
                    trade.id,
                    "high",
                    parseFloat(e.target.value)
                  )
                }
              />
            </td>
            <td>
              <input
                type="number"
                value={trade.low}
                onChange={(e) =>
                  handleInputChange(trade.id, "low", parseFloat(e.target.value))
                }
              />
            </td>
            <td>
              <input
                type="number"
                value={trade.close}
                onChange={(e) =>
                  handleInputChange(
                    trade.id,
                    "close",
                    parseFloat(e.target.value)
                  )
                }
              />
            </td>
            <td>
              <input
                type="number"
                value={trade.volume}
                onChange={(e) =>
                  handleInputChange(
                    trade.id,
                    "volume",
                    parseInt(e.target.value)
                  )
                }
              />
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
}

export default TradeTable;

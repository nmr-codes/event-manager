import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./index.css"; // global CSS, agar bo‘lsa

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

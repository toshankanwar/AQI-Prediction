import React, { useState, useEffect } from "react";
import { Link, useLocation } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  const [open, setOpen] = useState(false);
  const location = useLocation();

  useEffect(() => {
    setOpen(false); // close menu on route change
  }, [location.pathname]);

  return (
    <header className="navbar-wrapper">
      <div className="navbar">
        <div className="logo">🌿 AQI Predictor</div>
        <nav className={`nav-links ${open ? "open" : ""}`}>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
        </nav>
        <button className="menu-toggle" onClick={() => setOpen(!open)}>
          {open ? "✖" : "☰"}
        </button>
      </div>
    </header>
  );
}

export default Navbar;

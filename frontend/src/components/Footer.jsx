
import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <div className="footer-container">
        <p className="footer-text">
          &copy; {new Date().getFullYear()} AQI Predictor. All rights reserved.
        </p>
        <p className="footer-designer">
          Designed and developed by{" "}
          <a
            href="https://github.com/toshankanwar"  // 🔁 Replace with your desired link
            target="_blank"
            rel="noopener noreferrer"
          >
            Toshan Kanwar
          </a>
        </p>
      </div>
    </footer>
  );
}

export default Footer;


<<<<<<< HEAD
import React from "react";
import "../App.css";
import "./About.css";
import { Helmet } from "react-helmet";

function About() {
  return (
    <div className="page-container">
      <Helmet>
        <title>About | AQI Predictor</title>
      </Helmet>

      <div className="about-container">
        <div className="about-content">
          <h1 className="about-title">📚 About This Project</h1>
          <p>
            This AQI Prediction Web App leverages real-world air quality data collected between <strong>2019 to 2023</strong> across major Indian cities.
          </p>
          <p>
            It uses a <strong>deep learning model (LSTM)</strong> that understands seasonal and historical pollution patterns to predict future AQI values.
          </p>

          <p><strong>Model Highlights:</strong></p>
          <ul>
            <li>✓ Trained on city-wise AQI datasets</li>
            <li>✓ Takes date and city as inputs</li>
            <li>✓ Outputs predicted AQI level in real time</li>
          </ul>

          <p><strong>Data Source:</strong> 🔗 <a href="https://urbanemissions.info/india-air-quality/india-ncap-aqi-indian-cities-2015-2023/" target="_blank" rel="noopener noreferrer">
                Urban Emissions Website
              </a></p>
          <p>
            This tool aims to promote awareness about air quality and help citizens make informed decisions.
          </p>

          <hr className="about-divider" />

          <h2 className="about-subtitle">📊 Dataset Details</h2>
          <p>
            The dataset contains historical AQI values for over 277 major Indian cities from January 2019 to December 2023. Each record includes:
          </p>
          <ul>
            <li>✓ City Name</li>
            <li>✓ Date of Observation</li>
            <li>✓ AQI Value</li>
            <li>✓ Primary Pollutant</li>
            <li>✓ AQI Category (Good, Satisfactory, Moderate, etc.)</li>
          </ul>
          <p>
            Data was preprocessed to remove null values, normalize date formats, and handle missing AQI entries using interpolation.
          </p>

          <hr className="about-divider" />

          <h2 className="about-subtitle">💻 GitHub Repositories</h2>
          <p>You can explore the full project on GitHub:</p>
          <ul>
            <li>
              🔗 <a href="https://github.com/toshankanwar/AQI-Prediction/tree/main/backend" target="_blank" rel="noopener noreferrer">
                Backend (Flask + LSTM Model)
              </a>
            </li>
            <li>
              🔗 <a href="https://github.com/toshankanwar/AQI-Prediction/tree/main/frontend" target="_blank" rel="noopener noreferrer">
                Frontend (React + CSS3)
              </a>
            </li>
          </ul>

          <hr className="about-divider" />

          <h2 className="about-subtitle">📬 Contact</h2>
          <p>
            Have feedback or want to collaborate? Feel free to reach out:
          </p>
          <ul>
            <li>📧 Email: <a href="mailto:contact@toshankanwar.website/">contact@toshankanwar.website</a></li>
          </ul>
        </div>
      </div>
    </div>
  );

}

export default About;
=======
import React from "react";
import "../App.css";
import "./About.css";
import { Helmet } from "react-helmet";

function About() {
  return (
    <div className="page-container">
      <Helmet>
        <title>About | AQI Predictor</title>
      </Helmet>

      <div className="about-container">
        <div className="about-content">
          <h1 className="about-title">📚 About This Project</h1>
          <p>
            This AQI Prediction Web App leverages real-world air quality data collected between <strong>2019 to 2023</strong> across major Indian cities.
          </p>
          <p>
            It uses a <strong>deep learning model (LSTM)</strong> that understands seasonal and historical pollution patterns to predict future AQI values.
          </p>

          <p><strong>Model Highlights:</strong></p>
          <ul>
            <li>✓ Trained on city-wise AQI datasets</li>
            <li>✓ Takes date and city as inputs</li>
            <li>✓ Outputs predicted AQI level in real time</li>
          </ul>

          <p><strong>Data Source:</strong> 🔗 <a href="https://urbanemissions.info/india-air-quality/india-ncap-aqi-indian-cities-2015-2023/" target="_blank" rel="noopener noreferrer">
                Urban Emissions Website
              </a></p>
          <p>
            This tool aims to promote awareness about air quality and help citizens make informed decisions.
          </p>

          <hr className="about-divider" />

          <h2 className="about-subtitle">📊 Dataset Details</h2>
          <p>
            The dataset contains historical AQI values for over 277 major Indian cities from January 2019 to December 2023. Each record includes:
          </p>
          <ul>
            <li>✓ City Name</li>
            <li>✓ Date of Observation</li>
            <li>✓ AQI Value</li>
            <li>✓ Primary Pollutant</li>
            <li>✓ AQI Category (Good, Satisfactory, Moderate, etc.)</li>
          </ul>
          <p>
            Data was preprocessed to remove null values, normalize date formats, and handle missing AQI entries using interpolation.
          </p>

          <hr className="about-divider" />

          <h2 className="about-subtitle">💻 GitHub Repositories</h2>
          <p>You can explore the full project on GitHub:</p>
          <ul>
            <li>
              🔗 <a href="https://github.com/toshankanwar/AQI-Prediction/tree/main/backend" target="_blank" rel="noopener noreferrer">
                Backend (Flask + LSTM Model)
              </a>
            </li>
            <li>
              🔗 <a href="https://github.com/toshankanwar/AQI-Prediction/tree/main/frontend" target="_blank" rel="noopener noreferrer">
                Frontend (React + CSS3)
              </a>
            </li>
          </ul>

          <hr className="about-divider" />

          <h2 className="about-subtitle">📬 Contact</h2>
          <p>
            Have feedback or want to collaborate? Feel free to reach out:
          </p>
          <ul>
            <li>📧 Email: <a href="mailto:contact@toshankanwar.website/">contact@toshankanwar.website</a></li>
          </ul>
        </div>
      </div>
    </div>
  );

}

export default About;
>>>>>>> ea27301 (git add)

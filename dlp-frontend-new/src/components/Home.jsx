import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css';

function Home() {
  return (
    <div className="home-container">
      <div className="home-content">
        <div className="hero-section">
          <div className="shield-icon">🛡️</div>
          <h1 className="neon-title">
            <span className="neon-text">DLP SYSTEM</span>
          </h1>
          <p className="neon-subtitle">DATA LOSS PREVENTION</p>
          <p className="hero-description">
            Advanced AI-powered system to detect and protect sensitive information in real-time
          </p>
          
          <div className="cta-buttons">
            <Link to="/login" className="neon-btn primary">
              <span>LOGIN</span>
            </Link>
            <Link to="/register" className="neon-btn secondary">
              <span>REGISTER</span>
            </Link>
          </div>
        </div>

        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon">🔍</div>
            <h3>Real-time Scanning</h3>
            <p>Detect PII instantly with hybrid AI detection engine</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🎯</div>
            <h3>High Accuracy</h3>
            <p>95%+ confidence with regex + NLP hybrid engine</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">📊</div>
            <h3>Analytics Dashboard</h3>
            <p>Monitor threats with real-time insights and charts</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon">🔒</div>
            <h3>Secure & Private</h3>
            <p>Enterprise-grade security with JWT authentication</p>
          </div>
        </div>

        <div className="stats-section">
          <div className="stat-item">
            <h2 className="neon-number">10+</h2>
            <p>PII Types Detected</p>
          </div>
          <div className="stat-item">
            <h2 className="neon-number">95%</h2>
            <p>Detection Accuracy</p>
          </div>
          <div className="stat-item">
            <h2 className="neon-number">24/7</h2>
            <p>Real-time Protection</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Home;

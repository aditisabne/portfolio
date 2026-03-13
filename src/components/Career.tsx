import "./styles/Career.css";

const Career = () => {
  return (
    <div className="career-section section-container">
      <div className="career-container">
        <h2>
          My Education <span>&</span>
          <br /> Achievements
        </h2>
        <div className="career-info">
          <div className="career-timeline">
            <div className="career-dot"></div>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>B.Tech in Electronics and Computer Science</h4>
                <h5>PVPIT Budhgaon</h5>
              </div>
              <h3>2022-26</h3>
            </div>
            <p>
              CGPA: 6.05. Strong focus on software engineering, data structures, and machine learning principles along with hands-on IoT projects.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Hackathons & Competitions</h4>
                <h5>National & Regional Level</h5>
              </div>
              <h3>2025</h3>
            </div>
            <p>
              • Winner – Smart Cops Hackathon 2025, Sangli Cyber Police: Designed and developed an AI-Powered Women Safety Companion Chatbot that provides emotional support, real time tracking, and a secure emergency alert system.<br/>
              • Nirmiti 2025 – Electro-Mania (National Level): Secured Second Prize in a multi-round technical competition involving General Aptitude, C Programming, and digital logic hardware testing using ICs.
            </p>
          </div>
          <div className="career-info-box">
            <div className="career-info-in">
              <div className="career-role">
                <h4>Earlier Education</h4>
                <h5>HSC & SSC</h5>
              </div>
              <h3>2020-22</h3>
            </div>
            <p>
              • SSC from St. Alphonsa School, Miraj (98.20%)<br/>
              • HSC from Nav Krishna Valley School, Sangli (66.5%)
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Career;

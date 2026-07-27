import "./FeatureCard.css";

export default function FeatureCard({ title, description, icon }) {
    return (
        <div className="feature-card">

            <div className="feature-icon">
                {icon}
            </div>

            <h3>{title}</h3>

            <p>{description}</p>

        </div>
    );
}
import "./Navbar.css";
import { FaBookOpen } from "react-icons/fa";

export default function Navbar() {
    return (
        <nav className="navbar">
            <div className="navbar-logo">
                <FaBookOpen className="logo-icon" />
                <span>Research Paper Assistant</span>
            </div>

            <div className="navbar-right">
                <span>Powered by Azure AI</span>
            </div>
        </nav>
    );
}
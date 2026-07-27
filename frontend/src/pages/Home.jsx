import "./Home.css";

import Navbar from "../components/Navbar/Navbar";
import UploadCard from "../components/UploadCard/UploadCard";
import FeatureCard from "../components/FeatureCard/FeatureCard";
import Footer from "../components/Footer/Footer";

import {
    FaRobot,
    FaQuestionCircle,
    FaClipboardList,
    FaLightbulb
} from "react-icons/fa";

export default function Home(){

    return(

        <>

            <Navbar/>

            <UploadCard/>

            <section className="features">

                <FeatureCard

                    icon={<FaRobot/>}

                    title="AI Summary"

                    description="Generate concise summaries of lengthy research papers."

                />

                <FeatureCard

                    icon={<FaQuestionCircle/>}

                    title="Ask Questions"

                    description="Ask natural language questions about any uploaded paper."

                />

                <FeatureCard

                    icon={<FaClipboardList/>}

                    title="Generate Quiz"

                    description="Create MCQs for self-assessment."

                />

                <FeatureCard

                    icon={<FaLightbulb/>}

                    title="Explain Concepts"

                    description="Understand difficult concepts in simple language."

                />

            </section>

            <Footer/>

        </>

    );

}
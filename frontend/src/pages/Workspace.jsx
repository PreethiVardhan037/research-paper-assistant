import "./Workspace.css";

import Navbar from "../components/Navbar/Navbar";
import Footer from "../components/Footer/Footer";

import AskCard from "../components/AskCard/AskCard";
import SummaryCard from "../components/SummaryCard/SummaryCard";
import QuizCard from "../components/QuizCard/QuizCard";

import { getCurrentPaper } from "../services/api";

import { useNavigate } from "react-router-dom";
import { useState,useEffect } from "react";

export default function Workspace() {

    const [currentPaper,setCurrentPaper] = useState("")

    useEffect(() => {

        async function fetchPaper() {

            try {

                const response = await getCurrentPaper();

                setCurrentPaper(response.filename);

            } catch (err) {

                console.error(err);

            }

        }

        fetchPaper();

    }, []);
 
    const navigate = useNavigate();

    return (

    <>

        <Navbar />

        <main className="workspace">

            <div className="workspace-header">

                <div className="header-text">

                    <h1>Research Paper Workspace</h1>

                    <p>

                        Interact with your uploaded paper using Azure AI.

                    </p>

                </div>


                <div className="current-paper-n-button">

                    <div className="current-paper">

                        <span className="paper-label">

                            Current Paper:

                        </span>

                        <span className="paper-name">

                            📄 {currentPaper || "No paper uploaded"}

                        </span>

                    </div>

                        
                    <button className="back-btn" onClick={() => navigate("/")}>

                        Upload Another Paper

                    </button>

                </div>

            </div>

            <AskCard />

            <div className="workspace-grid">

                <SummaryCard />

                <QuizCard />

            </div>

        </main>

        <Footer />

    </>

);

}
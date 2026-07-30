import "./AskCard.css";

import { useState } from "react";

import { askQuestion } from "../../services/api";

import { FaQuestionCircle } from "react-icons/fa";

export default function AskCard() {

    const [question, setQuestion] = useState("");

    const [answer, setAnswer] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleAsk() {

        if (!question.trim()) return;

        try {

            setLoading(true);

            const response = await askQuestion(question);

            setAnswer(response);

        }

        catch (error) {

            console.error(error);

            setAnswer("Something went wrong.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <section className="ask-card">

            <h2 className="card-title">
                
                <FaQuestionCircle className="card-icon"/>

                Ask Questions 

            </h2>

            <div className="ask-input-row">

                <input
                    type="text"
                    placeholder="Ask something about the uploaded paper..."
                    value={question}
                    onChange={(e) => setQuestion(e.target.value)}
                    onKeyDown={(e) => {
                        if (e.key === "Enter") {
                            handleAsk();
                        }
                    }}
                />

                <button onClick={handleAsk} disabled={loading}>

                    {loading ? "Thinking..." : "Ask"}

                </button>

            </div>

            

            {
            answer &&

            <div className="answer-box">

                <h3>Answer</h3>

                <div className="answer-content">
                    {answer}
                </div>

            </div>
            }

        </section>

    );

}
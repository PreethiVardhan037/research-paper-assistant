import "./SummaryCard.css";

import { useState } from "react";

import { getSummary } from "../../services/api";

import { FaRobot } from "react-icons/fa";

export default function SummaryCard() {

    const [summary, setSummary] = useState("");

    const [loading, setLoading] = useState(false);

    async function handleSummary() {

        try {

            setLoading(true);

            const response = await getSummary();

            setSummary(response);

        }

        catch (error) {

            console.error(error);

            setSummary("Failed to generate summary.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <section className="summary-card">

            <h2 className="card-title">

                <FaRobot className="card-icon"/>

                AI Summary

            </h2>

            <button

                onClick={handleSummary}

                disabled={loading}

            >

                {

                    loading

                        ? "Generating..."
                        : "Generate Summary"

                }

            </button>

            {

                summary &&

                <div className="summary-box">

                    {summary}

                </div>

            }

        </section>

    );

}
import "./QuizCard.css";

import { useState } from "react";

import { getQuiz } from "../../services/api";

import { FaClipboardList } from "react-icons/fa";

export default function QuizCard() {

    const [quiz, setQuiz] = useState([]);

    const [selectedAnswers, setSelectedAnswers] = useState({});

    const [submitted, setSubmitted] = useState(false);

    const [score, setScore] = useState(0);

    const [loading, setLoading] = useState(false);

    const [quizGenerated, setQuizGenerated] = useState(false)

    function handleOptionSelect(questionIndex, option){

        if(submitted) return;

        setSelectedAnswers(prev => ({

            ...prev,

            [questionIndex]: option

        }));

    }

    function handleSubmit(){

        let correct = 0;

        quiz.forEach((q,index)=>{

            if(selectedAnswers[index] === q.answer){

                correct++;

            }

        });

        setScore(correct);

        setSubmitted(true);

    }

    async function handleQuiz() {

        try {

            setLoading(true);

            setQuiz([]);

            setSelectedAnswers({});

            setSubmitted(false);

            setScore(0);


            const response = await getQuiz();

            setQuiz(response.questions);

            setQuizGenerated(true);

            setSelectedAnswers({});

            setSubmitted(false);

            setScore(0);

            console.log(response.questions);

        }

        catch (error) {

            console.error(error);

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <section className="quiz-card">

            <h2 className="card-title">

                <FaClipboardList className="card-icon"/>

                Quiz

            </h2>

            <button onClick={handleQuiz} disabled={loading}>

                {
                    
                    loading ? "Generating..." : quizGenerated ? "Regenerate Quiz" : "Generate Quiz"

                }

            </button>

            {

                quiz.length > 0 &&

                quiz.map((q, index) => (

                    <div key={index} className="question">

                        <h4>

                            {index + 1}. {q.question}

                        </h4>

                        {

                            q.options.map((option, i) => (

                                <button

                                    key={i}

                                    className={

                                        `option-btn

                                        ${selectedAnswers[index] === option ? "selected" : ""}

                                        ${submitted && option === q.answer ? "correct" : ""}

                                        ${submitted &&
                                        selectedAnswers[index] === option &&
                                        option !== q.answer
                                        ? "wrong"
                                        : ""}`

                                    }

                                    onClick={() => handleOptionSelect(index, option)}

                                >

                                    {option}

                                </button>



                            ))

                        }

                    </div>

                ))

            }

            {
                quiz.length > 0 && !submitted &&

                <button className="submit-btn" onClick={handleSubmit}>

                    Submit Quiz

                </button>

            }

            {

                submitted &&

                <h3>

                    Your Score: {score} / {quiz.length}

                </h3>

            }

        </section>

    );

}
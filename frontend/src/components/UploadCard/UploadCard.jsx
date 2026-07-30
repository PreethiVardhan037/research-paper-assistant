import "./UploadCard.css";
import { FaCloudUploadAlt } from "react-icons/fa";
import { useRef, useState } from "react";
import { uploadPaper } from "../../services/api";
import { useNavigate } from "react-router-dom";



export default function UploadCard() {

    const inputRef = useRef(null);

    const [file, setFile] = useState(null);

    const [loading, setLoading] = useState(false);

    const [message, setMessage] = useState("");

    const navigate = useNavigate();

    function handleFileSelect(event) {

        if (!event.target.files.length) return;

        setFile(event.target.files[0]);

        setMessage("");

    }

    function handleDrop(event) {

        event.preventDefault();

        if (!event.dataTransfer.files.length) return;

        const droppedFile = event.dataTransfer.files[0];

        if (droppedFile.type !== "application/pdf") {

            setMessage("Please upload a PDF file.");

            return;

        }

        setFile(droppedFile);

        setMessage("");

    }

    function handleDragOver(event) {

        event.preventDefault();

    }

    async function handleUpload() {

        if (!file) return;

        try {

            setLoading(true);

            setMessage("");

            await uploadPaper(file);

            setMessage("Paper uploaded successfully!");

            setTimeout(() => {
                navigate("/workspace");
            }, 1000);
        
        }

        catch (error) {

            console.error(error);

            setMessage("Upload failed.");

        }

        finally {

            setLoading(false);

        }

    }

    return (

        <section className="upload-card">

            <h1>

                Understand Research Papers Faster

            </h1>

            <p>

                Upload any research paper and let Azure AI summarize,
                explain concepts, answer questions, and generate quizzes.

            </p>

            <div

                className="upload-box"

                onDrop={handleDrop}

                onDragOver={handleDragOver}

                onClick={() => inputRef.current.click()}

            >

                <FaCloudUploadAlt className="upload-icon"/>

                <h2>Drag & Drop PDF Here</h2>

                <span>or click to browse</span>

                <input

                    ref={inputRef}

                    hidden

                    type="file"

                    accept=".pdf"

                    onChange={handleFileSelect}

                />

            </div>

            {

                file &&

                <div className="selected-file">

                    📄 {file.name}

                </div>

            }

            <button

                className="upload-btn"

                disabled={!file || loading}

                onClick={handleUpload}

            >

                {

                    loading

                    ?

                    "Uploading..."

                    :

                    "Upload Paper"

                }

            </button>

            {

                message &&

                <p className="upload-message">

                    {message}

                </p>

            }

        </section>

    );

}
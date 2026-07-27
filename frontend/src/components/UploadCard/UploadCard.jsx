import "./UploadCard.css";
import { FaCloudUploadAlt } from "react-icons/fa";

export default function UploadCard(){

    return(

        <section className="upload-card">

            <h1>
                Understand Research Papers Faster
            </h1>

            <p>

                Upload any research paper and let Azure AI summarize,
                explain concepts, answer questions, and generate quizzes.

            </p>

            <label className="upload-box">

                <FaCloudUploadAlt className="upload-icon"/>

                <h2>Drag & Drop PDF Here</h2>

                <span>or click to browse</span>

                <input
                    type="file"
                    accept=".pdf"
                    hidden
                />

            </label>

        </section>

    );

}
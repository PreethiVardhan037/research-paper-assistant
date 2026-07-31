import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.MODE === "development"
        ? "http://localhost:7071/api"
        : "/api",
});

export default api;

export async function uploadPaper(file){

    const formData = new FormData();

    formData.append("file", file);

    const response = await api.post(

        "/upload",

        formData,

        {

            headers:{

                "Content-Type":"multipart/form-data"

            }

        }

    );

    return response.data;

}

export async function askQuestion(question) {

    const response = await api.post(
        "/ask",
        {
            question
        }
    );

    return response.data;
}

export async function getSummary() {

    const response = await api.post(
        "/summary",
        {}
    );

    return response.data;
}

export async function getQuiz() {

    const response = await api.post(
        "/quiz",
        {}
    );

    return response.data;
}

export async function getCurrentPaper() {

    const response = await api.get(
        "/current-paper"
    );

    return response.data;
}
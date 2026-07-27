import axios from "axios";

const api = axios.create({
    baseURL: "http://localhost:7071/api",
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